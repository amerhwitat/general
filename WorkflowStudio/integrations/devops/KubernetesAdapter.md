# Kubernetes adapter

The adapter targets the Kubernetes API through a configured service account or external identity. It reconciles desired deployment state and reports rollout status, pods, events and logs. It does not execute arbitrary shell commands and does not treat Kubernetes itself as a CI engine.

Capabilities: deployment/status/logs/events/configuration references. Credentials are injected at runtime and never stored in repository files.