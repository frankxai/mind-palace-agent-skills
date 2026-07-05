# Contributing

This library has two suites: the **Memory Palace** suite (the method of loci, for humans and agents)
and the **Blessing Protocol** suite ([bless](https://github.com/frankxai/bless)). Contributions are
welcome — a new skill, a deeper `references/` file, a fix to a loop, or a clearer line. The bar is
restraint: a skill earns its place by doing one thing whole.

## The two voices

Match the voice of the suite you are touching — never leak one into the other.

- **Memory Palace** — instructional and evidence-grounded. Cite primary literature for empirical
  claims. **No neuro-myths** (no left/right-brain, "10% of the brain", "photographic memory",
  "learning styles"). Prefer "render / build out / visualize" over "manifest". See
  [`spec/MEMORY-PALACE-METHOD.md`](spec/MEMORY-PALACE-METHOD.md) §6.
- **Blessing** — the witness register. Read
  [`skills/weekly-blessing/references/voice-register.md`](skills/weekly-blessing/references/voice-register.md).
  Allowed: witness, ratify, bless, attend, orient, cadence, wholeness, sovereign, restraint, lineage,
  closure. Refused: manifest, abundance, vibration, energy, resonance, journey, sacred, transformation,
  awakening — and the AI-slop tells (*delve, unlock, unleash, elevate, dive deep, seamless*). No emoji
  as ornament.

## Adding a skill

1. Copy [`template/SKILL.md`](template/SKILL.md) to `skills/<name>/SKILL.md`. The directory name and
   the frontmatter `name` must match.
2. Write the frontmatter — two fields:

   ```yaml
   ---
   name: my-skill
   description: What the skill does AND when to use it, third person, with explicit trigger phrases. Use when ...
   ---
   ```

   - `name` — lowercase, hyphenated, ≤64 chars, matching `^[a-z0-9]+(?:-[a-z0-9]+)*$`, identical to the folder.
   - `description` — specific, non-empty, ≤1024 chars. Name the triggers; a vague description never activates.
3. Keep the body surgical (under ~500 lines). Push depth into `skills/<name>/references/*.md`
   deep-dives (real substance, no padding) and link them from a `## References` section.
4. If the skill auto-activates, add a rule to [`skill-rules.json`](skill-rules.json). The validator
   checks both directions: every rule references a real skill, and every skill has a rule.

## Assets

- The HTML viewer (`assets/palace-viewer/index.html`) is self-contained (procedural textures), so it
  needs no committed images. Optional high-res textures/scenes are *generated on demand* from
  [`assets/manifest.json`](assets/manifest.json) — keep any committed images small (WebP, well under
  100 KB). Per-locus art belongs to the builder, not this library. See
  [`assets/ASSETS.md`](assets/ASSETS.md).

## Before you open the PR

```bash
python3 scripts/validate_skills.py            # frontmatter + structure + rules consistency
python3 scripts/generate_catalog.py           # regenerate docs/CATALOG.md + docs/index.html
python3 scripts/generate_catalog.py --check   # confirm they are in sync (exits 1 on drift)
python3 scripts/build_dist.py --no-assets     # confirm the kits build
```

If you added, renamed, or removed a skill or a reference, the catalog **must** be regenerated and
committed — the `--check` step fails the build otherwise. Open the PR as a **draft** against `main`.

## What does not get merged

- Skills that restate another skill instead of doing one thing whole.
- Refused-register vocabulary (Blessing) or neuro-myths (Memory Palace).
- A skill without `references/` depth where the topic clearly has more to say.
- Generated `docs/` left out of sync with the skills.

---

Built on SIP · Memory Palace Method v0.1 · The Blessing Protocol v0.1 · MIT
