# Open-source research and integration notes

The architecture was compared with:

1. **Scrapy** — mature asynchronous crawling, selectors, throttling and feed exports. Its current site describes async crawling, polite throttling and CSV/JSON export. https://www.scrapy.org/
2. **EasyCrawler / Email Crawler** — Java GUI pattern for email + arbitrary keyword crawling, configurable replacements for obfuscated addresses, crawl depth and CSV output. https://jasonbroker.github.io/EasyCrawler/
3. **GolamV2** — Go crawler pattern covering email/keyword extraction, dead links, robots.txt, a real-time dashboard and low-memory operation. https://github.com/nobrainghost/golamv2
4. **Python Email Crawler** — keyword-driven search-result crawling with bounded linked-page traversal. https://app.readthedocs.org/projects/python-email-crawler/
5. **OpenCrawler** — multi-crawler, robots-aware, keyword logging and multithreading ideas. https://github.com/merwin-asm/OpenCrawler
6. **TS email scraper** — TypeScript/Crawlee pattern for email extraction from search/domain sources. https://github.com/eneiromatos/TS-email-scraper

Integration decisions: use bounded depth, explicit concurrency and delay, robots-aware scheduling, normalized records, source provenance, keyword evidence and portable CSV/TXT formats. No third-party source code is copied; the implementations in this directory are original.

## Search providers
The Python reference supports a SearXNG-compatible JSON endpoint. Other providers can be added behind the same `search_urls()` interface so API keys remain external configuration rather than repository secrets.
