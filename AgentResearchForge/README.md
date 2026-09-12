# AgentResearchForge

AgentResearchForge is a local-first AI research and project-building workspace. A chat request can combine public web research, imported/local-library document retrieval, public code/API discovery, evidence synthesis, and safe project generation.

## Deep retrieval

- **Web:** configure `AGENT_SEARCH_URL` with a SearXNG-compatible or approved JSON search endpoint.
- **Library:** set `AGENT_LIBRARY_PATH` to recursively index a local library before the API starts.
- **Uploads:** `/documents` imports supported files into the local index.
- **Documents:** TXT, Markdown, HTML, JSON, CSV, XML, YAML and source code are built in; PDF, DOCX and PPTX have optional parsers; EPUB is a documented extension point.
- **Code:** GitHub repository discovery is available without requiring a token for basic public search.
- **APIs:** OpenAPI metadata can be registered without executing discovered operations.
- **Onion:** explicitly authorized/public `.onion` URLs can be fetched through a configured local Tor SOCKS proxy; the application does not enumerate onion space or bypass access controls.
- **Evidence:** results retain URL/source type/provenance/license metadata where available.

## Chat workflow

`request -> plan -> retrieve web/library/documents/code -> rank evidence -> summarize -> optionally generate project manifest -> human review`

Generated projects are returned as artifacts. They are not executed automatically.

## AI backends

The core accepts the portfolio RNN/GRU engine, external LLMs, RAG/vector stores, MCP servers, and agent frameworks through adapters. This keeps the core usable offline and avoids hard-coding provider credentials.

## Languages

The language-neutral protocol covers Python, TypeScript, JavaScript, C, C++, C#, Java, Kotlin, Go, Rust, Swift, Objective-C, PHP, Ruby, Dart, Julia, R, Lua, Bash, PowerShell, SQL, HTML/CSS and WebAssembly. See `languages/manifest.json`.

## Run

```bash
python -m pip install -e '.[api,documents]'
AGENT_LIBRARY_PATH=/path/to/library AGENT_SEARCH_URL=http://localhost:8080/search uvicorn AgentResearchForge.api.app:app --reload
```

Then POST JSON to `/chat` or upload a document to `/documents`. A browser UI is provided in `ui/index.html`.

## Safety

This project is designed for public/authorized research. It intentionally excludes credential collection, private-area crawling, authentication/CAPTCHA bypass, deanonymization, unsolicited network scanning, and automatic execution of generated code. Retrieved content is untrusted data and must never override tool permissions. Review `docs/SECURITY.md` before enabling external tools.
