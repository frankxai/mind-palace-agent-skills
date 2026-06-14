---
name: bless
description: Ratify a single piece of work as whole-at-this-moment. The Witness voice. Records the blessing in palace/blessings.jsonl. Use when one thing has reached internal coherence and further iteration would be restlessness, not improvement. Usage — /bless <slug-or-path> [reason]
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /bless — single-piece ratification

Anytime. Closes one thing.

> **Blessed = whole at this moment.** Further iteration is creator-restlessness, not improvement.
> Future-you may extend it from a new vantage; present-you does not.

## Process

1. Locate the target (path, route, slug, repo, or practice). Verify it exists.
2. Read its recent state — last few commits, its README/skill if present.
3. Sanity check: is it actually finishable, and not mid-flight? Refuse if there's an open PR,
   failing tests, or uncommitted churn in the relevant files.
4. Append one record to `palace/blessings.jsonl` (Blessing Protocol §4 schema) and add the row to
   the human table in `bless.md`.

## Refusals

- Mid-flight work → STOP. The witness does not bless what is still moving.
- Too young (< 7-day soak, soft default) → STOP unless given an explicit reason.
- Offered out of restlessness ("I want to move on") → surface it, ask for a clearer reason.

## Output

```
✓ Blessed: <slug>
  Ratified: <ISO> · Reason: <one sentence>
  Recorded: palace/blessings.jsonl
```

Blessings are private by default — they surface in the weekly entry, not as public posts.

---

Built on SIP · bless v0.1 · Voice: The Witness
