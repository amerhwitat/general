#!/usr/bin/env bash
set -euo pipefail
if [ "${1:-}" != "--approved" ]; then echo 'Refusing to build without explicit --approved'; exit 2; fi
LANGUAGE="${2:?language required}"
PROJECT="${3:?project directory required}"
python -c 'from AgentResearchForge.build.runner import build; import sys; print(build(sys.argv[1], sys.argv[2], approved=True))' "$LANGUAGE" "$PROJECT"
