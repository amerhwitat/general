# Chimera WorkFlow Studio

A self-hosted, cross-platform project/workflow/DevOps and service-management platform for computers and mobile devices. It combines Jira/Azure DevOps-style work tracking, Agile methods, ITIL 4-aligned service management, CI/CD orchestration, Kubernetes/OpenShift integration, observability, team collaboration, voice controls, trusted P2P synchronization, and a local-first RNN/LLM assistant.

## AI engine

`services/python/rnn_llm_engine.py` provides the reference local recurrent engine. It includes bounded recurrent state, short-term memory, explainable workflow recommendations and an optional trainable PyTorch GRU language-model backend. The AI layer is deliberately separated from production mutation: model output is advisory and policy approval remains required.

The AI architecture is informed by LangChain, LangGraph, LlamaIndex, Open WebUI, FastAPI, Chroma and state-space/RNN research such as Mamba. See `docs/AI_RNN_LLM.md`; these projects are references/integration boundaries, not copied source. citeturn0search2turn0search0turn0search1turn0search3turn1search0

## Current implementation
- Shared JSON domain/event contracts in `contracts/`.
- Data-driven Agile and ITIL 4 catalogs in `domain/`.
- Persistent-schema foundation in `database/`.
- Provider-neutral C++ workflow state machine and DevOps provider interfaces.
- Python sequence-model/inference and telemetry-correlation foundations.
- Local-first RNN/LLM engine and regression tests in `services/python/`.
- Trusted-P2P envelope/replay policy boundary and multilingual voice-command schema/router.
- Docker images for Python and Node services.
- Contract and observability smoke tests.

## Design principles
- API-first and event-driven; the same domain model is exposed to web, desktop, mobile and CLI clients.
- Open-source integration boundaries: Kubernetes, OpenShift-compatible APIs, Argo Workflows/Argo CD, Tekton, OpenTelemetry, Prometheus/Grafana, GitHub/GitLab/Gitea/Forgejo and container registries.
- Provider adapters never require proprietary SDKs when a standards-based API is available.
- Local-first AI: the assistant can operate without sending project data to a hosted model; external inference is opt-in.
- Secure P2P collaboration: explicit pairing/trust, signed messages, capability negotiation, replay protection and least privilege. No unsolicited scanning or arbitrary remote execution.
- AI recommendations are advisory and production mutations require policy approval.
- 128D semantic state is an optional metadata layer for perception/context, not a replacement for ordinary project or service records.

## Product areas
1. Portfolio / programs / projects
2. Backlog, epics, stories, tasks, bugs and dependencies
3. Scrum, Kanban, Scrumban, XP, Lean, scaled/portfolio views, Crystal, DSDM, FDD and hybrid planning templates
4. Roadmaps, releases, milestones, Gantt, capacity and risk registers
5. ITIL 4-aligned incident, problem, change, service request, knowledge, asset/configuration, SLA and continual-improvement records
6. CI/CD pipelines, artifacts, environments, approvals and deployment history
7. Kubernetes/OpenShift workload monitoring and reconciliation boundaries
8. Git provider integration and webhook/event ingestion
9. OpenTelemetry metrics/logs/traces with Prometheus/Grafana adapters
10. Team collaboration, mentions, notifications and optional P2P synchronization
11. Admin/user/role/team/workspace tenancy and audit trail
12. RNN/LLM assistant, project summarization, anomaly detection, prioritization and workflow recommendations
13. Speech-to-text/text-to-speech hooks with locale/voice controls

## Implementations
- `core/cpp` — portable C++20 domain/engine foundation
- `services/python` — FastAPI reference service, ML orchestration and recurrent language engine
- `services/node` — Node API and webhook worker
- `clients/web` — TypeScript web application shell
- `clients/android` — Kotlin Android client
- `clients/ios` — Swift iOS/iPadOS client
- `clients/flutter` — Dart cross-platform client
- `clients/java` — Java desktop/CLI SDK
- `clients/go` — Go automation/agent client
- `clients/rust` — Rust secure agent/CLI
- `deploy` — Docker, Kubernetes and OpenShift deployment boundaries
- `ci` — GitHub Actions and reusable CI/CD examples

## Documentation
- `ARCHITECTURE.md` — system architecture
- `docs/API.md` — API/event contract
- `docs/AGILE_ITIL4.md` — Agile and ITIL 4 workflows
- `docs/OPEN_SOURCE_RESEARCH.md` — open-source references and integration boundaries
- `docs/AI_RNN.md` — original RNN/ML assistant design
- `docs/AI_RNN_LLM.md` — expanded recurrent/LLM architecture and current research references
- `docs/IDENTITY_P2P_VOICE.md` — identity, P2P and voice
- `docs/SECURITY.md` — security model
- `docs/superpowers/specs/2026-09-12-workflow-studio-platform-design.md` — approved design
- `docs/superpowers/plans/2026-09-12-workflow-studio-platform.md` — implementation plan

## Verification status
Run `python -m unittest discover -s services/python/tests -v` from the repository root for the Python unit tests. Full native/mobile/container verification remains the responsibility of the appropriate CI/platform runners.

## License
Original project code: GPL-3.0-or-later. Third-party dependencies retain their own licenses. This project documents and integrates open APIs; it does not copy proprietary source code.
