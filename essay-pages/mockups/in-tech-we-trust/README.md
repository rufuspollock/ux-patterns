# In Tech We Trust: essay page mockup

One essay page layout in three styles (academic, magazine, personal), with desktop and phone views. Live: [claude.ai artifact](https://claude.ai/artifact/TdyivbY61BVeSmkKSieeEH).

Built from the board's "If I built one page" recipe ([Essay and Paper Pages board](https://claude.ai/artifact/PVtWUxMDeaWh8bi15bBeW9)): summary with the claim in bold, chapter bar, contents rail, sidenotes, figures in three widths, end matter. Layout sets the genre; style sets the register.

- `template.html`: page, CSS for all three styles, and script.
- `build.py`: pulls text and notes from `~/src/life-itself/2rbook/tech/essay.md` (about 3,100 words of the 9,800) into `index.html`. Run `python3 build.py` in this folder.
- `cover.jpg`: the paper's cover, resized.

## v2 (polish pass, 2026-10-26)

Live: [claude.ai artifact](https://claude.ai/artifact/HSKsnGU9JmQJn1MedRrNrA). Source in [v2/](v2/). v1 (above) is kept as the first pass.

Changes after Rufus's review and a cold critique by a Fable subagent:
- Spacing: one vertical scale (`--s1` to `--s6`); headings get more space above than below.
- Academic: Newsreader display over Source Serif text, larger byline names, run-in italic heads for the six features, margin chapter numbers.
- Magazine: Cormorant Garamond display (replacing Bodoni), Newsreader text; chapter labels, red subsection labels with a rule, italic display feature heads; full-measure pull quote; In brief left-aligned with a red rule so it no longer looks like an epigraph.
- Personal: In brief is a marked panel, distinct from italic quotes; book paragraph indents; much less monospace; stronger chapter heads.
- All: sidenotes 14px and darker; 17.5px body on phone; centred blocks go left on phone; end-matter notes in two columns.

### Rufus's verdicts on v2 (2026-10-26)

- Academic and Magazine have the most personality; their type weighting is better. Personal (Spectral) felt heavy.
- Keep for the design system: the Magazine chapter heading (red "Chapter N" label above the title), now shared by all three styles; red as accent; Magazine drop caps (a little OTT, but liked).
- Never indented paragraphs: always space between them. Footnotes and their numerals small.
- Applied: Personal now uses EB Garamond, a red accent, spaced paragraphs and smaller notes.

Next: pick a style (or mix), then extract tokens and components into a starter design system.
