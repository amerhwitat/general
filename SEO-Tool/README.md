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
