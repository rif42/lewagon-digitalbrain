#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/notes"
DEST="$ROOT/quartz/content"

if [ ! -d "$SRC" ]; then
  echo "Source notes dir not found: $SRC" >&2
  exit 1
fi

# wipe previous content (keep .gitkeep if present by re-creating)
rm -rf "$DEST"
mkdir -p "$DEST"

# copy everything under notes/ into quartz/content/
# use tar to preserve dotfiles if any; fallback to cp -a
if command -v rsync >/dev/null 2>&1; then
  rsync -a --delete "$SRC"/ "$DEST"/
else
  cp -a "$SRC"/. "$DEST"/
fi

# Ensure index.md exists at content root for Quartz landing
if [ ! -f "$DEST/index.md" ] && [ -f "$SRC/index.md" ]; then
  cp "$SRC/index.md" "$DEST/index.md"
fi

# Also keep AGENTS.md publishable if present at notes root: copy as index-adjacent
echo "Synced notes -> quartz/content ($(find "$DEST" -type f | wc -l | tr -d ' ') files)"
