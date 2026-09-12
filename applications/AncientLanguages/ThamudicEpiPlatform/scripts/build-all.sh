#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
NLP="${ROOT}/../nlp/ThamudicEpiPlatform"
if [[ ! -d "${NLP}" ]]; then echo "Canonical nlp checkout not found: ${NLP}" >&2; exit 2; fi
"${ROOT}/applications/AncientLanguages/ThamudicEpiPlatform/scripts/sync-nlp-assets.sh"
"${NLP}/scripts/check-dependencies.sh"
"${NLP}/scripts/build-all-languages.sh"
. "${NLP}/.venv/bin/activate"
"${NLP}/.venv/bin/python" -m pytest "${NLP}/server/tests" -q
if command -v npm >/dev/null 2>&1; then (cd "${NLP}/web" && npm install && npm run build); fi
echo "AncientLanguages build/test completed with OCR dependency checks."
