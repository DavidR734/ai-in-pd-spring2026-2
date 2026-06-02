# MP5 — Final Trust Ledger

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion
**Base document:** MP4 Part B Per-Subsystem Trust Assessment (`MP4/Part B/MP4_PartB_Trust_Assessment_Template.md`)
**Updated:** 2026-05-26 (post-Part B, entering MP5)

---

## Summary of Changes from MP4 Part B

The trust assessment below is carried forward from MP4 Part B with MP5-specific annotations marked **[MP5 UPDATE]**. No subsystem flags changed — the three Unknown subsystems remain Unknown because no CAD was created during MP5 prep.

---

## Subsystem 1: Four-Bar Linkage — **Needs work**

**What's verified:**
- Transmission angle: 61.3°–91.3° across −50° to +50° sweep (21.3° margin above 40° floor)
- Single-side displacement: 20.06 mm → 40.13 mm total jaw opening (meets the team's self-imposed 40 mm target; the MP1 brief specifies only a ~25 mm grip-object size)
- No interference across full sweep
- N = 1 coupling check: Part A range = operating range (no mismatch)
- **[MP5 UPDATE]** Comparison plots (`plots/displacement_comparison.png`, `plots/mu_comparison.png`) confirm David's and Haben's designs on same axes — selection rationale is documented and defensible

**What's not verified:**
- Symmetry under printed gear pair (manufacturing tolerance ~0.2 mm could introduce asymmetric play)
- Rigid-link assumption (PLA deflection under 5–8 N grip force, especially on L3 = 29 mm coupler)
- PLA pin wear (100+ cycles — MP1 open question)
- Housing clearance (47 mm ground link is >50% of 92 mm housing width)

**Print decision:** Would print for functional testing. Linkage geometry is the strongest subsystem analytically.

---

## Subsystem 2: Drive Train — **Needs work**

**What's verified:**
- Architecture A: two 20T gears at m = 1.0, center distance 20 mm
- Lewis bending stress: σ = 11.7 MPa, SF = 2.14 at nominal (25 MPa PLA limit)
- 1:1 meshing inherently counter-rotates at equal rates
- Packaging: 22 × 42 × 8 mm footprint = 3.2% of housing volume
- **[MP5 UPDATE]** Yoel's MP3 gear DFM skill independently validates: face width 8 mm ≥ 5 mm minimum, SF 2.14 ≥ 2.0 threshold, flat print orientation confirmed

**What's not verified:**
- Tooth strength under realistic load (Lewis is necessary but not sufficient — no bench test)
- Backlash in FDM-printed gears (0.10–0.15 mm designed in, but real meshing untested)
- Ergonomic feel of 0.28 turns (below MP1's 2–3 turn target)
- PLA creep under sustained grip load at tooth roots

**Print decision:** Would print for testing. Gear geometry is well-defined and stress margins are adequate. Test meshing quality and backlash with a print before committing to full assembly.

---

## Subsystem 3: Jaw Arms — **Unknown**

**What's verified:** Finger tip extension defined (9 mm past joint B). BigClaw reference available (45 mm jaw arm, 28 mm coupler).
**What's not verified:** Jaw arm geometry, cross-section, grip surface, attachment method, alignment tolerance (0.5 mm misalignment = top BigClaw complaint per Haben's MP3).
**Print decision:** Cannot print — no design exists.
**[MP5 UPDATE]** Remains the highest-priority design gap. Silicone grip pads (+40% force per BigClaw lessons) and fillet radii at bends should be incorporated when designed.

---

## Subsystem 4: Housing — **Unknown**

**What's verified:** Envelope defined (92 × 46 × 55 mm). Drive train fits with 25 mm clearance per side.
**What's not verified:** Shell geometry, wall thickness, shaft bore locations, snap-fit clip design, clearance to linkage sweep, split line.
**Print decision:** Cannot print — no design exists.
**[MP5 UPDATE]** Snap-fit chosen (per team decision) but PLA brittleness remains a risk. Screw boss fallback should be designed in.

---

## Subsystem 5: Input Wheel — **Unknown**

**What's verified:** 12–15 mm thumb wheel radius spec. Direct coupling to Side 1 gear shaft (Ø3.0 mm pin).
**What's not verified:** Thumb wheel geometry, shaft coupling (set screw or D-flat needed), ergonomic feel at N = 1.
**Print decision:** Cannot print — no design exists.

---

## Subsystem 6: Pins / Joints — **Needs work**

**What's verified:**
- Bore Ø3.40 mm, pin Ø3.0 mm → 0.40 mm designed clearance
- Post-FDM clearance: 0.20 mm (reliable sliding fit)
- Applied to all 10 joints (8 linkage + 2 gear shafts)
- **[MP5 UPDATE]** ACME-MFG-004 press-fit tolerance (0.10–0.15 mm) referenced to distinguish from our sliding fit design

**What's not verified:**
- Cycle life (100+ cycles)
- Dimensional consistency across 10 printed joints
- Pin deflection under load at longer link lengths

**Print decision:** Would print for testing. Single pin-in-bore test print is the minimum validation needed.

---

## Overall Prototype Readiness (unchanged from MP4 Part B)

**Not ready to print a complete gripper.** The linkage and drive train are analytically solid — three subsystems (1, 2, 6) would be printed for functional testing tomorrow. Three subsystems (3, 4, 5) have no CAD and cannot be printed.

**Critical path for a printable prototype:**
1. Housing CAD with gear pair and linkage pivots placed
2. Jaw arm geometry with alignment tolerances and grip surface
3. Thumb wheel with shaft coupling
4. Test print of one 20T gear pair to validate FDM mesh quality
5. Test print of one pin-in-bore joint to validate clearance

**[MP5 UPDATE]** The team chose dynamic simulation for the MP5 demo rather than a physical prototype, acknowledging these gaps honestly. The demo will show the linkage mechanism in motion and a live MCP tool call — proving the analytical work is sound even though the physical build is incomplete.
