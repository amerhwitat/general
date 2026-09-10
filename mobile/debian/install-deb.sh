#!/usr/bin/env bash
set -euo pipefail
pkg="${1:?usage: install-deb.sh package.deb}"
command -v dpkg-deb >/dev/null || { echo 'dpkg-deb is required for inspection' >&2; exit 2; }
arch="$(dpkg-deb -f "$pkg" Architecture)"
name="$(dpkg-deb -f "$pkg" Package)"
version="$(dpkg-deb -f "$pkg" Version)"
[ "$arch" = "arm64" ] || { echo "rejected: $name $version targets $arch, not arm64" >&2; exit 3; }
echo "INSPECTED package=$name version=$version architecture=$arch"
echo 'Chimera policy: stage, verify hash/signature, resolve dependencies, then commit atomically.'
echo 'This helper intentionally does not execute maintainer scripts outside the Chimera transaction sandbox.'
