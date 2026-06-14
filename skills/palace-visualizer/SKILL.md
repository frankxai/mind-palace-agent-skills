---
name: palace-visualizer
description: Render a memory palace as a navigable artifact — a self-contained HTML viewer plus image-generation prompts for each locus. Use when the user says "render my palace", "visualize the palace", "make a picture of my memory palace", "build out the palace", or wants a keepable visual. Reads palace.json, emits a standalone index.html (no build step) and per-locus image prompts; tolerates both memory-palace and blessing schemas.
version: 0.1
---

# palace-visualizer

> The render step — build the palace out into something you can see, walk, and keep. The agent
> helps make the imagined place concrete.

## When to use this

A palace exists in `palace.json` (or a Blessing `rooms.json`) and the user wants a visual artifact:
a navigable HTML scene, and/or image prompts to generate art for each locus.

## Instructions

1. **Read the source and branch on `type`.** `"memory-palace"` → render the nested
   room → station → locus hierarchy. `"blessing"` (or a `rooms.json`) → render the flat rooms. The
   shared `surface`/`accent` vocabulary means one renderer serves both.

2. **Emit a standalone `index.html`.** Start from `assets/palace-viewer/index.html` and inline the
   palace data so the file works offline with no build step and no fetch. One `<canvas>`, Three.js
   via CDN `importmap` + ESM, with a pure-CSS fallback if 3D is declined.

3. **Hold the craft discipline** (identical to `palace-build`, so both palaces look like one family):
   - One warm key light (`#ffe5cc`) + one cool rim (`#7da3ff`) + low ambient. Not five lights.
   - Dark background (`#09090b`). Selective bloom on emissive accents only — never global.
   - Glass that stays legible (thickness ~0.25, low chromatic aberration). Labels must read.
   - Damp camera motion; bind reveals to input. Respect `prefers-reduced-motion` (disable idle drift).
   - Each locus is a named plinth/orb; its `image.text` (or room `truth`) is legible on hover/select.
   - Map each room's `surface` to `assets/textures/<surface>.webp`, falling back to flat `accent`
     colour if the texture is missing — so a lone copied `index.html` still renders.

4. **Generate per-locus image prompts.** For each locus, derive an image-gen prompt from
   `image.text` (or write one if absent) and store it in `image.prompt`. Prompt template:
   *"<image.text>, dramatic single key light, dark background, photographic, highly detailed,
   no text"*. These can be rendered via the `~~image-generation` connector (e.g. Higgsfield) and the
   result path written back to `image.asset`.

5. **Keep `palace.json` the source of truth.** The viewer is a projection; never edit facts in the
   HTML. If the palace changes, re-render.

## Refusals

- Never overcrowd the scene — if a room holds many loci, group or summarise rather than spawn clutter.
- Never bake external data fetches into the standalone file; inline the data.
- Don't invent rooms/loci not present in the source; render what is there.

## References

- `assets/palace-viewer/index.html` — the standalone viewer/builder this skill ships and inlines.
- `assets/textures/` — the six surface textures.
- `spec/MEMORY-PALACE-METHOD.md` §5; Blessing SPEC §5 for the `rooms.json` branch.

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
