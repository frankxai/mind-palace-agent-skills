# Anki export

Anki is the most widely used open spaced-repetition tool. Exporting palace loci to Anki lets a user
review on any device while keeping the palace as the source of truth.

## The mapping

One Anki note per locus:

| Anki field | From `palace.json` |
|---|---|
| Front | the cue: `room.name` → `station.name` ("Kitchen → table") |
| Back | `locus.target` + `locus.fact` + `locus.image.text` (the encoding, so review reinforces the image, not bare facts) |
| Tags | palace `id`, `room.id` |

## Two export paths

1. **Plain-text TSV (simplest, no dependencies).** Write a `.txt` with `Front<TAB>Back<TAB>Tags`,
   one note per line. In Anki: *File → Import*, set the field separator to Tab, map columns, choose a
   deck. State (intervals) starts fresh.

2. **`.apkg` with scheduling state (advanced).** Build an Anki package with `genanki` (Python) to
   preserve deck structure and, where the schedulers align, carry over review state. Anki's modern
   scheduler is FSRS — if the palace already uses `scheduler: "fsrs"`, intervals translate cleanly;
   SM-2 state maps to Anki's legacy scheduler.

## Round-trip discipline

- Treat `palace.json` as canonical. If the user reviews in Anki, periodically pull grades back into
  the loci `recall` blocks so the palace's schedule stays accurate.
- Don't duplicate: one locus = one note. Re-exporting should update, not multiply, notes (match on
  the locus `id` in a tag or the GUID).
