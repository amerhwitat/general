# Shared local RNN/LLM intelligence layer

This directory defines a provider-neutral contract used by the repository's crawling, SEO, contact, research and email-list tools.

## Design
- **RNN-style scorer:** deterministic recurrent state update for lightweight local ranking/classification when no model server is available.
- **LLM adapter:** optional local Ollama-compatible HTTP endpoint (`/api/generate`) for summarization, tagging, segmentation suggestions and semantic normalization.
- **Privacy-first:** disabled by default; no credentials or external model calls are embedded.
- **Provenance:** callers must retain source URLs/record IDs alongside AI-derived fields.
- **Human approval:** AI suggestions do not automatically send mail, delete contacts, or change consent state.

Environment:
`CHIMERA_LLM_ENDPOINT=http://127.0.0.1:11434/api/generate`
`CHIMERA_LLM_MODEL=llama3.2`
`CHIMERA_AI_ENABLED=0`

## Implementations
The shared contract is currently represented directly in the EmailListManager language cores: Python, TypeScript, Go, C++20, C#, Java, Rust and PHP all contain the deterministic recurrent scorer. Python and TypeScript also contain optional local LLM HTTP adapters; the other implementations can adopt the same protocol without changing the data contract.

## Open-source research basis
The LLM boundary follows the documented [Ollama REST API](https://github.com/ollama/ollama/blob/main/docs/api.md). Local-RAG architecture patterns were also reviewed from [local-rag-stack](https://github.com/emilvrana/local-rag-stack). Mailing-list data-model ideas were reviewed from [listmonk](https://listmonk.app/). No third-party source code is copied.
