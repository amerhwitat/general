#!/usr/bin/env bash
set -euo pipefail
python3 -m pip install -e '.[gui,documents]'
python3 -m SEO_Tool.gui
