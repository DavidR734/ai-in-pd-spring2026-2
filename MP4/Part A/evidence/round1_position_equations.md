# Round 1 — AI Interaction: Position Equation Derivation

**Date/time:** 2026-05-19 22:15  
**Host:** Devin AI assistant (this session)

## Prompt

> I'm designing a four-bar linkage for the MiniClaw gripper (one side).
> I'm using a parallelogram configuration with L1 = L3 = 12 mm (ground/coupler)
> and L2 = L4 = 26 mm (input/output cranks), with the output ground pivot
> at (0, 12) directly above the input ground pivot at the origin.
> The input angle sweeps from 0° to 46°.
>
> Please derive the position equations using the two-circle intersection
> method so I can compute the finger tip position at any input angle.
> The tip extends 22 mm past joint B along the coupler direction.

## AI Response Summary

The AI correctly derived the two-circle intersection approach:

1. Joint A = O2 + L2 × (cos θ, sin θ) = (26 cos θ, 26 sin θ)
2. Joint B is the intersection of:
   - Circle of radius L3 = 12 centered on A
   - Circle of radius L4 = 26 centered on O4 = (0, 12)
3. The two-circle intersection formula:
   - d = |A − O4|
   - a = (d² + L3² − L4²) / (2d)
   - h = √(L3² − a²)
   - Foot of perpendicular: F = A + a × (O4 − A) / d
   - B = F ± h × perpendicular direction (branch selection)
4. For the parallelogram, use branch = −1 to get B on the correct side.
5. Tip = B + 22 × (coupler direction from A to B, normalized).

The AI also confirmed that for a parallelogram, B = A + (O4 − O2)
identically, which serves as a useful sanity check.

## Engineering Assessment

The derivation was correct and matched the approach in the matplotlib
starter notebook. The AI correctly identified the branch selection issue
and the parallelogram identity. One point of pushback: the AI initially
suggested extending the tip along the output crank direction (O4→B),
which would cause the finger to swing in an arc. I corrected this to use
the coupler direction (A→B), which for a parallelogram is fixed in the
world frame and gives parallel jaw motion.
