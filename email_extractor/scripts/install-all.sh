#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
run(){ echo "--- $1 ---"; shift; if command -v "$1" >/dev/null 2>&1; then "$@" || echo "WARN: $1 failed"; else echo "WARN: $1 not installed; skipped"; fi; }
command -v python3 >/dev/null 2>&1 || { echo 'Python 3 is required'; exit 1; }
[ -d .venv ] || python3 -m venv .venv
PY=.venv/bin/python
"$PY" -m pip install --upgrade pip setuptools wheel
"$PY" -m pip install -e .
run 'C# restore' dotnet restore core_csharp/EmailExtractor.CSharp.csproj
if command -v npm >/dev/null 2>&1 && [ -f ui_js/package.json ]; then (cd ui_js && npm install); fi
run 'Java dependencies' mvn -f core_java/pom.xml dependency:go-offline
if command -v composer >/dev/null 2>&1 && [ -f core_php/composer.json ]; then composer install --working-dir core_php --no-interaction; fi
run 'Rust dependencies' cargo fetch --manifest-path core_rust/Cargo.toml
run 'CMake availability' cmake --version
printf '\nDependency installation completed for available toolchains.\n'
