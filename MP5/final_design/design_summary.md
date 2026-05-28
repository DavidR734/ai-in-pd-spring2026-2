# MiniClaw Final Design Summary

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion
**Date:** 2026-05-26

---

## Design Overview

The MiniClaw is a hand-driven mechanical gripper designed to compete with Hiwonder's BigClaw at RobotExpo 2026. It uses a mirrored four-bar linkage mechanism driven by a thumb wheel through a single spur gear pair.

### Key Specifications

| Parameter | MP1 Target | Final Design | Status |
|---|---|---|---|
| Envelope | 92 × 46 × 55 mm | 92 × 46 × 55 mm | Met |
| Jaw opening | ≥ 40 mm | 40.13 mm | Met |
| Thumb-wheel turns | 2–3 | 0.28 | Renegotiated |
| Grip force | 5–8 N | Analytically feasible | Untested |
| Material | FDM PLA | FDM PLA (FilaTech PolyPro) | Met |
| Part count | < 15 | 25 | Over target |
| Cost per unit | < $3 at 500 units | ~$2–3 estimated | Estimated |

---

## Linkage Design

**Selected:** Haben Berhe's crossed-branch four-bar

| Link | Length (mm) | Function |
|---|---|---|
| L1 (ground) | 47 | Fixed frame |
| L2 (input crank) | 20 | Driven by gear shaft |
| L3 (coupler) | 29 | Connects input to output |
| L4 (output) | 23 | Drives jaw arm |

- **Output pivot offset:** O4 = (47, 0) mm from O2
- **Input range:** −50° to +50° (100° sweep)
- **Single-side displacement:** 20.06 mm → 40.13 mm total jaw opening
- **Transmission angle:** 61.3° to 91.3° (21.3° margin above 40° floor)
- **Tip extension:** 9 mm past joint B along coupler direction

---

## Drive Train

**Architecture:** A — Single Spur Pair (mating final pair for counter-rotation)

| Parameter | Value |
|---|---|
| Gear type | Spur, involute 20° pressure angle |
| Tooth count (each) | 20 |
| Module | 1.0 mm |
| Pitch diameter (each) | 20 mm |
| Addendum diameter (each) | 22 mm |
| Center distance | 20 mm |
| Face width | 8 mm |
| Bore diameter | Ø3.40 mm |
| Overall reduction N | 1 |
| Thumb-wheel turns (open→closed) | 0.28 |

**Lewis bending stress:**
- Nominal torque (0.3 N·m): σ = 11.7 MPa, SF = 2.14
- Max hand torque (0.5 N·m): σ = 19.5 MPa, SF = 1.28

---

## Parts List

| # | Part | Qty | Material | Notes |
|---|---|---|---|---|
| 1 | Housing shell (left) | 1 | PLA | Snap-fit closure |
| 2 | Housing shell (right) | 1 | PLA | Snap-fit closure |
| 3 | Ground link (L1) | 2 | PLA | Integral with housing or separate |
| 4 | Input crank (L2) | 2 | PLA | Ø3.40 bore at each pivot |
| 5 | Coupler (L3) | 2 | PLA | Ø3.40 bore at each pivot |
| 6 | Output link (L4) | 2 | PLA | Ø3.40 bore at each pivot |
| 7 | Jaw arm (left) | 1 | PLA | 9 mm tip extension |
| 8 | Jaw arm (right) | 1 | PLA | 9 mm tip extension |
| 9 | Spur gear (Side 1) | 1 | PLA | 20T, m=1.0, flat print |
| 10 | Spur gear (Side 2) | 1 | PLA | 20T, m=1.0, flat print |
| 11 | Thumb wheel | 1 | PLA | 12–15 mm radius |
| 12 | Pivot pins | 8 | PLA or metal | Ø3.0 mm × variable length |
| 13 | Gear shaft pins | 2 | PLA or metal | Ø3.0 mm |
| | | **25 total** | | |

---

## Assembly Notes

1. **Print orientation:** Gears flat on bed (involute profile in XY plane). Links flat. Housing shells on their flat face.
2. **Pin insertion:** Ø3.0 mm pins into Ø3.40 mm bores — designed 0.40 mm clearance, 0.20 mm post-FDM sliding fit. No reaming required.
3. **Gear meshing:** 20 mm center distance between gear shafts. Designed backlash 0.10–0.15 mm. Test mesh quality before full assembly.
4. **Housing closure:** Snap-fit clips. PLA is brittle — assemble gently. Consider screw boss fallback if clips crack.
5. **Jaw alignment:** Critical per BigClaw lessons — 0.5 mm misalignment between left and right jaws causes uneven gripping. Align before final closure.

---

## Annotated Drawings

- Drive train layout: [`MP4/Part B/sketches/drive_train.png`](../../MP4/Part%20B/sketches/drive_train.png)
- Displacement comparison: [`MP4/Part B/plots/displacement_comparison.png`](../../MP4/Part%20B/plots/displacement_comparison.png)
- Transmission angle comparison: [`MP4/Part B/plots/mu_comparison.png`](../../MP4/Part%20B/plots/mu_comparison.png)
