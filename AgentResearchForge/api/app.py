import os
from pathlib import Path

try:
    from fastapi import FastAPI, UploadFile, File
    from pydantic import BaseModel
except ImportError:
    FastAPI = None

from ..documents.index import DocumentIndexer
from ..core.research import ResearchEngine
from ..project_builder.generator import ProjectGenerator
from ..agents.orchestrator import AgentOrchestrator
from ..crawler.web import WebProvider
from ..code_search.github import GitHubCodeProvider

index = DocumentIndexer()
library_root = os.getenv('AGENT_LIBRARY_PATH')
if library_root:
    index.ingest_tree(library_root)

providers = {'library': index, 'documents': index, 'code': GitHubCodeProvider()}
search_url = os.getenv('AGENT_SEARCH_URL')
if search_url:
    providers['web'] = WebProvider(search_url=search_url)

engine = ResearchEngine(providers)
orchestrator = AgentOrchestrator(engine, ProjectGenerator())

if FastAPI:
    app = FastAPI(title='AgentResearchForge')

    class ChatRequest(BaseModel):
        message: str
        language: str = 'python'

    @app.get('/health')
    def health():
        return {'ok': True, 'providers': sorted(providers), 'library_records': len(index.records)}

    @app.post('/chat')
    def chat(request: ChatRequest):
        return orchestrator.handle(request.message, request.language)

    @app.post('/documents')
    async def documents(file: UploadFile = File(...)):
        target = Path('data/uploads') / Path(file.filename or 'upload.bin').name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(await file.read())
        indexed = index.ingest_path(str(target))
        return {'filename': target.name, 'indexed': indexed, 'records': len(index.records)}
else:
    app = None
