# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## Chimera WorkFlow Studio

`WorkflowStudio/` is the portfolio's cross-platform project, Agile, ITIL 4, DevOps and service-management application foundation. It provides Jira/Azure DevOps-style work tracking, Agile workflow templates, ITIL 4 service records, CI/CD provider boundaries, Kubernetes/OpenShift integration, OpenTelemetry observability, team collaboration, trusted P2P synchronization, voice controls and local-first RNN/ML assistance.

The implementation is deliberately provider-neutral: Kubernetes/OpenShift are deployment and reconciliation targets, while CI execution is delegated to adapters such as Argo Workflows, Tekton, Jenkins or source-control CI. External open-source projects are integrated through documented APIs and adapter boundaries; proprietary source is not copied.

### WorkflowStudio structure

- `WorkflowStudio/contracts/` — versioned domain and event schemas.
- `WorkflowStudio/domain/` — Agile and ITIL 4 catalogs.
- `WorkflowStudio/core/` — portable C++ workflow/domain engine.
- `WorkflowStudio/services/` — Python and Node service foundations.
- `WorkflowStudio/clients/` — Web, Android, iOS, Flutter, Java, Go and Rust clients.
- `WorkflowStudio/ai/` — sequence-model and neural-engine adapter boundaries.
- `WorkflowStudio/collaboration/` — identity, collaboration and trusted P2P protocol.
- `WorkflowStudio/voice/` — multilingual speech-command boundaries.
- `WorkflowStudio/integrations/` — DevOps and observability adapters.
- `WorkflowStudio/database/` — persistence schema.
- `WorkflowStudio/deploy/` — container/Kubernetes/OpenShift deployment boundaries.
- `WorkflowStudio/ci/` and `.github/workflows/workflowstudio.yml` — CI definitions.
- `WorkflowStudio/docs/superpowers/` — approved architecture specification and implementation plan.

## Central Apple implementations

`Apple-Implementations/` is the portfolio-wide Apple source tree. Each application has its own subdirectory with Objective-C/Xcode and Flutter iOS/macOS implementations, Apple-specific documentation and build boundaries. The structure preserves the owning repositories while providing a centralized Apple implementation surface.

## Chimera 3D/4D Studio

`Apple-Implementations/Chimera3D4D/` is the unified 3D/4D digital-content-creation application foundation. It combines a portable C++ scene/geometry core with modeling, sculpting, materials, animation, rigging, motion, rendering, VFX, procedural-node, interchange, Objective-C/Metal, Flutter and Web foundations.

## Chimera 128D

Applications and experiments can model state using the portfolio-wide 128D semantic framework: geometry, time, observer/perspective, light/shadow/material response, events, objects, properties and interaction rules, with extensible perception/cognition/vector dimensions.

## Authenticated P2P

The repository follows the common Chimera P2P contract for opt-in peer identity, capability negotiation, request/response, publish, snapshots and deltas. State is accepted only after local authorization and validation of sequencing, payload integrity and optional signatures. The protocol excludes unsolicited network scanning, credential/private-key exchange, arbitrary executable transfer and remote command execution.

## Portfolio relationships

- `ChimeraIIOS` — canonical OS and interoperability contracts.
- `CPU4096` / `CPU4096Simulator` — processor and simulation research.
- `nlp` / `PDFreaderPY` — linguistic and document research.
- `keygen` / `test` — Java and host integration tracks.
- `BizX` / `BizXtreme` — application/game tracks.
- `eth-key-check` / `bruteforce` — bounded cryptographic research.

## Licensing

Original project code is released under GNU GPL v3 or later. Third-party code and assets retain applicable licenses.
