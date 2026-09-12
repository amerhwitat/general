# AgentResearchForge

AgentResearchForge is a local-first AI research and project-building workspace. A chat request can combine deep public-web retrieval, imported/local-library document retrieval, public code/API discovery, bounded same-site crawling, evidence synthesis, artifact storage and safe project generation.

## Deep retrieval

- **Federated web:** configure `AGENT_SEARCH_URL` with a SearXNG-compatible or approved JSON search endpoint.
- **Deep web:** expand each query into multiple research angles and optionally crawl a bounded set of links on explicitly supplied public sites.
- **Library/uploads:** set `AGENT_LIBRARY_PATH` and/or use `/documents` to index local files.
- **Documents:** TXT/Markdown/HTML/JSON/CSV/XML/YAML/source code plus optional PDF/DOCX/PPTX/EPUB parsers; DjVu/OCR can be added as optional adapters.
- **Code:** public GitHub repository discovery and language-neutral project generation.
- **APIs:** OpenAPI metadata can be registered without executing discovered operations.
- **Dark web:** explicitly authorized/public `.onion` URLs can be fetched through a local Tor SOCKS proxy when `AGENT_ALLOW_ONION=1`. The application does not enumerate onion space or bypass access controls.
- **Evidence:** results retain URL/source type/provenance/license metadata where available.

## Source-code citation index

| Area | Source |
|---|---|
| Agent orchestration | [agents/orchestrator.py](agents/orchestrator.py) |
| API service | [api/app.py](api/app.py) |
| API registry | [api_registry/registry.py](api_registry/registry.py) |
| Artifact store | [artifacts/store.py](artifacts/store.py) |
| Build runner | [build/runner.py](build/runner.py) |
| GitHub code discovery | [code_search/github.py](code_search/github.py) |
| Core contracts | [core/contracts.py](core/contracts.py) |
| Research engine | [core/research.py](core/research.py), [core/deep_research.py](core/deep_research.py) |
| Web crawler | [crawler/web.py](crawler/web.py), [crawler/deep_crawl.py](crawler/deep_crawl.py) |
| Crawler policy | [crawler/policy.py](crawler/policy.py) |
| Authorized onion adapter | [crawler/onion.py](crawler/onion.py) |
| Document index | [documents/index.py](documents/index.py) |
| Exporters | [exporters/documents.py](exporters/documents.py) |
| Hosting registry | [hosting/registry.py](hosting/registry.py) |
| Project generator | [project_builder/generator.py](project_builder/generator.py) |
| Language matrix | [languages/manifest.json](languages/manifest.json), [languages/README.md](languages/README.md) |
| Local web UI | [ui/index.html](ui/index.html) |
| Automation | [scripts/](scripts/) |
| Tests | [tests/](tests/) |
| Architecture/security | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/SECURITY.md](docs/SECURITY.md) |
| Package configuration | [pyproject.toml](pyproject.toml) |

## Build, store and export

Generated projects have real starter templates for every language in `languages/manifest.json`. Artifacts are stored under `data/artifacts/`, include an `artifact.json` manifest, and can be archived as ZIP files. Generated code remains inert until a user explicitly chooses a build/test workflow.

Research can be exported through `/export` as Markdown, HTML, TXT, DOCX or PDF. This is designed for saving reports into the user's local environment; the browser client can then download or move those files using normal OS controls.

## Free hosting adapters

The `hosting/` registry documents public/free-tier deployment targets including GitHub Pages, Cloudflare Pages, Vercel, Netlify and Render. Deployment commands are generated as advisory instructions and require the user's own authenticated provider account and explicit deployment action. No credentials are collected or embedded by AgentResearchForge.

## Chat workflow

`request -> query expansion -> web/library/code retrieval -> optional bounded crawl -> optional authorized onion fetch -> evidence ranking -> synthesis -> project generation -> artifact store -> export -> human review`

## AI backends

The core accepts the portfolio RNN/GRU engine, external LLMs, RAG/vector stores, MCP servers, and agent frameworks through adapters. Retrieved content is untrusted data and never receives tool permissions.

## Languages

Python, TypeScript, JavaScript, C, C++, C#, Java, Kotlin, Go, Rust, Swift, Objective-C, PHP, Ruby, Dart, Julia, R, Lua, Bash, PowerShell, SQL, HTML/CSS and WebAssembly. See `languages/manifest.json`.

## Automation

- `scripts/setup.sh` — Linux/macOS setup
- `scripts/setup.bat` — Windows CMD setup
- `scripts/setup.ps1` — PowerShell setup
- `scripts/run.sh`, `run.bat`, `run.ps1` — local API startup

## Run

```bash
python -m pip install -e '.[api,documents,exports]'
export AGENT_LIBRARY_PATH=/path/to/library
export AGENT_SEARCH_URL=http://localhost:8080/search
uvicorn AgentResearchForge.api.app:app --reload
```

Then use `/chat`, `/documents`, and `/export`, or open `ui/index.html` through the local web app.

## Safety

This project is designed for public/authorized research. It intentionally excludes credential collection, private-area crawling, authentication/CAPTCHA bypass, deanonymization, unsolicited network scanning, and automatic execution of generated code. Review `docs/SECURITY.md` before enabling external tools.
