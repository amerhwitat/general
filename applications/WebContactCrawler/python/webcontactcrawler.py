#!/usr/bin/env python3
"""Reference WebContactCrawler implementation.

Public-web, bounded, robots-aware crawler. No authentication bypass or SMTP probing.
"""
from __future__ import annotations
import argparse, csv, re, sys, time
from collections import deque
from dataclasses import dataclass, asdict
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
from urllib.request import Request, urlopen

EMAIL = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
OBF = re.compile(r"([A-Z0-9._%+-]+)\s*(?:\[at\]|\(at\)| at )\s*([A-Z0-9.-]+)\s*(?:\[dot\]|\(dot\)| dot |\.)\s*([A-Z]{2,})", re.I)

@dataclass
class Contact:
    email: str
    source_url: str
    domain: str
    title: str = ""
    keywords: tuple[str, ...] = ()
    method: str = "regex"
    discovered_at: float = 0.0

class Crawler:
    def __init__(self, seeds, keywords=(), max_pages=100, max_depth=2, delay=0.5, timeout=10):
        self.queue = deque((u, 0) for u in seeds); self.seen=set(); self.contacts={}
        self.keywords=tuple(k.lower() for k in keywords); self.max_pages=max_pages
        self.max_depth=max_depth; self.delay=delay; self.timeout=timeout; self.pages=0
        self.robots={}
    def allowed(self, url):
        p=urlparse(url); root=f"{p.scheme}://{p.netloc}"
        if root not in self.robots:
            rp=RobotFileParser(root+"/robots.txt")
            try: rp.read()
            except Exception: rp.parse([])
            self.robots[root]=rp
        return self.robots[root].can_fetch("WebContactCrawler/1.0", url)
    def fetch(self, url):
        req=Request(url, headers={"User-Agent":"WebContactCrawler/1.0 (+responsible-crawler)"})
        with urlopen(req, timeout=self.timeout) as r:
            ctype=r.headers.get("Content-Type", "")
            if "text/html" not in ctype: return "", r.geturl()
            return r.read(2_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace"), r.geturl()
    def run(self):
        while self.queue and self.pages < self.max_pages:
            url, depth=self.queue.popleft()
            if url in self.seen or depth>self.max_depth: continue
            self.seen.add(url)
            if not self.allowed(url): continue
            try: html, final=self.fetch(url)
            except Exception as e:
                print(f"ERROR {url}: {e}", file=sys.stderr); continue
            self.pages += 1
            text=re.sub(r"<[^>]+>", " ", html)
            title=(re.search(r"<title[^>]*>(.*?)</title>", html, re.I|re.S) or ["",""])[1].strip()
            hits=set(EMAIL.findall(html))
            for a,b,c in OBF.findall(text): hits.add(f"{a}@{b}.{c}")
            matched=tuple(k for k in self.keywords if k in (title+" "+text).lower())
            for email in hits:
                key=email.lower()
                self.contacts[key]=Contact(email=email,source_url=final,domain=urlparse(final).netloc,title=title,keywords=matched,discovered_at=time.time())
            if depth < self.max_depth:
                for href in re.findall(r'href=["\']([^"\']+)', html, re.I):
                    nxt=urljoin(final, href).split('#')[0]
                    if urlparse(nxt).scheme in ("http","https") and urlparse(nxt).netloc==urlparse(final).netloc:
                        self.queue.append((nxt, depth+1))
            print(f"PROGRESS pages={self.pages} queued={len(self.queue)} emails={len(self.contacts)} url={final}")
            time.sleep(self.delay)
        return list(self.contacts.values())

def write_txt(rows, path):
    with open(path,"w",encoding="utf-8") as f:
        for r in rows: f.write(r.email+"\n")
def write_csv(rows, path):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(asdict(rows[0]).keys()) if rows else ["email"]); w.writeheader()
        for r in rows: w.writerow(asdict(r))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("urls",nargs="+"); ap.add_argument("-k","--keyword",action="append",default=[]); ap.add_argument("-o","--output",default="emails.csv"); ap.add_argument("--max-pages",type=int,default=100); ap.add_argument("--max-depth",type=int,default=2); ap.add_argument("--delay",type=float,default=.5)
    a=ap.parse_args(); rows=Crawler(a.urls,a.keyword,a.max_pages,a.max_depth,a.delay).run()
    write_txt(rows,a.output) if a.output.endswith(".txt") else write_csv(rows,a.output)
    print(f"DONE pages={len(rows)} unique_emails={len(rows)} output={a.output}")
if __name__=="__main__": main()
