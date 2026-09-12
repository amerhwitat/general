# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## Repository-wide source citation index

Maintained application trees include:
- [AgentResearchForge](AgentResearchForge/)
- [SEO-Tool](SEO-Tool/)
- [WebContactCrawler](applications/WebContactCrawler/)
- [Email Extractor](email_extractor/)
- [EmailKeywordCrawler](EmailKeywordCrawler/)
- [EmailListManager](EmailListManager/)
- [WorkflowStudio](WorkflowStudio/)
- [Apple-Implementations](Apple-Implementations/)
- [mobile](mobile/)
- [kotlin](kotlin/)
- [apple](apple/)
- [web](web/)
- [docs](docs/)
- [shared](shared/)
- [third_party](third_party/)

## Shared Network Module

`shared/network/` is the repository-wide application networking contract. It adds client, server, host (server + local client), P2P and hybrid modes so applications can launch networking from their existing UI. It defines a common session envelope, profile model, nickname/avatar handling, transport-selection policy, host-mode routing invariant and security rules. Native applications can use QUIC/TLS with TCP/TLS fallback; browser applications can use WebRTC plus WebSocket/WebTransport; libp2p is an optional discovery/NAT/relay layer.

Every participating application should expose a Network Center/Multiplayer/Connect action, allow a user-selected nickname and built-in avatar, and provide local avatar upload when built-in choices are unavailable. Avatar files are restricted to validated image formats and bounded dimensions/size.

See [`shared/network/README.md`](shared/network/README.md) and [`shared/network/PROTOCOL.md`](shared/network/PROTOCOL.md).

## EmailListManager

`EmailListManager/` is the new cross-language local-first contact-list manager. It provides normalized/deduplicated contacts, lists and memberships, tags, notes, source provenance, explicit consent/status fields, CSV interoperability, a deterministic lightweight RNN-style scorer and an optional local Ollama-compatible LLM adapter. It deliberately does not implement unsolicited bulk delivery.

## Shared AI layer

`shared/ai/` defines the repository-wide local intelligence contract: deterministic recurrent scoring plus an optional local LLM HTTP adapter. Crawlers, SEO tools, contact extractors, research tools and list management applications can use the same environment-based model configuration while preserving provenance and human approval boundaries.

## EmailKeywordCrawler

`EmailKeywordCrawler/` is the cross-language public/authorized-web keyword-driven email discovery application. It adds bounded search/crawling, robots-aware scheduling, concurrency and delay controls, detailed progress events, keyword matching, email normalization, provenance, TXT/CSV import/export and a static visual dashboard. The reference implementation is Python, with companion Node.js/TypeScript, Go, Java, C++20, Rust, C# and PHP implementations. It can feed normalized contacts into `EmailListManager`.

## Email Extractor

`email_extractor/` is the cross-language public/authorized-web contact discovery application with extraction, title/provenance handling, DNS/MX validation cores, SQLite/CSV/JSON persistence and cross-platform automation.

## AgentResearchForge

`AgentResearchForge/` provides local-first AI research, bounded public-web retrieval, local document retrieval, public code/API research, authorized onion retrieval, evidence synthesis, project generation, artifacts and document export.

## SEO-Tool

`SEO-Tool/` provides bounded HTTP/HTTPS technical SEO auditing, metadata/structured-data analysis, reports, GUI/CLI operation, document capture and an explicitly configured authorized `.onion` research boundary.

## WebContactCrawler

`applications/WebContactCrawler/` provides bounded public-web contact discovery, keyword-focused crawling, robots-aware scheduling, public email extraction, provenance, deduplication, progress telemetry and import/export.

## AI architecture layer

The portfolio uses local-first RNN/LLM patterns with bounded state, explicit memory, retrieval/vector boundaries, provenance/confidence and human/policy approval before consequential mutations.

## Chimera 3D/4D and 128D

`Apple-Implementations/Chimera3D4D/` provides the 3D/4D application foundation. Portfolio applications can use the 128D semantic model spanning geometry, time, observer/perspective, light/material response, events, objects, properties and interaction rules.

## Portfolio relationships

- `ChimeraIIOS` — canonical OS/interoperability repository.
- `CPU4096` / `CPU4096Simulator` — processor/simulation research.
- `nlp` / `PDFreaderPY` — language/document research.
- `BizX` / `BizXtreme` — application/game tracks.

## Licensing

Original project code is released under GNU GPL v3 or later. Third-party code and assets retain applicable licenses.
