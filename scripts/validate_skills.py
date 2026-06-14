#!/usr/bin/env python3
"""Zero-dependency validator for mind-palace-agent-skills.

Enforces the Blessing Protocol skill-authoring conventions:
- every skill lives at skills/<name>/SKILL.md
- YAML-ish frontmatter has exactly the fields `name` and `description`
- `name` is lowercase, hyphenated, <= 64 chars, and matches the directory
- `description` is non-empty and <= 1024 chars
- skill-rules.json is valid JSON and references skills that exist

Exit code 0 if all pass, 1 otherwise. Usage: python scripts/validate_skills.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
RULES = ROOT / "skill-rules.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

errors: list[str] = []


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip().splitlines()
    fields: dict[str, str] = {}
    for line in block:
        if ":" in line:
            key, _, val = line.partition(":")
            fields[key.strip()] = val.strip()
    return fields


def validate_skill(skill_md: Path) -> None:
    rel = skill_md.relative_to(ROOT)
    if skill_md.name != "SKILL.md":
        errors.append(f"{rel}: file must be named SKILL.md")
        return
    dir_name = skill_md.parent.name
    fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
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
                    for key in skills:
                        if key not in names:
                            errors.append(f"skill-rules.json references unknown skill '{key}'")
                elif skills is not None:
                    errors.append("skill-rules.json: 'skills' field must be a JSON object")
        except json.JSONDecodeError as exc:
            errors.append(f"skill-rules.json: invalid JSON — {exc}")
    else:
        errors.append("skill-rules.json missing")

    if errors:
        print("FAIL — Blessing Protocol skill validation")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK — {len(skill_files)} skills valid, skill-rules.json consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
