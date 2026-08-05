# Moodboards Howto with AI

> And how I can have AI help with first part [of the design process] ie the mood boarding to have those examples to work from -- or do I have to do that myself.

Great question — and honestly this is where AI can add a lot of value that most people don't use it for.

You don't have to do the moodboard gathering yourself. AI can act as a **creative director** in the early stage, helping you *discover and articulate* the right references before you've even seen them.

---

## What AI Can Do in the Moodboarding Phase

### 1. Reference Generation by Concept

Instead of you hunting Behance, ask AI to surface specific references:

> *"I'm building a brand for [X]. Give me 10 highly specific cultural and design references I should look at — not generic movements, but specific designers, publications, eras, or artifacts that would be interesting starting points. Explain why each one."*

This gives you a curated hunting list rather than starting from scratch.

### 2. Triangulation Questions

AI can interview you to narrow the territory through a series of forced choices — much faster than browsing:

> *"Ask me 10 rapid-fire either/or questions to help me identify the right aesthetic territory for this brand. Based on my answers, tell me what design world I'm actually describing."*

### 3. Mood-to-Reference Translation

If you have a feeling but no images:

> *"The feeling I want is [X]. Translate that into: 3 specific typefaces I should look at, 3 colour territory descriptions, 2 designers or studios whose work I should study, and 1 unexpected reference from outside design entirely."*

### 4. Reference Sourcing Guidance

AI can tell you exactly where to look for specific things — which Are.na channels, which Behance searches, which designers' portfolios, which books or publications.

---

## The Bit AI Can't Do Alone

AI can't *browse* Are.na or Behance for you in real time, and it can't generate actual moodboard images. So the flow is:

```
AI generates reference list
      ↓
You spend 20 mins collecting images
(Are.na, Behance, Google Images)
      ↓
You bring them back to AI for parsing
      ↓
AI extracts the design DNA
      ↓
Constraint brief → system generation
```

The collection step still requires you, but AI can make it **targeted and fast** rather than open-ended browsing.

---

## The Most Powerful Opening Prompt

If you want to start right now, this single prompt does a lot of work:

> *"I'm creating a design system for [describe your project in 2–3 sentences]. I don't have references yet. First, ask me 5 questions to understand the brand territory. Then give me a specific reference hunting list — designers, publications, cultural artifacts, specific eras — that I should collect images from. Finally, suggest the 3 most interesting aesthetic directions this could go, and explain what makes each one distinct and unexpected."*


# Where to Store a Moodboard for AI Access

There's no great solution yet. The human ideal (a visual canvas where you can see everything at once, drag and drop, and annotate) and the AI ideal (structured text or image files it can read directly) are currently in tension.

## Option A: Simple AI-friendly approach

Create a directory in this repo (e.g. `my-moodboard/`) with one `.md` file per reference, following the archive format: URL, screenshot via screenshotit.app, short note on why it's there. AI can read these files directly, see the screenshots as images, and parse design DNA across the whole set.

**Downside:** no visual canvas — you're editing markdown, not dragging images around.

## Option B: Excalidraw

Excalidraw gives you the human experience — visual canvas, drag and drop, annotations, everything visible at once. 

**Downside for AI:** Excalidraw stores as JSON; AI can't extract visual gestalt from it. To use it with AI you'd paste or drag the images directly into the conversation.

**Obsidian + Excalidraw** partially bridges this: the plugin stores embedded images as PNGs in your vault's assets folder, so the image files exist and can be shared with AI. Still requires a manual step to bring them into the conversation.

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
5. Paste the winning screenshots (or the picks.json plus a request to fetch/describe them) into a AI conversation and ask it to extract concrete shared traits — not adjectives, mechanics: type, colour behaviour, spacing, layout logic — into a moodboard constraint brief.
6. Use that brief as the actual design moodboard, following the directory format in `AGENTS.md`.

This reuses the curated candidate pool already built into `archive/` and `report-inspirations/` instead of scraping external galleries — v2 could add live scraping of Awwwards/One Page Love/Siteinspire if the existing pool proves too narrow.

