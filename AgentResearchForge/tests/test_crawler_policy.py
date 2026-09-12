import unittest
from AgentResearchForge.crawler.policy import CrawlPolicy

class TestPolicy(unittest.TestCase):
    def test_rejects_private_and_credential_urls(self):
        p = CrawlPolicy()
        self.assertFalse(p.validate('http://127.0.0.1:8000'))
        self.assertFalse(p.validate('https://user:pass@example.org'))
    def test_onion_requires_explicit_enablement(self):
        self.assertFalse(CrawlPolicy(False).validate('http://example.onion', onion=True))
        self.assertTrue(CrawlPolicy(True).validate('http://example.onion', onion=True))

if __name__ == '__main__': unittest.main()
