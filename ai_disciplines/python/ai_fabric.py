"""Provider-neutral AI discipline orchestration primitives.

Optional heavyweight frameworks are deliberately imported only by user code; this
module remains dependency-light and can describe ML/DL/RL/Symbolic/CV/NLP jobs.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List

DISCIPLINES = ("ml", "dl", "rl", "symbolic_ai", "computer_vision", "nlp")

@dataclass
class AIJob:
    discipline: str
    task: str
    data_kind: str
    framework: str | None = None
    parameters: Dict[str, Any] = field(default_factory=dict)
    provenance: Dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if self.discipline not in DISCIPLINES:
            raise ValueError(f"unsupported discipline: {self.discipline}")
        if not self.task:
            raise ValueError("task is required")
        if not self.data_kind:
            raise ValueError("data_kind is required")

    def manifest(self) -> Dict[str, Any]:
        self.validate()
        return {"schema": "CHIMERA-AI-JOB-1", **self.__dict__}

class AIFabric:
    def describe(self) -> List[str]:
        return list(DISCIPLINES)

    def make_job(self, discipline: str, task: str, data_kind: str, **kwargs: Any) -> AIJob:
        job = AIJob(discipline, task, data_kind, **kwargs)
        job.validate()
        return job
