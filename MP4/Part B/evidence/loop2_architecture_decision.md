# Evidence — Loop 2: Drive Train Architecture Decision

**Date:** 2026-05-26
**Lead:** David Ricciotti
**AI tool:** Devin (Cognition AI) — session URL in PR description

## Prompt

> List all team decisions needed for Part B, including drive-train
> architecture options with pros and cons. We need to understand the
> trade-offs before committing.

## Context provided

- Haben's linkage: 100° sweep (−50° to +50°)
- MP1 brief: 2–3 thumb-wheel turns, 92 × 46 × 55 mm envelope
- David's MP3 gear specs: 14T at m = 1.0
- Existing compound train (Architecture B): center distances summing to 126 mm (exceeds 92 mm)

## AI output — Architecture comparison

| Architecture | N feasible | Center dist. | Parts | Printability |
|---|---|---|---|---|
| A — Single spur pair | N = 1 (0.28 turns) | 20 mm | 2 gears | Easy |
| B — Compound spur | N = 16 (1.24 turns) | 126 mm total | 5 gears | Packaging fails |
| C — Worm + wheel | High N | Compact | 2 parts | Hard (FDM worm) |
| D — Sync + separate | Flexible | Varies | 3+ parts | Medium |

Key insight: Haben's 100° sweep reduces N_needed from 32 (David's 28°) to 9,
making Architecture A viable despite only achieving N = 1.

## Team decision

- Chose Architecture A (single spur pair, 20T × 20T at m = 1.0)
- Accepted 0.28 turns (below 2–3 target) for simplicity
- Part count: 29 → 25; center distance: 126 mm → 20 mm
