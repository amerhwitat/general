package org.chimera.seo;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class UrlPolicyTest {
    @Test void normalizesSchemeHostDefaultPortAndFragment() {
        assertEquals("https://example.com/a/../b?q=1".replace("/a/../b", "/b"),
                UrlPolicy.normalize("HTTPS://Example.COM:443/a/../b?q=1#section"));
    }

    @Test void rejectsNonHttpSchemes() {
        assertThrows(IllegalArgumentException.class, () -> UrlPolicy.normalize("file:///etc/passwd"));
        assertThrows(IllegalArgumentException.class, () -> UrlPolicy.normalize("javascript:alert(1)"));
    }

    @Test void rejectsEmbeddedCredentials() {
        assertThrows(IllegalArgumentException.class, () -> UrlPolicy.normalize("https://user:pass@example.com/"));
    }

    @Test void rejectsMalformedAndWhitespaceUrls() {
        assertThrows(IllegalArgumentException.class, () -> UrlPolicy.normalize("https://exa mple.com"));
        assertThrows(IllegalArgumentException.class, () -> UrlPolicy.normalize("not a URL"));
    }

    @Test void addsRootSlashAndPreservesQuery() {
        assertEquals("https://example.com/?a=1", UrlPolicy.normalize("https://example.com?a=1"));
    }
}