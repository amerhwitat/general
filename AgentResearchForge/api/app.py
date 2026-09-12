import os
from pathlib import Path
try:
    from fastapi import FastAPI, UploadFile, File
    from pydantic import BaseModel
except ImportError:
    FastAPI = None

from ..documents.index import DocumentIndexer
from ..core.research import ResearchEngine
from ..core.deep_research import DeepResearchEngine
from ..project_builder.generator import ProjectGenerator
from ..agents.orchestrator import AgentOrchestrator
from ..crawler.web import WebProvider
from ..crawler.onion import OnionProvider
from ..code_search.github import GitHubCodeProvider
from ..artifacts.store import ArtifactStore
from ..exporters.documents import export_markdown, export_html, export_text, export_docx, export_pdf
from ..hosting.registry import targets

index = DocumentIndexer()
library_root = os.getenv('AGENT_LIBRARY_PATH')
if library_root:
    index.ingest_tree(library_root)
providers = {'library': index, 'documents': index, 'code': GitHubCodeProvider()}
search_url = os.getenv('AGENT_SEARCH_URL')
if search_url:
    providers['web'] = WebProvider(search_url=search_url)
engine = ResearchEngine(providers)
artifacts = ArtifactStore(Path(os.getenv('AGENT_ARTIFACT_PATH', 'data/artifacts')))
onion = OnionProvider(allow_onion=os.getenv('AGENT_ALLOW_ONION', '0') == '1')
orchestrator = AgentOrchestrator(engine, ProjectGenerator(), artifacts, DeepResearchEngine(engine), onion)

if FastAPI:
    app = FastAPI(title='AgentResearchForge')
    class ChatRequest(BaseModel):
        message: str
        language: str = 'python'
        deep_search: bool = True
        onion_urls: list[str] = []

    class ExportRequest(BaseModel):
        title: str
        body: str
        sources: list[dict] = []
        format: str = 'md'

    @app.get('/health')
    def health():
        return {'ok': True, 'providers': sorted(providers), 'library_records': len(index.records), 'hosting_targets': targets(), 'onion_enabled': onion.allow_onion}

    @app.post('/chat')
    def chat(request: ChatRequest):
        return orchestrator.handle(request.message, request.language, request.deep_search, request.onion_urls)

    @app.post('/documents')
    async def documents(file: UploadFile = File(...)):
        target = Path('data/uploads') / Path(file.filename or 'upload.bin').name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(await file.read())
        indexed = index.ingest_path(str(target))
        return {'filename': target.name, 'indexed': indexed, 'records': len(index.records)}

    @app.post('/export')
    def export(request: ExportRequest):
        fmt = request.format.lower(); ext = {'md': '.md', 'markdown': '.md', 'html': '.html', 'txt': '.txt', 'docx': '.docx', 'pdf': '.pdf'}.get(fmt)
        if not ext:
            raise ValueError('Supported export formats: md, html, txt, docx, pdf')
        target = Path('data/exports') / f"result-{abs(hash(request.title))}{ext}"
        if fmt in {'md', 'markdown'}: path = export_markdown(str(target), request.title, request.body, request.sources)
        elif fmt == 'html': path = export_html(str(target), request.title, request.body, request.sources)
        elif fmt == 'txt': path = export_text(str(target), request.title, request.body)
        elif fmt == 'docx': path = export_docx(str(target), request.title, request.body, request.sources)
        else: path = export_pdf(str(target), request.title, request.body, request.sources)
        return {'path': path}
else:
    app = None
