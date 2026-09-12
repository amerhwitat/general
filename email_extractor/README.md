# Chimera Email Extractor

Cross-platform public-web email discovery and validation application. The project provides consistent UI and extraction contracts for Python/PyQt5, C#/WinForms, Electron/React/Node.js, Java/JavaFX, PHP, and Rust.

## Safety boundary

The crawler is intended for authorized/public-web collection. It respects configured crawl policies and must not be used to bypass authentication, access-control, robots restrictions, or private data.

## Features

- HTTP/HTTPS page fetching with timeouts and size limits
- Keyword/domain-focused URL collection
- Email extraction and normalization
- Deduplication and provenance (email, title, URL)
- DNS/MX validation where available
- Concurrent crawling with cancellation
- Page/contact/overall progress telemetry
- SQLite session persistence
- CSV/TSV/JSON export
- Import/export interoperability with WebContactCrawler
- Filter/search result grids
- Language-specific native UIs

## Layout

- `core_py/` Python reference extraction and persistence implementation
- `core_csharp/` C# extraction implementation
- `core_js/` Node/Electron extraction implementation
- `core_java/` Java extraction implementation
- `core_php/` PHP extraction implementation
- `core_rust/` Rust extraction implementation
- `ui_pyqt/`, `ui_csharp/`, `ui_js/`, `ui_java/`, `ui_php/`, `ui_rust/` native interfaces
- `tests/` cross-language test vectors

The implementations intentionally use the same result fields: `email`, `page_title`, `website`, `source_url`, `valid_mx`, and `status`.
