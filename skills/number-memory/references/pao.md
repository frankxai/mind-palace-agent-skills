# Dominic and PAO systems

Both turn two-digit numbers (00–99) into people doing things. They chunk better than single-word
codes because a person + action is more memorable and more distinct than a noun alone.

## Dominic System

Each digit maps to a **letter** (Dominic O'Brien's mapping): 1=A, 2=B, 3=C, 4=D, 5=E, 6=S, 7=G,
8=H, 9=N, 0=O. A two-digit number → a pair of initials → a **person** with a characteristic
**action**.

- **15** → A, E → **Albert Einstein** → action: writing E=mc² on a board.
- **27** → B, G → **Bill Gates** → action: typing on a laptop.

Encode a 4-digit number as one person doing another's action: **1527** → Einstein (15) *typing on a
laptop* (Gates's action, 27). This person-with-borrowed-action trick is what gives Dominic its
density.

## PAO (Person–Action–Object)

The competition standard. Each two-digit number 00–99 owns a fixed **Person**, **Action**, and
**Object**. Three two-digit numbers (6 digits) compress into ONE composite image:

- take the **Person** of the 1st pair,
- the **Action** of the 2nd pair,
- the **Object** of the 3rd pair.

Example with a tiny table:
- 15 = Einstein / writing-equations / chalkboard
- 27 = Gates / typing / laptop
- 42 = (your 42) / juggling / oranges

**152742** → *Einstein typing oranges* — one vivid scene for six digits. Place that scene at one
locus; the next six digits go at the next locus.

## Cards

Assign each of the 52 cards its own PAO triple (or reuse the 00–99 table mapped to cards). Read the
deck three cards at a time → one P+A+O scene per three cards → ~18 loci for a full deck.

## Building the table

- This only works with a **pre-memorized, stable** 00–99 (or 52-card) table. Build it once, drill it
  with `spaced-recall`, and reuse it forever.
- Choose vivid, distinct people; avoid two people who look alike. Give each a *signature* action and
  a concrete object.

Hand every generated scene to `loci-encoder` for placement along the route.
