# Cute Web Extractor-Style WebContactCrawler UI Implementation Plan

**Goal:** Rebuild the WebContactCrawler browser interface around the supplied Cute Web Email Extractor layout while adding live progress, scan controls, file import/export, and a local job API.

**Architecture:** Keep the existing Python crawler as the reference engine. Add a small local HTTP server that starts bounded crawler jobs in background threads and exposes JSON polling endpoints; the browser UI consumes those endpoints and can also replay saved JSONL event streams. Keep all crawling public/authorized, same-domain, rate-limited, and robots-aware.

**Tech Stack:** Python 3.11+, standard-library `http.server`, threading, existing WebContactCrawler crawler, HTML/CSS/JavaScript.

**Global Constraints:** Public/authorized resources only; no authentication/CAPTCHA/access-control bypass, anti-bot evasion or SMTP probing; preserve robots/domain/depth/page/byte/time limits; local user-selected output only.

### Task 1 — Local job API
- Create `applications/WebContactCrawler/python/gui_server.py` with `POST /api/scan`, `GET /api/jobs/<id>`, `POST /api/jobs/<id>/cancel`, and `POST /api/import`.
- Use background threads, JSONL progress events, and the existing crawler.
- Add focused tests for validation and event parsing.

### Task 2 — Cute-style UI
- Replace `applications/WebContactCrawler/web/index.html` and add `style.css` and `app.js`.
- Provide three modes: keyword discovery, website extraction, file extraction/import.
- Provide toolbar controls, counters, result grid, filters, validation, save/export, history, help/about, and live progress bars.
- Poll the local job API and support JSONL replay.

### Task 3 — Documentation
- Update `applications/WebContactCrawler/README.md` with source-code citations for every new UI/API file.
- Add `docs/UI.md` documenting layout, API, progress model, and responsible-use boundaries.

### Task 4 — Verification
- Run Python syntax compilation and the complete test suite when execution is available.
- Inspect changed source and README citations.
- Do not claim tests pass without observed execution output.
