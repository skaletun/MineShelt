#!/usr/bin/env python3
"""Validate MineShelt skill packaging and repository Markdown links.

This is a static documentation check. It does NOT create Minecraft buildings,
structure files, coordinates, worldgen, or block arrangements.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "mineshelt" / "SKILL.md"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def check_frontmatter(errors: list[str]) -> None:
    if not SKILL.is_file():
        errors.append("mineshelt/SKILL.md is missing")
        return

    text = SKILL.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append("SKILL.md must start with YAML frontmatter")
        return

    try:
        boundary = lines.index("---", 1)
    except ValueError:
        errors.append("SKILL.md frontmatter is not closed")
        return

    # Simple scalar-field check, not a generic YAML parser; current file only
    # uses single-line scalar fields for required name and description.
    fields: dict[str, str] = {}
    for line in lines[1:boundary]:
        match = re.match(r"^([a-zA-Z][a-zA-Z0-9_-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("\"'")

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not (1 <= len(name) <= 64 and NAME_PATTERN.fullmatch(name)):
        errors.append("Invalid Agent Skills name")
    elif SKILL.parent.name != name:
        errors.append("SKILL.md name does not match parent directory")
    if not (1 <= len(description) <= 1024):
        errors.append("Description must contain 1–1024 characters")
    if len(fields.get("compatibility", "")) > 500:
        errors.append("Compatibility field exceeds 500 characters")
    if boundary + 1 >= len(lines) or not text[sum(len(line) + 1 for line in lines[:boundary+1]):].strip():
        errors.append("SKILL.md instructions must not be empty")


def check_markdown_links(errors: list[str]) -> int:
    inspected = 0
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        inspected += 1
        content = source.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK.findall(content):
            url = raw.strip().split(" ", 1)[0].strip("<>")
            if url.startswith(("https://", "http://", "mailto:", "#")):
                continue
            url = unquote(url.split("#", 1)[0])
            if not url:
                continue
            target = (source.parent / url).resolve()
            if not target.is_relative_to(ROOT):
                errors.append(f"{source.relative_to(ROOT)}: link escapes repo: {raw}")
            elif not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing link target {raw}")
    return inspected


def check_curriculum(errors: list[str]) -> None:
    """Check the core curriculum can't be accidentally detached from SKILL.md."""
    if not SKILL.is_file():
        return
    body = SKILL.read_text(encoding="utf-8")
    required = (
        "references/block-palette-workshop.md",
        "references/terrain-sculpting-masterclass.md",
        "references/vegetation-and-custom-trees.md",
        "references/reference-study-and-image-analysis.md",
        "references/human-builder-practice-loop.md",
    )
    for relative in required:
        if relative not in body:
            errors.append(f"Missing curriculum link in SKILL.md: {relative}")
        if not (SKILL.parent / relative).is_file():
            errors.append(f"Required curriculum document missing: {relative}")

    scenarios = ROOT / "tests" / "scenarios.md"
    if not scenarios.is_file():
        errors.append("Missing tests/scenarios.md")
    else:
        count = len(re.findall(
            r"^##\s+\d+\.", scenarios.read_text(encoding="utf-8"), re.MULTILINE
        ))
        if count < 30:
            errors.append(f"Only {count} behavioral scenarios, expected at least 30")

    review = ROOT / "tests" / "review-sheet.md"
    if not review.is_file():
        errors.append("Missing tests/review-sheet.md")


def main() -> int:
    errors: list[str] = []
    check_frontmatter(errors)
    check_curriculum(errors)
    inspected = check_markdown_links(errors)
    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(f"MineShelt packaging OK; {inspected} Markdown files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
