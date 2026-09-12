# Chimera WorkFlow Studio

A self-hosted, cross-platform project/workflow/DevOps and service-management application for computers and mobile devices. It combines Jira/Azure DevOps-style work tracking, Agile methods, ITIL 4-aligned service management, CI/CD orchestration, Kubernetes/OpenShift integration, observability, team collaboration, voice controls, and a local-first RNN/ML assistant.

## Design principles
- API-first and event-driven; the same domain model is exposed to web, desktop, mobile and CLI clients.
- Open-source integration boundaries: Kubernetes, OpenShift-compatible APIs, Argo Workflows/Argo CD, Tekton, OpenTelemetry, Prometheus/Grafana, GitHub/GitLab/Gitea/Forgejo and container registries.
- Provider adapters never require proprietary SDKs when a standards-based API is available.
- Local-first AI: the assistant can operate without sending project data to a hosted model; external inference is opt-in.
- Secure P2P collaboration: explicit pairing/trust, signed messages, capability negotiation, replay protection and least privilege. No unsolicited scanning or remote command execution.
- 128D semantic state is an optional metadata layer for perception/context, not a replacement for ordinary project or service records.

## Product areas
1. Portfolio / programs / projects
2. Backlog, epics, stories, tasks, bugs and dependencies
3. Scrum, Kanban, Scrumban, XP, Lean, SAFe-inspired portfolio views, Crystal, DSDM, FDD and hybrid planning templates
4. Roadmaps, releases, milestones, Gantt, capacity and risk registers
5. ITIL 4-aligned incident, problem, change, service request, knowledge, asset/configuration, SLA and continual-improvement records
6. CI/CD pipelines, artifacts, environments, approvals and deployment history
7. Kubernetes/OpenShift cluster and workload monitoring
8. Git provider integration and webhook/event ingestion
9. OpenTelemetry metrics/logs/traces with Prometheus/Grafana adapters
10. Team chat/comments, mentions, notifications and optional P2P synchronization
11. Admin/user/role/team/workspace tenancy and audit trail
12. RNN/ML assistant, project summarization, anomaly detection, prioritization and workflow recommendations
13. Speech-to-text/text-to-speech hooks with locale/voice controls

## Implementations
- `core/cpp` — portable C++20 domain/engine foundation
- `services/python` — FastAPI reference service and ML orchestration
- `services/node` — TypeScript/Node API and webhook worker
- `clients/web` — TypeScript web application shell
- `clients/android` — Kotlin Android client
- `clients/ios` — Swift iOS/iPadOS client
- `clients/flutter` — Dart cross-platform client
- `clients/java` — Java desktop/CLI SDK
- `clients/go` — Go automation/agent client
- `clients/rust` — Rust secure agent/CLI
- `deploy` — Docker Compose, Kubernetes and OpenShift manifests
- `ci` — GitHub Actions and reusable CI/CD examples

## License
Original project code: GPL-3.0-or-later. Third-party dependencies retain their own licenses. This project documents and integrates open APIs; it does not copy proprietary source code.
