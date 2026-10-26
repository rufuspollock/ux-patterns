# How previews vary from page to page

[SEO Preview Images](./README.md) shows each site's home page. This page asks the more useful question: **what does the preview look like on the site's ordinary pages** (blog posts, docs pages, wiki notes)? On a blog or knowledge base it's the inner pages that get shared.

Method: for 26 blogs, docs sites and wikis, I took the `og:image` of 2–3 inner pages each (2026-10-26) and put them side by side. Each row below is one site. Click an image to open the page.

## TL;DR

Sites use one of four strategies, or combine them:

1. **Same image everywhere.** Every page shares the logo card. Zero variation (MDN; Anthropic news, mostly).
2. **One template, new art per post.** A fixed frame (logo, title position, colours) with a new picture each time (Cloudflare, Vercel, Stripe, Supabase). The best look, but someone has to make the art.
3. **Generated text card.** A template filled from the page's title, description and section, with no picture (Obsidian Help, Next.js, Astro, Mintlify, Tailwind, Stripe Docs, Life Itself). This is how docs and wikis get variety for free.
4. **Image from the page itself.** The first figure, lead image, chart or cover (Gwern, Wikipedia, Our World in Data, LessWrong, Flowershow blog). Great when there is one; when there isn't, you fall back to the logo or get nothing.

**The answer for Flowershow-like sites is to combine them:** use the page's own image when it has one, otherwise a generated card (Linear does this).


## 1. Same image everywhere

The preview tells you nothing about the page. Fine for a home page, a waste on a post.

### MDN

Same logo card on every docs page, even though each page has a clear title and section.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta"><img src="./images/per-page/mdn-0.jpg" alt="<meta> HTML metadata element - HTML | MDN" title="<meta> HTML metadata element - HTML | MDN" class="w-full rounded border border-gray-200" /></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid"><img src="./images/per-page/mdn-1.jpg" alt="grid CSS property - CSS | MDN" title="grid CSS property - CSS | MDN" class="w-full rounded border border-gray-200" /></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map"><img src="./images/per-page/mdn-2.jpg" alt="Array.prototype.map() - JavaScript | MDN" title="Array.prototype.map() - JavaScript | MDN" class="w-full rounded border border-gray-200" /></a>
</div>

### Anthropic news

Mostly the wordmark. Only some posts get their own art (middle).

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://www.anthropic.com/news/announcements"><img src="./images/per-page/anthropic-news-0.jpg" alt="Announcements" title="Announcements" class="w-full rounded border border-gray-200" /></a>
  <a href="https://www.anthropic.com/news/public-benefit-fund"><img src="./images/per-page/anthropic-news-1.jpg" alt="Investing in the public benefit" title="Investing in the public benefit" class="w-full rounded border border-gray-200" /></a>
  <a href="https://www.anthropic.com/news/cyber-verification-program"><img src="./images/per-page/anthropic-news-2.jpg" alt="Expanding the Cyber Verification Program" title="Expanding the Cyber Verification Program" class="w-full rounded border border-gray-200" /></a>
</div>

## 2. One template, new art per post

A fixed frame makes the brand obvious; new art inside it makes each post its own. Needs a designer or an illustration habit.

### Cloudflare blog

The clearest system: logo top-left, title left, an illustration right. Light or dark per post.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://blog.cloudflare.com/origin-range-requests/"><img src="./images/per-page/cloudflare-blog-0.jpg" alt="Origin Range Requests: Serving large files without range-request tuning" title="Origin Range Requests: Serving large files without range-request tuning" class="w-full rounded border border-gray-200" /></a>
  <a href="https://blog.cloudflare.com/post-quantum-geo-key-manager/"><img src="./images/per-page/cloudflare-blog-1.jpg" alt="Bringing post-quantum cryptography to geographically fenced key management" title="Bringing post-quantum cryptography to geographically fenced key management" class="w-full rounded border border-gray-200" /></a>
  <a href="https://blog.cloudflare.com/full-transaction-waf/"><img src="./images/per-page/cloudflare-blog-2.jpg" alt="Introducing full transaction detection for Cloudflare WAF" title="Introducing full transaction detection for Cloudflare WAF" class="w-full rounded border border-gray-200" /></a>
</div>

### Vercel blog

Black, triangle, title, plus a product drawing. Very consistent.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://vercel.com/blog/backends-on-vercel-python-containers-and-daemons"><img src="./images/per-page/vercel-blog-0.jpg" alt="Backends on Vercel: Python, containers, and Daemons" title="Backends on Vercel: Python, containers, and Daemons" class="w-full rounded border border-gray-200" /></a>
  <a href="https://vercel.com/blog/introducing-vercel-drives-persistent-storage-for-agents"><img src="./images/per-page/vercel-blog-1.jpg" alt="Introducing Vercel Drives: persistent storage for agents" title="Introducing Vercel Drives: persistent storage for agents" class="w-full rounded border border-gray-200" /></a>
  <a href="https://vercel.com/blog/how-vercel-agent-accesses-production-safely"><img src="./images/per-page/vercel-blog-3.jpg" alt="How Vercel Agent accesses production safely" title="How Vercel Agent accesses production safely" class="w-full rounded border border-gray-200" /></a>
</div>

### Stripe blog

Gradient field, title, sometimes a product shot.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://stripe.com/blog/trends-from-money20-20-2026-the-rise-of-hidden-financial-services"><img src="./images/per-page/stripe-blog-1.jpg" alt="Trends from Money20/20 2026: The rise of “hidden” financial services " title="Trends from Money20/20 2026: The rise of “hidden” financial services " class="w-full rounded border border-gray-200" /></a>
  <a href="https://stripe.com/blog/new-ways-for-fintechs-to-move-money-and-expand-globally"><img src="./images/per-page/stripe-blog-2.jpg" alt="New ways for fintechs to move money and expand globally" title="New ways for fintechs to move money and expand globally" class="w-full rounded border border-gray-200" /></a>
  <a href="https://stripe.com/blog/real-time-stripe-data-postgres"><img src="./images/per-page/stripe-blog-3.jpg" alt="Sync real-time Stripe data to Postgres with Stripe Data Pipeline" title="Sync real-time Stripe data to Postgres with Stripe Data Pipeline" class="w-full rounded border border-gray-200" /></a>
</div>

### Supabase blog

Dark, green accent, title plus UI or code.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://supabase.com/blog/give-your-supabase-app-its-own-mcp-server"><img src="./images/per-page/supabase-blog-0.jpg" alt="Give your Supabase app its own MCP server" title="Give your Supabase app its own MCP server" class="w-full rounded border border-gray-200" /></a>
  <a href="https://supabase.com/blog/getting-started-with-the-supabase-dotnet-sdk"><img src="./images/per-page/supabase-blog-1.jpg" alt="Getting started with the Supabase .NET SDK" title="Getting started with the Supabase .NET SDK" class="w-full rounded border border-gray-200" /></a>
  <a href="https://supabase.com/blog/operate-with-confidence-check-production-with-your-coding-agent"><img src="./images/per-page/supabase-blog-3.jpg" alt="Operate with confidence: check production with your coding agent" title="Operate with confidence: check production with your coding agent" class="w-full rounded border border-gray-200" /></a>
</div>

### GitHub blog

Topic art reused across posts (AI, Copilot, generic Mona). Varies by category, not by post.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://github.blog/ai-and-ml/generative-ai/how-ai-code-generation-works/"><img src="./images/per-page/github-blog-0.jpg" alt="How AI code generation works" title="How AI code generation works" class="w-full rounded border border-gray-200" /></a>
  <a href="https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/"><img src="./images/per-page/github-blog-2.jpg" alt="The bridge to agent-scale Git infrastructure" title="The bridge to agent-scale Git infrastructure" class="w-full rounded border border-gray-200" /></a>
  <a href="https://github.blog/ai-and-ml/github-copilot/how-3-java-champions-are-using-github-copilot-for-increased-productivity/"><img src="./images/per-page/github-blog-3.jpg" alt="How 3 Java Champions are using GitHub Copilot for increased productivity" title="How 3 Java Champions are using GitHub Copilot for increased productivity" class="w-full rounded border border-gray-200" /></a>
</div>

### Fully bespoke art

No frame, just a commissioned image or a hand-made title card per post.

### Every

A new editorial illustration for every piece. The magazine end of the scale.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://every.to/guides/openai-dots-guide"><img src="./images/per-page/every-0.jpg" alt="Dots: A Guide for Putting OpenAI’s Always-on Agents to Work" title="Dots: A Guide for Putting OpenAI’s Always-on Agents to Work" class="w-full rounded border border-gray-200" /></a>
  <a href="https://every.to/context-window/anthropic-s-duet-gets-to-work"><img src="./images/per-page/every-2.jpg" alt="Anthropic’s Duet Gets to Work" title="Anthropic’s Duet Gets to Work" class="w-full rounded border border-gray-200" /></a>
  <a href="https://every.to/vibe-check/vibe-check-duet-anthropic-s-always-on-agent"><img src="./images/per-page/every-3.jpg" alt="Vibe Check: Duet—Anthropic's Always-on Agent" title="Vibe Check: Duet—Anthropic's Always-on Agent" class="w-full rounded border border-gray-200" /></a>
</div>

### Josh Comeau

Hand-made per post: big title, a code-y background and his avatar. Unmistakably him.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://www.joshwcomeau.com/css/interop-2027/"><img src="./images/per-page/joshcomeau-0.jpg" alt="The Future of CSS ✨ • Josh W. Comeau" title="The Future of CSS ✨ • Josh W. Comeau" class="w-full rounded border border-gray-200" /></a>
  <a href="https://www.joshwcomeau.com/css/anchor-positioning/"><img src="./images/per-page/joshcomeau-1.jpg" alt="Getting Started with Anchor Positioning • Josh W. Comeau" title="Getting Started with Anchor Positioning • Josh W. Comeau" class="w-full rounded border border-gray-200" /></a>
  <a href="https://www.joshwcomeau.com/animation/scroll-driven-animations/"><img src="./images/per-page/joshcomeau-3.jpg" alt="Scroll-Driven Animations • Josh W. Comeau" title="Scroll-Driven Animations • Josh W. Comeau" class="w-full rounded border border-gray-200" /></a>
</div>

### Hugging Face blog

Each author makes a thumbnail, so quality varies, but the emoji mascot holds it together.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://huggingface.co/blog/torch-neuronx-model-support"><img src="./images/per-page/hf-blog-1.jpg" alt="Does Your Model Run on AWS Trainium? Look It Up" title="Does Your Model Run on AWS Trainium? Look It Up" class="w-full rounded border border-gray-200" /></a>
  <a href="https://huggingface.co/blog/hf-torchtpu"><img src="./images/per-page/hf-blog-2.jpg" alt="Hugging Face ❤️ TorchTPU: TPUs, Natively" title="Hugging Face ❤️ TorchTPU: TPUs, Natively" class="w-full rounded border border-gray-200" /></a>
  <a href="https://huggingface.co/blog/anylanguagemodel-1-0"><img src="./images/per-page/hf-blog-3.jpg" alt="AnyLanguageModel 1.0: One Year of Local Models on Apple Platforms" title="AnyLanguageModel 1.0: One Year of Local Models on Apple Platforms" class="w-full rounded border border-gray-200" /></a>
</div>

## 3. Generated text card

The docs and wiki answer: one template, filled from title, description and section. Every page gets a distinct preview with zero effort. Usually a dark or light field with the logo, a big title, a one-line description and often the section name.

### Obsidian Help

Title, the page's first sentence, logo. `ogimage.obsidian.md/og-image.png?title=…&description=…`. A text-only wiki that still previews well.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://help.obsidian.md/Home"><img src="./images/per-page/obsidian-help-0.jpg" alt="Home - Obsidian Help" title="Home - Obsidian Help" class="w-full rounded border border-gray-200" /></a>
  <a href="https://help.obsidian.md/Files+and+folders/Accepted+file+formats"><img src="./images/per-page/obsidian-help-1.jpg" alt="Accepted file formats - Obsidian Help" title="Accepted file formats - Obsidian Help" class="w-full rounded border border-gray-200" /></a>
  <a href="https://help.obsidian.md/Plugins/Graph+view"><img src="./images/per-page/obsidian-help-3.jpg" alt="Graph view - Obsidian Help" title="Graph view - Obsidian Help" class="w-full rounded border border-gray-200" /></a>
</div>

### Next.js docs

Title plus section ("Getting Started", "Functions"). Signed URL so nobody can render arbitrary text.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://nextjs.org/docs/app/getting-started/installation"><img src="./images/per-page/nextjs-docs-0.jpg" alt="Installation" title="Installation" class="w-full rounded border border-gray-200" /></a>
  <a href="https://nextjs.org/docs/app/api-reference/functions/generate-metadata"><img src="./images/per-page/nextjs-docs-1.jpg" alt="generateMetadata" title="generateMetadata" class="w-full rounded border border-gray-200" /></a>
  <a href="https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image"><img src="./images/per-page/nextjs-docs-2.jpg" alt="opengraph-image and twitter-image" title="opengraph-image and twitter-image" class="w-full rounded border border-gray-200" /></a>
</div>

### Astro docs

Pre-rendered at build time (`/open-graph/en/….webp`). Title, description, purple edge.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://docs.astro.build/en/getting-started/"><img src="./images/per-page/astro-docs-0.jpg" alt="Getting started" title="Getting started" class="w-full rounded border border-gray-200" /></a>
  <a href="https://docs.astro.build/en/guides/markdown-content/"><img src="./images/per-page/astro-docs-1.jpg" alt="Markdown in Astro" title="Markdown in Astro" class="w-full rounded border border-gray-200" /></a>
  <a href="https://docs.astro.build/en/guides/images/"><img src="./images/per-page/astro-docs-2.jpg" alt="Images" title="Images" class="w-full rounded border border-gray-200" /></a>
</div>

### Mintlify

Section ("Get started", "Formatting"), title and description. Every Mintlify docs site gets this.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://mintlify.com/docs"><img src="./images/per-page/mintlify-0.jpg" alt="Introduction - Mintlify" title="Introduction - Mintlify" class="w-full rounded border border-gray-200" /></a>
  <a href="https://mintlify.com/docs/quickstart"><img src="./images/per-page/mintlify-1.jpg" alt="Quickstart - Mintlify" title="Quickstart - Mintlify" class="w-full rounded border border-gray-200" /></a>
  <a href="https://mintlify.com/docs/text"><img src="./images/per-page/mintlify-2.jpg" alt="Format text - Mintlify" title="Format text - Mintlify" class="w-full rounded border border-gray-200" /></a>
</div>

### Tailwind docs

Section, title, description, version badge, over faint construction lines.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://tailwindcss.com/docs/installation"><img src="./images/per-page/tailwind-docs-0.jpg" alt="Installing with Vite - Installation" title="Installing with Vite - Installation" class="w-full rounded border border-gray-200" /></a>
  <a href="https://tailwindcss.com/docs/font-size"><img src="./images/per-page/tailwind-docs-1.jpg" alt="font-size - Typography" title="font-size - Typography" class="w-full rounded border border-gray-200" /></a>
  <a href="https://tailwindcss.com/docs/grid-template-columns"><img src="./images/per-page/tailwind-docs-2.jpg" alt="grid-template-columns - Flexbox & Grid" title="grid-template-columns - Flexbox & Grid" class="w-full rounded border border-gray-200" /></a>
</div>

### Stripe Docs

Title and description on navy with a gradient rule.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://docs.stripe.com/payments"><img src="./images/per-page/stripe-docs-0.jpg" alt="Paiements" title="Paiements" class="w-full rounded border border-gray-200" /></a>
  <a href="https://docs.stripe.com/webhooks"><img src="./images/per-page/stripe-docs-2.jpg" alt="Recevez les événements Stripe dans votre endpoint de webhook" title="Recevez les événements Stripe dans votre endpoint de webhook" class="w-full rounded border border-gray-200" /></a>
</div>

### Life Itself (Flowershow)

Flowershow's own generated card: site logo and name, serif title, description, URL, orange edge.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://lifeitself.org/"><img src="./images/per-page/lifeitself-0.jpg" alt="Home | Life Itself Collective" title="Home | Life Itself Collective" class="w-full rounded border border-gray-200" /></a>
  <a href="https://lifeitself.org/about"><img src="./images/per-page/lifeitself-1.jpg" alt="About | Life Itself Collective" title="About | Life Itself Collective" class="w-full rounded border border-gray-200" /></a>
  <a href="https://lifeitself.org/blog"><img src="./images/per-page/lifeitself-2.jpg" alt="Blog | Life Itself Collective" title="Blog | Life Itself Collective" class="w-full rounded border border-gray-200" /></a>
</div>

### Maggie Appleton

Same idea with a personal touch: the plant illustration is fixed, the title and description change.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://maggieappleton.com/garden"><img src="./images/per-page/maggie-2.jpg" alt="The Garden of Maggie Appleton" title="The Garden of Maggie Appleton" class="w-full rounded border border-gray-200" /></a>
  <a href="https://maggieappleton.com/essays"><img src="./images/per-page/maggie-3.jpg" alt="Essays by Maggie Appleton" title="Essays by Maggie Appleton" class="w-full rounded border border-gray-200" /></a>
</div>

## 4. Image from the page itself

Use the page's own picture: its first figure, lead image, chart or cover. Honest and varied, and free if pages have images. The weak spot is pages without one.

### Gwern

The essay's own first figure (a GPT-3 scaling plot). When there's no figure, back to the tall logo (right).

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://gwern.net/scaling-hypothesis"><img src="./images/per-page/gwern-0.jpg" alt="The Scaling Hypothesis" title="The Scaling Hypothesis" class="w-full rounded border border-gray-200" /></a>
  <a href="https://gwern.net/spaced-repetition"><img src="./images/per-page/gwern-1.jpg" alt="Spaced Repetition for Efficient Learning" title="Spaced Repetition for Efficient Learning" class="w-full rounded border border-gray-200" /></a>
  <a href="https://gwern.net/doc/index"><img src="./images/per-page/gwern-2.jpg" alt="‘docs’ directory" title="‘docs’ directory" class="w-full rounded border border-gray-200" /></a>
</div>

### Wikipedia

The article's lead image. Pages without one (e.g. "Markdown") get **no image at all**.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://en.wikipedia.org/wiki/Open_data"><img src="./images/per-page/wikipedia-0.jpg" alt="Open data - Wikipedia" title="Open data - Wikipedia" class="w-full rounded border border-gray-200" /></a>
  <a href="https://en.wikipedia.org/wiki/Ada_Lovelace"><img src="./images/per-page/wikipedia-1.jpg" alt="Ada Lovelace - Wikipedia" title="Ada Lovelace - Wikipedia" class="w-full rounded border border-gray-200" /></a>
  <a href="https://en.wikipedia.org/wiki/Wiki"><img src="./images/per-page/wikipedia-3.jpg" alt="Wiki - Wikipedia" title="Wiki - Wikipedia" class="w-full rounded border border-gray-200" /></a>
</div>

### Our World in Data

The chart is the preview. Grapher pages render the chart itself as the `og:image`.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://ourworldindata.org/co2-emissions"><img src="./images/per-page/owid-0.jpg" alt="CO₂ emissions" title="CO₂ emissions" class="w-full rounded border border-gray-200" /></a>
  <a href="https://ourworldindata.org/life-expectancy"><img src="./images/per-page/owid-1.jpg" alt="Life Expectancy" title="Life Expectancy" class="w-full rounded border border-gray-200" /></a>
  <a href="https://ourworldindata.org/grapher/share-of-population-in-extreme-poverty"><img src="./images/per-page/owid-2.jpg" alt="Share of population living in extreme poverty" title="Share of population living in extreme poverty" class="w-full rounded border border-gray-200" /></a>
</div>

### LessWrong

The post's first image or an author-set social image, cropped to 1.91:1 by Cloudinary.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://www.lesswrong.com/posts/3375SZNGA5dKHQMie/i-did-this-without-your-knowledge"><img src="./images/per-page/lesswrong-0.jpg" alt="I Did This Without Your Knowledge — LessWrong" title="I Did This Without Your Knowledge — LessWrong" class="w-full rounded border border-gray-200" /></a>
  <a href="https://www.lesswrong.com/posts/R5g8YT25G9DXJJ48n/glm-5-3-sometimes-considers-how-train-time-actions-shape"><img src="./images/per-page/lesswrong-1.jpg" alt="GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior — LessWrong" title="GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior — LessWrong" class="w-full rounded border border-gray-200" /></a>
  <a href="https://www.lesswrong.com/posts/oA23zoEjPnzqfHiCt/there-is-way-too-much-serendipity"><img src="./images/per-page/lesswrong-3.jpg" alt="There is way too much serendipity — LessWrong" title="There is way too much serendipity — LessWrong" class="w-full rounded border border-gray-200" /></a>
</div>

### Jacky Zhao (Quartz)

A mix: hand-made cards for some posts, a photo for others.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://jzhao.xyz/posts/eg-strider"><img src="./images/per-page/quartz-jzhao-0.jpg" alt="Making Eg-walker even faster" title="Making Eg-walker even faster" class="w-full rounded border border-gray-200" /></a>
  <a href="https://jzhao.xyz/posts/dappled-light"><img src="./images/per-page/quartz-jzhao-1.jpg" alt="Experiments in procedural dappled light shaders" title="Experiments in procedural dappled light shaders" class="w-full rounded border border-gray-200" /></a>
  <a href="https://jzhao.xyz/posts/driving"><img src="./images/per-page/quartz-jzhao-3.jpg" alt="On driving" title="On driving" class="w-full rounded border border-gray-200" /></a>
</div>

### Flowershow blog

A Japanese woodblock print as the cover for each post (frontmatter `image`). Beautiful and consistent, but raw: no title on the card.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://flowershow.app/blog/show-a-list-of-pages-anywhere"><img src="./images/per-page/flowershow-blog-0.jpg" alt="Show your latest posts anywhere | Flowershow" title="Show your latest posts anywhere | Flowershow" class="w-full rounded border border-gray-200" /></a>
  <a href="https://flowershow.app/blog/listing-pages-tutorial"><img src="./images/per-page/flowershow-blog-1.jpg" alt="Build a blog, portfolio or team page | Flowershow" title="Build a blog, portfolio or team page | Flowershow" class="w-full rounded border border-gray-200" /></a>
  <a href="https://flowershow.app/blog/2026-08-08-whats-actually-changeable-in-theming"><img src="./images/per-page/flowershow-blog-2.jpg" alt="What you can change in Flowershow theming, and who can | Flowershow" title="What you can change in Flowershow theming, and who can | Flowershow" class="w-full rounded border border-gray-200" /></a>
</div>

## Combining them: a fallback chain

Use hand-made art when a page has it and a generated card when it doesn't. Every page looks deliberate.

### Linear

Hub pages get the generated `/api/og/generic?title=…` card (left); essays get their own art (middle, right).

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://linear.app/now/product-launches"><img src="./images/per-page/linear-now-0.jpg" alt="Product launches - Linear" title="Product launches - Linear" class="w-full rounded border border-gray-200" /></a>
  <a href="https://linear.app/now/five-principles-working-with-loops"><img src="./images/per-page/linear-now-2.jpg" alt="Five principles for working with Loops" title="Five principles for working with Loops" class="w-full rounded border border-gray-200" /></a>
  <a href="https://linear.app/now/ci-bottleneck-reworked"><img src="./images/per-page/linear-now-3.jpg" alt="AI coding has made CI a bottleneck, so we reworked ours to keep up" title="AI coding has made CI a bottleneck, so we reworked ours to keep up" class="w-full rounded border border-gray-200" /></a>
</div>

### Substack (Lenny's Newsletter)

The post's image, cropped to 1200×675. I didn't check what a post with no image gets.

<div class="grid grid-cols-3 gap-2 mt-2 mb-6">
  <a href="https://www.lennysnewsletter.com/p/how-to-tell-if-a-startup-has-a-moat"><img src="./images/per-page/substack-lenny-1.jpg" alt="How to tell if a startup has a moat " title="How to tell if a startup has a moat " class="w-full rounded border border-gray-200" /></a>
  <a href="https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit"><img src="./images/per-page/substack-lenny-2.jpg" alt="All of the Lenny & Friends Summit talks are now online!" title="All of the Lenny & Friends Summit talks are now online!" class="w-full rounded border border-gray-200" /></a>
  <a href="https://www.lennysnewsletter.com/p/advanced-evals-how-to-find-and-fix"><img src="./images/per-page/substack-lenny-3.jpg" alt="Advanced evals: How to find (and fix) hidden AI failures in your product" title="Advanced evals: How to find (and fix) hidden AI failures in your product" class="w-full rounded border border-gray-200" /></a>
</div>

## What this means for Flowershow-like sites

Flowershow sites are mostly blogs, wikis and knowledge bases written in Markdown, so most pages have no picture. What they need:

1. **A generated card for every page by default** (strategy 3). Title, description (frontmatter, else a cleaned first sentence: Obsidian's card shows a run-on dump of page text, so leave it out rather than do that), site name and logo, and the **section or folder** ("Notes", "Blog", "Docs › Config"). The section is cheap and is what makes wiki previews look varied (Next.js, Mintlify, Tailwind).
2. **The page's featured image when it has one** (frontmatter `image`). Two ways to show it:
   - **Raw**, like the Flowershow blog's woodblock prints, Every and Substack. Best when the image is already a designed card or strong art. Crop it to 1.91:1 around the centre: the woodblock covers are 3:2 and get cut at the edges.
   - **Composed into the card**: picture on one side, title on the other, like Luma, Cloudflare and Vercel. The site stays recognisable and the title still shows. Probably the better default for a mixed site.
3. **Optional: the first image in the page** (Gwern, LessWrong). Off by default, since a random screenshot can make a worse card than text.
4. **Site image only for the home page**, and as a last resort. A site-wide image on every page is the MDN failure.
5. **The card should look like the site**: its fonts, colours and logo, not a generic template. Astro, Tailwind, Stripe and Obsidian cards are each instantly recognisable.

### Where Flowershow is today

I checked the Flowershow code: `resolveSocialImage` in `apps/flowershow/lib/social-preview.ts` (origin/main, 2026-10-26). The generated card is `/_og/…`, rendered with Satori from `components/og/social-card.tsx`. With social cards on, a page's preview is:

| Site | Page has `image` | No page image, site has `image` | Neither |
|---|---|---|---|
| Free | generated card (page image **ignored**) | generated card | generated card |
| Premium | page image, raw | **site image, on every such page** | generated card |
| Password-protected | site-level card | site-level card | site-level card |

- Good: the generated card exists and works (see Life Itself above). It shows logo, title, description and URL.
- **Gap 1 (premium):** a site-wide `image` beats the per-page card. Set one, and every page without its own image shows the same picture, the MDN failure. Fix: page image → generated card, with the site image only for `/`.
- **Gap 2 (free):** the opposite problem. A page's featured image never shows. Whether to allow it is a product call, but the featured image is the best preview a page has.
- **Gap 3:** a page `image` is used raw and uncropped. There's no composed option with the title on it.
- **Gap 4:** the card has a fixed look (orange edge, Source Serif and Inter) rather than the site's theme, and no section or breadcrumb line.
