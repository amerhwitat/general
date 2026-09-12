import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[2]
def test_domain_schema_has_core_kinds():
    s=json.loads((BASE/"contracts/schema.json").read_text())
    kinds=s["properties"]["kind"]["enum"]
    assert "project" in kinds and "incident" in kinds and "deployment" in kinds

def test_event_schema_has_correlation():
    s=json.loads((BASE/"contracts/events.json").read_text())
    assert "correlation_id" in s["required"]
