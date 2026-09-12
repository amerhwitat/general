# Open-source research and integration notes

The architecture was compared with:

1. **Scrapy** — mature asynchronous crawling, selectors, throttling and feed exports. Its current site describes async crawling, polite throttling and CSV/JSON export. https://www.scrapy.org/
2. **EasyCrawler / Email Crawler** — Java GUI pattern for email + arbitrary keyword crawling, configurable replacements for obfuscated addresses, crawl depth and CSV output. https://jasonbroker.github.io/EasyCrawler/
3. **GolamV2** — Go crawler pattern covering email/keyword extraction, dead links, robots.txt, a real-time dashboard and low-memory operation. https://github.com/nobrainghost/golamv2
4. **Python Email Crawler** — keyword-driven search-result crawling with bounded linked-page traversal. https://app.readthedocs.org/projects/python-email-crawler/
5. **OpenCrawler** — multi-crawler, robots-aware, keyword logging and multithreading ideas. https://github.com/merwin-asm/OpenCrawler
6. **TS email scraper** — TypeScript/Crawlee pattern for email extraction from search/domain sources. https://github.com/eneiromatos/TS-email-scraper
7. **listmonk** — subscriber/list relationships, segmentation, analytics and API/CSV synchronization informed the downstream `EmailListManager` design. https://listmonk.app/ and https://listmonk.app/docs/external-integration/
8. **Ollama** — local REST LLM boundary used by the shared optional adapter. The integration targets `/api/generate` with `stream:false`; no model weights or third-party source code are copied. https://github.com/ollama/ollama and https://github.com/ollama/ollama/blob/main/docs/api.md

Integration decisions: use bounded depth, explicit concurrency and delay, robots-aware scheduling, normalized records, source provenance, keyword evidence and portable CSV/TXT formats. Discovery outputs can be reviewed and handed to `EmailListManager`. The shared AI layer provides deterministic recurrent scoring and optional local LLM classification while preserving human consent/suppression controls.

## Search providers
The Python reference supports a SearXNG-compatible JSON endpoint. Other providers can be added behind the same `search_urls()` interface so API keys remain external configuration rather than repository secrets.

No third-party source code is copied; the implementations in this directory are original.
