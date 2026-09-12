try:
    from fastapi import FastAPI, UploadFile, File
    from pydantic import BaseModel
except ImportError:
    FastAPI = None

from pathlib import Path
from ..documents.index import DocumentIndexer
from ..core.research import ResearchEngine
from ..project_builder.generator import ProjectGenerator
from ..agents.orchestrator import AgentOrchestrator

index = DocumentIndexer()
engine = ResearchEngine({'library': index})
orchestrator = AgentOrchestrator(engine, ProjectGenerator())

if FastAPI:
    app = FastAPI(title='AgentResearchForge')
    class ChatRequest(BaseModel):
        message: str
        language: str = 'python'

    @app.post('/chat')
    def chat(request: ChatRequest):
        return orchestrator.handle(request.message, request.language)

    @app.post('/documents')
    async def documents(file: UploadFile = File(...)):
        target = Path('data/uploads') / Path(file.filename or 'upload.bin').name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(await file.read())
        indexed = index.ingest_path(str(target))
        return {'filename': target.name, 'indexed': indexed}
else:
    app = None
