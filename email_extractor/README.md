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

These links are maintained as code citations: documentation claims should map back to an implementation, project file, or architecture document in this repository.

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

## Automation

The `scripts/` directory provides one-command dependency installation, build, and run sweeps for Windows and POSIX systems:

- `scripts/install-all.bat`, `build-all.bat`, `run-all.bat` — Windows Command Prompt
- `scripts/install-all.ps1`, `build-all.ps1`, `run-all.ps1` — PowerShell 5+/7+
- `scripts/install-all.sh`, `build-all.sh`, `run-all.sh` — Linux/macOS/WSL shells

Automation detects available toolchains and skips unavailable ones while reporting warnings. It does not silently install OS packages or require administrator privileges. Python uses a local `.venv`; .NET uses NuGet restore; Node uses npm; Java uses Maven; PHP uses Composer when present; Rust uses Cargo; native code uses CMake.

## Pipeline

`keywords / URLs → search discovery → domain policy → bounded parallel HTTP/HTTPS fetch → extraction → normalization/deduplication → optional DNS/MX validation → SQLite → CSV/JSON export`

## Persistence contract

Every implementation targets the same logical SQLite table:

```sql
CREATE TABLE IF NOT EXISTS emails (
  email TEXT PRIMARY KEY,
  title TEXT,
  website TEXT
);
```

`Save` calls the language-specific storage helper; `Export CSV` writes a properly escaped CSV file.

## Automation commands

### Windows CMD

```bat
cd email_extractor
scripts\install-all.bat
scripts\build-all.bat
scripts\run-all.bat
```

### PowerShell

```powershell
Set-Location email_extractor
.\scripts\install-all.ps1
.\scripts\build-all.ps1
.\scripts\run-all.ps1
```

### Linux/macOS/WSL

```bash
cd email_extractor
bash scripts/install-all.sh
bash scripts/build-all.sh
bash scripts/run-all.sh
```

## Project and IDE files

- `EmailExtractor.sln` — Visual Studio solution
- `core_csharp/EmailExtractor.CSharp.csproj` — .NET/Visual Studio
- `native/EmailExtractor.Native.vcxproj` — native Visual Studio C/C++ project
- `native/CMakeLists.txt` — C/C++/ASM-capable CMake project
- `native/CodeBlocks.EmailExtractor.cbp` — Code::Blocks
- `pyproject.toml` — Python/PyCharm/packaging metadata
- `.idea/` — PyCharm/IntelliJ project metadata
- `.vscode/` — Visual Studio Code tasks
- `.project` — Eclipse-compatible project marker
- `core_java/pom.xml` — Maven/IntelliJ/Eclipse Java build
- `core_rust/Cargo.toml` — Cargo/RustRover/VS Code/CLion build
- `core_js/package.json` — Node.js/Electron project metadata

## Layout

- `core_py/` Python extraction, async crawler, search discovery, and SQLite persistence
- `core_csharp/` C# extraction, async crawler, and SQLite persistence
- `core_js/` Node/Electron extraction, bounded crawler, and SQLite persistence
- `core_java/` Java extraction, executor crawler, and SQLite persistence
- `core_php/` PHP extraction, curl-multi crawler, and SQLite persistence
- `core_rust/` Rust extraction, async crawler, and SQLite persistence
- `native/` C/C++/ASM build and IDE scaffolding
- `electron/` Electron main/preload integration
- `ui_pyqt/`, `ui_csharp/`, `ui_js/`, `ui_java/`, `ui_php/`, `ui_rust/` interfaces
- `scripts/` cross-platform automation
- `tests/` cross-language test vectors
- `docs/` architecture and implementation documentation

## Result schema

The crawler uses: `email`, `page_title`, `website`, `source_url`, `valid_mx`, and `status`. Persistence additionally maintains the compact SQLite export fields `email`, `title`, and `website`.

## Citation maintenance rule

Whenever a source file is added, renamed, or materially changes its public responsibility, update this README's **Code citation / source index** and the repository root README. Documentation must identify the actual implementation path rather than citing an abstract feature without a source location.
