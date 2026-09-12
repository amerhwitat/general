# Architecture

## Domain
`Project`, `WorkItem`, `Sprint`, `Release`, `Workflow`, `Pipeline`, `Deployment`, `Service`, `Incident`, `Problem`, `Change`, `SLA`, `KnowledgeArticle`, `Team`, `User`, `Role`, `AuditEvent`, `Peer`, `Metric`, `Trace`, `LogEvent`, `VoiceCommand` and `AIInsight` are stable API concepts.

## Agile engine
Workflow templates are data, not hard-coded screens. Each template defines states, transitions, WIP limits, ceremonies, estimation, metrics and required evidence. This permits Scrum/Kanban/XP/Lean/Scrumban/Crystal/DSDM/FDD/hybrid and portfolio templates to coexist.

## ITIL 4 layer
Service records connect incidents, problems, changes, requests, knowledge, SLAs, assets/configuration and continual-improvement actions. Change risk and approval gates can be linked to deployments.

## DevOps control plane
A provider-neutral `PipelineProvider` interface supports local runners, GitHub Actions, GitLab CI, Jenkins, Tekton, Argo Workflows, Argo CD, Kubernetes Jobs and OpenShift Pipelines/Deployments. Kubernetes remains the reconciliation substrate; the application records desired/current deployment state and events rather than pretending Kubernetes itself is a CI server.

## Observability
OpenTelemetry is the canonical telemetry boundary. Metrics, logs and traces are correlated to project/work-item/deployment IDs. Prometheus/Grafana are optional consumers.

## AI engine
A local Python service owns RNN/sequence-model interfaces. The interface accepts time-series/event sequences and returns classification, forecasting, anomaly scores and ranked recommendations. Model execution is isolated from the API process. The service may later bind to the existing Chimera neural-network engine through a gRPC/HTTP adapter.

## P2P
Peers are explicitly paired. Each peer has a public identity, capabilities, trust state and monotonic sequence. Messages use signed envelopes, timestamps/nonces and replay checks. Synchronization is CRDT/event-log friendly but server-authoritative policies still apply for permissions. P2P is collaboration/synchronization, not arbitrary remote execution.

## Security
Passwords are Argon2id/bcrypt through a vetted library; sessions use short-lived access tokens and rotating refresh tokens; RBAC/ABAC checks are server-side; secrets are references, never project messages; audit events are append-only. Production deployments should place TLS/mTLS at the gateway and use Kubernetes/OpenShift secrets or an external secret manager.
