# Shared Network Module

Repository-wide networking contract for applications that need **client/server**, **server+client (host mode)**, and **peer-to-peer** communication side by side.

## Architecture

```text
Application UI
  ├── Network Center
  │    ├── Offline
  │    ├── Client
  │    ├── Server
  │    ├── Host (server + local client)
  │    └── P2P / Mesh
  └── User Profile
       ├── Nickname
       └── Avatar (built-in or validated local upload)

NetworkSession
  ├── Client transport
  ├── Server transport
  ├── P2P transport
  ├── Peer/session registry
  ├── Presence
  ├── Room/channel routing
  └── Profile exchange
```

The application remains the owner of UI and domain state. The shared module only transports typed messages and connection/session events.

## Modes

- **Client:** connect to one or more configured servers.
- **Server:** listen for clients and optionally expose P2P discovery.
- **Host:** run the server and an in-process client simultaneously so the host participates exactly like another user.
- **P2P:** direct peer sessions when available; a rendezvous/relay may be used only for discovery or NAT traversal.
- **Hybrid:** use a server for room/state authority while allowing permitted peer channels for latency-sensitive or bulk data.

## Transport strategy

1. Native/server applications: QUIC first, TCP/TLS fallback where required.
2. Browser applications: WebRTC data channels for direct P2P and WebSocket/WebTransport for client/server connectivity.
3. libp2p adapters may provide discovery, multiplexing, encrypted peer identity, NAT traversal and relays.

QUIC supplies encrypted multiplexed streams and low-latency connection establishment; WebSocket provides interoperable full-duplex browser/server messaging; WebRTC supplies direct browser P2P data channels. See `PROTOCOL.md` for provenance.

## Profile

Every network participant has a session-local profile:

```json
{
  "nickname": "Player",
  "avatar": {
    "kind": "builtin",
    "id": "default-01"
  }
}
```

Local avatar uploads must be opt-in and validated by the host application. Recommended defaults: PNG/JPEG/WebP, bounded dimensions, bounded file size, decoded-image memory limit, and no executable formats. Avatar bytes are never required for authentication.

## Security invariants

- Never transmit wallet seeds, private keys, passwords, or unrelated secrets.
- Use TLS 1.3/QUIC or WebRTC encryption for network data.
- Validate message type, size, schema and rate before dispatch.
- Treat nicknames and avatars as untrusted remote content.
- Never infer or display a user's exact location from networking metadata.
- Do not persist raw IP addresses in user profiles.
- Server operators can configure authentication, authorization, rate limits and retention.

## Integration

Applications should expose a `Network Center`/`Multiplayer`/`Connect` action from their existing UI rather than launching a separate utility. The same controller should be usable by desktop, mobile and web front ends.
