# How to get Good Average ...

> What I see is I am getting results from this that are ok but quite middle of the road without much real personality or distinctiveness. How would I get Claude to be really creative ? Perhaps we mood board first and can Claude do mood parsing in a meaningful way?

This is a really sharp observation, and you're hitting on a real limitation in how most people prompt Claude for design work.

The core problem is that **vague creative briefs produce averaged-out results** — Claude (like any generative tool) defaults to the statistical centre of "good design" when given room to interpret. The fix is to force specificity before you generate anything.

---

## Why Moodboards Work (and Where Claude Can Help)

A moodboard isn't just aesthetic inspiration — it's a **constraint device**. It forces you to commit to a specific intersection of references before any design decision is made. Claude can genuinely help with mood *parsing* if you approach it right.

### What Claude can do well:
- **Extract design DNA from descriptions** — if you describe or paste images, Claude can articulate *why* something feels the way it does (not just "it's minimal" but "it uses geometric tension, editorial whitespace, and a single chromatic accent against neutral")
- **Translate cultural references into design language** — "feels like a 1970s Italian car magazine" → specific font moods, colour palette territory, layout logic
- **Identify the *specific* characteristics** that create a feeling, which you can then use as hard constraints

### Where it breaks down:
Claude can't *see* moodboard images natively in a design sense — it can describe what's in them but won't always extract the *gestalt*. You need to do some of that translation work yourself, or use it as a dialogue.

---

## A Better Creative Process

Instead of "design me a system", try this sequence:

**Step 1 — Reference Deconstruction**
Gather 5–8 images that feel right (Behance, Are.na, Muzli, Dribbble). Then ask Claude:

> *"I'm going to describe some reference images. For each one, extract: the specific typographic mood, the spatial logic, the colour behaviour, and the emotional register. Then find what they share."*

This gives you a **parsed creative brief** rather than a vague direction.

**Step 2 — The Constraint Brief**
Ask Claude to write you a design constraint document that is almost *uncomfortably specific*:

> *"Based on these parsed references, write a design constraint brief that would make it impossible to produce generic output. Include: exact typographic personality (not just 'serif' — what kind of serif, what era, what feeling), colour behaviour rules (not hex codes — how colour should act), spatial logic (how things should be spaced and why), and one thing this design should NEVER do."*

**Step 3 — Pressure-Test With Opposites**
Ask Claude: *"What would the opposite of this design system look like?"* — then use that as an explicit exclusion list.

**Step 4 — Generate From Hard Constraints**
Only now do you ask for actual output. With tight constraints Claude produces genuinely distinctive work instead of averaging toward safe choices.

---

## Prompting for Real Creativity

A few specific techniques that unlock better output:

**Name a specific intersection, not a vibe:**
Instead of *"modern and clean"* → *"the intersection of Swiss grid design and 1990s rave flyers"*

**Give Claude a creative persona:**
*"You are a type designer who worked at Emigre in the 90s and now runs a boutique digital studio. How would you approach this?"*

**Force an opinion:**
*"Don't give me options — make a single bold decision and defend it"*

**Use negative constraints explicitly:**
*"This should never look like a SaaS product, a fintech app, or anything that uses Inter or a purple gradient"*

**Ask for the unexpected move:**
*"What's the least expected design direction that would still work for this brand? Describe it specifically."*

---

## Practical Moodboard Workflow With Claude

1. Build your moodboard in **Are.na, Notion, or even a Pinterest board**
2. Screenshot or describe 4–5 key references to Claude
3. Ask it to extract the *specific characteristics* (not adjectives — mechanics)
4. Have it synthesise a constraint brief
5. Use that brief as your system prompt for all subsequent design generation


# XXX

> And how I can have Claude help with first part ie the mood boarding to have those examples or do I have to do that myself.

Great question — and honestly this is where Claude can add a lot of value that most people don't use it for.

You don't have to do the moodboard gathering yourself. Claude can act as a **creative director** in the early stage, helping you *discover and articulate* the right references before you've even seen them.

---

## What Claude Can Do in the Moodboarding Phase

**1. Reference Generation by Concept**
Instead of you hunting Behance, ask Claude to surface specific references:

> *"I'm building a brand for [X]. Give me 10 highly specific cultural and design references I should look at — not generic movements, but specific designers, publications, eras, or artifacts that would be interesting starting points. Explain why each one."*

This gives you a curated hunting list rather than starting from scratch.

**2. Triangulation Questions**
Claude can interview you to narrow the territory through a series of forced choices — much faster than browsing:

> *"Ask me 10 rapid-fire either/or questions to help me identify the right aesthetic territory for this brand. Based on my answers, tell me what design world I'm actually describing."*

**3. Mood-to-Reference Translation**
If you have a feeling but no images:

> *"The feeling I want is [X]. Translate that into: 3 specific typefaces I should look at, 3 colour territory descriptions, 2 designers or studios whose work I should study, and 1 unexpected reference from outside design entirely."*

**4. Reference Sourcing Guidance**
Claude can tell you exactly where to look for specific things — which Are.na channels, which Behance searches, which designers' portfolios, which books or publications.

---

## The Bit Claude Can't Do Alone

Claude can't *browse* Are.na or Behance for you in real time, and it can't generate actual moodboard images. So the flow is:

```
Claude generates reference list
      ↓
You spend 20 mins collecting images
(Are.na, Behance, Google Images)
      ↓
You bring them back to Claude for parsing
      ↓
Claude extracts the design DNA
      ↓
Constraint brief → system generation
```

The collection step still requires you, but Claude can make it **targeted and fast** rather than open-ended browsing.

---

## The Most Powerful Opening Prompt

If you want to start right now, this single prompt does a lot of work:

> *"I'm creating a design system for [describe your project in 2–3 sentences]. I don't have references yet. First, ask me 5 questions to understand the brand territory. Then give me a specific reference hunting list — designers, publications, cultural artifacts, specific eras — that I should collect images from. Finally, suggest the 3 most interesting aesthetic directions this could go, and explain what makes each one distinct and unexpected."*


# Where to Store a Moodboard for AI Access

There's no great solution yet. The human ideal (a visual canvas where you can see everything at once, drag and drop, and annotate) and the AI ideal (structured text or image files it can read directly) are currently in tension.

## Option A: Simple AI-friendly approach

Create a directory in this repo (e.g. `my-moodboard/`) with one `.md` file per reference, following the archive format: URL, screenshot via screenshotit.app, short note on why it's there. Claude can read these files directly, see the screenshots as images, and parse design DNA across the whole set.

**Downside:** no visual canvas — you're editing markdown, not dragging images around.

## Option B: Excalidraw

Excalidraw gives you the human experience — visual canvas, drag and drop, annotations, everything visible at once. 

**Downside for AI:** Excalidraw stores as JSON; Claude can't extract visual gestalt from it. To use it with AI you'd paste or drag the images directly into the conversation.

**Obsidian + Excalidraw** partially bridges this: the plugin stores embedded images as PNGs in your vault's assets folder, so the image files exist and can be shared with Claude. Still requires a manual step to bring them into the conversation.

## Practical takeaway

Use whichever suits the moment. If you want AI to parse the moodboard, the simplest path is to paste 4–6 images directly into the conversation — no storage format required.


# Pairwise Picker Workflow

A faster alternative to manually browsing for moodboard references: pick between pairs of already-curated sites instead of open-ended searching.

1. `python3 scripts/collect_candidates.py archive report-inspirations > scratch/candidates.json`
   Pulls every site already curated in this repo into a flat candidate list.
2. `python3 scripts/build_picker.py scratch/candidates.json scratch/picker.html`
   Generates a static picker page.
3. `open scratch/picker.html` and click through pairs — as many rounds as it takes to feel converged (start with ~20-30).
4. Click "Export picks.json" and save it somewhere durable (not `scratch/`, which is gitignored).
5. Paste the winning screenshots (or the picks.json plus a request to fetch/describe them) into a Claude conversation and ask it to extract concrete shared traits — not adjectives, mechanics: type, colour behaviour, spacing, layout logic — into a moodboard constraint brief.
6. Use that brief as the actual design moodboard, following the directory format in `AGENTS.md`.

This reuses the curated candidate pool already built into `archive/` and `report-inspirations/` instead of scraping external galleries — v2 could add live scraping of Awwwards/One Page Love/Siteinspire if the existing pool proves too narrow.

