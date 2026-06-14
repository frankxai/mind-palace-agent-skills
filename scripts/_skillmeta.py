#!/usr/bin/env python3
"""Shared SKILL.md frontmatter parsing for the mind-palace tooling.

Zero third-party dependencies. Handles the YAML subset real skill frontmatter
uses: plain ``key: value`` pairs and block scalars (``key: |`` / ``key: >``)
whose value spans several indented lines.

Files are read as strict UTF-8 so em-dashes and the witness register survive
intact instead of being mangled.
"""
from __future__ import annotations

import re

# Frontmatter block: tolerant of a BOM and of the closing ``---`` having no
# trailing newline. Frontmatter must not itself contain a ``---`` line.
FM_RE = re.compile(r"^\ufeff?---\s*\n(.*?)\n?---", re.S)
_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
_BLOCK_INDICATORS = {"|", ">", "|-", ">-", "|+", ">+"}


def read_text(path: str) -> str:
    """Read a file as strict UTF-8 (raises UnicodeDecodeError if corrupted)."""
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def parse_frontmatter(text: str) -> dict | None:
    """Return the frontmatter as a dict, or ``None`` if absent/malformed."""
    m = FM_RE.match(text)
    if not m:
        return None
    lines = m.group(1).split("\n")
    fm: dict[str, str] = {}
    i = 0
    while i < len(lines):
        km = _KEY_RE.match(lines[i])
        if not km:
            i += 1
            continue
        key, val = km.group(1), km.group(2).strip()
        if val in _BLOCK_INDICATORS:
            block: list[str] = []
            indent = None
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt.strip() == "":
                    block.append("")
                    i += 1
                    continue
                line_indent = len(nxt) - len(nxt.lstrip())
                if line_indent == 0:  # dedent ends the block
                    break
                if indent is None:
                    indent = line_indent
                # strip only the block's base indent, preserving relative nesting
                block.append(nxt[indent:].rstrip() if nxt.startswith(" " * indent) else nxt.strip())
                i += 1
            joiner = "\n" if val.startswith("|") else " "
            fm[key] = joiner.join(block).strip()
        else:
            fm[key] = val.strip().strip('"').strip("'")
            i += 1
    return fm
