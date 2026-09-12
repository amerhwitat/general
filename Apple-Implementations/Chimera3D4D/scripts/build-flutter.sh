#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../flutter"
command -v flutter >/dev/null 2>&1 || { echo 'Flutter SDK is required'; exit 1; }
flutter pub get
flutter analyze
flutter build web --release
