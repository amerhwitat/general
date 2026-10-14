package org.chimera.seo;

import java.net.IDN;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.Locale;

/** Deterministic HTTP(S) URL validation/normalization for the SEO-Tool JSONL boundary. */
public final class UrlPolicy {
    private UrlPolicy() {}

    public static String normalize(String input) {
        if (input == null || input.isBlank()) throw new IllegalArgumentException("url is required");
        if (input.chars().anyMatch(ch -> ch <= 0x20 || ch == 0x7f))
            throw new IllegalArgumentException("url must not contain whitespace or control characters");
        final URI parsed;
        try { parsed = new URI(input).normalize(); }
        catch (URISyntaxException exception) { throw new IllegalArgumentException("invalid URL syntax", exception); }
        String scheme = parsed.getScheme();
        if (scheme == null || !(scheme.equalsIgnoreCase("http") || scheme.equalsIgnoreCase("https")))
            throw new IllegalArgumentException("only http and https URLs are supported");
        if (parsed.getRawUserInfo() != null) throw new IllegalArgumentException("embedded credentials are not allowed");
        String host = parsed.getHost();
        if (host == null || host.isBlank()) throw new IllegalArgumentException("URL must contain a valid host");
        host = IDN.toASCII(host).toLowerCase(Locale.ROOT);
        int port = parsed.getPort();
        if (port < -1 || port > 65535) throw new IllegalArgumentException("port is out of range");
        if ((scheme.equalsIgnoreCase("http") && port == 80) || (scheme.equalsIgnoreCase("https") && port == 443)) port = -1;
        try {
            URI normalized = new URI(scheme.toLowerCase(Locale.ROOT), null, host, port,
                    parsed.getRawPath() == null || parsed.getRawPath().isEmpty() ? "/" : parsed.getRawPath(),
                    parsed.getRawQuery(), null);
            return normalized.toASCIIString();
        } catch (URISyntaxException exception) {
            throw new IllegalArgumentException("URL could not be normalized", exception);
        }
    }
}