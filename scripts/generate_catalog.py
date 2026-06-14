#!/usr/bin/env python3
"""Generate docs/CATALOG.md and docs/index.html from the skill set.

Reads the frontmatter (`name` + `description`) of every skills/*/SKILL.md and
collects each skill's references/*.md deep-dives. Writes two artifacts kept in
lockstep with the source:

  - docs/CATALOG.md   — the human index, one section per skill
  - docs/index.html   — a self-contained dark gold/violet SPA, no build step

Run after changing skills or references:

    python3 scripts/generate_catalog.py            # write both files
    python3 scripts/generate_catalog.py --check     # exit 1 if either would change

The witness register holds: this file lists what is whole; it does not bless.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _skillmeta import parse_frontmatter, read_text  # noqa: E402

HERE = os.path.dirname(__file__)
ROOT = os.path.normpath(os.path.join(HERE, ".."))
SKILLS = os.path.join(ROOT, "skills")
DOCS = os.path.join(ROOT, "docs")
CATALOG = os.path.join(DOCS, "CATALOG.md")
INDEX = os.path.join(DOCS, "index.html")

# The Sunday loop order — ingest, witness, grow, onboard.
STEP = {
    "github-bless": "ingest",
    "weekly-blessing": "witness",
    "palace-build": "grow",
    "blessing-standard": "onboard",
}
STEP_ORDER = {"ingest": 0, "witness": 1, "grow": 2, "onboard": 3}


def collect() -> list[dict]:
    """Return skills in loop order, each with name, description, refs."""
    skills: list[dict] = []
    for entry in sorted(os.listdir(SKILLS)):
        skill_dir = os.path.join(SKILLS, entry)
        skill_md = os.path.join(skill_dir, "SKILL.md")
        if not os.path.isfile(skill_md):
            continue
        fm = parse_frontmatter(read_text(skill_md))
        if not fm or not fm.get("name"):
            continue
        refs = []
        refs_dir = os.path.join(skill_dir, "references")
        if os.path.isdir(refs_dir):
            for ref in sorted(os.listdir(refs_dir)):
                if ref.endswith(".md"):
                    refs.append(ref)
        name = fm["name"]
        skills.append({
            "name": name,
            "description": " ".join(fm.get("description", "").split()),
            "step": STEP.get(name, ""),
            "path": f"skills/{entry}/SKILL.md",
            "dir": entry,
            "refs": refs,
        })
    skills.sort(key=lambda s: STEP_ORDER.get(s["step"], 99))
    return skills


def render_catalog(skills: list[dict]) -> str:
    n = len(skills)
    out: list[str] = [
        "# Catalog\n\n",
        f"The {n} skills of the **mind-palace-agent-skills** — the portable agent skills of the "
        "[Blessing Protocol](https://github.com/frankxai/bless). Each ships as a self-contained "
        "`SKILL.md` with two-field frontmatter (`name`, `description`) and runs in any runtime that "
        "reads `SKILL.md` skills.\n\n",
        "> This file is generated. After changing a skill or a reference, run "
        "`python3 scripts/generate_catalog.py`, then `python3 scripts/validate_skills.py`.\n\n",
        "The loop: **ingest → witness → grow → onboard**.\n\n",
        "| Skill | Step | What it does |\n|---|---|---|\n",
    ]
    for s in skills:
        out.append(f"| [`{s['name']}`](../{s['path']}) | {s['step']} | {s['description']} |\n")
    for s in skills:
        out.append(f"\n## `{s['name']}`\n\n")
        out.append(f"**Step:** {s['step']} · **Skill:** [`{s['path']}`](../{s['path']})\n\n")
        out.append(f"{s['description']}\n")
        if s["refs"]:
            out.append("\n**References:**\n\n")
            for ref in s["refs"]:
                rel = f"skills/{s['dir']}/references/{ref}"
                out.append(f"- [`{ref}`](../{rel})\n")
    out.append("\n---\n\nBuilt on SIP · The Blessing Protocol v0.1 · MIT\n")
    return "".join(out)


def render_index(skills: list[dict]) -> str:
    data = json.dumps(skills, ensure_ascii=False, separators=(",", ":"))
    n = len(skills)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>mind-palace-agent-skills — {n} portable agent skills</title>
<meta name="description" content="The {n} portable agent skills of the Blessing Protocol — ingest your GitHub, witness the week, grow a palace.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg:#09090b; --panel:#0f0f12; --panel2:#141418; --line:rgba(255,255,255,.08);
    --ink:#ecedf1; --muted:#9aa1ad; --gold:#f4c97a; --violet:#c9b6ff;
    --sans:'Geist','Segoe UI',system-ui,-apple-system,sans-serif;
    --mono:'Geist Mono','SFMono-Regular',ui-monospace,Menlo,monospace;
    --serif:'Instrument Serif',Georgia,serif;
  }}
  *{{box-sizing:border-box}}
  body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 var(--sans);
    -webkit-font-smoothing:antialiased}}
  a{{color:var(--gold);text-decoration:none}} a:hover{{text-decoration:underline}}
  .wrap{{max-width:960px;margin:0 auto;padding:64px 22px 96px}}
  header{{text-align:center;margin-bottom:40px}}
  .mark{{font-family:var(--mono);font-size:13px;letter-spacing:.04em;color:var(--muted)}}
  h1{{font-family:var(--serif);font-weight:400;font-size:46px;line-height:1.05;margin:14px 0 10px;letter-spacing:-.01em}}
  h1 .g{{color:var(--gold)}} h1 .v{{color:var(--violet)}}
  .tag{{color:var(--muted);font-size:18px;margin:0 auto 22px;max-width:560px}}
  .pills{{display:flex;gap:9px;justify-content:center;flex-wrap:wrap}}
  .pill{{border:1px solid var(--line);border-radius:999px;padding:5px 13px;color:var(--muted);font-size:13px}}
  .pill b{{color:var(--ink);font-weight:600}}
  .loop{{display:flex;gap:8px;justify-content:center;align-items:center;flex-wrap:wrap;
    margin:30px 0 8px;color:var(--muted);font-family:var(--mono);font-size:13.5px}}
  .loop b{{color:var(--gold);font-weight:500}}
  .loop .sep{{color:var(--line)}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:16px;margin-top:24px}}
  .card{{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:22px 22px 20px;
    transition:border-color .16s,transform .16s}}
  .card:hover{{border-color:rgba(244,201,122,.4);transform:translateY(-2px)}}
  .step{{font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--violet);
    display:inline-block;margin-bottom:9px}}
  .card h3{{margin:0 0 9px;font-size:18px}}
  .card h3 a{{font-family:var(--mono);font-size:17px;color:var(--ink)}}
  .card h3 a:hover{{color:var(--gold)}}
  .card p{{margin:0;color:var(--muted);font-size:14.5px;line-height:1.58}}
  .refs{{margin-top:14px;padding-top:13px;border-top:1px solid var(--line)}}
  .refs .lbl{{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
    display:block;margin-bottom:7px}}
  .refs a{{display:inline-block;font-family:var(--mono);font-size:12.5px;color:var(--gold);
    border:1px solid var(--line);border-radius:8px;padding:3px 9px;margin:0 6px 6px 0}}
  .refs a:hover{{border-color:rgba(244,201,122,.5);text-decoration:none}}
  footer{{text-align:center;color:var(--muted);margin-top:52px;font-size:13.5px}}
  footer .hair{{width:48px;height:1px;background:var(--line);margin:0 auto 20px}}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="mark">mind-palace-agent-skills</div>
    <h1>Ingest your GitHub.<br><span class="g">Witness</span> the week. <span class="v">Grow</span> a palace.</h1>
    <p class="tag">The {n} portable agent skills of the Blessing Protocol. Self-contained, runtime-agnostic, MIT-licensed.</p>
    <div class="pills">
      <span class="pill"><b>{n}</b> skills</span>
      <span class="pill">Blessing Protocol v0.1</span>
      <span class="pill">MIT</span>
      <span class="pill"><a href="https://github.com/frankxai/mind-palace-agent-skills">GitHub</a></span>
    </div>
    <div class="loop">
      <b>/sunday</b><span class="sep">→</span>ingest<span class="sep">→</span>witness<span class="sep">→</span>grow<span class="sep">→</span>onboard
    </div>
  </header>
  <div class="grid" id="grid"></div>
  <footer>
    <div class="hair"></div>
    Built on SIP · The Blessing Protocol v0.1 ·
    <a href="https://github.com/frankxai/bless">bless</a>
  </footer>
</div>
<script id="data" type="application/json">{data}</script>
<script>
  const REPO = 'https://github.com/frankxai/mind-palace-agent-skills/blob/main/';
  const SKILLS = JSON.parse(document.getElementById('data').textContent);
  const esc = s => {{ const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }};
  document.getElementById('grid').innerHTML = SKILLS.map(s => {{
    const refs = (s.refs || []).map(r =>
      '<a href="' + REPO + 'skills/' + s.dir + '/references/' + r + '">' + esc(r) + '</a>').join('');
    return '<div class="card">' +
      (s.step ? '<span class="step">' + esc(s.step) + '</span>' : '') +
      '<h3><a href="' + REPO + s.path + '">' + esc(s.name) + '</a></h3>' +
      '<p>' + esc(s.description) + '</p>' +
      (refs ? '<div class="refs"><span class="lbl">References</span>' + refs + '</div>' : '') +
      '</div>';
  }}).join('');
</script>
</body>
</html>
"""


def main() -> int:
    skills = collect()
    catalog = render_catalog(skills)
    index = render_index(skills)
    targets = [(CATALOG, catalog), (INDEX, index)]
    if "--check" in sys.argv:
        drift = False
        for path, content in targets:
            current = read_text(path) if os.path.exists(path) else ""
            if current != content:
                print(f"DRIFT: {os.path.relpath(path, ROOT)} is out of date. "
                      "Run scripts/generate_catalog.py.")
                drift = True
        if drift:
            return 1
        print(f"OK: catalog + index in sync ({len(skills)} skills).")
        return 0
    os.makedirs(DOCS, exist_ok=True)
    for path, content in targets:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
    ref_count = sum(len(s["refs"]) for s in skills)
    print(f"Wrote docs/CATALOG.md + docs/index.html — {len(skills)} skills, {ref_count} references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
