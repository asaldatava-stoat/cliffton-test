# Psych Tests

**Live:** https://asaldatava-stoat.github.io/cliffton-test/

Self-hosted, unofficial reconstructions of personality assessments — each a single self-contained HTML file, bilingual EN/RU, results stored only in your browser, JSON export for analysis with Claude.

| Test | Folder | Based on |
|---|---|---|
| Strengths Profiler | [`clifton/`](clifton/) | CliftonStrengths mechanics — 177 paired statements, 20 s timer, 34 themes / 4 domains |
| Enneagram Profiler | [`enneagram/`](enneagram/) | RHETI mechanics — 144 balanced pairs, 9 types, +18 instinct pairs, wing / tritype / arrows |

The root `index.html` is the landing page. Each test has its own README with mechanics and scoring details.

Not affiliated with Gallup or the Enneagram Institute; all statements are original text.

## Local

```bash
python3 -m http.server 8517
```

then open http://localhost:8517.
