# WebContactCrawler

Cross-language, responsible public-web crawler and contact extraction application.

## Features
- Seed URLs + keyword-focused, bounded crawling.
- robots.txt-aware, rate-limited, same-domain crawling.
- HTML links and public email extraction, including common `[at]` / `[dot]` obfuscation.
- Keyword relevance scoring and provenance for every result.
- Detailed JSONL progress/events with page, queue, email, error, skip and discovery counters.
- Visual dashboard in `web/` for replaying the JSONL event stream.
- Import/export TXT and CSV; CSV retains source URL, domain, title, keywords, score and method.
- Deduplication, domain scope, depth/page/request budgets and timeout/byte limits.
- Language-neutral JSON contract in `schema/` covering contacts and progress events.
- Pause/resume/cancel integration boundary via session/event contracts.
- Language adapters for the programming languages already represented in this repository.

## Quick start

```text
python webcontactcrawler.py https://example.org -k research -k contact --max-pages 25 --max-depth 2 --events events.jsonl -o contacts.csv
python webcontactcrawler.py https://example.org -o contacts.txt
python -m unittest discover -s tests -v
```

The browser dashboard can replay `events.jsonl` locally. TXT import accepts one address per line; CSV import expects an `email` column. Both normalize case and discard malformed/duplicate addresses.

## Responsible use
Only crawl public, authorized resources. The application does not bypass authentication, CAPTCHAs, access controls or anti-bot mechanisms and does not perform SMTP mailbox probing. Respect site terms, applicable robots directives, rate limits, privacy obligations and anti-spam law.

## Architecture
`schema/` contains the portable contact/event contract; `python/` is the executable reference implementation and test suite; language directories provide portable CLI adapters; `web/` contains the visual telemetry dashboard; `docs/` contains architecture, references, licensing and responsible-use records.

### Language targets
C, C++, Go, Rust, Java, C#, TypeScript, JavaScript, PHP, Ruby, Dart, Swift, Kotlin, Scala, Perl, Lua, Bash and PowerShell are represented by adapter/build boundaries. The Python engine is the reference implementation so every language consumes the same contract rather than silently implementing incompatible semantics.

## Open-source research

Architectural patterns were reviewed from:
- [Scrapy](https://github.com/scrapy/scrapy) — crawling, link extraction and feed/export architecture.
- [xcrawler](https://github.com/cardsurf/xcrawler) — concurrent crawler/output architecture.
- [Frostwork](https://github.com/scrapy/frostwork) — selector-oriented HTML extraction.
- [Heritrix](https://github.com/internetarchive/heritrix3) — crawler scheduling and extensible scope architecture.
- [Scrapely](https://github.com/scrapy/scrapely) — structured HTML extraction.
- [email-enrich](https://github.com/waterdoog/email-enrich) — public-contact provenance and rate limiting; SMTP probing is excluded.
- [Prowl](https://github.com/nettitude/prowl) — keyword-oriented discovery patterns.

No third-party source is copied into this directory. See `docs/OPEN_SOURCE_RESEARCH.md` and `docs/PORTFOLIO_REFERENCES.md` for adaptation and portfolio references.

## Portfolio references

- `amerhwitat/general` — integration workspace.
- `amerhwitat/ChimeraIIOS` — OS/interoperability contracts.
- `amerhwitat/nlp` and `amerhwitat/PDFreaderPY` — NLP/document ingestion research.
- `amerhwitat/CPU4096` and `amerhwitat/CPU4096Simulator` — processor/simulation research.
- `amerhwitat/BizX` and `amerhwitat/BizXtreme` — application/game tracks.
- `amerhwitat/keygen`, `amerhwitat/test`, `amerhwitat/eth-key-check`, `amerhwitat/bruteforce` — security/crypto research, intentionally not used for credential or mailbox probing.

## License
GPL-3.0-or-later for original project code. Third-party libraries remain under their own licenses.
