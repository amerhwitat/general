# Containerized version

Build and run:

```bash
docker compose build
docker compose up
```

The stack provides an isolated multi-runtime environment while preserving the native repository applications. Persistent data and logs are stored in named volumes.

Interactive diagnostics:

```bash
docker compose run --rm general-app bash
```
