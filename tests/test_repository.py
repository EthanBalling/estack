"""Repository documentation and compatibility guards; no Git or network required."""

import ast
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validator", ROOT / "skills/agent-workspace/scripts/validate_workspace.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def documentation():
    yield ROOT / "AGENTS.md"
    yield ROOT / "README.md"
    for folder in ("docs", "skills", "tests"):
        yield from sorted((ROOT / folder).rglob("*.md"))


class RepositoryTests(unittest.TestCase):
    def test_documentation_links_and_anchors_resolve(self):
        documents = list(documentation())
        self.assertGreater(len(documents), 15)
        for document in documents:
            with self.subTest(document=document.relative_to(ROOT)):
                findings = [(level, message) for level, message in validator.check_links(document, ROOT)
                            if "external link not checked" not in message]
                self.assertEqual(findings, [])

    def test_bundled_helpers_parse_with_python_3_9_grammar(self):
        # Static grammar guard for the documented minimum; it does not execute Python 3.9.
        for script in sorted((ROOT / "skills").rglob("*.py")):
            with self.subTest(script=script.relative_to(ROOT)):
                ast.parse(script.read_text(encoding="utf-8"), str(script), feature_version=(3, 9))


if __name__ == "__main__":
    unittest.main()
