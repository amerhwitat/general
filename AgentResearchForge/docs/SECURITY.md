# Security and trust model

AgentResearchForge is an evidence and artifact system, not an autonomous exploitation system.

## Network boundaries

Only public HTTP(S) resources and explicitly authorized/public `.onion` services are eligible. Private, loopback, link-local and credential-bearing URLs are rejected by the default policy. Crawling should honor applicable robots, terms, rate limits and authorization.

## Tool boundaries

External agents, MCP servers, APIs and code execution are disabled unless configured. Tool metadata can be discovered and registered without executing the tool. API discovery extracts OpenAPI operations but does not call them automatically.

## Generated code

Generated source is inert text. Builds/tests may be run only by a separately authorized local workflow or sandbox. Secrets are not inserted into generated source.

## Prompt injection

Retrieved web/document content is treated as untrusted data, not instructions. The orchestrator must keep user policy and tool permissions outside retrieved text.

## Dark-web boundary

The onion adapter is intended for lawful public/authorized research and defensive intelligence. It does not provide identity tracing, credential acquisition, marketplace transactions, access-control bypass or broad onion-network enumeration.
