from collections import deque
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from .web import WebProvider
from ..core.contracts import SourceRecord
from .policy import CrawlPolicy

class _Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for key, value in attrs:
                if key.lower() == 'href' and value: self.links.append(value)

class DeepWebCrawler:
    def __init__(self, provider: WebProvider, max_depth: int = 2, max_pages: int = 30):
        self.provider = provider; self.max_depth = max_depth; self.max_pages = max_pages

    def crawl(self, seeds: list[str]) -> list[SourceRecord]:
        queue = deque((url, 0) for url in seeds); seen=set(); results=[]
        while queue and len(results) < self.max_pages:
            url, depth = queue.popleft()
            if url in seen or not CrawlPolicy().validate(url): continue
            seen.add(url)
            try: record = self.provider.fetch(url)
            except Exception: continue
            results.append(record)
            if depth >= self.max_depth: continue
            parser = _Links()
            try: parser.feed(record.text)
            except Exception: continue
            base = urlparse(url)
            for href in parser.links:
                child = urljoin(url, href)
                parsed = urlparse(child)
                if parsed.scheme in {'http','https'} and parsed.netloc == base.netloc and child not in seen:
                    queue.append((child, depth + 1))
        return results
