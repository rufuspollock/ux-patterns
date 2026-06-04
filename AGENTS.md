# AGENTS.md — UX Patterns

Instructions for AI agents (Claude, Cursor, Copilot, etc.) working in this repo.

## Repo overview

A curated collection of UX/design inspiration. Two main content types:

- **archive/** — individual site clips, one file per site
- **moodboards** — themed collections of sites, each in their own directory (e.g. `report-inspirations/`)

## Adding an archive entry

Use `archive/` for a single site worth noting for design, UX, or aesthetic quality.

### 1. Create `archive/{slug}.md`

Slug = domain (`frankchimero.com.md`) or short descriptive name (`conductor.build.md`).

File format:

```markdown
One-line description of what makes it notable.

https://example.com

![Site name screenshot](https://screenshotit.app/https://example.com/)

Optional: further commentary, sections, tags.
```

Rules:
- First line is the one-liner — no heading, no prefix
- URL on its own line immediately after
- Screenshot on the line after a blank line
- Extra commentary or `## Section` headings are fine below
- Tags: `#tag` style inline, no separate tag block needed

### 2. Add a card to `archive/README.md`

Append a new card to the grid in `archive/README.md`. Copy an existing card and update all fields:

```html
<div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
  <a href="/archive/slug"><img src="https://screenshotit.app/https://example.com/" alt="Example.com screenshot" class="w-full h-48 object-cover object-top" /></a>
  <div class="p-4">
    <h3 class="font-semibold text-base"><a href="/archive/slug" class="hover:underline">Example.com</a></h3>
    <p class="text-sm text-gray-600 mt-1">One-line description matching the file's first line.</p>
    <a href="https://example.com" class="text-xs text-blue-500 mt-2 block">example.com →</a>
  </div>
</div>
```

Note: the `href="/archive/slug"` uses the filename without `.md`.

### Screenshots: screenshotit vs local

Default: **use `screenshotit.app`** — no binary in repo, zero friction.

```
https://screenshotit.app/https://example.com/
```

Modifiers: `@full` (full page), `@mobile`, `@refresh` (force new screenshot).

Use a **local asset** (`../assets/slug.jpg`) only when you need a specific crop or the screenshotit auto-capture misses the key UI. Save to `assets/`, use `../assets/slug.jpg` in the archive file and `../assets/slug.jpg` in the README card.

## Adding a moodboard (themed collection)

A moodboard is a named, themed collection of sites — same structure as `archive/` but with its own theme/focus.

> Note: `report-inspirations/` is a special case — it was bulk-imported from Are.na so everything lives in one README. New moodboards follow the archive pattern below.

### 1. Create a directory

Use a short kebab-case name: `saas-landing-pages/`, `dark-mode-uis/`, `portfolio-sites/`.

### 2. Create individual item files

Same format as archive entries — `{collection}/{slug}.md`:

```markdown
One-line description of what makes it relevant to this collection.

https://example.com

![Example screenshot](https://screenshotit.app/https://example.com/)

Optional further commentary.
```

### 3. Create `{collection}/README.md`

Same grid HTML as `archive/README.md`. Cards link to the individual item file:

```markdown
# Collection Title

One or two sentences on the theme and what belongs here.

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
    <a href="/{collection}/slug"><img src="https://screenshotit.app/https://example.com/" alt="Example screenshot" class="w-full h-48 object-cover object-top" /></a>
    <div class="p-4">
      <h3 class="font-semibold text-base"><a href="/{collection}/slug" class="hover:underline">Example.com</a></h3>
      <p class="text-sm text-gray-600 mt-1">One-line description matching the file's first line.</p>
      <a href="https://example.com" class="text-xs text-blue-500 mt-2 block">example.com →</a>
    </div>
  </div>
</div>
```

### 4. Add to site navigation (optional)

If the collection should appear in the site nav, link from `README.md`.

## Git workflow

```bash
git pull
git add archive/site-name.md archive/README.md   # or moodboard dir
git commit -m "Add site-name.com to archive"      # or "Add X moodboard"
git push
```

Always pull first. Commit message: `Add {name} to archive` or `Add {name} to {collection}`.
