---
name: palace-new
description: Start a new, empty memory palace from a place you know — the structure, before any items. Usage — /palace-new [place] (e.g. /palace-new my childhood home)
allowed-tools: Read, Write, Edit, Grep, Glob
---

# /palace-new — create an empty memory palace

Stands up the spatial structure so you can fill it later with `/memorize`.

1. **Choose the locus** — invoke `memory-palace-architect`. Prefer a real place the user knows; or
   offer a starter shell from `assets/scenes/`.
2. **Lay the route** — fixed, non-crossing; pick stations (fixed features) in route order with clear
   spacing.
3. **Assign materials** — give each room a `surface` (`obsidian | glass | bronze | marble | aurora |
   slate`) and one hex `accent`.
4. **Write** — emit a valid `palace.json` (`type: "memory-palace"`) with rooms and stations but
   empty `loci`, ready for `/memorize`.

## Note — not the Blessing `/palace`

This creates a **memory palace** (`palace.json`, the method of loci). The Blessing suite's `/palace`
rebuilds a *blessing* palace (`palace/rooms.json`) from a closure ledger. Different artifact,
different command.

## Output

```
✓ Empty palace created — "<title>"
  Rooms: R · Stations: S (loci: 0)
  File: palace.json
  Next: /memorize <target>
```

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
