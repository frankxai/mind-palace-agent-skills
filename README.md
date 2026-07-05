<div align="center">

<img src=".github/hero.svg" alt="mind-palace-agent-skills — build a mind palace with an agent" width="100%" />

# mind-palace-agent-skills

### Build a **mind palace** with an agent — the real, science-grounded kind

> The **method of loci** for both **human learners** and **AI agents**: design a palace, encode vivid
> images, walk it to self-test, schedule spaced review, render it as a navigable artifact. Plus the
> **Blessing Protocol** suite — witness your week's work and grow a palace from what is whole.
> Self-contained `SKILL.md` skills for Claude Code, Claude.ai, ChatGPT, Cursor, Codex, Gemini.

[![License: MIT](https://img.shields.io/badge/License-MIT-f4c97a.svg)](LICENSE)
[![Built on SIP](https://img.shields.io/badge/Built%20on-SIP-c9b6ff.svg)](https://github.com/frankxai/Starlight-Intelligence-System)
[![Blessing Protocol](https://img.shields.io/badge/Blessing%20Protocol-v0.1-f4c97a.svg)](https://github.com/frankxai/bless)
[![Skills](https://img.shields.io/badge/skills-13-f4c97a.svg)](docs/CATALOG.md)
[![Validate](https://github.com/frankxai/mind-palace-agent-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/frankxai/mind-palace-agent-skills/actions/workflows/validate.yml)

[**Memory Palace**](#the-memory-palace-suite) · [**Blessing**](#the-blessing-suite) · [**Install**](#install) · [**Catalog**](docs/CATALOG.md) · [**Contribute**](CONTRIBUTING.md)

</div>

---

Two suites, 13 skills, one library. Grounded in cognitive-science primary literature — no neuro-myths.
See [`spec/MEMORY-PALACE-METHOD.md`](spec/MEMORY-PALACE-METHOD.md).

## The Memory Palace suite

| Skill | Step | Does |
|---|---|---|
| [`palace-foundations`](skills/palace-foundations/SKILL.md) | start here | Teach the method of loci and route to the right skill. |
| [`memory-palace-architect`](skills/memory-palace-architect/SKILL.md) | design | Choose a locus, lay a fixed route, space the stations. |
| [`loci-encoder`](skills/loci-encoder/SKILL.md) | encode | Turn each item into a vivid, memorable image. |
| [`number-memory`](skills/number-memory/SKILL.md) | encode | Digits, dates, cards via Major / Dominic / PAO. |
| [`palace-walk`](skills/palace-walk/SKILL.md) | retrieve | Self-test by walking the route; repair weak loci. |
| [`spaced-recall`](skills/spaced-recall/SKILL.md) | schedule | Spaced repetition (FSRS/SM-2); Anki export. |
| [`imagination-gym`](skills/imagination-gym/SKILL.md) | train | Strengthen mental-imagery vividness. |
| [`agent-memory-palace`](skills/agent-memory-palace/SKILL.md) | for agents | Persistent spatial memory across sessions. |
| [`palace-visualizer`](skills/palace-visualizer/SKILL.md) | render | Standalone HTML palace + per-locus image prompts. |

Commands: `/memorize <target>` · `/recall` · `/palace-new`. The shared data shape is
[`palace.json`](spec/palace.schema.json).

**See it:** open [`assets/palace-viewer/index.html`](assets/palace-viewer/index.html) — a
self-contained 3D viewer + builder. It loads the example
[`spec/examples/solar-system.palace.json`](spec/examples/solar-system.palace.json), or drag in your own.

## The Blessing suite

| Skill | Step | Does |
|---|---|---|
| [`github-bless`](skills/github-bless/SKILL.md) | ingest | Roll the week's commits/PRs into a candidate set. |
| [`weekly-blessing`](skills/weekly-blessing/SKILL.md) | witness | The Sunday ritual — ratify what is whole. |
| [`palace-build`](skills/palace-build/SKILL.md) | grow | Turn the ledger into `rooms.json` + an HTML palace. |
| [`blessing-standard`](skills/blessing-standard/SKILL.md) | onboard | Scaffold the five Blessing files into any repo. |

Commands: `/sunday` · `/bless <slug>` · `/palace`. The standard:
[`frankxai/bless`](https://github.com/frankxai/bless). Each blessing skill carries a `references/`
deep-dive — the [voice register](skills/weekly-blessing/references/voice-register.md),
[3D craft](skills/palace-build/references/3d-craft.md),
[connectors](skills/github-bless/references/connectors.md).

## Install

**Download a kit** — grab a zip from the latest [release](../../releases)
(`mind-palace-skills.zip`, or a per-platform kit), unzip, follow its `INSTALL.md`.

**Claude Code (plugin)** — `/plugin marketplace add frankxai/mind-palace-agent-skills`

**Clone & copy**
```bash
git clone https://github.com/frankxai/mind-palace-agent-skills
cp -r mind-palace-agent-skills/skills/*    ~/.claude/skills/
cp -r mind-palace-agent-skills/commands/*  ~/.claude/commands/
```

Other runtimes (ChatGPT, Cursor, Codex, Gemini): see [`MULTI_RUNTIME.md`](MULTI_RUNTIME.md). `SKILL.md`
is universal; only the install path differs.

## Build & validate

```bash
python3 scripts/validate_skills.py            # frontmatter + structure + rules
python3 scripts/generate_catalog.py           # regenerate docs/CATALOG.md + docs/index.html
python3 scripts/generate_catalog.py --check   # confirm catalog + Pages index are in sync
python3 scripts/build_dist.py                 # build dist/ zips (use --no-assets for lean)
```

A browsable catalog is generated to [`docs/`](docs/CATALOG.md) and served via GitHub Pages.

## The Blessing family

| Repo | Role |
|---|---|
| [**bless**](https://github.com/frankxai/bless) | The open standard — the Blessing Protocol |
| [**mind-palace-agent-skills**](https://github.com/frankxai/mind-palace-agent-skills) | Portable agent skills — Memory Palace + Blessing |
| [**frankx-mind-palace**](https://github.com/frankxai/frankx-mind-palace) | The mind — Frank's blessed work as data |
| [**frankx-palace**](https://github.com/frankxai/frankx-palace) | The palace — the 3D memory palace that grows each Sunday |

## Part of the Mind Intelligence ecosystem

The memory-palace family is the reflection-and-training-practice sibling of the wider
[Mind Intelligence Systems](https://github.com/frankxai/mind-intelligence-systems) swarm — where the
cognitive family *models* the mind, the palace family *trains, witnesses, and keeps* what is whole.
Start from the [curated map](https://github.com/frankxai/awesome-mind-agent-skills).

| Family | What it does | Entry point |
|---|---|---|
| canon | naming · models · mesh | [mind-intelligence-systems](https://github.com/frankxai/mind-intelligence-systems) |
| cognitive · lived OS | model → schemas → personal OS | [agentic-mind-os](https://github.com/frankxai/agentic-mind-os) |
| memory palace | method of loci + witness & keep finished work | [mind-palace-agent-skills](https://github.com/frankxai/mind-palace-agent-skills) |
| discovery | the front door | [awesome-mind-agent-skills](https://github.com/frankxai/awesome-mind-agent-skills) |

<sub>Built on SIP · Memory Palace Method v0.1 · The Blessing Protocol v0.1 · MIT</sub>
