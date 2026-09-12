from collections.abc import Iterable
from .contracts import QueryRequest, SearchProvider, SourceRecord

class ResearchEngine:
    def __init__(self, providers: dict[str, SearchProvider]):
        self.providers = providers

    def search(self, request: QueryRequest) -> list[SourceRecord]:
        seen: set[str] = set()
        results: list[SourceRecord] = []
        for source in request.sources:
            provider = self.providers.get(source)
            if provider is None:
                continue
            for item in provider.search(request.text, request.max_results):
                if item.url in seen:
                    continue
                seen.add(item.url)
                results.append(item)
                if len(results) >= request.max_results:
                    return results
        return results

    @staticmethod
    def summarize(records: Iterable[SourceRecord]) -> dict:
        rows = list(records)
        return {
            "summary": " ".join(r.text.strip().replace("\n", " ")[:500] for r in rows[:8]),
            "sources": [
                {"url": r.url, "title": r.title, "type": r.source_type,
                 "provenance": r.provenance, "license": r.license}
                for r in rows
            ],
        }
