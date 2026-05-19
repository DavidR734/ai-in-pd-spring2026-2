# Round 2 — AI Interaction: Transmission Angle Check

**Date/time:** 2026-05-19 22:35  
**Host:** Devin AI assistant (this session)

## Prompt

> For my parallelogram four-bar (L1=L3=12, L2=L4=26, O4=(0,12), range 0°–46°),
> what is the transmission angle at each end of the input range?
> Will the linkage stay within the 40°–140° workable band?
> If not, what geometry changes would fix it?

## AI Response Summary

The AI computed the transmission angle μ as the angle at joint B between
the coupler (B→A direction) and the output crank (B→O4 direction).

For this vertical parallelogram, the AI derived that:
- μ = arccos(sin θ) = 90° − θ (valid for θ in [0°, 90°])
- At θ = 0°: μ = 90° (ideal)
- At θ = 46°: μ = 44° (within the 40° floor)

The AI confirmed the linkage stays in band throughout the input range.
It suggested that if margin is needed, options include:
1. Reducing THETA_MAX slightly (e.g., to 44° gives μ_min = 46°)
2. Tilting the ground link away from vertical
3. Using a non-parallelogram four-bar (sacrificing pure parallel motion)

## Engineering Assessment

The μ = 90° − θ identity for a vertical parallelogram is mathematically
correct and easy to verify by hand. The AI nailed this one — the key
insight is that for a vertical ground link with equal-length opposite
sides, the transmission angle has a clean analytical form. My chosen
range (0°–46°) keeps μ_min = 44°, which is 4° above the 40° floor.
That's tight but acceptable for a desk-toy application where loads are
low. If the team's Part B gear ratio shifts the effective input range,
the margin could erode — that's a flag for the trust ledger.

## What Changed for Round 3

I was satisfied with the transmission angle behavior but wanted the AI
to help verify the displacement calculation and confirm the mechanism
fits the MiniClaw envelope. I also wanted to cross-check by asking the
AI to compute positions at three specific angles for the hand calc.
