# Link previews: design brief

A brief you can reuse for any project's link previews: the `og:image`, title and description shown when a URL is pasted into Slack, Zoom, X, LinkedIn, WhatsApp or iMessage. It's distilled from [the moodboard](./README.md) and [the per-page study of 26 sites](./per-page-variation.md). Flowershow's [phase 2 spec](https://github.com/flowershow/flowershow/blob/main/docs/plans/2026-10-26-social-preview-cards-phase-2-design.md) is a worked example, and the build advice in section 8 comes from it.

**Pixel numbers** (margins, type sizes, ratios, thresholds) are starting defaults, not measured. Tune them on your own pages.

## The one rule

**Every page gets its own preview, and it never breaks.** A preview should tell someone *which page* this is before they click. One logo on every page fails the first half; an empty or broken image fails the second.

## 1. Pick the strategy by site type

| Site | Strategy | Examples |
|---|---|---|
| Marketing site, a handful of pages | Hand-designed image per page | (most landing pages in [the moodboard](./README.md)) |
| Blog or magazine with an art habit | **Template plus per-post art**: fixed frame, new picture | Cloudflare, Stripe, Supabase, Vercel (recent posts; older ones fall back to the logo card) |
| Docs, wiki, knowledge base (mostly text) | **Generated text card**: title, description and section from the page | Next.js, Obsidian Help, Mintlify, Astro |
| Content is visual (charts, media, events) | **The content is the image** | Our World in Data, Spotify, Luma |
| Mixed (most real sites) | **Fallback chain** (section 2) | Linear |

If unsure, build the fallback chain. It includes the others.

## 2. The fallback chain

Resolve each page's preview in this order. Stop at the first that works:

1. **Explicit social image** set for this page (a dedicated field such as `social_image`). Use it raw.
2. **Page's featured image** (frontmatter `image`, cover, hero). Show it in an **image card** (section 4), or raw if it already looks like a social card (section 5).
3. **First good image in the page**, computed with filters (section 6). Shown the same way as step 2.
4. **Generated text card** (section 3).
5. **Site-level card**: site name, tagline and logo, with no page data. Use it for the home page, password-protected pages and missing pages.
6. **Static fallback image.** Last resort if rendering fails. Never emit an empty `og:image`.

A site-wide image belongs **only** at step 5, or inside the image card's tile. It must never sit above step 4: that's the "same picture on every page" failure.

## 3. Text card anatomy

The default for any page without a picture. Canvas 1200×630.

```
┌──────────────────────────────────────────────────────┐
│ [logo] Site name                                      │  identity, top-left, ~28px
│                                                       │
│ SECTION                                               │  kicker, uppercase, ~22px, accent colour
│ Page title in the heading font,                       │  54–76px, step down for long titles,
│ up to three lines                                     │  clamp at ~90 chars
│ One-sentence description, two lines max               │  ~28px, muted
│                                                       │
│ example.com/path                                      │  URL, bottom-left, ~22px
└──────────────────────────────────────────────────────┘
```

- **Section line.** The folder or category ("Docs", "Getting Started"). It's the cheapest way to make wiki pages look different from each other.
- **Description.** Use the frontmatter description, else a cleaned first sentence. If you can't produce a clean sentence, leave it out: a run-on dump of page text is worse than nothing.
- **Look like the site.** Use its fonts, background, accent colour and logo. A card should be recognisable without reading it (Astro, Stripe, Tailwind).
- **Margins.** Keep everything at least 64–72px from every edge. The title block should also be readable in the **centre square (630×630)**, because WhatsApp and iMessage may crop to it.
- **Contrast.** Big title, high contrast, one idea. It has to read at about 300px wide, the size it shows in chat.

## 4. Image card anatomy

For pages with a picture: the text card with the image added, so the two read as one system.

- **Split (recommended default):** the text block on the left, as in the text card. The image is a framed tile on the right (about 40–45% of the width), cropped to fill and centred (Luma, Cloudflare, Vercel).
- **Band:** image across the top, title below (Substack's in-app style). Good for wide photos.
- **Cover:** title over a full-bleed image with a scrim. Most striking, and the most fragile: contrast fails on busy images.

Test it on real pages before committing to it (fixtures in section 9).

## 5. When to use an image raw

Use it as-is only if it already looks like a social card: aspect ratio 1.8–2.05 and at least 1000px wide. Authors who design their own 1200×630 (Josh Comeau, Every, Hugging Face) shouldn't get it wrapped in another card. Everything else goes in the image card, so it isn't cropped badly by each platform and the title stays visible.

## 6. Computing an image from the page

The first image in the body is often a good preview (Gwern's first figure, LessWrong) and sometimes a terrible one. Filter:

- Skip SVG, GIF, emoji, badges (shields.io and the like), images inside callouts, tables or HTML blocks, and external hotlinks.
- Skip anything under about 400px on its shorter side.
- Check that the file exists and resolve it to an absolute URL. Relative paths (and wiki-style links, on Markdown sites) in `og:image` are a common silent bug.
- Flag it as computed, so the page itself (its hero) doesn't suddenly show it. Decide explicitly whether listings use it; usually yes.

Text beats a bad image. When in doubt, fall through to the text card.

## 7. Tags checklist

```html
<meta property="og:title" content="Page title">
<meta property="og:site_name" content="Site name">
<meta property="og:description" content="One human sentence.">
<meta property="og:image" content="https://example.com/_og/path?v=abc123">  <!-- absolute -->
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="What the image shows (the title is fine for text cards)">
<meta property="og:url" content="https://example.com/path">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary_large_image">
```

- Absolute `https` URLs only. Always send width and height: some platforms lay out the card before fetching the image.
- **Serve PNG or JPEG**, under about 1MB (a starting default, not measured). 1200×630 is enough for most; 2400×1260 (Raycast, Anthropic and Framer do this) looks sharper on retina screens for the cost of file size.
- Platforms disagree on putting the site name in `og:title`. `og:site_name` is the clean way; adding " · Site" to the title is a common fallback.
- Don't hardcode `twitter:creator` or similar per-person fields across a multi-author site.

## 8. Building it

- **Render options:**
  - on request with Satori or `@vercel/og` (JSX to PNG, as Next.js `opengraph-image` does);
  - at build time (Astro docs pre-render `.webp` cards);
  - with a CDN image template (Luma resizes one master image with Cloudflare image resizing).
- **Cache by content:** put a version hash in the URL (`?v=`). Hash the inputs (title, description, section, the image's file hash, theme and a template version). Serve immutable long-cache only when `v` matches; otherwise serve a short cache, so random `v` values can't fill your cache.
- **Bump the template version** whenever the design changes, so every cached card URL changes.
- **Fetch images safely:**
  - read your own images from storage, not over HTTP;
  - for external URLs: https only, block private IPs after DNS, follow redirects by hand, cap the size, PNG and JPEG only;
  - convert WebP and AVIF inputs to PNG or JPEG first (per the Flowershow review, Satori can't decode them; not independently verified). Give Satori TTF, OTF or WOFF fonts, not WOFF2.
- **Privacy:** protected or draft pages get the site-level card only. The card must never leak a title or text the page itself hides.
- **Failure:** image card fails → text card → site card → static image. A preview should never be broken.

## 9. Testing

- Paste real links into Slack, X, LinkedIn, WhatsApp, iMessage and Zoom. WhatsApp and iMessage often crop square or show a small thumbnail.
- Use [opengraph.xyz](https://www.opengraph.xyz/) and the LinkedIn Post Inspector. Platforms cache previews, so use a fresh `?v=` to force a re-fetch.
- Fixtures to test:
  - long title and no description;
  - a portrait image, a screenshot and a 3:2 artwork;
  - a relative image path;
  - a protected page;
  - a page with only a badge image.

## Anti-patterns

The two most common, both from the study:

- **The same image on every page** (MDN). The preview tells you nothing about the page.
- **The wrong shape:** a square or tall logo in a 1.91:1 slot (Gwern's home page). It gets cropped or letterboxed.
