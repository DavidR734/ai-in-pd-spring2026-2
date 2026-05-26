# MP4 Part B — Gear Pair Design

**Team:** David Ricciotti, Haben Berhe, Yoel Tesfatsion
**Chosen linkage (see Linkage Comparison):** _[to be confirmed by team — pre-filled below assuming David's linkage]_
**Linkage input angle range:** from 0° to 28° *(from David's Part A design)*

---

This is the work that Part A explicitly deferred to the team. The drive
train sits between the thumb wheel input and the linkage input pivot —
it synchronizes the two sides (counter-rotation at the same rate) AND
sets the reduction between thumb wheel turns and linkage input angle.
The reduction and the linkage choice are coupled: if the chosen
reduction pushes the linkage outside its workable transmission angle
band, you fix one or the other.

A labeled sketch is enough — full production CAD on the drive train is
not required.

> "Gear pair" is short-hand. The actual hardware that does these two
> jobs is up to the team: a single spur pair, a compound (multi-stage)
> spur train, a worm + worm wheel, or a sync-only spur pair with a
> separate reduction element. A single spur pair is usually too small
> a ratio to handle 2–3 thumb-wheel turns alone (the envelope can't
> hold the tooth counts a one-stage 18:1 would need), so most teams
> end up at a compound train or worm. The worksheet below adapts.

---

## Ratio Convention (read this before filling anything in)

Everything below uses **overall reduction N**, defined unambiguously:

> **N = (thumb wheel angle range, deg) / (linkage input angle range, deg)**

N is a single dimensionless number ≥ 1 for a step-down (which is what
the MP1 brief asks for: 2–3 thumb-wheel turns into a small linkage
sweep). For a single spur pair with z₁ on the thumb-wheel side and z₂
on the linkage side, **N = z₂ / z₁**. For a compound train,
**N = (z₂/z₁) × (z₄/z₃) × …** — the product of per-stage ratios. For
a worm + worm wheel, **N ≈ z_wheel / (worm thread starts)**.

Use this one definition for every number on this page. Bigger N means
more reduction means more thumb-wheel turns per linkage degree.

---

## Architecture Choice

Pick one. The choice tells you which rows of the specs table to fill.

- [ ] **A. Single spur pair.** One pair of meshing spur gears does both
  jobs (sync + reduction). Simplest. Usually only feasible if the team
  accepts fewer thumb-wheel turns than the MP1 target — N values around
  18 don't fit a single spur pair in this envelope.
- [x] **B. Compound spur train (multi-stage).** Two or more spur stages
  in series, each contributing part of the reduction. Common solution
  when N ≳ 5 and the envelope can't hold one big gear.
- [ ] **C. Worm + worm wheel.** High reduction in one stage, with a 90°
  axis change. Compact for big N. Note: worm gears tend to self-lock
  and are harder to print well at small scale.
- [ ] **D. Sync-only spur pair (1:1) + separate reduction element.**
  A 1:1 spur pair couples the two sides for counter-rotation; the
  reduction lives elsewhere (lead-screw, friction wheel, separate
  reduction stage). State what the separate reduction element is.

**Why we chose this architecture (2–3 sentences):**
> A compound spur train provides the high overall reduction needed (~32:1) while keeping individual gear diameters within the 92 × 46 × 55 mm envelope. A single spur pair at N ≈ 32 would require an impractically large driven gear (~450 mm pitch diameter at m = 1.0). A worm gear is compact but harder to print reliably at this scale with FDM PLA and tends to self-lock, which would make the gripper feel stiff to operate. Two spur stages at ~4:1 each (from David's MP3 pinion design: 14T at m = 1.0) combined with a sync pair gives manageable gear sizes that fit the housing.

_[Team: confirm this architecture choice or adjust based on your discussion]_

---

## Drive Train Specifications

Fill in the row(s) that match your architecture. For a compound train,
add a row per stage. For a worm + wheel, fill the worm-stage row. For
the sync-only architecture, fill stage 1 with z_driver = z_driven so
the stage ratio is 1.0, and name the separate reduction element below.

### Spur stages

_[Pre-filled using David's MP3 Part B gear specs as the starting point. Stage 1 is from MP3 (14T pinion, m=1.0, 4:1). Stage 2 and sync stage need team confirmation.]_

| Stage | Module m (mm) | z_driver | z_driven | Stage ratio (z_driven / z_driver) | Center distance m × (z_driver + z_driven) / 2 (mm) | Face width (mm) |
|-------|---------------|----------|----------|------------------------------------|------------------------------------------------------|-----------------|
| 1 (thumb wheel → intermediate) | 1.0 | 14 | 56 | 4.0 | 1.0 × (14 + 56) / 2 = 35.0 | 8.0 |
| 2 (intermediate → linkage input) | 1.0 | 14 | 56 | 4.0 | 1.0 × (14 + 56) / 2 = 35.0 | 8.0 |
| 3 (sync pair: left ↔ right) | 1.0 | _[needs team decision]_ | _[same as driver — 1:1 for sync]_ | 1.0 | _[depends on tooth count]_ | 8.0 |

_[Note: Stage 1 specs are from David's MP3 Part B refinement: 14T pinion at module 1.0 mm, root fillet R0.60, bore Ø3.00 +0.20/−0.00 mm, hub OD Ø8.00 mm. Stage 2 reuses the same gear geometry. The sync pair is 1:1 to achieve counter-rotation. Team should confirm or adjust these specs.]_

### Worm stage *(if any)*

| Module m_n (mm) | Worm thread starts | Worm wheel z | Stage ratio (z_wheel / starts) | Center distance (mm) | Face width (mm) |
|------------------|--------------------|--------------|---------------------------------|----------------------|------------------|
| N/A — compound spur chosen | — | — | — | — | — |

### Separate reduction element *(Architecture D only)*

> N/A — Architecture B (compound spur train) chosen.

### Overall

| Parameter | Value |
|-----------|-------|
| Overall reduction N (product of stage reductions) | 4.0 × 4.0 × 1.0 = **16.0** _[team needs to verify this gives acceptable thumb-wheel turn count — see Rationale]_ |
| Drive-train bounding-box footprint (mm) | _[needs CAD/sketch — estimate ~70 × 40 × 12 based on center distances]_ |
| Packaging position relative to linkage | _[needs team sketch — behind the linkage ground pivots, within the housing base]_ |

> Typical FDM PLA values: module 1.0–1.5 mm for spur, ~1.0 for worm.
> z ≥ 12 for FDM spur gears; lower tooth counts have undercut issues
> and print poorly.

---

## Rationale

**Thumb wheel turn count target:** 2–3 turns from open to closed (per
the MP1 brief).

**Linkage input range (from David's Part A design):** from 0° to 28°
→ linkage sweep = 28°

**Reduction needed to hit the 2.5-turn target on this linkage:**
> N_needed = (thumb-wheel turns × 360°) / (linkage sweep, deg)
> = (2.5 × 360°) / (28°)
> = **32.1**

**Our overall reduction N (from the specs table):** 16.0 _(with two 4:1 stages + 1:1 sync)_

**Does our N match N_needed?** No.

> With N = 16, the 28° linkage sweep maps to 16 × 28° = 448° of thumb-wheel rotation = **1.24 turns** from open to closed. This is below the 2–3 turn target from MP1 — the gripper opens and closes faster than the brief requests, which could feel less precise but is mechanically simpler. Alternatives the team should consider:
> - **Accept 1.24 turns** — faster operation, fewer gear stages, simpler housing. May feel "snappy" rather than "precision-engineered."
> - **Add a third reduction stage** to hit N ≈ 32 (e.g., three 4:1 stages × 1:1 sync = N = 64, which overshoots; or use 3.2:1 per stage to get N ≈ 32.8). This adds complexity and another gear pair to print.
> - **Use a higher first-stage ratio** (e.g., 14T → 112T at m=1.0, giving 8:1 per stage → N = 64 at two stages — but 112T is Ø112 mm, too large for the 46 mm half-width).
> - **Increase the linkage input range** to reduce N_needed — but this compresses the transmission angle margin.
>
> _[Team must decide which trade-off to accept. The current N = 16 is a reasonable starting point if the team accepts ~1.2 turns instead of 2.5.]_

---

## Symmetry Arrangement

Both sides of the gripper share the drive train through some
arrangement that achieves counter-rotating symmetry. Common
arrangements:

- **Mating final pair:** the final reduction gear drives one side AND
  meshes with a same-size gear on the other side — counter-rotation by
  meshing.
- **Idler between the sides:** the final gear drives an idler that
  meshes with both side gears; the sides rotate in opposite directions
  naturally.
- **Mirrored worm wheels on a common worm shaft:** one worm drives two
  worm wheels (one per side) sitting on opposite sides of the worm.
- **Other:** describe.

**Our arrangement:**
> Mating final pair: the final-stage driven gear (56T) on one side meshes directly with an identical 56T gear on the other side. Since meshing spur gears naturally counter-rotate, this achieves symmetric counter-rotation at a 1:1 rate. Both gears sit on the same-diameter shaft (Ø3.00 mm, matching David's MP3 bore spec) and rotate in opposite directions, each driving its respective four-bar input crank. The center distance between the two sync gears equals 1.0 × (56 + 56) / 2 = 56 mm — this needs to fit within the 92 mm housing width.

_[Team: verify this fits the housing envelope. 56 mm center distance for the sync pair plus gear diameters may be tight in 92 mm total width.]_

---

## Coupling Check

The critical sanity check. If the team holds the thumb-wheel turn count
at the 2.5-turn target, the chosen N forces a specific linkage input
sweep — which may differ from the Part A-designed range. Re-check the
transmission angle at the implied range.

**Linkage input sweep implied by our N (at 2.5 thumb-wheel turns):**
> implied sweep = (2.5 × 360°) / N = (2.5 × 360°) / 16.0 = **56.25°**

**Implied linkage input range:** from 0° to 56.25°
*(anchored at the start angle the linkage was designed around)*

**Transmission angle across this implied range:** 33.75° to 90°
_(μ = 90° − θ for the vertical parallelogram)_

**In band (40°–140°)?** **No** — μ_min = 33.75° is below the 40° floor.

> At N = 16 with 2.5 thumb-wheel turns, the implied linkage sweep of 56.25° pushes the transmission angle below the 40° floor by ~6°. **This means the team must either:**
> 1. Accept fewer thumb-wheel turns (~1.24 turns at the designed 28° sweep), OR
> 2. Increase N to ~32 to keep the 2.5-turn target within the 28° sweep (which requires a third reduction stage or a different architecture), OR
> 3. Accept the out-of-band transmission angle at full closure (μ = 33.75° is marginal, not catastrophic — the gripper will still work but with reduced force efficiency at full closure).
>
> _[Team must make this call and document the decision.]_

---

## Packaging Within the Housing Envelope

The MP1 brief calls for a ~92 × 46 × 55 mm total envelope. Where does
the drive train live?

- **Driver location** (relative to thumb-wheel axis): _[needs team sketch — thumb wheel on the 92 mm long axis, pinion on the same shaft]_
- **Final-stage gear / worm-wheel location** (relative to linkage input
  pivot O₂): _[the final 56T gear sits on the same shaft as O₂ for each side]_
- **Total drive-train footprint vs. available housing volume:** _[Stage 1 center distance 35 mm + Stage 2 center distance 35 mm + sync pair center distance 56 mm. This likely exceeds 92 mm — team needs to optimize gear layout or reduce tooth counts.]_
- **Clearance to the linkage:** _[needs team CAD/sketch verification]_

> _The packaging is flagged as a "needs work" item. The current center
> distances sum to more than the 92 mm housing length, which means
> either the gear layout must be non-linear (offset/stacked stages)
> or the tooth counts / module must be reduced. Team should sketch
> this out._

---

## Labeled Sketch

_[Team: create a labeled sketch showing the gear train layout within the housing. A hand sketch is fine.]_

`<!-- ![Drive train sketch](sketches/drive_train.png) -->`

> A hand sketch is fine. The point is that someone other than you can
> read it.

---

## Gear Strength (Optional)

Lewis bending stress analysis was practice work back in MP1 and tooth
strength at this scale is unlikely to be the failure mode. If your team
wants to do it anyway as a Part B trust-assessment input, fill this in
for the most loaded stage (usually the highest-torque pinion):

_[From David's MP1 Part B stress analysis at the 14T pinion:]_

- **Tangential force at pitch radius:** _[from MP1: F_t at 0.3 N·m nominal on 14 mm pitch diameter → F_t = 0.3 / 0.007 = 42.9 N]_
- **Lewis form factor Y for the pinion:** _[~0.30 for 14T at 20° pressure angle]_
- **Estimated bending stress:** _[σ = F_t / (b × m × Y) = 42.9 / (8 × 1.0 × 0.30) = 17.9 MPa]_
- **Derated PLA limit you're using:** 25–30 MPa _(from David's MP1 Part B — printed PLA, not bulk)_
- **Verdict:** **MARGINAL** _(SF = 25/17.9 = 1.40 at nominal; SF = 25/29.8 = 0.84 at 0.5 N·m max — fails under aggressive use, per MP1 findings)_

> Optional. Not graded for absence; graded for sloppy presence.
