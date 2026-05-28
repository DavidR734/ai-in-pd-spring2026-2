# Evidence — Loop 3: DFM and Pin Clearance Review

**Date:** 2026-05-26
**Lead:** David Ricciotti
**AI tool:** Devin (Cognition AI) — session URL in PR description

## Prompt

> Review the DFM checklist for the updated design. In particular, the
> pin clearance was flagged as borderline — what bore diameter gives a
> reliable sliding fit after FDM tolerance?

## Context provided

- 20T gear at m = 1.0 (new Architecture A design)
- Existing pin spec: Ø3.0 mm pin in Ø3.20 mm bore
- MP1 FDM tolerance: holes print ~0.10 mm undersize, pins ~0.10 mm oversize

## AI output — Pin clearance analysis

| Bore Ø (mm) | Designed clearance | FDM offset | Post-FDM clearance | Verdict |
|---|---|---|---|---|
| 3.20 | 0.20 mm | −0.20 mm | 0.00 mm | Borderline interference |
| 3.30 | 0.30 mm | −0.20 mm | 0.10 mm | Tight sliding fit |
| **3.40** | **0.40 mm** | **−0.20 mm** | **0.20 mm** | **Reliable sliding fit** |

Also computed: Lewis bending stress for 20T gear
- σ = 11.7 MPa at nominal (0.3 N·m), SF = 2.14
- σ = 19.5 MPa at max hand torque (0.5 N·m), SF = 1.28

## Team decision

- Bore increased to Ø3.40 mm across all 10 rotating joints
- No post-processing (reaming) required
- 20T Lewis stress margins confirmed adequate
