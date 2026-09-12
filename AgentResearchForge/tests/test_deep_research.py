from AgentResearchForge.core.deep_research import DeepResearchEngine
from AgentResearchForge.core.contracts import SourceRecord

class Provider:
    def search(self, query, limit=20):
        return [SourceRecord('https://example.org/a', 'A', f'result for {query}', 'web', 'test')]

def test_deep_search_expands_and_deduplicates():
    from AgentResearchForge.core.research import ResearchEngine
    result = DeepResearchEngine(ResearchEngine({'web': Provider()}), max_subqueries=3).search(__import__('AgentResearchForge.core.contracts', fromlist=['QueryRequest']).QueryRequest('test'))
    assert len(result['subqueries']) == 3
    assert len(result['sources']) == 1
