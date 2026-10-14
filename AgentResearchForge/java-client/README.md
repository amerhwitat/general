# AgentResearchForge Java HTTP client

Java 17+ client for the documented AgentResearchForge `GET /health` and `POST /chat` endpoints. It uses Java's `HttpClient` and Jackson for JSON. The server must be running and configured separately.

## Build and test

```sh
mvn test
mvn package
```

Example:

```java
var client = new AgentResearchForgeClient(java.net.URI.create("http://127.0.0.1:8000/"));
var health = client.health();
var answer = client.chat(AgentResearchForgeClient.ChatRequest.standard("Summarize these public sources"));
```

The client validates its base URL and rejects non-HTTP(S) schemes and embedded credentials. It does not bypass access controls or automatically enable onion access; server-side configuration and authorization policy remain authoritative. This is an API client, not a Java port of the Python agent/retrieval engine.
