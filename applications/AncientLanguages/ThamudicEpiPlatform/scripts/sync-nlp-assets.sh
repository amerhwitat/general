#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
NLP="${ROOT}/../nlp/ThamudicEpiPlatform"
[[ -d "$NLP" ]] || { echo "Missing canonical nlp checkout: $NLP" >&2; exit 2; }
NLP_SHA="$(git -C "${ROOT}/../nlp" rev-parse HEAD 2>/dev/null || true)"
printf '{"canonical_repository":"amerhwitat/nlp","canonical_sha":"%s","path":"ThamudicEpiPlatform","checked_at":"%s"}\n' "$NLP_SHA" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "${ROOT}/applications/AncientLanguages/ThamudicEpiPlatform/data/sync-status.json"
echo "Canonical nlp revision: ${NLP_SHA:-unknown}"
