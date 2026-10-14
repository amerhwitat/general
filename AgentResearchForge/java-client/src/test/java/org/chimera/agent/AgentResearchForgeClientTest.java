package org.chimera.agent;

import com.sun.net.httpserver.HttpServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import java.net.InetSocketAddress;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.atomic.AtomicReference;
import static org.junit.jupiter.api.Assertions.*;

class AgentResearchForgeClientTest {
    private HttpServer server;

    @AfterEach void stopServer() { if (server != null) server.stop(0); }

    @Test void rejectsNonHttpBaseUriAndEmbeddedCredentials() {
        assertThrows(IllegalArgumentException.class, () -> new AgentResearchForgeClient(URI.create("file:///tmp")));
        assertThrows(IllegalArgumentException.class, () -> new AgentResearchForgeClient(URI.create("http://user:pass@localhost")));
    }

    @Test void healthReadsDocumentedApiResponse() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/api/health", exchange -> {
            byte[] body = "{\"ok\":true,\"providers\":[\"library\"]}".getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, body.length);
            exchange.getResponseBody().write(body);
            exchange.close();
        });
        server.start();
        var client = new AgentResearchForgeClient(URI.create("http://127.0.0.1:" + server.getAddress().getPort() + "/api/"));
        var result = client.health();
        assertTrue(result.path("ok").asBoolean());
        assertEquals("library", result.path("providers").get(0).asText());
    }

    @Test void chatUsesSnakeCaseApiContract() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        AtomicReference<String> bodySeen = new AtomicReference<>();
        server.createContext("/chat", exchange -> {
            bodySeen.set(new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8));
            byte[] body = "{\"ok\":true}".getBytes(StandardCharsets.UTF_8);
            exchange.sendResponseHeaders(200, body.length);
            exchange.getResponseBody().write(body);
            exchange.close();
        });
        server.start();
        var client = new AgentResearchForgeClient(URI.create("http://127.0.0.1:" + server.getAddress().getPort()));
        assertTrue(client.chat(AgentResearchForgeClient.ChatRequest.standard("Summarize this public report")).path("ok").asBoolean());
        assertTrue(bodySeen.get().contains("\"deep_search\":true"));
        assertTrue(bodySeen.get().contains("\"onion_urls\":[]"));
    }

    @Test void chatRejectsBlankMessage() {
        assertThrows(IllegalArgumentException.class, () -> AgentResearchForgeClient.ChatRequest.standard(" "));
    }
}