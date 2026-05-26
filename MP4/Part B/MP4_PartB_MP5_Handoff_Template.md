# MP5 Handoff Document — Team Ricciotti-Berhe-Tesfatsion

This document explicitly bridges MP4 → MP5. The team uses it as the seed
for the MP5 presentation outline. Same team continues; same design
continues. Don't redo work in MP5 that this document already captured.

---

## Final Design Summary

> _[Requires team finalization — draft below based on David's Part A data and preliminary drive train:]_
>
> The MiniClaw uses David Ricciotti's parallelogram four-bar linkage (L1=L3=12 mm, L2=L4=26 mm, vertical ground link, O4=(0,12)) with a 0°–28° input range producing 25 mm total jaw opening. The drive train is a compound spur train (Architecture B): two 4:1 spur stages (14T→56T at m=1.0, from David's MP3 pinion refinement) plus a 1:1 mating final pair for counter-rotation synchronization, giving overall reduction N = 16. _[Team: update with final architecture decision, especially if N is adjusted to meet the 2–3 thumb-wheel-turn target.]_

---

## What's Prototype-Ready

Pulled directly from the per-subsystem trust assessment.

- Linkage kinematics: transmission angle stays in the 62°–90° band across full 0°–28° input range (22° margin above 40° floor), verified by three independent methods (code, hand calc, centaur loop) agreeing within 0.1 mm.
- Single-side displacement of 12.5 mm delivers 25 mm total jaw opening, matching the MP1 target.
- No interference detected across full linkage sweep; mechanism fits within half-envelope budget (26 × 46.2 mm vs. 46 × 55 mm allowed).
- Stage 1 gear geometry (14T at m=1.0) refined through three MP iterations with stress analysis, tolerance specs, and CAD parameterization.
- _[Team: add additional items from the trust assessment once completed]_

---

## What's Not Ready (and Why)

Pulled directly from the per-subsystem trust assessment.

- Drive train packaging: center distances (35 + 35 + 56 mm) exceed the 92 mm housing length in a linear layout. Gear arrangement must be non-linear or tooth counts reduced. No physical sketch or CAD verifies that the gears fit inside the housing.
- Pin joint clearance: designed 0.20 mm diametral clearance nets to 0.00 mm after FDM tolerance. Pins may not fit without post-processing. Bore tolerance needs to increase to ≥ 0.30 mm.
- No housing, jaw arm, or thumb wheel CAD exists — these subsystems are flagged as "Unknown" in the trust assessment.
- Part count (29 estimated) is nearly double the 15-part target from MP1. Merges and simplifications needed.
- Tooth strength under realistic load: Lewis analysis showed marginal SF at nominal torque and failure at max hand torque with degraded PLA. No bench test.
- _[Team: add items from Haben's and Yoel's subsystem reviews]_

---

## What We're Choosing to Demonstrate in MP5

_[Requires team decision:]_

> _[Suggested: demonstrate the linkage motion with a mirrored two-sided gripper closing on a small object (pencil or marker). The linkage kinematics are the most thoroughly verified subsystem. Whether the demo uses a physical 3D-printed prototype or a dynamic simulation depends on whether the team resolves the housing and gear packaging before the MP5 deadline. Name the specific demo and the closing action that shows "this is the MiniClaw and it works."]_

---

## Open Questions Going Into MP5

Be honest. The product team review next week is more interesting if the
team names what it doesn't yet know.

- Will the m=1.0 gear teeth (root fillet R0.60) print with sufficient fidelity on FDM PLA to mesh smoothly under load?
- Can the drive train (center distances totaling 126 mm) be physically arranged within the 92 × 46 × 55 mm housing?
- _[Team: add at least one more open question from the integration work]_

---

## Team Composition for MP5

Same team. Confirm member names and any role notes (who's leading the
narrative, who's running the demo, who's handling slides):

- David Ricciotti — _[role TBD by team]_
- Haben Berhe — _[role TBD by team]_
- Yoel Tesfatsion — _[role TBD by team]_

---

## Pointers Into MP4 Artifacts

For the MP5 portfolio narrative — link, don't copy:

- Linkage Comparison Worksheet: `MP4/Part B/MP4_PartB_Linkage_Comparison.md`
- Drive-Train Design Worksheet: `MP4/Part B/MP4_PartB_Gear_Pair_Design.md`
- Per-Subsystem Trust Assessment: `MP4/Part B/MP4_PartB_Trust_Assessment_Template.md` (completed version)
- DFM Checklist (completed): `MP4/Part B/dfm_checklist_completed.md`
- Team Centaur Log: `MP4/Part B/MP4_PartB_Team_Centaur_Log_Template.md` (completed)
- David Ricciotti's Part A: [DavidR734/ai-in-pd-spring2026-2 — MP4/Part A/MP4_PartA_Build_to_Verify.ipynb](https://github.com/DavidR734/ai-in-pd-spring2026-2/blob/main/MP4/Part%20A/MP4_PartA_Build_to_Verify.ipynb)
- Haben Berhe's Part A: _[needs link to Haben's repo]_
- Yoel Tesfatsion's Part A: _[needs link to Yoel's repo]_
