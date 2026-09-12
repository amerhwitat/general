import unittest
from AgentResearchForge.core.contracts import QueryRequest, SourceRecord
from AgentResearchForge.core.research import ResearchEngine

class Provider:
    def __init__(self, rows): self.rows = rows
    def search(self, query, limit=20): return self.rows

class TestResearch(unittest.TestCase):
    def test_deduplicates_and_preserves_provenance(self):
        row = SourceRecord('https://example.org/a', 'A', 'evidence', 'web', 'official')
        engine = ResearchEngine({'web': Provider([row]), 'library': Provider([row])})
        result = engine.search(QueryRequest('x', ('web','library'), 10))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].provenance, 'official')

if __name__ == '__main__': unittest.main()
