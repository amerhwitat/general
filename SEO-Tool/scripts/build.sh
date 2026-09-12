#!/usr/bin/env bash
set -euo pipefail
python3 -m pip install -e '.[gui,documents,audit]'
python3 -m pytest -q SEO-Tool/tests
