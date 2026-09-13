# Routing, TCP/IP and SDN architecture

The application network layer is transport-neutral. Routing is provided by a common route table and protocol-adapter boundary so applications can use static/local routes without requiring a distributed control plane, while Chimera II OS can progressively add dynamic routing.

## Address families

- IPv4 and IPv6 are first-class.
- Dual-stack is the default for new deployments.
- TCP and UDP are exposed through the OS networking boundary.
- IPv6 Neighbor Discovery, ICMPv6 and IPv4 ARP/ICMP belong to the IP stack, not application code.

## Routing protocols

The capability registry covers:

- Static / connected routes
- RIP / RIPng
- OSPFv2 / OSPFv3
- IS-IS
- BGP-4
- EIGRP compatibility adapter
- Babel
- BFD
- VRRP
- PIM
- OpenFabric
- BGP-LS

FRRouting is used as the external compatibility/reference boundary rather than copied into application repositories. Current FRR documents BGP, RIP, OSPF, IS-IS, BFD, Babel, PIM, OpenFabric, VRRP and alpha EIGRP support; FRR also documents BGP-LS for SDN topology consumers. citeturn0search6turn0search1

## SDN/control interfaces

The adapter registry includes:

- OpenFlow
- P4Runtime
- NETCONF
- RESTCONF
- gNMI
- BGP-LS
- Envoy xDS for application/service routing

Envoy xDS provides gRPC/REST discovery APIs for listeners, routes, clusters and endpoints, allowing static configurations to evolve into dynamic discovery without changing application business logic. citeturn1search3turn1search9

## Static vs dynamic routing

`static` mode is the low-complexity default. `dynamic` mode is enabled only when the host/OS has the corresponding routing engine and policy. Applications must never silently enable routing daemons or modify host routes.

## Service-to-service routing

For application RPCs, prefer persistent HTTP/2/gRPC channels and streaming for long-lived flows. gRPC's current performance guidance recommends channel reuse, keepalive where appropriate, and streaming to avoid repeated connection/RPC setup. citeturn0search5

## Observability

Every network request should carry W3C trace context when supported. OpenTelemetry context propagation correlates trace/span information across process and network boundaries. Logs, metrics and traces should converge through an OpenTelemetry Collector. citeturn0search9turn1search5

## Distributed-system policy

Do not split a function into a network service merely because it can be split. Default to a modular monolith/local process boundary for latency-sensitive or tightly transactional functions. Introduce a service boundary only when independent scaling, isolation, deployment or ownership justifies the network cost.

Use:

- Saga/workflow compensation for cross-service transactions.
- Event sourcing only where audit/replay requirements justify it.
- Service-local data ownership.
- Idempotency keys and monotonic event versions.
- Outbox/inbox processing for reliable event publication.
- Bounded retries with exponential backoff and jitter.
- Circuit breakers and bulkheads for dependency failure.
- Blue/green or canary deployment for incompatible changes.
