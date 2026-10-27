# Reading System

A small, reusable stylesheet for long-form essay and paper pages: one CSS file, an optional script, three themes, a few switches. It grew out of the [Essay and Paper Pages](/essay-pages/) research and the [In Tech We Trust mockups](/essay-pages/mockups/in-tech-we-trust/).

**Demo:** [demo/](demo/) (live: [claude.ai artifact](https://claude.ai/artifact/L9JyqBYN941wu8ofFJGYAo)). Switch theme, accent colour, contents rail, drop caps, and desktop or phone.

## What you get

- **Themes:** `academic` (journal: Newsreader titles over Source Serif), `magazine` (art-directed: Cormorant Garamond titles over Newsreader, drop caps), `personal` (quiet: EB Garamond).
- **Options:** contents rail on or off (`data-rs-rail`), drop caps on or off (`data-rs-dropcap`), pull quotes off (`data-rs-pull="off"`), cover hidden (`data-rs-cover="none"`), automatic chapter numbers (`data-rs-chapters="auto"`).
- **Accent:** one colour, set with `--rs-accent`. Defaults: red for Magazine, blue for Academic, brick red for Personal.
- **Pieces:** chapter bar with reading progress, header block with cover, summary with the claim in bold, red "Chapter N" labels, In brief, epigraphs, pull quote, sidenotes, figures in three widths (margin, column, wide), end matter (notes, cite with copy, versions, responses, references, series nav).
- **Layout** reflows to its own width (container queries), so it works inside any site's column.

## Use it

```html
<link rel="stylesheet" href="reading.css">
<script src="reading.js" defer></script>   <!-- optional -->

<div class="rs" data-rs-theme="magazine" data-rs-rail="on" data-rs-dropcap="on" style="--rs-accent:#c8281e">
  <div class="rs-body"><div class="rs-wrap">
    <nav class="rs-rail"><span class="rs-rail-label">Contents</span><ol class="rs-toc" data-rs-auto></ol></nav>
    <article class="rs-text">
      <!-- your Markdown output goes here -->
    </article>
  </div></div>
</div>
```

The demo's `template.html` shows the full page: chapter bar, header, summary and end matter.

### Fonts

Not bundled. Load the line for your theme:

- **Academic:** `Newsreader` and `Source Serif 4` and `Source Sans 3`
- **Magazine:** `Cormorant Garamond` and `Newsreader` and `Instrument Sans`
- **Personal:** `EB Garamond` and `IBM Plex Mono`

The demo's `<link>` line has the exact Google Fonts URL.

### Markdown

Inside `.rs-text`, plain Markdown output is styled as is:

| Markdown | Becomes |
|---|---|
| `## Title` | chapter. For the "Chapter 2" label, either add `<span class="rs-num">2</span>` inside the heading, or set `data-rs-chapters="auto"` to number every `h2` (class `rs-unnumbered` skips one). Use one or the other, not both |
| `### Title` | section |
| `#### Title` | subsection (Magazine: small red label with a rule) |
| `##### Title` | short definitions (Academic: run-in italic head) |
| `> quote` | epigraph: small italic, with emphasis set upright. For a source line, write the quote in HTML with `<cite>Name</cite>`. Blockquotes are always styled as epigraphs, so don't use them for callouts |
| `[^1]` footnotes | sidenotes in the margin with `reading.js`; tap to open on phones. Without the script they stay at the end. GFM's "Footnotes" heading is ignored by contents and chapter numbers |
| `---` | section break (⁂, or ✻ in Personal) |

Add these by hand where you want them:

- **In brief:** `<p class="rs-inbrief"><span class="rs-inbrief-label">In brief</span> The claim…</p>`
- **Pull quote:** `<aside class="rs-pull"><p>“…”</p></aside>`
- **Figures:** `<figure class="rs-margin | rs-column | rs-wide">…<figcaption><span class="rs-fignum">Figure 1</span> …</figcaption></figure>`
- **Notes in the end matter:** an empty `<div data-rs-notes-slot></div>`; `reading.js` moves the footnote list there.

### Widths

The layout responds to the width of `.rs` itself: below 760px it is the phone layout (notes open on tap); from 760px notes sit in the margin; from 1080px the contents rail appears. So give `.rs` the full page width, not a narrow content column.

Drop caps and Personal's small-caps first line work without the script for the usual cases (first paragraph after a chapter heading, or after its In brief).

### Flowershow

- Put `reading.css` in the site and import it from `custom.css`, or paste it in.
- Wrap a page in `<div class="rs" data-rs-theme="…">` using `layout: plain`, so `.rs` is full width (Flowershow's normal prose column is too narrow for margin notes or the rail).
- Scripts work (premium): add `scripts: /js/reading.js` to a page's frontmatter (page scripts), or load it site-wide through Custom Head Code. As a page script it must be safe to re-run and clean up on `flowershow:page-leave` (see the Flowershow page-scripts docs). Without it, footnotes stay at the end, styled.
- Plan for rufuspollock.com: `~/src/rufuspollock/rufuspollock.com/docs/plans/2026-10-27-reading-system.md` (bead `rp-5og`).
- Set `--rs-sticky-top` to the height of Flowershow's sticky navbar so the chapter bar sits under it.

## Tokens

All on `.rs`, all overridable: `--rs-accent`, `--rs-on-accent` (text on accent fills), `--rs-tint` (light wash for In brief and notes, derived from the accent), `--rs-bg`, `--rs-ink`, `--rs-ink2`, `--rs-muted`, `--rs-rule`, `--rs-text`, `--rs-display`, `--rs-ui`, `--rs-size`, `--rs-size-phone`, `--rs-lh`, `--rs-measure`, `--rs-margin`, `--rs-gap`, `--rs-rail-w`, `--rs-max`, `--rs-sticky-top`, and the spacing scale `--rs-s1` to `--rs-s6`.

## House rules (from Rufus's reviews)

- Never indented paragraphs; space between them.
- The chapter label (small accent capitals "Chapter N" above the title) is the signature. Keep it in every theme.
- Footnotes and their numbers small and light.
- Light only for now: these are paper pages.

## Build the demo

```bash
cd demo && python3 build.py
```

It reads `~/src/life-itself/publications/tech/essay.md` (about 3,100 of the 9,800 words).

v0.1, 2026-10-26.
