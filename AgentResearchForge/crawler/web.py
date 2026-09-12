from dataclasses import dataclass
from urllib.parse import urlparse
import requests
from .policy import CrawlPolicy
from ..core.contracts import SourceRecord

@dataclass
class WebProvider:
    search_url: str = 'http://localhost:8080/search'
    timeout: int = 15

    def search(self, query: str, limit: int = 20) -> list[SourceRecord]:
        r = requests.get(self.search_url, params={'q': query, 'format': 'json'}, timeout=self.timeout)
        r.raise_for_status()
        out = []
        for row in r.json().get('results', [])[:limit]:
            out.append(SourceRecord(row.get('url',''), row.get('title',''), row.get('content') or row.get('snippet',''), 'web', 'search-backend'))
        return out

    def fetch(self, url: str) -> SourceRecord:
        if not CrawlPolicy().validate(url):
            raise ValueError('URL rejected by crawl policy')
        r = requests.get(url, timeout=self.timeout, headers={'User-Agent': 'AgentResearchForge/0.1'})
        r.raise_for_status()
        return SourceRecord(url, url, r.text[:2_000_000], 'web', 'direct-fetch')
