#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
command -v python3 >/dev/null || { echo 'python3 is required'; exit 1; }
python3 -m venv "$ROOT/.venv"
. "$ROOT/.venv/bin/activate"
python -m pip install --upgrade pip
python -m pip install -r "$ROOT/../../../../nlp/ThamudicEpiPlatform/server/requirements.txt"
if [[ "${INSTALL_OCR_EXTRAS:-0}" == "1" ]]; then python -m pip install 'kraken>=7,<8' 'easyocr>=1.7,<2' 'paddleocr>=3,<4'; fi
python - <<'PY'
mods=['PIL','numpy','cv2','fastapi','pypdf','reportlab']
for m in mods: __import__(m); print(m+': OK')
PY
