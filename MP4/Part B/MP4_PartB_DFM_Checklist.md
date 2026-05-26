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

Updated with Haben's linkage (L1=47, L2=20, L3=29, L4=23) and Architecture A (single spur pair, 20T × 20T at m=1.0).

| Part | Orientation | Why | Supports? |
|------|-------------|-----|-----------|
| Linkage links (ground L1=47mm, input L2=20mm, coupler L3=29mm, output L4=23mm) | Flat on bed | Layer lines perpendicular to pin bore axis → strongest in shear at the pivot joints; longest link (47 mm) fits any standard bed | No |
| Gear (20T, m=1.0, Ø20 pitch / Ø22 addendum) | Flat on bed, tooth profile facing up | Tooth profile fidelity — FDM prints involute curves best in the XY plane, with layers stacking along the face width axis | No |
| Jaw arm | Flat on bed (long axis along X) | Grip force acts along the arm — layer lines parallel to force direction gives best tensile strength | No (assuming symmetric cross-section) |
| Housing (each shell, if split clamshell) | Flat on bed, inner face up | Largest flat surface on bed for stability; snap-fit clips print upward for clean geometry | Yes — internal features (gear shaft bores, linkage pivot mounts) likely need support |
| Pins (Ø3.0 mm × ~8–10 mm) | Upright (axis perpendicular to bed) | Layers perpendicular to shear plane at the joint — strongest orientation for shear loading | No |
| Thumb wheel (Ø24–30 mm) | Flat on bed | Knurl pattern prints cleanly in XY; shaft bore centered | No |

**AI assist:** Centaur Loop 3 (DFM and pin clearance review) captured the key insight that pin clearance needed to increase from 0.20 mm to 0.40 mm diametral to survive FDM tolerance.

---

## 2. Wall Thickness and Feature Size

Minimum dimensions per part vs. FDM PLA capability. Standard FDM
nozzle: 0.4 mm; minimum feature: ~1 mm; minimum wall: 1.2 mm
(2 perimeters); minimum positive feature: ~0.8 mm.

Updated with Haben's linkage dimensions and Architecture A gear specs.

| Part | Thinnest wall (mm) | Smallest feature (mm) | Flagged? |
|------|---------------------|------------------------|----------|
| Linkage ground link (47 mm, cross-section TBD) | Target ≥ 3 mm for strength (longer span than David's 12 mm link) | Pin bore Ø3.0 | No (bore is printable) |
| Linkage coupler (29 mm) | Target ≥ 3 mm | Pin bore Ø3.0 | No — but longer span means more deflection risk under load |
| Linkage input/output (20 mm / 23 mm) | Target ≥ 3 mm | Pin bore Ø3.0 | No |
| Gear (20T, m=1.0) | Tooth root width ≈ 1.1 mm | Root fillet ~R0.50 mm | **Marginal** — root fillet near FDM minimum. Better than the 14T design (wider root at z=20). |
| Hub (OD Ø8.0, bore Ø3.40) | Wall = (8.0 − 3.40)/2 = 2.3 mm | Bore Ø3.40 | No |
| Housing | Target ≥ 1.5 mm walls | Shaft bore Ø3.40, snap-fit clips | **Yes** — snap-fit clips in PLA are brittle; recommend ≥ 2.0 mm clip thickness |
| Pins (Ø3.0 mm) | 3.0 mm diameter | Entire part is the feature | No |

**Notes:** The 20T gear at m = 1.0 has wider tooth roots than the original 14T design, reducing the printability risk at the root fillet. The snap-fit clips on the housing remain the highest-risk feature for PLA brittleness.

---

## 3. Pin and Joint Clearances

For each rotating joint:

Updated with team decision to increase bore diameter.

- **Pin OD (CAD nominal):** 3.00 mm
- **Hole ID (CAD nominal):** 3.40 mm *(increased from MP3's Ø3.20 to guarantee sliding fit)*
- **Designed clearance:** 0.40 mm diametral (0.20 mm radial)
- **Expected clearance after print** (typical FDM: holes print ~0.10 mm
  undersize, pins ~0.10 mm oversize; net effect ≈ −0.20 mm on the
  designed clearance): 0.40 − 0.20 = **0.20 mm** (good sliding fit)
- **Fit class:** Sliding fit — adequate clearance for rotation without excessive wobble
- **Accept?** **Yes** — 0.20 mm post-print clearance provides a reliable sliding fit for printed PLA. No reaming required.

> Same pin geometry applies to all 8 linkage pivots (4 per side) and
> the 2 gear shaft bores (one per gear, each in a housing mount point).
> Total rotating joints: 10.

---

## 4. Gear Printability

Updated with Architecture A gear specs (20T × 20T at m = 1.0).

| Check | Value | Notes |
|-------|-------|-------|
| Module (mm) | 1.0 | At the FDM minimum. Works but leaves no margin for extrusion width variation. m=1.5 is safer if packaging allows. |
| Smallest tooth feature (root width or fillet) | ~1.1 mm root width; ~R0.50 fillet | Improved over 14T design (wider roots at z = 20). Fillet printable with 0.4 mm nozzle. |
| Tooth count (each gear) | 20 / 20 (identical pair) | z = 20 is well above the z ≥ 12 FDM floor. Ø22 mm addendum circle — easily printable. |
| Face width (mm) | 8.0 | Adequate — ≥ 3 mm threshold met with margin. |
| Print orientation | Flat on bed (tooth profile in XY plane) | Strongly preferred for involute fidelity. |
| Backlash designed in (mm) | 0.10–0.15 mm | Slightly increased from MP3's 0.05–0.10 mm to account for FDM over-extrusion. Test print recommended. |

---

## 5. Overhangs and Bridges

Standard FDM PLA: overhangs to 45° usually clean; 60° often acceptable
with cooling; bridges up to ~10 mm typically fine.

| Feature | Angle / span | Concern? | Mitigation |
|---------|--------------|----------|------------|
| Gear tooth tips (involute profile) | Near-vertical walls on tooth flanks | Low — tooth height at m=1.0 is ~2.25 mm, well within overhang limits | None needed |
| Gear hub bore (Ø3.40 × 8.0 mm face width) | Circular bore, printed as bridging layers | Low — Ø3.40 is within bridging capability | Drill/ream post-print if needed |
| Housing top inner edge | Likely 45°–60° overhang depending on design | Moderate — large spans may sag | Add chamfer or fillet; use supports if span > 10 mm |
| Housing snap-fit clips | Cantilever with thin cross-section | **High** — PLA snap-fits are brittle and may crack | Print clips separately and glue, or design clip thickness ≥ 2 mm. Screw fasteners remain a fallback per trust assessment. |
| Linkage pin bores (Ø3.40 through links) | Circular bore through ≤ 5 mm thick walls | Low | None needed for short bores |

---

## 6. Assembly Sequence

Order of operations from raw printed parts to functional gripper.

1. Press pins into linkage links to form the four-bar on each side (4 pins per side, 8 total). Pin OD Ø3.0 into bore Ø3.40 → sliding fit, no tools required.
2. Install gear onto Side 1's linkage input crank shaft (Ø3.0 pin through Ø3.40 gear bore).
3. Install gear onto Side 2's linkage input crank shaft, meshing with Side 1's gear at 20 mm center distance.
4. Mount both linkage assemblies into housing (press gear/linkage shaft pins into housing bore mounts).
5. Attach jaw arms to coupler links (pin connection).
6. Close housing (snap-fit second shell over first).
7. Install thumb wheel onto Side 1's gear shaft (press fit or set screw).

**Accessibility check:** If housing is a clamshell split along the horizontal midplane, all internals (gears, linkage pivots, pins) are accessible before closing the second shell. The single spur pair (only 2 gears at 20 mm center distance) is significantly easier to assemble than the compound train (5 gears across 126 mm).

**Snap-fit engagement:** PLA snap-fit clips are brittle. Team decided to keep snap-fit per MP1 spec, but should design clips with ≥ 2 mm thickness and short deflection distances (< 1 mm). Add screw bosses to the housing as a fallback — if clips crack during first assembly, two M2 screws can hold the shells together.

---

## 7. Part Count

Target from the MP1 brief: **< 15 total parts**.

Updated with Architecture A (2 gears instead of 5) and Haben's linkage.

| Part | Count |
|------|-------|
| Linkage links (×4 per side × 2 sides) | 8 |
| Pins (4 per side × 2 sides + 2 gear shafts) | 10 |
| Gears (1 per side) | 2 |
| Jaw arms (1 per side) | 2 |
| Housing pieces (clamshell: 2) | 2 |
| Input wheel / knob | 1 |
| **Total** | **25** |

**Under target?** **No** — still over the 15-part target, but reduced from 29 (compound train) to 25 by eliminating 3 gears and 1 shaft. The main contributor is the 8 linkage links and 10 pins. Possible simplifications for MP5:
- Integrate the ground link into the housing shell (eliminates 2 links + 2 pins = −4 parts → 21)
- Use shaft-in-bore instead of separate pins where possible (eliminate 2–4 pins)
- Print jaw arms as part of the coupler link (eliminates 2 parts → saves 2 more)
- Aggressive integration could reach ~17 parts, approaching the target.

---

## 8. Print Time and Material Budget

Rough estimate from a slicer (PrusaSlicer, Bambu Studio, Cura) on the
team's chosen geometry. Don't sweat ±20% accuracy.

Estimates based on typical FDM PLA at 0.2 mm layer height, 20% infill.

- **Total print time (hours):** ~3–6 hours total across all prints (Architecture A is simpler than compound train)
- **Total material (grams or meters):** ~40–80 g PLA (reduced from compound train estimate due to fewer gears)
- **Print bed pieces (how many separate prints?):** 3 prints:
  1. All linkage links + pins (small parts, batch on one bed) — ~1 hour
  2. Both gears + jaw arms + thumb wheel — ~1 hour
  3. Housing shell 1 + housing shell 2 — ~2–4 hours (largest print)
- **Notes:** Housing is the largest print and the most likely to need supports. Gears and linkage links are small enough to batch efficiently. The reduced gear count (2 vs. 5) saves ~1 hour of print time compared to the compound train.

---

## DFM Summary

**Top 3 printability risks (in order):**
1. **Snap-fit housing clips** — PLA brittleness makes snap-fit clips the most likely point of failure during assembly. Mitigation: design thick clips (≥ 2 mm), add screw boss fallback.
2. **Gear tooth fidelity at m = 1.0** — root fillets (~R0.50) are near the FDM minimum feature size. A test print of one gear pair is recommended before committing to the full build. The 20T design is less risky than the original 14T design.
3. **Pin-bore fit consistency across 10 joints** — even with 0.40 mm designed clearance, FDM dimensional variability means some joints may be tighter or looser than others. A test print of one pin-in-bore joint validates the clearance design.

**AI assist:** DFM risks identified through Centaur Loops 3 and 4 (this Devin session). Key AI contributions: calculating post-FDM-tolerance clearances, flagging the compound train packaging problem that led to the Architecture A switch, and computing Lewis bending stress for the new 20T gear design.
