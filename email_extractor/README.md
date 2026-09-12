# Chimera Email Extractor

Cross-platform public/authorized-web email discovery and validation application. Consistent extraction, persistence, export, concurrent crawling, keyword/search discovery, and UI contracts are provided for Python/PyQt5, C#/WinForms, Electron/React/Node.js, Java/JavaFX, PHP, Rust, plus native C/C++/ASM build scaffolding.

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

Typical Windows PowerShell workflow:

```powershell
Set-Location email_extractor
.\scripts\install-all.ps1
.\scripts\build-all.ps1
.\scripts\run-all.ps1
```

Typical Linux/macOS/WSL workflow:

```bash
cd email_extractor
bash scripts/install-all.sh
bash scripts/build-all.sh
bash scripts/run-all.sh
```

## Persistence contract

Every implementation targets the same logical SQLite table:

```sql
CREATE TABLE IF NOT EXISTS emails (
  email TEXT PRIMARY KEY,
  title TEXT,
  website TEXT
);
```

`Save` calls the language-specific storage helper; `Export CSV` writes a properly escaped CSV file. The database is a session store, not a source for bypassing access controls.

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
- `core_php/storage.php` — PHP/Composer-compatible storage module

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

## Result schema

The crawler uses: `email`, `page_title`, `website`, `source_url`, `valid_mx`, and `status`. Persistence additionally maintains the compact SQLite export fields `email`, `title`, and `website`.
