from __future__ import annotations
import argparse
from pathlib import Path
from .core import CrawlConfig, SeoCrawler

def main():
    p=argparse.ArgumentParser(description='SEO-Tool authorized website crawler')
    p.add_argument('--url',required=True)
    p.add_argument('--output',default='./seo-results')
    p.add_argument('--max-pages',type=int,default=250)
    p.add_argument('--max-depth',type=int,default=8)
    p.add_argument('--workers',type=int,default=4)
    p.add_argument('--delay',type=float,default=.5)
    p.add_argument('--no-robots',action='store_true')
    p.add_argument('--allow-onion',action='store_true')
    p.add_argument('--capture-raw',action='store_true')
    a=p.parse_args()
    c=CrawlConfig(seed=a.url,output=Path(a.output),max_pages=a.max_pages,max_depth=a.max_depth,workers=a.workers,delay=a.delay,obey_robots=not a.no_robots,allow_onion=a.allow_onion,capture_raw=a.capture_raw)
    pages,issues=SeoCrawler(c).crawl()
    print(f'completed: pages={len(pages)} issues={len(issues)} output={c.output.resolve()}')

if __name__=='__main__': main()
