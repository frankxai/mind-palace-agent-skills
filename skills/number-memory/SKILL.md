---
name: number-memory
description: Memorize digits, dates, phone numbers, and playing cards by converting numbers into images. Use when the user says "memorize this number", "remember these dates", "how do I memorize a deck of cards", "PAO system", "Major System", or "Dominic System". Supplies the encoding for numeric targets, then hands the resulting images to loci-encoder for placement.
version: 0.1
---

# number-memory

> Numbers are not directly imageable. These systems turn them into people, actions, and objects you
> can place in a palace like anything else.

## When to use this

The target is numeric or symbolic (digits, dates, binary, cards) and needs a stable conversion to
imagery before it can go on a locus.

## Instructions

1. **Pick the system to fit the load:**
   - **Major System** — maps each digit 0–9 to a consonant sound; you build words from the sounds
     (e.g. 32 → "moon"). Best general-purpose, fully phonetic. See `references/major-system.md`.
   - **Dominic System** — maps each two-digit number to a *person* + their characteristic *action*.
     Strong for sequences because person-action pairs chunk cleanly. See `references/pao.md`.
   - **PAO (Person–Action–Object)** — each two-digit number owns a Person, an Action, and an Object;
     three numbers compress into one P+A+O scene (00–99 → one image per 6 digits). The competition
     standard for long digit strings and cards. See `references/pao.md`.

2. **Build (or reuse) the user's table once.** These systems work only with a *stable, memorized*
   mapping. If the user has none, help them build a personal 00–99 table and treat it as durable
   memory (`spaced-recall` can drill it). Never silently invent a fresh table each session.

3. **Chunk the target.** Split digits into 2-digit (Major/Dominic) or 6-digit (PAO) groups. For
   dates, encode the distinctive part (year's last two digits, or month+day).

4. **Cards:** assign each of the 52 cards a PAO triple; read the deck in threes → one scene per
   three cards.

5. **Convert, then hand off.** Produce the image(s) for each chunk and pass them to `loci-encoder`
   to place on stations in route order. number-memory makes the image; the palace holds it.

## Refusals

- Don't drill a target on a table the user hasn't actually memorized — encode the table first.
- Don't mix two systems for one target mid-stream; pick one and stay consistent.

## References

- `references/major-system.md` — the digit→consonant map and worked words.
- `references/pao.md` — Dominic and PAO construction, with examples.
- `spec/MEMORY-PALACE-METHOD.md` §3.

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
