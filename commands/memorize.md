---
name: memorize
description: Memorize something with a memory palace — design the structure, then encode each item as a vivid image. Usage — /memorize <what to remember> (e.g. /memorize the 12 cranial nerves)
allowed-tools: Read, Write, Edit, Grep, Glob
---

# /memorize — build a palace for a target

The encode loop, in order:

1. **Orient (if new)** — invoke `palace-foundations` to confirm the user knows the method and to
   pick the right path. Skip if they're already fluent.
2. **Design** — invoke `memory-palace-architect`: count the items, choose a place they know, lay a
   fixed route, space the stations, assign each room a `surface`/`accent`. Write the `palace.json`
   skeleton per `spec/palace.schema.json`.
3. **Convert numbers first** — if the target is digits/dates/cards, invoke `number-memory` to turn
   them into images before placing.
4. **Encode** — invoke `loci-encoder` to make one vivid image per locus (bizarre, multisensory,
   interacting with the station) and fill `palace.json`'s `loci[]`.
5. **First walk** — offer an immediate `palace-walk` so the user feels it stick, then suggest
   `/recall` for scheduled review.

## Rules

- Real place over imagined; fixed non-crossing route; one item per station.
- No bland literal images — those are not encodings.
- This builds a memory palace (`palace.json`), distinct from the Blessing `/palace`.

## Output

```
✓ Palace built — "<title>"
  Rooms: R · Stations: S · Loci encoded: N
  File: palace.json
  Next: /recall to walk and schedule it
```

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
