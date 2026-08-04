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
