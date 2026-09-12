#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
command -v flutter >/dev/null || { echo "Flutter is required"; exit 1; }
command -v xcodebuild >/dev/null || { echo "Xcode command-line tools are required"; exit 1; }
for app in "$ROOT"/*; do
  [ -d "$app/flutter" ] || continue
  echo "=== Flutter: $(basename "$app") ==="
  (cd "$app/flutter" && flutter pub get && flutter build ios --release --no-codesign && flutter build macos --release)
done
for app in "$ROOT"/*; do
  [ -d "$app/objc" ] || continue
  echo "=== Objective-C: $(basename "$app") ==="
  (cd "$app/objc" && command -v xcodegen >/dev/null && xcodegen generate || true)
done
