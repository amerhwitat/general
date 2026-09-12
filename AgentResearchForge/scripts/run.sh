#!/usr/bin/env bash
set -euo pipefail
. .venv/bin/activate
exec uvicorn AgentResearchForge.api.app:app --host "${AGENT_HOST:-127.0.0.1}" --port "${AGENT_PORT:-8000}"
