#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../../.." && pwd)"
NLP="${ROOT}/../nlp/ThamudicEpiPlatform"
if [[ ! -d "${NLP}" ]]; then echo "Canonical nlp checkout not found: ${NLP}" >&2; exit 2; fi
python3 -m venv "${NLP}/.venv"
"${NLP}/.venv/bin/python" -m pip install -r "${NLP}/server/requirements.txt"
"${NLP}/.venv/bin/python" -m pytest "${NLP}/server/tests" -q
if command -v npm >/dev/null 2>&1; then (cd "${NLP}/web" && npm ci && npm run build); fi
echo "AncientLanguages build/test completed."
