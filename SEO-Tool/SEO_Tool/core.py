from __future__ import annotations

import csv, hashlib, json, os, re, sqlite3, time
from collections import deque
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

@dataclass
class CrawlConfig:
    seed: str
    output: Path
    max_pages: int = 250
    max_depth: int = 8
    workers: int = 4
    delay: float = 0.5
    timeout: float = 15.0
    obey_robots: bool = True
    capture_documents: bool = True
    capture_raw: bool = False
    allow_onion: bool = False
    tor_proxy: str = "socks5h://127.0.0.1:9050"
    max_download_bytes: int = 8_000_000

@dataclass
class Page:
    url: str
    status: int
    final_url: str
    depth: int
    content_type: str
    title: str = ""
    description: str = ""
    h1_count: int = 0
    word_count: int = 0
    canonical: str = ""
    noindex: bool = False
    nofollow: bool = False
    lang: str = ""
    viewport: bool = False
    hreflang_count: int = 0
    jsonld_count: int = 0
    og_count: int = 0
    image_count: int = 0
    missing_alt: int = 0
    response_ms: float = 0.0
    size_bytes: int = 0

@dataclass
class Link:
    source: str
    target: str
    anchor: str
    internal: bool
    status: int | None = None

@dataclass
class Issue:
    url: str
    severity: str
    code: str
    message: str

class SeoCrawler:
    def __init__(self, config: CrawlConfig):
        self.config = config
        self.session = requests.Session()
        self.pages: list[Page] = []
        self.links: list[Link] = []
        self.issues: list[Issue] = []
        self.visited: set[str] = set()
        self.robot_cache: dict[str, RobotFileParser | None] = {}
        self.output = Path(config.output).expanduser().resolve()
        self.output.mkdir(parents=True, exist_ok=True)
        self.doc_dir = self.output / "documents"
        self.raw_dir = self.output / "raw"
        if config.capture_documents: self.doc_dir.mkdir(exist_ok=True)
        if config.capture_raw: self.raw_dir.mkdir(exist_ok=True)
        self._db = sqlite3.connect(self.output / "crawl.sqlite3")
        self._db.execute("CREATE TABLE IF NOT EXISTS pages (url TEXT PRIMARY KEY, data TEXT NOT NULL)")
        self._db.commit()

    def _allowed(self, url: str) -> bool:
        p = urlparse(url)
        if p.scheme not in {"http", "https"} or p.username or p.password or not p.hostname:
            return False
        host = p.hostname.lower()
        if host.endswith(".onion"):
            return self.config.allow_onion
        return True

    def _get(self, url: str):
        proxies = None
        if urlparse(url).hostname and urlparse(url).hostname.lower().endswith('.onion'):
            if not self.config.allow_onion: raise PermissionError("onion crawling is disabled")
            proxies = {"http": self.config.tor_proxy, "https": self.config.tor_proxy}
        return self.session.get(url, timeout=self.config.timeout, allow_redirects=True,
                                headers={"User-Agent": "SEO-Tool/0.1 (+authorized-audit)"}, proxies=proxies, stream=True)

    def _robots_ok(self, url: str) -> bool:
        if not self.config.obey_robots: return True
        p = urlparse(url)
        if p.hostname and p.hostname.lower().endswith('.onion'): return True
        base = f"{p.scheme}://{p.netloc}"
        if base not in self.robot_cache:
            rp = RobotFileParser()
            rp.set_url(base + "/robots.txt")
            try: rp.read(); self.robot_cache[base] = rp
            except Exception: self.robot_cache[base] = None
        rp = self.robot_cache[base]
        return True if rp is None else rp.can_fetch("SEO-Tool", url)

    def _normalize(self, url: str, base: str) -> str | None:
        absolute = urldefrag(urljoin(base, url))[0]
        p = urlparse(absolute)
        if p.scheme not in {"http", "https"} or not p.hostname: return None
        return absolute

    def _issue(self, url, severity, code, message):
        self.issues.append(Issue(url, severity, code, message))

    def _analyze(self, url: str, response, depth: int) -> tuple[Page, list[str]]:
        started = time.perf_counter()
        content_type = response.headers.get("content-type", "").lower()
        body = response.content[:self.config.max_download_bytes]
        final = response.url
        page = Page(url=url, status=response.status_code, final_url=final, depth=depth,
                    content_type=content_type, response_ms=(time.perf_counter()-started)*1000,
                    size_bytes=len(body))
        if response.status_code >= 400:
            self._issue(url, "error", "http", f"HTTP {response.status_code}")
            return page, []
        if "text/html" not in content_type and "application/xhtml" not in content_type:
            if self.config.capture_documents:
                name = hashlib.sha256(final.encode()).hexdigest()[:16]
                ext = ".bin"
                if "pdf" in content_type: ext = ".pdf"
                path = self.doc_dir / f"{name}{ext}"
                path.write_bytes(body)
            return page, []
        text = body.decode(response.encoding or "utf-8", errors="replace")
        soup = BeautifulSoup(text, "html.parser")
        page.title = soup.title.get_text(" ", strip=True) if soup.title else ""
        desc = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
        page.description = desc.get("content", "").strip() if desc else ""
        page.h1_count = len(soup.find_all("h1"))
        page.word_count = len(re.findall(r"\b\w+\b", soup.get_text(" ", strip=True)))
        can = soup.find("link", rel=lambda x: x and "canonical" in x)
        page.canonical = can.get("href", "") if can else ""
        robots = soup.find("meta", attrs={"name": re.compile("^robots$", re.I)})
        rv = robots.get("content", "").lower() if robots else ""
        page.noindex, page.nofollow = "noindex" in rv, "nofollow" in rv
        page.lang = soup.html.get("lang", "") if soup.html else ""
        page.viewport = bool(soup.find("meta", attrs={"name": re.compile("^viewport$", re.I)}))
        page.hreflang_count = len(soup.find_all("link", attrs={"hreflang": True}))
        page.jsonld_count = len(soup.find_all("script", attrs={"type": re.compile("ld\\+json", re.I)}))
        page.og_count = len(soup.find_all("meta", property=re.compile("^og:", re.I)))
        imgs = soup.find_all("img"); page.image_count = len(imgs)
        page.missing_alt = sum(1 for x in imgs if x.get("alt") is None)
        targets=[]
        for a in soup.find_all("a", href=True):
            target=self._normalize(a["href"], final)
            if not target: continue
            internal=urlparse(target).netloc.lower()==urlparse(final).netloc.lower()
            self.links.append(Link(final,target,a.get_text(" ",strip=True)[:200],internal))
            if internal: targets.append(target)
        if not page.title: self._issue(final,"error","missing-title","Missing title")
        elif len(page.title)>60: self._issue(final,"warning","long-title","Title exceeds typical SERP width")
        if not page.description: self._issue(final,"warning","missing-description","Missing meta description")
        if page.h1_count==0: self._issue(final,"warning","missing-h1","Missing H1")
        if page.h1_count>1: self._issue(final,"warning","multiple-h1","Multiple H1 elements")
        if page.missing_alt: self._issue(final,"warning","image-alt","Images missing alt attributes")
        if page.noindex: self._issue(final,"info","noindex","Page is marked noindex")
        if final.startswith("http://"): self._issue(final,"warning","insecure-http","Page is served over HTTP")
        if page.word_count<200: self._issue(final,"info","thin-content","Low extracted word count")
        return page, targets

    def crawl(self):
        if not self._allowed(self.config.seed): raise ValueError("seed must be an allowed HTTP/HTTPS URL")
        q=deque([(self.config.seed,0)])
        while q and len(self.visited)<self.config.max_pages:
            url,depth=q.popleft()
            if url in self.visited or depth>self.config.max_depth or not self._allowed(url) or not self._robots_ok(url): continue
            self.visited.add(url)
            try:
                response=self._get(url)
                page,children=self._analyze(url,response,depth)
                self.pages.append(page)
                self._db.execute("INSERT OR REPLACE INTO pages(url,data) VALUES(?,?)",(page.url,json.dumps(asdict(page))))
                self._db.commit()
                if self.config.capture_raw and "text/html" in response.headers.get("content-type",""):
                    (self.raw_dir/(hashlib.sha256(page.final_url.encode()).hexdigest()+".html")).write_bytes(response.content[:self.config.max_download_bytes])
                for child in children:
                    if child not in self.visited: q.append((child,depth+1))
                time.sleep(max(0,self.config.delay))
            except Exception as exc:
                self._issue(url,"error","fetch",str(exc)[:300])
        self._postprocess(); self.export()
        return self.pages, self.issues

    def _postprocess(self):
        titles={}
        for p in self.pages:
            titles.setdefault(p.title.strip().casefold(),[]).append(p.url)
        for title, urls in titles.items():
            if title and len(urls)>1:
                for u in urls: self._issue(u,"warning","duplicate-title",f"Duplicate title across {len(urls)} pages")
        internal=[x for x in self.links if x.internal]
        inbound={x.target for x in internal}
        for p in self.pages:
            if p.url!=self.config.seed and p.url not in inbound: self._issue(p.url,"warning","orphan","No discovered internal inbound link")

    def export(self):
        data={"config":asdict(self.config)|{"output":str(self.output)},"pages":[asdict(x) for x in self.pages],"links":[asdict(x) for x in self.links],"issues":[asdict(x) for x in self.issues]}
        (self.output/"report.json").write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
        with (self.output/"pages.csv").open("w",newline="",encoding="utf-8") as f:
            rows=[asdict(x) for x in self.pages]; w=csv.DictWriter(f,fieldnames=list(asdict(self.pages[0]).keys()) if rows else ["url"]); w.writeheader(); w.writerows(rows)
        with (self.output/"issues.csv").open("w",newline="",encoding="utf-8") as f:
            rows=[asdict(x) for x in self.issues]; w=csv.DictWriter(f,fieldnames=["url","severity","code","message"]); w.writeheader(); w.writerows(rows)
        summary=f"# SEO-Tool report\n\nPages: {len(self.pages)}\nIssues: {len(self.issues)}\nLinks: {len(self.links)}\n\n"
        summary += "\n".join(f"- **{i.severity}** `{i.code}` — {i.url}: {i.message}" for i in self.issues[:200])
        (self.output/"summary.md").write_text(summary,encoding="utf-8")
        (self.output/"site-graph.json").write_text(json.dumps([asdict(x) for x in self.links],ensure_ascii=False,indent=2),encoding="utf-8")
