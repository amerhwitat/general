# Email List Manager

A new local-first contact-list management tool inspired by open-source mailing-list managers such as listmonk, while keeping the implementation original and focused on **contact data management rather than unsolicited mail delivery**. listmonk demonstrates useful patterns including subscriber/list relationships, segmentation, CSV synchronization and analytics. citeturn0search4turn0search13

## Features
- Contacts, lists, memberships, tags, notes and source provenance.
- Status and consent fields; suppression/deactivation remains explicit.
- CSV import/export and normalized/deduplicated email addresses.
- Lightweight recurrent (RNN-style) local scoring for ranking/classification.
- Optional local Ollama-compatible LLM adapter for conservative labels, summaries and segment suggestions.
- Browser dashboard with local scoring and CSV export.
- Implementations for Python, TypeScript, Go, C++20, C#, Java, Rust and PHP.
- No automatic bulk email sending, credential collection, access-control bypass or private-source harvesting.

## AI contract
AI is disabled by default. Set `CHIMERA_AI_ENABLED=1` and configure `CHIMERA_LLM_ENDPOINT` / `CHIMERA_LLM_MODEL` to use a local Ollama-compatible service. AI output is advisory and must not modify consent or suppression state automatically.

The recurrent scorer is intentionally small and deterministic so every implementation can operate without a model server. It is an integration primitive, not a claim of a trained production neural network.

## Open-source research
The architecture reviewed listmonk's subscriber/list schema and API/CSV synchronization ideas, plus local RAG/Ollama patterns. No third-party source code is copied. citeturn0search4turn0search13turn0search8

## Safety and compliance
Use only contacts you are authorized to manage. Respect consent, suppression, privacy, terms of service and applicable anti-spam/data-protection laws. This tool deliberately does not implement unsolicited bulk delivery.

## Layout
- `python/` reference SQLite manager + local AI adapter
- `typescript/` Node/TypeScript manager
- `go/` Go manager
- `cpp/` C++20 manager
- `csharp/` .NET manager
- `java/` Java manager
- `rust/` Rust manager
- `php/` PHP manager
- `web/` standalone browser UI
- `docs/` architecture and source citations
