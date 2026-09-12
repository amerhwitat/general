# WebContactCrawler

Cross-language, responsible public-web crawler and contact extraction application.

## Features
- Seed URLs + keyword-focused crawling.
- robots.txt-aware, rate-limited, bounded crawling.
- HTML links, sitemap and mailto discovery.
- Public email extraction and normalization, including common `[at]` / `[dot]` obfuscation.
- Keyword relevance scoring and provenance for every result.
- Detailed live progress/events, crawl tree and domain statistics.
- Import/export TXT and CSV; JSON session export.
- Deduplication, domain allow/deny lists, depth/page/request budgets.
- Pause/resume/cancel session model.
- Language-neutral JSON contracts for interoperable implementations.

## Responsible use
Only crawl public, authorized resources. The application does not bypass authentication, CAPTCHAs, access controls or anti-bot mechanisms and does not perform SMTP mailbox probing. Respect site terms, robots directives where applicable, rate limits, privacy obligations and anti-spam law.

## Architecture
`core/` contains the language-neutral contract; `python/` is the reference implementation; `typescript/`, `go/`, `rust/`, `cpp/`, `java/`, `csharp/`, `php/`, `ruby/`, `dart/`, `swift/`, `kotlin/`, `scala/`, `perl/`, `lua/`, `bash/` and `powershell/` provide portable CLI/API adapters. `web/` contains the dashboard contract/UI foundation.

## Open-source research incorporated by design
Concepts were reviewed from Scrapy link extraction, xcrawler's concurrent crawl/output model, Frostwork's selector-oriented extraction, Heritrix's extensible crawler architecture, and public-email harvesting projects. No third-party source is copied into this directory; each dependency remains replaceable behind adapters.

## License
GPL-3.0-or-later for original project code. Third-party libraries remain under their own licenses.
