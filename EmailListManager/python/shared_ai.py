from __future__ import annotations
import os, math, json, urllib.request

class RNNLLM:
    """Tiny recurrent ranker + optional Ollama-compatible local LLM adapter."""
    def __init__(self, endpoint=None, model=None, enabled=None):
        self.endpoint = endpoint or os.getenv("CHIMERA_LLM_ENDPOINT", "http://127.0.0.1:11434/api/generate")
        self.model = model or os.getenv("CHIMERA_LLM_MODEL", "llama3.2")
        self.enabled = (enabled if enabled is not None else os.getenv("CHIMERA_AI_ENABLED", "0") == "1")
        self.state = 0.0
    def recurrent_score(self, text: str) -> float:
        # Stable lightweight recurrent state; useful for ranking without a model server.
        for ch in text.lower()[:4096]:
            x = (ord(ch) % 97) / 96.0
            self.state = math.tanh(0.86 * self.state + 0.14 * x)
        return (self.state + 1.0) / 2.0
    def generate(self, prompt: str) -> str | None:
        if not self.enabled: return None
        body = json.dumps({"model": self.model, "prompt": prompt, "stream": False}).encode()
        req = urllib.request.Request(self.endpoint, data=body, headers={"Content-Type":"application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode()).get("response")
        except Exception:
            return None
    def classify_contact(self, email: str, context: str = "") -> dict:
        score = self.recurrent_score(email + " " + context)
        text = self.generate(f"Classify this public contact record conservatively. Email={email}; Context={context}. Return one short label.")
        return {"score": round(score, 6), "label": (text or "heuristic").strip()[:120]}
