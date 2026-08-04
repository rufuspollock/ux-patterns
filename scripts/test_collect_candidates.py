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
