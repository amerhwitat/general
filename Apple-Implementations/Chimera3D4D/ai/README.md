# Chimera 3D/4D AI engine

The `ai/` layer adds local-first recurrent sequence intelligence to scene, animation, material and motion workflows.

## Features

- bounded recurrent scene memory
- time-series/animation observation
- explainable scene recommendations
- optional PyTorch GRU next-token backend
- future RAG/vector-store boundary for authorized project assets and documentation
- model provenance/confidence boundary
- no automatic destructive scene mutation

## Architecture references

The integration is informed by current open-source AI architecture patterns:

- LangChain — composable LLM application components and integrations: https://github.com/langchain-ai/langchain. citeturn0search2
- LangGraph — stateful workflows, persistence and human-in-the-loop orchestration: https://github.com/langchain-ai/langgraph. citeturn0search0
- LlamaIndex — document/RAG and agent data integration: https://github.com/run-llama/llama_index. citeturn0search1
- Chroma — vector/hybrid/full-text search infrastructure: https://github.com/chroma-core/chroma. citeturn0search3
- Mamba — selective state-space sequence modeling for future long-context experiments: https://github.com/state-spaces/mamba. citeturn1search0turn1search3
- Open WebUI — optional local-model UI reference: https://github.com/open-webui/open-webui. citeturn0search9

No external proprietary source is copied. Optional dependencies remain adapter boundaries.

## 128D integration

The engine may consume the application's optional 128-component semantic state as metadata/context. It does not reinterpret spatial geometry or time as an LLM token dimension; geometry and time remain explicit application state.
