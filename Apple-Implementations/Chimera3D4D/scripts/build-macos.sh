#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cmake -S "$ROOT" -B "$ROOT/build-macos" -DCMAKE_BUILD_TYPE=Release
cmake --build "$ROOT/build-macos" --parallel
ctest --test-dir "$ROOT/build-macos" --output-on-failure
if command -v xcodegen >/dev/null 2>&1; then (cd "$ROOT/apple" && xcodegen generate); fi
