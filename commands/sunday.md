---
name: sunday
description: Run the weekly Sunday blessing — ingest the week, witness what is whole, grow the palace. Portable command from the Blessing Protocol. Usage — /sunday [optional-week-anchor like 2026-06-14]
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /sunday — the weekly blessing

The full Sunday loop, in order:

1. **Ingest** — invoke the `github-bless` skill to roll the week across the builder's repos and
   connectors. Name every gap explicitly.
2. **Witness** — invoke the `weekly-blessing` skill to compose `weekly/YYYY-W##.md` (six sections),
   ratify what is whole, and append blessing records to `palace/blessings.jsonl`.
3. **Grow** — invoke the `palace-build` skill to regenerate `palace/rooms.json` (and the portable
   HTML palace) so the palace reflects this week's blessings.

## Rules

- Invoked, never auto-fired. A skipped week is silent.
- The witness voice: calm, sovereign, non-compulsive. No spiritual-bypass vocabulary.
- Refuse a future week. Refuse to bless mid-flight work.

## Output

```
✓ Sunday blessing complete — 2026-W24
  Blessed: N · Deferred: M · Rooms now: R
  This week's path: <one sentence>
  Filed: weekly/2026-W24.md
```

---

Built on SIP · bless v0.1 · Voice: The Witness
