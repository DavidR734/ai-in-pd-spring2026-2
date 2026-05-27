# MP5 Handoff Document — Team Ricciotti-Berhe-Tesfatsion

This document explicitly bridges MP4 → MP5. The team uses it as the seed
for the MP5 presentation outline. Same team continues; same design
continues. Don't redo work in MP5 that this document already captured.

---

## Final Design Summary

The MiniClaw uses Haben Berhe's crossed-branch four-bar linkage (L1=47, L2=20, L3=29, L4=23, O4=(47,0)) with a −50° to +50° input range (100° sweep) producing 40.13 mm total jaw opening — meeting the MP1 40 mm target. The drive train is a single spur pair (Architecture A): two identical 20T gears at m=1.0, meshing 1:1 for counter-rotation synchronization. Overall reduction N = 1, giving 0.28 thumb-wheel turns from open to closed. The team accepts this deviation from the MP1 2–3 turn target in exchange for dramatically simpler mechanics (2 gears vs. 5, 20 mm center distance vs. 126 mm). Pin bores increased to Ø3.40 mm for reliable post-FDM sliding fit.

---

## What's Prototype-Ready

Pulled directly from the per-subsystem trust assessment.

- Linkage kinematics: transmission angle stays in the 61.3°–91.3° band across full −50° to +50° input range (21.3° margin above 40° floor), verified by three independent methods (code, hand calc, centaur loop) agreeing within 0.1 mm.
- Single-side displacement of 20.06 mm delivers 40.13 mm total jaw opening, meeting the MP1 target.
- No interference detected across full linkage sweep.
- Drive train packaging: 20 mm center distance fits within 92 mm housing with 72 mm clearance. The packaging problem from the compound train is eliminated.
- Gear stress: Lewis bending SF = 2.14 at nominal torque (0.3 N·m) for the 20T gear — comfortable margin against 25 MPa printed PLA.
- Pin clearance: 0.40 mm diametral designed, 0.20 mm post-FDM — reliable sliding fit.

---

## What's Not Ready (and Why)

Pulled directly from the per-subsystem trust assessment.

- No housing, jaw arm, or thumb wheel CAD exists — these subsystems are flagged as "Unknown" in the trust assessment. They need to be designed in CAD before any prototype build.
- No physical test prints have been done — pin fit, gear meshing, and PLA dimensional accuracy are all analytically predicted but unverified.
- Ergonomic unknown: 0.28 thumb-wheel turns (100° of rotation) may feel too fast for precise gripping tasks. Only a physical or dynamic prototype can evaluate this.
- Part count (25 estimated) exceeds the 15-part target from MP1. Aggressive integration (ground link into housing, jaw arms into coupler) could approach ~17 parts.
- Snap-fit housing closure is a known brittleness risk with PLA. Screw boss fallback should be designed in.

---

## What We're Choosing to Demonstrate in MP5

**Demo plan:** Dynamic simulation of Haben's four-bar linkage motion, showing the jaw opening and closing through the full −50° to +50° input range. The simulation will show the finger tip trajectory, the displacement curve, and the transmission angle staying within the workable band — all animated on screen.

**Live MCP tool call:** A live function call to recompute the transmission angle for a perturbed geometry (e.g., "what happens if we change L3 from 29 mm to 32 mm?") — demonstrating the Tools & Integration pillar.

**Fallback:** Pre-recorded video of the simulation running on David's laptop, uploaded to the repo at `MP5/demo/`.

**Punchline:** "This linkage achieves 40 mm jaw opening while staying inside the workable transmission angle band. The single spur pair syncs both sides with just two gears. Here's the simulation proving it works."

---

## The Wrong-AI Moment

The AI (Devin) initially designed David's Part A linkage with a 40 mm jaw opening target and 0°–46° input range, producing parameters that looked correct (L1=L3=12, L2=L4=26, 20.3 mm single-side displacement). But when David provided his MP1 and MP3 context documents, the real target turned out to be 25 mm jaw opening with a 0°–28° input range — the AI had been confidently designing to the wrong specification because it lacked the project context. The error was caught because David compared the AI's output against his own prior work. The fix required updating all sections, evidence files, and motion artifacts.

This directly illustrates the Centaur Engineering and Context Management pillars: the AI does the math correctly but needs the human to supply and validate the right inputs. Without the MP1/MP3 context, the AI produced a technically sound but factually wrong design.

---

## Open Questions Going Into MP5

Be honest. The product team review next week is more interesting if the
team names what it doesn't yet know.

- Will the 0.28-turn thumb wheel operation feel ergonomically acceptable, or does the gripper need a detent or friction brake to prevent accidental opening?
- Can the 47 mm ground link fit within the housing envelope alongside the jaw arm sweep path and the 20 mm gear center distance?
- Will the snap-fit PLA housing clips survive repeated assembly/disassembly, or should we design screw bosses from the start?

---

## Team Composition for MP5

Same team. Confirmed member roles:

- David Ricciotti — leads the narrative / presentation
- Haben Berhe — handles the slides
- Yoel Tesfatsion — runs the demo

---

## Pointers Into MP4 Artifacts

For the MP5 portfolio narrative — link, don't copy:

- Linkage Comparison Worksheet: `MP4/Part B/MP4_PartB_Linkage_Comparison.md`
- Comparison Plots: `MP4/Part B/plots/displacement_comparison.png`, `MP4/Part B/plots/mu_comparison.png`
- Drive-Train Design Worksheet: `MP4/Part B/MP4_PartB_Gear_Pair_Design.md`
- Drive-Train Sketch: `MP4/Part B/sketches/drive_train.png`
- Per-Subsystem Trust Assessment: `MP4/Part B/MP4_PartB_Trust_Assessment_Template.md`
- DFM Checklist: `MP4/Part B/MP4_PartB_DFM_Checklist.md`
- Team Centaur Log: `MP4/Part B/MP4_PartB_Team_Centaur_Log_Template.md`
- David Ricciotti's Part A: [DavidR734/ai-in-pd-spring2026-2 — MP4/Part A/MP4_PartA_Build_to_Verify.ipynb](https://github.com/DavidR734/ai-in-pd-spring2026-2/blob/main/MP4/Part%20A/MP4_PartA_Build_to_Verify.ipynb)
- Haben Berhe's Part A: [hab27/ai-in-pd-spring2026](https://github.com/hab27/ai-in-pd-spring2026)
- Yoel Tesfatsion's repo: [YoelUW/ai-in-pd-spring2026](https://github.com/YoelUW/ai-in-pd-spring2026) (contains MP1–MP3; no MP4 Part A submitted — Yoel's MP3 Part B gear DFM skill and RAG server inform the team's gear design and DFM checklist)
