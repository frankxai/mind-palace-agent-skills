# Multi-runtime support

> Skills are authored once in the `SKILL.md` format (Markdown + a two-field YAML header). That format
> is universal — every assistant can read it. Runtimes differ only in **where the file is installed**,
> not in what it contains.

## Import matrix

| Runtime | Native location | How to install | Status |
|---|---|---|---|
| **Claude Code** | `~/.claude/skills/<name>/SKILL.md` + `~/.claude/commands/*.md` | `cp -r skills/* ~/.claude/skills/` and `cp -r commands/* ~/.claude/commands/`, or add the plugin marketplace | ✅ native |
| **Claude.ai / cowork** | Project knowledge / custom instructions | paste a `SKILL.md` body, or attach `skills/` to the Project | ✅ portable |
| **ChatGPT (Projects / GPTs)** | Custom instructions / Project files | paste the `SKILL.md` you want, or attach `skills/`; see `CONNECTORS.md` for the tools each expects | ✅ portable |
| **Cursor** | `.cursor/rules/<name>.mdc` | keep the `name` + `description` frontmatter, paste the body as a rule | 🟡 convert |
| **Codex CLI** | `AGENTS.md` / project docs | reference or paste the skill | 🟡 paste |
| **Gemini CLI** | `~/.gemini/` templates | paste the skill body | 🟡 paste |

## Download kits

`python scripts/build_dist.py` produces ready-to-install kits:

- `dist/mind-palace-skills.zip` — everything (skills, commands, spec, assets, docs).
- `dist/kits/claude-code.zip` — laid out for `~/.claude/`, with an `INSTALL.md`.
- `dist/kits/chatgpt-cowork.zip` — skills + connectors, no Claude-specific files.
- `dist/kits/cursor.zip` — skills + conversion note.
- `dist/skills/<name>.zip` — any single skill on its own.

Tagged releases (`v*`) attach all of these as GitHub Release assets automatically.

## Why `skill-rules.json` is Claude-specific

`skill-rules.json` drives *auto-activation* (keyword/command triggers) in Claude runtimes. Other
assistants don't read it — there, you invoke a skill by pasting or referencing it. The kits that
target non-Claude runtimes omit it (or keep it as documentation only).
