from dataclasses import dataclass
from ..core.contracts import QueryRequest
from ..core.research import ResearchEngine
from ..core.deep_research import DeepResearchEngine
from ..project_builder.generator import ProjectGenerator
from ..crawler.onion import OnionProvider
from ..artifacts.store import ArtifactStore

@dataclass
class AgentOrchestrator:
    research: ResearchEngine
    generator: ProjectGenerator
    artifacts: ArtifactStore
    deep: DeepResearchEngine | None = None
    onion: OnionProvider | None = None

    def handle(self, message: str, language: str = 'python', deep_search: bool = True, onion_urls: list[str] | None = None) -> dict:
        request = QueryRequest(message)
        if deep_search and self.deep:
            answer = self.deep.summarize(self.deep.search(request))
        else:
            answer = self.research.summarize(self.research.search(request))
        if onion_urls and self.onion:
            answer['dark_web_sources'] = []
            for url in onion_urls:
                try:
                    answer['dark_web_sources'].append(self.onion.fetch(url).__dict__)
                except Exception as exc:
                    answer['dark_web_sources'].append({'url': url, 'error': str(exc)})
        if any(word in message.lower() for word in ('build', 'create', 'implement', 'code', 'project', 'website', 'web app')):
            manifest = self.generator.render(self.generator.plan(message, language))
            stored = self.artifacts.save_project(manifest.name, manifest.files, {'language': manifest.language, 'description': manifest.description})
            answer['artifact'] = {'name': manifest.name, 'language': manifest.language, 'files': manifest.files, 'storage': stored}
        answer['policy'] = {'execution': 'disabled-by-default', 'external_tools': 'permission-required', 'dark_web': 'authorized/public onion targets only; no enumeration or access-control bypass', 'hosting': 'provider authentication and explicit deployment action required'}
        return answer
