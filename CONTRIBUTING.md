# Contributing

Thanks for improving `mind-palace-agent-skills`. The bar is high and the rules are few.

## Authoring a skill

1. Copy [`template/SKILL.md`](template/SKILL.md) to `skills/<your-skill>/SKILL.md`.
2. `name` must be lowercase-hyphenated, ≤64 chars, and **match the directory name**.
3. `description` must be **a single line**, ≤1024 chars, third person, stating *what* the skill
   does and *when* to use it, with real trigger keywords. Do **not** wrap it onto a second line and
   do **not** use YAML folded (`>`) or literal (`|`) markers — the zero-dep validator reads one line.
4. Keep `SKILL.md` under ~500 lines. Push number tables, long recipes, and deep notes into
   `skills/<your-skill>/references/`. Scripts go in `scripts/`, bundled files in `assets/`.
5. Register the skill in [`skill-rules.json`](skill-rules.json) — **every** skill directory needs an
   entry, or validation fails.

## Voice

- Memory Palace suite: instructional, evidence-grounded. Cite primary literature for empirical
  claims. **No neuro-myths** (no left/right-brain, "10% of brain", "photographic memory",
  "learning styles"). Prefer "render / build out / visualize" over "manifest".
- Blessing suite: the Witness register defined by the [Blessing Protocol](https://github.com/frankxai/bless)
  SPEC §7. Do not leak one suite's voice into the other.

## Assets

- Committed images under `assets/` are generated (Higgsfield) and MIT-licensed alongside the repo.
  Keep them small: textures as WebP, ~1024², well under 100 KB each; few starter scenes.
- Per-locus images that a user generates for their own palace are theirs, not committed here.

## Before opening a PR

```bash
python scripts/validate_skills.py            # must print: OK — N skills valid
python scripts/generate_catalog.py --check   # CATALOG.md must be up to date
python scripts/build_dist.py --no-assets     # build must succeed
```

Regenerate the catalog after adding/renaming/removing a skill:

```bash
python scripts/generate_catalog.py
```

Open the PR as a **draft** against `main`. CI re-runs all three checks.

## License

MIT. By contributing you agree your work ships under it.
