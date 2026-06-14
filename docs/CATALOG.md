# Catalog

The 4 skills of the **mind-palace-agent-skills** — the portable agent skills of the [Blessing Protocol](https://github.com/frankxai/bless). Each ships as a self-contained `SKILL.md` with two-field frontmatter (`name`, `description`) and runs in any runtime that reads `SKILL.md` skills.

> This file is generated. After changing a skill or a reference, run `python3 scripts/generate_catalog.py`, then `python3 scripts/validate_skills.py`.

The loop: **ingest → witness → grow → onboard**.

| Skill | Step | What it does |
|---|---|---|
| [`github-bless`](../skills/github-bless/SKILL.md) | ingest | Ingest a builder's GitHub (and optional connectors) and roll the week's work into a blessable set. Use when starting a weekly blessing, when the user says "what did I ship this week", "roll my week", "ingest my repos for the blessing", or before running the weekly-blessing skill. Reads commits and merged PRs across repos and emits a structured candidate list — it does not bless anything itself. |
| [`weekly-blessing`](../skills/weekly-blessing/SKILL.md) | witness | Run the weekly Sunday blessing ritual on a builder's work — witness what shipped, ratify what is whole, name what to ignore for seven days, and surface the one path forward. Use when the user says "run the weekly blessing", "do my Sunday review", "bless this week", or invokes /sunday or /bless. Writes weekly/YYYY-W##.md and appends to the blessing ledger. Invoked, never auto-fired. |
| [`palace-build`](../skills/palace-build/SKILL.md) | grow | Turn a builder's blessing ledger into a palace — emit palace/rooms.json for a React/Three.js renderer and a portable standalone HTML palace that works with no build step. Use when the user says "build my palace", "render the palace", "regenerate rooms.json", or after a weekly blessing adds new rooms. Reads blessings.jsonl + palace.md; writes rooms.json and an optional self-contained index.html. |
| [`blessing-standard`](../skills/blessing-standard/SKILL.md) | onboard | Scaffold the five Blessing Protocol files (soul.md, agent.md, skills.md, palace.md, bless.md) into any repository and fill them from what the repo already is. Use when the user says "adopt bless here", "make this repo blessable", "scaffold the blessing files", "set up the mind palace standard". Reads the repo to draft soul.md first, then derives the rest; never overwrites a filled file without asking. |

## `github-bless`

**Step:** ingest · **Skill:** [`skills/github-bless/SKILL.md`](../skills/github-bless/SKILL.md)

Ingest a builder's GitHub (and optional connectors) and roll the week's work into a blessable set. Use when starting a weekly blessing, when the user says "what did I ship this week", "roll my week", "ingest my repos for the blessing", or before running the weekly-blessing skill. Reads commits and merged PRs across repos and emits a structured candidate list — it does not bless anything itself.

**References:**

- [`connectors.md`](../skills/github-bless/references/connectors.md)

## `weekly-blessing`

**Step:** witness · **Skill:** [`skills/weekly-blessing/SKILL.md`](../skills/weekly-blessing/SKILL.md)

Run the weekly Sunday blessing ritual on a builder's work — witness what shipped, ratify what is whole, name what to ignore for seven days, and surface the one path forward. Use when the user says "run the weekly blessing", "do my Sunday review", "bless this week", or invokes /sunday or /bless. Writes weekly/YYYY-W##.md and appends to the blessing ledger. Invoked, never auto-fired.

**References:**

- [`voice-register.md`](../skills/weekly-blessing/references/voice-register.md)

## `palace-build`

**Step:** grow · **Skill:** [`skills/palace-build/SKILL.md`](../skills/palace-build/SKILL.md)

Turn a builder's blessing ledger into a palace — emit palace/rooms.json for a React/Three.js renderer and a portable standalone HTML palace that works with no build step. Use when the user says "build my palace", "render the palace", "regenerate rooms.json", or after a weekly blessing adds new rooms. Reads blessings.jsonl + palace.md; writes rooms.json and an optional self-contained index.html.

**References:**

- [`3d-craft.md`](../skills/palace-build/references/3d-craft.md)

## `blessing-standard`

**Step:** onboard · **Skill:** [`skills/blessing-standard/SKILL.md`](../skills/blessing-standard/SKILL.md)

Scaffold the five Blessing Protocol files (soul.md, agent.md, skills.md, palace.md, bless.md) into any repository and fill them from what the repo already is. Use when the user says "adopt bless here", "make this repo blessable", "scaffold the blessing files", "set up the mind palace standard". Reads the repo to draft soul.md first, then derives the rest; never overwrites a filled file without asking.

---

Built on SIP · The Blessing Protocol v0.1 · MIT
