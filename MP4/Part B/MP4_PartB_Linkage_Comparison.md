# MP4 Part B — Linkage Comparison Worksheet

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion

This is your day-one integration artifact. Each member arrives with a
four-bar linkage from Part A — same one-side problem, same BigClaw
reference, different design choices. Compare the candidates on the same
axes and pick (or merge) one. The team's first activity is concrete: this
worksheet.

> The plots come from combining your Part A data — they are not new
> analysis. Reuse each member's `compute_finger_position()` and
> `compute_transmission_angle()` outputs.

---

## Candidate Linkages

One row per team member. Pull the numbers from each member's Part A
Section 1 design summary and Section 7 trust ledger.

| Member | L1 / L2 / L3 / L4 (mm) | Output pivot offset (mm) | Single-side displacement (mm) | Implied total jaw opening (2× displacement, mm) | Min / max transmission angle | Part A trust ledger highlight |
|--------|-------------------------|---------------------------|-------------------------------|-------------------------------------------------|------------------------------|--------------------------------|
| David Ricciotti | 12 / 26 / 12 / 26 | (0, 12) | 12.5 | 25.0 | 62° / 90° | In band the whole time (22° margin above 40° floor). Symmetry assumption and gear-ratio-to-input-range mapping flagged as unverified. PLA pin wear at pivot joints (100+ cycle question from MP1). |
| Haben Berhe | 47 / 20 / 29 / 23 | (47, 0) | 20.06 | 40.13 | 61.3° / 91.3° | In band the whole time (21.3° margin above 40° floor). Symmetry assumption unverified — counter-rotation depends on gear pair. Housing clearance near joint B and coupler path not yet checked. Pin tolerance and friction assumed ideal. |
| Yoel Tesfatsion | _[needs Yoel's Part A data]_ | _[needs data]_ | _[needs data]_ | _[needs data]_ | _[needs data]_ | _[needs Yoel's trust ledger highlight]_ |

---

## Side-by-Side Plots

Embed (or link to) two combined plots showing all candidate linkages on
the same axes:

1. **Single-side finger displacement vs. input angle** — all candidates
   on one chart, with a horizontal reference line at the displacement
   that produces the target total jaw opening.
2. **Transmission angle vs. input angle** — all candidates on one chart,
   with the 40°–140° workable band shaded.

_[Plots to be generated once all three members' Part A data is available. Use the Python script below to combine.]_

> A short Python script that reads each member's geometry and replots is
> the typical way to do this. The matplotlib animation starter from Part
> A has the kinematics — adapt it.

```python
# Template script — fill in each member's parameters once available
import numpy as np
import matplotlib.pyplot as plt

# David's design
david = {'L1': 12, 'L2': 26, 'L3': 12, 'L4': 26,
         'O4': (0, 12), 'tip_ext': 22, 'theta_range': (0, 28),
         'label': 'David'}

# Haben's design
haben = {'L1': 47, 'L2': 20, 'L3': 29, 'L4': 23,
         'O4': (47, 0), 'tip_ext': 9, 'theta_range': (-50, 50),
         'label': 'Haben'}

# Yoel's design — fill from Part A
# yoel = {'L1': ?, 'L2': ?, 'L3': ?, 'L4': ?,
#         'O4': (?, ?), 'tip_ext': ?, 'theta_range': (?, ?),
#         'label': 'Yoel'}

# Use compute_finger_position() and compute_transmission_angle()
# from Part A to sweep each design and overlay on shared axes.
```

---

## Comparison Notes

For each candidate, 2–3 sentence assessment:

- **Linkage David Ricciotti:** Parallelogram (L1=L3=12, L2=L4=26) with vertical ground link gives pure translational jaw motion and a generous 22° margin above the 40° transmission angle floor. Envelope fit is comfortable (26 mm horizontal, 46.2 mm vertical vs. 46 × 55 mm budget). Unverified: symmetry under the mirrored gear pair, PLA link deflection under 5–8 N grip load.
- **Linkage Haben Berhe:** Crossed-branch four-bar (L1=47, L2=20, L3=29, L4=23) with horizontal ground link and 100° sweep (−50° to +50°) — reaches 20.06 mm single-side displacement, meeting the 40 mm total jaw opening target exactly. Transmission angle (61.3°–91.3°) stays in band with 21.3° margin. Larger footprint than David's design (47 mm ground link vs. 12 mm), which may be tighter in the housing envelope. Unverified: housing clearance near joint B, printed pin tolerance and friction.
- **Linkage Yoel Tesfatsion:** _[needs Yoel's Part A data and assessment]_

---

## The Team's Selection

_[Requires team discussion after comparing all three linkages]_

**Chosen linkage:** _[to be decided by team]_

**Why this one (2–4 sentences of engineering reasoning):**

> _[to be filled after team comparison of displacement curves, transmission angle margins, and envelope fits]_

**What got carried over from the others (if anything):**

- _[to be filled by team]_
- _[to be filled by team]_

**What got cut and why (be explicit):**

- _[to be filled by team]_
- _[to be filled by team]_

---

## Inputs to the Drive-Train Worksheet

Carry these forward into `MP4_PartB_Gear_Pair_Design.md`:

_[Values below assume David's linkage is selected — update if the team picks a different linkage]_

- **Chosen linkage's input angle range:** from 0° to 28°
- **Chosen linkage's transmission angle band across that range:** 62° to 90°
- **Implied input angle range tolerance** — how much can the
  drive-train reduction N shift this range before the transmission
  angle leaves the workable band? 22° _(μ_min = 62° at θ = 28°; the 40° floor is hit at θ = 50°, so the range could expand by up to 22° before leaving the band)_

> This last number is the coupling between Layer 1 (drive train) and
> Layer 2 (linkage). The drive-train design has to respect it.
