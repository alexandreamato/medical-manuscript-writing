#!/usr/bin/env bash
# Publish the medical-manuscript-writing skill to a NEW private GitHub repo.
# Usage:
#   bash dist/publish-to-github.sh                  # repo named medical-manuscript-writing
#   bash dist/publish-to-github.sh my-custom-name   # repo with a custom name
#
# Requirements:
#   - gh CLI installed and authenticated (run `gh auth login` once if not).
#     Install on Mac: brew install gh
#   - Run this script from the skill folder root, e.g.:
#     cd "$HOME/Amato Dropbox/Alexandre Amato/Projects/Informatica/skills/medical-manuscript-writing"
set -euo pipefail

REPO_NAME="${1:-medical-manuscript-writing}"

# 0. Pre-flight checks
command -v gh >/dev/null 2>&1 || {
  echo "ERROR: gh CLI not found. Install with: brew install gh"
  exit 1
}
command -v git >/dev/null 2>&1 || {
  echo "ERROR: git not found."
  exit 1
}
gh auth status >/dev/null 2>&1 || {
  echo "ERROR: gh not authenticated. Run: gh auth login"
  exit 1
}

# 1. Init a fresh git repo here (idempotent — skips if already a repo)
if [ ! -d .git ]; then
  git init -b main
  echo "Initialized empty git repo on branch main."
else
  echo "Repo already initialized — using existing .git."
fi

# 2. Stage and commit everything except .gitignore'd files
git add -A
if git diff --cached --quiet; then
  echo "Nothing new to commit."
else
  git commit -m "Initial commit: medical-manuscript-writing skill v1.5.0

Author: Alexandre Campos Moraes Amato
License: CC BY 4.0
Reporting standards: CONSORT 2010, STROBE, PRISMA 2020, STARD 2015, CARE 2013
Citation default: Vancouver (ICMJE)
Diagram tools: enciclopedia.med.br/{prisma2020, consort2010, care-timeline}"
fi

# 3. Create the private remote repo (if it does not already exist) and push.
#    --source=. uses the current folder; --push pushes the current branch.
GH_USER="$(gh api user --jq .login)"
if gh repo view "${GH_USER}/${REPO_NAME}" >/dev/null 2>&1; then
  echo "Repo ${GH_USER}/${REPO_NAME} already exists — pushing to it."
  git remote add origin "https://github.com/${GH_USER}/${REPO_NAME}.git" 2>/dev/null || true
  git push -u origin main
else
  gh repo create "${REPO_NAME}" \
    --private \
    --source=. \
    --remote=origin \
    --push \
    --description "Medical and biomedical manuscript writing skill — IMRaD, CONSORT, STROBE, PRISMA 2020, STARD, CARE; Vancouver default."
fi

echo
echo "Done. Repo URL:"
gh repo view "${GH_USER}/${REPO_NAME}" --json url -q .url
