# Architecture

1. **Discovery** — seed URLs and approved search-provider results become a bounded frontier.
2. **Policy** — scope, robots.txt, scheme, domain, depth, page budget, timeout and rate limits are checked before fetch.
3. **Fetch** — HTTP client retrieves public HTML only; content-size limits prevent unbounded downloads.
4. **Extract** — links, titles, visible text and public email patterns are extracted.
5. **Score** — keyword matches attach relevance metadata without inventing contacts.
6. **Deduplicate** — normalized email + provenance records are merged.
7. **Persist** — JSON session data supports pause/resume and reproducibility.
8. **Export** — TXT and CSV contact lists plus richer JSON provenance.
9. **Observe** — progress events expose queue, pages, rate, errors, domains and extracted contacts.

The language implementations follow the same schema so results can move between implementations.
