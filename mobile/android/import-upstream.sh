#!/usr/bin/env bash
set -euo pipefail
mkdir -p third_party/android/upstream
cat <<'EOF'
Android upstream acquisition boundary:
- AOSP: obtain from official Android Open Source Project sources.
- Waydroid: use its namespace/container architecture as the current Linux integration reference.
- Anbox: historical reference only; upstream repository is archived.
- Android images and APKs remain separately licensed artifacts and are not blindly vendored.
EOF
