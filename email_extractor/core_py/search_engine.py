"""Search-provider adapters. Prefer official APIs; HTML search is opt-in and bounded."""
from urllib.parse import quote, urlparse
import requests
from bs4 import BeautifulSoup

def search_google(keyword: str, max_results: int = 10):
    url=f"https://www.google.com/search?q={quote(keyword)}"
    r=requests.get(url,headers={"User-Agent":"ChimeraEmailExtractor/1.0"},timeout=10); r.raise_for_status()
    soup=BeautifulSoup(r.text,"html.parser"); out=[]
    for a in soup.select('a[href]'):
        href=a.get('href','')
        if href.startswith('/url?q='):
            candidate=href.split('/url?q=',1)[1].split('&',1)[0]
            if urlparse(candidate).scheme in {'http','https'} and candidate not in out: out.append(candidate)
        if len(out)>=max_results: break
    return out
