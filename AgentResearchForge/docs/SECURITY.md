# Security and trust model

AgentResearchForge is an evidence and artifact system, not an autonomous exploitation system.

## Deep web

Deep retrieval means federating public search, public APIs/documentation, local libraries and bounded same-site crawling. It does not mean bypassing paywalls, authentication, robots controls, CAPTCHAs or private network boundaries.

## Network boundaries

Only public HTTP(S) resources and explicitly authorized/public `.onion` services are eligible. Private, loopback, link-local and credential-bearing URLs are rejected by the default policy. Crawling should honor applicable robots, terms, rate limits and authorization.

## Dark web / onion services

The onion adapter requires `AGENT_ALLOW_ONION=1` and explicit `.onion` URLs supplied by the user or a configured allowlist. The system may fetch those targets through a local Tor SOCKS proxy, but it does not enumerate onion space, discover hidden services indiscriminately, defeat authentication, deanonymize people, acquire credentials, transact with illicit markets, or bypass access controls.

## Tool boundaries

External agents, MCP servers, APIs and code execution are disabled unless configured. Tool metadata can be discovered and registered without executing the tool. API discovery extracts OpenAPI operations but does not call them automatically.

## Generated code and compiled artifacts

Generated source is inert text. Compilation/building must be an explicit local or sandbox workflow; the application does not silently execute generated programs. Stored artifacts include provenance/metadata and can be archived as ZIP files.

## Hosting

The application can generate deployment manifests and provider-specific commands for free/public hosting platforms. It never creates an account, consumes credentials, or deploys without explicit provider authentication and an explicit deployment action. Free tiers and provider policies change over time, so the UI should treat hosting metadata as advisory.

## Prompt injection

Retrieved web/document content is treated as untrusted data, not instructions. The orchestrator must keep user policy and tool permissions outside retrieved text.
