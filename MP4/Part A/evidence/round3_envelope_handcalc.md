# Round 3 — AI Interaction: Envelope Check and Hand Calc Verification

**Date/time:** 2026-05-19 22:55  
**Host:** Devin AI assistant (this session)

## Prompt

> For my parallelogram four-bar (L1=L3=12, L2=L4=26, O4=(0,12),
> TIP_EXT=22, range 0°–46°):
>
> 1. Compute the finger tip position and single-side displacement at
>    θ = 0° (open), θ = 23° (mid), and θ = 46° (closed).
> 2. Does the mechanism fit within ~46 × 55 mm (one side of the
>    MiniClaw housing)?
> 3. Does the maximum displacement reach the 20 mm target for
>    40 mm total jaw opening?

## AI Response Summary

The AI computed three positions:

| θ_in | A (mm) | B (mm) | Tip (mm) | Disp (mm) | Total Jaw (mm) |
|------|--------|--------|----------|-----------|----------------|
| 0° (open) | (26.00, 0.00) | (26.00, 12.00) | (26.00, 34.00) | 0.0 | 0.0 |
| 23° (mid) | (23.93, 10.16) | (23.93, 22.16) | (23.93, 44.16) | 10.4 | 20.7 |
| 46° (closed) | (18.06, 18.71) | (18.06, 30.71) | (18.06, 52.71) | 20.3 | 40.6 |

Envelope check:
- Max horizontal extent: 26 mm at θ = 0° → fits within 46 mm ✓
- Max vertical extent: 52.7 mm at θ = 46° → fits within 55 mm ✓
- Maximum displacement: 20.3 mm → total jaw opening 40.6 mm ≈ 40 mm target ✓

## Engineering Assessment

The numbers check out. I verified the θ = 0° position by hand:
A = (26 cos 0°, 26 sin 0°) = (26, 0), B = (26, 12), tip = (26, 34).
The displacement formula for a parallelogram simplifies to
L2 × √(2 − 2 cos θ) = 26 × √(2 − 2 cos 46°) = 20.3 mm, confirming
the AI's answer. The envelope fit is tight vertically (52.7 mm vs.
55 mm budget = 2.3 mm margin) but acceptable for a 3D-printed prototype.

## Stack Notes

For these three rounds, I used Devin as my AI assistant. The stack
performed well for this type of analytical kinematics problem — the
two-circle intersection derivation was correct on the first try, and
the transmission angle analysis was handled cleanly. The main
correction I made was the tip-extension direction (coupler vs. output
crank), which is a common pitfall noted in the starter code. The stack
did not use an MCP server or RAG for these queries — the analysis was
based on standard four-bar kinematics that the AI handled from its
training data. For Part B integration, connecting the MCP server
with MiniClaw-specific context would likely improve design trade-off
discussions.
