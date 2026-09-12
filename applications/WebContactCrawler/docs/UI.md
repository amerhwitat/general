# WebContactCrawler GUI

The browser interface in `web/` follows the visual hierarchy of the supplied Cute Web Email Extractor reference: blue desktop-style menu, three extraction tabs, keyword/search-engine area, crawl settings strip, icon toolbar, result grid, statistics panel, and a bottom status/progress area.

## Source map

- UI markup: [`web/index.html`](../web/index.html)
- Visual theme/layout: [`web/style.css`](../web/style.css)
- Browser behavior and live polling: [`web/app.js`](../web/app.js)
- Local API/job server: [`python/gui_server.py`](../python/gui_server.py)
- Reference crawler: [`python/webcontactcrawler.py`](../python/webcontactcrawler.py)
- GUI API tests: [`python/tests/test_gui_server.py`](../python/tests/test_gui_server.py)

## Progress model

The crawler emits JSONL events containing pages, queue size, discovered URLs, unique emails, errors and rate. The local GUI server reads the newest event for each job and the browser polls `/api/jobs/<id>` about every 700 ms. The page budget drives the overall progress bar; queue size drives the queue activity bar.

## Modes

1. **Search Engine Via Keywords** — keyword-focused workflow using a supplied public/authorized seed URL and relevance scoring.
2. **Website Extraction** — bounded same-domain crawling from the supplied seed.
3. **Files** — local TXT/CSV import and normalization.

The interface deliberately separates visual similarity from implementation: no Cute Web Extractor source code is copied.

## Local API

Run the server from the Python directory:

```text
python gui_server.py
```

Then open `http://127.0.0.1:5088/`.

`POST /api/scan` starts a local background crawl. `GET /api/jobs/<id>` returns state and the latest telemetry event. `POST /api/jobs/<id>/cancel` requests cooperative cancellation. `POST /api/import` normalizes TXT/CSV email lists.

## Responsible use

Only use the crawler on public resources you are authorized to crawl. The UI does not implement authentication bypass, CAPTCHA solving, anti-bot evasion, private-area crawling, credential collection, or SMTP mailbox probing. Respect robots directives, rate limits, terms, privacy obligations and applicable law.
