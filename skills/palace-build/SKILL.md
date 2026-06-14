---
name: palace-build
description: Turn a builder's blessing ledger into a palace — emit palace/rooms.json for a React/Three.js renderer and a portable standalone HTML palace that works with no build step. Use when the user says "build my palace", "render the palace", "regenerate rooms.json", or after a weekly blessing adds new rooms. Reads blessings.jsonl + palace.md; writes rooms.json and an optional self-contained index.html.
---

# palace-build

> The build step. Blessed work becomes rooms; rooms become a place. The palace grows more
> beautiful each week, not more crowded — restraint over accumulation.

## When to use this

After a weekly blessing, or whenever the ledger changed and the palace should reflect it. Produces
two artifacts: the machine-readable `rooms.json` (for the Next.js + react-three-fiber renderer) and
a portable standalone `index.html` (so a builder gets a palace even with no toolchain).

## Instructions

1. **Read the ledger + manifest.** `palace/blessings.jsonl` (what is whole) and `palace.md` (how it
   maps to rooms: surface vocabulary, ordering, accents).

2. **Build the room set.** One blessing → at most one room. For each, produce a room object per the
   Blessing Protocol §5 schema:
   ```json
   {"id":"acos","name":"Agentic Creator OS","path":"frankxai/agentic-creator-os","kind":"os","week":"2026-W24","ring":0,"truth":"<one line>","surface":"obsidian","accent":"#7da3ff"}
   ```
   - `name` is a **named artifact**, never a category badge.
   - Assign `ring` by week — oldest week is ring `0`; later weeks accrue outward.
   - Assign `surface` by the nature of the thing (infra → `slate`/`obsidian`; creative → `aurora`/`glass`;
     canon → `bronze`/`marble`). Distinct surfaces — never six recolors of one orb.

3. **Write `palace/rooms.json`.** Wrap rooms with `version`, `owner`, and the array. Validate it parses.

4. **Render the portable HTML (optional but default).** Emit a single self-contained `index.html`:
   - One `<canvas>` with a light Three.js scene via CDN (`<script type="importmap">` + ESM), or a
     pure-CSS constellation fallback if 3D is declined.
   - One strong warm key light + one cool rim. No global bloom. Dark background (`#09090b`).
   - Each room is a named plinth/orb with its `truth` legible on hover/select.
   - Respect `prefers-reduced-motion` — disable idle camera drift when set.
   - No external data fetch: inline the room data into the file so it works offline.

5. **Keep the schema as the single source of truth.** `rooms.json` is consumed unchanged by the
   `frankx-palace` renderer. Do not invent fields the spec doesn't define; supply defaults for missing
   optional fields rather than failing.

## Design discipline (from the 3D memory-palace research)

- One strong directional light, not five. Warm key (`#ffe5cc`) + cool rim (`#7da3ff`) + low ambient.
- Selective bloom on emissive accents only — never global postprocessing.
- Glass that preserves legibility: thickness ~0.25, chromatic aberration ~0.02 (high values look
  luxurious but make labels unreadable).
- Camera motion is half the perceived premium — damp it; bind reveals to input, not wall-clock.
- Artifact-first: a room has weight and a name, like a book on a shelf — not a category chip.

## Refusals

- Never create a room for unblessed work. The palace renders closure, not backlog.
- Never overcrowd — if a week blessed many small things, group or summarise rather than spawn clutter.

## References

- Blessing Protocol §5 (room schema): `github.com/frankxai/bless`.
- Renderer: `github.com/frankxai/frankx-palace` (Next.js + react-three-fiber reference).
- 3D craft: the Starlight 3D-memory-palace survey (one light, selective bloom, legible glass).

---

Built on SIP · mind-palace-agent-skills · bless v0.1
