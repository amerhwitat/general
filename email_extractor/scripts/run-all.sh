#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
PY=.venv/bin/python; [ -x "$PY" ] || PY=python3
if [ -f ui_pyqt/main.py ]; then echo 'Starting Python PyQt UI'; "$PY" ui_pyqt/main.py & fi
if [ -d core_java/target/classes ]; then echo 'Starting Java UI'; java -cp core_java/target/classes EmailExtractorUI & fi
if [ -f ui_php/index.php ]; then echo 'Starting PHP server at http://127.0.0.1:8080'; php -S 127.0.0.1:8080 -t ui_php & fi
if [ -f ui_js/package.json ]; then echo 'Starting JavaScript UI'; (cd ui_js && npm run start) & fi
if [ -f ui_rust/Cargo.toml ]; then echo 'Starting Rust UI'; cargo run --manifest-path ui_rust/Cargo.toml & fi
wait
