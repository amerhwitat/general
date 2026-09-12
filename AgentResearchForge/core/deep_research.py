from dataclasses import dataclass
from typing import Iterable
from .contracts import QueryRequest, SourceRecord
from .research import ResearchEngine

@dataclass
class DeepResearchEngine:
    engine: ResearchEngine
    max_subqueries: int = 8

    def _expand(self, query: str) -> list[str]:
        base = query.strip()
        variants = [base, f"{base} documentation", f"{base} implementation", f"{base} examples", f"{base} open source", f"{base} API", f"{base} security and limitations", f"{base} recent research"]
        seen = set(); out = []
        for item in variants:
            key = item.casefold()
            if key not in seen:
                seen.add(key); out.append(item)
        return out[: self.max_subqueries]

    def search(self, request: QueryRequest) -> dict:
        records: list[SourceRecord] = []
        subqueries = self._expand(request.text)
        for query in subqueries:
            records.extend(self.engine.search(QueryRequest(query, request.sources, request.max_results)))
        unique = {}
        for record in records:
            key = (record.url or record.title or record.text[:80]).casefold()
            unique[key] = record
        ranked = sorted(unique.values(), key=lambda r: (len(r.text or ''), r.source_type), reverse=True)
        return {'subqueries': subqueries, 'sources': ranked[:request.max_results]}

    def summarize(self, result: dict) -> dict:
        sources = result.get('sources', [])
        text = "\n\n".join((s.text or '')[:3000] for s in sources[:12])
        return {'summary': text[:18000], 'sources': [s.__dict__ for s in sources], 'subqueries': result.get('subqueries', [])}
