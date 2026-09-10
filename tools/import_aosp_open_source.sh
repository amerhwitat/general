#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-third_party/aosp/src}"
mkdir -p "$ROOT"
repos=(
  platform/frameworks/base
  platform/frameworks/native
  platform/system/core
  platform/art
  platform/bionic
  platform/hardware/interfaces
  platform/packages/modules
  platform/external/perfetto
  platform/external/boringssl
)
for r in "${repos[@]}"; do
  d="$ROOT/${r#platform/}"
  mkdir -p "$(dirname "$d")"
  if [[ -d "$d/.git" ]]; then
    git -C "$d" fetch --depth=1 origin main || true
  else
    git clone --depth=1 "https://android.googlesource.com/$r" "$d"
  fi
done
printf '%s\n' "AOSP sources acquired under $ROOT. Review LICENSE/NOTICE files before redistribution." 
