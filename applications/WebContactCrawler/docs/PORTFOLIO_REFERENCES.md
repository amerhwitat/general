# WebContactCrawler references

## Portfolio code references

This application is maintained in `amerhwitat/general` and is designed to interoperate with the user's broader portfolio without copying unrelated source code.

- `amerhwitat/general` — integration workspace and shared application contracts.
- `amerhwitat/ChimeraIIOS` — OS/interoperability contracts and host-side systems research.
- `amerhwitat/nlp` — NLP, document and language-processing components that can consume exported contact records.
- `amerhwitat/PDFreaderPY` — document ingestion research; useful for future authorized offline contact-list imports.
- `amerhwitat/CPU4096` — processor research; relevant only to future high-throughput local processing experiments.
- `amerhwitat/CPU4096Simulator` — simulation research; not required by the crawler.
- `amerhwitat/BizX` and `amerhwitat/BizXtreme` — application/game repositories; no runtime dependency.
- `amerhwitat/keygen`, `amerhwitat/test`, `amerhwitat/eth-key-check`, `amerhwitat/bruteforce` — security/crypto research; deliberately not used for credential or mailbox probing.

## Open-source projects reviewed

- Scrapy (`scrapy/scrapy`) — crawler lifecycle, link extraction, rules and feed-export architecture.
- xcrawler (`cardsurf/xcrawler`) — bounded concurrency and output-file patterns.
- Frostwork (`scrapy/frostwork`) — fast selector-oriented HTML extraction ideas.
- Heritrix (`internetarchive/heritrix3`) — extensible crawler scheduling and crawl-scope architecture.
- Scrapely (`scrapy/scrapely`) — structured HTML extraction concepts.
- email-enrich (`waterdoog/email-enrich`) — public-email provenance, normalization and rate-limit concepts. Its optional SMTP verification is intentionally **not** adopted.
- Prowl (`nettitude/Prowl`) — keyword-oriented discovery concept.

References are architectural citations, not copied source. Before adding third-party code or dependencies, verify the current license and compatibility with GPL-3.0-or-later.

## Safety boundary

The crawler is intentionally limited to public/authorized resources and bounded workloads. It does not bypass authentication, CAPTCHAs, access controls or anti-bot mechanisms; it does not collect credentials, crawl private areas, or probe SMTP mailboxes. Users remain responsible for site terms, applicable privacy/anti-spam law, and authorization to process contact information.
