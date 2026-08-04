import tempfile
import unittest
from pathlib import Path

from collect_candidates import parse_archive_file, parse_card_grid


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


if __name__ == "__main__":
    unittest.main()
