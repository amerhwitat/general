from __future__ import annotations
import asyncio, csv, re
from collections import deque
from dataclasses import dataclass, asdict
from urllib.parse import urljoin, urlparse, quote_plus
import httpx
from bs4 import BeautifulSoup

EMAIL_RE = re.compile(r"[A-Z0-9._%+-]+\s*(?:@|\[at\]|\(at\))\s*[A-Z0-9.-]+\s*(?:\.|\[dot\]|\(dot\))\s*[A-Z]{2,}", re.I)

@dataclass(frozen=True)
class EmailRecord:
    email: str
    source_url: str
    keywords: str
    title: str = ""

class EmailCrawler:
    def __init__(self, keywords, depth=2, concurrency=8, delay=0.25, timeout=15, same_domain=True):
        self.keywords = [k.lower() for k in keywords if k.strip()]
        self.depth, self.concurrency, self.delay, self.timeout = depth, concurrency, delay, timeout
        self.same_domain = same_domain
        self.visited, self.records, self.progress = set(), {}, asyncio.Queue()
        self._robots = {}

    async def _allowed(self, client, url):
        # Conservative robots handling: fetch robots.txt and cache disallowed paths.
        p = urlparse(url); root = f"{p.scheme}://{p.netloc}"
        if root not in self._robots:
            try:
                r = await client.get(root + "/robots.txt", timeout=self.timeout)
                rules = [line.split(":",1)[1].strip() for line in r.text.splitlines() if line.lower().startswith("disallow:")]
                self._robots[root] = rules
            except Exception:
                self._robots[root] = []
        return not any(p.path.startswith(x) for x in self._robots[root] if x)

    def _normalize_email(self, raw):
        e = re.sub(r"\s+", "", raw.lower()).replace("[at]", "@").replace("(at)", "@").replace("[dot]", ".").replace("(dot)", ".")
        return e.strip(".,;:<>\"'")

    async def crawl(self, seeds):
        queue = deque((u, 0) for u in seeds)
        async with httpx.AsyncClient(follow_redirects=True, headers={"User-Agent":"EmailKeywordCrawler/1.0 (public-web research)"}) as client:
            while queue:
                batch = []
                while queue and len(batch) < self.concurrency:
                    url, depth = queue.popleft()
                    if url in self.visited or depth > self.depth: continue
                    self.visited.add(url); batch.append((url, depth))
                if not batch: break
                await self.progress.put({"event":"batch","queued":len(queue),"visited":len(self.visited),"emails":len(self.records)})
                results = await asyncio.gather(*(self._fetch(client,u,d) for u,d in batch), return_exceptions=True)
                for (url, depth), result in zip(batch, results):
                    if isinstance(result, Exception):
                        await self.progress.put({"event":"error","url":url,"error":str(result)}); continue
                    text, links, title = result
                    hits = [k for k in self.keywords if k in text.lower()]
                    for raw in EMAIL_RE.findall(text):
                        email = self._normalize_email(raw)
                        if hits and email:
                            self.records.setdefault(email, EmailRecord(email,url,",".join(hits),title))
                    await self.progress.put({"event":"page","url":url,"depth":depth,"keywords":hits,"emails":len(self.records)})
                    if depth < self.depth:
                        base = urlparse(url).netloc
                        for link in links:
                            if link.startswith(("http://","https://")) and (not self.same_domain or urlparse(link).netloc == base):
                                if link not in self.visited: queue.append((link,depth+1))
                await asyncio.sleep(self.delay)
        await self.progress.put({"event":"done","visited":len(self.visited),"emails":len(self.records)})
        return list(self.records.values())

    async def _fetch(self, client, url, depth):
        if not await self._allowed(client,url):
            return "", [], ""
        r = await client.get(url, timeout=self.timeout)
        r.raise_for_status()
        if "text/html" not in r.headers.get("content-type", ""): return "", [], ""
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script","style","noscript"]): tag.decompose()
        for a in soup.select('a[href^="mailto:"]'):
            soup.append(soup.new_string(" " + a.get("href","")[7:]))
        return soup.get_text(" ", strip=True), [urljoin(url,a.get("href")) for a in soup.select("a[href]")], soup.title.get_text(strip=True) if soup.title else ""

async def search_urls(endpoint, query, limit=20):
    if not endpoint: return []
    async with httpx.AsyncClient() as c:
        r = await c.get(endpoint, params={"q":query,"format":"json"}, timeout=20); r.raise_for_status()
        data = r.json(); return [x.get("url") for x in data.get("results",[])[:limit] if x.get("url")]

def import_seeds(path):
    with open(path, encoding="utf-8", errors="ignore") as f: return [x.strip() for x in f if x.strip()]

def export_records(records, txt=None, csv_path=None):
    if txt:
        with open(txt,"w",encoding="utf-8") as f: f.write("\n".join(r.email for r in records)+"\n")
    if csv_path:
        with open(csv_path,"w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=["email","source_url","keywords","title"]); w.writeheader(); w.writerows(asdict(r) for r in records)
