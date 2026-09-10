#!/usr/bin/env bash
set -euo pipefail
cmd="${1:-help}"; shift || true
case "$cmd" in
 search|install|remove|update|upgrade|info) exec /usr/lib/chimera/chimera-pkg "$cmd" "$@";;
 apt|apt-get|aptitude|dpkg|rpm|dnf|yum|pacman|apk|nix|flatpak|snap|git|gh) exec /usr/lib/chimera/chimera-pkg manager "$cmd" "$@";;
 *) echo 'chimera-pkg: search install remove update upgrade info manager' >&2; exit 2;;
esac
