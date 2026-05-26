# MP4 Part B — Team Centaur Log

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion

> Common topics for Part B centaur loops: synthesizing across the linkage
> comparison, choosing a drive-train architecture (single spur pair,
> compound, worm, or sync-pair + separate reduction), sizing it (per-stage
> ratios, packaging), checking that the chosen reduction N doesn't push
> the linkage out of its workable transmission angle band, running DFM
> checks on the chosen geometry, identifying risks in the per-subsystem
> trust assessment, drafting the MP5 narrative.
>
> The five required loops do not all have to be design loops —
> evaluation and synthesis loops count. A loop where the team asked the
> AI "what's wrong with this drive-train sketch?" is just as valid as
> one where the team asked "design a drive train that hits reduction N."

Minimum: **5 loops across the team**. Quality, not volume. Different
team members can lead different loops; the lead member is captured in
the entry.

---

## Loop 1 — Linkage Comparison and Selection

**Date:** 2026-05-26
**Lead team member:** David Ricciotti
**Context provided to AI:** Haben's completed Part A notebook (`MP4_PartA_Build_to_Verify_completed.ipynb`), David's Part A notebook (already merged in repo), MP1 Part B brief (40 mm jaw opening target), MP3 Part B gear CAD specs.
**What we asked:**
> Integrate Haben's Part A data into the Part B linkage comparison worksheet. Extract his design parameters, fill in his row in the comparison table, write the comparison notes, and generate side-by-side plots.

**What we got back:**
> Devin extracted Haben's design: L1=47, L2=20, L3=29, L4=23, O4=(47,0), tip extension 9 mm, input range −50° to +50°, single-side displacement 20.06 mm (40.13 mm total jaw opening), transmission angle 61.3°–91.3°. Generated two comparison plots (displacement vs. input angle, transmission angle vs. input angle) showing both designs on the same axes. Identified the key difference: Haben's design meets the 40 mm MP1 target while David's only reaches 25 mm. Evidence: `plots/displacement_comparison.png`, `plots/mu_comparison.png`.

**Team assessment:**
> The team agreed with the AI's analysis. The comparison plots made the difference clear: Haben's design hits 40 mm exactly, David's falls 15 mm short. The transmission angle margins are nearly identical (21.3° vs. 22°), so there's no penalty for choosing the larger opening. The team selected Haben's linkage.

**What changed:**
> Haben's linkage selected as the team's design. This cascaded into all subsequent worksheets: the gear pair design, trust assessment, and DFM checklist were all updated to use Haben's geometry. The 100° input sweep (vs. David's 28°) fundamentally changed the drive train requirements.

---

## Loop 2 — Drive Train Architecture Decision

**Date:** 2026-05-26
**Lead team member:** David Ricciotti
**Context provided to AI:** Haben's linkage parameters (100° sweep), MP1 brief (2–3 thumb-wheel turns, 92 × 46 × 55 mm envelope), David's MP3 gear specs (14T at m=1.0), the existing compound train design (Architecture B) with its packaging problems.
**What we asked:**
> List all team decisions needed for Part B, including drive-train architecture options with pros and cons. We need to understand the trade-offs before committing.

**What we got back:**
> Devin listed 9 decisions with options for each. For the drive train, four architectures were presented: (A) single spur pair — simplest, but N limited; (B) compound spur train — current design, but packaging issues (center distances > 92 mm); (C) worm — compact for high N, but self-locking and hard to print; (D) sync-only pair + separate reduction. The AI flagged that with Haben's wider 100° sweep, the N needed for 2.5 turns drops from 32 (David's linkage) to 9, making a single spur pair more viable. Evidence: the decision list message in this Devin session.

**Team assessment:**
> The team chose Architecture A (single spur pair) because the wider input range from Haben's linkage means the drive train can be dramatically simpler. With N = 1 (two identical 20T gears), the thumb wheel maps directly to linkage input. The team accepted 0.28 turns from open to closed — this is fewer than the MP1 target of 2–3 turns, but the trade-off of eliminating multi-stage gearing, reducing part count by 3, and solving the packaging problem was worth it.

**What changed:**
> Architecture switched from B (compound spur) to A (single spur pair). Gear count dropped from 5 to 2. Overall part count dropped from 29 to 25. Center distances dropped from 126 mm (over budget) to 20 mm (well within 92 mm envelope). The packaging problem that was the #1 risk in the compound train is now eliminated.

---

## Loop 3 — DFM and Pin Clearance Review

**Date:** 2026-05-26
**Lead team member:** David Ricciotti
**Context provided to AI:** Updated gear design (20T at m=1.0), existing pin clearance analysis (Ø3.0 pin in Ø3.20 bore = 0.00 mm post-FDM), MP1 FDM tolerance assumptions (holes print ~0.10 mm undersize, pins ~0.10 mm oversize).
**What we asked:**
> Review the DFM checklist for the updated design. In particular, the pin clearance was flagged as borderline — what bore diameter gives a reliable sliding fit after FDM tolerance?

**What we got back:**
> Devin recalculated: with Ø3.00 pin and Ø3.20 bore, the designed clearance is 0.20 mm diametral, but FDM tolerance eats all of it (−0.20 mm net), leaving 0.00 mm — borderline interference. Increasing the bore to Ø3.40 mm gives 0.40 mm designed clearance, netting 0.20 mm post-FDM — a reliable sliding fit without reaming. The AI also computed Lewis bending stress for the new 20T gear: σ = 11.7 MPa at nominal torque (SF = 2.14), a meaningful improvement over the 14T design. Evidence: updated DFM checklist.

**Team assessment:**
> The team agreed to increase the bore to Ø3.40 mm across all joints. This was a straightforward fix that eliminates the need for post-processing (reaming). The improved gear stress margins from moving to 20T were a bonus of the Architecture A switch that the AI surfaced quantitatively.

**What changed:**
> Bore diameter increased from Ø3.20 to Ø3.40 mm across all 10 rotating joints. Pin clearance went from "borderline — may not fit" to "reliable sliding fit." Lewis safety factor improved from ~1.4 (14T) to 2.14 (20T) at nominal torque. DFM checklist updated with all new values.

---

## Loop 4 — Trust Assessment Integration

**Date:** 2026-05-26
**Lead team member:** David Ricciotti
**Context provided to AI:** Haben's Part A trust ledger, David's Part A trust ledger, the new drive train design (Architecture A, 20T × 20T), the updated pin clearance spec, the DFM checklist.
**What we asked:**
> Update the per-subsystem trust assessment to reflect the team's chosen linkage (Haben's) and drive train (Architecture A). For each subsystem, flag what's verified, what's not, and the risk if we print as-is.

**What we got back:**
> Devin rebuilt the trust assessment from Haben's data: Subsystem 1 (linkage) inherits Haben's three-path verification (code, hand calc, centaur loop) and his trust ledger's symmetry and housing clearance flags. Subsystem 2 (drive train) got a complete rewrite — the packaging problem is eliminated (20 mm center distance vs. 126 mm), the Lewis stress margin is better (SF = 2.14 vs. ~1.4), and the coupling check is trivially satisfied (N = 1). Subsystems 3–5 remain Unknown. Subsystem 6 (pins) was updated with the new Ø3.40 bore spec. The AI identified three critical gaps: no housing/jaw arm/thumb wheel CAD, no physical test prints, and the ergonomic unknown of 0.28-turn operation.

**Team assessment:**
> The trust assessment accurately reflects where we are. The team noted that the AI correctly identified the 47 mm ground link as a housing clearance risk that Haben's own trust ledger flagged. The "0.28 turns may feel too fast" observation was new — the team hadn't considered the ergonomic feel of such a direct drive.

**What changed:**
> Trust assessment completely rewritten for the final design. The overall readiness conclusion is "not ready to print tomorrow" — the analytical work is solid, but three subsystems have no CAD and no physical testing has been done. The biggest shift from the previous version: the drive train went from "biggest risk" (packaging doesn't fit) to "well-sized and compact" (20 mm center distance).

---

## Loop 5 — MP5 Handoff and Demonstration Planning

**Date:** 2026-05-26
**Lead team member:** David Ricciotti
**Context provided to AI:** MP5 README and rubric (uploaded to repo), team role assignments (David = narrative, Haben = slides, Yoel = demo), team decision on dynamic simulation for demo, the completed trust assessment and DFM checklist.
**What we asked:**
> Update the MP5 handoff document with the final design decisions, team roles, and demo plan. The demo will be a dynamic simulation (not a physical prototype). Also identify the wrong-AI moment for the presentation.

**What we got back:**
> Devin updated the handoff with: (1) final design summary using Haben's linkage + Architecture A drive train, (2) prototype-ready list (linkage kinematics verified, gear stress passing), (3) not-ready list (no CAD for housing/jaw/wheel, no test prints, 0.28-turn ergonomic unknown), (4) demo plan (dynamic simulation of Haben's linkage motion + live MCP tool call), (5) team roles assigned, (6) open questions for MP5. The AI identified the wrong-AI moment: the original design used 40 mm jaw opening target with a 0°–46° input range, but when David provided MP1/MP3 context, the real target was 25 mm with 0°–28° — the AI's initial design parameters were confidently wrong because it didn't have the project context.

**Team assessment:**
> The handoff document captures the state accurately. The wrong-AI moment is a good story for the presentation — the AI started with the right methodology but wrong parameters because it lacked the MP1/MP3 context. The team caught it by comparing against the original brief. This directly illustrates the Context Management and Centaur Engineering pillars.

**What changed:**
> MP5 handoff document finalized with all decisions. Team roles locked in. Demo plan committed: dynamic simulation of linkage motion + live MCP tool call for a real engineering question (e.g., recomputing transmission angles for a perturbed geometry). The wrong-AI moment is ready for the presentation narrative.

---

## Bonus loops (optional)

> _Add as many additional `## Loop N` blocks as you want. Five is the
> floor, not the ceiling — bonus loops are useful evidence for the
> centaur engineering pillar in MP5._
