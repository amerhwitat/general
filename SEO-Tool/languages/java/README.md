# SEO-Tool Java URL-policy adapter

A concrete Java 17+ implementation of the SEO-Tool JSONL integration boundary. It accepts one JSON object per input line:

```json
{"op":"normalize_url","url":"HTTPS://Example.COM:443/a/../b?q=1#section"}
```

and returns a JSON object with `ok` and `normalized` (or `error`). This component validates/normalizes URLs only; it deliberately does not fetch pages or claim feature parity with the Python crawler.

## Build/test

```sh
mvn test
mvn package
printf '%s\n' '{"op":"normalize_url","url":"https://example.com"}' | mvn -q exec:java
```

Requires JDK 17+, Maven 3.9+, and network access to resolve Jackson/JUnit during first build. Use only on owned or explicitly authorized research targets when integrating with the full crawler.
