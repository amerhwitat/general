from dataclasses import dataclass
@dataclass(frozen=True)
class Correlation:
    service_id:str; deployment_id:str|None; incident_id:str|None; correlation_id:str

def correlate(telemetry_event:dict, deployment:dict|None, incident:dict|None)->Correlation:
    cid=telemetry_event.get("correlation_id") or (deployment or {}).get("correlation_id") or (incident or {}).get("correlation_id")
    if not cid: raise ValueError("correlation_id required")
    return Correlation((telemetry_event.get("service_id") or (deployment or {}).get("service_id") or "unknown"),(deployment or {}).get("id"),(incident or {}).get("id"),cid)
