from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

@dataclass
class ResearchConfig:
    max_pages: int = 50
    timeout: float = 15
    allow_onion: bool = False
    tor_proxy: str = 'socks5h://127.0.0.1:9050'

class DeepWebResearch:
    """Search-expansion crawler for public/authorized web resources.

    This follows explicitly supplied URLs and links discovered from those pages;
    it does not enumerate private services or onion address space.
    """
    def __init__(self, config: ResearchConfig | None = None): self.config=config or ResearchConfig()
    def _get(self,url):
        host=url.split('/')[2].lower() if '://' in url else ''
        if host.endswith('.onion'):
            if not self.config.allow_onion: raise PermissionError('onion research disabled')
            proxies={'http':self.config.tor_proxy,'https':self.config.tor_proxy}
        else: proxies=None
        return requests.get(url,timeout=self.config.timeout,headers={'User-Agent':'SEO-Tool-Research/0.1'},proxies=proxies)
    def expand(self,seeds:list[str],terms:list[str]) -> list[dict]:
        queue=list(seeds); seen=set(); results=[]
        while queue and len(seen)<self.config.max_pages:
            url=queue.pop(0)
            if url in seen: continue
            seen.add(url)
            try:
                r=self._get(url)
                soup=BeautifulSoup(r.text,'html.parser') if 'html' in r.headers.get('content-type','') else None
                title=soup.title.get_text(' ',strip=True) if soup and soup.title else ''
                text=soup.get_text(' ',strip=True) if soup else ''
                score=sum(1 for t in terms if t.casefold() in text.casefold())
                results.append({'url':r.url,'status':r.status_code,'title':title,'score':score,'text':text[:10000]})
                if soup:
                    for a in soup.find_all('a',href=True):
                        nxt=urljoin(r.url,a['href']).split('#')[0]
                        if nxt.startswith(('http://','https://')) and nxt not in seen: queue.append(nxt)
            except Exception as e: results.append({'url':url,'error':str(e)[:300]})
        return sorted(results,key=lambda x:x.get('score',0),reverse=True)
    def save(self,results:list[dict],directory:Path):
        directory.mkdir(parents=True,exist_ok=True)
        (directory/'deep-research.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
        (directory/'deep-research.md').write_text('\n\n'.join(f"## {x.get('title','')}\n{x.get('url','')}\n\n{x.get('text','')[:4000]}" for x in results),encoding='utf-8')
