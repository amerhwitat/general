# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## AgentResearchForge

`AgentResearchForge/` is the portfolio's AI research and project-generation workspace. It provides chat-driven deep retrieval across public web sources, local libraries/documents and public code/API sources, plus bounded crawling, authorized onion retrieval, evidence synthesis, multi-language project generation, persistent artifact storage and document export.

## SEO-Tool

`SEO-Tool/` is the dedicated technical SEO and authorized deep-web research crawler. It supports HTTP and HTTPS audit targets, bounded crawling, sitemap/link discovery, metadata and structured-data extraction, indexability and canonical analysis, duplicate/thin-content heuristics, security headers, site graphs, persistent SQLite crawl sessions, document capture/extraction and JSON/CSV/Markdown reporting. A local GUI, CLI, Linux/macOS shell, Windows CMD and PowerShell automation are included.

SEO-Tool provides an explicitly enabled Tor SOCKS adapter for public/authorized `.onion` targets. It follows supplied seeds and discovered links rather than enumerating onion space, and never bypasses authentication, CAPTCHA, access controls or rate limits. HTTP is supported deliberately because insecure transport is itself an audit finding.

The design is informed by open-source SEO projects including Open SEO Crawler, Crawlie, NovaCrawl, CrawlObserver and FreeCrawl, whose public feature sets demonstrate useful patterns such as sitemap analysis, concurrent crawling, duplicate detection, JavaScript rendering, issue scoring, export, persistence and agent/MCP interfaces. These projects are references, not copied source.

SEO-Tool has a language-adapter matrix covering Python, JavaScript, TypeScript, C, C++, C#, Java, Kotlin, Go, Rust, Swift, Objective-C, PHP, Ruby, Dart, Julia, R, Lua, Bash, PowerShell, SQL, HTML/CSS and WebAssembly. The stable JSONL interface lets all language tracks share the same audited engine.

## AI architecture layer

The portfolio uses a common local-first RNN/LLM architecture pattern: bounded recurrent state, explicit memory, optional trainable GRU inference, retrieval/vector-store boundaries, explainable recommendations, provenance/confidence and human/policy approval before consequential mutations.

## WebContactCrawler

`applications/WebContactCrawler/` is the portfolio's cross-language public-web contact crawler with bounded keyword-focused crawling, robots-aware scheduling, public email extraction, provenance, deduplication, detailed JSONL progress telemetry, a visual dashboard, and TXT/CSV import/export.

## Chimera WorkFlow Studio

`WorkflowStudio/` is the portfolio's cross-platform project, Agile, ITIL 4, DevOps and service-management application foundation with a local-first RNN/LLM assistant.

## Central Apple implementations

`Apple-Implementations/` is the portfolio-wide Apple source tree with Objective-C/Xcode and Flutter iOS/macOS implementations and Apple-specific build boundaries.

## Chimera 3D/4D Studio

`Apple-Implementations/Chimera3D4D/` is the unified 3D/4D digital-content-creation application foundation with local-first recurrent scene intelligence and optional GRU language modeling.

## Chimera 128D

Applications and experiments can model state using the portfolio-wide 128D semantic framework: geometry, time, observer/perspective, light/shadow/material response, events, objects, properties and interaction rules, with extensible perception/cognition/vector dimensions.

## Source-code citation index

The repository README set now treats source code as the implementation record: every major implementation area has a direct source-tree or source-file reference, while local component READMEs document their own detailed file inventories.

### Core application source

- [AgentResearchForge source](AgentResearchForge/) — `agents/`, `api/`, `api_registry/`, `artifacts/`, `build/`, `code_search/`, `core/`, `crawler/`, `documents/`, `exporters/`, `hosting/`, `languages/`, `project_builder/`, `scripts/`, `tests/`, `ui/`.
- [SEO-Tool source](SEO-Tool/) — `SEO_Tool/`, `languages/`, `scripts/`, `tests/`, `web/`, `pyproject.toml`.
- [WebContactCrawler source](applications/WebContactCrawler/) — `python/`, language adapters, `schema/`, `web/`, `docs/`.
- [WorkflowStudio source](WorkflowStudio/) — `ai/`, `clients/`, `collaboration/`, `contracts/`, `core/`, `database/`, `deploy/`, `domain/`, `integrations/`, `services/`, `tests/`, `voice/`.

### Platform source

- [Chimera mobile source](mobile/) — C++ mobile runtime, package fabric/manager/adapters, ARM64/Android/iOS targets, Aurora web shell, tests and packaging.
- [Apple implementations](Apple-Implementations/) — Flutter and Objective-C application implementations plus the full `Chimera3D4D` native/web source tree.
- [Swift integration](apple/) — Swift package/application boundary and Apple build scripts.
- [Web implementations](web/) — JavaScript and PHP browser/server entry points.
- [Kotlin mobile integration](kotlin/) — Kotlin mobile communication implementation.

### Documentation and provenance

- [Portfolio integration docs](docs/) — ecosystem, mobile, web, library, publication and architecture records.
- [Third-party/upstream records](third_party/) — upstream attribution and source-boundary records.
- [Performance/concurrency notes](PERFORMANCE_CONCURRENCY.md).
- [Linux command source integration](docs/LINUX_COMMANDS_SOURCE_INTEGRATION.md).

### Exact source links for the active flagship applications

- [SEO crawler engine](SEO-Tool/SEO_Tool/core.py)
- [SEO CLI](SEO-Tool/SEO_Tool/cli.py)
- [SEO GUI](SEO-Tool/SEO_Tool/gui.py)
- [SEO research engine](SEO-Tool/SEO_Tool/research.py)
- [SEO document extraction](SEO-Tool/SEO_Tool/documents.py)
- [SEO language manifest](SEO-Tool/languages/manifest.json)
- [WebContactCrawler Python engine](applications/WebContactCrawler/python/webcontactcrawler.py)
- [WebContactCrawler import/export](applications/WebContactCrawler/python/import_export.py)
- [WebContactCrawler contact schema](applications/WebContactCrawler/schema/contact.schema.json)
- [WorkflowStudio Python service](WorkflowStudio/services/python/main.py)
- [WorkflowStudio RNN/LLM engine](WorkflowStudio/services/python/rnn_llm_engine.py)
- [WorkflowStudio C++ workflow core](WorkflowStudio/core/cpp/main.cpp)
- [WorkflowStudio web client](WorkflowStudio/clients/web/src/App.tsx)
- [WorkflowStudio Android client](WorkflowStudio/clients/android/Main.kt)
- [WorkflowStudio iOS client](WorkflowStudio/clients/ios/WorkflowClient.swift)
- [Mobile C++ runtime](mobile/src/runtime.cpp)
- [Mobile package fabric](mobile/src/package_fabric.cpp)
- [Chimera 3D/4D geometry](Apple-Implementations/Chimera3D4D/core/src/geometry.cpp)
- [Chimera 3D/4D scene engine](Apple-Implementations/Chimera3D4D/core/src/scene.cpp)
- [Chimera 3D/4D recurrent AI](Apple-Implementations/Chimera3D4D/ai/rnn_llm_engine.py)

## Portfolio relationships

- `ChimeraIIOS` — canonical OS and interoperability contracts.
- `CPU4096` / `CPU4096Simulator` — processor and simulation research.
- `nlp` / `PDFreaderPY` — linguistic and document research.
- `BizX` / `BizXtreme` — application/game tracks.

## Licensing

Original project code is released under GNU GPL v3 or later. Third-party code and assets retain applicable licenses.
