# Shared Network Protocol v1

## Session

A session starts with `hello` and negotiates protocol version, application ID, capabilities and profile.

Message envelope:

```json
{
  "v": 1,
  "type": "chat.message",
  "id": "uuid",
  "room": "main",
  "sender": "peer-id",
  "timestamp": 0,
  "payload": {}
}
```

## Core message types

- `hello` / `welcome`
- `profile.set`
- `presence.join` / `presence.leave`
- `room.join` / `room.leave`
- `chat.message`
- `state.request` / `state.update`
- `peer.offer` / `peer.answer` / `peer.candidate`
- `ping` / `pong`
- `error` / `goodbye`

## Host mode

Host mode creates one server session and one local client session. Domain messages from the local client enter the same routing path as remote clients; there is no privileged local message path.

## P2P coexistence

The session registry can maintain both server connections and direct peer connections. A message has a routing policy such as `server`, `peer`, `broadcast`, or `hybrid`. The application decides which data is safe to send directly.

## Presence and profile

Profiles contain only user-selected presentation data: nickname, avatar reference/hash and optional status. IP addresses and transport endpoints are connection metadata, not profile fields.

## Avatar upload

If built-in avatars are empty, the UI exposes `Upload avatar`. Accept only configured image MIME types, decode the image before use, enforce byte/pixel limits, strip metadata where possible, and generate a normalized application thumbnail. Remote avatars should be rendered from the normalized representation rather than trusted as executable content.

## Suggested transport matrix

| Environment | Client/server | P2P | Primary |
|---|---|---|---|
| Native desktop | QUIC/TLS | QUIC/libp2p | QUIC |
| Native mobile | QUIC/TLS | WebRTC/libp2p | QUIC/WebRTC |
| Browser | WebSocket/WebTransport | WebRTC/libp2p | WebTransport/WebRTC |
| LAN fallback | TCP/TLS | TCP/QUIC | TCP/TLS |

## References

- IETF RFC 9000 (QUIC)
- IETF RFC 6455 (WebSocket)
- IETF RFC 8831 (WebRTC Data Channels)
- libp2p transport and peer-network architecture
