# mind-palace-agent-skills

Build a **mind palace** with an agent — the real, science-backed kind. Portable skills that teach and
operate the **method of loci** for both **human learners** and **AI agents**: design a palace, encode
vivid images, walk it to self-test, schedule spaced review, and render it as a navigable artifact.

Plus the **Blessing Protocol** suite — witness your week's work and grow a palace from what is whole.

Two suites, 13 skills, one library. Works in any runtime that reads `SKILL.md` (Claude Code,
Claude.ai, ChatGPT, Cursor, Codex, Gemini). Grounded in cognitive-science primary literature — no
neuro-myths. See [`spec/MEMORY-PALACE-METHOD.md`](spec/MEMORY-PALACE-METHOD.md).

## Quick start

**Download the kit** — grab a zip from the latest [release](../../releases) (`mind-palace-skills.zip`,
or a per-platform kit), unzip, and follow its `INSTALL.md`.

**Claude Code (plugin)**
```
/plugin marketplace add frankxai/mind-palace-agent-skills
```

**Clone & copy**
```bash
git clone https://github.com/frankxai/mind-palace-agent-skills
cp -r mind-palace-agent-skills/skills/*    ~/.claude/skills/
cp -r mind-palace-agent-skills/commands/*  ~/.claude/commands/
```

**Other runtimes** — see [`MULTI_RUNTIME.md`](MULTI_RUNTIME.md). `SKILL.md` is universal; only the
install path differs.

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
self-contained 3D viewer + builder. It loads the example at
[`spec/examples/solar-system.palace.json`](spec/examples/solar-system.palace.json), or drag in your
own.

## The Blessing suite

| Skill | Step | Does |
|---|---|---|
| [`github-bless`](skills/github-bless/SKILL.md) | ingest | Roll the week's commits/PRs into a candidate set. |
| [`weekly-blessing`](skills/weekly-blessing/SKILL.md) | witness | The Sunday ritual — ratify what is whole. |
| [`palace-build`](skills/palace-build/SKILL.md) | grow | Turn the ledger into `rooms.json` + an HTML palace. |
| [`blessing-standard`](skills/blessing-standard/SKILL.md) | onboard | Scaffold the five Blessing files into any repo. |

Commands: `/sunday` · `/bless <slug>` · `/palace`. The standard:
[`frankxai/bless`](https://github.com/frankxai/bless).

> Full catalog: [`docs/CATALOG.md`](docs/CATALOG.md) · Connectors: [`CONNECTORS.md`](CONNECTORS.md).

## Build & validate

```bash
python scripts/validate_skills.py            # frontmatter + rules consistency
python scripts/generate_catalog.py           # regenerate docs/CATALOG.md
python scripts/build_dist.py                 # build dist/ zips (use --no-assets for lean)
```

## License

MIT. See [`LICENSE`](LICENSE).

Built on SIP · Memory Palace Method v0.1 · The Blessing Protocol v0.1
