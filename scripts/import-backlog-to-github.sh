#!/usr/bin/env bash
# Wrapper — import/sync backlog vers GitHub Project « Projet10 backlog »
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/import-backlog-to-github.py "$@"
