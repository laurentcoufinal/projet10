#!/usr/bin/env bash
# Régénère les SVG Mermaid (Kroki) pour export OpenOffice
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)/veille-presentation"
mkdir -p "$ROOT/svg"
for f in "$ROOT/diagrams"/*.mmd; do
  name=$(basename "$f" .mmd)
  echo "→ svg/${name}.svg"
  curl -sS -X POST "https://kroki.io/mermaid/svg" \
    -H "Content-Type: text/plain" \
    --data-binary @"$f" \
    -o "$ROOT/svg/${name}.svg"
  sleep 0.3
done
echo "Done. Ouvrir veille-presentation/veille-openoffice.html dans LibreOffice."
