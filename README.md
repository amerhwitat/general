# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## AgentResearchForge

`AgentResearchForge/` is the portfolio's new AI research and project-generation workspace. It provides a chat-driven orchestration layer that can combine public web search, imported/local-library document retrieval, public code/API discovery, evidence synthesis and safe multi-language project generation.

The application supports a dependency-light core plus optional SearXNG/search providers, Tor SOCKS access for explicitly authorized/public `.onion` resources, PDF/DOCX/PPTX/EPUB parsers, GitHub repository discovery, OpenAPI metadata registration, RAG/vector/LLM adapters and a language-neutral JSONL protocol. Generated code remains inert until a separately authorized build/execution workflow reviews it.

The design is informed by current agentic retrieval patterns such as MCP-native web research, agentic document RAG, hybrid search and provenance-preserving retrieval. Recent open-source examples include Agent Search, web-retrieval MCP, MCP-RAG and pdf-mcp; these are architectural references rather than copied source.

## AI architecture layer

The portfolio now uses a common local-first RNN/LLM architecture pattern across applications: bounded recurrent state, explicit memory, optional trainable GRU inference, retrieval/vector-store boundaries, explainable recommendations, provenance/confidence and human/policy approval before consequential mutations.

## WebContactCrawler

`applications/WebContactCrawler/` is the portfolio's cross-language public-web contact crawler. It provides bounded keyword-focused crawling, robots-aware scheduling, public email extraction, provenance, deduplication, detailed JSONL progress telemetry, a visual dashboard, and TXT/CSV import/export. The crawler is responsible-use oriented: public/authorized resources only; no authentication/CAPTCHA bypass, anti-bot evasion, credential collection, private-area crawling or SMTP mailbox probing.

## Chimera WorkFlow Studio

`WorkflowStudio/` is the portfolio's cross-platform project, Agile, ITIL 4, DevOps and service-management application foundation with a local-first RNN/LLM assistant.

## Central Apple implementations

`Apple-Implementations/` is the portfolio-wide Apple source tree. Each application has its own subdirectory with Objective-C/Xcode and Flutter iOS/macOS implementations, Apple-specific documentation and build boundaries.

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
