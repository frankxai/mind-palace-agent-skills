# Catalog

The 13 skills of **mind-palace-agent-skills** — a real, science-grounded **Memory Palace** suite (the method of loci, for humans and agents) plus the **Blessing Protocol** suite ([bless](https://github.com/frankxai/bless)). Each ships as a self-contained `SKILL.md` and runs in any runtime that reads `SKILL.md` skills.

> This file is generated. After changing a skill or a reference, run `python3 scripts/generate_catalog.py`, then `python3 scripts/validate_skills.py`.

## Memory Palace suite

| Skill | Step | What it does |
|---|---|---|
| [`palace-foundations`](../skills/palace-foundations/SKILL.md) | start here | Teach the method of loci and route the user to the right memory-palace skill. Use when someone says "teach me the memory palace", "how does the method of loci work", "help me memorize X", "I want to remember a list/speech/deck", or is new to spatial memory. The start-here skill that explains the four-level model then dispatches to architect, encoder, number-memory, walk, or spaced-recall. |
| [`memory-palace-architect`](../skills/memory-palace-architect/SKILL.md) | design | Design a memory palace — choose a real or imagined locus, lay a fixed non-crossing route, and space the stations. Use when the user says "design a memory palace", "pick a place to memorize in", "lay out my palace", "map a route for N items", or needs a structure before encoding. Writes the rooms/stations skeleton of palace.json for loci-encoder to fill. |
| [`loci-encoder`](../skills/loci-encoder/SKILL.md) | encode | Turn each target into a vivid, memorable image and place it at a station. Use when the user says "encode these items", "make images for my palace", "help me remember names and faces", "turn this list into pictures", or after memory-palace-architect lays out the rooms. Applies bizarreness, multisensory, exaggeration, motion, and dual-coding; fills the loci[] of palace.json. |
| [`number-memory`](../skills/number-memory/SKILL.md) | encode | Memorize digits, dates, phone numbers, and playing cards by converting numbers into images. Use when the user says "memorize this number", "remember these dates", "how do I memorize a deck of cards", "PAO system", "Major System", or "Dominic System". Supplies the encoding for numeric targets, then hands the resulting images to loci-encoder for placement. |
| [`palace-walk`](../skills/palace-walk/SKILL.md) | retrieve | Walk the palace from memory to self-test recall, score it, and repair weak loci. Use when the user says "test me on my palace", "let me recall the list", "walk my palace", "quiz me", or after a palace is built or due for review. Runs retrieval practice (the testing effect), marks which loci held and which failed, and updates the recall block of palace.json. |
| [`spaced-recall`](../skills/spaced-recall/SKILL.md) | schedule | Schedule spaced repetition over a memory palace so it lasts, and export to Anki. Use when the user says "spaced repetition", "when should I review", "schedule my reviews", "keep this long-term", "export to Anki", "FSRS", or "SM-2". Computes next-due dates from palace-walk grades, writes the recall block of palace.json, and drives durable retention against the forgetting curve. |
| [`imagination-gym`](../skills/imagination-gym/SKILL.md) | train | Train mental-imagery vividness and scene construction so memory-palace images are stronger. Use when the user says "my mental pictures are weak/blurry", "I can't visualize", "train my imagination", "help me see images more clearly", or struggles to encode loci. Drills based on imagery research — multisensory detail, manipulation, and scene construction — to make encoding work better. |
| [`agent-memory-palace`](../skills/agent-memory-palace/SKILL.md) | for agents | Give an AI agent persistent, navigable memory across sessions using a memory-palace structure. Use when building agent memory, when the user says "remember this across sessions", "give the agent long-term memory", "persistent context", "knowledge graph for my agent", or for coding agents, Claude cowork, and ChatGPT projects that must retain state. Reads and writes palace.json as a durable spatial knowledge store the agent reloads each session. |
| [`palace-visualizer`](../skills/palace-visualizer/SKILL.md) | render | Render a memory palace as a navigable artifact — a self-contained HTML viewer plus image-generation prompts for each locus. Use when the user says "render my palace", "visualize the palace", "make a picture of my memory palace", "build out the palace", or wants a keepable visual. Reads palace.json, emits a standalone index.html (no build step) and per-locus image prompts; tolerates both memory-palace and blessing schemas. |

## Blessing suite

| Skill | Step | What it does |
|---|---|---|
| [`github-bless`](../skills/github-bless/SKILL.md) | ingest | Ingest a builder's GitHub (and optional connectors) and roll the week's work into a blessable set. Use when starting a weekly blessing, when the user says "what did I ship this week", "roll my week", "ingest my repos for the blessing", or before running the weekly-blessing skill. Reads commits and merged PRs across repos and emits a structured candidate list — it does not bless anything itself. |
| [`weekly-blessing`](../skills/weekly-blessing/SKILL.md) | witness | Run the weekly Sunday blessing ritual on a builder's work — witness what shipped, ratify what is whole, name what to ignore for seven days, and surface the one path forward. Use when the user says "run the weekly blessing", "do my Sunday review", "bless this week", or invokes /sunday or /bless. Writes weekly/YYYY-W##.md and appends to the blessing ledger. Invoked, never auto-fired. |
| [`palace-build`](../skills/palace-build/SKILL.md) | grow | Turn a builder's blessing ledger into a palace — emit palace/rooms.json for a React/Three.js renderer and a portable standalone HTML palace that works with no build step. Use when the user says "build my palace", "render the palace", "regenerate rooms.json", or after a weekly blessing adds new rooms. Reads blessings.jsonl + palace.md; writes rooms.json and an optional self-contained index.html. |
| [`blessing-standard`](../skills/blessing-standard/SKILL.md) | onboard | Scaffold the five Blessing Protocol files (soul.md, agent.md, skills.md, palace.md, bless.md) into any repository and fill them from what the repo already is. Use when the user says "adopt bless here", "make this repo blessable", "scaffold the blessing files", "set up the mind palace standard". Reads the repo to draft soul.md first, then derives the rest; never overwrites a filled file without asking. |

### `palace-foundations`

**Suite:** Memory Palace · **Step:** start here · **Skill:** [`skills/palace-foundations/SKILL.md`](../skills/palace-foundations/SKILL.md)

Teach the method of loci and route the user to the right memory-palace skill. Use when someone says "teach me the memory palace", "how does the method of loci work", "help me memorize X", "I want to remember a list/speech/deck", or is new to spatial memory. The start-here skill that explains the four-level model then dispatches to architect, encoder, number-memory, walk, or spaced-recall.

### `memory-palace-architect`

**Suite:** Memory Palace · **Step:** design · **Skill:** [`skills/memory-palace-architect/SKILL.md`](../skills/memory-palace-architect/SKILL.md)

Design a memory palace — choose a real or imagined locus, lay a fixed non-crossing route, and space the stations. Use when the user says "design a memory palace", "pick a place to memorize in", "lay out my palace", "map a route for N items", or needs a structure before encoding. Writes the rooms/stations skeleton of palace.json for loci-encoder to fill.

### `loci-encoder`

**Suite:** Memory Palace · **Step:** encode · **Skill:** [`skills/loci-encoder/SKILL.md`](../skills/loci-encoder/SKILL.md)

Turn each target into a vivid, memorable image and place it at a station. Use when the user says "encode these items", "make images for my palace", "help me remember names and faces", "turn this list into pictures", or after memory-palace-architect lays out the rooms. Applies bizarreness, multisensory, exaggeration, motion, and dual-coding; fills the loci[] of palace.json.

**References:**

- [`names-faces.md`](../skills/loci-encoder/references/names-faces.md)

### `number-memory`

**Suite:** Memory Palace · **Step:** encode · **Skill:** [`skills/number-memory/SKILL.md`](../skills/number-memory/SKILL.md)

Memorize digits, dates, phone numbers, and playing cards by converting numbers into images. Use when the user says "memorize this number", "remember these dates", "how do I memorize a deck of cards", "PAO system", "Major System", or "Dominic System". Supplies the encoding for numeric targets, then hands the resulting images to loci-encoder for placement.

**References:**

- [`major-system.md`](../skills/number-memory/references/major-system.md)
- [`pao.md`](../skills/number-memory/references/pao.md)

### `palace-walk`

**Suite:** Memory Palace · **Step:** retrieve · **Skill:** [`skills/palace-walk/SKILL.md`](../skills/palace-walk/SKILL.md)

Walk the palace from memory to self-test recall, score it, and repair weak loci. Use when the user says "test me on my palace", "let me recall the list", "walk my palace", "quiz me", or after a palace is built or due for review. Runs retrieval practice (the testing effect), marks which loci held and which failed, and updates the recall block of palace.json.

### `spaced-recall`

**Suite:** Memory Palace · **Step:** schedule · **Skill:** [`skills/spaced-recall/SKILL.md`](../skills/spaced-recall/SKILL.md)

Schedule spaced repetition over a memory palace so it lasts, and export to Anki. Use when the user says "spaced repetition", "when should I review", "schedule my reviews", "keep this long-term", "export to Anki", "FSRS", or "SM-2". Computes next-due dates from palace-walk grades, writes the recall block of palace.json, and drives durable retention against the forgetting curve.

**References:**

- [`anki-export.md`](../skills/spaced-recall/references/anki-export.md)

### `imagination-gym`

**Suite:** Memory Palace · **Step:** train · **Skill:** [`skills/imagination-gym/SKILL.md`](../skills/imagination-gym/SKILL.md)

Train mental-imagery vividness and scene construction so memory-palace images are stronger. Use when the user says "my mental pictures are weak/blurry", "I can't visualize", "train my imagination", "help me see images more clearly", or struggles to encode loci. Drills based on imagery research — multisensory detail, manipulation, and scene construction — to make encoding work better.

### `agent-memory-palace`

**Suite:** Memory Palace · **Step:** for agents · **Skill:** [`skills/agent-memory-palace/SKILL.md`](../skills/agent-memory-palace/SKILL.md)

Give an AI agent persistent, navigable memory across sessions using a memory-palace structure. Use when building agent memory, when the user says "remember this across sessions", "give the agent long-term memory", "persistent context", "knowledge graph for my agent", or for coding agents, Claude cowork, and ChatGPT projects that must retain state. Reads and writes palace.json as a durable spatial knowledge store the agent reloads each session.

### `palace-visualizer`

**Suite:** Memory Palace · **Step:** render · **Skill:** [`skills/palace-visualizer/SKILL.md`](../skills/palace-visualizer/SKILL.md)

Render a memory palace as a navigable artifact — a self-contained HTML viewer plus image-generation prompts for each locus. Use when the user says "render my palace", "visualize the palace", "make a picture of my memory palace", "build out the palace", or wants a keepable visual. Reads palace.json, emits a standalone index.html (no build step) and per-locus image prompts; tolerates both memory-palace and blessing schemas.

### `github-bless`

**Suite:** Blessing · **Step:** ingest · **Skill:** [`skills/github-bless/SKILL.md`](../skills/github-bless/SKILL.md)

Ingest a builder's GitHub (and optional connectors) and roll the week's work into a blessable set. Use when starting a weekly blessing, when the user says "what did I ship this week", "roll my week", "ingest my repos for the blessing", or before running the weekly-blessing skill. Reads commits and merged PRs across repos and emits a structured candidate list — it does not bless anything itself.

**References:**

- [`connectors.md`](../skills/github-bless/references/connectors.md)

### `weekly-blessing`

**Suite:** Blessing · **Step:** witness · **Skill:** [`skills/weekly-blessing/SKILL.md`](../skills/weekly-blessing/SKILL.md)

Run the weekly Sunday blessing ritual on a builder's work — witness what shipped, ratify what is whole, name what to ignore for seven days, and surface the one path forward. Use when the user says "run the weekly blessing", "do my Sunday review", "bless this week", or invokes /sunday or /bless. Writes weekly/YYYY-W##.md and appends to the blessing ledger. Invoked, never auto-fired.

**References:**

- [`voice-register.md`](../skills/weekly-blessing/references/voice-register.md)

### `palace-build`

**Suite:** Blessing · **Step:** grow · **Skill:** [`skills/palace-build/SKILL.md`](../skills/palace-build/SKILL.md)

Turn a builder's blessing ledger into a palace — emit palace/rooms.json for a React/Three.js renderer and a portable standalone HTML palace that works with no build step. Use when the user says "build my palace", "render the palace", "regenerate rooms.json", or after a weekly blessing adds new rooms. Reads blessings.jsonl + palace.md; writes rooms.json and an optional self-contained index.html.

**References:**

- [`3d-craft.md`](../skills/palace-build/references/3d-craft.md)

### `blessing-standard`

**Suite:** Blessing · **Step:** onboard · **Skill:** [`skills/blessing-standard/SKILL.md`](../skills/blessing-standard/SKILL.md)

Scaffold the five Blessing Protocol files (soul.md, agent.md, skills.md, palace.md, bless.md) into any repository and fill them from what the repo already is. Use when the user says "adopt bless here", "make this repo blessable", "scaffold the blessing files", "set up the mind palace standard". Reads the repo to draft soul.md first, then derives the rest; never overwrites a filled file without asking.

---

Built on SIP · Memory Palace Method v0.1 · The Blessing Protocol v0.1 · MIT
