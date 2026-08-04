#!/usr/bin/env python3
"""
Collect candidate (url, screenshot, title) tuples from this repo's
curated content, for use as input to the pairwise picker.

Usage:
  python3 scripts/collect_candidates.py [dir ...] > candidates.json

Defaults to scanning archive/ (per-file entries) and any README.md
files under moodboard-style directories (card-grid entries) if no
dirs are given.
"""
import json
import re
import sys
from pathlib import Path

URL_RE = re.compile(r"^https?://\S+$", re.MULTILINE)
IMG_RE = re.compile(r"!\[([^\]]*)\]\((\S+?)\)")


def parse_archive_file(path: Path):
    text = path.read_text()
    url_match = URL_RE.search(text)
    img_match = IMG_RE.search(text)
    if not url_match or not img_match:
        return None
    return {
        "title": path.stem,
        "url": url_match.group(0).strip(),
        "screenshot": img_match.group(2).strip(),
        "source": str(path),
    }


def collect_archive_dir(dir_path: Path):
    candidates = []
    for path in sorted(dir_path.glob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        entry = parse_archive_file(path)
        if entry:
            candidates.append(entry)
    return candidates


def main():
    dirs = [Path(d) for d in sys.argv[1:]] or [Path("archive")]
    candidates = []
    for d in dirs:
        if d.is_dir():
            candidates.extend(collect_archive_dir(d))
    json.dump(candidates, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
