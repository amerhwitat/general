#!/usr/bin/env bash
set -euo pipefail
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[api,documents]'
mkdir -p data/uploads data/artifacts data/builds
printf '%s\n' 'AgentResearchForge setup complete.'
printf '%s\n' 'Set AGENT_SEARCH_URL and AGENT_LIBRARY_PATH before starting deep research.'
