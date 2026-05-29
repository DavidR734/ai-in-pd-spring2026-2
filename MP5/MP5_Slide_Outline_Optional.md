# MP5 Slide Outline — Team Ricciotti-Berhe-Tesfatsion

Based on the optional 12-slide structure. Content pulled from the Pillar
Narrative Worksheet and MP1–MP4 artifacts.

---

## Slide 1: Title (30 s) — *David*

**MiniClaw: From Wrong Requirements to Honest Design**

Team Ricciotti-Berhe-Tesfatsion | ME 493B | RobotExpo 2026

---

## Slide 2: The Brief (1 min) — *David*

**What Jordan asked for:**
- Compete with Hiwonder's BigClaw at RobotExpo 2026
- 92 × 46 × 55 mm envelope
- ≥ 40 mm jaw opening, 2–3 thumb-wheel turns
- 5–8 N grip force, FDM PLA, < 15 parts, < $3/unit at 500 units

*Visual: MP1 design brief header + BigClaw dimensional drawing side by side*

---

## Slide 3: Where We Ended Up (1 min) — *David*

**What we delivered:**

| Spec | Target | Actual |
|---|---|---|
| Jaw opening | ≥ 40 mm | 40.13 mm ✓ |
| Envelope | 92 × 46 × 55 | 92 × 46 × 55 ✓ |
| Turns | 2–3 | 0.28 ✗ (renegotiated) |
| Parts | < 15 | 25 (over) |
| Gear stress SF | ≥ 2.0 | 2.14 ✓ |

*Visual: drive train sketch + displacement comparison plot*

---

## Slide 4: Goal & Direction (1 min) — *David*

**The renegotiation story:**

We accepted 0.28 thumb-wheel turns instead of 2–3 because the compound spur train (N=16) had center distances summing to 126 mm — 34 mm over the housing width. Switching to a single spur pair (N=1) dropped center distance to 20 mm and part count from 29 to 25.

*Visual: Architecture B packaging failure (126 mm) vs. Architecture A (20 mm)*

**Moment:** Centaur Loop 2 — the AI showed that Haben's wider sweep made Architecture A viable. The team chose simplicity over the turn-count spec.

---

## Slide 5: Context Management (1 min) — *Haben*

**Where context saved us:**

The AI designed to wrong requirements (40 mm / 46° range) until David fed it the MP1 brief and MP3 evidence. One document upload corrected the entire design basis: link lengths changed, input range narrowed, displacement target dropped.

**Where context was missing:**

Haben's repo was private → 403 error. Once public, we extracted ACME press-fit tolerances, BigClaw teardown dimensions, and the SF ≥ 2.0 standard. Yoel's MP4 Part A was submitted late — his linkage (24 mm jaw, μ=57°–119°) confirmed Haben's design as the right selection.

*Visual: before/after parameter table showing the context correction*

---

## Slide 6: Tools & Integration (1 min) — *Yoel*

**Our stack:**
- **Devin** (Cognition AI): Part A notebooks, Part B templates, plots, sketches, stress analysis
- **Copilot agent mode**: Haben's Part A, David's MP3 gear CAD
- **MiniClaw gear DFM skill** (Yoel's MP3): MCP RAG server + ACME corpus
- **GitHub**: 12 PRs, version-controlled integration

**Live demo preview:** Dynamic simulation of Haben's linkage + live `compute_transmission_angle()` call on perturbed geometry

*Hands off to Slide 11 for live demo*

---

## Slide 7: Centaur Engineering (1 min) — *Haben*

**Strongest loop: Pin Clearance Review (Loop 3)**

David asked Devin: "What bore diameter gives a reliable sliding fit after FDM tolerance?"

- AI calculated: Ø3.20 bore → 0.00 mm post-FDM clearance (interference)
- AI proposed: Ø3.40 bore → 0.20 mm post-FDM (sliding fit)
- Neither side alone: David had the FDM tolerance data, the AI did the systematic stack calculation

**Result:** Bore increased across all 10 joints. No reaming needed.

*Visual: tolerance stack table from evidence/loop3_dfm_pin_clearance.md*

---

## Slide 8: Evaluation & Trust — The Wrong-AI Moment (2 min) — *David*

**The claim:** Devin designed David's linkage targeting 40 mm jaw opening with 0°–46° input range. Complete, internally consistent design — position equations, plots, hand calculations all checked out.

**The truth:** David's MP1 brief specified 25 mm jaw opening, 0°–28° range.

**How we caught it:** David compared the AI's output against his original design brief. The numbers didn't match. One document upload fixed everything.

**What it teaches:** The AI will confidently build on wrong assumptions if you don't provide the requirements document. Context management isn't optional — it's the difference between a correct design and a plausible-looking wrong one.

*Visual: screenshot/quote of the AI's original wrong parameters vs. the corrected ones*

---

## Slide 9: Per-Subsystem Trust (1 min) — *Haben*

| Subsystem | Flag | Print? |
|---|---|---|
| Linkage | Needs work | Yes — strongest analytically |
| Drive train | Needs work | Yes — SF 2.14, compact |
| Jaw arms | Unknown | No — no CAD |
| Housing | Unknown | No — no CAD |
| Input wheel | Unknown | No — no CAD |
| Pins | Needs work | Yes — test one joint first |

**Bottom line:** Not ready to print a complete gripper. Three subsystems are analytically solid; three have no CAD. Honest assessment.

---

## Slide 10: What We'd Do Differently (1 min) — *Yoel*

**One honest answer:**

Set up a shared team repo from Day 1. The cross-repo integration (cloning Haben's private repo, cloning Yoel's repo, extracting parameters) added friction that a single shared workspace would have eliminated.

Also: build the transmission angle MCP tool earlier. Having it live during linkage selection (Loop 1) would have made the comparison interactive instead of static.

---

## Slide 11: Live Demo (3 min) — *Yoel*

**Part 1:** Dynamic simulation — Haben's four-bar sweeping −50° to +50°, showing jaw opening reaching 40 mm, transmission angle staying in band.

**Part 2:** Live tool call — `compute_transmission_angle()` on perturbed geometry (L3=32 instead of 29). Shows the angle drops — tool catches bad geometry instantly.

*Run: `python3 MP5/demo/linkage_simulation.py` then `python3 MP5/demo/transmission_angle_check.py`*

**Fallback:** Pre-recorded video + static plots from MP4/Part B/plots/

---

## Slide 12: Q&A (5 min) — *All*

**Designated answerers:**
- Goal & Direction → David
- Context Management → Haben
- Tools & Integration → Yoel
- Centaur Engineering → Haben
- Evaluation & Trust → David

---

## Timing Budget

| Slide | Time | Cumulative |
|---|---|---|
| 1. Title | 0:30 | 0:30 |
| 2. Brief | 1:00 | 1:30 |
| 3. Where we ended up | 1:00 | 2:30 |
| 4. Goal & Direction | 1:00 | 3:30 |
| 5. Context Management | 1:00 | 4:30 |
| 6. Tools & Integration | 1:00 | 5:30 |
| 7. Centaur Engineering | 1:00 | 6:30 |
| 8. Wrong-AI Moment | 2:00 | 8:30 |
| 9. Trust Assessment | 1:00 | 9:30 |
| 10. What we'd do differently | 1:00 | 10:30 |
| 11. Live demo | 3:00 | 13:30 |
| 12. Q&A | 5:00 | 18:30 |
| Buffer | 1:30 | **20:00** |
