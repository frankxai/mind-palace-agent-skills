---
name: spaced-recall
description: Schedule spaced repetition over a memory palace so it lasts, and export to Anki. Use when the user says "spaced repetition", "when should I review", "schedule my reviews", "keep this long-term", "export to Anki", "FSRS", or "SM-2". Computes next-due dates from palace-walk grades, writes the recall block of palace.json, and drives durable retention against the forgetting curve.
---

# spaced-recall

> The durability step. Building encodes; spacing keeps it. Review each locus just before it would
> fade — not daily, not never.

## When to use this

The user wants a palace to survive weeks and months, asks when to review, or wants their loci in a
spaced-repetition tool (Anki). Pairs with `palace-walk`, which supplies the grades.

## Instructions

1. **Pick the scheduler:**
   - **FSRS** (Free Spaced Repetition Scheduler) — modern, evidence-led, models per-card stability
     and difficulty. Default. Targets a desired retention (e.g. 0.9) and spaces accordingly.
   - **SM-2** — the classic Anki algorithm; simpler ease-factor model. Use when matching legacy Anki
     decks or when the user explicitly wants it.

2. **Read the grades.** Take per-locus results from `palace-walk` (`got`/`partial`/`missed`, mapped
   to the scheduler's grade scale). A `missed` is a lapse and shortens the next interval sharply.

3. **Compute next-due.** Update each locus's `recall` block: `stability`, `difficulty`, `reps`,
   `lapses`, `lastReviewed`, and the new `due` (ISO date). New loci start with a short first
   interval; well-recalled loci stretch out.

4. **Surface today's queue.** When asked "what's due", list only loci whose `due` ≤ today, in route
   order, and hand them to `palace-walk`. Never front-load the whole palace — spacing is the point.

5. **Export to Anki** when asked — see `references/anki-export.md`: one note per locus
   (front = station/cue, back = target + image), preserving FSRS/SM-2 state where possible.

6. **Respect the no-guilt rule.** A skipped review is silent; just recompute from the real
   `lastReviewed`. No streak penalties, no nagging.

## Refusals

- Don't schedule reviews more often than the algorithm warrants ("review everything daily" wastes
  effort and isn't spacing).
- Don't fabricate `recall` state for loci that were never walked — schedule only what's been tested.

## References

- `references/anki-export.md` — the Anki export format.
- `spec/MEMORY-PALACE-METHOD.md` §4 (forgetting curve, spacing, FSRS/SM-2).

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
