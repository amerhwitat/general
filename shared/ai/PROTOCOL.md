# RNN/LLM integration protocol

All participating tools expose the same conceptual operations:

1. `score(text)` — deterministic recurrent state score in `[0,1]`.
2. `generate(prompt)` — optional local LLM generation; disabled unless explicitly enabled.
3. `classify(record)` — advisory classification with provenance retained by the caller.

Recommended environment:
- `CHIMERA_AI_ENABLED=0`
- `CHIMERA_LLM_ENDPOINT=http://127.0.0.1:11434/api/generate`
- `CHIMERA_LLM_MODEL=llama3.2`

The HTTP shape follows Ollama's documented `POST /api/generate` interface with `{model,prompt,stream:false}`. Implementations may use native language HTTP clients or official SDKs. No remote API key is required by the base contract.

AI must not:
- override consent/suppression state;
- bypass robots, authentication or access controls;
- automatically send email;
- discard provenance;
- make irreversible repository mutations without explicit policy/human approval.
