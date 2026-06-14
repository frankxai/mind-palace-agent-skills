# Connectors

Some skills are stronger when wired to an external tool. These are **optional** — every skill works
without them — and **vendor-agnostic**: the `~~placeholder` names below mean "any tool that fills
this role." Configure the concrete MCP server (or paste the equivalent into your assistant) per
deployment.

## The roles

| Role | Used by | Fills it (examples) |
|---|---|---|
| `~~image-generation` | `palace-visualizer`, `assets/manifest.json` | Higgsfield (NB2 / `nano_banana_pro`), any text-to-image MCP. Renders per-locus art and base textures/scenes. |
| `~~spaced-repetition` | `spaced-recall` | Anki (via TSV import or `genanki` `.apkg`). Review loci on any device. |
| `~~source-control` | `agent-memory-palace`, Blessing `github-bless` | GitHub MCP / `git`. Grounds agent-memory `refs` and rolls the builder's week. |
| `~~knowledge-base` | `agent-memory-palace` | Notion / Obsidian / a repo directory. An alternative home for a durable palace. |

## How to read a placeholder

In a `SKILL.md`, a line like "render via the `~~image-generation` connector" means: if such a tool is
available, use it; if not, emit the prompt/spec for the user to run elsewhere. Skills must **degrade
gracefully** — never hard-fail because a connector is missing.

## Notes

- Never store secrets or private data in a `palace.json` (see `agent-memory-palace` refusals).
- The image connector returns assets the skill should save *into the user's palace* (write the path
  back to `locus.image.asset`), not into this library.
