# Maintaining Mind Palace Agent Skills

Read CONTRIBUTING.md for the two suites' teaching voice and evidence standards.
The shared method, data schema and viewer live in spec/ and assets/. Edit those
sources and let the distribution builder copy them into installable skills.

For packaging changes, run the regression checks from the repository root.

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skills.py
python3 scripts/generate_catalog.py --check
```

A single-skill installation is ready when a person can copy only the skill
directory from the zip and use the files its instructions require. Check a
lean kit too. Keep member-authored palaces, recall history and generated
personal imagery out of committed examples and distributed fixtures.
