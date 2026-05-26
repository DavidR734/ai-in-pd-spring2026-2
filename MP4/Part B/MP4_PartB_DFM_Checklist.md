# MP4 Part B — DFM Checklist

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion

> If your team's chosen linkage geometry exists only as plots and not in
> CAD yet, prioritize bringing it (and the drive train) into a CAD tool
> of any team member's choice — SolidWorks, Fusion, Onshape, Blender,
> FreeCAD. A design that exists only in plot or sketch form will not
> survive Jordan's prototype review. He needs printable geometry.

This is the application checklist. Use your AI stack to walk it part by
part; commit your filled-in version as
`MP4/Part B/dfm_checklist_completed.md`. You can edit this file in place
or copy it to that name — either is fine, as long as the completed
version is in the repo.

The team is not expected to do a full formal DFM pass. The goal is to
identify the printability risks the team would actually flag at a print
queue review, and to document who looked at what.

---

## 1. Print Orientation

For each major part, name the orientation, why, and whether supports
are needed.

_[Pre-filled with David's linkage and gear data. Team: update once housing and jaw arm designs exist.]_

| Part | Orientation | Why | Supports? |
|------|-------------|-----|-----------|
| Linkage links (ground, input, coupler, output — 26 mm cranks, 12 mm ground/coupler) | Flat on bed | Layer lines perpendicular to pin bore axis → strongest in shear at the pivot joints; 26 mm length fits any bed | No |
| Gear 1 (14T pinion, m=1.0) | Flat on bed, tooth profile facing up | Tooth profile fidelity — FDM prints involute curves best in the XY plane, with layers stacking along the face width axis | No |
| Gear 2 (56T driven, m=1.0) | Flat on bed | Same reason; 56 mm OD fits standard print bed | No |
| Jaw arm | _[needs jaw arm design — likely flat for strength along grip axis]_ | _[to be determined by team]_ | _[likely no if symmetric cross-section]_ |
| Housing (each shell, if split) | _[needs housing design — likely split horizontal, each half flat on bed]_ | _[to be determined by team]_ | _[likely yes for internal features — gear shaft bores, snap-fit clips]_ |
| Pins (Ø3 mm × ~8–10 mm) | Upright (axis perpendicular to bed) | Layer lines along pin axis = weakest direction for shear; upright orients layers perpendicular to shear plane | No |

**AI assist:** _[team: cite which centaur loop captured the most useful DFM insight here]_

---

## 2. Wall Thickness and Feature Size

Minimum dimensions per part vs. FDM PLA capability. Standard FDM
nozzle: 0.4 mm; minimum feature: ~1 mm; minimum wall: 1.2 mm
(2 perimeters); minimum positive feature: ~0.8 mm.

_[Pre-filled with David's known dimensions. Team: update once CAD exists for all parts.]_

| Part | Thinnest wall (mm) | Smallest feature (mm) | Flagged? |
|------|---------------------|------------------------|----------|
| Linkage cranks (26 mm, cross-section TBD) | _[needs CAD — target ≥ 3 mm for strength]_ | Pin bore Ø3.0 | No (bore is printable) |
| Pinion (14T, m=1.0) | Tooth root width ≈ 1.0 mm (root fillet R0.60 from MP3) | Root fillet R0.60 mm | **Yes** — root fillet is at the FDM minimum; may need m=1.5 if teeth break |
| Driven gear (56T, m=1.0) | Tooth root width ≈ 1.2 mm | Root fillet ~R0.40 mm | Marginal — root fillet below 0.5 mm is hard to resolve |
| Hub (OD Ø8.0, bore Ø3.0) | Wall = (8.0 − 3.0)/2 = 2.5 mm | Bore Ø3.0 | No |
| Housing | _[needs CAD — target ≥ 1.5 mm walls]_ | _[shaft bore Ø3.0, snap-fit clips]_ | _[likely yes for snap-fit clips — PLA is brittle]_ |
| Pins (Ø3.0 mm) | 3.0 mm diameter | Entire part is the feature | No |

**Notes:** The 14T pinion root fillet (R0.60) and driven gear root fillet are the riskiest features. At m=1.0, tooth roots approach the FDM minimum feature size. If teeth break during testing, the team should consider bumping to m=1.5 (which would increase all gear diameters by 50% and the packaging challenge with them).

---

## 3. Pin and Joint Clearances

For each rotating joint:

_[Pre-filled from David's MP1 and MP3 pin specs.]_

- **Pin OD (CAD nominal):** 3.00 mm
- **Hole ID (CAD nominal):** 3.20 mm _(Ø3.00 +0.20/−0.00 from MP3)_
- **Designed clearance:** 0.20 mm diametral (0.10 mm radial)
- **Expected clearance after print** (typical FDM: holes print ~0.10 mm
  undersize, pins ~0.10 mm oversize; net effect ≈ −0.20 mm on the
  designed clearance): 0.20 − 0.20 = **0.00 mm** (borderline)
- **Fit class:** Borderline sliding / interference
- **Accept?** **No** — designed clearance should be increased to ≥ 0.30 mm diametral (hole = Ø3.30 or Ø3.40) to guarantee a sliding fit after FDM tolerance. Alternatively, ream the bore post-print with a 3.0 mm drill bit.

> Same pin geometry applies to all 8 linkage pivots (4 per side) and
> the 3–4 gear shaft bores. _[Team: decide whether to increase bore
> tolerance or plan for post-processing.]_

---

## 4. Gear Printability

_[Pre-filled from David's MP3 gear specs.]_

| Check | Value | Notes |
|-------|-------|-------|
| Module (mm) | 1.0 | At the FDM minimum. Works but leaves no margin for extrusion width variation. m=1.5 is safer if packaging allows. |
| Smallest tooth feature (root width or fillet) | ~1.0 mm root width; R0.60 fillet | The R0.60 fillet is at the edge of what 0.4 mm nozzle can resolve. |
| Tooth count (each gear) | 14 / 56 (both stages) | z=14 is above the z≥12 FDM floor. 56T gives Ø56 mm — printable. |
| Face width (mm) | 8.0 | Adequate — ≥3 mm threshold met with margin. |
| Print orientation | Flat on bed (tooth profile in XY plane) | Strongly preferred for involute fidelity. |
| Backlash designed in (mm) | 0.05–0.10 mm (from MP3) | May need to increase to 0.15–0.20 mm for FDM over-extrusion. Test print recommended. |

---

## 5. Overhangs and Bridges

Standard FDM PLA: overhangs to 45° usually clean; 60° often acceptable
with cooling; bridges up to ~10 mm typically fine.

_[Pre-filled for known features. Team: update once housing design exists.]_

| Feature | Angle / span | Concern? | Mitigation |
|---------|--------------|----------|------------|
| Gear tooth tips (involute profile) | Near-vertical walls on tooth flanks | Low — tooth height at m=1.0 is ~2.25 mm, well within overhang limits | None needed |
| Gear hub bore (Ø3.0 × 8.0 mm face width) | Circular bore, printed as bridging layers | Low — Ø3.0 is within bridging capability | Drill/ream post-print if needed |
| Housing top inner edge | _[needs housing design — likely 45°–60° overhang]_ | _[likely moderate]_ | _[support or chamfer — team decision]_ |
| Housing snap-fit clips | _[needs housing design]_ | _[high — PLA snap-fits are brittle]_ | _[consider screw fasteners instead]_ |

---

## 6. Assembly Sequence

Order of operations from raw printed parts to functional gripper.

_[Preliminary sequence — team needs to finalize once all parts are designed.]_

1. Press pins into linkage links to form the four-bar on each side (4 pins per side, 8 total)
2. Install Stage 1 pinion on thumb-wheel shaft; install Stage 1 driven gear (56T) on intermediate shaft
3. Install Stage 2 pinion on intermediate shaft; install Stage 2 driven gear (56T) on linkage input shaft
4. Install sync gear (56T) on opposite-side linkage input shaft, meshing with Stage 2 driven gear
5. Mount gear train assembly into housing (press shafts into housing bores)
6. Attach linkage assemblies to input cranks on both sides
7. Attach jaw arms to coupler links
8. Close housing (snap-fit or screw second shell)
9. Install thumb wheel on Stage 1 pinion shaft

**Accessibility check:** can each fastener / pin be reached during
assembly without disassembling the part you just installed? _[Unknown — needs housing design. If housing is a clamshell split, all internals are accessible before closing. If monolithic, gear shafts must slide in from one end.]_

**Snap-fit engagement:** if the design uses snap fits, has the team
reviewed the deflection geometry against PLA brittleness? _[No — MP1 spec assumes snap-fit housing closure, but PLA snap-fits are known to be brittle. Team should consider M2 or M3 screws as an alternative.]_

---

## 7. Part Count

Target from the MP1 brief: **< 15 total parts**.

_[Pre-filled with estimated counts from David's design. Team: adjust once all parts are finalized.]_

| Part | Count |
|------|-------|
| Linkage links (×4 per side × 2 sides) | 8 |
| Pins (4 per side × 2 sides + gear shafts) | 11 _[8 linkage + 3 gear shafts]_ |
| Gears (2 stages × 2 gears + 1 sync gear) | 5 |
| Jaw arms (1 per side) | 2 |
| Housing pieces (clamshell: 2) | 2 |
| Input wheel / knob | 1 |
| **Total** | **29** |

**Under target?** **No** — significantly over the 15-part target. The main contributors are the 8 linkage links and 11 pins. Possible simplifications for MP5:
- Integrate link pairs (e.g., print ground link + housing as one piece) to reduce link count
- Use living hinges instead of separate pins (risky with PLA)
- Combine the two gear stages into a compound gear (pinion + driven on same shaft = 1 less gear)
- _[Team: discuss which merges are feasible]_

---

## 8. Print Time and Material Budget

Rough estimate from a slicer (PrusaSlicer, Bambu Studio, Cura) on the
team's chosen geometry. Don't sweat ±20% accuracy.

_[Rough estimates — no slicer run yet because full CAD does not exist. Team: run actual slicer estimate once CAD is complete.]_

- **Total print time (hours):** _[estimate 4–8 hours total across all prints, depending on infill and support settings]_
- **Total material (grams or meters):** _[estimate 50–100 g PLA based on housing volume + linkage + gears]_
- **Print bed pieces (how many separate prints?):** _[estimate 3–4 prints: (1) all gears + pins, (2) linkage links, (3) housing shell 1, (4) housing shell 2 + jaw arms + thumb wheel]_
- **Notes:** _[housing is the largest print; gears and linkage links are small and can be batched on one bed]_

---

## DFM Pass Bottom Line

_[Draft — requires team review:]_

> We would **not** send this to the print queue tomorrow. The three flags we'd most want to address first: (1) **Pin clearance** — the designed 0.20 mm diametral clearance nets to 0.00 mm after FDM tolerance, meaning pins will likely not fit without post-processing. Increase bore to Ø3.30–3.40 mm. (2) **Gear tooth fidelity at m=1.0** — root fillets (R0.60) are at the FDM resolution floor. A test print of one gear pair before committing to the full build is essential. (3) **Part count (29)** is nearly double the 15-part target. The team needs to identify which parts can be merged before printing.

---

## AI Use During the DFM Pass

Document briefly which centaur loops in
`MP4_PartB_Team_Centaur_Log_Template.md` produced DFM findings, and
which AI suggestions the team rejected (and why).

> _[Team: fill in after completing the centaur loops. Reference the specific loop numbers that informed DFM decisions.]_
