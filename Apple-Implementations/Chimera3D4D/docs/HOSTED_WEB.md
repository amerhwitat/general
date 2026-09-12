# Hosted Web architecture

The browser editor is designed to run as a static frontend while collaboration services remain separate from rendering.

## Recommended deployment

1. Build `web/` with Vite.
2. Serve the generated static assets from a CDN or static host with HTTPS.
3. Store canonical scene files as OpenUSD/glTF-compatible assets behind authenticated APIs.
4. Use WebSocket/WebRTC channels for live collaboration and presence.
5. Apply optimistic operations with version numbers and deterministic conflict resolution.
6. Keep large binary assets in object storage and stream low-resolution previews to the browser.
7. Integrate Chimera trusted-node/P2P contracts only after authentication, authorization, audit logging and explicit trust establishment are implemented.

No credentials, hosted secrets or production endpoint is embedded in this repository.
