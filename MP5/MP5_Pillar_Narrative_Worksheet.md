# MP5 Pillar Narrative Worksheet — Team Ricciotti-Berhe-Tesfatsion

For each pillar, answer in 3–5 sentences. The answers become the spine of
your presentation — slides illustrate, the narrative carries. Build this
worksheet first, then build slides; resist the temptation to start in
PowerPoint.

This worksheet is **not submitted as a separate artifact**. It exists so
the team thinks the story through together before splitting up the deck.

---

## Pillar 1: Goal & Direction

**MP1 starting requirements:**
> The Jordan Chen design brief asked for a MiniClaw gripper to compete with Hiwonder's BigClaw at RobotExpo 2026. Envelope: 92 × 46 × 55 mm. Jaw opening: ≥ 40 mm. Thumb-wheel turns: 2–3 from open to closed. Grip force: 5–8 N. Material: FDM PLA on ACME's Prusa MK4S. Part count target: < 15 parts. Cost: < $3 per unit at 500-unit scale.

**Final requirements:**
> Our unified MP4 design meets the 40 mm jaw opening target exactly (40.13 mm via Haben's linkage). The transmission angle stays within the 40°–140° workable band with 21.3° margin. The thumb-wheel turn count dropped from the 2–3 target to 0.28 turns — a deliberate trade-off we accepted. Part count is 25 (above the < 15 target, but the brief acknowledged this was aggressive for a four-bar + gear train design). The 92 × 46 × 55 mm envelope is respected, with the gear pair occupying only 3.2% of housing volume.

**What changed and why:**
> The biggest renegotiation was the thumb-wheel turn count. The MP1 brief asked for 2–3 turns; our Architecture A single spur pair delivers 0.28 turns. We accepted this because the alternative — a compound spur train (Architecture B) with N=16 — had center distances summing to 126 mm, exceeding the 92 mm housing width. Switching to Architecture A dropped center distance to 20 mm, part count from 29 to 25, and eliminated the #1 packaging risk. David's original parallelogram linkage (25 mm jaw opening) was cut in favor of Haben's crossed-branch design (40 mm) because meeting the jaw opening target took priority over the compact envelope.

**Strongest example moment:**
> The architecture decision in Centaur Loop 2. The team asked Devin to list all decision options with trade-offs. The AI showed that Haben's wider 100° sweep reduced N_needed from 32 to 9, making Architecture A viable. The team chose simplicity over the turn-count spec — this was a deliberate engineering renegotiation, not an oversight. We documented the trade-off explicitly: "0.28 turns may feel too fast for precise gripping" was flagged as an open ergonomic question for MP5.

---

## Pillar 2: Context Management

**Where context saved you:**
> In MP4 Part A, Devin initially designed David's linkage with a 40 mm jaw opening target and 0°–46° input range — confidently wrong parameters. When David provided his MP1 Part B brief and MP3 Part B evidence documents, the AI corrected to the actual 25 mm target with a 0°–28° range. Without that MP1/MP3 context, the design would have been built on incorrect requirements. Similarly, Yoel's MP3 gear DFM skill (built on ACME corpus documents ACME-ENG-001, ACME-MFG-002) confirmed that our gear face width (8 mm) exceeds the 5 mm minimum and our safety factor (2.14) passes the SF ≥ 2.0 threshold — grounded in project-specific data, not generic PLA properties.

**Where context was missing:**
> Haben's repo was initially private (403 Forbidden), so the first round of Part B integration couldn't reference his MP3 Part B data (ACME press-fit tolerances, BigClaw teardown dimensions, jaw arm lessons). Once the repo was made public, we extracted critical data: ACME-MFG-004 press-fit tolerances (0.10–0.15 mm structural), BigClaw reference dimensions (crank=32, coupler=28, jaw=45, ground=38 mm), and the SF ≥ 2.0 recommendation for printed gears. This data changed how we wrote the DFM checklist and trust assessment. Yoel's MP4 Part A was submitted late as a completed package — his gear-and-connecting-rod four-bar (24 mm jaw opening, μ=57°–119°) confirmed the team's selection of Haben's design as the only candidate hitting 40 mm.

**What your team learned about managing context across MPs:**
> Context that isn't in the AI's window doesn't exist to the AI. The single most impactful thing we did was feeding Devin the MP1 brief and MP3 evidence documents — that one action corrected the entire design basis. A junior engineer onboarding should learn: always provide the project requirements document before asking for design work. The AI will confidently build on wrong assumptions if you don't.

---

## Pillar 3: Tools & Integration

**Your team's stack — final form:**
> Devin (Cognition AI) as the primary AI assistant — used for all Part A notebook completion, Part B template integration, comparison plot generation, drive-train sketch creation, Lewis stress analysis, and DFM tolerance calculations. GitHub for version control (12 PRs across the project). Haben used Copilot agent mode in VS Code for his Part A work. Yoel built a MiniClaw gear DFM review MCP skill with a `query_miniclaw_rag` server backed by the ACME corpus. David's MP3 work used Copilot agent mode for gear CAD iteration. matplotlib for generating comparison plots and the drive-train sketch programmatically.

**Live demo plan:**
> (1) Dynamic simulation of Haben's four-bar linkage showing jaw motion from −50° to +50° input angle — the audience sees the jaw opening from 0 to 40 mm and closing back. The simulation highlights the transmission angle staying in the workable band throughout. (2) Live MCP tool call: run `compute_transmission_angle()` on a perturbed geometry (e.g., change L3 from 29 mm to 32 mm) and show that the transmission angle drops below the 40° floor — demonstrating why the team's chosen dimensions matter and how the tool catches bad geometry in real time.

**What you'd build differently if starting over:**
> We would set up a shared team repo from Day 1 of MP4, not after Part A was already done in individual repos. The cross-repo integration (cloning Haben's repo, cloning Yoel's repo, extracting data) added friction that a single shared workspace would have eliminated. We would also build the MCP tool call for transmission angle checking earlier — having it as a live tool during the linkage selection discussion (Loop 1) would have made the comparison more interactive.

---

## Pillar 4: Centaur Engineering

**Strongest centaur loop:**
> Loop 3 — DFM and Pin Clearance Review. David asked Devin to review the DFM checklist, specifically the pin clearance spec (Ø3.0 mm pin in Ø3.20 mm bore). The AI calculated that FDM tolerance (−0.10 mm on holes, +0.10 mm on pins) would eat all 0.20 mm of designed clearance, leaving 0.00 mm — borderline interference. The AI proposed Ø3.40 mm bore (0.40 mm designed → 0.20 mm post-FDM). Neither the human alone (who hadn't done the tolerance stack) nor the AI alone (which needed the FDM tolerance assumptions from MP1) would have caught this — the combination of David's project-specific FDM data and Devin's systematic calculation produced an actionable design change across all 10 rotating joints.

**What each side contributed:**
> The AI contributed: systematic calculation of clearance stacks across multiple bore diameters, Lewis bending stress analysis for the 20T gear (σ = 11.7 MPa, SF = 2.14), programmatic generation of comparison plots and drive-train sketches, and consistent formatting across 6 Part B templates. The human contributed: project requirements (MP1 brief, MP3 evidence), team decisions (linkage selection, architecture choice, bore increase), engineering judgment on trade-offs (accepting 0.28 turns, choosing snap-fit over screws despite PLA brittleness), and catching the AI's initial wrong parameters (40 mm/46° vs. 25 mm/28°). The combination mattered because the AI could process data faster than the team could manually, but the team had to provide the right context and make the judgment calls.

**Where it failed:**
> The AI initially designed David's Part A linkage with completely wrong parameters (40 mm jaw opening, 0°–46° input range) because it didn't have the MP1/MP3 context. It was confidently wrong — the design looked internally consistent, the math checked out, and the AI never flagged that it was guessing the requirements. The team caught it only because David compared the output against his own MP1 brief. This is the wrong-AI moment. A second failure: the AI's initial compound train (Architecture B) had center distances summing to 126 mm — it didn't flag that this exceeded the 92 mm housing until the team explicitly asked about packaging.

---

## Pillar 5: Evaluation & Trust

**The wrong-AI moment** *(the story Jordan asked for explicitly):*
> In MP4 Part A, Devin designed David's four-bar linkage targeting 40 mm jaw opening with a 0°–46° input range. The AI produced a complete, internally consistent design — position equations, transmission angle analysis, motion plots, hand calculations. Everything checked out mathematically. But the claim was wrong: David's MP1 Part B brief specified a 25 mm jaw opening target, and his MP3 Part B evidence showed a 0°–28° input range. David caught it by comparing the AI's output against his original design brief. The fix cascaded: link lengths changed from 40/20 to 12/26, input range narrowed from 46° to 28°, displacement dropped from 20.3 mm to 12.5 mm. The mechanism of catching it was simple — the human knew the requirements and the AI didn't. This directly illustrates why context management is not optional.

**Per-subsystem trust call:**
> From MP4 Part B trust assessment — Subsystem 1 (Linkage): **would print** — kinematics verified by three independent paths (code, hand calc, centaur loop), transmission angle margin is 21.3° above the floor. Subsystem 2 (Drive Train): **would print with reservation** — geometry and tooth stress verified (SF = 2.14), but backlash, mesh quality, and ergonomic feel of 0.28 turns are untested. Subsystem 6 (Pins): **would print with reservation** — bore spec designed for FDM tolerance, but cycle life unknown. Subsystems 3–5 (Jaw Arms, Housing, Input Wheel): **would NOT print** — no CAD exists. These are the MP5 gap.

**What you would verify before mass production:**
> Bench test the printed 20T gear pair under realistic load — our Lewis analysis gives SF = 2.14 at nominal, but PLA creep under sustained load and interlayer fatigue at the tooth root are failure modes Lewis doesn't capture. Print one complete linkage assembly and measure actual pin-bore clearance across all 10 joints — FDM dimensional variability means some joints may bind while others are loose, even with the 0.40 mm designed clearance. Test the 0.28-turn operation with actual users — the ergonomic question of whether direct-drive feels controllable for precision gripping can only be answered with a physical prototype.

---

## Narrative Through-Line

**The story of your MiniClaw — 2 to 3 sentences:**

> We started by trusting the AI too much — it confidently designed to wrong requirements because we hadn't given it our project context. Once we fed it the real specs, the AI became a powerful calculation engine, but every major decision (which linkage, which architecture, which bore diameter) was a human judgment call. The MiniClaw we present is honest: the linkage and drive train are analytically solid, but three subsystems have no CAD and the ergonomic question is unanswered — we know exactly what we'd verify next.

---

## Sanity Check Before Building Slides

Before you open PowerPoint or Slides, the team can read this worksheet
top-to-bottom and:

- [x] Each pillar's strongest example is concrete (a moment, not a
      generality)
- [x] The wrong-AI moment is specific enough that someone could fact-check it
- [x] The narrative through-line is one sentence the team can say without
      reading from the page
- [ ] Every team member can speak to at least one pillar from memory
