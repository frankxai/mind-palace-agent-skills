---
name: palace
description: Build or rebuild the palace from the blessing ledger — regenerate rooms.json and the portable HTML palace. Usage — /palace [build|status]
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /palace — grow the palace

Invoke the `palace-build` skill.

## Modes

- `/palace build` (default) — read `palace/blessings.jsonl` + `palace.md`, regenerate
  `palace/rooms.json` and the portable `index.html`. One blessing → at most one room; rooms accrue
  by week as concentric rings.
- `/palace status` — report the current palace: room count, rings, newest week, surfaces in use.

## Discipline

- The palace renders **closure, not backlog** — only blessed work becomes rooms.
- More beautiful, not more crowded. Restraint over accumulation.
- A room is a named artifact with weight, never a category badge.

## Output

```
✓ Palace rebuilt
  Rooms: R across W weekly rings · newest: 2026-W24
  Wrote: palace/rooms.json (+ index.html)
```

---

Built on SIP · bless v0.1 · Voice: Palace Architect
