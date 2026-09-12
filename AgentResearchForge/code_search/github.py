from ..core.contracts import SourceRecord
import requests

class GitHubCodeProvider:
    def __init__(self, api_base='https://api.github.com', timeout=15):
        self.api_base = api_base.rstrip('/')
        self.timeout = timeout

    def search(self, query: str, limit: int = 10) -> list[SourceRecord]:
        r = requests.get(f'{self.api_base}/search/repositories', params={'q': query, 'per_page': min(limit, 30)}, timeout=self.timeout, headers={'Accept':'application/vnd.github+json'})
        r.raise_for_status()
        return [SourceRecord(x['html_url'], x.get('full_name',''), x.get('description') or '', 'github', 'github-public', metadata={'license': (x.get('license') or {}).get('spdx_id'), 'stars': x.get('stargazers_count')}) for x in r.json().get('items', [])]
