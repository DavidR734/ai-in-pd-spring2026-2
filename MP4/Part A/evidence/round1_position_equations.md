# Round 1 — AI Interaction: Position Equation Derivation

**Date/time:** 2026-05-19 22:15  
**Host:** Copilot agent mode in VS Code; MiniClaw skill loaded from MP3 stack

## Prompt

> I'm designing a parallelogram four-bar linkage for the MiniClaw gripper
> (one side), with L1 = L3 = 12 mm, L2 = L4 = 26 mm, O4 = (0, 12).
> My MP1 design targets ~25 mm total jaw opening (12.5 mm per side).
> Derive the position equations using the two-circle intersection method
> so I can compute the finger tip position at any input angle. The tip
> extends 22 mm past joint B along the coupler direction.

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
world frame and gives parallel jaw motion. The starter code's pitfall
note explicitly warns about this distinction.
