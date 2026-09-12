# Chimera Email Extractor

Cross-platform public/authorized-web email discovery and validation application. Consistent extraction, persistence, export, concurrent crawling, keyword/search discovery, and UI contracts are provided for Python/PyQt5, C#/WinForms, Electron/React/Node.js, Java/JavaFX, PHP, Rust, plus native C/C++/ASM build scaffolding.

## Code citation / source index

The following repository paths are the canonical source-of-record implementations for the features described here:

| Component | Canonical source |
|---|---|
| Python extraction | [`core_py/extractor.py`](core_py/extractor.py) |
| Python async crawler | [`core_py/crawler_async.py`](core_py/crawler_async.py) |
| Python search discovery | [`core_py/search_engine.py`](core_py/search_engine.py) |
| Python SQLite/CSV storage | [`utils/storage.py`](utils/storage.py) |
| Python persistence | [`core_py/persistence.py`](core_py/persistence.py) |
| C# extraction | [`core_csharp/Extractor.cs`](core_csharp/Extractor.cs) |
| C# async crawler | [`core_csharp/Crawler.cs`](core_csharp/Crawler.cs) |
| C# SQLite/CSV storage | [`core_csharp/Storage.cs`](core_csharp/Storage.cs) |
| Node.js extraction | [`core_js/extractor.js`](core_js/extractor.js) |
| Node.js concurrent crawler | [`core_js/crawler.js`](core_js/crawler.js) |
| Node.js SQLite/CSV storage | [`core_js/storage.js`](core_js/storage.js) |
| Java extraction | [`core_java/Extractor.java`](core_java/Extractor.java) |
| Java executor crawler | [`core_java/Crawler.java`](core_java/Crawler.java) |
| Java SQLite/CSV storage | [`core_java/Storage.java`](core_java/Storage.java) |
| PHP extraction | [`core_php/extractor.php`](core_php/extractor.php) |
| PHP curl-multi crawler | [`core_php/crawler.php`](core_php/crawler.php) |
| PHP SQLite/CSV storage | [`core_php/storage.php`](core_php/storage.php) |
| Rust extraction | [`core_rust/extractor.rs`](core_rust/extractor.rs) |
| Rust async crawler | [`core_rust/crawler.rs`](core_rust/crawler.rs) |
| Rust SQLite/CSV storage | [`core_rust/storage.rs`](core_rust/storage.rs) |
| PyQt interface | [`ui_pyqt/main.py`](ui_pyqt/main.py) |
| WinForms interface | [`ui_csharp/MainForm.cs`](ui_csharp/MainForm.cs) |
| Electron main process | [`electron/main.js`](electron/main.js) |
| JavaFX interface | [`ui_java/EmailExtractorUI.java`](ui_java/EmailExtractorUI.java) |
| PHP interface | [`ui_php/index.php`](ui_php/index.php) |
| Rust TUI | [`ui_rust/src/main.rs`](ui_rust/src/main.rs) |
| Native C/C++/ASM CMake | [`native/CMakeLists.txt`](native/CMakeLists.txt) |
| Code::Blocks project | [`native/CodeBlocks.EmailExtractor.cbp`](native/CodeBlocks.EmailExtractor.cbp) |
| Visual Studio solution | [`EmailExtractor.sln`](EmailExtractor.sln) |
| Architecture | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| Cross-platform automation | [`scripts/README.md`](scripts/README.md) |
| Contact-list handoff | [`../EmailListManager/`](../EmailListManager/) |
| Shared RNN/LLM contract | [`../shared/ai/README.md`](../shared/ai/README.md) |

These links are maintained as code citations: documentation claims should map back to an implementation, project file, or architecture document in this repository or its shared integration layer.

## RNN/LLM integration

Extraction remains deterministic and provenance-first. Optional AI can rank/classify extracted contacts through the repository-wide `shared/ai` contract. The local RNN-style scorer works without a model server; the LLM adapter is optional and intended for a local Ollama-compatible endpoint. AI output is advisory and must never override consent, suppression, robots or access-control policy.

## Safety boundary

The crawler is intended for authorized/public-web collection. It must not bypass authentication, access-control, robots restrictions, rate limits, CAPTCHA/anti-bot controls, or private data. Configure crawl scope, domain policy, concurrency, and rate limits conservatively.

## Features

- HTTP/HTTPS page fetching with timeouts and response-size limits
- Keyword/domain-focused URL collection
- Pluggable search-provider discovery; official provider APIs are preferred where available
- Email extraction, normalization, deduplication, and provenance
- DNS/MX validation where available
- Concurrent/async crawl loops with bounded worker pools and cancellation hooks
- Page/contact/overall progress telemetry
- Domain allowlist/denylist integration points
- SQLite session persistence with resumable result storage
- CSV export with consistent `Email,Title,Website` schema
- JSON/TSV interoperability and WebContactCrawler import/export compatibility
- Filter/search result grids and native desktop/web interfaces
- EmailListManager interoperability for list/tag/consent/status workflows

## Pipeline

`keywords / URLs → search discovery → domain policy → bounded parallel HTTP/HTTPS fetch → extraction → normalization/deduplication → optional DNS/MX validation → optional AI ranking → SQLite → EmailListManager/human review → CSV/JSON export`

## Citation maintenance rule

Whenever a source file is added, renamed, or materially changes its public responsibility, update this README's **Code citation / source index** and the repository root README. Documentation must identify the actual implementation path rather than citing an abstract feature without a source location.
