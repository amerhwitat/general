package org.chimera.seo;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

/** JSONL adapter for URL-policy requests; it does not fetch or crawl remote pages. */
public final class JsonlMain {
    private static final ObjectMapper JSON = new ObjectMapper();
    private JsonlMain() {}

    public static void main(String[] args) throws Exception {
        try (var reader = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.isBlank()) continue;
                ObjectNode output = JSON.createObjectNode();
                try {
                    JsonNode request = JSON.readTree(line);
                    String op = request.path("op").asText("");
                    if (!"normalize_url".equals(op)) throw new IllegalArgumentException("unsupported op; expected normalize_url");
                    output.put("ok", true);
                    output.put("normalized", UrlPolicy.normalize(request.path("url").asText(null)));
                } catch (Exception exception) {
                    output.put("ok", false);
                    output.put("error", exception.getMessage() == null ? "invalid request" : exception.getMessage());
                }
                System.out.println(JSON.writeValueAsString(output));
            }
        }
    }
}