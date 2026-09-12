# EmailKeywordCrawler

Cross-language public-web email discovery application for **authorized/publicly accessible websites**. Search is keyword-driven and crawl depth is bounded. The reference implementation is Python; companion implementations provide compatible CLI/data formats.

## Features
- Seed URLs plus optional search-provider discovery (SearXNG-compatible endpoint).
- Keyword scoring/filtering for pages and extracted addresses.
- robots.txt-aware crawling, same-domain defaults, bounded depth, timeout and concurrency controls.
- Email extraction from visible HTML text, `mailto:` links and common obfuscations such as `[at]` / `(at)`.
- Detailed live progress events: queued, fetched, matched, emails, errors, rate limiting and completion.
- TXT and CSV import/export; normalized, deduplicated records with source URL and keyword evidence.
- Optional DNS/MX validation hook (disabled by default).
- No authentication bypass, private-area access, CAPTCHA bypass, or stealth/anti-bot evasion.
- Respects configured rate limits and robots.txt where available.

## Layout
- `python/` — full reference crawler + CLI + terminal progress dashboard.
- `typescript/` — Node.js implementation.
- `go/` — concurrent Go implementation.
- `java/` — Java 17 implementation.
- `cpp/` — C++20 implementation.
- `rust/` — Rust implementation.
- `csharp/` — .NET implementation.
- `php/` — PHP 8 implementation.
- `web/` — browser dashboard/API contract and static UI.
- `scripts/` — dependency installation, build and run sweeps for Windows/POSIX.
- `docs/` — architecture, safety, format and open-source research notes.

## Quick start
```bash
python -m pip install -r python/requirements.txt
python python/main.py --url https://example.org --keyword contact --keyword team --depth 2 --export-csv emails.csv
```

Import an existing list:
```bash
python python/main.py --import-file seeds.txt --keyword contact --export-txt emails.txt --export-csv emails.csv
```

Use a SearXNG-compatible search endpoint:
```bash
python python/main.py --search-endpoint http://localhost:8080/search --query "Jordan software company contact" --keyword contact
```

## Data/ethics boundary
This project is intended for public, authorized web research and contact discovery. Users are responsible for applicable privacy, anti-spam, terms-of-service, copyright, and local law requirements. Do not use it to target private individuals, evade access controls, or conduct unsolicited bulk messaging.

## Research basis
The design borrows architectural ideas from Scrapy's asynchronous crawling and feed-export model, and from open-source email/keyword crawlers that use bounded depth, configurable replacements and multi-threaded fetching. No third-party source code is copied into this directory; adaptations are original implementations. See `docs/RESEARCH.md` for sources and attribution.

## License
GNU GPL v3 or later for original code in this directory. Third-party dependencies retain their own licenses.
