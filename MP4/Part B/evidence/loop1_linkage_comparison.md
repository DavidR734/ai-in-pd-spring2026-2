# Evidence — Loop 1: Linkage Comparison and Selection

**Date:** 2026-05-26
**Lead:** David Ricciotti
**AI tool:** Devin (Cognition AI) — session URL in PR description

## Prompt

> Integrate Haben's Part A data into the Part B linkage comparison
> worksheet. Extract his design parameters, fill in his row in the
> comparison table, write the comparison notes, and generate
> side-by-side plots.

## Context provided

- Haben's completed notebook: `MP4_PartA_Build_to_Verify_completed.ipynb`
- David's Part A notebook (already in repo at `MP4/Part A/`)
- MP1 Part B design brief: ~25 mm grip-object size (no numeric jaw opening stated), 92 × 46 × 55 mm envelope; team adopted a self-imposed ≥40 mm jaw-opening target

## AI output (key extracted parameters)

| Parameter | David | Haben |
|-----------|-------|-------|
| L1 / L2 / L3 / L4 (mm) | 12 / 26 / 12 / 26 | 47 / 20 / 29 / 23 |
| Output pivot offset | (0, 12) | (47, 0) |
| Single-side displacement | 12.5 mm | 20.06 mm |
| Total jaw opening | 25.0 mm | 40.13 mm |
| Transmission angle band | 62°–90° | 61.3°–91.3° |
| Input range | 0°–28° | −50° to +50° |

## Generated artifacts

- `plots/displacement_comparison.png` — both curves on one chart with 20 mm target line
- `plots/mu_comparison.png` — both curves with 40°–140° workable band shaded

## Team decision

Selected Haben's linkage: only candidate meeting the team's self-imposed 40 mm jaw-opening target, comparable μ margin, wider sweep.
