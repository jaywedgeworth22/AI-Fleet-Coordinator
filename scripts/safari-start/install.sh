#!/usr/bin/env bash
# Install Jay's Safari start page on this Mac.  Copies index.html to ~/Sites/safari-start and points
# Safari's homepage, new tabs, and new windows at it.  Re-run after editing index.html.
#   scripts/safari-start/install.sh           install or refresh
#   scripts/safari-start/install.sh --revert  restore Safari's built-in Start Page
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="$HOME/Sites/safari-start"
if [[ "${1:-}" == "--revert" ]]; then
  defaults write com.apple.Safari HomePage -string "https://www.apple.com/startpage/"
  defaults delete com.apple.Safari NewTabBehavior 2>/dev/null || true
  defaults delete com.apple.Safari NewWindowBehavior 2>/dev/null || true
  echo "Safari is back on its built-in Start Page.  The page itself is still at $DEST/index.html."
  exit 0
fi
mkdir -p "$DEST"
cp "$HERE/index.html" "$DEST/index.html"
URL="file://$DEST/index.html"
defaults write com.apple.Safari HomePage -string "$URL"
defaults write com.apple.Safari NewTabBehavior -int 0
defaults write com.apple.Safari NewWindowBehavior -int 0
echo "Installed $DEST/index.html and pointed Safari at it.  Open a new tab; if the old Start Page still shows, quit and reopen Safari."
