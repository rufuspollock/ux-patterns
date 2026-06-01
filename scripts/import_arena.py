#!/usr/bin/env python3
"""
Import an Are.na channel as a card-grid README.

Usage:
  python scripts/import_arena.py <channel-slug>

Prints Markdown card HTML for each block to stdout.
Pipe to a file or paste into a collection README.

Images come from Are.na's hosted screenshots (block.image.display.url),
so no local screenshot tool needed.
"""
import sys
import json
try:
    import requests
except ImportError:
    sys.exit("pip install requests")

CARD_TEMPLATE = """\
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
    <a href="{url}"><img src="{img}" alt="{title}" class="w-full h-48 object-cover object-top" /></a>
    <div class="p-4">
      <h3 class="font-semibold text-base"><a href="{url}" class="hover:underline">{title}</a></h3>
      <p class="text-sm text-gray-600 mt-1">{desc}</p>
      <a href="{url}" class="text-xs text-blue-500 mt-2 block">{domain} →</a>
    </div>
  </div>"""


def get_image(block):
    img = block.get("image") or {}
    for size in ("display", "large", "original"):
        url = (img.get(size) or {}).get("url", "")
        if url:
            return url
    return ""


def get_url(block):
    return (
        (block.get("source") or {}).get("url")
        or (block.get("attachment") or {}).get("url")
        or ""
    )


def get_domain(url):
    try:
        from urllib.parse import urlparse
        return urlparse(url).netloc.lstrip("www.")
    except Exception:
        return url


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: import_arena.py <channel-slug>")

    slug = sys.argv[1]
    resp = requests.get(
        f"https://api.are.na/v2/channels/{slug}/contents",
        params={"per": 100},
    )
    resp.raise_for_status()
    blocks = resp.json().get("contents", [])

    print('<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">')
    for block in blocks:
        title = block.get("title") or "Untitled"
        url = get_url(block)
        img = get_image(block)
        desc = block.get("description") or ""
        domain = get_domain(url)
        print(CARD_TEMPLATE.format(
            title=title, url=url, img=img, desc=desc, domain=domain
        ))
    print("</div>")


if __name__ == "__main__":
    main()
