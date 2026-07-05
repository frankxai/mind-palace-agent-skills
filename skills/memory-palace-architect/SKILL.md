---
name: memory-palace-architect
description: Design a memory palace — choose a real or imagined locus, lay a fixed non-crossing route, and space the stations. Use when the user says "design a memory palace", "pick a place to memorize in", "lay out my palace", "map a route for N items", or needs a structure before encoding. Writes the rooms/stations skeleton of palace.json for loci-encoder to fill.
---

# memory-palace-architect

> The design step. A good palace is a place you already know, walked in a fixed order, with room
> for every item and no two items crowding one spot.

## When to use this

The user has a memorization target (a list, a speech, a syllabus, a deck of cards) and needs the
spatial structure to hold it. This skill produces the empty palace; `loci-encoder` fills it.

## Instructions

1. **Count the targets.** Establish how many discrete items must be placed. This sets how many
   stations (loci) the palace needs — aim for a little headroom, not a tight fit.

2. **Choose the locus.** Prefer a **real place the user knows cold** (childhood home, daily commute,
   workplace). Real beats imagined because the spatial detail is already encoded. If imagined, build
   it from a familiar template and keep it stable across sessions. Offer a starter scene from
   `assets/scenes/` if they want a ready-made shell.

3. **Lay a fixed, non-crossing route.** Walk it the same way every time — e.g. always clockwise,
   always entering rooms left-to-right. A consistent route is what preserves *order* on recall.
   Never let the path cross itself or fork.

4. **Place stations with spacing.** Within each room, pick fixed features as stations (door, window,
   table, lamp) in route order. Leave clear gaps — crowded loci blur into each other. One memorable
   item per station.

5. **Choose alternative structures when they fit:**
   - **Body method (loci-on-self):** for ~10 quick items with no place handy — toes, knees, belt,
     chest, etc., bottom to top.
   - **Peg structures** (rhyming/alphabet pegs) for short ordered lists; hand off numeric pegs to
     `number-memory`.

6. **Assign the material vocabulary.** Give each room a `surface` from the shared enum
   (`obsidian | glass | bronze | marble | aurora | slate`) and one hex `accent`, so the palace
   renders distinctly (not six recolors of one room). Match surface to the room's feel.

7. **Write the skeleton.** Emit `palace.json` per `spec/palace.schema.json` with `type`,
   `version`, `id`, `title`, `locus`, and the `rooms[]` → `stations[]` populated but `loci` left
   for `loci-encoder`. Validate it parses.

## Refusals

- Never design a crossing or branching route — it destroys order recall.
- Never overcrowd a station with multiple items to save space; add a station instead.
- Don't invent schema fields; default missing optional ones.

## References

- `spec/MEMORY-PALACE-METHOD.md` §2 (route discipline, spacing) and §5 (schema).
- `assets/scenes/` — archetypal starter-palace shells.

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
