"""Local-first recurrent language engine for Workflow Studio.

The engine is deliberately small and dependency-optional: PyTorch enables a trainable
GRU language model, while the deterministic state/memory layer works without it.
It is an application integration boundary, not a claim of a pretrained foundation model.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Sequence
import math
import re

TOKEN_RE = re.compile(r"\w+|[^\w\s]", re.UNICODE)


@dataclass
class RecurrentState:
    values: List[float]
    step: int = 0
    memory: List[str] = field(default_factory=list)


class RNNLLMEngine:
    """A bounded recurrent semantic engine with optional PyTorch GRU inference."""

    def __init__(self, hidden_size: int = 128, max_memory: int = 64):
        self.hidden_size = hidden_size
        self.max_memory = max_memory
        self.state = RecurrentState([0.0] * hidden_size)

    def reset(self) -> None:
        self.state = RecurrentState([0.0] * self.hidden_size)

    def remember(self, text: str) -> None:
        text = str(text).strip()
        if text:
            self.state.memory.append(text)
            self.state.memory = self.state.memory[-self.max_memory :]

    def step(self, text: str) -> List[float]:
        """Update recurrent state using a deterministic tanh recurrence."""
        for token in TOKEN_RE.findall(text.lower()):
            seed = sum(ord(c) for c in token) % 997
            for i, value in enumerate(self.state.values):
                drive = math.sin((seed + i * 13) * 0.017)
                self.state.values[i] = math.tanh(0.97 * value + 0.03 * drive)
            self.state.step += 1
        self.remember(text)
        return list(self.state.values)

    def context(self) -> str:
        return "\n".join(self.state.memory[-self.max_memory :])

    def summarize_state(self) -> dict:
        values = self.state.values
        energy = sum(v * v for v in values) / max(1, len(values))
        return {"steps": self.state.step, "memory_items": len(self.state.memory),
                "hidden_size": self.hidden_size, "state_energy": energy}

    def suggest_workflow_action(self, events: Sequence[str]) -> dict:
        """Produce an explainable advisory from recent event text."""
        joined = " ".join(events[-16:])
        self.step(joined)
        lowered = joined.lower()
        signals = {
            "incident": sum(k in lowered for k in ("incident", "outage", "error")),
            "delivery": sum(k in lowered for k in ("deploy", "release", "pipeline")),
            "risk": sum(k in lowered for k in ("risk", "blocked", "late", "failed")),
        }
        if signals["incident"]:
            action = "review_incident_cluster_and_recent_deployments"
        elif signals["risk"]:
            action = "prioritize_blocked_work_and_review_dependencies"
        elif signals["delivery"]:
            action = "correlate_pipeline_health_with_release_work"
        else:
            action = "summarize_recent_workflow_state"
        confidence = min(0.99, 0.45 + max(signals.values()) * 0.15)
        return {"action": action, "confidence": confidence, "signals": signals, "state": self.summarize_state()}


class TorchGRULanguageModel:
    """Optional trainable GRU LM wrapped as a proper PyTorch module."""

    def __init__(self, vocab_size: int, embedding_size: int = 256, hidden_size: int = 512):
        import torch.nn as nn

        class _Model(nn.Module):
            def __init__(self):
                super().__init__()
                self.embedding = nn.Embedding(vocab_size, embedding_size)
                self.gru = nn.GRU(embedding_size, hidden_size, batch_first=True)
                self.head = nn.Linear(hidden_size, vocab_size)

            def forward(self, token_ids, hidden=None):
                x = self.embedding(token_ids)
                x, hidden = self.gru(x, hidden)
                return self.head(x), hidden

        self.model = _Model()

    def parameters(self):
        return self.model.parameters()

    def forward(self, token_ids, hidden=None):
        return self.model(token_ids, hidden)
