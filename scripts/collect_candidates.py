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


# Each card in the grid template (see AGENTS.md) has three anchors:
#   1. `<a href="..."><img ... alt="...X..."></a>` wrapping the screenshot.
#      In report-inspirations/README.md (Are.na import) this href is the
#      real external URL. In archive/README.md and research-sites/README.md
#      (AGENTS.md's documented template) it's an *internal* link like
#      `/research-sites/slug`, and `alt` is suffixed with " screenshot".
#   2. `<h3>` anchor — duplicate of (1), ignored here.
#   3. `<a href="..." class="text-xs ...">domain.com &rarr;</a>` — the real
#      external site link in the AGENTS.md template.
# We capture both (1) and (3) and prefer (3) whenever (1) looks like an
# internal path, so both shapes resolve to the correct external URL.
CARD_RE = re.compile(
    r'<a href="(?P<first_href>[^"]+)"><img src="(?P<img>[^"]+)"[^>]*alt="(?P<alt>[^"]*)"'
    r'.*?'
    r'<a href="(?P<real_href>[^"]+)" class="text-xs[^"]*">',
    re.DOTALL,
)

SCREENSHOT_ALT_SUFFIX = " screenshot"


def parse_card_grid(html: str, source: str):
    entries = []
    for match in CARD_RE.finditer(html):
        first_href = match.group("first_href")
        real_href = match.group("real_href")
        url = real_href if first_href.startswith("/") else first_href
        alt = match.group("alt")
        if alt.endswith(SCREENSHOT_ALT_SUFFIX):
            alt = alt[: -len(SCREENSHOT_ALT_SUFFIX)]
        entries.append({
            "title": alt,
            "url": url,
            "screenshot": match.group("img"),
            "source": source,
        })
    return entries


def collect_card_grid_file(path: Path):
    return parse_card_grid(path.read_text(), source=str(path))


def main():
    dirs = [Path(d) for d in sys.argv[1:]] or [Path("archive"), Path("report-inspirations")]
    candidates = []
    for d in dirs:
        if not d.is_dir():
            continue
        archive_entries = collect_archive_dir(d)
        if archive_entries:
            # This dir has per-file entries (e.g. archive/, research-sites/);
            # its README.md, if any, is just a card-grid rendering of the
            # same sites, so scanning it too would duplicate every entry.
            candidates.extend(archive_entries)
            continue
        readme = d / "README.md"
        if readme.exists():
            candidates.extend(collect_card_grid_file(readme))
    json.dump(candidates, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
