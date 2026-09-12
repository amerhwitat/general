#!/usr/bin/env bash
set -euo pipefail
[[ $# -ge 1 ]] || { echo 'usage: webcontactcrawler.sh <html-file>'; exit 1; }
grep -Eoi '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}' "$1" | tr '[:upper:]' '[:lower:]' | sort -u | tee "${2:-emails.txt}"
