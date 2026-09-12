# WorkflowStudio API contract

The API is versioned under `/api`. Core resources are projects, work-items, teams, services, incidents, problems, changes, requests, SLAs, pipelines, deployments and events.

## Event envelope

```json
{"event_id":"evt-1","event_type":"deployment.completed","occurred_at":"2026-09-12T00:00:00Z","tenant_id":"tenant-1","actor_id":"user-1","correlation_id":"rel-1","schema_version":1,"payload":{}}
```

Clients should use idempotency keys for mutation retries and the `version` field for optimistic concurrency. Long-running provider actions return an operation/run identifier and are observed asynchronously.