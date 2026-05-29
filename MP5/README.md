# MiniClaw — MP5 Final Team Presentation

## Team Roster

| Name | Role (MP5) | Responsibilities |
|---|---|---|
| David Ricciotti | Narrative lead | Slides 1–4, 8 (wrong-AI moment); Goal & Direction + Evaluation & Trust Q&A |
| Haben Berhe | Slides lead | Slides 5, 7, 9; Context Management + Centaur Engineering Q&A |
| Yoel Tesfatsion | Demo lead | Slides 6, 10, 11 (live demo); Tools & Integration Q&A |

---

## Tools Used

| Tool | What it did |
|---|---|
| Devin (Cognition AI) | Primary AI assistant — Part A notebooks, Part B template integration, comparison plots, drive-train sketch, Lewis stress analysis, DFM tolerance calculations, PR creation |
| GitHub Copilot (agent mode) | Haben's Part A notebook completion, David's MP3 gear CAD iteration |
| MiniClaw Gear DFM Skill (Yoel) | MCP RAG server querying ACME corpus (ACME-ENG-001, ACME-MFG-002) for gear DFM validation |
| matplotlib / numpy | Programmatic generation of comparison plots, linkage simulation, drive-train sketch |
| GitHub | Version control — 12+ PRs across the project lifecycle |

---

## Demo Instructions

### Option A: Pre-rendered simulation video (recommended for projector)

Play the video file directly — no dependencies needed:
```
MP5/demo/miniclaw_simulation.mp4
```
SolidWorks-style animation of Haben's four-bar linkage sweeping −50° to +50°, with real-time data panel showing jaw opening and transmission angle.

### Option B: Jupyter notebook on GitHub (click and view)

Navigate to [`MP5/demo/MiniClaw_Demo.ipynb`](demo/MiniClaw_Demo.ipynb) on GitHub. All outputs are pre-rendered — no code needs to run. Shows:
1. Six key linkage positions with SolidWorks-style rendering
2. `compute_transmission_angle()` tool call comparing 3 designs
3. Transmission angle comparison chart

### Option C: Live Python scripts (if running interactively)

**Prerequisites:** Python 3.8+, `numpy`, `matplotlib` (`pip install numpy matplotlib`)

```bash
cd MP5/demo
python3 linkage_simulation.py       # animated four-bar linkage
python3 transmission_angle_check.py  # tool call comparing designs
```

### Fallback

If video/animation won't play on the projector:
1. Open `MiniClaw_Demo.ipynb` on GitHub (browser only, no setup)
2. Run `python3 transmission_angle_check.py` in a terminal (text output)
3. Show pre-generated plots from `MP4/Part B/plots/`

---

## Artifact Index

| Artifact | Path |
|---|---|
| Slide deck (PDF) | [`MP5/slides.pdf`](slides.pdf) |
| Slide deck (PPTX source) | [`MP5/slides.pptx`](slides.pptx) |
| Design summary + parts list | [`MP5/final_design/design_summary.md`](final_design/design_summary.md) |
| Final trust ledger | [`MP5/trust_ledger_final.md`](trust_ledger_final.md) |
| Demo plan | [`MP5/demo/demo_plan.md`](demo/demo_plan.md) |
| Simulation video | [`MP5/demo/miniclaw_simulation.mp4`](demo/miniclaw_simulation.mp4) |
| Demo notebook | [`MP5/demo/MiniClaw_Demo.ipynb`](demo/MiniClaw_Demo.ipynb) |
| Linkage simulation (source) | [`MP5/demo/linkage_simulation.py`](demo/linkage_simulation.py) |
| Transmission angle tool | [`MP5/demo/transmission_angle_check.py`](demo/transmission_angle_check.py) |
| Pillar narrative worksheet | [`MP5/MP5_Pillar_Narrative_Worksheet.md`](MP5_Pillar_Narrative_Worksheet.md) |
| Self-assessment checklist | [`MP5/MP5_Self_Assessment.md`](MP5_Self_Assessment.md) |
| Slide outline | [`MP5/MP5_Slide_Outline_Optional.md`](MP5_Slide_Outline_Optional.md) |
| MP4 Part B artifacts | [`MP4/Part B/`](../MP4/Part%20B/) |

---

## Repository

**Repo URL (submit on Canvas):** `https://github.com/DavidR734/ai-in-pd-spring2026-2`

Each team member submits this same URL on Canvas.
