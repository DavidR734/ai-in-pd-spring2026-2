# MP5 — Final Team Presentation

**Worth:** 300 points (the single largest assessment of the quarter)
**Team:** same as MP4 Part B
**Window:** Fri May 29 (kickoff, same day MP4 Part B is due) through Thu Jun 4 (presentation day)
**Hard deadline:** slide deck and final repo state due by **11:59 PM the night before your team's session** (Mon Jun 1 for any Tuesday presenters; Wed Jun 3 for Thursday presenters). Grading is live — what runs in the room is what gets scored.

---

## When does our team present?

- **Default presentation day:** Thursday June 4 (Session 20, last day of instruction).
  All teams should plan for Thursday unless they need a conflict slot.
- **Alternative slot:** Tuesday June 2 (Session 19). Available for teams
  with a Thursday conflict — just let the instructor know on Slack. Late
  requests are fine, even day-of.
- **Slot length:** 20 minutes per team (15 min presentation + 5 min Q&A).
- **Attendance:** Whichever day your team presents, you're strongly
  encouraged to attend the other session as audience — the other teams'
  decks are part of how we close out the quarter together.

---

## Where to put everything

All MP5 artifacts live in the **team repo** under `MP5/`:

```
<team-repo>/
├── MP5/
│   ├── slides.pdf                    (the deck you'll present from — PDF, not editable)
│   ├── final_design/                 (CAD or sim, drawings or annotated screenshots, parts list, assembly notes)
│   ├── trust_ledger_final.md         (updated post-Part B)
│   ├── demo/                         (demo files, fallback video, instructions)
│   └── README.md                     (team roster, tools used, demo instructions)
```

The repo URL goes on Canvas, submitted by every team member.

---

## What to use the support materials for

You'll find four support files in this folder:

| File | Use it to... |
|------|--------------|
| `MP5_Presentation_Brief.docx` | Read first. Jordan's fifth memo — the in-world framing for what you're presenting and to whom. |
| `MP5_Pillar_Narrative_Worksheet.md` | Fill in **before building slides**. Forces the team to settle on the story together so the deck has one spine, not five. Not graded as a separate artifact. |
| `MP5_Self_Assessment.md` | Run through 24 hours before presenting. Catches the "we forgot to upload the slide deck" class of mistake. |
| `MP5_Slide_Outline_Optional.md` | Optional starting structure if the team wants one. Skip it if you have a better deck shape. |

The official rubric and timeline live in
`MP5_Final_Team_Presentation.docx` (the Canvas assignment document).

---

## About the live demo

The demo is required and must **move** — a physical 3D-printed prototype
operated in front of the class, OR a dynamic CAD/sim that actually runs
(assembly motion in CAD, Rapier playback, video of the printed mechanism
working). A static rendering does not count.

The demo also needs to include **at least one live MCP tool call or
function call** on a real engineering question relevant to your design —
that's how Tools & Integration shows up during the presentation. Run it
back-to-back with the prototype/sim or weave it in; what matters is that
the audience sees the tool actually called, on something real.

Graded on whether it runs, not on whether the answer matches a golden
output. Have a fallback — a recorded video of the demo running on your
home setup is acceptable insurance.

---

## The wrong-AI moment

Jordan's memo asks for it explicitly: pick one moment where the AI was
confidently wrong and your team caught it. Tell that story directly in
the deck.

This isn't a gotcha — it's the thing the broader product team will
learn the most from. Everyone in that room is figuring out how to use
these tools responsibly. You have nine weeks of evidence. Show one
piece of it.

If the team genuinely cannot remember a wrong-AI moment, that's worth
investigating — go back through your notebooks, transcripts, MCP logs,
and centaur-loop entries from MP1 through Part B. There is one in
there. Find it.

---

## This is a portfolio, not a pitch

The honest story always lands better than the polished one. The team
that says "we cut our jaw-opening target from 50 mm to 40 mm because
we couldn't reconcile the gear ratio with the transmission angle band"
earns more credit than the team that quietly hits 40 mm and pretends
50 mm was always the goal.

You've spent nine weeks producing evidence. Stand on it.

---

## Help

- Questions about scope, format, or the schedule: Slack `#mp5` or
  office hours.
- Lost the original Jordan Chen design brief: it's in your MP1 repo
  (`MP1/Part B/MP1_PartB_Design_Brief.docx`).
- Demo logistics (cables, projector, room layout): test the projector
  with your laptop during the Tuesday June 2 working session, or arrive
  ~15 minutes before your presentation day. Don't leave projector setup
  as a day-of-Thursday discovery. (Wed Jun 3 is the submission deadline
  for Thursday presenters, so the Tuesday session is your last test window.)

---

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

### Prerequisites

- Python 3.8+
- `numpy` and `matplotlib` installed (`pip install numpy matplotlib`)

### Running the dynamic simulation

```bash
cd MP5/demo
python3 linkage_simulation.py
```

This opens an animated window showing Haben's four-bar linkage sweeping from −50° to +50°, with real-time display of jaw displacement and transmission angle.

### Running the live tool call

```bash
cd MP5/demo
python3 transmission_angle_check.py
```

This computes and compares transmission angles for:
1. Haben's design (L3=29) — in band, 21.3° margin
2. Perturbed geometry (L3=32) — margin changes
3. David's design (L1=12, L2=26) — 25 mm jaw opening, 22° margin

### Fallback

If the animation doesn't work on the projector:
1. Run `transmission_angle_check.py` in a terminal (text output only)
2. Show pre-generated plots from `MP4/Part B/plots/`
3. Play pre-recorded video of the simulation (record before presentation day)

---

## Artifact Index

| Artifact | Path |
|---|---|
| Slide deck (PDF) | `MP5/slides.pdf` *(team to create and upload)* |
| Design summary + parts list | [`MP5/final_design/design_summary.md`](final_design/design_summary.md) |
| Final trust ledger | [`MP5/trust_ledger_final.md`](trust_ledger_final.md) |
| Demo plan | [`MP5/demo/demo_plan.md`](demo/demo_plan.md) |
| Linkage simulation | [`MP5/demo/linkage_simulation.py`](demo/linkage_simulation.py) |
| Transmission angle tool | [`MP5/demo/transmission_angle_check.py`](demo/transmission_angle_check.py) |
| Pillar narrative worksheet | [`MP5/MP5_Pillar_Narrative_Worksheet.md`](MP5_Pillar_Narrative_Worksheet.md) |
| Self-assessment checklist | [`MP5/MP5_Self_Assessment.md`](MP5_Self_Assessment.md) |
| Slide outline | [`MP5/MP5_Slide_Outline_Optional.md`](MP5_Slide_Outline_Optional.md) |
| MP4 Part B artifacts | [`MP4/Part B/`](../MP4/Part%20B/) |
| MP4 Part B README | [`MP4_PartB_README.md`](../MP4_PartB_README.md) |
