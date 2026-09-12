"""Shared OCR geometry contract mirrored from the canonical nlp platform."""
from dataclasses import dataclass
from enum import Enum

class Direction(str, Enum):
    RTL='rtl'; LTR='ltr'; TTB='ttb'; BTT='btt'; SPIRAL='spiral'; REVERSE='reverse'; UNKNOWN='unknown'

@dataclass
class Route:
    direction: Direction
    operations: list[str]
    confidence: float

def route(direction: str | None = None, *, skewed: bool = False, weathered: bool = False) -> Route:
    d = Direction((direction or 'unknown').lower()) if (direction or 'unknown').lower() in {x.value for x in Direction} else Direction.UNKNOWN
    ops = ['normalize','quality-check']
    if skewed: ops += ['deskew','perspective-unwarp']
    if weathered: ops += ['denoise','contrast-enhance','local-threshold']
    ops += ['vertical-line-segmentation' if d in {Direction.TTB,Direction.BTT} else 'spiral-path-segmentation' if d is Direction.SPIRAL else 'reverse-reading-hypothesis' if d is Direction.REVERSE else 'line-segmentation']
    return Route(d, ops, 0.65 if d is not Direction.UNKNOWN else 0.25)
