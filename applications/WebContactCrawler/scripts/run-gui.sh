#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../python"
exec python3 gui_server.py
