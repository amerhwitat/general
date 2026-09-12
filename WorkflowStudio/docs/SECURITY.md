# Security model

## Identity
Users authenticate locally or through OIDC/OAuth2. Administrative roles require MFA when supported by the identity provider.

## Authorization
RBAC is mandatory at organization/project/service boundaries. High-impact operations use explicit policy checks and audit events.

## Secrets
Passwords, API keys, signing keys and cluster credentials are runtime secret references only. Never commit them to source or manifests.

## AI safety
AI outputs are advisory. Production changes require a human/policy approval path. Model output includes confidence and provenance where available.

## P2P safety
Peers must be explicitly paired. Messages use identity, sequence, timestamp, payload hash and signature metadata. Replay, capability and trust checks happen before synchronization. The platform does not provide unsolicited peer scanning or arbitrary remote command execution.

## Transport
Use TLS for client/API traffic and mTLS for trusted service/peer deployments where appropriate. Apply short-lived access tokens, rotating refresh tokens, rate limits, request correlation and audit logging.
