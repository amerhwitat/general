"""Local-first recurrent semantic engine for Chimera 3D/4D Studio.

It provides compact scene/time-series memory and an optional PyTorch GRU backend.
The engine is an inference/training boundary; it is not a pretrained foundation model.
"""
from dataclasses import dataclass, field
import math
import re
from typing import Iterable

TOKEN = re.compile(r"\w+|[^\w\s]", re.UNICODE)

@dataclass
class SceneState:
    hidden: list[float]
    memories: list[str] = field(default_factory=list)
    step: int = 0

class SceneRNNLLM:
    def __init__(self, hidden_size: int = 128, max_memory: int = 64):
        self.hidden_size = hidden_size
        self.max_memory = max_memory
        self.state = SceneState([0.0] * hidden_size)

    def reset(self):
        self.state = SceneState([0.0] * self.hidden_size)

    def observe(self, text: str) -> dict:
        for token in TOKEN.findall(str(text).lower()):
            seed = sum(map(ord, token)) % 997
            for i, value in enumerate(self.state.hidden):
                self.state.hidden[i] = math.tanh(0.98 * value + 0.02 * math.sin((seed + i) * 0.013))
            self.state.step += 1
        if text.strip():
            self.state.memories.append(text.strip())
            self.state.memories = self.state.memories[-self.max_memory:]
        return self.summary()

    def scene_prompt(self) -> str:
        return "\n".join(self.state.memories)

    def suggest(self, scene_text: str) -> dict:
        self.observe(scene_text)
        s = scene_text.lower()
        if any(k in s for k in ("camera", "tracking", "motion")):
            recommendation = "analyze motion stream and camera trajectory"
        elif any(k in s for k in ("material", "shader", "texture")):
            recommendation = "inspect material graph and texture dependencies"
        elif any(k in s for k in ("time", "animation", "keyframe")):
            recommendation = "inspect temporal continuity and keyframe density"
        else:
            recommendation = "summarize scene structure and recent changes"
        return {"recommendation": recommendation, "state": self.summary()}

    def summary(self) -> dict:
        energy = sum(v*v for v in self.state.hidden) / max(1, self.hidden_size)
        return {"steps": self.state.step, "memory_items": len(self.state.memories),
                "hidden_size": self.hidden_size, "state_energy": energy}

class TorchGRUBackend:
    """Optional PyTorch GRU next-token backend for future scene-language training."""
    def __init__(self, vocab_size: int, embedding_size: int = 256, hidden_size: int = 512):
        import torch.nn as nn
        self.embedding = nn.Embedding(vocab_size, embedding_size)
        self.gru = nn.GRU(embedding_size, hidden_size, batch_first=True)
        self.head = nn.Linear(hidden_size, vocab_size)

    def forward(self, token_ids, hidden=None):
        x = self.embedding(token_ids)
        x, hidden = self.gru(x, hidden)
        return self.head(x), hidden
