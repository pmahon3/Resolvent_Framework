# W-P feasibility ladder + the ramen-fold crux (ORIENTATION, PARKED)

*Operating structure for testing whether the perspectivity constraint W-P
(`PERSPECTIVITY_WALL_CANDIDATE_2026-07-19.md`) has a way forward.
Provenance: LLM-derived (Claude, in chat) 2026-07-19 design conversation,
banked as a handoff note. Every mathematical claim ⟦HAND — UNVERIFIED⟧
until its rung is run fresh-context. This note does NOT advance the
construction; it fixes the ORDER of tests so effort is not spent on rung 2
while rung 1 is unresolved.*

**Current honest status: on RUNG 1, NOT cleared.** Everything in W-P §2–§3
and the crux below is conditional on rung 1.

## The crux, located by hand (⟦HAND⟧, decision-relevant, not banked)

The rope/noodle intuition bottomed at a concrete proof-shape for the
witness's hard core:

- A witness would be a **never-closing infinitely-continued thread**:
  coherent at every countable stage, closed at no stage — which is
  exactly what a **Hausdorff gap** is ("fold it forever, don't fold it
  shut"). Not a closed loop (= gap filled = contradiction), not fully
  separated strands (= tame).
- **The ramen fold = Mackey–Gleason.** The natural move to kill the twist
  (fold all strands into one never-repeating strand) requires a
  **perspectivity** to close the single strand into a loop; a Hausdorff
  gap is *defined* by the non-existence of that closing bridge. Supplying
  the closing perspectivity IS the "abundant perspectivity forces
  tameness" mechanism. The move that removes the twist removes the
  witness — same move.
- **Therefore the danger, stated sharply:** lattice closure may perform
  the fold for you — every forced meet/join is a candidate closing
  bridge. **The witness exists iff latticehood's meets and joins can all
  be forced while NONE closes the loop.** This is the σ-nerve seed's B2
  crux with its proof-shape now visible: a collision between latticehood
  inserting bridges and the gap forbidding the closing one.

## Rung 1 — Identification test (CHEAP; gates everything; DO FIRST)

The load-bearing equation is **perspectivity = the full bonding
constraint `ρ`** of the ODBC nerve
(`oml_distributed_boundary_compactness.md`: `X_p(J)`, fibres `Y_B`, bonds
`ρ^K_J`).

> **Check:** can two blocks `B, B'` share a compatible state-value (agree
> under some section in `X_p(·)`) WITHOUT their relevant projections being
> perspective?

- **No (perspectivity = whole bond):** W-P §2–§3 is the real witness spec;
  proceed to rung 2 with the never-closing-fold as target.
- **Yes (perspectivity = only part):** W-P local form is at most a
  NECESSARY wall; the twist rides the **remainder** of the bond, and
  naming that remainder becomes the Stage-0 deliverable. The rope picture
  was about the wrong structure — and rung 1 just saved the effort.

Cost: an afternoon, by hand on a small ODBC example. Highest
information-per-hour available. This is W-P §5 restated as the first
gate; it must resolve before the W-P §6 finite calibration
(perspectivity on pentagon + Ψ-witness) is meaningful.

## Rung 2 — The miniature collision (the actual theorem; weeks)

Only if rung 1 clears. Do NOT attempt the full ω₁ construction. Put the
two opposed forces in one small room:

> Smallest configuration with GENUINE countable structure (NOT a finite
> toy — finite ⇒ tame for free; needs real gap-vs-closure tension: a short
> Hausdorff-gap / two-sided tower stub on a small concrete carrier). Force
> lattice closure BY HAND. Watch what forced meets/joins do to the closing
> bridge.

Two decisive, both-valuable outcomes:

- **Forced bridges always include a closing one** → if structural,
  generalizes to a **positive Φ theorem** (lattice closure forces
  tameness, witness impossible = the conjecture PROVED, negative
  resolution). A major result, not a failure.
- **Forced bridges can land off the closing bridge** → a **finite-scale
  survival witness**; green light to attempt ω₁ extension.

The miniature DISCRIMINATES either way. **Hardest design decision =
building the RIGHT miniature** (small enough to compute, rich enough to
show the fight, not degenerate-tame). Treat "what is the right miniature"
as the real question, not an assumed-easy step.

**Rung 2 concretized** = the twist-count experiment
(`W_P_TWIST_COUNT_EXPERIMENT_2026-07-19.md`): the dial is the twist count
(each twist = one forced perspectivity bridge = a tight-pack, not a
weld), the invariant is the winding/orientation group (REPORT it, do not
assume ℤ/2), and the race is watched by tracking where the
latticehood-forced `∧`/`∨` of two tight-packed arcs lands (ON the closing
bridge = gap filled = witness dead; OFF = strand never closes). **Hard
constraint verified this session: neither the pentagon (finite ⇒ always
closes) nor the Ψ-witness (NOT a lattice — `sigma_essential_witness.md`
Cor 4.4, no forced meet) can produce the survival-witness outcome; they
are calibration + boundary-demonstration only. The real rung-2
deliverable is the missing non-degenerate concrete σ-complete LATTICE
with genuine countable structure.** The experiment also raises a new
named open sub-question **Q-⊥**: are the twist-parity obstruction and the
orthocomplement-compatibility obstruction the SAME invariant (orthomodularity
identifies them) or TWO independent ones? — reportable on the pentagon.

## Rung 3 — Measure knot (PARK with trigger)

Even a perfect never-closing topology may carry no σ-additive state
(topology-carries-measure ≠ topology-has-twist). Trigger: "attempt state
construction when a lattice-closed open-loop survivor exists at finite
scale." Not before (park-by-default / allocation discipline).

## Base rate + disposition

Every prior direct confrontation (Campaigns 11, 12, 13) resolved AGAINST
the witness; the repo's base rate favors obstruction. Not pessimism: the
rung-2 collision is valuable whichever way it falls — a clean obstruction
there is **proving Φ**, a real theorem toward the negative resolution.
Both resolutions are worth proving; neither is knowable from the armchair.
Run rung 1, then rung 2's miniature, and let them say which theorem is on
the table.

## Integrity flags (mandatory)

- LLM-originated across one design conversation → correlated-confidence
  risk: the same prior underwrites the citations AND the structural
  readings. Verify independently per claim, never "the chat said so."
- **EPV verification discrepancy — DO NOT SMOOTH OVER.** This note's
  source §1 asserts the EPV type-I₂ **non-extension dual** is "stated
  flatly in the intro, ⟦VERIFIED-web⟧." The repo's own WebFetch of the
  arXiv:2509.03213 abstract (E-thread session, 2026-07-19) found ONLY the
  positive direction (no-I₂ ⇒ extension); the I₂ dual was **NOT present in
  the abstract**. Treat the I₂ dual as UNVERIFIED pending E4's full-PDF
  read, per `linearization_E3_scout_verdict.md`. The
  uniform-continuity-is-load-bearing reading (Prop 3.5) is likewise
  ⟦HAND — one-read⟧, also for E4.
- The perspectivity = bonding-map identification is ⟦HAND — UNVERIFIED⟧ =
  rung 1; the rope/noodle/ramen chain is ⟦HAND⟧ and conditional on it.
- Sharpest hope needing a reality check: that rung 2's miniature
  discriminates cleanly rather than yielding an ambiguous degenerate
  middle. Building a non-degenerate miniature is itself hard — the first
  thing to put to the session, not assume.

## Ordered next actions (folds into the E4 handoff first-actions)

1. **Rung 1** by hand on a small ODBC example; record verdict. Gates all
   below. (= W-P §5 gate.)
2. If rung 1 clears: verify-and-promote W-P into `SIGMA_LAYER_TARGET.md`
   (Stage 0), resolving the necessary-vs-sufficient flag as settled.
3. If rung 1 clears: design the **rung-2 miniature** (the hard step) and
   run the collision by hand; record which outcome fires.
4. Regardless: E4 re-checks the EPV I₂ dual + uniform-continuity reading
   against the full PDF before W-P hardens; upgrade the ⟦HAND⟧ tags.
5. Keep the finite calibration (perspectivity on pentagon + Ψ-witness) as
   the cheap self-falsifier alongside the `X_p(J)` and E2a/E2b receipts.
