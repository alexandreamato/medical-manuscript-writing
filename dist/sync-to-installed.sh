#!/usr/bin/env bash
# Sync this Dropbox-hosted source repo to the installed skill at
# ~/.claude/skills/medical-manuscript-writing (used by Claude Desktop / Claude Code).
#
# Run from the source folder root, e.g.:
#   cd "$HOME/Amato Dropbox/Alexandre Amato/Projects/Informatica/skills/medical-manuscript-writing"
#   bash dist/sync-to-installed.sh
#
# What it does:
#   1. Verifies you're inside a source folder that contains SKILL.md.
#   2. Mirrors the source to ~/.claude/skills/medical-manuscript-writing/.
#   3. Excludes build/dev artifacts (.git, dist/*.zip, .DS_Store, IDE folders).
#   4. Uses --delete so files removed in the source are removed from the install.
set -euo pipefail

SRC="$(pwd)"
DEST="$HOME/.claude/skills/medical-manuscript-writing"

# Sanity checks
if [ ! -f "$SRC/SKILL.md" ]; then
  echo "ERROR: SKILL.md not found in $SRC."
  echo "       Run this script from the skill source folder root."
  exit 1
fi
if ! grep -q "^name: medical-manuscript-writing" "$SRC/SKILL.md"; then
  echo "ERROR: $SRC/SKILL.md does not look like the medical-manuscript-writing skill."
  exit 1
fi

mkdir -p "$DEST"

echo "Syncing:"
echo "  src:  $SRC"
echo "  dest: $DEST"
echo

rsync -a --delete \
  --exclude='.git/' \
  --exclude='.DS_Store' \
  --exclude='._*' \
  --exclude='*.swp' \
  --exclude='*~' \
  --exclude='.vscode/' \
  --exclude='.idea/' \
  --exclude='dist/*.zip' \
  --exclude='dist/*.sh' \
  --exclude='NOTES.local.md' \
  --exclude='scratch/' \
  "$SRC/" "$DEST/"

# Quick verification
if [ -f "$DEST/SKILL.md" ]; then
  echo "Done. Installed skill files:"
  find "$DEST" -type f | wc -l | awk '{print $1 " files at " ENVIRON["HOME"] "/.claude/skills/medical-manuscript-writing/"}'
  echo
  echo "Tip: restart Claude Desktop or open a fresh conversation so the skill reloads."
else
  echo "ERROR: sync completed but SKILL.md is missing at the destination."
  exit 1
fi
