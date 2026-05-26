# MP4 Part B — Per-Subsystem Trust Assessment

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion
**Linkage base:** _[to be confirmed by team — pre-filled assuming David Ricciotti's parallelogram design from Part A]_
**Design base for the rest of the MiniClaw:** David Ricciotti's MP1 Part B MiniClaw requirements and MP3 Part B gear CAD work serve as the base for housing envelope, gear geometry, and PLA constraints. _[Team: update if using a different member's design base]_

---

This is the central evaluation artifact. Every subsystem gets a flag —
**Ready to print**, **Needs work**, or **Unknown**. "Mostly there" is not
a flag. If the team doesn't know, that's also useful information; flag
it Unknown and write what you'd need in order to upgrade it.

The four-bar linkage and the drive train are top-level subsystems
because they are the two integration anchors. Subsystem categories
below can be adjusted if the team's design organizes differently — but
every part of the gripper must show up somewhere with a flag.

---

## Subsystem 1: Four-Bar Linkage (single side, mirrored for the other)

**Status:** Needs work

**What's verified:**
- Transmission angle stays in the 62°–90° band throughout the 0°–28° input range, with 22° margin above the 40° floor — verified by Part A Section 4 plot and analytically (μ = 90° − θ for the vertical parallelogram). _(David's Part A trust ledger, entry 1)_
- Single-side displacement reaches 12.5 mm at θ = 28°, giving 25.2 mm total jaw opening — confirmed by three independent methods (code, hand calc, centaur loop) agreeing within 0.1 mm. _(David's Part A trust ledger, entry 2)_
- No interference detected across the full sweep; all links clear of each other and the housing envelope with minimum clearance of ~23 mm between non-adjacent links. _(David's Part A trust ledger, entry 3)_
- Mechanism fits within the half-envelope budget: 26 mm horizontal, 46.2 mm vertical vs. 46 × 55 mm allowed (8.8 mm vertical margin). _(David's Part A trust ledger, entry 4)_
- _[If the team's chosen reduction N shifted the input range, re-check transmission angle at the new range and note the result here]_

**What's not verified:**
- **Symmetry assumption** — the other side will mirror correctly only if the drive train (Subsystem 2) achieves counter-rotation at the same rate. The sync gear pair is designed on paper but not bench-tested. Manufacturing tolerance in 3D-printed PLA (~0.2 mm, per David's MP3 bore tolerance spec) could introduce asymmetric play between the two sides.
- **Rigid-link assumption** — position analysis assumes perfectly rigid links. Under the 5–8 N grip force (MP1 requirement), PLA links (especially the 26 mm cranks) could deflect enough to change effective geometry. David's MP3 stress work flagged PLA bending safety factors as tight (SF ≈ 1.1–1.3 at 25–30 MPa printed strength).
- **PLA pin wear** — MP1 flagged "Will printed PLA/PETG pivot pins sustain 100+ cycles without wear or slack?" as a key unknown. 3–4 mm pin diameter with 0.1–0.2 mm clearance needs cycle testing. Four pivot joints per side = 8 total wear points.

**Risk if we print as-is:** The linkage geometry is well-verified analytically, but the rigid-link assumption and untested pin wear mean the first print may have sloppy joints and reduced grip force compared to the analysis predictions.

---

## Subsystem 2: Drive Train

*(compound spur train: two 4:1 stages + 1:1 sync pair — per current architecture choice)*

**Status:** Needs work

**What's verified:**
- Architecture choice (compound spur, Architecture B) documented with rationale tied to envelope constraints and MP3 pinion specs.
- Stage 1 gear geometry (14T at m=1.0) refined through David's MP3 Part B CAD work: root fillet R0.60, bore Ø3.00 +0.20/−0.00, hub OD Ø8.00 mm. Stress analysis done in MP1 and MP3.
- Symmetry arrangement identified (mating final 56T pair for counter-rotation).
- _[Team: add coupling check results once N is finalized]_

**What's not verified:**
- **Tooth strength under realistic load** — Lewis bending stress analysis from MP1 showed SF ≈ 1.4 at nominal torque (0.3 N·m) but SF < 1.0 at maximum hand torque (0.5 N·m) with degraded PLA (25 MPa). No physical bench test has been done.
- **Backlash in printed gears** — designed backlash of 0.05–0.10 mm (from MP3) may be insufficient for FDM over-extrusion; real-world meshing under load not tested.
- **Packaging fit** — center distances sum to more than the 92 mm housing length with the current tooth counts. Gear layout must be non-linear (offset/stacked) or tooth counts reduced. Not resolved yet.
- **Overall reduction N vs. thumb-wheel turn count** — current N = 16 gives only ~1.24 turns (target: 2–3). Team must decide whether to accept this, add a third stage, or change architecture.

**Risk if we print as-is:** The drive train packaging hasn't been verified to fit the housing, and the N = 16 reduction gives fewer thumb-wheel turns than the MP1 brief targets. The most likely first-print failure is gears that don't mesh smoothly due to FDM dimensional variability.

---

## Subsystem 3: Jaw Arms (gripper fingers)

**Status:** Unknown

**What's verified:** _[No jaw arm design exists yet — this is Part B integration work. The finger tip extension (22 mm past joint B along the coupler direction) is defined in David's Part A, but the physical jaw arm shape, cross-section, and attachment method are not designed.]_
**What's not verified:** _[Everything — jaw arm geometry, cross-section for 5–8 N grip force, attachment to the coupler link, contact surface for gripping, PLA stiffness under load]_
**Risk if we print as-is:** _[Cannot print — no jaw arm design exists. Team needs to create jaw arm geometry in CAD.]_

---

## Subsystem 4: Housing and Mounting

**Status:** Unknown

**What's verified:** _[The housing envelope is defined from MP1 (92 × 46 × 55 mm). No housing CAD exists for the team's specific linkage + drive train combination.]_
**What's not verified:** _[Housing shell geometry, wall thickness, shaft bore locations, assembly method (snap-fit from MP1 spec), mounting for gear shafts, clearance to linkage motion, split line for assembly access]_
**Risk if we print as-is:** _[Cannot print — no housing design exists. Team needs to create housing geometry that holds the gear shafts, linkage pivots, and thumb wheel in the correct positions.]_

---

## Subsystem 5: Input Wheel / Servo Coupling

**Status:** Unknown

**What's verified:** _[MP1 spec calls for a hand-driven thumb wheel with 12–15 mm radius for comfortable grip. No specific thumb wheel design exists for this drive train.]_
**What's not verified:** _[Thumb wheel geometry, knurling pattern, shaft coupling to the first-stage pinion, ergonomic torque at the designed N, whether servo coupling is needed (MP1 mentioned future servo baseline)]_
**Risk if we print as-is:** _[Cannot print — no thumb wheel design exists. Team needs a thumb wheel that couples to the Stage 1 pinion shaft.]_

---

## Subsystem 6: Pin / Joint System

**Status:** Needs work

**What's verified:** _[David's MP1 specified Ø3–4 mm pins with 0.1–0.2 mm clearance. MP3 refined the bore to Ø3.00 +0.20/−0.00 mm for FDM growth. The pin/bore design exists but is untested in print.]_
**What's not verified:**
- Cycle life (100+ cycles per MP1 requirement) — no physical test
- Print dimensional accuracy for the bore tolerance
- Whether snap-fit / press-fit pins (MP1 spec: no tools required) actually achieve the desired fit class in PLA
- Pin deflection under load at the 26 mm crank length

**Risk if we print as-is:** Pins may be too tight (interference fit from FDM oversizing) or too loose (if bore tolerance is generous), leading to either impossible assembly or sloppy joints. A test print of one pin-in-bore joint is the minimum bench test needed.

---

## Overall Prototype Readiness

> _[Requires team discussion to finalize. Draft below based on David's data:]_
>
> The team is **not ready to print tomorrow**. The linkage kinematics are well-verified (Subsystem 1 is the strongest subsystem), and the gear geometry has been through three iterations of MP1/MP3 refinement. However, three critical gaps remain: (1) the drive train packaging hasn't been verified to fit the 92 mm housing, (2) no housing, jaw arm, or thumb wheel CAD exists, and (3) no physical test prints have been done to validate pin fit, gear meshing, or PLA dimensional accuracy.
>
> The single biggest risk is the drive train packaging — the current center distances don't fit a linear gear layout in the housing, and the team hasn't sketched an alternative arrangement. If Jordan handed us another day, we would focus on a housing CAD sketch with the gear train laid out inside it, followed by a single test print of one gear pair and one pin joint to validate FDM dimensions.

---

## Pointers Into Source Artifacts

For graders and teammates who want the underlying evidence, list
explicit paths:

- Chosen Part A linkage source: `MP4/Part A/MP4_PartA_Build_to_Verify.ipynb` (David Ricciotti's repo: [DavidR734/ai-in-pd-spring2026-2](https://github.com/DavidR734/ai-in-pd-spring2026-2))
- Linkage Comparison Worksheet: `MP4/Part B/MP4_PartB_Linkage_Comparison.md`
- Drive-Train Design Worksheet: `MP4/Part B/MP4_PartB_Gear_Pair_Design.md`
- DFM Checklist (completed): `MP4/Part B/dfm_checklist_completed.md`
- Team Centaur Log: `MP4/Part B/MP4_PartB_Team_Centaur_Log_Template.md` (completed)
- CAD or sketches folder: _[team: add path once sketches are created]_
- Haben Berhe's Part A repo: _[needs link]_
- Yoel Tesfatsion's Part A repo: _[needs link]_
