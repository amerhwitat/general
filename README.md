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

## Portfolio relationships

- `ChimeraIIOS` — canonical OS and interoperability contracts.
- `CPU4096` / `CPU4096Simulator` — processor and simulation research.
- `nlp` / `PDFreaderPY` — linguistic and document research.
- `BizX` / `BizXtreme` — application/game tracks.

## Licensing

Original project code is released under GNU GPL v3 or later. Third-party code and assets retain applicable licenses.
