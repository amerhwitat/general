from dataclasses import dataclass
from ..core.contracts import QueryRequest
from ..core.research import ResearchEngine
from ..project_builder.generator import ProjectGenerator

@dataclass
class AgentOrchestrator:
    research: ResearchEngine
    generator: ProjectGenerator

    def handle(self, message: str, language: str = 'python') -> dict:
        request = QueryRequest(message)
        evidence = self.research.search(request)
        answer = self.research.summarize(evidence)
        if any(word in message.lower() for word in ('build', 'create', 'implement', 'code', 'project')):
            manifest = self.generator.render(self.generator.plan(message, language))
            answer['artifact'] = {'name': manifest.name, 'language': manifest.language, 'files': manifest.files}
        answer['policy'] = {'execution': 'disabled-by-default', 'external_tools': 'permission-required'}
        return answer
