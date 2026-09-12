#!/bin/bash
set -euo pipefail
xcode-select --install 2>/dev/null || true
command -v brew >/dev/null || { echo "Install Homebrew first: https://brew.sh"; exit 1; }
brew update
brew install --formula flutter xcodegen cocoapods || true
flutter doctor -v
xcodebuild -version
xcrun simctl list devices available | head -80
