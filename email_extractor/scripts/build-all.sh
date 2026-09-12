#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
run(){ echo "--- $1 ---"; shift; if command -v "$1" >/dev/null 2>&1; then "$@" || echo "WARN: $1 failed"; else echo "WARN: $1 not installed; skipped"; fi; }
if [ -x .venv/bin/python ]; then .venv/bin/python -m compileall core_py utils; else run 'Python compile' python3 -m compileall core_py utils; fi
run 'C# build' dotnet build core_csharp/EmailExtractor.CSharp.csproj -c Release
run 'Java build' mvn -f core_java/pom.xml -DskipTests package
if command -v npm >/dev/null 2>&1 && [ -f ui_js/package.json ]; then (cd ui_js && npm run build) || echo 'WARN: JavaScript build failed'; fi
run 'PHP syntax check' php -l core_php/extractor.php
run 'Rust build' cargo build --manifest-path core_rust/Cargo.toml
run 'CMake configure' cmake -S native -B native/build -DCMAKE_BUILD_TYPE=Release
run 'CMake build' cmake --build native/build --config Release
printf '\nBuild sweep completed.\n'
