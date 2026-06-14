---
name: recall
description: Walk a memory palace to self-test, then schedule the next review. Usage — /recall [palace-id] (defaults to the palace in the working directory)
allowed-tools: Read, Write, Edit, Grep, Glob
---

# /recall — walk and schedule

The retrieval loop, in order:

1. **Select** — load the `palace.json`. If `spaced-recall` state exists, walk only the loci due
   today (route order); otherwise walk the whole palace.
2. **Walk** — invoke `palace-walk`: at each station prompt for recall *before* revealing the stored
   image/target; score `got` / `partial` / `missed` per locus; repair weak loci on the spot.
3. **Schedule** — invoke `spaced-recall`: turn the grades into updated `recall` blocks (FSRS default)
   and compute each locus's next `due` date.
4. **Report** — show the score and what's queued next.

## Rules

- Never reveal the answer before the user attempts recall (preserve the testing effect).
- Honest scoring — a partial is not a `got`.
- A skipped review is silent; recompute from real `lastReviewed`. No streaks, no guilt.

## Output

```
✓ Walked "<title>" — got N · partial M · missed K
  Repaired: <loci>
  Next due: <date> (<count> loci)
```

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
