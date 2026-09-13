#!/usr/bin/env bash
set -euo pipefail
if [[ $# -gt 0 ]]; then exec "$@"; fi
if [[ -f /app/package.json ]]; then npm install --omit=dev >/tmp/npm.log 2>&1 || true; npm start 2>/dev/null && exit 0 || true; fi
if [[ -f /app/CMakeLists.txt ]]; then cmake -S /app -B /tmp/build -DCMAKE_BUILD_TYPE=Release && cmake --build /tmp/build -j"$(nproc)"; fi
for f in /app/main.py /app/app.py /app/main.js; do [[ -f "$f" ]] || continue; case "$f" in *.py) exec python3 "$f";; *.js) exec node "$f";; esac; done
[[ -f /app/index.html ]] && exec python3 -m http.server 8000 --directory /app
exec bash
