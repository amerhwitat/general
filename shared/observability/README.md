# Shared observability and distributed-service policy

## Goals

Prevent the operational complexity of distributed services from becoming the default architecture.

### Default architecture

1. Modular monolith or local process for tightly coupled functions.
2. Shared libraries for pure computation.
3. Separate services only when scaling, security, deployment, ownership or fault isolation requires it.
4. Network boundaries use versioned contracts.

## Telemetry

Use OpenTelemetry for traces, metrics and logs. W3C Trace Context is the default propagation format. The Collector provides a vendor-neutral pipeline for receivers, processors and exporters. citeturn0search9turn1search0turn1search5

Jaeger is a tracing backend/UI option; current Jaeger guidance recommends OpenTelemetry instrumentation rather than the historical Jaeger SDKs. citeturn0search13

## Reliability

- Timeouts on every network dependency.
- Exponential backoff + jitter.
- Circuit breakers and bulkheads.
- Idempotency for retried commands.
- Dead-letter queues for asynchronous failures.
- Health/readiness/liveness endpoints.
- Graceful shutdown and connection draining.
- Bounded queues and memory budgets.

## Data consistency

Each service owns its data. Cross-service workflows use explicit events and Saga-style compensation. ACID transactions remain local to a service boundary whenever possible.

## Latency

- Reuse connections/channels.
- Prefer HTTP/2/gRPC for typed internal RPC.
- Stream long-lived flows.
- Co-locate hot-path components.
- Cache immutable/reference boundary data locally.
- Avoid chatty request graphs.

## Deployment

Use immutable versioned artifacts and compatibility windows. Prefer canary or blue/green rollout for distributed changes. Keep protocol/schema versions backward compatible during rollout.

## Resource controls

Every service declares CPU/memory/file-descriptor/network limits and a maximum concurrency. Tiny stateless jobs may use serverless execution, but only when startup and platform costs are lower than a persistent worker.
