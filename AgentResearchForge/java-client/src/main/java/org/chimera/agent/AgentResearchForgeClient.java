package org.chimera.agent;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.List;
import java.util.Objects;

/** Typed Java client for AgentResearchForge's documented local HTTP API. */
public final class AgentResearchForgeClient {
    private static final ObjectMapper JSON = new ObjectMapper();
    private final URI baseUri;
    private final HttpClient http;

    public AgentResearchForgeClient(URI baseUri) {
        this(baseUri, HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(5)).build());
    }

    AgentResearchForgeClient(URI baseUri, HttpClient http) {
        this.baseUri = validateBaseUri(baseUri);
        this.http = Objects.requireNonNull(http, "http");
    }

    public JsonNode health() throws IOException, InterruptedException {
        return send(HttpRequest.newBuilder(endpoint("health")).timeout(Duration.ofSeconds(15)).GET().build());
    }

    public JsonNode chat(ChatRequest request) throws IOException, InterruptedException {
        Objects.requireNonNull(request, "request");
        if (request.message() == null || request.message().isBlank())
            throw new IllegalArgumentException("message must not be blank");
        HttpRequest httpRequest = HttpRequest.newBuilder(endpoint("chat"))
                .timeout(Duration.ofSeconds(60))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(JSON.writeValueAsString(request)))
                .build();
        return send(httpRequest);
    }

    private JsonNode send(HttpRequest request) throws IOException, InterruptedException {
        HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() < 200 || response.statusCode() >= 300)
            throw new IOException("AgentResearchForge API returned HTTP " + response.statusCode());
        return JSON.readTree(response.body());
    }

    private URI endpoint(String path) { return baseUri.resolve(path); }

    private static URI validateBaseUri(URI uri) {
        Objects.requireNonNull(uri, "baseUri");
        String scheme = uri.getScheme();
        if (scheme == null || !(scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https"))
                || uri.getHost() == null || uri.getRawUserInfo() != null
                || uri.getRawQuery() != null || uri.getRawFragment() != null) {
            throw new IllegalArgumentException("baseUri must be an HTTP(S) origin/path without credentials, query, or fragment");
        }
        String text = uri.normalize().toString();
        return URI.create(text.endsWith("/") ? text : text + "/");
    }

    public record ChatRequest(
            String message,
            String language,
            @JsonProperty("deep_search") boolean deepSearch,
            @JsonProperty("onion_urls") List<String> onionUrls) {
        public ChatRequest {
            if (message == null || message.isBlank()) throw new IllegalArgumentException("message must not be blank");
            language = language == null || language.isBlank() ? "python" : language;
            onionUrls = onionUrls == null ? List.of() : List.copyOf(onionUrls);
        }

        public static ChatRequest standard(String message) {
            return new ChatRequest(message, "python", true, List.of());
        }
    }
}