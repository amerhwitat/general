# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## WebContactCrawler

`applications/WebContactCrawler/` is the portfolio's cross-language public-web contact crawler. It provides bounded keyword-focused crawling, robots-aware scheduling, public email extraction, provenance, deduplication, detailed progress telemetry, a visual dashboard, and TXT/CSV import/export. The directory contains the language-neutral JSON contract, reference Python implementation, portable language adapters, web UI, architecture and open-source research records.

The crawler is intentionally responsible-use oriented: public/authorized resources only; no authentication or CAPTCHA bypass, anti-bot evasion, credential collection, private-area crawling or SMTP mailbox probing. Third-party projects are used as architectural references or through documented adapters; proprietary source is not copied.

### WebContactCrawler structure

- `applications/WebContactCrawler/schema/` — portable contact schema.
- `applications/WebContactCrawler/python/` — reference crawler and TXT/CSV helpers.
- `applications/WebContactCrawler/{c,cpp,go,rust,java,csharp,typescript,javascript,php,ruby,dart,swift,kotlin,scala,perl,lua,bash,powershell}/` — language adapters.
- `applications/WebContactCrawler/web/` — visual progress dashboard foundation.
- `applications/WebContactCrawler/docs/` — architecture, open-source research and responsible-use documentation.

## Chimera WorkFlow Studio

`WorkflowStudio/` is the portfolio's cross-platform project, Agile, ITIL 4, DevOps and service-management application foundation. It provides Jira/Azure DevOps-style work tracking, Agile workflow templates, ITIL 4 service records, CI/CD provider boundaries, Kubernetes/OpenShift integration, OpenTelemetry observability, team collaboration, trusted P2P synchronization, voice controls and local-first RNN/ML assistance.

The implementation is deliberately provider-neutral: Kubernetes/OpenShift are deployment and reconciliation targets, while CI execution is delegated to adapters such as Argo Workflows, Tekton, Jenkins or source-control CI. External open-source projects are integrated through documented APIs and adapter boundaries; proprietary source is not copied.

## Central Apple implementations

`Apple-Implementations/` is the portfolio-wide Apple source tree. Each application has its own subdirectory with Objective-C/Xcode and Flutter iOS/macOS implementations, Apple-specific documentation and build boundaries.

## Chimera 3D/4D Studio

`Apple-Implementations/Chimera3D4D/` is the unified 3D/4D digital-content-creation application foundation.

## Chimera 128D

Applications and experiments can model state using the portfolio-wide 128D semantic framework: geometry, time, observer/perspective, light/shadow/material response, events, objects, properties and interaction rules, with extensible perception/cognition/vector dimensions.

## Authenticated P2P

The repository follows the common Chimera P2P contract for opt-in peer identity, capability negotiation, request/response, publish, snapshots and deltas. The protocol excludes unsolicited network scanning, credential/private-key exchange, arbitrary executable transfer and remote command execution.

## Portfolio relationships

- `ChimeraIIOS` — canonical OS and interoperability contracts.
- `CPU4096` / `CPU4096Simulator` — processor and simulation research.
- `nlp` / `PDFreaderPY` — linguistic and document research.
- `keygen` / `test` — Java and host integration tracks.
- `BizX` / `BizXtreme` — application/game tracks.
- `eth-key-check` / `bruteforce` — bounded cryptographic research.

## Licensing

Original project code is released under GNU GPL v3 or later. Third-party code and assets retain applicable licenses.
