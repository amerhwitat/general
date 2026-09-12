# Architecture

AgentResearchForge combines several evidence channels behind a single query contract:

1. **Chat/Planner** interprets the request and selects sources.
2. **Web provider** performs configurable public-web search.
3. **Onion provider** handles explicitly authorized `.onion` URLs through Tor SOCKS.
4. **Document index** searches imported uploads and local library folders.
5. **Code/API registry** records public repositories and OpenAPI operations.
6. **RAG/LLM adapters** can rank, synthesize and cite evidence.
7. **Project builder** turns descriptions into inert source artifacts.
8. **Human approval** remains the boundary for external tools, builds, writes and execution.

The design is compatible with MCP, SearXNG, vector databases and the portfolio's RNN/GRU engine without making them mandatory dependencies.
