from dataclasses import dataclass
from math import exp
from statistics import mean
@dataclass(frozen=True)
class SequenceInsight:
    score: float
    confidence: float
    explanation: str
    model_version: str
class SequenceModel:
    """Safe reference sequence model; replaceable by ONNX/PyTorch/TensorFlow adapters."""
    def score(self, values: list[float]) -> SequenceInsight:
        if not values: return SequenceInsight(0.0,0.0,"empty sequence","reference-1")
        m=mean(values); spread=mean((x-m)*(x-m) for x in values)**0.5
        score=1.0-exp(-spread)
        return SequenceInsight(round(score,6),round(min(0.99,0.5+len(values)/200),6),f"sequence spread={spread:.4f}","reference-1")
    def forecast(self, values: list[float], horizon: int) -> list[float]:
        if horizon<0: raise ValueError("horizon must be non-negative")
        if not values: return [0.0]*horizon
        return [float(values[-1]) for _ in range(horizon)]
