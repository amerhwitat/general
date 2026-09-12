# WebContactCrawler Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Strengthen WebContactCrawler into a portable, testable public-web contact discovery application with reliable import/export, visual progress telemetry, cross-language contracts, and traceable open-source/portfolio references.

**Architecture:** Keep Python as the executable reference engine. Define a language-neutral JSON/schema contract and lightweight adapters for the repository's supported languages. Emit structured JSONL telemetry so the web dashboard can render crawl lifecycle, queue, rate, keyword matches, errors, and completion state without coupling UI to crawler internals.

**Tech Stack:** Python 3, standard-library HTTP/HTML/CSV/JSON tooling, JSON Schema, browser JavaScript/HTML, existing repository language adapters.

**Spec:** `applications/WebContactCrawler/README.md` and this plan.

## Global Constraints

- Crawl only public/authorized resources.
- Respect robots.txt, same-domain scope, request/page/depth/byte/time budgets, and configured delays.
- Do not bypass authentication, CAPTCHAs, access controls or anti-bot mechanisms.
- Do not collect credentials or perform SMTP mailbox probing.
- Normalize and deduplicate public email addresses and preserve provenance.
- Support TXT and CSV import/export.
- Keep cross-language behavior aligned through the shared schema/contract.
- Document third-party inspiration and portfolio references without copying third-party source.

---

### Task 1: Regression tests for extraction and import/export

**Files:**
- Create: `applications/WebContactCrawler/python/tests/test_webcontactcrawler.py`
- Modify: `applications/WebContactCrawler/python/webcontactcrawler.py`

- [ ] Write failing tests for normal/obfuscated email extraction, keyword scoring, TXT import, CSV import, TXT export, CSV export, and deterministic deduplication.
- [ ] Run tests and confirm the expected failures.
- [ ] Implement the smallest production changes required for the tests.
- [ ] Run the complete Python test suite.
- [ ] Commit the tested changes.

### Task 2: Improve crawl telemetry and correctness

**Files:**
- Modify: `applications/WebContactCrawler/python/webcontactcrawler.py`
- Modify: `applications/WebContactCrawler/schema/contact.schema.json`

- [ ] Add explicit counters for fetched pages, discovered URLs, skipped URLs, errors, and unique contacts.
- [ ] Ensure final telemetry reports correct page/contact counts.
- [ ] Include normalized URL and HTTP/content metadata where available without collecting private data.
- [ ] Keep telemetry JSONL-compatible and schema-documented.
- [ ] Run tests.
- [ ] Commit.

### Task 3: Visual progress dashboard

**Files:**
- Modify: `applications/WebContactCrawler/web/index.html`
- Modify: `applications/WebContactCrawler/README.md`

- [ ] Render lifecycle status, progress counters, queue depth, crawl rate, keyword matches, errors and contact totals.
- [ ] Support replay of JSONL events without requiring the crawler to run inside the browser.
- [ ] Document how to launch/use the dashboard.
- [ ] Validate with representative JSONL events.
- [ ] Commit.

### Task 4: Cross-language adapter consistency

**Files:**
- Modify language adapter directories under `applications/WebContactCrawler/` only where behavior/contracts are missing or inconsistent.
- Modify: `applications/WebContactCrawler/schema/contact.schema.json`

- [ ] Make adapters consume the shared contract and delegate complex crawl semantics to the reference engine or implement the same bounded contract.
- [ ] Add import/export format compatibility notes.
- [ ] Avoid claiming support for languages not actually represented in the repository.
- [ ] Run available language-level syntax/build checks.
- [ ] Commit.

### Task 5: Documentation and references

**Files:**
- Modify: `applications/WebContactCrawler/README.md`
- Modify: repository README files that directly document this application.
- Modify/create: `applications/WebContactCrawler/docs/OPEN_SOURCE_RESEARCH.md`
- Modify/create: `applications/WebContactCrawler/docs/PORTFOLIO_REFERENCES.md`

- [ ] Document architecture, responsible-use limits, formats, telemetry and test commands.
- [ ] Cite open-source projects reviewed for architecture, distinguishing inspiration from copied code.
- [ ] Reference relevant code in the user's connected repositories.
- [ ] Record licensing considerations.
- [ ] Commit.

### Task 6: Final verification

**Files:**
- No source changes unless verification reveals a defect.

- [ ] Run Python tests.
- [ ] Run syntax checks for web assets and supported adapters where toolchains exist.
- [ ] Inspect changed-file list and README references.
- [ ] Verify the repository tree contains the complete application under one subdirectory.
- [ ] Report only verified results.
