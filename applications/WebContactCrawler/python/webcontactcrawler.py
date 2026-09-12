#!/usr/bin/env python3
"""Bounded public-web contact crawler.

Responsible-use boundary: crawl only public/authorized resources; no auth/CAPTCHA
bypass, anti-bot evasion, credential collection, private-area crawling or SMTP probing.
"""
import argparse, csv, json, re, sys, time
from collections import deque
from dataclasses import dataclass, asdict
from html import unescape
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

EMAIL = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,63}", re.I)
OBF = re.compile(r"([A-Z0-9._%+-]+)\s*(?:\[at\]|\(at\)|\bat\b)\s*([A-Z0-9.-]+)\s*(?:\[dot\]|\(dot\)|\bdot\b)\s*([A-Z]{2,63})", re.I)
LINK = re.compile(r'''href\s*=\s*["']([^"']+)["']''', re.I)
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)

@dataclass
class Contact:
    email: str
    source_url: str
    domain: str
    title: str = ""
    keywords: tuple = ()
    score: int = 0
    method: str = "regex"
    discovered_at: float = 0.0

class Crawler:
    def __init__(self, seeds, keywords=(), max_pages=100, max_depth=2, delay=.5,
                 timeout=10, max_bytes=2_000_000, allowed_domains=None, event_file=None):
        self.queue = deque((u, 0) for u in seeds)
        self.seen, self.contacts, self.robots = set(), {}, {}
        self.keywords = tuple(k.lower().strip() for k in keywords if k.strip())
        self.max_pages, self.max_depth, self.delay = max(1, max_pages), max(0, max_depth), max(0, delay)
        self.timeout, self.max_bytes = timeout, max_bytes
        self.allowed_domains = set(allowed_domains or [urlparse(u).netloc for u in seeds])
        self.event_file = event_file
        self.pages = self.errors = 0
        self.started = time.time()

    def event(self, kind, **data):
        payload = {"ts": time.time(), "event": kind, "pages": self.pages,
                   "queued": len(self.queue), "emails": len(self.contacts),
                   "errors": self.errors, **data}
        print("PROGRESS " + json.dumps(payload, ensure_ascii=False), flush=True)
        if self.event_file:
            with open(self.event_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(payload, ensure_ascii=False) + "\n")

    def allowed(self, url):
        p = urlparse(url)
        if p.scheme not in ("http", "https") or p.netloc not in self.allowed_domains:
            return False
        root = f"{p.scheme}://{p.netloc}"
        if root not in self.robots:
            rp = RobotFileParser(root + "/robots.txt")
            try: rp.read()
            except Exception: rp.parse([])
            self.robots[root] = rp
        return self.robots[root].can_fetch("WebContactCrawler/1.0", url)

    def fetch(self, url):
        req = Request(url, headers={"User-Agent": "WebContactCrawler/1.0 (+responsible-crawler)", "Accept": "text/html,application/xhtml+xml"})
        with urlopen(req, timeout=self.timeout) as r:
            ctype = r.headers.get("Content-Type", "")
            if "text/html" not in ctype and "application/xhtml+xml" not in ctype:
                return "", r.geturl()
            raw = r.read(self.max_bytes)
            return raw.decode(r.headers.get_content_charset() or "utf-8", "replace"), r.geturl()

    def run(self):
        self.event("start", seeds=list(self.queue), keywords=list(self.keywords))
        while self.queue and self.pages < self.max_pages:
            url, depth = self.queue.popleft()
            if url in self.seen or depth > self.max_depth: continue
            self.seen.add(url)
            if not self.allowed(url):
                self.event("skip", url=url, reason="scope-or-robots")
                continue
            self.event("fetch", url=url, depth=depth)
            try: html, final = self.fetch(url)
            except Exception as exc:
                self.errors += 1; self.event("error", url=url, error=str(exc)); continue
            self.pages += 1
            text = unescape(re.sub(r"<[^>]+>", " ", html))
            title_m = TITLE.search(html)
            title = re.sub(r"\s+", " ", unescape(title_m.group(1))).strip() if title_m else ""
            haystack = (title + " " + text).lower()
            matched = tuple(k for k in self.keywords if k in haystack)
            score = len(matched)
            hits = set(EMAIL.findall(html))
            hits.update(f"{a}@{b}.{c}" for a, b, c in OBF.findall(text))
            for email in hits:
                email = email.lower().strip()
                self.contacts[email] = Contact(email, final, urlparse(final).netloc, title, matched, score, "regex/obfuscated", time.time())
            if depth < self.max_depth:
                for href in LINK.findall(html):
                    nxt = urljoin(final, href).split("#")[0]
                    if urlparse(nxt).netloc == urlparse(final).netloc and nxt not in self.seen:
                        self.queue.append((nxt, depth + 1))
            rate = self.pages / max(time.time() - self.started, .001)
            self.event("page", url=final, depth=depth, matched_keywords=list(matched), rate=round(rate, 3))
            time.sleep(self.delay)
        self.event("done", elapsed=round(time.time() - self.started, 3))
        return sorted(self.contacts.values(), key=lambda r: (-r.score, r.email))

def import_txt(path):
    with open(path, encoding="utf-8") as f: return sorted({x.strip().lower() for x in f if x.strip()})

def import_csv(path, column="email"):
    with open(path, newline="", encoding="utf-8") as f:
        return sorted({r.get(column, "").strip().lower() for r in csv.DictReader(f) if r.get(column, "").strip()})

def export(rows, path):
    if path.lower().endswith(".txt"):
        with open(path, "w", encoding="utf-8") as f: f.write("\n".join(sorted({r.email.lower() for r in rows})) + "\n")
    elif path.lower().endswith(".csv"):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["email","source_url","domain","title","keywords","score","method","discovered_at"]); w.writeheader()
            for r in rows:
                d = asdict(r); d["keywords"] = ";".join(r.keywords); w.writerow(d)
    else: raise ValueError("output must end in .txt or .csv")

def main():
    ap = argparse.ArgumentParser(description="Bounded public-web email/contact crawler")
    ap.add_argument("urls", nargs="+", help="public/authorized seed URLs")
    ap.add_argument("-k", "--keyword", action="append", default=[])
    ap.add_argument("-o", "--output", default="emails.csv")
    ap.add_argument("--max-pages", type=int, default=100); ap.add_argument("--max-depth", type=int, default=2)
    ap.add_argument("--delay", type=float, default=.5); ap.add_argument("--timeout", type=float, default=10)
    ap.add_argument("--max-bytes", type=int, default=2_000_000); ap.add_argument("--events", help="JSONL progress event file")
    a = ap.parse_args()
    rows = Crawler(a.urls, a.keyword, a.max_pages, a.max_depth, a.delay, a.timeout, a.max_bytes, event_file=a.events).run()
    export(rows, a.output); print(f"DONE pages={len(rows)} unique_emails={len(rows)} output={a.output}")

if __name__ == "__main__": main()
