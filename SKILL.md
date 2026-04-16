---
name: ux-patterns
description: "Add site entries to the UX patterns archive with screenshots via screenshotit.app, file naming by domain, and curated gallery indexing. Use when adding a website to the design archive, cataloguing UX inspiration, documenting site typography or themes, or updating the curated gallery index."
---

# UX Patterns

Add and organize entries in the UX patterns archive — a curated collection of sites notable for design, elegance, or UX quality.

## Repo Structure

```
ux-patterns/
├── archive/          # Individual site entries (one file per site)
├── assets/           # Screenshots
├── journal/          # Dated notes
├── Website Inspiration.md  # Curated gallery index
├── themes.md         # Theme notes
├── typography.md     # Typography notes
└── README.md
```

## Workflow

1. Pull latest changes: `git pull`
2. Screenshot the landing page using screenshotit.app:
   `![Description](https://screenshotit.app/https://example.com/)`
   - Modifiers: `@full` (full page), `@mobile`, `@refresh` (force refresh)
   - Reference: https://github.com/flowershow/screenshotit
3. Save the screenshot to `assets/`
4. Create `archive/<site-name>.md` following the entry format below
5. If the site is a curated gallery or resource, add it to `Website Inspiration.md`
6. Commit and push:
   ```bash
   git add archive/<site-name>.md assets/<site-name>.jpg
   git commit -m "Add <site-name> — <one-line reason>"
   git push
   ```

## Entry Format

File naming: use the domain (`conductor.build.md`, `nan.fyi.md`) or a descriptive title matching the repo style (`Dia Browser landing page is elegant.md`).

```markdown
One-line description of what makes it notable.

https://example.com

![Description](../assets/site-name.jpg)

Brief note on what the site/product is and why it's interesting.
```
