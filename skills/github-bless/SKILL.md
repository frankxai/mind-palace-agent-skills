---
name: github-bless
description: Ingest a builder's GitHub (and optional connectors) and roll the week's work into a blessable set. Use when starting a weekly blessing, when the user says "what did I ship this week", "roll my week", "ingest my repos for the blessing", or before running the weekly-blessing skill. Reads commits and merged PRs across repos and emits a structured candidate list — it does not bless anything itself.
---

# github-bless

> The ingest step of the Blessing Protocol. Read the week. Surface what changed. Hand a clean
> candidate set to `weekly-blessing`. Witness honestly — never invent activity, never hide a gap.

## When to use this

At the start of a weekly blessing, or any time the builder wants an honest roll-up of the last
seven days across their repositories and connectors. This skill **gathers**; it does not judge,
ratify, or write the weekly entry. That is `weekly-blessing`'s job.

## Instructions

1. **Define the week.** Seven days ending on the most recent Sunday on or before the anchor date
   (default: today). State the exact window (e.g. `2026-06-08 → 2026-06-14, ISO week 2026-W24`).

2. **List the repos in scope.** Read `bless.md` / `palace.md` for a declared repo set if present.
   Otherwise ask the builder, or use the GitHub MCP tools (`search_repositories`, `list_commits`,
   `list_pull_requests`) / `gh` CLI to enumerate repos with activity in the window.

3. **Roll each repo's week.** For each repo, collect:
   - Commits in the window — prefer conventional-commit prefixes (`feat:`, `fix:`, `ship:`,
     `feat(scope):`) to infer intent. Group by scope.
   - Merged PRs in the window (title + one-line outcome).
   - Releases/tags cut, if any.
   Summarise each repo in 1–3 lines. Do not paste raw git logs into the candidate set.

4. **Pull connector signals (optional).** If connectors are configured (issues closed, content
   published, music released, deploys shipped), fold them in as additional candidates, each tagged
   with its source.

5. **Emit the candidate set.** A compact structured list the `weekly-blessing` skill consumes:
   ```
   ## Blessing candidates — 2026-W24 (2026-06-08 → 2026-06-14)
   - [repo] agentic-creator-os — v10 safety hooks + agent IAM landed. (12 commits, 3 PRs)
   - [repo] Starlight-Intelligence-System — composition layer + crypto IS. (8 commits)
   - [gap]  arcanea-ai-app — UNREACHABLE this run (auth/clone failed). Noted, not dropped.
   ```

6. **Name every gap explicitly.** If a repo is unreachable, a connector is down, or the window is
   partial, say so in the candidate set with a `[gap]` marker. A silent gap produces a dishonest
   witness — the one thing this skill must never do.

## Refusals

- Never fabricate commits, PRs, or counts. If you cannot reach a source, mark it `[gap]`.
- Never bless or rank — emit candidates only. Wholeness is decided in `weekly-blessing`.
- Never widen the window to "feel productive" — the week is the week.

## Hand-off

Pass the candidate set to **`weekly-blessing`**. Provenance (commit SHAs, PR numbers) travels with
each candidate so the blessing record can cite `commitAtBlessing`.

## References

- Blessing Protocol §3 (ritual inputs) and §4 (record schema): `github.com/frankxai/bless`.
- Week-roll lineage: the FrankX `scripts/chronicle-roll-week.mjs` auto-roll pattern.

---

Built on SIP · mind-palace-agent-skills · bless v0.1
