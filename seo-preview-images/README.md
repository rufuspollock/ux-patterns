# SEO Preview Images

Map of content and moodboard for link previews: the image, title and description that appear when a URL is pasted into Slack, Zoom, X, LinkedIn, WhatsApp or iMessage. These come from the Open Graph `og:image` and `twitter:card` tags.

The images here are each site's actual `og:image`, fetched 2026-10-23. Started from [Luma](./luma.com-event.md), whose event previews look great in Zoom chat:

<img src="./luma-zoom-chat-preview.png" alt="Luma link preview in Zoom chat" class="w-72 rounded-lg" />

## What makes a good one

- **It's generated from the page, not a site-wide logo.** The best ones (Luma, GitHub, Maggie Appleton) are one template filled per page, so every link has its own preview.
- **It's a composed card, not a raw photo.** Big title, one small brand mark, one image or illustration. Readable at about 300px wide, the size it shows in chat.
- **Key content sits in the centre.** Platforms crop differently (see below).
- **One idea, high contrast.** Busy screenshots turn to mush at thumbnail size.
- **Title and description work without the image:** `Page title · Site` plus one human sentence.

## Generated per page: the card is built from the page's own data

The strongest pattern. One template, filled per page with title, description, stats or a poster. Every link gets its own good preview without anyone designing it.

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/luma-1200x630.jpg" alt="Luma event link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Luma event</h3>
      <p class="text-sm text-gray-600 mt-1">Event title + RSVP pill + the event's poster framed on the right. Dark gradient pulled from the poster.</p>
      <a href="https://luma.com/s4gq0lbr" class="text-xs text-blue-500 mt-2 block">luma.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/github-default.jpg" alt="GitHub repo (default) link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">GitHub repo (default)</h3>
      <p class="text-sm text-gray-600 mt-1">Owner/repo in big type, description, avatar, then contributors / issues / stars / forks. Information-dense but calm.</p>
      <a href="https://github.com/flowershow/flowershow" class="text-xs text-blue-500 mt-2 block">github.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/claude-code-gh.jpg" alt="GitHub repo (another) link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">GitHub repo (another)</h3>
      <p class="text-sm text-gray-600 mt-1">Same template; the org avatar is the only branding. Shows how consistent a generated card can be.</p>
      <a href="https://github.com/anthropics/claude-code" class="text-xs text-blue-500 mt-2 block">github.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/maggie.jpg" alt="Maggie Appleton link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Maggie Appleton</h3>
      <p class="text-sm text-gray-600 mt-1">Serif title, short description and a hand-drawn plant, from a generated `/og.png?title=…&description=…`. Garden-like and personal.</p>
      <a href="https://maggieappleton.com/" class="text-xs text-blue-500 mt-2 block">maggieappleton.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/linear.jpg" alt="Linear changelog link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Linear changelog</h3>
      <p class="text-sm text-gray-600 mt-1">`/api/og/generic?title=Changelog`: logo + one word on black. Austere template that works for every page.</p>
      <a href="https://linear.app/changelog" class="text-xs text-blue-500 mt-2 block">linear.app →</a>
    </div>
  </div>
</div>

## Illustrated and editorial

A commissioned picture. Reads as a magazine cover, so it stands out in a feed of screenshots.

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/every.jpg" alt="Every link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Every</h3>
      <p class="text-sm text-gray-600 mt-1">Row of illustrated postage stamps under a serif headline. Editorial, warm, very un-SaaS.</p>
      <a href="https://every.to/" class="text-xs text-blue-500 mt-2 block">every.to →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/cloudflare.jpg" alt="Cloudflare blog post link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Cloudflare blog post</h3>
      <p class="text-sm text-gray-600 mt-1">Each post gets its own flat illustration in a fixed pastel style. Recognisable before you read the title.</p>
      <a href="https://blog.cloudflare.com/" class="text-xs text-blue-500 mt-2 block">blog.cloudflare.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/posthog.jpg" alt="PostHog link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">PostHog</h3>
      <p class="text-sm text-gray-600 mt-1">Their hedgehog mascot plus a big yellow headline. Brand-led and funny, and consistent across the site.</p>
      <a href="https://posthog.com/blog" class="text-xs text-blue-500 mt-2 block">posthog.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/partiful.jpg" alt="Partiful link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Partiful</h3>
      <p class="text-sm text-gray-600 mt-1">Collage of real event flyers. Sells the product by showing what users make.</p>
      <a href="https://partiful.com/" class="text-xs text-blue-500 mt-2 block">partiful.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/framer.jpg" alt="Framer link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Framer</h3>
      <p class="text-sm text-gray-600 mt-1">Grid of sites made with Framer: the gallery is the pitch.</p>
      <a href="https://www.framer.com/" class="text-xs text-blue-500 mt-2 block">framer.com →</a>
    </div>
  </div>
</div>

## Product UI as the image

A cropped, polished screenshot. Fine for landing pages; weaker for content pages.

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/cal.jpg" alt="Cal.com link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Cal.com</h3>
      <p class="text-sm text-gray-600 mt-1">Headline left, booking UI right, on white. Clear and quiet.</p>
      <a href="https://cal.com/" class="text-xs text-blue-500 mt-2 block">cal.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/notion.jpg" alt="Notion link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Notion</h3>
      <p class="text-sm text-gray-600 mt-1">Headline with a highlighted word, a row of avatars, the product underneath.</p>
      <a href="https://www.notion.com/" class="text-xs text-blue-500 mt-2 block">notion.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/raycast.jpg" alt="Raycast link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Raycast</h3>
      <p class="text-sm text-gray-600 mt-1">Dark product shot with glow; the command bar is the hero.</p>
      <a href="https://www.raycast.com/" class="text-xs text-blue-500 mt-2 block">raycast.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/resend.jpg" alt="Resend link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Resend</h3>
      <p class="text-sm text-gray-600 mt-1">Black, one line of type, faint code. Developer-premium.</p>
      <a href="https://resend.com/" class="text-xs text-blue-500 mt-2 block">resend.com →</a>
    </div>
  </div>
</div>

## Minimal brand mark

Just the logo or one line. Safe and elegant, but every page looks the same, so it says nothing about the page being shared.

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/anthropic.jpg" alt="Anthropic link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Anthropic</h3>
      <p class="text-sm text-gray-600 mt-1">Wordmark on warm off-white. Quiet confidence.</p>
      <a href="https://www.anthropic.com/" class="text-xs text-blue-500 mt-2 block">anthropic.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/arc.jpg" alt="Arc (farewell) link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Arc (farewell)</h3>
      <p class="text-sm text-gray-600 mt-1">Logo + one serif line on black: "A farewell to Arc". A minimal card can still carry a message.</p>
      <a href="https://arc.net/" class="text-xs text-blue-500 mt-2 block">arc.net →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/nextjs-post.jpg" alt="Next.js 15 link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Next.js 15</h3>
      <p class="text-sm text-gray-600 mt-1">Version lock-up with thin construction lines. Turns a release into an event.</p>
      <a href="https://nextjs.org/blog/next-15" class="text-xs text-blue-500 mt-2 block">nextjs.org →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/supabase.jpg" alt="Supabase Launch Week 15 link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Supabase Launch Week 15</h3>
      <p class="text-sm text-gray-600 mt-1">"LW 15" with a 3D object between. Campaign identity.</p>
      <a href="https://supabase.com/launch-week" class="text-xs text-blue-500 mt-2 block">supabase.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/stripe-press.jpg" alt="Stripe Press link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Stripe Press</h3>
      <p class="text-sm text-gray-600 mt-1">Tiny gold mark on black. Bookish restraint, maybe too small to read at chat size.</p>
      <a href="https://press.stripe.com/" class="text-xs text-blue-500 mt-2 block">press.stripe.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/apple.jpg" alt="Apple link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Apple</h3>
      <p class="text-sm text-gray-600 mt-1">Grey apple on white. The far end of minimal.</p>
      <a href="https://www.apple.com/" class="text-xs text-blue-500 mt-2 block">apple.com →</a>
    </div>
  </div>
</div>

## The content is the image

Media sites just use the thing itself. Hard to beat when you have it.

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/spotify.jpg" alt="Spotify album link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Spotify album</h3>
      <p class="text-sm text-gray-600 mt-1">The album cover, square, full bleed.</p>
      <a href="https://open.spotify.com/" class="text-xs text-blue-500 mt-2 block">open.spotify.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/youtube.jpg" alt="YouTube link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">YouTube</h3>
      <p class="text-sm text-gray-600 mt-1">The video thumbnail at max resolution.</p>
      <a href="https://www.youtube.com/" class="text-xs text-blue-500 mt-2 block">youtube.com →</a>
    </div>
  </div>
</div>

## Counter-examples

What to avoid.

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/substack.jpg" alt="Substack publication home link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Substack publication home</h3>
      <p class="text-sm text-gray-600 mt-1">400×400 logo, which platforms show as a small thumbnail or stretch. Individual Substack posts do better.</p>
      <a href="https://www.lennysnewsletter.com/" class="text-xs text-blue-500 mt-2 block">lennysnewsletter.com →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/gwern.jpg" alt="Gwern link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Gwern</h3>
      <p class="text-sm text-gray-600 mt-1">Tall 1238×1400 logo: the wrong shape for a 1.91:1 slot, so it gets cropped or letterboxed. The site is lovely; the card isn't.</p>
      <a href="https://gwern.net/" class="text-xs text-blue-500 mt-2 block">gwern.net →</a>
    </div>
  </div>
  <div class="rounded-lg overflow-hidden border border-gray-200 shadow-sm">
    <img src="./images/vercel-post.jpg" alt="Vercel blog post link preview image" class="w-full" />
    <div class="p-4">
      <h3 class="font-semibold text-base">Vercel blog post</h3>
      <p class="text-sm text-gray-600 mt-1">The post falls back to the site-wide triangle, so every post looks the same. Missed chance.</p>
      <a href="https://vercel.com/blog" class="text-xs text-blue-500 mt-2 block">vercel.com →</a>
    </div>
  </div>
</div>

## Sizes and crops

- **Make it 1200×630 (1.91:1).** It's the common default: Facebook, LinkedIn, Slack, Discord and X `summary_large_image` all take it. Retina-minded sites (Raycast, Anthropic, Framer) serve 2400×1260.
- Add `og:image:width` / `og:image:height` so platforms can lay out the card before the image loads.
- `twitter:card` = `summary_large_image` for the big card; `summary` gives a small square thumbnail.
- **Crops vary by platform.** Zoom chat and X are wide; WhatsApp and iMessage often crop square or show a thumbnail. Luma's own image shows the problem. Here is the same image at 1200×630 and cropped square by its CDN:

<div class="grid grid-cols-2 gap-4 mt-4">
  <img src="./images/luma-1200x630.jpg" alt="Luma og image at 1200x630" />
  <img src="./images/luma-800x800.jpg" alt="Luma og image cropped square, title cut off" />
</div>

  The square crop cuts the title. Keep the essentials in the centre square (about 630×630) if WhatsApp matters.

## Tools

- Preview across platforms: [opengraph.xyz](https://www.opengraph.xyz/), [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/), and paste the link into a Slack DM to yourself.
- Generate per page: [Vercel OG / `@vercel/og`](https://vercel.com/docs/og-image-generation) (JSX to PNG, used by Next.js `opengraph-image`), [Satori](https://github.com/vercel/satori), or a Cloudflare Worker. Luma and Linear both use a URL-parameterised endpoint (`/og?title=…`).
- Resize on the fly: Luma serves one master image through Cloudflare image resizing (`width=,height=,fit=cover`).

## How to add an example

Fetch the page's `og:image` (e.g. `curl -sL URL | grep og:image`), save it to `images/{slug}.jpg` at 1200px wide, and add a card to the right section. If you have a screenshot of how the preview looked in a real chat, add that too; it shows the crop, which the raw image doesn't.
