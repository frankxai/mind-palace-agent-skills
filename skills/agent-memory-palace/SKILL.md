---
name: agent-memory-palace
description: Give an AI agent persistent, navigable memory across sessions using a memory-palace structure. Use when building agent memory, when the user says "remember this across sessions", "give the agent long-term memory", "persistent context", "knowledge graph for my agent", or for coding agents, Claude cowork, and ChatGPT projects that must retain state. Reads and writes palace.json as a durable spatial knowledge store the agent reloads each session.
---

# agent-memory-palace

> The agent-facing application of the method. Instead of memorizing for a human, the agent keeps
> its *own* durable memory as a palace: rooms are domains, stations are topics, loci are facts —
> a structure that is both human-legible and machine-navigable.

## When to use this

An agent (coding assistant, cowork session, ChatGPT/Claude project) needs to retain knowledge
beyond a single context window: project conventions, decisions, user preferences, API contracts,
recurring facts. This skill defines how the agent stores and retrieves them.

## Instructions

1. **One palace file, known location.** Keep a single `palace.json` (`type: "memory-palace"`) at a
   stable path the agent reloads at session start — e.g. `.agent/memory/palace.json` in the repo, or
   the project's knowledge directory. It is the agent's durable memory.

2. **Map the structure for knowledge, not lists:**
   - `room` = a domain (e.g. "build system", "API contracts", "user preferences").
   - `station` = a topic within the domain.
   - `locus` = one fact, with `target` (the fact, terse), `fact` (elaboration), and optional `refs`
     (file paths / URLs that ground it).

3. **Write protocol (capture):** when a durable fact appears (a decision, a convention, a fix), add
   or update a locus. Keep `target` atomic and self-contained. Record `refs` so the fact is
   verifiable, and `recall.lastReviewed` as the write timestamp. Append, don't silently overwrite —
   if a fact changes, update it and note what changed.

4. **Read protocol (session start):** load the palace, skim room/station names to rebuild a map of
   what is known, and pull the loci relevant to the current task. Treat it as memory to *verify
   against source*, not as ground truth — facts can go stale (re-check `refs`).

5. **Retrieve protocol (during work):** match the task to the nearest room → station → loci. Prefer
   structural navigation (domain → topic) over scanning everything; that is the efficiency the
   palace buys an agent.

6. **Keep it portable.** Same schema as the human palace, so `palace-visualizer` can render the
   agent's memory and a human can inspect it. Tolerate unknown fields; default missing ones.

7. **Prune.** When a room grows noisy, consolidate near-duplicate loci and archive obsolete facts
   (move to an `archive` room rather than deleting outright).

## Refusals

- Never store secrets, credentials, or private user data in the palace file.
- Never treat a stored fact as authoritative about current state without re-checking its `refs` —
  memory is a cache, the source is the truth.
- Don't let the file sprawl unstructured — every fact lives in a room and a station.

## References

- `spec/MEMORY-PALACE-METHOD.md` §5 (schema, agent mapping).
- `spec/palace.schema.json` — the contract this skill reads and writes.

---

Built on SIP · mind-palace-agent-skills · Memory Palace Method v0.1
