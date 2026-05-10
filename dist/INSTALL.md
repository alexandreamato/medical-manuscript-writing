# Medical Manuscript Writing — Installation guide

Three install formats are provided in this folder. Pick the one that matches where you want the skill to run.

| File | Where it installs | Size |
| --- | --- | --- |
| `medical-manuscript-writing-claudeai.zip` | Claude.ai web/desktop (uploaded skill) | 258 KB |
| `medical-manuscript-writing-local.zip` | Claude Code or Cowork (local skills folder) | 258 KB |
| `medical-manuscript-writing-plugin.zip` | Claude Code plugin (with `.claude-plugin/plugin.json`) for marketplace or shared distribution | 265 KB |

All three contain the same skill content. Only the wrapping differs.

---

## 1. Claude.ai upload (web or desktop app)

Requires Claude Pro, Max, Team, or Enterprise.

1. Open Claude.ai → click your initials in the bottom-left → **Settings** → **Capabilities** → **Skills**.
2. Click **Upload skill**.
3. Choose `medical-manuscript-writing-claudeai.zip`.
4. Confirm. The skill appears in your skill list and is available in any new conversation.

To invoke it in a chat, ask Claude something like: "Use the medical manuscript writing skill to draft the Methods section of my RCT."

To update later, upload the same zip again — Claude.ai replaces the existing skill.

---

## 2. Claude Code or Cowork — local skills folder

For personal use on your Mac (or Linux/Windows). The skill lives in your home folder and is automatically discovered.

```
unzip medical-manuscript-writing-local.zip
mkdir -p ~/.claude/skills
mv medical-manuscript-writing ~/.claude/skills/
```

Verify:

```
ls ~/.claude/skills/medical-manuscript-writing/SKILL.md
```

Restart Claude Code (or open a new Cowork conversation). Confirm it loaded:

- In Claude Code: run `/skills` — the skill should appear in the list.
- In Cowork: it appears under `<available_skills>` in any new session.

Updating later: delete the folder and re-extract, or `rsync -a --delete medical-manuscript-writing/ ~/.claude/skills/medical-manuscript-writing/`.

---

## 3. Claude Code plugin (marketplace / shared distribution)

For sharing across a team, distributing through a marketplace, or version-managing the skill alongside other plugins.

Plugin structure inside the zip:

```
medical-manuscript-writing-plugin/
├── .claude-plugin/
│   └── plugin.json          ← manifest (name, version, author, license, keywords)
└── skills/
    └── medical-manuscript-writing/
        ├── SKILL.md
        ├── README.md
        ├── CHANGELOG.md
        ├── LICENSE
        ├── references/...
        ├── templates/...
        └── agents/...
```

Install options:

A. Drop into a personal marketplace folder (simplest):

```
unzip medical-manuscript-writing-plugin.zip -d ~/my-claude-marketplace/
```

Then in Claude Code: `/plugin marketplace add ~/my-claude-marketplace` followed by `/plugin install medical-manuscript-writing`.

B. Publish through GitHub for shared use:

1. Create a public or private repo (for example `username/claude-plugins`).
2. Copy the contents of `medical-manuscript-writing-plugin/` into a `plugins/medical-manuscript-writing/` subfolder.
3. Add a top-level `.claude-plugin/marketplace.json` listing the plugin (see Anthropic's plugin docs at https://docs.claude.com).
4. Users install with: `/plugin marketplace add username/claude-plugins` then `/plugin install medical-manuscript-writing`.

C. Direct local install without a marketplace:

```
unzip medical-manuscript-writing-plugin.zip
# Then point Claude Code at the unzipped folder:
/plugin install ./medical-manuscript-writing-plugin
```

---

## Verifying the skill loaded correctly

After install in any of the three formats, ask Claude:

> List the section guides in the medical-manuscript-writing skill.

A correctly loaded skill returns the five Section Guide groups from `SKILL.md` (A. Section guides, B. Article types, C. Cross-cutting standards, D. Form/format/presentation, E. Writing quality and process). If it does not, the skill is not loaded — check the install path and restart the client.

## Updating

The version is recorded in two places: `CHANGELOG.md` (current: `1.5.0` — 2026) and (plugin format only) `.claude-plugin/plugin.json`. Bump both when you release a new version.

## License

CC BY 4.0. Author: Alexandre Campos Moraes Amato (alexandre@amato.com.br).
