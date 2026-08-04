# Moodboard Pairwise Picker Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a minimal pairwise-comparison tool that lets Rufus converge on a moodboard direction by clicking through A/B choices of real site screenshots, instead of open-ended browsing or a text-only prompt brief.

**Architecture:** Two small Python scripts, no new dependencies beyond the stdlib and `requests` (already used by `scripts/import_arena.py`).

1. `scripts/collect_candidates.py` — parses this repo's existing curated content (`archive/*.md` per-file entries, and card-grid `README.md` files like `report-inspirations/README.md`) into a flat JSON list of `{title, url, screenshot, source}` candidates. No scraping of external galleries in v1 — the repo already has 60+ hand-curated sites; use those first.
2. `scripts/build_picker.py` — reads a candidates JSON file, generates random pairs, and writes a single self-contained static HTML file with vanilla JS: shows one pair at a time, click a screenshot to pick it, tracks picks in `localStorage`, has an "Export picks" button that downloads a JSON file of winners (with an optional one-line "why" typed in per pick).

The output of a picker session (`picks.json`) is not auto-analyzed by code — the last step of the workflow is manual: paste the winning screenshots into a Claude conversation and ask it to extract concrete shared traits (type, colour behaviour, spacing, layout logic) into a moodboard directory, following the format already documented in `AGENTS.md`.

**Tech Stack:** Python 3 stdlib (`unittest`, `re`, `json`, `pathlib`), plain HTML/CSS/vanilla JS for the picker page (no build step, no framework — must open directly in a browser via `file://`).

---

### Task 1: Candidate extraction — per-file archive entries

**Files:**
- Create: `scripts/collect_candidates.py`
- Test: `scripts/test_collect_candidates.py`

**Step 1: Write the failing test**

```python
# scripts/test_collect_candidates.py
import tempfile
import unittest
from pathlib import Path

from collect_candidates import parse_archive_file


class TestParseArchiveFile(unittest.TestCase):
    def test_parses_url_and_screenshot(self):
        content = (
            "A clean, minimal portfolio site.\n\n"
            "https://example.com\n\n"
            "![Example screenshot](https://screenshotit.app/https://example.com/)\n\n"
            "Some extra commentary that should be ignored.\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "example.com.md"
            path.write_text(content)
            entry = parse_archive_file(path)

        self.assertEqual(entry["title"], "example.com")
        self.assertEqual(entry["url"], "https://example.com")
        self.assertEqual(
            entry["screenshot"],
            "https://screenshotit.app/https://example.com/",
        )
        self.assertEqual(entry["source"], str(path))

    def test_returns_none_when_no_image(self):
        content = "Just a description.\n\nhttps://example.com\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "no-image.md"
            path.write_text(content)
            entry = parse_archive_file(path)

        self.assertIsNone(entry)


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `cd scripts && python3 -m unittest test_collect_candidates -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'collect_candidates'`

**Step 3: Write minimal implementation**

```python
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
```

**Step 4: Run test to verify it passes**

Run: `cd scripts && python3 -m unittest test_collect_candidates -v`
Expected: PASS (2 tests)

**Step 5: Commit**

```bash
git add scripts/collect_candidates.py scripts/test_collect_candidates.py
git commit -m "Add candidate extraction for archive-style entries"
```

---

### Task 2: Candidate extraction — card-grid README files

`report-inspirations/README.md` and any future moodboard `README.md` store entries as HTML card blocks (`<a href="URL"><img src="IMG" alt="TITLE" .../></a> ... <h3>...<a href="URL">TITLE</a></h3>`), not per-file. Add a second parser for this format.

**Files:**
- Modify: `scripts/collect_candidates.py`
- Test: `scripts/test_collect_candidates.py`

**Step 1: Write the failing test**

Add to `scripts/test_collect_candidates.py`:

```python
from collect_candidates import parse_card_grid


class TestParseCardGrid(unittest.TestCase):
    def test_parses_multiple_cards(self):
        html = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
    <a href="https://example.com"><img src="https://images.are.na/foo.png" alt="Example Site" class="w-full h-48 object-cover object-top" /></a>
    <div class="p-4">
      <h3 class="font-semibold text-base"><a href="https://example.com" class="hover:underline">Example Site</a></h3>
      <p class="text-sm text-gray-600 mt-1">A description.</p>
      <a href="https://example.com" class="text-xs text-blue-500 mt-2 block">example.com &rarr;</a>
    </div>
  </div>
</div>
"""
        entries = parse_card_grid(html, source="report-inspirations/README.md")
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["title"], "Example Site")
        self.assertEqual(entries[0]["url"], "https://example.com")
        self.assertEqual(entries[0]["screenshot"], "https://images.are.na/foo.png")
        self.assertEqual(entries[0]["source"], "report-inspirations/README.md")
```

**Step 2: Run test to verify it fails**

Run: `cd scripts && python3 -m unittest test_collect_candidates -v`
Expected: FAIL with `ImportError: cannot import name 'parse_card_grid'`

**Step 3: Write minimal implementation**

Add to `scripts/collect_candidates.py` (near the other parse function):

```python
CARD_RE = re.compile(
    r'<a href="(?P<url>[^"]+)"><img src="(?P<img>[^"]+)"[^>]*alt="(?P<alt>[^"]*)"',
    re.DOTALL,
)


def parse_card_grid(html: str, source: str):
    entries = []
    for match in CARD_RE.finditer(html):
        entries.append({
            "title": match.group("alt"),
            "url": match.group("url"),
            "screenshot": match.group("img"),
            "source": source,
        })
    return entries


def collect_card_grid_file(path: Path):
    return parse_card_grid(path.read_text(), source=str(path))
```

Update `main()` to also scan for `README.md` files in the given dirs and pull card entries:

```python
def main():
    dirs = [Path(d) for d in sys.argv[1:]] or [Path("archive"), Path("report-inspirations")]
    candidates = []
    for d in dirs:
        if not d.is_dir():
            continue
        candidates.extend(collect_archive_dir(d))
        readme = d / "README.md"
        if readme.exists():
            candidates.extend(collect_card_grid_file(readme))
    json.dump(candidates, sys.stdout, indent=2)
    print()
```

**Step 4: Run test to verify it passes**

Run: `cd scripts && python3 -m unittest test_collect_candidates -v`
Expected: PASS (3 tests)

**Step 5: Commit**

```bash
git add scripts/collect_candidates.py scripts/test_collect_candidates.py
git commit -m "Add candidate extraction for card-grid README entries"
```

---

### Task 3: Generate the real candidate pool

**Files:**
- Create: `scratch/candidates.json` (gitignored working file — see Task 6)

**Step 1: Run the collector against the real repo content**

Run: `python3 scripts/collect_candidates.py archive report-inspirations > scratch/candidates.json`

**Step 2: Sanity-check the output**

Run: `python3 -c "import json; c = json.load(open('scratch/candidates.json')); print(len(c)); print(c[0])"`
Expected: count roughly 60-100 (archive has ~50 files, report-inspirations README has several dozen cards); first entry has non-empty `title`, `url`, `screenshot`.

No commit — this is a generated working file (see `.gitignore` update in Task 6).

---

### Task 4: Pairwise picker HTML generator

**Files:**
- Create: `scripts/build_picker.py`
- Test: `scripts/test_build_picker.py`

**Step 1: Write the failing test**

```python
# scripts/test_build_picker.py
import json
import tempfile
import unittest
from pathlib import Path

from build_picker import build_picker_html


class TestBuildPickerHtml(unittest.TestCase):
    def test_embeds_all_candidates_as_json(self):
        candidates = [
            {"title": "A", "url": "https://a.com", "screenshot": "https://a.com/shot.png", "source": "x"},
            {"title": "B", "url": "https://b.com", "screenshot": "https://b.com/shot.png", "source": "y"},
            {"title": "C", "url": "https://c.com", "screenshot": "https://c.com/shot.png", "source": "z"},
        ]
        html = build_picker_html(candidates)

        self.assertIn("https://a.com/shot.png", html)
        self.assertIn("https://b.com/shot.png", html)
        self.assertIn("https://c.com/shot.png", html)
        self.assertIn("<script", html)
        self.assertIn("localStorage", html)

    def test_raises_on_fewer_than_two_candidates(self):
        with self.assertRaises(ValueError):
            build_picker_html([{"title": "A", "url": "https://a.com", "screenshot": "s", "source": "x"}])


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `cd scripts && python3 -m unittest test_build_picker -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'build_picker'`

**Step 3: Write minimal implementation**

```python
#!/usr/bin/env python3
"""
Build a self-contained static HTML pairwise picker from a candidates
JSON file (produced by collect_candidates.py).

Usage:
  python3 scripts/build_picker.py scratch/candidates.json scratch/picker.html

Open the output file directly in a browser (file:// is fine — no
server needed). Click a screenshot to pick it; picks are kept in
localStorage so a session survives a reload. Use the "Export picks"
button to download picks.json when done.
"""
import json
import sys
from pathlib import Path

PICKER_TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Moodboard Picker</title>
<style>
  body {{ font-family: system-ui, sans-serif; background: #111; color: #eee; margin: 0; padding: 2rem; }}
  h1 {{ font-size: 1rem; opacity: 0.7; font-weight: normal; }}
  .pair {{ display: flex; gap: 1rem; margin-top: 2rem; }}
  .card {{ flex: 1; cursor: pointer; border: 3px solid transparent; border-radius: 8px; overflow: hidden; }}
  .card:hover {{ border-color: #6cf; }}
  .card img {{ width: 100%; display: block; }}
  .card .title {{ padding: 0.5rem; font-size: 0.85rem; opacity: 0.8; }}
  #why {{ width: 100%; margin-top: 1rem; padding: 0.5rem; }}
  #status {{ margin-top: 1rem; opacity: 0.6; font-size: 0.85rem; }}
  button {{ margin-top: 1rem; padding: 0.5rem 1rem; }}
</style>
</head>
<body>
<h1 id="status">Loading...</h1>
<div class="pair" id="pair"></div>
<input id="why" placeholder="Optional: why did you pick that one? (applies to next click)">
<button id="export">Export picks.json</button>

<script>
const candidates = {candidates_json};
const picks = JSON.parse(localStorage.getItem('moodboard_picks') || '[]');
let current = [];

function pickRandomPair() {{
  const shuffled = [...candidates].sort(() => Math.random() - 0.5);
  return [shuffled[0], shuffled[1]];
}}

function render() {{
  document.getElementById('status').textContent = `${{picks.length}} picks so far`;
  current = pickRandomPair();
  const pairEl = document.getElementById('pair');
  pairEl.innerHTML = '';
  current.forEach((c, i) => {{
    const div = document.createElement('div');
    div.className = 'card';
    div.innerHTML = `<img src="${{c.screenshot}}" alt="${{c.title}}"><div class="title">${{c.title}}</div>`;
    div.onclick = () => choose(i);
    pairEl.appendChild(div);
  }});
}}

function choose(i) {{
  const why = document.getElementById('why').value;
  picks.push({{ winner: current[i], loser: current[1 - i], why: why }});
  localStorage.setItem('moodboard_picks', JSON.stringify(picks));
  document.getElementById('why').value = '';
  render();
}}

document.getElementById('export').onclick = () => {{
  const blob = new Blob([JSON.stringify(picks, null, 2)], {{ type: 'application/json' }});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'picks.json';
  a.click();
}};

render();
</script>
</body>
</html>
"""


def build_picker_html(candidates):
    if len(candidates) < 2:
        raise ValueError("Need at least 2 candidates to build a picker")
    return PICKER_TEMPLATE.format(candidates_json=json.dumps(candidates))


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: build_picker.py <candidates.json> <output.html>")
    candidates = json.loads(Path(sys.argv[1]).read_text())
    html = build_picker_html(candidates)
    Path(sys.argv[2]).write_text(html)
    print(f"Wrote {sys.argv[2]} with {len(candidates)} candidates")


if __name__ == "__main__":
    main()
```

**Step 4: Run test to verify it passes**

Run: `cd scripts && python3 -m unittest test_build_picker -v`
Expected: PASS (2 tests)

**Step 5: Commit**

```bash
git add scripts/build_picker.py scripts/test_build_picker.py
git commit -m "Add pairwise picker HTML generator"
```

---

### Task 5: Generate and manually smoke-test the picker

**Files:**
- Create: `scratch/picker.html` (gitignored working file)

**Step 1: Build it**

Run: `python3 scripts/build_picker.py scratch/candidates.json scratch/picker.html`
Expected: `Wrote scratch/picker.html with N candidates`

**Step 2: Manual smoke test**

Run: `open scratch/picker.html` (macOS) to open it in the default browser.

Check:
- A pair of two different screenshots renders.
- Clicking one advances to a new pair and the status line's pick count increments.
- Reloading the page preserves the pick count (localStorage persistence).
- "Export picks.json" downloads a JSON file with `winner`/`loser`/`why` entries.

This step is manual — no automated browser test in v1 (no headless browser dependency in this repo). If broken, fix `build_picker.py` and re-run Task 4's tests plus this manual check.

No commit (generated file).

---

### Task 6: Ignore generated working files, document the workflow

**Files:**
- Modify: `.gitignore` (create if it doesn't exist)
- Modify: `howto-moodboards.md`

**Step 1: Add scratch/ to .gitignore**

```
scratch/
```

**Step 2: Append a workflow section to `howto-moodboards.md`**

Add after the existing "Where to Store a Moodboard for AI Access" section:

```markdown

# Pairwise Picker Workflow

A faster alternative to manually browsing for moodboard references: pick between pairs of already-curated sites instead of open-ended searching.

1. `python3 scripts/collect_candidates.py archive report-inspirations > scratch/candidates.json`
   Pulls every site already curated in this repo into a flat candidate list.
2. `python3 scripts/build_picker.py scratch/candidates.json scratch/picker.html`
   Generates a static picker page.
3. `open scratch/picker.html` and click through pairs — as many rounds as it takes to feel converged (start with ~20-30).
4. Click "Export picks.json" and save it somewhere durable (not `scratch/`, which is gitignored).
5. Paste the winning screenshots (or the picks.json plus a request to fetch/describe them) into a Claude conversation and ask it to extract concrete shared traits — not adjectives, mechanics: type, colour behaviour, spacing, layout logic — into a moodboard constraint brief.
6. Use that brief as the actual design moodboard, following the directory format in `AGENTS.md`.

This reuses the curated candidate pool already built into `archive/` and `report-inspirations/` instead of scraping external galleries — v2 could add live scraping of Awwwards/One Page Love/Siteinspire if the existing pool proves too narrow.
```

**Step 3: Commit**

```bash
git add .gitignore howto-moodboards.md
git commit -m "Document pairwise picker workflow, ignore scratch/ working files"
```

---

### Task 7: First real run

Not a code task — run the full workflow against a real backlog item from `planning/projects/2026-design-reps-with-ai.md` (e.g. "Life Itself: hero section") and note in that project's Log section whether the resulting moodboard brief produced a less generic design than the Developmental Spaces / ecosystem attempts. This is the actual test of the plan's hypothesis (tool vs. reps/skill gap) — write up the result in a new dated entry in that file's `## Log` section.
