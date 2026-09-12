# AgentResearchForge Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a local-first, cross-language AI research and project-generation application that searches public web sources and explicitly authorized onion services, retrieves imported/library documents, discovers public code/API metadata, summarizes evidence with provenance, and generates multi-language project artifacts from chat requests.

**Architecture:** Dependency-light contracts sit below pluggable web, onion, document, code, API, RAG, LLM and project-generation providers. Python is the reference implementation; language adapters expose a shared JSONL protocol.

**Global constraints:** public/authorized sources only; no credential theft, private-area crawling, authentication/CAPTCHA bypass, deanonymization, malware deployment or unsolicited network scanning; preserve provenance/license data; generated code is inert until separately reviewed and authorized; external tools require explicit configuration.

**Tasks:**
1. Core contracts/research engine and tests.
2. Local library/document indexing and optional PDF/DOCX/PPTX/EPUB parsers.
3. Public web and explicitly authorized onion adapters with SSRF/private-target policy.
4. Public code/API discovery and safe project manifest generation.
5. Agent orchestration, document upload endpoint and chat UI.
6. Multi-language protocol and language-generation matrix.
7. Documentation, portfolio README integration and verification.
