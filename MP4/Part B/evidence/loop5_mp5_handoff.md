# Evidence — Loop 5: MP5 Handoff and Demonstration Planning

**Date:** 2026-05-26
**Lead:** David Ricciotti
**AI tool:** Devin (Cognition AI) — session URL in PR description

## Prompt

> Update the MP5 handoff document with the final design decisions,
> team roles, and demo plan. The demo will be a dynamic simulation
> (not a physical prototype). Also identify the wrong-AI moment for
> the presentation.

## Context provided

- MP5 README and rubric (in repo)
- Team roles: David = narrative, Haben = slides, Yoel = demo
- Demo choice: dynamic simulation
- Completed trust assessment and DFM checklist

## AI output — Handoff summary

**Final design:** Haben's linkage (L1=47, L2=20, L3=29, L4=23) +
Architecture A (20T × 20T spur pair, m=1.0, N=1)

**Prototype-ready:**
1. Linkage kinematics verified (3 independent paths)
2. Gear tooth stress passing (SF = 2.14)
3. Pin clearance designed for FDM (Ø3.40 bore)

**Not ready:**
1. No housing CAD
2. No jaw arm CAD
3. No thumb wheel CAD
4. No test prints
5. Ergonomic unknown (0.28 turns)

**Wrong-AI moment identified:**
The AI's initial MP4 Part A design used 40 mm jaw opening with 0°–46° input
range. When David provided MP1/MP3 context, the correct target was 25 mm with
0°–28° range. The AI was confidently wrong because it lacked project context —
illustrates the Context Management and Centaur Engineering pillars.

## Team decision

- Demo: dynamic simulation of Haben's linkage motion + live MCP tool call
- Wrong-AI moment ready for presentation narrative
- All roles confirmed
