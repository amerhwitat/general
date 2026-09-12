# RNN + LLM engine

Workflow Studio now contains a local-first recurrent language/sequence engine at `services/python/rnn_llm_engine.py`.

## Architecture

1. **State layer** — bounded recurrent state and short-term memory.
2. **Semantic layer** — deterministic event encoding and explainable workflow signals.
3. **RNN layer** — optional PyTorch GRU language model (`TorchGRULanguageModel`) for trainable next-token modeling.
4. **Retrieval boundary** — application code can supply authorized project/service documents or events as context.
5. **Agent boundary** — recommendations are advisory; production changes require policy approval.

The implementation intentionally separates the small reference RNN from external foundation models. LangChain is treated as a composable integration layer, LangGraph as the stateful workflow/orchestration reference, LlamaIndex as the document/RAG integration reference, Open WebUI as an optional local model UI, FastAPI as the service boundary, and Chroma as an optional vector-search layer. These projects are not copied into this repository.

## Research references

- LangChain: https://github.com/langchain-ai/langchain — composable LLM application and agent components. citeturn0search2
- LangGraph: https://github.com/langchain-ai/langgraph — durable stateful workflows, memory and human-in-the-loop orchestration. citeturn0search0
- LlamaIndex: https://github.com/run-llama/llama_index — document processing, agents and RAG integrations. citeturn0search1
- Open WebUI: https://github.com/open-webui/open-webui — optional self-hosted model interface. citeturn0search9
- FastAPI: https://github.com/fastapi/fastapi — service/API integration boundary.
- Chroma: https://github.com/chroma-core/chroma — vector, hybrid and full-text search infrastructure. citeturn0search3
- Mamba: https://github.com/state-spaces/mamba — selective state-space sequence modeling and a useful future backend for long-context sequence workloads. citeturn1search0turn1search3

## Safety and governance

Training data must be explicitly authorized. Credentials, private keys, customer data and team communications are not silently collected for training. Model output is advisory and carries provenance/confidence metadata where practical.

## Verification

Run from `services/python`:

```bash
python -m unittest discover -s tests -v
```

The repository's CI/native environments should perform full dependency and platform verification.
