#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../web"
command -v npm >/dev/null 2>&1 || { echo 'npm is required'; exit 1; }
npm ci
npm run build
