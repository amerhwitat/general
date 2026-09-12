#!/usr/bin/env bash
set -euo pipefail
cmake -S . -B build-macos -DCMAKE_BUILD_TYPE=Release
cmake --build build-macos --parallel
ctest --test-dir build-macos --output-on-failure
if command -v xcodegen >/dev/null 2>&1; then (cd apple && xcodegen generate); fi
