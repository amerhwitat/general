# Open-source research and adaptation record

The application was designed after reviewing public projects and documentation for crawler/extraction architecture. The implementation uses ideas, not copied source, unless a dependency is later added under its compatible license.

| Project | Useful concept | Integration boundary |
|---|---|---|
| Scrapy | link extraction and CrawlSpider-style rules | crawler/link adapter |
| xcrawler | multithreaded crawling and output files | concurrency/output contract |
| Frostwork | selector-oriented fast HTML extraction | optional extraction engine |
| Heritrix | extensible, focused/broad crawl architecture | scheduler/plugin model |
| email-enrich | public email harvesting, provenance, rate limits | public-contact extraction concepts |
| Prowl | keyword-oriented discovery | keyword relevance module |

The attached research material also identifies LangChain, LangGraph, CrewAI, LlamaIndex, Open WebUI, FastAPI and Chroma as useful application building blocks. These are treated as optional integration patterns rather than mandatory dependencies.

## Licensing

Before incorporating any third-party source code, verify its current repository license and compatibility with this repository's GPL-3.0-or-later distribution. The application does not copy source code from the projects above.

## Safety

No CAPTCHA bypass, authentication bypass, anti-bot evasion, credential collection, private-area crawling or SMTP mailbox probing is part of the core design.
