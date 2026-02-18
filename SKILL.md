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
- Take with browser tool, save to `assets/site-name.jpg`
- Embed with relative path: `../assets/site-name.jpg`

### Steps
1. Screenshot landing page → save to `assets/`
2. Create `archive/site-name.md` with URL and screenshot
3. If it's a curated gallery/resource, add to `Website Inspiration.md`
4. Git add, commit, push

## Git Workflow

```bash
cd ~/src/rufuspollock/ux-patterns
git pull   # always pull first
git add archive/site-name.md assets/site-name.jpg
git commit -m "Add site-name.com to archive"
git push
```
