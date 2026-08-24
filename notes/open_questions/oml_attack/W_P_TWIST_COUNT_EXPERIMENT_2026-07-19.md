# W-P rung-2 twist-count experiment (the tight-packing picture) — PARKED behind rung 1

*Continues `W_P_FEASIBILITY_LADDER_2026-07-19.md` (rung 2, made concrete)
and `PERSPECTIVITY_WALL_CANDIDATE_2026-07-19.md` §6. Provenance:
LLM-derived (Claude, in chat) 2026-07-19, user-driven hand intuition.
Every claim ⟦HAND — UNVERIFIED⟧ and CONDITIONAL ON RUNG 1 (perspectivity
= the ODBC nerve bond). Read the ladder note first. This note does NOT
run anything; it specs the rung-2 experiment and fixes what is and is not
a valid test object.*

**Status: rung 2, gated on rung 1 (NOT cleared). Do not run before rung
1 clears.** If perspectivity is only PART of the bond, twist-count
measures only PART of the obstruction.

## The physical picture (load-bearing intuition, ⟦HAND⟧)

Twist a single ramen strand held at two points: between them the arcs
**pack infinitely tight but DO NOT weld into one element.** They crowd
arbitrarily close; the element they would converge to is exactly the one
NOT present — that missing meeting-point **is the gap** (an accumulation
with no limit point in the structure = a Hausdorff-gap configuration). If
the arcs ever merged, the loop closes → gap filled → witness dead. The
live object is the **never-closing** thread with tight-packing nodes
(corrects the naive "fold into one closed loop," which is the gap filled
= Mackey–Gleason winning).

## The crux, sharpest form: the forced-bound race (§0a)

**Split into its definitional part (flat) and its decision-relevant part
(conditional) — do not conflate.**

- **DEFINITIONAL, unconditional (standard lattice theory).** A lattice
  requires every pair to have a meet and a join *as elements somewhere*;
  it does NOT require tight-packed / nearby elements to coincide. A node
  where two arcs pack tight does not supply `∧`/`∨` by welding — it
  creates the OBLIGATION that `arc-A ∧ arc-B` and `arc-A ∨ arc-B` exist
  as their own elements, distinct from the arcs. Latticehood demands the
  bounds exist; it does not demand they coincide with anything present.
- **DECISION-RELEVANT, conditional on rung 1 (the crux as an OPEN
  QUESTION — bank the question, not an answer).** The forced bound lands
  in one of two places: ON the closing bridge (it IS the convergence
  point → gap filled → strand welds → witness dead) or OFF it (bound
  exists elsewhere, latticehood satisfied, strand still never closes).
  So latticehood and the gap are not in contradiction — they RACE:

  > **The witness exists iff, every time latticehood forces the bound of
  > two tight-packed arcs, that bound lands OFF the closing bridge.** "Do
  > the forced meets/joins avoid the gap-filler?" — the whole question,
  > localized to one element at one node.

  This imports the perspectivity=bond picture and the gap-as-accumulation
  model = rung 1; it is NOT "just definitions."

## The dial: twist count (the finite, computable invariant)

Each twist = one node = one forced perspectivity bridge (tight-pack, not
weld). Twist count = how many closing-type bridges the fold carries —
a countable, computable quantity; the finite calibration W-P §6 asked
for, now with a number to compute. Turning 1→2→3→… is a Möbius-type
operation with **orientation parity** (odd = orientation-reversing,
genuine local-irremovable twist; even = removable), reproducing the
repo's **ring-parity theorem** (contextual scope on odd-period
recurrences) one cardinal down — IF the node=bridge identification holds.

**⚠ Do NOT harden "parity" (ℤ/2).** A real fold may carry richer winding
(ℤ or larger). Safe statement: *there is a finite computable winding
invariant at each stage; its group is for the computation to REPORT, not
assume.*

## Why no finite twist count is the witness (the key negative)

Every finite n (odd or even) → finitely many nodes → the strand closes
after n twists → closed loop → gap filled → tame, witness dead. Odd n
carries a *finite* parity anomaly = ring parity = finite scale, no
σ-essential state. **The finite twist tower explores the whole finite
world and never leaves it** — which is WHY the witness must be genuinely
infinite: a twist at every countable stage, accumulating toward ω₁,
coherent climbing, closing never; the winding refuses a consistent global
value at ω₁ = **nonvanishing lim¹ of the winding-torsor system**.

## OPEN SUB-QUESTION Q-⊥ (new this note, named, load-bearing)

Between two adjacent twists a span of parallel arcs runs bottom→top and
carries a **mirror under orthocomplementation** `⊥` (`p ↦ 1−p`, order-
reversing: sends 0↔1, meets↔joins, flips each span). This is NOT a second
structure — the same strand seen through `⊥`; orthomodularity is what
forces the two readings COMPATIBLE. Odd twists are orientation-reversing
and so is `⊥`, so an odd twist between two spans raises: does the twist's
flip and the complement's flip AGREE or FIGHT? A fight = the strand's
winding incompatible with its own mirror = the obstruction wearing
another face (contextuality as strand-vs-mirror mismatch).

> **Q-⊥ (genuinely open, decision-relevant):** are the twist-parity
> obstruction and the orthocomplement-compatibility obstruction the SAME
> invariant, or TWO independent ones? SAME ⇒ orthomodularity identifies
> them (would explain why the setting is orthomodular lattices
> specifically). TWO ⇒ the witness needs BOTH the winding
> non-globalization AND the complement-incompatibility (harder, two
> obstructions to arrange at once). Do NOT prejudge "two spaces": one
> strand, two readings; whether they are compatible is what
> orthomodularity decides. The pentagon has both a twist structure and an
> orthocomplement, both small enough to check — the computation REPORTS
> which, it is not assumed.

## THE EXPERIMENT — and the hard constraint on valid test objects

**⚠ Neither named finite object can produce the survival-witness
outcome. Verified this session:**

- **Pentagon is FINITE** ⇒ by the key negative above, every twist tower
  closes ⇒ it can ONLY ever report outcome (a) "always closes." The
  survival-witness outcome (b) is impossible there by construction.
- **The amended product-Ulam Ψ-witness is NOT A LATTICE.** Its carrier is
  a σ-complete orthomodular POSET (`sigma_essential_witness.md`
  Corollary 4.4: `A ∧ B` does not exist in L — no maximum among the lower
  bounds). So the "latticehood forces the bound" RACE cannot run on it —
  there is no forced meet to track. (This is exactly why Theorem 2, the
  OML/lattice form, is the OPEN target: the Ψ-witness settles the OMP
  form, not the lattice form.)

**Therefore the experiment on pentagon + Ψ-witness is
CALIBRATION-AND-BOUNDARY-DEMONSTRATION ONLY:**
1. **Winding group at each finite twist stage** (steps §5.1): identify the
   forced perspectivity bridges (nodes), compute the orientation/winding
   invariant, **REPORT its group** (ℤ/2? ℤ? larger?) — do not assume.
2. **Ring-parity match** (§5.2): confirm the odd/even (or richer) anomaly
   matches ring parity where both are computable. Mismatch = a genuine
   finding (node≠bridge, feeding back to rung 1; or richer group).
3. **Forced-bound landing** (§5.3): at each node compute the forced `∧`,
   `∨` of the two tight-packed arcs, determine ON vs OFF the closing
   bridge — watching the race. On the pentagon this is a finite,
   always-closes demonstration; on the Ψ-witness it does not run (no
   forced meet). Report the pattern where it runs.
4. **Q-⊥ same-vs-two** (§5.4): compute BOTH the twist-parity/winding AND
   the orthocomplement-compatibility invariant on the pentagon; report
   COINCIDE (same) or DIFFER (two). This is checkable on the pentagon.
5. **Boundary demonstration** (§5.5): the pentagon MUST report "always
   closes" — bank it as the concrete demonstration of WHY the witness
   must be genuinely infinite. **The survival-witness outcome (winding
   marches toward ω₁ without closing) is NOT reachable on these two
   objects.**

**The real rung-2 deliverable is therefore the missing object:** a
**non-degenerate concrete σ-complete OML (a genuine LATTICE) with real
countable structure**, on which the forced-bound race can actually run
and the winding CAN in principle fail to globalize. Building/confirming
that object is the first hard step of rung 2 — not assumed easy, and not
supplied by the pentagon or the Ψ-witness. Only there can outcome (b)
(the green light to attempt ω₁ extension) appear.

## Integrity flags

- ⟦HAND — UNVERIFIED⟧ throughout; conditional on ladder rung 1.
- Two load-bearing identifications, both = rung 1 in disguise: **node =
  forced perspectivity bridge**, **twist-parity = ring-parity winding**.
  Verify before hardening.
- The §0a forced-bound localization: its DEFINITIONAL half is solid
  (lattice axioms + gap definition); its RACE half is conditional on
  rung 1. Bank the QUESTION ("do forced bounds avoid the gap-filler?"),
  not an answer.
- **Q-⊥ (same-vs-two) is genuinely open** and the one new item here (not
  a restatement). Same = a HOPE, not established. Do not assume either;
  the pentagon reports which.
- Do NOT harden parity/ℤ/2 — report the actual winding group.
- **Test-object constraint (verified this session, not conditional):**
  pentagon = finite ⇒ always-closes only; Ψ-witness = not a lattice ⇒
  race does not run. Survival-witness needs a not-yet-built non-degenerate
  lattice object. A future session must not run these two expecting a
  green light that provably cannot appear.
