"""Optional adapters for established AI ecosystems.

No third-party source is vendored. Imports happen only when an adapter is used.
"""
from __future__ import annotations

class ProviderUnavailable(RuntimeError):
    pass

def _require(module: str):
    try:
        return __import__(module)
    except ImportError as exc:
        raise ProviderUnavailable(f"Optional provider '{module}' is not installed") from exc

def ml_provider():
    return _require("sklearn")

def dl_provider(name: str = "torch"):
    return _require(name)

def rl_provider(name: str = "gymnasium"):
    return _require(name)

def symbolic_provider():
    return _require("sympy")

def cv_provider(name: str = "cv2"):
    return _require(name)

def nlp_provider(name: str = "spacy"):
    return _require(name)
