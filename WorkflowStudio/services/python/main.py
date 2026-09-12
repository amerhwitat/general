from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Chimera WorkFlow Studio API", version="0.1.0")

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
