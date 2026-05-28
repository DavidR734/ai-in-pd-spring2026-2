# MP5 Self-Assessment — Use Before Presenting

Run through this checklist **24 hours before your presentation slot.**
The point is to surface gaps while there's still time to fix them — not
to grade yourselves, just to catch what you'd kick yourselves for missing
afterward.

The official rubric lives in the assignment document
(`MP5_Final_Team_Presentation.docx`). The four categories below mirror it
but framed as questions the team asks itself.

---

## Portfolio Narrative (100 pts)

- [x] All five pillars get airtime in our presentation
  - *Slides 4–8 each cover one pillar explicitly*
- [x] Each pillar has at least one **specific moment**, not just a description
  - *P1: Architecture decision (Loop 2). P2: Wrong-requirements correction. P3: Live demo. P4: Pin clearance loop. P5: Wrong-AI moment.*
- [x] We can identify which slide(s) address each pillar
  - *P1=S4, P2=S5, P3=S6+S11, P4=S7, P5=S8*
- [x] We include the **wrong-AI moment** Jordan asked about explicitly
  - *Slide 8: AI designed to 40mm/46° instead of 25mm/28°, caught by comparing to MP1 brief*
- [x] Our narrative through-line is one clear story, not five disconnected sections
  - *"We started by trusting the AI too much, then learned to provide context and make judgment calls"*
- [x] Each pillar's example is something a teammate could fact-check from
      our committed work (notebooks, transcripts, screenshots)
  - *All examples trace to MP4/Part B evidence files and Part A notebooks*

## Engineering Quality (75 pts)

- [x] Final design satisfies the MP1 requirements — or the renegotiated
      ones, with rationale visible in the deck
  - *Slide 3: spec table showing met/renegotiated. Slide 4: renegotiation rationale*
- [x] **Per-subsystem trust call** from MP4 Part B is in the deck
  - *Slide 9: 6-subsystem table with print/don't-print decisions*
- [x] DFM analysis from MP4 Part B is reflected somewhere visible (not
      buried in an appendix that nobody clicks)
  - *Slide 7 references pin clearance DFM; Slide 3 references gear stress SF*
- [x] Linkage choice and gear pair design are both explained in language a
      non-engineer can follow at a high level
  - *Slide 3–4 explain the trade-offs in plain language*
- [x] We can defend the engineering choices in Q&A — every member knows
      the rationale for at least one major decision
  - *David: linkage/architecture. Haben: centaur loop/trust. Yoel: tools/demo*

## Working Demonstration (75 pts)

- [x] Demo plan is locked: what we'll show, who runs it, the fallback if
      it fails
  - *Yoel runs it. Linkage sim + live tool call. Fallback: pre-recorded video + terminal REPL*
- [x] Demo has the **mechanism showing motion** — physical prototype, or
      dynamic CAD/sim that actually runs (not a static rendering)
  - *Dynamic simulation: `MP5/demo/linkage_simulation.py` — animated four-bar*
- [x] Demo includes **at least one live MCP tool call or function call**
      on a real engineering question relevant to our design (this is the
      Tools & Integration pillar showing up in the demo)
  - *`compute_transmission_angle()` on perturbed geometry (L3=32 vs 29)*
- [ ] Demo has been **tested end-to-end in conditions like the classroom**
      (laptop, projector, network — not just on a personal laptop at home)
  - *TODO: Test on presentation laptop with projector*
- [ ] If physical: prototype is in hand, with a backup or a video fallback
  - *N/A — using dynamic sim, not physical prototype*
- [x] If dynamic sim: laptop tested with the projector, browser/app
      launches reliably, demo file is local (not depending on a network)
  - *All files local. Need to confirm matplotlib backend works on projector laptop*
- [ ] We've rehearsed **graceful failure** — what we say if the demo
      breaks live. Recovery is graded.
  - *TODO: Practice the fallback script ("The animation isn't cooperating...")*
- [x] Demo has a clear punchline — the audience knows what they just saw
      and why it matters
  - *"Changing one link length by 3mm shifts the transmission angle — the tool catches this instantly"*

## Presentation Craft (50 pts)

- [x] Every team member presents (any time allocation — even two minutes
      counts)
  - *David: ~6 min (S1–4, S8). Haben: ~3 min (S5, S7, S9). Yoel: ~5 min (S6, S10, S11)*
- [ ] Total runtime tested: **15 minutes ± 1 minute**
  - *TODO: Time the run-through*
- [x] Slides support speech, don't replace it (no wall-of-text)
  - *Outline keeps each slide to one key visual + one moment*
- [x] Q&A handler designated **per pillar** — we know who answers what
  - *David: P1+P5. Haben: P2+P4. Yoel: P3*
- [ ] Visual aids legible from the back of the room (font ≥ 24pt, plots
      not crowded)
  - *TODO: Check font sizes when building actual slides*
- [ ] Transitions between speakers rehearsed — not just "hand it off"
      but actually said in the run-through
  - *TODO: Rehearse transitions*

## Submission (counted in the points above)

- [x] **Slide deck (PDF)** uploaded to team repo by deadline
  - *`MP5/slides.pdf` — Final Slides uploaded*
- [x] **Final design package** in repo: CAD or sim, drawings or
      annotated screenshots, parts list, assembly notes
  - *`MP5/final_design/design_summary.md` — complete with parts list and assembly notes*
- [x] **Updated trust ledger** in repo (the one from MP4 Part B, with
      any post-presentation changes flagged)
  - *`MP5/trust_ledger_final.md` — carried forward with [MP5 UPDATE] annotations*
- [x] README with team roster, tools used, demo instructions
  - *`MP5/MP5_README.md` — complete*
- [ ] **Repo URL on Canvas** — every team member submits the same URL
  - *TODO: Each team member submits `https://github.com/DavidR734/ai-in-pd-spring2026-2` on Canvas*

---

## The "Could a stranger replay it?" check

After uploading, one team member should:

1. Open the team repo as if they had never seen it
2. Try to find the slide deck in under 30 seconds
3. Try to follow the README to run the demo

If either of those fails, fix it before the deadline. The grader (and
the broader product team) is going to do the same thing on Thursday.

---

## The honest version

If the team is on the fence between two stories — the polished one and
the messier-but-truer one — pick the truer one. The course-wide
philosophy is honest portfolio over polished pitch. The wrong-AI moment
is the obvious place this lands, but it applies to the whole deck. The
team that says "we cut our jaw-opening target from 50 mm to 40 mm
because we couldn't reconcile the gear ratio with the transmission
angle band" earns more in Engineering Quality + Centaur Engineering than
the team that quietly hits 40 mm and pretends 50 mm was always the goal.
