---
name: loci-encoder
description: Turn each target into a vivid, memorable image and place it at a station. Use when the user says "encode these items", "make images for my palace", "help me remember names and faces", "turn this list into pictures", or after memory-palace-architect lays out the rooms. Applies bizarreness, multisensory, exaggeration, motion, and dual-coding; fills the loci[] of palace.json.
---

# loci-encoder

> The encoding step — the irreducible core of the method. A locus only works if its image is
> impossible to ignore.

## When to use this

The palace skeleton exists (from `memory-palace-architect`) and each station needs the target
converted into an image that sticks. For digits/dates/cards, route to `number-memory` first to get
an image, then place it here.

## Instructions

1. **One image per locus.** For each target, craft a single image and bind it to the station's
   physical feature — the image must *interact* with the feature (sitting on it, smashing it,
   growing from it), not just sit nearby.

2. **Apply the levers** (use 2–3 per image, not all at once):
   - **Bizarreness / distinctiveness** — make it strange; ordinary images vanish.
   - **Multisensory** — add sound, smell, texture, temperature, not just sight.
   - **Exaggeration** — oversize, multiply, or distort scale.
   - **Motion / interaction** — dynamic images beat static tableaux.
   - **Emotion** — funny, gross, or startling outlasts neutral.
   - **Dual-coding** — keep the target word *and* its picture linked, so two routes lead back.

3. **Encode meaning, not spelling.** For a concept, picture what it *does* or *means*. For a word in
   another language, use a sound-alike substitute image (keyword method) plus the meaning.

4. **Names and faces** — see `references/names-faces.md`: convert the name to an image, anchor it to
   a distinctive facial feature, and place the pair at a station.

5. **Keep the route honest.** Place images in route order; don't reorder for convenience. Spacing
   from the architect step must survive — if two images bleed together, make them more distinct.

6. **Write back.** Fill each `loci[].image` in `palace.json`: `text` (the image in words),
   `techniques` (which levers you used), and optionally a `prompt` for `palace-visualizer` to render.

## Refusals

- No bland, literal images ("a photo of the planet") — those are not encodings.
- Don't place two targets at one station to finish faster; that is where recall fails.
- Don't fabricate facts to make an image neater; encode the real target.

## References

- `references/names-faces.md` — the names-and-faces recipe.
- `spec/MEMORY-PALACE-METHOD.md` §3 (the encoding principles and their sources).

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
