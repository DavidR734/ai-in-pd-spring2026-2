# MP4 Part B — Per-Subsystem Trust Assessment

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion
**Linkage base:** Haben Berhe's crossed-branch four-bar (L1=47, L2=20, L3=29, L4=23), selected by team — see Linkage Comparison worksheet.
**Design base for the rest of the MiniClaw:** David Ricciotti's MP1 Part B MiniClaw requirements and MP3 Part B gear CAD work serve as the base for housing envelope, gear geometry, and PLA constraints. Drive train updated to Architecture A (single spur pair) per team decision.

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
- Transmission angle stays in the 61.3°–91.3° band throughout the −50° to +50° input range, with 21.3° margin above the 40° floor — verified by Haben's Part A Section 4 plot and hand calculation.
- Single-side displacement reaches 20.06 mm at θ = 50°, giving 40.13 mm total jaw opening — confirmed by three independent methods (code, hand calc, centaur loop) agreeing within 0.1 mm. This meets the MP1 40 mm target.
- No interference detected across the full sweep; all links clear of each other.
- The 1:1 gear pair (N = 1) maps the thumb wheel directly to linkage input, so the Part A-designed range is exactly the operating range — no coupling mismatch.

**What's not verified:**
- **Symmetry assumption** — the other side will mirror correctly only if the drive train (Subsystem 2) achieves counter-rotation at the same rate. The 1:1 spur pair guarantees equal angular rates by geometry, but manufacturing tolerance in 3D-printed PLA (~0.2 mm, per David's MP3 tolerance spec) could introduce asymmetric play between the two sides.
- **Rigid-link assumption** — position analysis assumes perfectly rigid links. Under the 5–8 N grip force (MP1 requirement), PLA links could deflect enough to change effective geometry. Haben's L3 = 29 mm coupler is longer than David's 12 mm coupler, meaning more potential deflection.
- **PLA pin wear** — MP1 flagged "Will printed PLA/PETG pivot pins sustain 100+ cycles without wear or slack?" as a key unknown. Haben's design has the same 4 pivot joints per side = 8 total wear points.
- **Housing clearance** — Haben's Part A trust ledger explicitly flagged that the housing envelope must be overlaid with the linkage sweep to confirm clearance near joint B and the coupler path. The 47 mm ground link is over half the 92 mm housing width.

**Risk if we print as-is:** The linkage geometry is well-verified analytically, but the rigid-link assumption and untested pin wear mean the first print may have sloppy joints and reduced grip force. The 47 mm ground link occupies significant housing width — clearance verification is critical.

---

## Subsystem 2: Drive Train

*(single spur pair: two 20T gears at m = 1.0, 1:1 ratio — Architecture A)*

**Status:** Needs work

**What's verified:**
- Architecture A (single spur pair) selected by team, replacing the compound train. Rationale documented: simpler, fewer parts, packaging fits easily.
- Gear geometry: z = 20 at m = 1.0, pitch diameter = 20 mm each, center distance = 20 mm. This fits comfortably in the 92 mm housing (22 mm total drive train width vs. 92 mm available).
- Symmetry: the 1:1 meshing pair inherently counter-rotates at equal rates — no additional sync mechanism needed.
- Lewis bending stress: σ ≈ 11.7 MPa at nominal torque (SF = 2.14 against 25 MPa printed PLA), improving over the original 14T pinion design.
- N = 1 means the coupling check is trivially satisfied — the operating range equals the Part A-designed range with no mismatch.

**What's not verified:**
- **Tooth strength under realistic load** — Lewis analysis shows passing SF at nominal torque (2.14) and marginal at max hand torque (1.28 at 0.5 N·m). No physical bench test has been done.
- **Backlash in printed gears** — FDM over-extrusion may require additional backlash allowance beyond the involute profile. Real-world meshing under load not tested.
- **Thumb-wheel turn count** — N = 1 gives only 0.28 turns from open to closed, well below the MP1 target of 2–3 turns. The team accepts this trade-off, but it means the gripper will feel very fast/direct rather than precision-geared. User feedback on ergonomics is unknown.

**Risk if we print as-is:** The drive train geometry is compact and the stress analysis shows adequate margins. The main risk is ergonomic: 0.28 turns may feel too fast for precise gripping tasks. Gear meshing quality in FDM PLA at m = 1.0 is unknown without a test print.

---

## Subsystem 3: Jaw Arms (gripper fingers)

**Status:** Unknown

**What's verified:** The finger tip extension (9 mm past joint B along the coupler direction, per Haben's Part A design) is defined, but the physical jaw arm shape, cross-section, and attachment method are not designed. BigClaw reference dimensions are available from Haben's MP3 RAG query: BigClaw uses a 45 mm output link (jaw arm) with 28 mm coupler and 32 mm crank arm, achieving 0–86 mm jaw range.
**What's not verified:** Jaw arm geometry, cross-section for 5–8 N grip force, attachment to the coupler link, contact surface for gripping, PLA stiffness under load. Per Haben's MP3 BigClaw teardown: jaw alignment is critical — even 0.5 mm misalignment between left and right jaws causes uneven gripping (top customer complaint in GripperBot v1). Silicone grip pads improved grip force by ~40% without increasing mechanism force. Haben's MP3 CAD review also showed that fillets at jaw arm bends are important for reducing stress concentration in PLA.
**Risk if we print as-is:** Cannot print — no jaw arm design exists. Team needs to create jaw arm geometry in CAD, paying attention to alignment tolerances and stress concentration at bends (per Haben's MP3 lessons).

---

## Subsystem 4: Housing and Mounting

**Status:** Unknown

**What's verified:** The housing envelope is defined from MP1 (92 × 46 × 55 mm). The drive train (20 mm center distance, two Ø22 mm gears) fits within this envelope with generous clearance. Housing closure method: snap-fit (per team decision, matching MP1 spec).
**What's not verified:** Housing shell geometry, wall thickness (target ≥ 1.5 mm), shaft bore locations, snap-fit clip design (PLA is brittle — snap-fit clips may need to be thicker than typical), clearance to linkage motion, split line for assembly access.
**Risk if we print as-is:** Cannot print — no housing design exists. The snap-fit closure is a known risk with PLA — clips may crack during assembly. Team should consider adding screw bosses as a fallback.

---

## Subsystem 5: Input Wheel / Servo Coupling

**Status:** Unknown

**What's verified:** MP1 spec calls for a hand-driven thumb wheel with 12–15 mm radius for comfortable grip. The thumb wheel connects directly to Side 1's gear shaft (Ø3.0 mm pin).
**What's not verified:** Thumb wheel geometry, knurling pattern, shaft coupling to gear, ergonomic torque at N = 1 (with 0.28 turns, the user applies torque for only ~100° of rotation — feels like a quarter-turn valve), whether servo coupling is needed for future motorization.
**Risk if we print as-is:** Cannot print — no thumb wheel design exists. The coupling is simple (round shaft through a bore) but needs a set screw or D-flat to prevent slipping.

---

## Subsystem 6: Pin / Joint System

**Status:** Needs work

**What's verified:** David's MP1 specified Ø3–4 mm pins with 0.1–0.2 mm clearance. Bore diameter updated to Ø3.40 mm (increased from MP3's Ø3.20 mm) to provide 0.40 mm diametral clearance (0.20 mm radial), guaranteeing a sliding fit after FDM tolerance (holes print ~0.10 mm undersize, pins ~0.10 mm oversize → net clearance = 0.40 − 0.20 = 0.20 mm). This applies to all 8 linkage pivots and 2 gear shaft bores.
**What's not verified:**
- Cycle life (100+ cycles per MP1 requirement) — no physical test
- Print dimensional accuracy for the 0.40 mm clearance at Ø3.40 bore
- Whether printed PLA pins sustain repeated loading without mushrooming or wearing
- Pin deflection under load at the longer link lengths (L3 = 29 mm coupler, L4 = 23 mm output)

**Risk if we print as-is:** The increased bore tolerance (0.40 mm) should ensure a sliding fit, but cycle life and wear are completely unknown. A test print of one pin-in-bore joint is the minimum bench test needed.

---

## Overall Prototype Readiness

The team is **not ready to print tomorrow**, but the critical path is clear. The linkage kinematics (Subsystem 1) are the strongest subsystem — thoroughly verified by Haben's Part A work with three independent confirmation paths. The drive train (Subsystem 2) is simple and well-sized, with Lewis stress analysis showing adequate margins (SF = 2.14 at nominal load).

Three critical gaps remain:
1. **No housing, jaw arm, or thumb wheel CAD** — Subsystems 3–5 are all flagged Unknown. These are the MP5 deliverables.
2. **No physical test prints** — pin fit, gear meshing, and PLA dimensional accuracy are all analytically predicted but unverified in print.
3. **Ergonomic unknowns** — the 0.28-turn operation (N = 1 with 100° sweep) may feel too fast for precise gripping. This can only be evaluated with a physical or dynamic prototype.

If Jordan handed us another day, we would focus on: (1) a housing CAD sketch with the gear pair and linkage pivots placed, (2) a single test print of the 20T gear pair meshing to validate FDM dimensions, and (3) a dynamic simulation of the linkage motion to validate the trajectory before committing to a full prototype build.

---

## Pointers Into Source Artifacts

For graders and teammates who want the underlying evidence, list
explicit paths:

- Chosen Part A linkage source: Haben Berhe's `MP4_PartA_Build_to_Verify_completed.ipynb` ([hab27/ai-in-pd-spring2026](https://github.com/hab27/ai-in-pd-spring2026))
- David Ricciotti's Part A: `MP4/Part A/MP4_PartA_Build_to_Verify.ipynb` ([DavidR734/ai-in-pd-spring2026-2](https://github.com/DavidR734/ai-in-pd-spring2026-2))
- Yoel Tesfatsion's repo: [YoelUW/ai-in-pd-spring2026](https://github.com/YoelUW/ai-in-pd-spring2026) (MP1–MP3 only; no MP4 Part A — gear DFM skill and RAG server from MP3 Part B inform the team's design)
- Linkage Comparison Worksheet: `MP4/Part B/MP4_PartB_Linkage_Comparison.md`
- Drive-Train Design Worksheet: `MP4/Part B/MP4_PartB_Gear_Pair_Design.md`
- DFM Checklist: `MP4/Part B/MP4_PartB_DFM_Checklist.md`
- Team Centaur Log: `MP4/Part B/MP4_PartB_Team_Centaur_Log_Template.md`
- Comparison plots: `MP4/Part B/plots/`
- Drive train sketch: `MP4/Part B/sketches/drive_train.png`
