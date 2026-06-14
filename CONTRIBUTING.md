# Contributing

This is the portable agent-skills layer of the [Blessing Protocol](https://github.com/frankxai/bless).
Contributions are welcome — a new skill, a deeper `references/` file, a fix to the loop, or a clearer line.
The bar is restraint: a skill earns its place by doing one thing whole, in the witness register.

## The voice

Everything here speaks in one register. Before opening a PR, read
[`skills/weekly-blessing/references/voice-register.md`](skills/weekly-blessing/references/voice-register.md).
In short:

- **Allowed:** witness, ratify, bless, attend, orient, cadence, wholeness, sovereign, restraint, lineage, closure.
- **Refused:** manifest, abundance, vibration, energy, resonance, alignment-with-the-universe, journey, sacred,
  transformation, awakening — and the ordinary AI-slop tells (*delve, unlock, unleash, elevate, dive deep,
  seamless*). No emoji as ornament.

## Adding a skill

1. Create `skills/<name>/SKILL.md`. The directory name and the frontmatter `name` must match.
2. Write the frontmatter — exactly two fields:

   ```yaml
   ---
   name: my-skill
   description: What the skill does AND when to use it, third person, with explicit trigger phrases. Use when ...
   ---
   ```

   - `name` — lowercase, hyphenated, ≤ 64 chars, matching `^[a-z0-9]+(?:-[a-z0-9]+)*$`, identical to the folder.
   - `description` — specific, non-empty, ≤ 1024 chars. Name the triggers; a vague description never activates.

3. Keep the body surgical. Push depth into `skills/<name>/references/*.md` deep-dives (≈ 60–150 lines each, real
   substance, no padding) and link them from a `## References` section in the SKILL.md.
4. If the skill auto-activates, add a rule to [`skill-rules.json`](skill-rules.json). The validator checks that
   every rule references a skill that exists.

## Before you open the PR

Run both checks — CI runs the same two on every push and PR to `main`:

```bash
python3 scripts/validate_skills.py        # frontmatter + structure + rules consistency
python3 scripts/generate_catalog.py       # regenerate docs/CATALOG.md + docs/index.html
python3 scripts/generate_catalog.py --check   # confirm they are in sync (exits 1 on drift)
```

If you added, renamed, or removed a skill or a reference, the catalog **must** be regenerated and committed —
the `--check` step fails the build otherwise.

## What does not get merged

- Skills that restate another skill instead of doing one thing whole.
- Refused-register vocabulary, or any line that would make a skeptical engineer wince read aloud.
- A skill without `references/` depth where the topic clearly has more to say.
- Generated `docs/` left out of sync with the skills.

---

Built on SIP · The Blessing Protocol v0.1 · MIT
