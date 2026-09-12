# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## AI architecture layer

The portfolio now uses a common local-first RNN/LLM architecture pattern across applications: bounded recurrent state, explicit memory, optional trainable GRU inference, retrieval/vector-store boundaries, explainable recommendations, provenance/confidence and human/policy approval before consequential mutations.

The architecture research is informed by LangChain (composable LLM applications), LangGraph (stateful workflows), LlamaIndex (document/RAG integration), Open WebUI (local-model UI), FastAPI (service boundary), Chroma (vector/hybrid search) and Mamba (state-space sequence modeling). These are references and optional integration boundaries, not copied proprietary source. citeturn0search2turn0search0turn0search1turn0search9turn0search3turn1search0

## WebContactCrawler

`applications/WebContactCrawler/` is the portfolio's cross-language public-web contact crawler. It provides bounded keyword-focused crawling, robots-aware scheduling, public email extraction, provenance, deduplication, detailed JSONL progress telemetry, a visual dashboard, and TXT/CSV import/export. The directory contains the language-neutral contact/event schema, executable Python reference implementation, portable language adapters, web UI, architecture and open-source research records.

The crawler is intentionally responsible-use oriented: public/authorized resources only; no authentication or CAPTCHA bypass, anti-bot evasion, credential collection, private-area crawling or SMTP mailbox probing. Third-party projects are used as architectural references or through documented adapters; proprietary source is not copied.

## Chimera WorkFlow Studio

`WorkflowStudio/` is the portfolio's cross-platform project, Agile, ITIL 4, DevOps and service-management application foundation. It provides Jira/Azure DevOps-style work tracking, Agile workflow templates, ITIL 4 service records, CI/CD provider boundaries, Kubernetes/OpenShift integration, OpenTelemetry observability, team collaboration, trusted P2P synchronization, voice controls and a local-first RNN/LLM assistant. The expanded recurrent engine is in `WorkflowStudio/services/python/rnn_llm_engine.py` with tests and architecture documentation in `WorkflowStudio/docs/AI_RNN_LLM.md`.

## Central Apple implementations

`Apple-Implementations/` is the portfolio-wide Apple source tree. Each application has its own subdirectory with Objective-C/Xcode and Flutter iOS/macOS implementations, Apple-specific documentation and build boundaries.

## Chimera 3D/4D Studio

`Apple-Implementations/Chimera3D4D/` is the unified 3D/4D digital-content-creation application foundation. Its `ai/` layer now provides local-first recurrent scene intelligence, optional GRU language modeling, scene/time-series memory and explainable recommendations.

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
