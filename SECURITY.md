# Security policy

## Credential and key hygiene

Never commit private keys, seed phrases, passwords, access tokens, cloud credentials or copied production configuration. If a credential is exposed in repository history or an issue, revoke/rotate it immediately and remove the secret from all supported history where possible.

## Network security

- TLS 1.3/QUIC or equivalent encrypted transports for remote application traffic.
- Validate and bound every incoming message.
- Apply authentication and authorization before state-changing operations.
- Rate-limit public endpoints.
- Do not persist raw IP addresses as user-profile data.
- Do not expose exact user location through network metadata.
- Uploaded avatars are treated as untrusted files: allow only configured image formats, enforce byte/pixel limits, decode and normalize before rendering, and strip unnecessary metadata.

## Routing security

Dynamic routing and SDN controllers are privileged infrastructure. Applications must not modify host routing or SDN state unless an explicit OS capability grants it. Control-plane changes require authenticated, authorized and versioned configuration.

## Dependency/provenance

External projects are referenced through provenance and license metadata. Upstream code is not copied merely because it is publicly accessible.

## Reporting

For vulnerabilities, avoid publishing credentials or exploit details in a public issue. Use the repository's private security-reporting mechanism when available.
