# Open-source integration research

The design was informed by current public documentation and repositories for:
- OpenProject — GPLv3 project management with classic, agile and hybrid capabilities.
- Plane — AGPL-3.0 Community Edition with projects, wiki/AI, REST API/webhooks and Docker/Kubernetes deployment.
- Kubernetes — declarative workload management and controller/reconciliation model.
- Argo Workflows / Argo CD — Kubernetes-native workflow and GitOps delivery boundaries.
- Tekton — Kubernetes-native CI/CD pipeline primitives.
- OpenTelemetry — common metrics/logs/traces instrumentation boundary.
- Prometheus/Grafana — optional monitoring and dashboard consumers.
- GitHub Actions, GitLab CI, Jenkins, Gitea/Forgejo — provider adapters.
- OpenShift — Kubernetes-compatible platform target; manifests remain standard Kubernetes where possible.

Third-party source code is not copied into this directory. Adapters should use their documented APIs/CRDs, and each dependency keeps its own license.
