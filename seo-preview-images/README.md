# SEO Preview Images

Map of content for link previews: the title, description and image that show when a URL is pasted into Slack, Zoom, X, LinkedIn, WhatsApp, iMessage and so on (Open Graph `og:image`, `twitter:card`).

What belongs here: examples of previews that look good (with a screenshot of how they render in a real chat), the tags behind them, and notes on sizes, crops and tooling.

## Examples

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
    <a href="/seo-preview-images/luma.com-event"><img src="./luma-zoom-chat-preview.png" alt="Luma link preview in Zoom chat" class="w-full h-48 object-cover object-top" /></a>
    <div class="p-4">
      <h3 class="font-semibold text-base"><a href="/seo-preview-images/luma.com-event" class="hover:underline">Luma event page</a></h3>
      <p class="text-sm text-gray-600 mt-1">Composed card image: title, RSVP pill and framed poster. Reads well even when cropped.</p>
      <a href="https://luma.com/s4gq0lbr" class="text-xs text-blue-500 mt-2 block">luma.com →</a>
    </div>
  </div>
</div>

## Sizes and crops (to fill in)

- `og:image` common size: 1200×630 (1.91:1); Luma uses 800×420.
- Same image is cropped differently per platform (Zoom chat is closer to square-ish; X `summary_large_image` is 2:1). Keep key content centred and away from the edges.
- To add: per-platform size table, safe-zone template, tools to preview (opengraph.xyz, Slack/X validators), how to generate images per page.

## How to add an example

Add `seo-preview-images/{slug}.md` in the usual archive format (one-liner, URL, screenshot of the preview in a real chat, the tags), then a card above. Save chat screenshots here as local assets, since screenshotit shows the page, not the preview.
