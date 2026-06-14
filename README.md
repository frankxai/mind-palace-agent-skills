# mind-palace-agent-skills

Portable agent skills that run the [Blessing Protocol](https://github.com/frankxai/bless) — ingest a
builder's GitHub, witness the week, and grow a palace from what is whole.

Install into any agent runtime that reads `SKILL.md` skills (Claude Code, Claude.ai, Cursor, Codex,
Gemini, and others). Each skill is self-contained and follows the two-field frontmatter convention
(`name` + `description`).

## The skills

| Skill | Step | Does |
|---|---|---|
| [`github-bless`](skills/github-bless/SKILL.md) | ingest | Roll the week's commits/PRs across repos + connectors into a candidate set. Names every gap. |
| [`weekly-blessing`](skills/weekly-blessing/SKILL.md) | witness | The Sunday ritual — six-section entry, ratify what is whole, append the ledger. |
| [`palace-build`](skills/palace-build/SKILL.md) | grow | Turn the ledger into `rooms.json` + a portable HTML palace. |
| [`blessing-standard`](skills/blessing-standard/SKILL.md) | onboard | Scaffold the five Blessing Protocol files into any repo, filled from what the repo is. |

## Commands

`/sunday` (the full loop) · `/bless <slug>` (single-piece ratification) · `/palace` (rebuild the palace).
Auto-activation rules live in [`skill-rules.json`](skill-rules.json).

## The loop

```
/sunday → github-bless (ingest) → weekly-blessing (witness) → palace-build (grow)
```

## Install

```bash
# copy the skills into your agent's skills directory, e.g.
cp -r skills/* ~/.claude/skills/
cp -r commands/* ~/.claude/commands/
```

## Validate

```bash
python scripts/validate_skills.py
```

## Relationship to the ecosystem

- **Standard:** [`bless`](https://github.com/frankxai/bless) — the protocol these skills implement.
- **Reference adoption:** [`frankx-mind-palace`](https://github.com/frankxai/frankx-mind-palace) — the data.
- **Renderer:** [`frankx-palace`](https://github.com/frankxai/frankx-palace) — the 3D palace.

## License

MIT. See [`LICENSE`](LICENSE).

Built on SIP · The Blessing Protocol v0.1
