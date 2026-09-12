#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
NLP="${ROOT}/../nlp/ThamudicEpiPlatform"
if [[ ! -d "${NLP}" ]]; then echo "Canonical nlp checkout not found: ${NLP}" >&2; exit 2; fi
"${NLP}/scripts/check-dependencies.sh"
. "${NLP}/.venv/bin/activate"
"${NLP}/.venv/bin/python" -m pytest "${NLP}/server/tests" -q
if command -v npm >/dev/null 2>&1; then (cd "${NLP}/web" && npm ci && npm run build); fi
echo "AncientLanguages build/test completed with OCR dependency checks."
