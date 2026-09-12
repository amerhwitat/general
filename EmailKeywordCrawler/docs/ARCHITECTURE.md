# Architecture

`EmailKeywordCrawler` has a shared conceptual pipeline:

`seed/import/search -> bounded scheduler -> robots policy -> HTTP fetch -> HTML/text extraction -> keyword filter -> email normalization -> deduplication -> provenance -> TXT/CSV export -> progress events`

The Python implementation is the reference behavior. Other language implementations are deliberately small native ports that consume the same URLs and emit compatible data. A future service layer can expose the reference crawler over HTTP/SSE/WebSocket for the visual dashboard.

### Progress event contract
Events use JSON-like fields: `event`, `url`, `depth`, `visited`, `queued`, `emails`, `keywords`, `error`. Clients can render counters, queue depth, current URL, error count and completion state.
