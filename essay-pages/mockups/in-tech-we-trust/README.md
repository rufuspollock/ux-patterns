# In Tech We Trust: essay page mockup

One essay page layout in three styles (academic, magazine, personal), with desktop and phone views. Live: [claude.ai artifact](https://claude.ai/artifact/TdyivbY61BVeSmkKSieeEH).

Built from the board's "If I built one page" recipe ([Essay and Paper Pages board](https://claude.ai/artifact/PVtWUxMDeaWh8bi15bBeW9)): summary with the claim in bold, chapter bar, contents rail, sidenotes, figures in three widths, end matter. Layout sets the genre; style sets the register.

- `template.html`: page, CSS for all three styles, and script.
- `build.py`: pulls text and notes from `~/src/life-itself/2rbook/tech/essay.md` (about 3,100 words of the 9,800) into `index.html`. Run `python3 build.py` in this folder.
- `cover.jpg`: the paper's cover, resized.

2026-10-26. Next: pick a style (or mix), then extract tokens and components into a starter design system.
