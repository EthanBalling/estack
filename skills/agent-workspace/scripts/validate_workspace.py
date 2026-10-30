#!/usr/bin/env python3
"""Read-only, bounded Markdown checks; no Git or third-party dependencies."""

import argparse
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def prose(text):
    """Omit fenced examples so template links are not treated as live routes."""
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            continue
        if marker:
            fence = marker[1]
        else:
            lines.append(line)
    return "\n".join(lines)


def anchors(text):
    found, counts = set(), {}
    for title in re.findall(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        occurrence = counts.get(slug, 0)
        counts[slug] = occurrence + 1
        found.add(slug if not occurrence else f"{slug}-{occurrence}")
    found.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    return found


def boundary(path, root):
    """Check lexical path before reading; don't traverse a symlink/repo boundary."""
    path = Path(path).absolute()
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        return "outside selected root"
    current = root
    for part in parts:
        if part == "..":
            current = current.parent
            if current != root and root not in current.parents:
                return "outside selected root"
            continue
        current = current / part
        if current.is_symlink():
            return "symlink boundary"
        if current.is_dir() and ((current / ".git").exists() or (current / ".git").is_symlink()):
            return "nested repository"
    return None


def documents(root):
    router = root / "AGENTS.md"
    if router.is_file() and not router.is_symlink():
        yield router
    resources = root / ".agents"
    if resources.is_dir() and not boundary(resources, root):
        for folder, dirs, files in os.walk(resources, followlinks=False):
            dirs[:] = sorted(d for d in dirs if not boundary(Path(folder) / d, root))
            for name in sorted(files):
                path = Path(folder) / name
                if path.suffix == ".md" and not path.is_symlink():
                    yield path


def check_links(path, root):
    findings = []
    text = prose(path.read_text(encoding="utf-8"))
    if re.search(r"\[[^\]]+\]\[[^\]]*\]|^\s*\[[^\]]+\]:", text, re.M):
        findings.append(("warning", f"{path.relative_to(root)}: reference-style links need manual review"))
    # Ordinary inline links, including angle-wrapped paths and optional titles.
    for match in re.finditer(r"\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
        destination = match[1].strip("<>")
        url = urlsplit(destination)
        if url.scheme or url.netloc:
            findings.append(("warning", f"{path.relative_to(root)}: external link not checked: {destination}"))
            continue
        target = path.parent / unquote(url.path) if url.path else path
        reason = boundary(target, root)
        label = f"{path.relative_to(root)} -> {destination}"
        if reason:
            findings.append(("warning", f"{label}: {reason}; not read"))
        elif not target.exists():
            findings.append(("error", f"{label}: missing target"))
        elif url.fragment and target.is_file():
            if target.suffix != ".md":
                findings.append(("warning", f"{label}: non-Markdown anchor needs manual review"))
            elif unquote(url.fragment) not in anchors(target.read_text(encoding="utf-8")):
                findings.append(("error", f"{label}: missing anchor"))
    return findings


def validate(root):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("target must be a directory")
    findings = []
    for name, directory in (("AGENTS.md", False), (".agents", True)):
        path = root / name
        if path.is_symlink():
            findings.append(("warning", f"{name}: symlink boundary; not read"))
        elif path.exists() and path.is_dir() != directory:
            findings.append(("error", f"{name}: file/directory collision"))
    router = root / "AGENTS.md"
    if not router.exists():
        findings.append(("warning", "AGENTS.md: absent; existing conventions may be valid"))
    elif router.is_file() and not router.is_symlink():
        count = len(router.read_text(encoding="utf-8").split())
        if count > 300:
            findings.append(("warning", f"AGENTS.md: {count} words; review bulk without discarding necessary rules"))
    paths = list(documents(root))
    if len(paths) > 2 and not (root / ".agents/INDEX.md").is_file():
        findings.append(("warning", ".agents/INDEX.md: consider navigation for multiple resources"))
    for path in paths:
        findings.extend(check_links(path, root))
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    args = parser.parse_args()
    try:
        findings = validate(args.target)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    for level, message in findings:
        print(f"{level}: {message}")
    print("Mechanical checks only; review preservation, ownership, privacy, and loading separately.")
    return int(any(level == "error" for level, _ in findings))


if __name__ == "__main__":
    sys.exit(main())
