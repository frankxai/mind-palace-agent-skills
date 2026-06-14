# Connectors — rolling a week honestly

`github-bless` gathers; it never judges. Its one inviolable duty is an honest witness: every candidate is
real, every gap is named. This reference is the mechanics of rolling a week from git and GitHub, and the
discipline for folding in connector signals without letting them lie.

## Defining the window

Seven days ending on the most recent Sunday on or before the anchor date (default: today). State the exact
window in the candidate set so the reader can audit it — e.g. `2026-06-08 → 2026-06-14, ISO week 2026-W24`.
Never widen the window to "feel productive." The week is the week; a thin week is reported thin.

## Rolling from git directly

When the repos are on disk, git is the ground truth and needs no network:

```bash
# commits in the window, one repo, subject lines only
git -C <repo> log --since="2026-06-08" --until="2026-06-15" --pretty=format:'%h %s'

# group intent by conventional-commit prefix
git -C <repo> log --since="2026-06-08" --until="2026-06-15" --pretty=format:'%s' \
  | grep -oE '^(feat|fix|ship|refactor|docs|chore)(\([^)]+\))?' | sort | uniq -c | sort -rn

# tags cut in the window
git -C <repo> tag --sort=-creatordate --format='%(refname:short) %(creatordate:short)'
```

Prefer conventional-commit prefixes (`feat:`, `fix:`, `ship:`, `feat(scope):`) to infer intent, and group by
scope. Summarise each repo in 1–3 lines — never paste a raw `git log` into the candidate set.

## Rolling from GitHub (MCP or gh)

When repos are not local, or to catch merged PRs and releases, use the GitHub MCP tools or the `gh` CLI:

- **MCP:** `search_repositories` to enumerate active repos, `list_commits` per repo within the window,
  `list_pull_requests` filtered to merged in-window, `list_releases` for tags cut.
- **gh CLI:**

  ```bash
  # merged PRs this week across an owner
  gh search prs --owner <owner> --merged ">=2026-06-08" --json repository,title,number,mergedAt

  # commits in one repo's default branch
  gh api "repos/<owner>/<repo>/commits?since=2026-06-08T00:00:00Z&until=2026-06-15T00:00:00Z" \
    --jq '.[].commit.message | split("\n")[0]'
  ```

For each repo collect: commits (grouped by scope), merged PRs (title + one-line outcome), releases/tags. The
provenance — SHAs, PR numbers — travels with each candidate so `weekly-blessing` can cite `commitAtBlessing`
when it ratifies.

## Folding in connector signals honestly

Beyond code, a builder's week often shows up elsewhere: issues closed, content published, music released,
deploys shipped, a workshop delivered. Fold these in as additional candidates, each tagged with its source:

```
- [content]  3 posts published — 2 long-form, 1 newsletter. (source: blog RSS)
- [deploy]   frankx.ai deployed 4× this week, all green. (source: Vercel)
- [music]    2 tracks released to Spotify. (source: Distrokid)
```

The rule for connectors is the same as for git: **a signal you cannot verify is not a candidate.** Do not
infer a deploy from a commit, or a release from a draft. If the connector is the source, the connector must
have actually said so.

## Naming every gap

A silent gap produces a dishonest witness — the one failure mode this skill must never have. Mark gaps
explicitly with `[gap]` and say *why*:

```
- [gap]  arcanea-ai-app — UNREACHABLE this run (auth/clone failed). Noted, not dropped.
- [gap]  Spotify connector — not configured; music releases this week are unknown, not zero.
```

The distinction in that last line is load-bearing: **unknown is not zero.** A missing connector means the
witness cannot see, not that nothing happened. Reporting "no music this week" when the connector is simply
absent is a lie of omission. Report the blindness instead.

## What github-bless never does

- Never fabricate commits, PRs, counts, or connector signals. Unreachable → `[gap]`, always.
- Never bless or rank — it emits candidates only. Wholeness is decided in `weekly-blessing`.
- Never widen the window, and never convert an absent connector into a confident "zero."

Hand the candidate set — with its gaps intact — to `weekly-blessing`.
