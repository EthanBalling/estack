"""Deterministic checker/package tests; behavioral walkthroughs live in scenarios.md."""

import hashlib
import importlib.util
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/agent-workspace/scripts/validate_workspace.py"
SPEC = importlib.util.spec_from_file_location("validator", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def snapshot(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file() and not p.is_symlink()}


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_non_git_read_only_repeat(self):
        self.write("AGENTS.md", "# Atlas\nMaintain a local plant catalog.\n")
        before = snapshot(self.root)
        self.assertEqual(validator.validate(self.root), [])
        self.assertEqual(validator.validate(self.root), [])
        self.assertEqual(snapshot(self.root), before)
        self.assertFalse((self.root / ".git").exists())

    @unittest.skipUnless(shutil.which("git"), "Git fixture requires Git")
    def test_dirty_git_index_and_unrelated_work_unchanged(self):
        def git(*args):
            return subprocess.check_output(["git", "-C", str(self.root), *args])
        git("init", "-q")
        self.write("AGENTS.md", "# Existing instructions\nKeep user data local.\n")
        git("add", "AGENTS.md")
        self.write("AGENTS.md", "# Existing instructions\nKeep user data local.\nNew uncommitted rule.\n")
        self.write("source.txt", "unrelated untracked content")
        before, index = snapshot(self.root), git("ls-files", "--stage")
        status = git("status", "--porcelain=v1")
        self.assertEqual(validator.validate(self.root), [])
        self.assertEqual(snapshot(self.root), before)
        self.assertEqual(git("ls-files", "--stage"), index)
        self.assertEqual(git("status", "--porcelain=v1"), status)

    def test_existing_directory_resources_and_links(self):
        self.write("AGENTS.md", "Read [index](.agents/INDEX.md) for relevant topics.")
        self.write(".agents/INDEX.md", "For pruning, [notes](NOTES/plants.md#pruning).")
        self.write(".agents/NOTES/plants.md", "# Plants\n## Pruning\nUse clean tools.\n")
        self.assertEqual(validator.validate(self.root), [])

    def test_artifact_group_routes_without_reading_binary_payloads(self):
        self.write("AGENTS.md", "For task evidence, read [index](.agents/INDEX.md).")
        self.write(".agents/INDEX.md", "For the import investigation, [task](TASKS.md).")
        self.write(".agents/TASKS.md", "For reproduction only, [working group](imports/) and [snapshot](imports/sample.bin).")
        payload = self.root / ".agents/imports/sample.bin"
        payload.parent.mkdir()
        payload.write_bytes(b"\xff\x00synthetic evidence")
        before = snapshot(self.root)
        self.assertEqual(validator.validate(self.root), [])
        self.assertEqual(snapshot(self.root), before)
        payload.unlink()
        errors = [msg for level, msg in validator.validate(self.root) if level == "error"]
        self.assertEqual(len(errors), 1)
        self.assertIn("sample.bin: missing target", errors[0])

    def test_nested_git_pointer_is_boundary_inside_agent_artifacts(self):
        self.write("AGENTS.md", "For reproduction, [index](.agents/INDEX.md).")
        self.write(".agents/INDEX.md", "[checkout](working/repro/) [internal](working/repro/NOTES.md)")
        self.write(".agents/working/repro/.git", "gitdir: ../../../administration\n")
        (self.root / ".agents/working/repro/NOTES.md").write_bytes(b"\xff")
        before = snapshot(self.root)
        findings = validator.validate(self.root)
        self.assertEqual(len(findings), 2)
        self.assertTrue(all(level == "warning" and "nested repository; not read" in msg
                            for level, msg in findings))
        self.assertEqual(snapshot(self.root), before)

    def test_clean_mechanics_do_not_certify_legacy_coverage(self):
        self.write("AGENTS.md", "# Project\nKeep data local.\n")
        self.write("files/operational.md", "Unassessed operational plan.")
        result = subprocess.run(["python3", str(SCRIPT), str(self.root)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("coverage", result.stdout)
        self.assertIn("dispositions", result.stdout)

    def test_missing_file_and_anchor(self):
        self.write("AGENTS.md", "[missing](missing.md) [heading](.agents/NOTES.md#absent)")
        self.write(".agents/NOTES.md", "# Known\n")
        errors = [message for level, message in validator.validate(self.root) if level == "error"]
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("missing anchor" in message for message in errors))

    def test_boundary_references_are_not_read(self):
        external = self.root / "external"
        external.mkdir()
        (external / "bad.md").write_bytes(b"\xff")
        project = self.root / "project"
        project.mkdir()
        (project / "linked").symlink_to(external, target_is_directory=True)
        (project / "nested/.git").mkdir(parents=True)
        (project / "nested/bad.md").write_bytes(b"\xff")
        (project / "AGENTS.md").write_text("[x](linked/bad.md) [y](nested/bad.md) [z](../external/bad.md) [escape](linked/../bad.md)")
        findings = validator.validate(project)
        self.assertEqual(len(findings), 4)
        self.assertTrue(all(level == "warning" and "not read" in message for level, message in findings))

    def test_collision_bulk_and_unsupported_links(self):
        self.write("AGENTS.md", "rule " * 301 + "\n[reference][owner]\n[owner]: elsewhere.md\n")
        self.write(".agents", "collision")
        findings = validator.validate(self.root)
        self.assertTrue(any(level == "error" and "collision" in msg for level, msg in findings))
        self.assertTrue(any("301" in msg or "words" in msg for _, msg in findings))
        self.assertTrue(any("reference-style" in msg for _, msg in findings))

    def test_fenced_examples_and_duplicate_anchors(self):
        self.write("AGENTS.md", "```md\n[x](absent.md)\n```\n[ok](.agents/NOTES.md#result-1)")
        self.write(".agents/NOTES.md", "# Result\n# Result\n")
        self.assertEqual(validator.validate(self.root), [])

    def test_undecodable_resource_is_reported_without_hiding_other_findings(self):
        self.write("AGENTS.md", "Read [notes](.agents/notes.md) and [legacy](.agents/legacy.md#intro).")
        self.write(".agents/notes.md", "[gone](absent.md)")
        (self.root / ".agents/legacy.md").write_bytes(b"# Intro\ncaf\xe9 notes\n")
        before = snapshot(self.root)
        result = subprocess.run(["python3", "-B", str(SCRIPT), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(".agents/notes.md -> absent.md: missing target", result.stdout)
        self.assertIn(".agents/legacy.md: not readable as UTF-8 Markdown", result.stdout)
        self.assertIn("AGENTS.md -> .agents/legacy.md#intro: anchor not checked", result.stdout)
        self.assertEqual(snapshot(self.root), before)

    @unittest.skipIf(not hasattr(os, "geteuid") or os.geteuid() == 0, "needs non-root permission checks")
    def test_unreadable_file_and_directory_are_reported(self):
        self.write("AGENTS.md", "# Project\n")
        locked = self.write(".agents/locked.md", "private")
        hidden = self.root / ".agents/sealed"
        self.write(".agents/sealed/inner.md", "[gone](absent.md)")
        locked.chmod(0)
        hidden.chmod(0)
        self.addCleanup(locked.chmod, 0o644)
        self.addCleanup(hidden.chmod, 0o755)
        findings = validator.validate(self.root)
        self.assertTrue(any(level == "error" and ".agents/locked.md: not readable" in msg
                            for level, msg in findings), findings)
        self.assertTrue(any(level == "warning" and ".agents/sealed: directory not readable" in msg
                            for level, msg in findings), findings)

    def test_inline_code_titles_and_balanced_destinations(self):
        self.write("AGENTS.md", "Template: `[name](owner.md)` or ``[x](`y`.md)``.\n"
                                "[single](absent-a.md 'title') [paren](absent-b.md (title)) "
                                "[balanced](.agents/file_(1).md) [code `x` text](.agents/file_(1).md)\n")
        self.write(".agents/file_(1).md", "# Notes\n")
        errors = sorted(msg for level, msg in validator.validate(self.root) if level == "error")
        self.assertEqual(errors, ["AGENTS.md -> absent-a.md: missing target",
                                  "AGENTS.md -> absent-b.md: missing target"])

    def test_rendered_heading_text_anchors(self):
        self.write("AGENTS.md", "[a](.agents/N.md#collaboration-practices) [b](.agents/N.md#snake_case-option) "
                                "[c](.agents/N.md#__init__-hook) [d](.agents/N.md#linked-title) "
                                "[e](.agents/N.md#bold-term)")
        self.write(".agents/N.md", "## _Collaboration Practices_ \n## snake_case option\n## `__init__` hook\n"
                                   "## [Linked](N.md) title\n### **Bold** __term__\n")
        self.assertEqual(validator.validate(self.root), [])

    def test_byte_order_mark_and_empty_heading_anchors(self):
        self.write("AGENTS.md", "﻿[first](.agents/NOTES.md#first) [fake](.agents/NOTES.md#next-line)")
        self.write(".agents/NOTES.md", "﻿# First\n#\nNext line\n")
        errors = [msg for level, msg in validator.validate(self.root) if level == "error"]
        self.assertEqual(errors, ["AGENTS.md -> .agents/NOTES.md#next-line: missing anchor"])

    def test_independent_packages_outside_checkout(self):
        for name in ("agent-workspace", "update-memory"):
            package = self.root / name
            shutil.copytree(ROOT / "skills" / name, package)
            for doc in package.rglob("*.md"):
                text = doc.read_text()
                if doc.name == "SKILL.md":
                    self.assertTrue(text.startswith(f"---\nname: {name}\n"))
                    description = text.split("description: ", 1)[1].splitlines()[0]
                    self.assertLessEqual(len(description), 1024)
                    self.assertLess(len(text.split()), 700)
                self.assertEqual(validator.check_links(doc, package), [], doc)
                self.assertIsNone(re.search(r"/srv/|/home/|/Users/|Fedora|T3 Code|Paseo", text))
        project = self.root / "target"
        project.mkdir()
        (project / "AGENTS.md").write_text("# Independent target\n")
        result = subprocess.run(["python3", str(self.root / "agent-workspace/scripts/validate_workspace.py"), str(project)],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
