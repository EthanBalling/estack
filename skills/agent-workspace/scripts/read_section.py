"""Read an exact ATX Markdown section without modifying the source."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Heading:
    line: int
    level: int
    text: str


def headings(lines: list[str]) -> list[Heading]:
    result: list[Heading] = []
    fence: str | None = None
    fence_length = 0
    for index, line in enumerate(lines):
        text = line.rstrip("\r\n")
        if fence is not None:
            if re.fullmatch(r" {0,3}" + re.escape(fence) + "{" + str(fence_length) + r",}[ \t]*", text):
                fence = None
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", text)
        if opening and (opening[1][0] != "`" or "`" not in opening[2]):
            fence = opening[1][0]
            fence_length = len(opening[1])
            continue
        match = re.match(r"^ {0,3}(#{1,6})(?:[ \t]+|$)", text)
        if match:
            # Trailing whitespace is not heading content; keep markers and indentation exact.
            result.append(Heading(index, len(match[1]), text.rstrip(" \t")))
    return result


def read_section(content: str, target: str, preamble: bool = False) -> str:
    lines = content.splitlines(keepends=True)
    entries = headings(lines)
    target = target.rstrip(" \t")
    matches = [i for i, entry in enumerate(entries) if entry.text == target]
    if len(matches) != 1:
        raise ValueError(f"expected one exact heading {target!r}; found {len(matches)} (use --list)")
    position = matches[0]
    selected = entries[position]
    end = next((h.line for h in entries[position + 1:] if h.level <= selected.level), len(lines))
    spans: list[tuple[int, int]] = []
    if preamble:
        spans.append((0, entries[0].line))
        ancestors: list[int] = []
        for i, entry in enumerate(entries[:position]):
            while ancestors and entries[ancestors[-1]].level >= entry.level:
                ancestors.pop()
            ancestors.append(i)
        while ancestors and entries[ancestors[-1]].level >= selected.level:
            ancestors.pop()
        spans.extend((entries[i].line, entries[i + 1].line) for i in ancestors)
    spans.append((selected.line, end))
    return "".join("".join(lines[start:stop]) for start, stop in spans)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("heading", nargs="?", help="exact heading line including # markers; see --list")
    parser.add_argument("--list", action="store_true", help="list real ATX headings with 1-based line numbers")
    parser.add_argument("--preamble", action="store_true", help="include document lead and ancestor introductions")
    arguments = parser.parse_args()
    if arguments.list and (arguments.heading is not None or arguments.preamble):
        parser.error("--list cannot be combined with a heading or --preamble")
    if not arguments.list and arguments.heading is None:
        parser.error("provide an exact heading or --list")
    try:
        content = arguments.file.read_text(encoding="utf-8-sig")  # A leading BOM is not content.
        if arguments.list:
            output = "".join(f"{h.line + 1}\t{h.text}\n" for h in headings(content.splitlines(keepends=True)))
        else:
            output = read_section(content, arguments.heading, arguments.preamble)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"read_section: {error}", file=sys.stderr)
        return 1
    sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
