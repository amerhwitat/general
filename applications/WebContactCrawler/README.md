# WebContactCrawler

Cross-language, responsible public-web crawler and contact extraction application. The browser interface has been rebuilt in the visual structure of the supplied **Cute Web Email Extractor Advance 1.8.9** reference: desktop-style blue menu, three extraction tabs, keyword/search area, crawl settings, action toolbar, results grid, statistics panel, and live progress bars. The implementation is original and does not copy third-party source code.

## Features
- Seed URLs + keyword-focused, bounded crawling.
- HTTP/HTTPS public and authorized crawling.
- robots.txt-aware, rate-limited, same-domain crawling.
- HTML links and public email extraction, including common `[at]` / `[dot]` obfuscation.
- Keyword relevance scoring and provenance for every result.
- Detailed JSONL progress/events with page, queue, email, error, skip and discovery counters.
- **Cute-style GUI:** search/website/file tabs, toolbar actions, settings strip, result grid and statistics sidebar.
- **Live progress:** overall page progress, queue activity, elapsed time, current URL, pages, emails, errors and queue counters.
- Local background jobs with cooperative cancellation through the GUI API.
- Import TXT/CSV and normalize/deduplicate email addresses.
- Browser-side CSV save/export and result filtering/validation.
- User-defined local output path for crawler results and telemetry.
- Language-neutral JSON contracts and language adapter boundaries.
- Portable CLI plus browser dashboard.

## GUI source-code citation index

| Component | Source |
|---|---|
| Reference crawler | [`python/webcontactcrawler.py`](python/webcontactcrawler.py) |
| GUI/job API | [`python/gui_server.py`](python/gui_server.py) |
| GUI API tests | [`python/tests/test_gui_server.py`](python/tests/test_gui_server.py) |
| Crawler tests | [`python/tests/test_webcontactcrawler.py`](python/tests/test_webcontactcrawler.py) |
| Cute-style interface markup | [`web/index.html`](web/index.html) |
| Cute-style visual theme/layout | [`web/style.css`](web/style.css) |
| Live progress/import/export browser logic | [`web/app.js`](web/app.js) |
| UI architecture | [`docs/UI.md`](docs/UI.md) |
| Open-source research | [`docs/OPEN_SOURCE_RESEARCH.md`](docs/OPEN_SOURCE_RESEARCH.md) |
| Portfolio references | [`docs/PORTFOLIO_REFERENCES.md`](docs/PORTFOLIO_REFERENCES.md) |
| Portable contact schema | [`schema/contact.schema.json`](schema/contact.schema.json) |

## Quick start — GUI

From `applications/WebContactCrawler/python/`:

```text
python gui_server.py
```

Open the local address printed by the server. Enter a public/authorized URL, optional keywords, crawl depth and page budget, then use **Search Now**. Progress is streamed through JSONL-backed polling and shown in the statistics/progress area.

## Quick start — CLI

```text
python webcontactcrawler.py https://example.org -k research -k contact --max-pages 25 --max-depth 2 --events events.jsonl -o contacts.csv
python webcontactcrawler.py https://example.org -o contacts.txt
python -m unittest discover -s tests -v
```

## Three interface modes

1. **Email Addresses from Search Engine Via Keywords** — keyword-oriented workflow using a supplied public/authorized seed URL. The current reference implementation uses the seed URL as the crawl boundary; it does not scrape search-engine accounts or bypass search-provider controls.
2. **Extract Email Addresses from Websites** — bounded same-domain website crawl.
3. **Extract Email Addresses from Files** — local TXT/CSV import and normalization.

## Progress and saved work

Each GUI crawl writes an events file beside the requested output, for example `emails.events.jsonl`. Events contain timestamp, event type, page count, queue size, email count, error count, discovered URL count, current URL and crawl rate. The GUI uses this stream to update its progress bars and status area. The crawler output is written to the user-selected `.csv` or `.txt` destination.

## Responsible use

Only crawl public, authorized resources. The application does not bypass authentication, CAPTCHAs, access controls or anti-bot mechanisms and does not perform SMTP mailbox probing. Respect site terms, applicable robots directives, rate limits, privacy obligations and anti-spam law.

## Architecture

`schema/` contains portable contracts; `python/` is the executable reference implementation and tests; `python/gui_server.py` provides the local job API; `web/` contains the Cute-style interface and telemetry client; `docs/` contains architecture, research, licensing and UI records; language directories provide portable CLI/build boundaries.

## Language targets

C, C++, Go, Rust, Java, C#, TypeScript, JavaScript, PHP, Ruby, Dart, Swift, Kotlin, Scala, Perl, Lua, Bash and PowerShell are represented by adapter/build boundaries. The Python engine remains the reference implementation so every language consumes the same contract rather than silently implementing incompatible semantics.

## Open-source research

Architectural patterns were reviewed from public projects including Scrapy, xcrawler, Frostwork, Heritrix, Scrapely, email-enrich and Prowl. The GUI layout was inspired by the supplied screenshot; no third-party source code is copied into this directory. See [`docs/OPEN_SOURCE_RESEARCH.md`](docs/OPEN_SOURCE_RESEARCH.md) for the research record.

## Portfolio references

- `amerhwitat/general` — integration workspace.
- `amerhwitat/ChimeraIIOS` — OS/interoperability contracts.
- `amerhwitat/nlp` and `amerhwitat/PDFreaderPY` — NLP/document ingestion research.
- `amerhwitat/CPU4096` and `amerhwitat/CPU4096Simulator` — processor/simulation research.
- `amerhwitat/BizX` and `amerhwitat/BizXtreme` — application/game tracks.

## License

GPL-3.0-or-later for original project code. Third-party libraries remain under their own licenses.
