# Distributed deployment profiles

The repositories use a progressive deployment model rather than forcing Kubernetes/service-mesh complexity onto every application.

## Profile A — local / modular monolith

Default for desktop, mobile, CLI and small web tools. One process can contain multiple modules and uses local routing. No service discovery is required.

## Profile B — multi-process host

Use when isolation or independent restart is useful. Processes communicate through loopback IPC, Unix domain sockets/named pipes or persistent local gRPC. Avoid network hops for hot paths.

## Profile C — managed container platform

For services that need independent scaling, choose an operator-managed platform such as EKS, GKE or AKS. Kubernetes manifests must declare CPU/memory limits, readiness/liveness probes, disruption budgets, rollout strategy and network policy.

## Profile D — service mesh

Introduce Envoy/xDS-based traffic management only when routing, mTLS, retries, traffic shifting or observability justify the control plane. Envoy supports static, DNS and xDS-based service discovery, and xDS can dynamically update listeners, routes, clusters and endpoints. citeturn1search4turn1search9

## Deployment invariants

- Immutable versioned artifacts.
- Backward-compatible API/schema versions during rollout.
- Canary or blue/green deployments.
- Graceful connection draining.
- Automated health checks and rollback signals.
- Secrets supplied at runtime, never committed.
- Per-service resource ceilings.
- OpenTelemetry traces/metrics/logs through a Collector where appropriate. citeturn1search5

## Data consistency

Service-local ACID transactions are preferred. Cross-service workflows use idempotent commands, outbox/inbox processing, versioned events and Saga compensation. Event sourcing is optional and reserved for domains that require complete replay/audit history.

## Cost control

Measure actual CPU, memory, network egress and storage before splitting another service. Small stateless workloads may use serverless execution; persistent low-latency workloads generally remain workers/services.
