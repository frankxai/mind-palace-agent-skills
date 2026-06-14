---
name: palace-walk
description: Walk the palace from memory to self-test recall, score it, and repair weak loci. Use when the user says "test me on my palace", "let me recall the list", "walk my palace", "quiz me", or after a palace is built or due for review. Runs retrieval practice (the testing effect), marks which loci held and which failed, and updates the recall block of palace.json.
version: 0.1
---

# palace-walk

> The retrieval step. Recalling is what makes memory durable — re-reading is not. Make the user
> walk the route and *produce* each item before showing them anything.

## When to use this

A palace exists and the user wants to practise, self-test, or do a scheduled review. This is where
learning actually consolidates.

## Instructions

1. **Walk in route order.** Take rooms and stations in their fixed order from `palace.json`. At each
   station, prompt for recall *before* revealing anything: "Station: kitchen table — what's here?"

2. **Test, don't show.** Let the user attempt retrieval cold. Reveal the stored `image.text` and
   `target` only after their attempt. The effortful attempt is the active ingredient, even when it
   fails (productive failure).

3. **Score each locus** honestly: `got` (clean), `partial` (image but not target, or vice versa),
   `missed`. Record per-locus, not just a total.

4. **Repair on the spot.** For `partial`/`missed`, diagnose: weak image (→ re-encode via
   `loci-encoder` with stronger levers), crowded station (→ ask `memory-palace-architect` to add
   spacing), or just under-rehearsed (→ schedule sooner). Make the fix, then re-walk that locus.

5. **Update recall state.** Write each locus's `recall` block (or create it on first review):
   `reps`, `lapses`, `lastReviewed`, and hand the grades to `spaced-recall` to compute the next
   `due` date and stability/difficulty.

6. **Report the walk.** End with a terse line: items tested, `got`/`partial`/`missed` counts, and
   the loci queued for repair. No celebration — just the state.

## Refusals

- Never reveal the answer before the user attempts recall — that turns a test back into re-reading
  and kills the testing effect.
- Don't mark a locus `got` on a partial; honest scoring is what makes the schedule work.

## References

- `spec/MEMORY-PALACE-METHOD.md` §4 (testing effect, durability).

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
