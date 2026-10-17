from __future__ import annotations
from datetime import datetime, timezone
import os
from enum import Enum
from typing import Any
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Chimera WorkFlow Studio API", version="0.1.0")

# CORS is opt-in by origin. Add the published browser GUI origin explicitly when
# you intend to use it; never use wildcard origins for a local service with writes.
_DEFAULT_CORS_ORIGINS = "http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173,http://127.0.0.1:5173"
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("WORKFLOW_STUDIO_CORS_ORIGINS", _DEFAULT_CORS_ORIGINS).split(",")
    if origin.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

class WorkType(str, Enum):
    epic='epic'; story='story'; task='task'; bug='bug'; incident='incident'; change='change'; problem='problem'

class WorkItem(BaseModel):
    id: str
    project_id: str
    title: str
    type: WorkType = WorkType.task
    status: str = 'backlog'
    priority: int = Field(default=3, ge=1, le=5)
    assignee: str | None = None
    labels: list[str] = []
    metadata: dict[str, Any] = {}

class Project(BaseModel):
    id: str
    name: str
    methodology: str = 'scrum'
    owner: str

class InMemoryStore:
    def __init__(self): self.projects: dict[str, Project] = {}; self.items: dict[str, WorkItem] = {}
store = InMemoryStore()

@app.get('/health')
def health(): return {'status':'ok','time':datetime.now(timezone.utc).isoformat()}

@app.post('/api/projects')
def create_project(project: Project):
    if project.id in store.projects: raise HTTPException(409, 'project exists')
    store.projects[project.id] = project
    return project

@app.get('/api/projects')
def projects(): return list(store.projects.values())

@app.post('/api/work-items')
def create_item(item: WorkItem):
    if item.project_id not in store.projects: raise HTTPException(404, 'project not found')
    store.items[item.id] = item
    return item

@app.get('/api/projects/{project_id}/work-items')
def project_items(project_id: str): return [x for x in store.items.values() if x.project_id == project_id]

@app.post('/api/ai/sequence-score')
def sequence_score(payload: dict[str, Any]):
    # Reference contract: a real RNN/ML model is injected behind this endpoint.
    values = payload.get('values', [])
    if not values: return {'score':0.0,'anomaly':False,'model':'reference-rnn-contract'}
    mean = sum(float(x) for x in values) / len(values)
    last = float(values[-1])
    delta = abs(last - mean)
    return {'score':delta,'anomaly':delta > max(1.0, abs(mean)*0.5),'model':'reference-rnn-contract'}
