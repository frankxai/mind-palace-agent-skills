---
name: blessing-standard
description: Scaffold the five Blessing Protocol files (soul.md, agent.md, skills.md, palace.md, bless.md) into any repository and fill them from what the repo already is. Use when the user says "adopt bless here", "make this repo blessable", "scaffold the blessing files", "set up the mind palace standard". Reads the repo to draft soul.md first, then derives the rest; never overwrites a filled file without asking.
---

# blessing-standard

> The onboarding step. Make any repo blessable by dropping in the five files — and fill them with
> the repo's actual essence, not empty boilerplate.

## When to use this

When a builder wants to adopt the Blessing Protocol in a new repo. Produces the five lowercase files
seeded from what the repo already contains, so the first weekly blessing has real ground to stand on.

## Instructions

1. **Read the repo.** README, existing `CLAUDE.md` / `AGENTS.md` / `SOUL.md`, package metadata,
   directory shape. Understand what this repo *is* before writing its soul.

2. **Draft `soul.md` first.** Everything inherits from it. Name 4–6 invariants (what must not drift)
   and the drift test. Pull the essence from the repo's own voice — do not impose a generic identity.

3. **Derive the other four** from `soul.md` + the repo:
   - `agent.md` — the operating contract (voice, behavioural rules, refusals, repo-specific hard stops).
   - `skills.md` — index the repo's existing skills/commands; always list `weekly-blessing` + `palace-build`.
   - `palace.md` — the room mapping (surface vocabulary, ordering) suited to this repo's domain.
   - `bless.md` — cadence + what's blessable here + an empty ledger table ready for the first blessing.

4. **Reconcile, don't duplicate.** If the repo already has SIP-tier files (`SOUL.md` / `AGENTS.md` /
   `SKILL.md`), make the lowercase file a short public projection that *points at* the substrate file
   rather than restating it (Blessing Protocol §6). Note the relationship in the file.

5. **Create the ledger scaffold.** `palace/blessings.jsonl` (empty) and a `weekly/` directory. Do not
   write a weekly entry — that is the first blessing's job, run intentionally.

6. **Respect existing files.** Never overwrite a filled `soul.md`/etc. without showing a diff and
   asking. Scaffolding is additive.

## Output

Report the files created/updated and the one next action: *"Run the weekly blessing when you're ready
to close this week."*

## Refusals

- Never write generic, soulless boilerplate — if you cannot find the repo's essence, ask the builder
  rather than inventing one.
- Never overwrite filled standard files silently.

## References

- Templates: `github.com/frankxai/bless/templates/`.
- The contract + reconciliation: Blessing Protocol §2 and §6.

---

Built on SIP · mind-palace-agent-skills · bless v0.1
