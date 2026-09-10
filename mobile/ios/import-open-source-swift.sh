#!/usr/bin/env bash
set -euo pipefail
mkdir -p third_party/swift/upstream
cat <<'EOF'
Open-source Swift boundary:
- Swift Package Manager: source/package workflow.
- swift-foundation / swift-corelibs-foundation: portable Foundation APIs.
- SwiftNIO: non-blocking networking primitives.
- Darwin-only proprietary iOS frameworks are not copied or represented as open source.
EOF
