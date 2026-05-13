---
name: miniclaw_geartrain_review
description: >
  Evaluates MiniClaw gear trains for strength, durability, printability, and kinematic correctness. Trigger whenever a user asks whether a gear or gear train will survive PLA loading, whether tooth geometry is correct, or whether a design matches BigClaw reference performance.
---

# MiniClaw GearTrain Check Skill

## When to use this skill

Use this skill when the user is asking about a Miniclaw Geartrain component, and its mechanical statistics. 

- “Will this gear survive?” / “Is this gear ratio OK?”
- Lewis stress, bending strength, or tooth root failure
- Contact ratio, backlash, or mesh quality
- PLA‑specific limits for printed gears
- Whether a MiniClaw gear train matches BigClaw reference performance
- Whether a gear train is printable on Prusa‑class FDM machines
- Whether a gear pair will bind, skip, or wear prematurely

Do not use this skill for:

- General DFM questions (use the MiniClaw DFM Check)

- Jaw‑arm bending or structural analysis

- Supplier gear sourcing questions

## Workflow

1. **Identify the gear type.** Spur, helical‑approximation spur, idler, pinion, compound gear, or rack.
    Different types have different stress and contact‑ratio constraints.

2. **Check Lewis Bending Stress.** Compute or estimate Lewis stress using the Lewis stress equation. 
    Compare against PLA interlayer bending limit (≈ 18–22 MPa for printed teeth).
    Flag any design where:
    Tooth width < 5 mm for MiniClaw torque levels
    Module < 0.8 for load‑bearing gears
    Stress ratio > 0.6 of PLA limit (safety factor < 1.7)

3. **Check Hertzian contact stress.** 
    Printed PLA gears pit early if contact stress exceeds ~35–40 MPa.
    Flag:

    Very small pinions (≤10 teeth)

    High torque on small‑module meshes

    Narrow face widths (<4 mm)

4. **Check contact ratio.** Target contact ratio ≥ 1.4 for smooth operation.
    Flag:

    Undercut pinions

    Incorrect addendum modification

    Non‑standard center distances without compensation

    Printed gears with poor tooth fidelity (layer artifacts reduce effective contact ratio)

5. **Check backlash and tolerance allowances.** Per MiniClaw printed‑gear guidance:

    Add +0.10 to +0.20 mm backlash allowance for FDM variability

    Center‑distance tolerance ±0.15 mm typical
    Flag:

    Zero‑backlash designs

    Tight center‑distance constraints without adjustability

Gears intended to run dry without clearance

6. **Check print orientation and tooth fidelity.**   Per ACME gear print guidelines:

    Print gears flat so teeth lie in‑plane

    Avoid printing gears on‑edge (interlayer shear failure)
    Flag:

    Tooth tips aligned with layer lines

    Overhangs on modified tooth profiles

    Thin hubs (<3 mm) or spokes that cause warping

7. **Compare against BigClaw reference gear trains.** Use BigClaw’s validated gear sets as benchmarks:

    Module 1.0 spur gears

    Minimum 12‑tooth pinion

    –7 mm face width

    Contact ratio 1.45–1.55
    Flag deviations unless justified by load reduction or speed increase.

8. **Summarize findings.** 
    For each gear pair: PASS / FLAG / FAIL  
    Include:

    Stress margin

    Contact ratio

    Backlash adequacy

    Printability

    BigClaw comparison

## What to flag
  Lewis stress above PLA interlayer limit — risk of tooth‑root failure

  Contact ratio < 1.4 — noisy, skipping, or intermittent contact

  Pinions ≤10 teeth — undercut + high stress concentration

  Face width < 4 mm — insufficient load capacity

  Backlash not included — FDM prints will bind

  Gears designed to print on‑edge — interlayer shear failure

  Center distances without tolerance allowance — binding or excessive slop

  Non‑standard tooth profiles without justification — unpredictable mesh behavior

## What NOT to do

- Do not approve a gear train without checking both Lewis and Hertzian stress.

- Do not assume bulk PLA strength equals printed tooth strength.

- Do not recommend zero‑backlash designs for FDM gears.

- Do not ignore BigClaw reference values — they represent validated load cases.

- Do not rely on slicer‑generated tooth compensation — adjust CAD geometry instead.
