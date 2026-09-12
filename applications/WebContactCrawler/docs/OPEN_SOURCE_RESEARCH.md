# Open-source research and adaptation record

The application was designed after reviewing public projects and documentation for crawler/extraction architecture. The implementation uses ideas and adapter boundaries, not copied source, unless a dependency is later added under its compatible license.

| Project | Reference | Useful concept | Integration boundary |
|---|---|---|---|
| Scrapy | https://github.com/scrapy/scrapy | link extraction, CrawlSpider rules, structured feed exports | crawler/link and export adapter |
| xcrawler | https://github.com/cardsurf/xcrawler | bounded multithreaded crawling and output files | concurrency/output contract |
| Frostwork | https://github.com/scrapy/frostwork | selector-oriented fast HTML extraction | optional extraction engine |
| Heritrix | https://github.com/internetarchive/heritrix3 | extensible crawl scheduling and scope | scheduler/plugin model |
| Scrapely | https://github.com/scrapy/scrapely | structured HTML extraction | extraction adapter |
| email-enrich | https://github.com/waterdoog/email-enrich | public email harvesting, provenance and rate limits | contact extraction concepts; SMTP probing excluded |
| Prowl | https://github.com/nettitude/prowl | keyword-oriented discovery | keyword relevance module |

## Design adaptations

1. **Crawl rules:** bounded depth/page/request budgets, same-domain scope and robots-aware checks.
2. **Extraction:** direct `mailto`/HTML email detection plus common public `[at]`/`[dot]` forms.
3. **Relevance:** keyword matching is recorded with each result and a simple score.
4. **Observability:** JSONL events expose fetch/skip/error/page/done events for the visual dashboard.
5. **Interchange:** TXT and CSV import/export use the portable contact schema; provenance is retained in CSV.
6. **Portability:** other language folders expose adapters around the same command/schema contract rather than maintaining incompatible data models.

## Licensing

Before incorporating any third-party source code, verify its current repository license and compatibility with this repository's GPL-3.0-or-later distribution. Third-party source is not copied into this directory.

## Responsible use

Only crawl public, authorized resources. The application does not bypass authentication, CAPTCHAs, access controls or anti-bot mechanisms; it does not collect credentials, crawl private areas or perform SMTP mailbox probing. Respect site terms, applicable robots directives, rate limits, privacy obligations and anti-spam law.
