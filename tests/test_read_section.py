"""Behavior tests use temporary Markdown fixtures only."""

import subprocess
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/agent-workspace/scripts/read_section.py"


class SectionReaderTests(unittest.TestCase):
    def run_reader(self, content: str, *arguments: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "fixture.md"
            source.write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(source), *arguments],
                capture_output=True, text=True, check=False,
            )

    def test_descendants_stop_at_peer_or_ancestor(self) -> None:
        content = "# Doc\nscope\n## A\na\n### Child\nc\n## B\nb\n"
        result = self.run_reader(content, "## A")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "## A\na\n### Child\nc\n")
        self.assertEqual(self.run_reader(content, "### Child").stdout, "### Child\nc\n")

    def test_fences_hide_headings_and_require_matching_closer(self) -> None:
        content = "# Doc\n## A\n````md\n## B\n```\n## B\n````\n~~~\n## B\n```\n~~~\n## B\nreal\n"
        result = self.run_reader(content, "## B")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "## B\nreal\n")

    def test_preamble_includes_ancestor_intros_without_siblings(self) -> None:
        content = "lead\n# Doc\nscope\n## Earlier\nprivate\n## Parent\nlimits\n### Sibling\nother\n### Target\nbody\n#### Child\nchild\n## After\nend\n"
        result = self.run_reader(content, "### Target", "--preamble")
        self.assertEqual(result.stdout, "lead\n# Doc\nscope\n## Parent\nlimits\n### Target\nbody\n#### Child\nchild\n")
        self.assertEqual(result.returncode, 0)

    def test_missing_duplicate_and_nonexact_targets_fail_without_content(self) -> None:
        for content, target in [("## Here\nbody\n", "Here"), ("## A\nsecret\n## A\nother\n", "## A")]:
            with self.subTest(target=target):
                result = self.run_reader(content, target)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertTrue(result.stderr)

    def test_list_ignores_fences_and_accepts_atx_closing_hashes(self) -> None:
        result = self.run_reader("# Doc\n   ## Target ##\n~~~text\n# Hidden\n~~~\n", "--list")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "1\t# Doc\n2\t   ## Target ##\n")

    def test_missing_file_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = subprocess.run([sys.executable, str(SCRIPT), str(Path(temporary) / "absent.md"), "## A"], capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")

    def test_invalid_encoding_and_directory_input_fail_without_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            invalid = Path(temporary) / "invalid.md"
            invalid.write_bytes(b"# Heading\n\xffprivate")
            for source in (invalid, Path(temporary)):
                result = subprocess.run([sys.executable, str(SCRIPT), str(source), "--list"],
                                        capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertIn("read_section:", result.stderr)

    def test_standalone_copy_preserves_input_on_repeat(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "independent-package"
            shutil.copytree(SCRIPT.parents[1], package)
            source = root / "topic with spaces.md"
            source.write_text("# Topic\nscope\n## Selected\nbody\n## Other\nexcluded\n")
            before = (source.read_bytes(), source.stat().st_mtime_ns)
            for _ in range(2):
                result = subprocess.run([sys.executable, str(package / "scripts/read_section.py"),
                                         str(source), "## Selected", "--preamble"],
                                        cwd=root, capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, "# Topic\nscope\n## Selected\nbody\n")
                self.assertEqual((source.read_bytes(), source.stat().st_mtime_ns), before)

    def test_unclosed_fence_hides_rest_of_document(self) -> None:
        result = self.run_reader("# Doc\n```\n## Hidden\n", "## Hidden")
        self.assertEqual(result.returncode, 1)
        self.assertIn("found 0", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_exact_target_and_duplicate_diagnostics(self) -> None:
        result = self.run_reader("## A\none\n## A\ntwo\n", "## A")
        self.assertEqual(result.returncode, 1)
        self.assertIn("found 2", result.stderr)
        self.assertEqual(result.stdout, "")
        result = self.run_reader("## A ##\nbody\n", "## A")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.run_reader("## A ##\nbody\n", "## A ##").stdout, "## A ##\nbody\n")

    def test_no_headings_empty_file_and_cli_errors(self) -> None:
        self.assertEqual(self.run_reader("plain\n", "--list").stdout, "")
        self.assertEqual(self.run_reader("", "## A").returncode, 1)
        self.assertEqual(self.run_reader("# Doc\n", "--list", "# Doc").returncode, 2)

    def test_byte_order_mark_does_not_hide_first_heading(self) -> None:
        content = "﻿# Doc\nlead\n## A\nx\n"
        self.assertEqual(self.run_reader(content, "--list").stdout, "1\t# Doc\n3\t## A\n")
        result = self.run_reader(content, "# Doc")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "# Doc\nlead\n## A\nx\n")

    def test_trailing_whitespace_is_ignored_and_duplicates_still_fail(self) -> None:
        content = "# Doc\n## A  \nbody\n## B\t\nb\n"
        self.assertEqual(self.run_reader(content, "--list").stdout, "1\t# Doc\n2\t## A\n4\t## B\n")
        for target in ("## A", "## A "):
            result = self.run_reader(content, target)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "## A  \nbody\n")
        result = self.run_reader("## A\none\n## A \ntwo\n", "## A")
        self.assertEqual(result.returncode, 1)
        self.assertIn("found 2", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_preamble_does_not_duplicate_target_root(self) -> None:
        self.assertEqual(self.run_reader("lead\n# Doc\nscope\n## A\na\n", "# Doc", "--preamble").stdout, "lead\n# Doc\nscope\n## A\na\n")


if __name__ == "__main__":
    unittest.main()
