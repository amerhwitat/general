# OpenShift adapter

OpenShift is integrated through its Kubernetes-compatible APIs and OpenShift-specific resources where required. The adapter reports deployment/rollout state and observability data and delegates pipeline execution to a CI provider such as Tekton, Argo Workflows, Jenkins, or a source-control CI service.

Runtime credentials are external secret references; no tokens or passwords belong in this repository.