import unittest
from AgentResearchForge.documents.index import DocumentIndexer

class TestDocuments(unittest.TestCase):
    def test_index_and_search(self):
        idx = DocumentIndexer(); idx.add_text('a.md', 'Chimera research architecture and RNN engine')
        rows = idx.search('RNN engine')
        self.assertTrue(rows); self.assertEqual(rows[0]['path'], 'a.md')

if __name__ == '__main__': unittest.main()
