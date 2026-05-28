# MiniClaw Live Demo Plan

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion
**Demo operator:** Yoel Tesfatsion
**Duration:** ~3 minutes

---

## Demo Overview

Two-part demo: (1) pre-rendered SolidWorks-style simulation video of the four-bar linkage, and (2) a live MCP tool call / function call on a real engineering question.

---

## Part 1: Dynamic Linkage Simulation Video (~2 min)

**What it shows:** Haben's four-bar linkage (L1=47, L2=20, L3=29, L4=23) sweeping from −50° to +50° input angle, with the jaw opening from 0 to 40 mm and closing back.

**How to play:**
Simply open and play the video file — no Python or dependencies needed:
```
MP5/demo/miniclaw_simulation.mp4
```

**What the audience sees:**
- SolidWorks-style dark background with colored solid links
- Rounded link bodies with visible pin joints
- Jaw tip tracing its path (red trail)
- Real-time data panel showing: input angle, displacement, jaw opening, transmission angle
- Transmission angle bar with workable band indicator
- Color-coded margin warning (green/yellow/red)

**Punchline:** "This is Haben's linkage — it hits exactly 40 mm jaw opening while keeping the transmission angle 21° above the safety floor the entire time."

---

## Part 2: Live MCP Tool Call (~1 min)

**What it shows:** A live function call that answers a real engineering question about the design — demonstrating that the tools we built actually work on our geometry.

**Suggested call:** Compute transmission angle for a perturbed geometry.

```python
# Example: What happens if we change L3 from 29 mm to 32 mm?
result = compute_transmission_angle(
    L1=47, L2=20, L3=32, L4=23,  # L3 changed from 29 to 32
    O4=(47, 0),
    theta_range=(-50, 50)
)
print(f"Min μ = {result['mu_min']:.1f}°, Max μ = {result['mu_max']:.1f}°")
# Expected: transmission angle drops — may fall below 40° floor
```

**Punchline:** "When we change one link length by 3 mm, the transmission angle drops below the safety floor. This is why our chosen dimensions matter — and how the tool catches bad geometry in real time."

**Alternative call (if the above doesn't land well):**
```python
# What jaw opening do we get with David's linkage vs. Haben's?
david_disp = compute_finger_position(L1=12, L2=26, L3=12, L4=26, ...)
haben_disp = compute_finger_position(L1=47, L2=20, L3=29, L4=23, ...)
# Show 25 mm vs. 40 mm side by side
```

---

## Fallback Plan

The primary simulation is already a pre-rendered video — no live rendering dependencies. If video playback fails:
1. **Open in browser** — drag `miniclaw_simulation.mp4` into Chrome
2. **Static plots** from `MP4/Part B/plots/` as backup visuals
3. **Live Python REPL** — run `python3 transmission_angle_check.py` in a terminal

**Recovery script:** "Let me switch to the computation directly — [run transmission_angle_check.py in terminal]"

---

## Setup Checklist (day before)

- [ ] Test laptop → projector connection
- [ ] Verify `miniclaw_simulation.mp4` plays on presentation laptop (any video player)
- [ ] Have `transmission_angle_check.py` ready in a terminal (needs Python + numpy)
- [ ] Verify network is not required (all files are local)
