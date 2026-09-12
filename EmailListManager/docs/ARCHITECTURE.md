# Architecture

`EmailListManager` is intentionally separate from `email_extractor` and `EmailKeywordCrawler`.

Flow: `import/discovery -> normalize -> deduplicate -> contact -> list membership -> consent/status policy -> optional AI ranking -> export/API`.

AI has two layers: a deterministic recurrent state scorer available in every language, and an optional local LLM HTTP adapter. The LLM is advisory only. Source/provenance fields stay attached to contacts and AI outputs are never authoritative for consent.

Interoperability targets are CSV/JSON and a future REST API. The manager does not send mail; delivery belongs to a separately authorized mail subsystem.
