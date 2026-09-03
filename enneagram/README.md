# Enneagram Profiler

An unofficial, self-hosted reconstruction of the **RHETI-style** Enneagram assessment. Not affiliated with the Enneagram Institute; all 144 + 18 statements are original text keyed to the publicly documented nine types and three instinctual variants.

## What it replicates

- **144 paired statements** — two self-descriptors per screen, choose which describes you better on a 5-point scale (Strongly / Describes me / Neutral / Describes me / Strongly)
- **Perfectly balanced matrix** — every one of the 36 type pairs meets exactly 4 times; each type appears 32 times; each of its 16 statements is used exactly twice; no statement pair repeats
- **+18 pairs for the instinctual variant** (self-preservation / social / one-to-one) in a short second part
- **No going back** — answered items lock; no timer (the original has none)
- **Report**: ranked scores for all 9 types with an enneagram diagram (dot size = score, stress/growth arrows and wing highlighted), core type in detail (fear, desire, blind spot, actions), **wing** (e.g. 4w5, with Riso-Hudson wing label), **tritype** (lead type in each center), centers distribution, **instinct stack** (e.g. sx/sp), an auto-composed closing summary, and rank deltas vs. the previous attempt

## Mechanics

- Pairs are generated with a **fixed-seed PRNG** (`mulberry32(20260903)` for types, `20260904` for instincts), so every attempt uses identical pairs — retakes are directly comparable. Only presentation order shuffles.
- Scoring is ipsative: the chosen side's type earns 2 (strong) or 1 (moderate) points, normalized by that type's answered appearances.
- Wing = the higher-scoring neighbour of the lead type (within 0.5 pts → "balanced"). Tritype = highest type in each of Body (8-9-1), Heart (2-3-4), Head (5-6-7). Arrows follow the standard lines: stress 1→4→2→8→5→7→1, 9→6→3→9; growth the reverse.
- Progress autosaves to `localStorage`; interrupted attempts resume. Full attempt history is kept.
- **Copy results for analysis** exports a JSON summary (type, wing, tritype, instinct stack, centers, full ranking, closing summary, previous top 3) to paste into Claude or any tool.

## Languages

Fully bilingual **English / Russian** — the RU/EN button switches UI, all statements and all interpretations. The choice persists; switching mid-test is safe (answers are stored against pair indices, not text).

## Usage

Open `index.html` in a browser — a single self-contained file, no build, no dependencies. For localStorage persistence serve it from a stable origin, e.g.:

```bash
python3 -m http.server 8519
```

then open http://localhost:8519.
