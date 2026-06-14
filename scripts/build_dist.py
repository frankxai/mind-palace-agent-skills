#!/usr/bin/env python3
"""Zero-dependency distribution builder for mind-palace-agent-skills.

Validates first, then emits downloadable zips under dist/:
  - dist/mind-palace-skills.zip      the master bundle (everything)
  - dist/kits/<platform>.zip         per-runtime kits (claude-code, chatgpt-cowork, cursor)
  - dist/skills/<name>.zip           one zip per skill

Usage:
  python scripts/build_dist.py              # full build (includes assets/)
  python scripts/build_dist.py --no-assets  # lean build (skip assets/, smaller zips)

Pure stdlib. Deterministic (sorted) so zips are reproducible.
"""
from __future__ import annotations

import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
EXCLUDE_DIRS = {".git", "dist", "__pycache__", ".github"}
EXCLUDE_NAMES = {".DS_Store"}

# Top-level paths included in the master bundle.
MASTER_INCLUDE = [
    "skills", "commands", "spec", "assets", "docs", "template",
    "skill-rules.json", "README.md", "LICENSE", "CONTRIBUTING.md",
    "MULTI_RUNTIME.md", "CONNECTORS.md", ".claude-plugin",
]

# Per-platform kits: included paths + the INSTALL.md note written into the zip.
KITS = {
    "claude-code": {
        "include": ["skills", "commands", "skill-rules.json", ".claude-plugin",
                    "spec", "assets", "README.md", "LICENSE"],
        "install": (
            "# Install — Claude Code\n\n"
            "Copy the skills and commands into your Claude config:\n\n"
            "    cp -r skills/* ~/.claude/skills/\n"
            "    cp -r commands/* ~/.claude/commands/\n\n"
            "Or add as a plugin marketplace (see .claude-plugin/marketplace.json):\n\n"
            "    /plugin marketplace add frankxai/mind-palace-agent-skills\n"
        ),
    },
    "chatgpt-cowork": {
        "include": ["skills", "spec", "assets", "CONNECTORS.md", "README.md", "LICENSE"],
        "install": (
            "# Install — ChatGPT / Codex / cowork\n\n"
            "SKILL.md is plain Markdown — paste the skill(s) you want into a Project's custom\n"
            "instructions, or attach the skills/ folder to a Project's files. skill-rules.json is\n"
            "Claude-specific and omitted here. See CONNECTORS.md for the external tools each skill\n"
            "expects (image generation, Anki, GitHub).\n"
        ),
    },
    "cursor": {
        "include": ["skills", "spec", "README.md", "LICENSE"],
        "install": (
            "# Install — Cursor\n\n"
            "Each skills/<name>/SKILL.md is portable Markdown. Convert the frontmatter to a Cursor\n"
            "rule (.cursor/rules/<name>.mdc) keeping the name + description, and paste the body.\n"
        ),
    },
}


def iter_files(rel_root: str, no_assets: bool):
    """Yield (abs_path, arc_path) for a top-level path, honouring excludes."""
    base = ROOT / rel_root
    if not base.exists():
        return
    if base.is_file():
        yield base, rel_root
        return
    for path in sorted(base.rglob("*")):
        if path.is_dir():
            continue
        if any(part in EXCLUDE_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.name in EXCLUDE_NAMES:
            continue
        if no_assets and path.relative_to(ROOT).parts[0] == "assets":
            continue
        yield path, str(path.relative_to(ROOT))


def write_zip(zip_path: Path, includes: list[str], no_assets: bool, extra: dict[str, str] | None = None) -> tuple[int, int]:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel in includes:
            for abs_path, arc in iter_files(rel, no_assets):
                zf.write(abs_path, arc)
                count += 1
        for name, body in (extra or {}).items():
            zf.writestr(name, body)
            count += 1
    return count, zip_path.stat().st_size


def human(size: int) -> str:
    for unit in ("B", "KB", "MB"):
        if size < 1024:
            return f"{size:.0f}{unit}"
        size /= 1024
    return f"{size:.1f}GB"


def main() -> int:
    no_assets = "--no-assets" in sys.argv[1:]

    # Step 0 — never ship invalid skills.
    print("validating…")
    rc = subprocess.call([sys.executable, str(ROOT / "scripts" / "validate_skills.py")])
    if rc != 0:
        print("ABORT — validation failed")
        return rc

    if DIST.exists():
        import shutil
        shutil.rmtree(DIST)

    built: list[tuple[str, int, int]] = []

    n, sz = write_zip(DIST / "mind-palace-skills.zip", MASTER_INCLUDE, no_assets)
    built.append(("mind-palace-skills.zip", n, sz))

    for name, spec in KITS.items():
        inc = spec["include"]
        n, sz = write_zip(DIST / "kits" / f"{name}.zip", inc, no_assets,
                          extra={"INSTALL.md": spec["install"]})
        built.append((f"kits/{name}.zip", n, sz))

    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        name = skill_md.parent.name
        n, sz = write_zip(DIST / "skills" / f"{name}.zip", [f"skills/{name}"], no_assets,
                          extra={"INSTALL.md": f"# {name}\n\nCopy this skill into your agent:\n\n    cp -r skills/{name} ~/.claude/skills/\n"})
        built.append((f"skills/{name}.zip", n, sz))

    print(f"\nbuilt {len(built)} zips under dist/{' (no assets)' if no_assets else ''}:")
    for rel, n, sz in built:
        print(f"  {rel:42} {n:4d} files  {human(sz):>8}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
