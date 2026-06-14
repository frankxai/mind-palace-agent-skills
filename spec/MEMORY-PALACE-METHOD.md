# The Memory Palace Method — methodology + science

> The normative reference for the Memory Palace suite of `mind-palace-agent-skills`.
> The skills implement this; the [`palace.schema.json`](palace.schema.json) is its machine form.

Status: **v0.1 (stable enough to build on)** · License: MIT

---

## 1. What this is

The **method of loci** (the "memory palace") is the oldest and best-attested deliberate memory
technique: information is encoded as vivid imagery and *placed* at locations along a familiar
spatial route, then recalled by walking that route. It is not folklore — it is the technique used
by every World Memory Championship competitor, and brain imaging shows ordinary people who train it
recruit the same spatial-memory circuitry that distinguishes elite memorizers (Dresler et al.,
2017).

This suite makes the method **operable by agents and humans together**: an agent helps you design
the palace, encode the images, walk it to self-test, schedule review, and render it as a navigable
artifact you can keep.

It is a learnable skill, not a talent. There is no "photographic memory."

## 2. The four-level model

A memory palace is a four-level hierarchy. The machine form is `palace.json` (§5).

```
palace            a named place, real or imagined, with a route
  └─ room         a distinct space along the route (surface + accent)
       └─ station  a fixed feature within a room (a shelf, a window, a door)
            └─ locus  one placed item: a target fact + the image that encodes it
```

- **Route discipline.** The route through rooms and stations must be **fixed and non-crossing** —
  order is the whole point of the method (it preserves sequence, which raw association does not).
- **Spacing.** Leave clear gaps between stations; crowded loci blur. Restraint over density.
- **One locus, one item.** Recall degrades when a station holds several competing images.

## 3. The encoding principles (what makes an image stick)

A locus only works if its image is *memorable*. The evidence-backed levers, applied by
`loci-encoder`:

| Principle | Why it works | Source |
|---|---|---|
| **Vivid mental imagery** | Imagery is recalled far better than verbal labels; the imagery instruction is the active ingredient. | Bower, 1970 |
| **Bizarreness / distinctiveness** | Distinctive items resist interference (the isolation effect). | Von Restorff, 1933 |
| **Multisensory + motion** | More retrieval cues; dynamic, interacting images beat static ones. | Bower, 1970 |
| **Exaggeration / emotion** | Salient, affect-laden images are prioritized in memory. | — |
| **Dual coding** | A concept held as *both* word and picture has two independent routes to recall. | Paivio, 1971 |
| **Self-reference & survival framing** | Material tied to oneself or to survival is remembered better. | Nairne et al., 2007 |

For numbers, dates, and abstract data, raw imagery is not enough — `number-memory` supplies the
**Major System**, **Dominic System**, and **Person–Action–Object (PAO)** to convert digits into
encodable images.

## 4. Retrieval and durability (why a palace alone is not enough)

Building the palace encodes; **retrieval practice and spacing** are what make it last.

- **Testing effect.** Recalling material (walking the palace from memory) produces far more durable
  learning than re-studying it. Build the test *into* the practice. (Roediger & Karpicke, 2006.)
- **The forgetting curve.** Without review, recall decays predictably and fast. (Ebbinghaus, 1885.)
- **Spacing.** Reviews timed to just before predicted forgetting maximize retention per unit effort.
  `spaced-recall` schedules with **FSRS** (modern, evidence-led) or **SM-2** (the classic Anki
  default), and can export to Anki.

`palace-walk` runs the retrieval; `spaced-recall` schedules it; both write the optional
`loci[].recall` block in `palace.json`.

## 5. The `palace.json` schema and its relationship to the Blessing palace

This repo carries **two** palace artifacts. They are deliberately distinct and must not be confused.

| | Blessing `rooms.json` | Memory `palace.json` |
|---|---|---|
| Defined in | `frankxai/bless` SPEC §5 (external, read-only) | this file + `palace.schema.json` |
| Purpose | render **closure** — blessed work as rooms | encode **knowledge** — facts on loci for recall |
| Shape | flat list of rooms | four-level nested (room → station → locus) |
| Discriminator | implicitly `"blessing"` | required `"type": "memory-palace"` |

**Non-collision rules:**

1. Different filename (`palace/rooms.json` vs `palace.json`) and a required top-level `type` field so
   a renderer can branch safely.
2. **Shared material vocabulary (reuse, not collision):** a room's `surface` uses the enum defined by
   the Blessing Protocol SPEC §5 — `obsidian | glass | bronze | marble | aurora | slate` — plus a hex
   `accent`. This is **pinned to bless v0.1** and referenced, never redefined here, so one texture set
   and one HTML viewer (`assets/palace-viewer/index.html`) serve both schemas.
3. Renderers and readers **must tolerate unknown fields** and supply sane defaults for missing
   optional ones (same rule as Blessing SPEC §5).

Required fields: `type`, `version`, `id`, `title`, `rooms`. Everything else is optional. The
`recall` block is absent on a freshly built palace and added by `spaced-recall`/`palace-walk` after
the first review. `agent-memory-palace` uses the same file, mapping `room = domain`,
`station = topic`, `locus = fact`, and may add an optional `loci[].refs` array (source paths/URLs).

See [`examples/solar-system.palace.json`](examples/solar-system.palace.json) for a worked instance.

## 6. Voice register (for skill authors)

The Memory Palace suite is **instructional and evidence-grounded**. It is a different register from
the Blessing suite's Witness voice, but it shares one discipline: **no pseudo-science**.

- **Cite** primary literature for any empirical claim.
- **Refuse the neuro-myths:** no left-brain/right-brain, no "we use 10% of the brain," no
  "photographic / eidetic memory" as an attainable adult skill, no "learning styles."
- Prefer **"render / build out / visualize"** over "manifest"; keep "imagination" anchored to the
  mental-imagery research above, never to the spiritual-bypass vocabulary the Blessing SPEC §7 lists.

## 7. References

- Yates, F. A. (1966). *The Art of Memory.*
- Bower, G. H. (1970). Analysis of a mnemonic device. *American Scientist.*
- Paivio, A. (1971). *Imagery and Verbal Processes.*
- Ebbinghaus, H. (1885). *Über das Gedächtnis* (the forgetting curve).
- Von Restorff, H. (1933). The isolation effect.
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science.*
- Nairne, J. S., et al. (2007). Adaptive memory: survival processing. *JEP:LMC.*
- Maguire, E. A., et al. (2003). Routes to remembering: the brains behind superior memory.
  *Nature Neuroscience.*
- Dresler, M., et al. (2017). Mnemonic training reshapes brain networks. *Neuron.*
- FSRS (Free Spaced Repetition Scheduler) and SM-2 — open spaced-repetition algorithms.

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1 · MIT
