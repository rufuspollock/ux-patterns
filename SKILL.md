# UX Patterns - Skill

How to add entries to this repo.

## Repo Structure

```
ux-patterns/
├── archive/          # Individual site/tool entries (one file per site)
├── assets/           # Screenshots
├── journal/          # Dated notes
├── Website Inspiration.md  # Curated gallery index
├── themes.md         # Theme notes
├── typography.md     # Typography notes
└── README.md
```

## Adding a Site Entry (archive/)

Use `archive/` for individual sites worth noting for design, elegance, or UX quality.

### File naming
- Use the domain: `conductor.build.md`, `nan.fyi.md`
- Or a descriptive title matching the repo style: `Dia Browser landing page is elegant.md`

### Content format
```markdown
One-line description of what makes it notable (design quality, aesthetic, etc).

https://example.com

![Description](../assets/site-name.jpg)

Brief note on what the site/product is and why it's interesting.
```

### Screenshot
- Default to screenshotit.app (no binary in repo, stable external URL):
  `![Description](https://screenshotit.app/https://example.com/@full)`
- Modifiers: `@full` (full page), `@mobile`, `@refresh` (force refresh)
- See: https://github.com/flowershow/screenshotit
- Only save a local file to `assets/` when screenshotit misses the key UI or
  you need a specific crop — this is the exception, not the default.

### Writing the commentary (for an AI agent)

Don't write the note from the URL/description alone — actually look at the
page:

1. `curl -sL "https://screenshotit.app/<url>/@full" -o /tmp/shot.png` — the
   response is often WebP despite the `.png`-looking name; if `file` reports
   `Web/P image`, convert first: `sips -s format png /tmp/shot.png --out /tmp/shot.png`.
2. Read the converted image (Read tool can view local images) to see the
   actual layout, palette, type, and details.
3. Ask the user for their own one-line take (why they saved it) if they
   haven't given one — don't invent their aesthetic judgment. Combine their
   words with what you can see (typography, layout, color, illustration
   style) for the fuller commentary paragraph.

### Steps
1. Get the screenshotit.app URL (default) or a local crop in `assets/` (exception)
2. Create `archive/site-name.md` with URL, screenshot, and commentary (see above)
3. Add a matching card to `archive/README.md`
4. If it's a curated gallery/resource, add to `Website Inspiration.md`
5. Git add, commit, push

## Git Workflow

```bash
cd ~/src/me/ux-patterns
git pull   # always pull first
git add archive/site-name.md archive/README.md   # + assets/site-name.jpg if using a local crop
git commit -m "Add site-name.com to archive"
git push
```
