# SEO-Tool

Cross-platform, local-first SEO intelligence and authorized web research suite.

## Scope

SEO-Tool crawls and audits HTTP/HTTPS websites, analyzes technical SEO, content, links, structured data, accessibility and security signals, discovers public related resources, and can use an explicitly configured Tor SOCKS proxy for public/authorized `.onion` targets.

It is designed for owned or explicitly authorized targets. It does not bypass authentication, CAPTCHAs, access controls, rate limits, robots policies, or private services, and it does not enumerate onion space.

## Research-informed features

The architecture incorporates ideas observed in open-source tools such as Open SEO Crawler, Crawlie, NovaCrawl, CrawlObserver and FreeCrawl: concurrent crawling, sitemap analysis, duplicate detection, JavaScript rendering adapters, SEO issue scoring, report export, persistent crawl sessions, graph analysis and agent/MCP integration. These are independent implementations, not copied source.

## Features

- HTTP and HTTPS crawling with redirect tracking.
- Configurable depth, URL/page budget, concurrency and per-host delay.
- robots.txt-aware operation by default.
- Sitemap discovery and coverage analysis.
- Canonical, robots, noindex, hreflang, Open Graph and JSON-LD extraction.
- Titles, descriptions, headings, language, viewport, images and alt-text analysis.
- Internal/external link graph and broken-link detection.
- Duplicate/thin-content heuristics.
- Response/security header inspection.
- Optional JavaScript-rendering adapter.
- Public web search integration.
- Deep research across search results, linked pages, sitemaps and configured sources.
- Authorized onion research through Tor SOCKS.
- Document extraction for HTML, TXT, Markdown, JSON, CSV, XML and downloaded public documents; optional PDF/DOCX adapters.
- User-selected output directory.
- JSON, CSV, Markdown, HTML, XML and JSONL reports.
- Evidence/provenance records for downloaded material.
- Crawl database/session storage.
- Site graph export.
- AgentResearchForge integration.
- MCP-compatible metadata boundary.
- Language-neutral JSONL interface.
- Automation scripts for Linux/macOS, Windows CMD and PowerShell.
- Starter adapters/templates for Python, JavaScript, TypeScript, C, C++, C#, Java, Kotlin, Go, Rust, Swift, Objective-C, PHP, Ruby, Dart, Julia, R, Lua, Bash, PowerShell, SQL, HTML/CSS and WebAssembly.

## Source-code index

All implementation files are explicitly referenced here so the README remains a navigable code citation for the project:

| Area | Source |
|---|---|
| Core crawler/audit engine | [SEO_Tool/core.py](SEO_Tool/core.py) |
| CLI | [SEO_Tool/cli.py](SEO_Tool/cli.py) |
| Local GUI/API | [SEO_Tool/gui.py](SEO_Tool/gui.py) |
| Research/deep-web expansion | [SEO_Tool/research.py](SEO_Tool/research.py) |
| Document extraction | [SEO_Tool/documents.py](SEO_Tool/documents.py) |
| Package metadata | [SEO_Tool/__init__.py](SEO_Tool/__init__.py), [pyproject.toml](pyproject.toml) |
| Language matrix | [languages/manifest.json](languages/manifest.json), [languages/generate_adapters.py](languages/generate_adapters.py) |
| Language documentation | [languages/README.md](languages/README.md) |
| Browser UI | [web/index.html](web/index.html), [web/app.js](web/app.js), [web/style.css](web/style.css), [web/package.json](web/package.json) |
| Automated execution | [scripts/run.sh](scripts/run.sh), [scripts/run.bat](scripts/run.bat), [scripts/run.ps1](scripts/run.ps1) |
| Build automation | [scripts/build.sh](scripts/build.sh), [scripts/build.bat](scripts/build.bat), [scripts/build.ps1](scripts/build.ps1) |
| Regression tests | [tests/test_core.py](tests/test_core.py) |
| CI | [.github/workflows/ci.yml](.github/workflows/ci.yml) |

## Quick start

```bash
python -m pip install -e '.[gui,documents]'
python -m SEO_Tool.cli --url https://example.org --output ./seo-results
python -m SEO_Tool.gui
```

The GUI starts locally and never requires a hosted account.

## Onion research

Configure a local Tor SOCKS proxy and explicitly enable onion targets:

```bash
SEO_TOOL_ALLOW_ONION=1 SEO_TOOL_TOR_PROXY=socks5h://127.0.0.1:9050 python -m SEO_Tool.cli --url http://exampleexample.onion --output ./seo-results
```

Only targets explicitly supplied by the operator are eligible. No onion discovery/enumeration is performed.

## Output

A crawl creates a session directory containing:

- `report.json`
- `pages.csv`
- `issues.csv`
- `links.csv`
- `sitemaps.json`
- `documents/`
- `raw/` when raw capture is enabled
- `site-graph.json`
- `summary.md`
- `summary.html`

Raw downloads are bounded by size and are saved only when enabled.

## Safety

Crawling an arbitrary website can create load and can collect personal or copyrighted material. Use targets you own or are authorized to assess, respect terms and robots policies, use conservative concurrency/delays, and review data-retention requirements. HTTP without TLS is supported for auditing because the protocol itself is part of the audit surface; it is not treated as secure transport.


## Browser-native GUI mode

The `web/` interface now includes a static browser-native HTML audit mode. Paste HTML from a site you own or are authorized to assess to inspect title/description metadata, heading counts, viewport and language declarations, canonical/robots tags, Open Graph and JSON-LD presence, image alt attributes, links, and text length. Export findings as JSON or issue CSV. This mode runs entirely in the browser and does not fetch target pages.

For full multi-page crawling, use the local Python crawler and explicitly configure the local bridge endpoint in the browser GUI. The bridge is optional and remains a local service; GitHub Pages does not execute this Python code. The current browser audit is a useful subset, not feature parity with the Python crawler's robots parsing, crawl graph, sitemap analysis, persistence, document capture, or report generation.

Use only authorized targets, keep robots-aware crawling enabled, and choose conservative crawl limits and delays.


### Connect the hosted browser audit to the local crawler

The hosted SEO Audit Studio can call the local Flask crawler only when the service is running and the portfolio origin is explicitly allowed. The local UI served by Flask remains same-origin and does not require this opt-in. To enable the hosted UI, set:

```bash
SEO_TOOL_CORS_ORIGINS=https://amerhwitat.github.io python3 -m SEO_Tool.gui
```

The CLI entrypoint is also available; use the project's documented startup command if your environment launches the GUI module differently. The service defaults to port 5088. CORS uses exact origins, not a wildcard; only targets you are authorized to audit should be submitted.
