---
name: weekly-blessing
description: Run the weekly Sunday blessing ritual on a builder's work — witness what shipped, ratify what is whole, name what to ignore for seven days, and surface the one path forward. Use when the user says "run the weekly blessing", "do my Sunday review", "bless this week", or invokes /sunday or /bless. Writes weekly/YYYY-W##.md and appends to the blessing ledger. Invoked, never auto-fired.
---

# weekly-blessing

> The heart of the Blessing Protocol. The witness voice. Reflective, sovereign, non-compulsive.
> The reader should feel permission, not pressure.

## When to use this

On Sunday (or when invoked), to close the week. Consumes the candidate set from `github-bless`
(run it first if the week has not been rolled). Produces one weekly entry and updates the ledger.
Never auto-fires on a hook — a skipped week is silent.

## Instructions

1. **Gather inputs.** The week's candidate set (`github-bless`), the current `bless.md` ledger, and
   the previous `weekly/*.md` entry (continuity matters — reference last week's deferred items honestly).

2. **Compose the entry** at `weekly/YYYY-W##.md` (ISO week) with this exact six-section structure:
   - **§0 — The structural truth.** One paragraph: what the system actually *became* this week.
   - **§1 — What is whole and should be blessed.** Wholeness, not completeness. For each item,
     decide if it passes the blessing test (below). Each blessed item also gets a ledger record.
   - **§2 — Structurally important but unfinished.** The load-bearing gaps, ranked.
   - **§3 — Ignore for the next seven days.** Explicit permission to not-do. This list is the leverage.
   - **§4 — The one highest-leverage path for the coming week.** One sentence, then the unpacking.
   - **§5 — Handover note.** Code-block formatted; copies cleanly into the next session's prompt.

   Length: 800–1500 words. Surgical, not exhaustive.

3. **Apply the blessing test** to each §1 candidate:
   > Whole at this moment? Further iteration would be creator-restlessness, not improvement?
   > Soaked ≥7 days against reality? No open PR / failing tests / uncommitted churn?
   If yes → bless. If no → it belongs in §2, not §1.

4. **Append blessing records.** For each blessed item, append one line to `palace/blessings.jsonl`:
   ```json
   {"id":"bless_<ts>_<slug>","slug":"...","path":"...","ratifiedAt":"<ISO>","reason":"<one sentence>","scope":"file|dir|repo|os|route|practice","commitAtBlessing":"<sha>","week":"YYYY-W##"}
   ```
   Also add the row to the human table in `bless.md`.

5. **Report tersely.** File path + counts. Do not announce, do not celebrate.
   ```
   ✓ Weekly blessing filed: weekly/2026-W24.md
     Blessed: N · Deferred: M · This week's path: <one sentence>
   ```

## Voice rules (load-bearing)

- Calm, sovereign, non-compulsive. Permission, not pressure.
- Allowed register: witness, ratify, bless, attend, orient, cadence, structural, wholeness, sovereign, restraint.
- Refused: manifest, abundance, vibration, energy, resonance, alignment-with-the-universe, journey, sacred, transformation, awakening.
- No emoji. No ornament beyond `---`. No hagiography — a blessed thing is named, not celebrated.
- No future tense for work that has not shipped. The witness sees only what *is*.

## Refusals

- Refuse a future week (the witness only sees what is).
- Refuse to bless mid-flight work, work too young, or work offered out of restlessness — push back and ask.
- Refuse to inflate to monthly/quarterly/annual. This is the weekly cadence.

## Hand-off

After filing, `palace-build` can regenerate the palace from the updated ledger + `palace.md` mapping.

## References

- Blessing Protocol §3 (output structure), §3.3 (blessing definition), §3.4 (refusals), §7 (voice):
  `github.com/frankxai/bless`.
- Lineage: the FrankX `starlight-chronicle` skill (the private reference implementation).

---

Built on SIP · mind-palace-agent-skills · bless v0.1
