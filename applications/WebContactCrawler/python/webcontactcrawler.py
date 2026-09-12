#!/usr/bin/env python3
"""Reference WebContactCrawler: bounded, public-web, robots-aware crawling."""
import argparse,csv,re,sys,time
from collections import deque
from dataclasses import dataclass,asdict
from urllib.parse import urljoin,urlparse
from urllib.robotparser import RobotFileParser
from urllib.request import Request,urlopen
EMAIL=re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}",re.I)
OBF=re.compile(r"([A-Z0-9._%+-]+)\s*(?:\[at\]|\(at\)| at )\s*([A-Z0-9.-]+)\s*(?:\[dot\]|\(dot\)| dot |\.)\s*([A-Z]{2,})",re.I)
@dataclass
class Contact:
    email:str; source_url:str; domain:str; title:str=""; keywords:tuple=(); method:str="regex"; discovered_at:float=0.0
class Crawler:
    def __init__(self,seeds,keywords=(),max_pages=100,max_depth=2,delay=.5,timeout=10):
        self.queue=deque((u,0) for u in seeds);self.seen=set();self.contacts={};self.keywords=tuple(k.lower() for k in keywords);self.max_pages=max_pages;self.max_depth=max_depth;self.delay=delay;self.timeout=timeout;self.pages=0;self.errors=0;self.robots={}
    def allowed(self,url):
        p=urlparse(url);root=f"{p.scheme}://{p.netloc}"
        if root not in self.robots:
            rp=RobotFileParser(root+"/robots.txt")
            try:rp.read()
            except Exception:rp.parse([])
            self.robots[root]=rp
        return self.robots[root].can_fetch("WebContactCrawler/1.0",url)
    def fetch(self,url):
        req=Request(url,headers={"User-Agent":"WebContactCrawler/1.0 (+responsible-crawler)"})
        with urlopen(req,timeout=self.timeout) as r:
            if "text/html" not in r.headers.get("Content-Type",""):return "",r.geturl()
            return r.read(2_000_000).decode(r.headers.get_content_charset() or "utf-8","replace"),r.geturl()
    def run(self):
        started=time.time()
        while self.queue and self.pages<self.max_pages:
            url,depth=self.queue.popleft()
            if url in self.seen or depth>self.max_depth:continue
            self.seen.add(url)
            if not self.allowed(url):continue
            try:html,final=self.fetch(url)
            except Exception as e:self.errors+=1;print(f"ERROR {url}: {e}",file=sys.stderr);continue
            self.pages+=1;text=re.sub(r"<[^>]+>"," ",html);m=re.search(r"<title[^>]*>(.*?)</title>",html,re.I|re.S);title=m.group(1).strip() if m else "";hits=set(EMAIL.findall(html));hits.update(f"{a}@{b}.{c}" for a,b,c in OBF.findall(text));matched=tuple(k for k in self.keywords if k in (title+" "+text).lower())
            for email in hits:self.contacts[email.lower()]=Contact(email=email,source_url=final,domain=urlparse(final).netloc,title=title,keywords=matched,discovered_at=time.time())
            if depth<self.max_depth:
                for href in re.findall(r'href=["\']([^"\']+)',html,re.I):
                    nxt=urljoin(final,href).split('#')[0]
                    if urlparse(nxt).scheme in ("http","https") and urlparse(nxt).netloc==urlparse(final).netloc:self.queue.append((nxt,depth+1))
            rate=self.pages/max(time.time()-started,.001);print(f"PROGRESS pages={self.pages} queued={len(self.queue)} emails={len(self.contacts)} errors={self.errors} rate={rate:.2f}/s url={final}");time.sleep(self.delay)
        return list(self.contacts.values())
def write_txt(rows,path):
    with open(path,"w",encoding="utf-8") as f:f.write("\n".join(sorted({r.email.lower() for r in rows}))+"\n")
def write_csv(rows,path):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["email","source_url","domain","title","keywords","method","discovered_at"]);w.writeheader()
        for r in rows:
            d=asdict(r);d["keywords"]=";".join(r.keywords);w.writerow(d)
def main():
    ap=argparse.ArgumentParser();ap.add_argument("urls",nargs="+");ap.add_argument("-k","--keyword",action="append",default=[]);ap.add_argument("-o","--output",default="emails.csv");ap.add_argument("--max-pages",type=int,default=100);ap.add_argument("--max-depth",type=int,default=2);ap.add_argument("--delay",type=float,default=.5);a=ap.parse_args();rows=Crawler(a.urls,a.keyword,a.max_pages,a.max_depth,a.delay).run();write_txt(rows,a.output) if a.output.endswith(".txt") else write_csv(rows,a.output);print(f"DONE pages={len(rows)} unique_emails={len(rows)} output={a.output}")
if __name__=="__main__":main()
