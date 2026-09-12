# Email Extractor Architecture

## Pipeline

`keywords / URLs -> bounded search-provider discovery -> URL policy filters -> concurrent HTTP/HTTPS fetch -> email extraction -> normalization/deduplication -> optional DNS/MX validation -> optional local RNN/LLM ranking -> SQLite session -> human review -> EmailListManager -> CSV/JSON export`

## Concurrency

The language cores provide bounded concurrency rather than an unbounded `Promise.all`/task fan-out. The default worker count is 8 and should be configurable. Progress callbacks report completed pages and unique contacts without blocking the UI.

## AI boundary

The repository-wide `shared/ai` layer provides a deterministic lightweight recurrent scorer and an optional local Ollama-compatible LLM adapter. AI is disabled by default and remains advisory: it cannot override consent, suppression, robots, access-control or domain policy. Source URL/provenance stays attached to every extracted record.

## Contact management

`EmailListManager/` is the downstream list-management boundary for normalized contacts, list membership, tags, notes, explicit consent/status and suppression. Extraction and discovery do not imply permission to message a contact.

## Search providers

Provider adapters may use official APIs where credentials are available. HTML result-page parsing is an optional adapter and must respect provider terms, rate limits, robots policies where applicable, and HTTP status/error handling. No CAPTCHA, authentication, access-control, paywall, or anti-bot bypass is implemented.

## Safety boundary

The crawler is designed for public or explicitly authorized HTTP/HTTPS collection. Domain allowlists/denylists should be applied before fetches. It does not access private accounts, credentials, restricted datasets, or protected systems.

## Persistence

All implementations target the common `emails(email PRIMARY KEY, title, website)` SQLite shape and CSV columns `Email,Title,Website`. Additional provenance/session tables may be added without breaking the core schema.
