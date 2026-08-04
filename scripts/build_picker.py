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
