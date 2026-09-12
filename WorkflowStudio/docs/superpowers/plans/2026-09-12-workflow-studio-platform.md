# Workflow Studio Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn WorkflowStudio into a testable cross-platform project, Agile, ITIL 4, DevOps, observability, collaboration, AI, voice and trusted-P2P platform while preserving provider-neutral boundaries.

**Architecture:** Build shared contracts first, then persistence/auth/API, provider adapters, AI/voice/P2P services, clients, deployment and verification. Keep external systems behind adapters and keep production-changing AI/P2P actions policy-gated.

**Tech Stack:** C++20, Python/FastAPI, Node.js/TypeScript/Express, React/TypeScript, Java, Go, Rust/Axum, Kotlin/Android, Swift/iOS, Dart/Flutter, PostgreSQL/SQLite-compatible persistence, Kubernetes/OpenShift, OpenTelemetry, Prometheus/Grafana, ONNX Runtime/PyTorch/TensorFlow adapters.

**Spec:** `WorkflowStudio/docs/superpowers/specs/2026-09-12-workflow-studio-platform-design.md`

## Global Constraints

- Preserve original-code licensing and use external projects only through documented APIs/adapters or clearly attributed references.
- Kubernetes/OpenShift are deployment/reconciliation targets; they are not treated as CI systems.
- AI may propose production changes but cannot execute them without explicit policy approval.
- P2P requires explicit pairing, signed messages, replay protection, capability negotiation and least privilege.
- Secrets are stored as references, never committed plaintext.
- Native platform builds are only reported as passing when actually run on the required toolchain.
- Shared domain/API/event contracts remain language-neutral.

---

### Task 1: Shared domain and event contracts

**Files:**
- Create: `WorkflowStudio/contracts/schema.json`
- Create: `WorkflowStudio/contracts/events.json`
- Create: `WorkflowStudio/contracts/README.md`
- Create: `WorkflowStudio/domain/agile/workflows.json`
- Create: `WorkflowStudio/domain/itil4/practices.json`

**Interfaces:**
- Produces canonical JSON representations for Project, WorkItem, Sprint, Release, Service, Incident, Problem, Change, Request, SLA, Pipeline, Deployment, Environment, User, Team, Peer, TelemetryEvent, AIInsight and VoiceCommand.
- Event envelope fields: `event_id`, `event_type`, `occurred_at`, `tenant_id`, `actor_id`, `correlation_id`, `payload`, `schema_version`.

- [ ] Write contract fixtures covering one Agile work item, one ITIL incident, one deployment event and one signed-P2P metadata envelope.
- [ ] Validate required fields and enum values with a JSON-schema validator.
- [ ] Document compatibility/versioning rules.
- [ ] Commit the contracts independently.

### Task 2: Persistent backend and API service

**Files:**
- Modify: `WorkflowStudio/services/python/main.py`
- Create: `WorkflowStudio/services/python/storage.py`
- Create: `WorkflowStudio/services/python/auth.py`
- Create: `WorkflowStudio/services/python/api.py`
- Create: `WorkflowStudio/services/python/tests/test_api.py`
- Modify: `WorkflowStudio/services/python/pyproject.toml`

**Interfaces:**
- `Repository` interface with `create`, `get`, `list`, `update`, `delete`.
- REST resources `/api/projects`, `/api/work-items`, `/api/teams`, `/api/services`, `/api/incidents`, `/api/changes`, `/api/pipelines`, `/api/deployments`, `/api/events`.
- Authentication middleware exposes `request.state.actor` and authorization checks roles before mutations.

- [ ] Add failing tests for persistence and authorization boundaries.
- [ ] Implement SQLite-compatible repository with transaction boundaries and optimistic version fields.
- [ ] Implement admin/user roles and project-scoped authorization.
- [ ] Implement API routes using the repository interface.
- [ ] Run Python tests and syntax checks.
- [ ] Commit backend persistence/API work.

### Task 3: Node.js gateway and event bus

**Files:**
- Modify: `WorkflowStudio/services/node/server.mjs`
- Create: `WorkflowStudio/services/node/event-bus.mjs`
- Create: `WorkflowStudio/services/node/auth.mjs`
- Create: `WorkflowStudio/services/node/tests/server.test.mjs`
- Modify: `WorkflowStudio/services/node/package.json`

**Interfaces:**
- `publish(event)` and `subscribe(eventType, handler)` for internal events.
- Gateway forwards API events and WebSocket/SSE-compatible notifications without duplicating domain storage.

- [ ] Add failing health/event/auth tests.
- [ ] Implement event bus and request correlation.
- [ ] Add role-aware middleware and safe event ingestion.
- [ ] Add tests and run Node syntax/test commands.
- [ ] Commit gateway work.

### Task 4: Agile and ITIL workflow engine

**Files:**
- Create: `WorkflowStudio/core/workflow/WorkflowEngine.hpp`
- Create: `WorkflowStudio/core/workflow/WorkflowEngine.cpp`
- Create: `WorkflowStudio/core/workflow/StateMachine.hpp`
- Create: `WorkflowStudio/core/workflow/StateMachine.cpp`
- Create: `WorkflowStudio/core/workflow/tests.cpp`

**Interfaces:**
- `StateMachine::transition(work_item_id, from, to, actor, policy)` returns a transition result containing validation errors and emitted event names.
- Templates load Scrum/Kanban/Scrumban/XP/Lean/Crystal/DSDM/FDD/hybrid and ITIL incident/problem/change/request/release flows.

- [ ] Write failing transition tests for Scrum and ITIL flows.
- [ ] Implement data-driven state machines and policy checks.
- [ ] Emit canonical events for transitions.
- [ ] Compile the C++ unit test target where the environment permits.
- [ ] Commit workflow engine.

### Task 5: DevOps provider adapters

**Files:**
- Create: `WorkflowStudio/integrations/devops/Provider.hpp`
- Create: `WorkflowStudio/integrations/devops/ProviderRegistry.hpp`
- Create: `WorkflowStudio/integrations/devops/KubernetesAdapter.md`
- Create: `WorkflowStudio/integrations/devops/OpenShiftAdapter.md`
- Create: `WorkflowStudio/integrations/devops/ArgoAdapter.md`
- Create: `WorkflowStudio/integrations/devops/TektonAdapter.md`
- Create: `WorkflowStudio/integrations/devops/GitProviders.md`
- Create: `WorkflowStudio/integrations/devops/tests/provider-contracts.json`

**Interfaces:**
- Provider methods: `validate`, `start`, `cancel`, `status`, `logs`, `artifacts`, `deploy`.
- Kubernetes/OpenShift adapters reconcile desired deployment state; CI adapters handle pipeline execution.

- [ ] Define adapter conformance fixtures.
- [ ] Implement provider registry and safe capability discovery.
- [ ] Add Kubernetes/OpenShift/Argo/Tekton integration boundaries.
- [ ] Add GitHub/GitLab/Gitea/Forgejo webhook contracts.
- [ ] Verify adapters do not contain provider-specific credentials.
- [ ] Commit provider layer.

### Task 6: Observability and service-health correlation

**Files:**
- Create: `WorkflowStudio/integrations/observability/OpenTelemetry.md`
- Create: `WorkflowStudio/integrations/observability/TelemetryCorrelator.py`
- Create: `WorkflowStudio/integrations/observability/tests/test_correlator.py`
- Create: `WorkflowStudio/deploy/observability/otel-collector.yaml`
- Create: `WorkflowStudio/deploy/observability/prometheus.yaml`

**Interfaces:**
- `correlate(telemetry_event, deployment, service)` returns normalized service-health evidence and correlation IDs.

- [ ] Write tests for trace/deployment/incident correlation.
- [ ] Implement normalized telemetry envelope handling.
- [ ] Add OTel collector and Prometheus deployment definitions.
- [ ] Run Python tests.
- [ ] Commit observability layer.

### Task 7: AI/RNN and neural-engine integration

**Files:**
- Modify: `WorkflowStudio/services/python/main.py`
- Create: `WorkflowStudio/ai/rnn/SequenceModel.py`
- Create: `WorkflowStudio/ai/rnn/Inference.py`
- Create: `WorkflowStudio/ai/rnn/tests/test_sequence_model.py`
- Create: `WorkflowStudio/ai/chimera/ChimeraNeuralAdapter.hpp`
- Create: `WorkflowStudio/ai/chimera/ChimeraNeuralAdapter.cpp`

**Interfaces:**
- `score_sequence(sequence)` returns `{score, confidence, explanation, model_version}`.
- `forecast(sequence, horizon)` returns predictions with confidence intervals.
- `recommend_change(context)` returns a proposal object only; it cannot execute infrastructure actions.

- [ ] Add deterministic tests for anomaly scoring and policy gating.
- [ ] Implement a lightweight sequence-model interface with ONNX/PyTorch/TensorFlow adapters.
- [ ] Add Chimera neural-engine adapter boundary without coupling WorkflowStudio to private implementation details.
- [ ] Add provenance and confidence fields to AI output.
- [ ] Run tests and static checks.
- [ ] Commit AI layer.

### Task 8: Identity, collaboration and trusted P2P

**Files:**
- Create: `WorkflowStudio/collaboration/identity/IdentityModel.md`
- Create: `WorkflowStudio/collaboration/p2p/PeerProtocol.hpp`
- Create: `WorkflowStudio/collaboration/p2p/PeerProtocol.cpp`
- Create: `WorkflowStudio/collaboration/p2p/TrustStore.py`
- Create: `WorkflowStudio/collaboration/p2p/tests/test_replay.py`
- Create: `WorkflowStudio/collaboration/chat/README.md`

**Interfaces:**
- `PairPeer(peer_identity, capabilities, trust_policy)`.
- `VerifyEnvelope(envelope, peer_key, expected_sequence)`.
- `Reconcile(local_events, remote_events)` returns accepted/rejected/conflict sets.

- [ ] Write failing replay/signature/least-privilege tests.
- [ ] Implement signed envelope metadata and sequence/replay checks using vetted crypto libraries.
- [ ] Implement explicit pairing and capability policies.
- [ ] Add offline queue and deterministic reconciliation model.
- [ ] Document that unsolicited scanning and remote execution are prohibited.
- [ ] Commit P2P/collaboration layer.

### Task 9: Voice and multilingual controls

**Files:**
- Create: `WorkflowStudio/voice/VoiceProvider.md`
- Create: `WorkflowStudio/voice/VoiceCommandSchema.json`
- Modify: `WorkflowStudio/clients/flutter/lib/main.dart`
- Modify: `WorkflowStudio/clients/ios/WorkflowClient.swift`
- Modify: `WorkflowStudio/clients/android/Main.kt`
- Create: `WorkflowStudio/voice/python/voice_router.py`

**Interfaces:**
- Voice command: `{locale, transcript, intent, confidence, parameters}`.
- TTS controls: locale, voice, rate, pitch, volume, output device.

- [ ] Add voice command parsing tests.
- [ ] Implement push-to-talk and platform adapter boundaries.
- [ ] Add local Whisper-compatible STT and Piper/Coqui-compatible TTS documentation/interfaces.
- [ ] Add Arabic/English locale examples and extensible locale registry.
- [ ] Commit voice layer.

### Task 10: Web/desktop/mobile client expansion

**Files:**
- Modify: `WorkflowStudio/clients/web/src/App.tsx`
- Create: `WorkflowStudio/clients/web/src/api.ts`
- Create: `WorkflowStudio/clients/web/src/components/ProjectBoard.tsx`
- Create: `WorkflowStudio/clients/web/src/components/ServiceDesk.tsx`
- Create: `WorkflowStudio/clients/web/src/components/DevOpsDashboard.tsx`
- Create: `WorkflowStudio/clients/desktop/README.md`
- Modify: `WorkflowStudio/clients/android/Main.kt`
- Modify: `WorkflowStudio/clients/ios/WorkflowClient.swift`
- Modify: `WorkflowStudio/clients/flutter/lib/main.dart`

**Interfaces:**
- All clients consume the same REST/event contracts.
- UI modules: Portfolio, Board, Sprint, Roadmap, Service Desk, Pipelines, Deployments, Observability, Team, AI Assistant, Admin and Voice.

- [ ] Add API/client tests for project and work-item flows.
- [ ] Implement responsive web dashboard and event refresh.
- [ ] Implement Android/iOS/Flutter API integration and voice hooks.
- [ ] Define desktop packaging boundary for Windows/macOS/Linux without claiming native build success until tested.
- [ ] Commit clients.

### Task 11: Database, deployment and CI/CD packaging

**Files:**
- Create: `WorkflowStudio/database/schema.sql`
- Create: `WorkflowStudio/database/migrations/001_initial.sql`
- Create: `WorkflowStudio/deploy/docker/Dockerfile.python`
- Create: `WorkflowStudio/deploy/docker/Dockerfile.node`
- Modify: `WorkflowStudio/deploy/kubernetes/base.yaml`
- Create: `WorkflowStudio/deploy/kubernetes/postgres.yaml`
- Create: `WorkflowStudio/deploy/openshift/README.md`
- Modify: `WorkflowStudio/ci/github-actions.yml`

**Interfaces:**
- PostgreSQL is the production persistence target; SQLite remains suitable for local development/tests.
- Deployment manifests consume images and environment-based secret references.

- [ ] Add migration/schema validation tests.
- [ ] Implement database schema and indexes for tenant/project/work-item/service/event data.
- [ ] Add container images and Kubernetes/PostgreSQL manifests.
- [ ] Add CI jobs for Python, Node, C++, Java, Go, Rust and schema validation where runner toolchains exist.
- [ ] Commit deployment/CI packaging.

### Task 12: Documentation, security verification and release readiness

**Files:**
- Modify: `WorkflowStudio/README.md`
- Modify: `WorkflowStudio/ARCHITECTURE.md`
- Modify: `WorkflowStudio/docs/AGILE_ITIL4.md`
- Modify: `WorkflowStudio/docs/OPEN_SOURCE_RESEARCH.md`
- Modify: `WorkflowStudio/docs/AI_RNN.md`
- Modify: `WorkflowStudio/docs/IDENTITY_P2P_VOICE.md`
- Create: `WorkflowStudio/docs/API.md`
- Create: `WorkflowStudio/docs/SECURITY.md`
- Create: `WorkflowStudio/docs/OPERATIONS.md`
- Create: `WorkflowStudio/docs/DEVELOPER_GUIDE.md`
- Create: `WorkflowStudio/tests/smoke/README.md`

**Interfaces:**
- Documentation must describe actual implemented endpoints, configuration, roles, security boundaries and supported adapters.

- [ ] Audit docs for stale claims and placeholders.
- [ ] Run available unit, syntax, schema and compile checks.
- [ ] Run dependency/security checks where supported.
- [ ] Verify no plaintext credentials are present.
- [ ] Update status to distinguish verified builds from platform-specific unverified builds.
- [ ] Commit release-readiness documentation.
