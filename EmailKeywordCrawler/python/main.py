import argparse, asyncio
from crawler import EmailCrawler, import_seeds, export_records, search_urls

async def main():
    p=argparse.ArgumentParser(description='Keyword-driven public-web email crawler')
    p.add_argument('--url',action='append',default=[]); p.add_argument('--import-file'); p.add_argument('--keyword',action='append',default=[])
    p.add_argument('--query',action='append',default=[]); p.add_argument('--search-endpoint'); p.add_argument('--depth',type=int,default=2)
    p.add_argument('--concurrency',type=int,default=8); p.add_argument('--delay',type=float,default=.25); p.add_argument('--export-txt'); p.add_argument('--export-csv')
    a=p.parse_args(); seeds=list(a.url)
    if a.import_file: seeds += import_seeds(a.import_file)
    for q in a.query: seeds += await search_urls(a.search_endpoint,q)
    seeds=list(dict.fromkeys(seeds))
    if not seeds: p.error('provide --url, --import-file, or --query with --search-endpoint')
    crawler=EmailCrawler(a.keyword,a.depth,a.concurrency,a.delay)
    task=asyncio.create_task(crawler.crawl(seeds))
    while not task.done():
        try:
            e=await asyncio.wait_for(crawler.progress.get(),timeout=.4)
            print(f"[{e['event']}] visited={e.get('visited','-')} queued={e.get('queued','-')} emails={e.get('emails','-')} {e.get('url','')}",flush=True)
        except asyncio.TimeoutError: pass
    records=await task; export_records(records,a.export_txt,a.export_csv); print(f'Completed: {len(records)} unique emails')

if __name__=='__main__': asyncio.run(main())
