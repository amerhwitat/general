from dataclasses import dataclass, field
from typing import Any, Protocol

@dataclass(frozen=True)
class QueryRequest:
    text: str
    sources: tuple[str, ...] = ("web", "library", "documents", "code")
    max_results: int = 20

@dataclass(frozen=True)
class SourceRecord:
    url: str
    title: str
    text: str
    source_type: str
    provenance: str = "unknown"
    license: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

class SearchProvider(Protocol):
    def search(self, query: str, limit: int = 20) -> list[SourceRecord]: ...

class ResearchResult(dict):
    pass
