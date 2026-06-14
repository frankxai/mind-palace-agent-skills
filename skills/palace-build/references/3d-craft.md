# 3D craft — building a palace that reads as premium, not as a tech demo

This distils the Starlight 3D-memory-palace survey (`premium-3d-memory-palace-survey-2026-05-17`,
Starlight Intelligence System) into the decisions that matter when `palace-build` emits the portable
HTML palace or hands `rooms.json` to the `frankx-palace` renderer. The survey is research-first across
Apple Liquid Glass, Linear, Bruno Simon, Active Theory, Stripe Press, NASA Eyes, and Heptabase; the lines
below are the parts a builder's palace actually depends on.

## One key, one rim

The convergent signal across Bruno Simon, Active Theory's *Neon*, and NASA Eyes is the same: **one strong
directional light, never five.** A scene lit by N point lights "to make it pop" is the slop default.

- One warm key light, elevated, casting a soft contact shadow. The survey's value: `#ffe5cc`, intensity ~1.2.
- One cool rim from behind to separate rooms from the void. Survey value: `#7da3ff`, intensity ~0.3 — though
  the palace's own accent is **gold `#f4c97a` + violet `#c9b6ff`**, so tune the rim toward violet for identity.
- Low HDRI/ambient underneath (intensity 0.4–0.6, not 1.0), ACES tone mapping in the renderer.

A per-room light is allowed **only** when tied to cursor proximity (the Halo 5 trick) — it fades to zero past
a few units, giving the nearest room "awareness." Never a constant glow on every room.

## Selective bloom, never global

Active Theory isolates emissive objects to their own render target, blurs *that*, and composites it back.
A globally bloomed scene reads as "vibe-coded WebGL" — everything glows, so nothing is special. In the
portable HTML palace, bloom (if any) lands on the gold central pulse and selected room accents only, via an
`EffectComposer` selective pass keyed on a layer — not on the whole frame.

## Legible glass is a budget

Linear explicitly *removed* refraction because it harms dense-info legibility. A room that contains a name and
a one-line truth must stay readable, so treat `MeshTransmissionMaterial` as a budget, not a luxury dial:

- `thickness ~0.25` (not 1.0 — high thickness drowns the label)
- `chromaticAberration ~0.02` (half the drei default; >0.05 gives rainbow edges that read "tech demo")
- `roughness ~0.05` (tiny but non-zero — pure 0 reads as plastic)
- `ior ~1.15`, optionally animated 1.07 → 1.5 on hover to let the glass *breathe*
- `samples 8`, `resolution 256` (256 is the sweet spot; lower pixelates)

The pure-CSS constellation fallback exists for exactly this reason: a legible, still constellation beats an
illegible refractive one. When 3D is declined, the fallback is not a downgrade — it is the same discipline.

## Camera motion is half the premium

Bruno Simon's portfolio is cited for restraint, not effects — hand-tuned camera damping is most of why it
feels expensive. **Camera motion is ~50% of the perceived premium.** So:

- Damp every camera move. Spring on hover/select around `response 0.3, dampingFraction 0.6` (Linear's value).
- Bind reveals to **input or scroll position, not wall-clock.** A `useFrame` ramp that runs unconditionally is
  the Lenis-discipline violation the survey warns against.
- **No idle wobble.** When the builder isn't touching anything, the scene is still. Constant idle rotation is
  the #1 AI-slop motion tell. The palace at rest is *at rest* — a quiet room, not a screensaver.

## Artifact-first naming

Stripe Press treats each book as a named artifact with weight; Heptabase treats each note as a card, not a
category. The palace inherits this directly: **a room is a named artifact, never a category badge.** Assign
distinct `surface` values by the nature of the thing (infra → `slate`/`obsidian`; creative → `aurora`/`glass`;
canon → `bronze`/`marble`) so a builder recognises a room as *itself* — not as the sixth recolor of one orb.
This is also why `palace-build` refuses to spawn clutter: one blessing → at most one room, and a week of many
small blessings is grouped, not scattered. Restraint over accumulation is the whole aesthetic.

## Frame-locked reveals

Lenis is 3KB and almost beside the point — what it represents is the rule: **WebGL and DOM share one
timeline, locked to scroll/input, never to wall-clock.** Every room reveal, every ring that accrues outward by
week, every halo state-change binds to a position the builder controls. A palace that animates on its own
clock is performing; a palace that animates under the builder's hand is *theirs*.

— Source: Starlight Intelligence System, `docs/research/premium-3d-memory-palace-survey-2026-05-17.md`.
