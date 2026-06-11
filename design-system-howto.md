# Design System Howto

How to create a design system.

## What to Prepare Before You Start

Think of it as three layers of input, from abstract to concrete:

### 1. Brand Foundation (most important first step)

This is the "why" and "what" behind the design. You don't need a polished document, but Claude works much better with:

- **Brand narrative** — what the brand is, who it's for, the feeling it should evoke
- **Tone & personality** — e.g. "trustworthy but playful", "brutally minimal", "premium and refined"
- **Audience** — who will use this, their expectations and context

### 2. Design Brief / Direction

Once you have the brand foundation, a brief helps Claude commit to a specific aesthetic instead of defaulting to generic choices. It should include:

- What you're building (web app, marketing site, mobile app, etc.)
- Any existing brand assets (logo, colors, fonts) — or a blank slate
- Reference examples ("something like Linear but warmer")
- Technical constraints (React, plain HTML/CSS, Tailwind, etc.)

### 3. Scope Definition**

Decide what the design system actually needs to contain:

- Tokens only (colors, spacing, typography)?
- Component library (buttons, inputs, cards)?
- Full documentation / Storybook-style?

---

## How AI Can Help at Each Stage

| Stage | What to ask Claude |
|---|---|
| Brand narrative | "Help me write a brand narrative for [X]" |
| Design language | "Based on this narrative, define a visual direction — tone, color mood, typography personality" |
| Token generation | "Create a full CSS/JS token set: colors, spacing scale, type scale, radius, shadows" |
| Component design | "Build a [button/card/input] component that matches this design language" |
| Design system doc | "Create a design system reference page with all tokens and components" |

---

## Recommended Workflow

```
Brand Narrative → Design Brief → Visual Direction
       ↓
  Token System (colors, type, spacing)
       ↓
  Core Components (buttons, forms, layout)
       ↓
  Patterns & Compositions
       ↓
  Documentation
```

**The key insight:** Claude produces far better results when you feed it a strong brand narrative and aesthetic direction upfront. Without it, you'll get competent but generic output. With it, you get something that feels genuinely designed.

---

## Practical Tips for Working with AI on This

- **Be specific about the *feeling***, not just the specs — "warm, editorial, slightly retro" beats "blue primary color"
- **Iterate in layers** — start with tokens, validate them visually, then move to components
- **Use artifacts** — Claude can output a living HTML/React design system reference you can keep iterating on in the same conversation
- **Paste in references** — if you have screenshots or URLs of things you like, describe them

