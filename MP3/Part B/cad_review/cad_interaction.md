# CAD Review and Iterations

# Reviewing a Pinion Gear from the Gear Train

### Checkpoint 1 - Initial Concept

**SOLIDWORKS 2024**

![gear v2](cad_review/Pinion_Gear_v1.png)

**Prompt to AI host (Copilot agent, MiniClaw skill loaded):**
> Given this design and the below table for our pinion gear,
> what should I check over given our PLA constraints?

**AI response (excerpt):**
> Calling `query_miniclaw_rag` for ACME's printed-gear standards...
>
> Based on `ACME-ENG-001` and the WidgetBot test report, here are key things
> to check:
> 1. Undercut risk — With only 12 teeth at module 1.5 mm, 
>    you're in the danger zone. Minimum teeth without undercut is ~14–16 at 20°.
>    Action: Increase root fillet from R0.40 to 0.5–0.6 mm if feasible; thin roots will fail in fatigue.
> 2. Face width stress — 12 mm is generous, but the 3.50 mm bore and hub transition need a generous fillet.
>    Action: Enlarge the bore–hub fillet (R0.40 shown) to reduce stress concentration.
> 3. Tooth root bending — 12 teeth means higher load per tooth.
>    Action: Run a Lewis bending check for 5–8 N grip forces; face width is OK, but root fillet is critical.
> 4. Print orientation & layer strength — Print flat, teeth in-plane; avoid upright printing.
> 5. Center distance tolerance — Add +0.05–0.10 mm allowance for PLA growth and note bore clearance.
> 6. Surface finish & mesh quality — Expect layer-line noise; consider post-processing if quiet operation matters.

**What I changed:** 

Root fillet increased from R0.40 → R0.60 mm for better undercut protection and lower bending stress.

Root diameter relaxed from 14.25 → 14.60 mm to thicken the tooth base.

Bore–hub fillet enlarged to R0.80 min, with hub Ø9.00 mm for improved torsional strength.

Bore tolerance widened to Ø3.50 +0.25 / 0.00 mm to account for FDM growth and ensure shaft clearance.

---

### Checkpoint 2 — Refined version

![gear v2](cad_review/Pinion_Gear_v2.png)

**Prompt:**
> Given this image and the changes I made are there any other things you'd flag?

**AI response (excerpt):**
> Solid improvements—you've addressed most of the critical PLA stress points.

What looks good:

> R0.60 root fillet and increased root diameter improve bending strength.

> R0.80 MIN bore–hub fillet and larger hub OD help with torsional load.

> Bore tolerance +0.25 / –0.00 mm is appropriate for FDM growth.

> Print orientation locked to “gear axis horizontal, teeth in XY plane” is correct for layer strength.

Flags to check:  
> 1. Undercut margin with 12 teeth at 1.5 mm module — still near the minimum tooth count; verify involute isn’t compromised.

> 2. Torque limit — 0.40 N·m max is tight; cross-check against system torque budget.

> 3. Hub design — at ~0.40 N·m, shear stress near the bore is close to PLA limits; consider extra margin.

> 4. Bore tolerance growth — confirm whether the mating shaft is metal or plastic; growth interactions matter.

> 5. Noise and post-processing — optional resin coating is a good path if quiet operation is important.

Recommended design shift: move to a 14T, module 1.0 pinion to avoid undercut and improve tooth geometry while keeping torque in a safer range.

**What I changed:**

Teeth/module: switched from 12T, m = 1.5 to 14T, m = 1.0 to eliminate undercut risk and improve tooth geometry.

Root diameter: set to ≈11.8–12.0 mm for a stronger tooth base with adequate clearance.

Root fillet: kept at R0.60 mm to maintain low bending stress.

Bore: changed to Ø3.00 +0.20 / 0.00 mm for a cleaner clearance fit on a metal shaft.

Hub OD: set to Ø8.00 mm for a stiffer torsional section.

Hub–bore fillet: R0.80 min to reduce stress concentration at the hub.

Face width: adjusted to 8.00 mm, still sufficient for 0.30–0.40 N·m torque.

Torque note: added 0.30 N·m nominal, 0.40 N·m max to the drawing so the system limits user torque.

Print orientation note: “Gear axis horizontal, teeth in XY plane” added to the manufacturing notes.

Assembly note: specified +0.05–0.10 mm backlash at center distance to account for PLA growth and ensure smooth meshing.