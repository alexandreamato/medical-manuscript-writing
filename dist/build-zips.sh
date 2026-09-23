#!/usr/bin/env bash
# Build the three distribution zips from the source tree.
#
#   bash dist/build-zips.sh
#
# The version comes from the first "## [x.y.z]" heading of CHANGELOG.md and is
# written into the plugin's plugin.json, so the two can never disagree.
set -euo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)"
NAME="medical-manuscript-writing"
VERSION="$(grep -m1 -oE '^## \[[0-9]+\.[0-9]+\.[0-9]+\]' "$SRC/CHANGELOG.md" | tr -d '#[] ')"
[ -n "$VERSION" ] || { echo "ERROR: no version heading in CHANGELOG.md"; exit 1; }

STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

# Same exclusions as sync-to-installed.sh, plus build products of the kit.
rsync -a \
  --exclude='.git/' --exclude='.claude/' --exclude='dist/' --exclude='.DS_Store' --exclude='._*' \
  --exclude='*.swp' --exclude='*~' --exclude='.vscode/' --exclude='.idea/' --exclude='.gitignore' \
  --exclude='__pycache__/' --exclude='templates/build-kit/outputs/' --exclude='templates/build-kit/build/' \
  --exclude='NOTES.local.md' --exclude='scratch/' \
  "$SRC/" "$STAGE/$NAME/"
# The kit is copied into users' projects, where its .gitignore is wanted.
cp "$SRC/templates/build-kit/.gitignore" "$STAGE/$NAME/templates/build-kit/.gitignore"

rm -f "$SRC/dist/$NAME-claudeai.zip" "$SRC/dist/$NAME-local.zip" "$SRC/dist/$NAME-plugin.zip"
(cd "$STAGE" && zip -qr -X "$SRC/dist/$NAME-local.zip" "$NAME")
cp "$SRC/dist/$NAME-local.zip" "$SRC/dist/$NAME-claudeai.zip"

PLUG="$STAGE/$NAME-plugin"
mkdir -p "$PLUG/.claude-plugin" "$PLUG/skills"
cp -R "$STAGE/$NAME" "$PLUG/skills/$NAME"
cat > "$PLUG/.claude-plugin/plugin.json" <<JSON
{
  "name": "$NAME",
  "version": "$VERSION",
  "description": "Medical and biomedical manuscript writing — IMRaD, CONSORT 2025, SPIRIT 2025, STROBE, PRISMA 2020, STARD, CARE; Vancouver-default citations; CONSORT / STROBE / PRISMA / CARE Timeline web-tool integration; procedural .docx build kit with journal profiles and reference verification; read-as-reader review; respond-to-reviewers letter templates.",
  "author": {
    "name": "Alexandre Campos Moraes Amato",
    "email": "alexandre@amato.com.br"
  },
  "license": "CC-BY-4.0",
  "homepage": "https://enciclopedia.med.br",
  "keywords": ["medical-writing", "biomedical", "manuscript", "imrad", "consort", "spirit", "strobe", "prisma",
               "stard", "care", "vancouver", "pandoc", "docx", "reviewer-response", "systematic-review", "rct",
               "case-report"]
}
JSON
(cd "$STAGE" && zip -qr -X "$SRC/dist/$NAME-plugin.zip" "$NAME-plugin")

echo "Built version $VERSION:"
for f in "$SRC/dist/"*.zip; do printf "  %s  %s\n" "$(du -h "$f" | cut -f1)" "$(basename "$f")"; done
