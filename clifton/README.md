# Strengths Profiler

**Live:** https://asaldatava-stoat.github.io/cliffton-test/

An unofficial, self-hosted reconstruction of the **CliftonStrengths** assessment mechanics. Not affiliated with Gallup; all 177 statements are original text keyed to the publicly documented 34 talent themes.

## What it replicates

- **177 paired statements** — two self-descriptors per screen, choose which describes you better on a 5-point scale (Strongly / Describes me / Neutral / Describes me / Strongly)
- **20-second timer per item** — expires → item skipped, test moves on (toggleable "practice mode" without timer)
- **No going back** — answered or expired items are locked
- **Ranked output of all 34 themes** across the four domains (Executing, Influencing, Relationship Building, Strategic Thinking), with the Top 5 "signature themes" interpreted in detail (description, blind spots, actions)

## Mechanics

- Statement pairs are generated with a **fixed-seed PRNG**, so every attempt uses identical pairs — retakes are directly comparable. Only presentation order shuffles.
- Each theme appears 10–11 times; scoring is ipsative: the chosen side's theme earns 2 (strong) or 1 (moderate) points, normalized by that theme's answered appearances.
- Progress autosaves to `localStorage`; interrupted attempts resume. Full attempt history is kept, and each retake shows rank deltas (▲/▼) versus the previous attempt.
- **Copy results for analysis** exports a JSON summary (ranking, percentages, strong-pick counts, previous top 10) to paste into Claude or any tool for deeper interpretation.

## Languages

Fully bilingual **English / Russian** — the RU/EN button in the top-right corner switches everything: UI, all 177 statements, and the 34 theme interpretations. The choice persists between visits, and you can switch mid-test (answers are stored against pair indices, not text, so results are identical either way).

## Usage

Open `index.html` in a browser — it's a single self-contained file, no build, no dependencies. For localStorage persistence across sessions, serve it from a stable origin, e.g.:

```bash
python3 -m http.server 8517
```

then open http://localhost:8517.
