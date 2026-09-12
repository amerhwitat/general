from dataclasses import dataclass
import requests
from .policy import CrawlPolicy
from ..core.contracts import SourceRecord

@dataclass
class OnionProvider:
    proxy: str = 'socks5h://127.0.0.1:9050'
    timeout: int = 20
    allow_onion: bool = False

    def fetch(self, url: str) -> SourceRecord:
        if not CrawlPolicy(self.allow_onion).validate(url, onion=True):
            raise ValueError('Onion URL rejected: provide an explicitly authorized/public .onion target and enable allow_onion')
        r = requests.get(url, timeout=self.timeout, proxies={'http': self.proxy, 'https': self.proxy}, headers={'User-Agent': 'AgentResearchForge/0.1'})
        r.raise_for_status()
        return SourceRecord(url, url, r.text[:2_000_000], 'onion', 'tor-socks-direct')
