#!/usr/bin/env python3
"""Zero-dependency validator for mind-palace-agent-skills.

Enforces the skill-authoring conventions for both suites (Memory Palace + Blessing):
- every skill lives at skills/<name>/SKILL.md
- frontmatter carries `name` and `description` (parsed via the shared _skillmeta module,
  which tolerates a BOM and block scalars)
- `name` is lowercase, hyphenated, <= 64 chars, and matches the directory
- `description` is non-empty and <= 1024 chars
- skill-rules.json is valid JSON, references only skills that exist, and registers
  every skill directory (the reverse check — no skill goes unregistered)
- spec/palace.schema.json and any spec/examples/*.palace.json parse as JSON

Exit code 0 if all pass, 1 otherwise. Usage: python scripts/validate_skills.py
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _skillmeta import parse_frontmatter, read_text  # noqa: E402

from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
RULES = ROOT / "skill-rules.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

errors: list[str] = []


def validate_skill(skill_md: Path) -> None:
    rel = skill_md.relative_to(ROOT)
    if skill_md.name != "SKILL.md":
        errors.append(f"{rel}: file must be named SKILL.md")
        return
    dir_name = skill_md.parent.name
    fm = parse_frontmatter(read_text(str(skill_md)))
    if fm is None:
        errors.append(f"{rel}: missing or malformed frontmatter")
        return
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        errors.append(f"{rel}: frontmatter missing `name`")
    else:
        if not NAME_RE.match(name):
            errors.append(f"{rel}: name '{name}' must be lowercase-hyphenated")
        if len(name) > 64:
            errors.append(f"{rel}: name exceeds 64 chars")
        if name != dir_name:
            errors.append(f"{rel}: name '{name}' != directory '{dir_name}'")
    if not desc:
        errors.append(f"{rel}: frontmatter missing `description`")
    elif len(desc) > 1024:
        errors.append(f"{rel}: description exceeds 1024 chars ({len(desc)})")


def main() -> int:
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md")) if SKILLS_DIR.is_dir() else []
    if not skill_files:
        errors.append("no skills found under skills/*/SKILL.md")
    names = set()
    for sm in skill_files:
        validate_skill(sm)
        names.add(sm.parent.name)

    if RULES.exists():
        try:
            rules = json.loads(RULES.read_text(encoding="utf-8"))
            if not isinstance(rules, dict):
                errors.append("skill-rules.json: root must be a JSON object")
            else:
                skills = rules.get("skills")
                if isinstance(skills, dict):
                    registered = set(skills)
                    for key in skills:
                        if key not in names:
                            errors.append(f"skill-rules.json references unknown skill '{key}'")
                    for skill_name in sorted(names - registered):
                        errors.append(f"skill '{skill_name}' has no skill-rules.json entry")
                elif skills is not None:
                    errors.append("skill-rules.json: 'skills' field must be a JSON object")
        except json.JSONDecodeError as exc:
            errors.append(f"skill-rules.json: invalid JSON — {exc}")
    else:
        errors.append("skill-rules.json missing")

    # spec JSON artifacts must parse (schema + worked examples)
    for json_path in [ROOT / "spec" / "palace.schema.json",
                      *sorted((ROOT / "spec" / "examples").glob("*.palace.json"))]:
        if json_path.exists():
            try:
                json.loads(json_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{json_path.relative_to(ROOT)}: invalid JSON — {exc}")

    if errors:
        print("FAIL — skill validation")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK — {len(skill_files)} skills valid, skill-rules.json consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
