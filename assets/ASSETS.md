# Assets — the palace's look

This directory holds the visual layer of the palace: the standalone viewer, and the *reproducible
recipe* for the base imagery.

## What's here

| Path | What |
|---|---|
| `palace-viewer/index.html` | Self-contained Three.js **viewer + builder**. Loads a `palace.json` (inline / `?src=` / drag-drop), renders both the memory-palace and blessing schemas, and exports an edited palace. No build step, works offline. |
| `manifest.json` | Machine-readable prompt set for the six surface textures and five starter scenes. |
| `textures/` | Optional high-res `<surface>.webp` tiles (see below). |
| `scenes/` | Optional starter-palace scene renders (see below). |

## The base images are reproducible, not bundled

The viewer is **fully self-contained**: it generates procedural surface textures in-canvas, so it
looks premium with **zero asset files**. High-res photographic textures and scene art are therefore
*optional upgrades*, generated on demand rather than committed as binaries.

To generate them, run each prompt in [`manifest.json`](manifest.json) through your image connector
(`~~image-generation` — e.g. Higgsfield NB2 / `nano_banana_pro`, 1:1, 1k or higher), then save:

- textures → `assets/textures/<surface>.webp` (the viewer auto-upgrades to these if present)
- scenes → `assets/scenes/<name>.webp` (offered by `memory-palace-architect` as starter shells)

The six surfaces match the **shared material vocabulary** (`obsidian | glass | bronze | marble |
aurora | slate`) so one texture set serves both the memory palace and the Blessing palace.

## Per-locus images

The art that makes a memory palace *yours* is the per-locus imagery — one vivid picture per item.
Those are generated from each `locus.image.prompt` by the `palace-visualizer` skill, saved to the
user's own palace (written back to `locus.image.asset`), and are **not** committed here — they belong
to the builder, not the library.

## Licensing

Any images committed under `textures/` or `scenes/` are generated assets, MIT-licensed alongside the
repo. Per-locus images a user generates for their own palace are theirs.
