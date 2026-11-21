import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import build_dist as dist


def package(includes, lean=False):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as output:
        dist.write_contents(output, includes, lean, {})
    return zipfile.ZipFile(stream)


class DistributionTests(unittest.TestCase):
    def test_memory_agent_carries_a_working_example_and_its_contract(self):
        folder = "skills/agent-memory-palace"
        with package([folder], lean=True) as archive:
            for item in ("spec/MEMORY-PALACE-METHOD.md", "spec/palace.schema.json",
                         "spec/examples/solar-system.palace.json"):
                self.assertEqual(archive.read(folder + "/" + item), (dist.ROOT / item).read_bytes())

    def test_individual_skills_can_be_copied_without_repository_root(self):
        for source in sorted((dist.ROOT / "skills").glob("*/SKILL.md")):
            folder = source.parent.relative_to(dist.ROOT).as_posix()
            with self.subTest(skill=folder), package([folder]) as archive:
                self.assertEqual(archive.read(folder + "/LICENSE"), (dist.ROOT / "LICENSE").read_bytes())
                if "spec/" in source.read_text(encoding="utf-8"):
                    for item in ("spec/MEMORY-PALACE-METHOD.md", "spec/palace.schema.json"):
                        self.assertEqual(archive.read(folder + "/" + item), (dist.ROOT / item).read_bytes())

    def test_visualizer_contains_original_viewer_in_single_and_lean_runtime_kits(self):
        folder = "skills/palace-visualizer"
        viewer = "assets/palace-viewer/index.html"
        for paths in ([folder], dist.KITS["claude-code"]["include"]):
            with self.subTest(includes=paths), package(paths, lean=True) as archive:
                self.assertEqual(archive.read(folder + "/" + viewer), (dist.ROOT / viewer).read_bytes())
                names = archive.namelist()
                self.assertEqual(len(names), len(set(names)))

    def test_failure_preserves_existing_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "existing.zip"
            target.write_bytes(b"previous archive")
            with patch.object(dist, "write_contents", side_effect=OSError("interrupted")):
                with self.assertRaises(OSError):
                    dist.write_zip(target, [], False)
            self.assertEqual(target.read_bytes(), b"previous archive")
