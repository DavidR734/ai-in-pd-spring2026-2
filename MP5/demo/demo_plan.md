# MiniClaw Live Demo Plan

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion
**Demo operator:** Yoel Tesfatsion
**Duration:** ~3 minutes

---

## Demo Overview

Two-part demo: (1) dynamic simulation of the four-bar linkage in motion, and (2) a live MCP tool call / function call on a real engineering question.

---

## Part 1: Dynamic Linkage Simulation (~2 min)

**What it shows:** Haben's four-bar linkage (L1=47, L2=20, L3=29, L4=23) sweeping from −50° to +50° input angle, with the jaw opening from 0 to 40 mm and closing back.

**How to run:**
```bash
cd MP5/demo
python3 linkage_simulation.py
```

**What the audience sees:**
- Animated four-bar linkage with all four links visible
- Jaw tip tracing its path
- Real-time display of: input angle, single-side displacement, transmission angle
- Transmission angle bar/indicator showing it stays in the 40°–140° band
- The jaw opening reaching 40 mm at full extension

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

If the live demo fails:
1. **Pre-recorded video** of the simulation running (record before presentation day)
2. **Static plots** from `MP4/Part B/plots/` as backup visuals
3. **Live Python REPL** — run the computation functions directly in a terminal if the animation fails

**Recovery script:** "The animation isn't cooperating with the projector, but let me show you the computation directly — [switch to terminal, run the function call]"

---

## Setup Checklist (day before)

- [ ] Test laptop → projector connection
- [ ] Verify Python + matplotlib + numpy are installed on presentation laptop
- [ ] Run `linkage_simulation.py` end-to-end on the presentation laptop
- [ ] Record fallback video of the simulation running
- [ ] Verify network is not required (all files are local)
- [ ] Have `compute_transmission_angle()` ready in a terminal/notebook
