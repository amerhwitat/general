# AgentResearchForge

AgentResearchForge is a local-first AI research and project-building workspace. A chat request can combine public web research, imported/local-library document search, public code/API discovery, evidence synthesis, and safe project generation.

## Deep retrieval

- Web: configure a SearXNG-compatible endpoint or another approved search provider.
- Documents/library: index local folders and uploaded files; optional parsers cover PDF, DOCX, PPTX and EPUB.
- Code: use the GitHub/code-search adapter for public repository and API metadata.
- Onion: optionally fetch explicitly authorized/public `.onion` URLs through a local Tor SOCKS proxy. It does not scan onion space or bypass access controls.
- Evidence: every result carries URL/source type/provenance/license metadata where available.

## Chat workflow

`request -> plan -> retrieve web/library/code -> rank evidence -> summarize -> optionally generate project manifest -> human review`

Generated projects are returned as artifacts. They are not executed automatically.

## AI backends

The core accepts the portfolio RNN/GRU engine, external LLMs, RAG/vector stores, MCP servers, and agent frameworks through adapters. This keeps the core usable offline and avoids hard-coding provider credentials.

## Documents

Supported baseline formats include TXT, Markdown, HTML, JSON, CSV, XML, YAML, source code and optional PDF/DOCX/PPTX/EPUB integrations. OCR can be added as an optional parser for scanned material.

## Languages

The language-neutral contract covers Python, TypeScript, JavaScript, C, C++, C#, Java, Kotlin, Go, Rust, Swift, Objective-C, PHP, Ruby, Dart, Julia, R, Lua, Bash, PowerShell, SQL, HTML/CSS and WebAssembly.

## Run

```bash
python -m pip install -e '.[api,documents]'
uvicorn AgentResearchForge.api.app:app --reload
```

Then POST JSON to `/chat` or upload a document to `/documents`. A browser UI is provided in `ui/index.html`.

## Safety

This project is designed for public/authorized research. It intentionally excludes credential collection, private-area crawling, authentication/CAPTCHA bypass, deanonymization, unsolicited network scanning, and automatic execution of generated code. Review `docs/SECURITY.md` before enabling external tools.
