<div align="center">

<img src=".github/hero.svg" alt="mind-palace-agent-skills — ingest your GitHub, witness the week, grow a palace" width="100%" />

# mind-palace-agent-skills

### Portable agent skills that run the [Blessing Protocol](https://github.com/frankxai/bless)

> Ingest a builder's GitHub, witness the week, and grow a palace from what is whole. Self-contained
> `SKILL.md` skills for Claude Code, Claude.ai, Cursor, Codex, Gemini, and any runtime that reads them.

[![License: MIT](https://img.shields.io/badge/License-MIT-f4c97a.svg)](LICENSE)
[![Built on SIP](https://img.shields.io/badge/Built%20on-SIP-c9b6ff.svg)](https://github.com/frankxai/Starlight-Intelligence-System)
[![Blessing Protocol](https://img.shields.io/badge/Blessing%20Protocol-v0.1-f4c97a.svg)](https://github.com/frankxai/bless)
[![Skills](https://img.shields.io/badge/skills-4-f4c97a.svg)](docs/CATALOG.md)
[![Validate](https://github.com/frankxai/mind-palace-agent-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/frankxai/mind-palace-agent-skills/actions/workflows/validate.yml)

[**The skills**](#the-skills) · [**The loop**](#the-loop) · [**Install**](#install) · [**Catalog**](docs/CATALOG.md) · [**Contribute**](CONTRIBUTING.md)

</div>

---

## The skills

| Skill | Step | Does |
|---|---|---|
| [`github-bless`](skills/github-bless/SKILL.md) | ingest | Roll the week's commits/PRs across repos + connectors into a candidate set. Names every gap. |
| [`weekly-blessing`](skills/weekly-blessing/SKILL.md) | witness | The Sunday ritual — six-section entry, ratify what is whole, append the ledger. |
| [`palace-build`](skills/palace-build/SKILL.md) | grow | Turn the ledger into `rooms.json` + a portable HTML palace. |
| [`blessing-standard`](skills/blessing-standard/SKILL.md) | onboard | Scaffold the five Blessing Protocol files into any repo, filled from what the repo is. |

Each skill carries a `references/` deep-dive where it earns one — the
[voice register](skills/weekly-blessing/references/voice-register.md),
[3D craft](skills/palace-build/references/3d-craft.md), and
[connectors](skills/github-bless/references/connectors.md).

## The loop

```mermaid
flowchart LR
  S["/sunday"] --> G["github-bless<br/>ingest"]
  G --> W["weekly-blessing<br/>witness"]
  W --> P["palace-build<br/>grow"]
  P --> Palace["a palace that<br/>grows each week"]
```

Commands: `/sunday` (the full loop) · `/bless <slug>` (single-piece ratification) · `/palace` (rebuild).
Auto-activation rules live in [`skill-rules.json`](skill-rules.json).

## Install

```bash
# copy the skills + commands into your agent's directory, e.g.
cp -r skills/* ~/.claude/skills/
cp -r commands/* ~/.claude/commands/
```

## Validate

```bash
python scripts/validate_skills.py            # frontmatter + rules
python scripts/generate_catalog.py --check   # catalog + index in sync
```

A browsable catalog is generated to [`docs/`](docs/CATALOG.md) and served via GitHub Pages.

## The Blessing family

| Repo | Role |
|---|---|
| [**bless**](https://github.com/frankxai/bless) | The open standard — the Blessing Protocol |
| [**mind-palace-agent-skills**](https://github.com/frankxai/mind-palace-agent-skills) | Portable agent skills — ingest · witness · grow |
| [**frankx-mind-palace**](https://github.com/frankxai/frankx-mind-palace) | The mind — Frank's blessed work as data |
| [**frankx-palace**](https://github.com/frankxai/frankx-palace) | The palace — the 3D memory palace that grows each Sunday |

<sub>Built on SIP · The Blessing Protocol v0.1 · MIT</sub>

## Part of the Mind Intelligence ecosystem

The memory-palace family is the reflection-practice sibling of the wider
[Mind Intelligence Systems](https://github.com/frankxai/mind-intelligence-systems) swarm —
where the cognitive family *models* the mind, the palace family *witnesses and keeps* what is
whole. Start from the [curated map](https://github.com/frankxai/awesome-mind-agent-skills).

| Family | What it does | Entry point |
|---|---|---|
| canon | naming · models · mesh | [mind-intelligence-systems](https://github.com/frankxai/mind-intelligence-systems) |
| cognitive · lived OS | model → schemas → personal OS | [agentic-mind-os](https://github.com/frankxai/agentic-mind-os) |
| memory palace | witness & keep finished work | [mind-palace-agent-skills](https://github.com/frankxai/mind-palace-agent-skills) |
| discovery | the front door | [awesome-mind-agent-skills](https://github.com/frankxai/awesome-mind-agent-skills) |
