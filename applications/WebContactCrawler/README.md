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

## Complete source-code citation index

| Implementation / component | Source |
|---|---|
| Python reference crawler | [`python/webcontactcrawler.py`](python/webcontactcrawler.py) |
| Python GUI/job API | [`python/gui_server.py`](python/gui_server.py) |
| Python crawler tests | [`python/tests/test_webcontactcrawler.py`](python/tests/test_webcontactcrawler.py) |
| Python GUI tests | [`python/tests/test_gui_server.py`](python/tests/test_gui_server.py) |
| C implementation | [`c/main.c`](c/main.c) |
| C++ implementation | [`cpp/main.cpp`](cpp/main.cpp) |
| C# implementation | [`csharp/Program.cs`](csharp/Program.cs) |
| Go implementation | [`go/main.go`](go/main.go) |
| Rust implementation | [`rust/src/main.rs`](rust/src/main.rs) |
| Java implementation | [`java/WebContactCrawler.java`](java/WebContactCrawler.java) |
| Kotlin implementation | [`kotlin/Main.kt`](kotlin/Main.kt) |
| Scala implementation | [`scala/WebContactCrawler.scala`](scala/WebContactCrawler.scala) |
| Swift implementation | [`swift/WebContactCrawler.swift`](swift/WebContactCrawler.swift) |
| TypeScript implementation | [`typescript/index.ts`](typescript/index.ts) |
| JavaScript implementation | [`javascript/index.js`](javascript/index.js) |
| PHP implementation | [`php/webcontactcrawler.php`](php/webcontactcrawler.php) |
| Ruby implementation | [`ruby/webcontactcrawler.rb`](ruby/webcontactcrawler.rb) |
| Dart implementation | [`dart/bin/webcontactcrawler.dart`](dart/bin/webcontactcrawler.dart) |
| Perl implementation | [`perl/webcontactcrawler.pl`](perl/webcontactcrawler.pl) |
| Lua implementation | [`lua/webcontactcrawler.lua`](lua/webcontactcrawler.lua) |
| Bash implementation | [`bash/webcontactcrawler.sh`](bash/webcontactcrawler.sh) |
| PowerShell implementation | [`powershell/WebContactCrawler.ps1`](powershell/WebContactCrawler.ps1) |
| Portable contact schema | [`schema/contact.schema.json`](schema/contact.schema.json) |
| Browser UI markup | [`web/index.html`](web/index.html) |
| Browser UI theme/layout | [`web/style.css`](web/style.css) |
| Browser progress/import/export logic | [`web/app.js`](web/app.js) |
| GUI architecture | [`docs/UI.md`](docs/UI.md) |
| Open-source research | [`docs/OPEN_SOURCE_RESEARCH.md`](docs/OPEN_SOURCE_RESEARCH.md) |
| Portfolio references | [`docs/PORTFOLIO_REFERENCES.md`](docs/PORTFOLIO_REFERENCES.md) |
| Implementation plan | [`docs/superpowers/plans/2026-09-12-cute-web-extractor-ui.md`](docs/superpowers/plans/2026-09-12-cute-web-extractor-ui.md) |
| Windows GUI launcher | [`scripts/run-gui.bat`](scripts/run-gui.bat) |
| Unix GUI launcher | [`scripts/run-gui.sh`](scripts/run-gui.sh) |
| GitHub Actions verification | [`../../.github/workflows/webcontactcrawler.yml`](../../.github/workflows/webcontactcrawler.yml) |

## Quick start — GUI

From `applications/WebContactCrawler/python/`:

```text
python gui_server.py
```

Or use [`scripts/run-gui.bat`](scripts/run-gui.bat) on Windows or [`scripts/run-gui.sh`](scripts/run-gui.sh) on Unix-like systems. Open the local address printed by the server. Enter a public/authorized URL, optional keywords, crawl depth and page budget, then use **Search Now**. Progress is JSONL-backed and displayed in the statistics/progress area.

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

Each GUI crawl writes an events file beside the requested output, for example `emails.events.jsonl`. Events contain timestamp, event type, page count, queue size, email count, error count, discovered URL count, current URL and crawl rate. Contact events also carry email, source URL, title, score and extraction method, allowing the browser grid to update while the crawl is running. The crawler output is written to the user-selected `.csv` or `.txt` destination.

## UI design mapping

The supplied reference's major regions are retained as an original implementation: top menu, three workflow tabs, engine/keyword controls, crawl settings row, action toolbar, large results grid, right-side statistics, progress area and status bar. See [`docs/UI.md`](docs/UI.md) for the source map and API behavior.

## Verification

GitHub Actions verifies the Python test suite and compiles `webcontactcrawler.py` and `gui_server.py` on changes under this application. The workflow is [`../../.github/workflows/webcontactcrawler.yml`](../../.github/workflows/webcontactcrawler.yml). A repository status with no completed run for the latest commit is not treated as proof of passing tests.

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
