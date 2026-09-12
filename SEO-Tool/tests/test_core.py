from pathlib import Path
from SEO_Tool.core import CrawlConfig, SeoCrawler

def test_url_policy(tmp_path):
    c=SeoCrawler(CrawlConfig('https://example.org',Path(tmp_path)))
    assert c._allowed('https://example.org')
    assert c._allowed('http://example.org')
    assert not c._allowed('file:///tmp/x')
    assert not c._allowed('https://user:pass@example.org')

def test_onion_policy(tmp_path):
    a=SeoCrawler(CrawlConfig('http://example.org',Path(tmp_path),allow_onion=False))
    assert not a._allowed('http://sample.onion')
    b=SeoCrawler(CrawlConfig('http://example.org',Path(tmp_path),allow_onion=True))
    assert b._allowed('http://sample.onion')
