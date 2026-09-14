#!/usr/bin/env bash
# Gera o HTML e imprime o PDF em A4 retrato.
# Uso: ./build.sh  (precisa de python3 e de um Chromium/Chrome no PATH ou em $CHROME)
set -euo pipefail
cd "$(dirname "$0")"
python3 src/build.py
CHROME="${CHROME:-$(command -v chromium || command -v chromium-browser || command -v google-chrome || command -v chrome || true)}"
if [ -z "$CHROME" ] && [ -x /opt/pw-browsers/chromium-1194/chrome-linux/chrome ]; then
  CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
fi
if [ -z "$CHROME" ]; then echo "Chromium não encontrado. Defina CHROME=/caminho/do/chrome"; exit 1; fi
"$CHROME" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PWD/dist/de-tola-a-virtuosa.pdf" "file://$PWD/dist/de-tola-a-virtuosa.html" 2>/dev/null
echo "PDF: dist/de-tola-a-virtuosa.pdf"
