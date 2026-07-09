# Joint 2 of universal impossibility: grading = imprimitivity, step 1 = Wielandt

**Date:** 2026-07-09. **Status:** step (2) reduced to classical; step (1) has a
Wielandt proof skeleton, empirically confirmed but NOT proved. ⟦HAND⟧, raw-DFS
oracle = ground truth.

## What Joint 2 is

Universal impossibility's second joint (distinct from the pruning lemma = Joint 1).
For a strongly-connected non-symmetric recurrent-branching language, the intended
argument (seed 2.2t design-lane) is:
  (1) rich-safe (safe at enough lengths to pass a K4-minor frame's circuits)
      ⟹ the unsafe set is residue-structured (cofinitely a union of residue
      classes mod d);
  (2) residue-structured ⟹ one of grading / potential / phase-code (a taming);
  (3) each taming localises the polytope.
Step (2) was the load-bearing unexamined converse.

## Finding 1: grading = Perron–Frobenius imprimitivity (step 2 is classical)

Taming 4 "grading" = transfer digraph fibered over ℤ_d. **Verified computationally**
(`scratchpad/joint2_wielandt.py` part I): a language is graded-at-some-d ⟺ its
digraph period (gcd of cycle lengths) ≥ 2. Exact match on all examples
(graded-d2, 3-cycle, 2-cycle graded; golden-mean, full2 primitive⟹not graded).

This is classical Perron–Frobenius: a strongly connected digraph has period d ⟺
its vertices d-partition into cyclic classes that arcs advance through ⟺ fibered
over ℤ_d. So the **DICTIONARY** grading ⟺ imprimitivity is classical.

**⚠ BUT step (2) itself is NOT thereby classical (overclaim caught).** Step (2) is
"residue-structured-unsafe ⟹ grading (= imprimitive)", i.e. "unsafe-set-modulus =
digraph-period." **This is FALSE without non-symmetry.** Counterexample from own
data: golden mean `{(0,0),(0,1),(1,0)}` is PRIMITIVE (cycle lengths 1,2, gcd 1)
yet its unsafe set = odds = residue class mod 2 (from the PARITY theorem =
winding/TU, NOT digraph imprimitivity). So residue-structured unsafe sets have ≥2
independent sources (parity/winding AND digraph-period); digraph-period is only one.
Only the dictionary is free; the implication is the real work.

## Finding 2: step (1) is a Wielandt statement (primitive ⟹ cofinitely unsafe)

The real difficulty is the contrapositive of step (1):
  **primitive (period 1) strongly-connected transfer digraph ⟹ cofinitely unsafe
  ⟹ not rich-safe.**

**Empirical confirmation** (`scratchpad/joint2_wielandt.py` II + `joint2_deep.py`):
scanned 110 primitive strongly-connected non-symmetric total languages (|A|≤3).
Six appeared "rich-safe" in the small window L≤9 (safe at {3,4,7}) — an ARTIFACT
of the small window. Pushed to L=30: **all are unsafe at every L in [8,30]; safe
set = {3,4,7}, FINITE.** No primitive language is genuinely rich-safe. This is the
Wielandt shape: a primitive digraph goes cofinitely unsafe.

**Proof skeleton (NOT a proof):** Wielandt's theorem — a primitive n×n 0-1 matrix
M has M^k > 0 for all k ≥ (n−1)²+1 (the Wielandt index). So past the index, between
ANY two states there is a walk of EVERY length. A winding-2 simple cycle needs two
vertex-disjoint off-diagonal strands P (a→b) and Q (b→a) of length L swapping
endpoints. Primitivity supplies walks a→b and b→a of every large length; the
remaining content is the **off-diagonal + vertex-disjoint refinement** (that the
two walks can be chosen non-colliding). The length availability is pure Wielandt;
the disjointness refinement is the genuine open combinatorial step.

⚠ The observed last-safe L=7 is PAST the |A|=3 Wielandt index 5, so the bound is
NOT the naive "unsafe for all L ≥ index" — the disjointness refinement shifts the
threshold. The skeleton is real but incomplete; do not claim step (1) proved.

## THE CRUX (CORRECTED 2026-07-09): "non-symmetry" was a MIS-STATEMENT

Earlier framing: "why does non-symmetry force primitive ⟹ cofinitely-unsafe."
**This is WRONG — refuted by golden mean.** Golden mean is PRIMITIVE and (up to the
loop) SYMMETRIC, yet residue-safe at even L. Its safety is NOT a non-symmetry
effect: **safe ⟺ layered ring bipartite (even L) ⟺ signability/TU (taming 3)
fires.** Verified by building (`scratchpad`, safe⟺bipartite exactly, L=3..10). So
golden-mean's residue-safety IS a taming firing, not evidence for a non-symmetry
axis. Non-symmetry was never the discriminator.

**THE CORRECTED CRUX (the real Joint 2):**

  **The tamings are the only sources of residue-safety in a primitive language.**
  I.e. classify the sources of residue-safety; show each is a catalogued taming.

This is exactly "the tamings are complete" — the same theorem that would de-mess
the paper (ten sufficient conditions → one necessary-and-sufficient classification).
The 4 finite-safe non-symmetric candidates and golden-mean are now UNIFIED: each
safe residue is a taming firing (signability on the bipartite residue for gm; the
non-symmetric ones simply have NO safe residue past Wielandt = no taming fires).
Not "the non-symmetric case" — the SOURCES-OF-SAFETY classification. Needs an idea.

## Finding 3 (DOWNGRADED to a question): do Joints 1 and 2 share an engine?

Tempting: both run on transfer-digraph period. But golden mean shows the unsafe
set's period can come from PARITY (winding/TU), decoupled from digraph-period. So
≥2 mechanisms feed the residue structure, and "Joints 1+2 = one period engine" is
too simple. Keep as an open question, not a leaning.

## What is proved vs open (do not overclaim)

- **CLASSICAL (dictionary only):** grading ⟺ digraph imprimitivity (period ≥2).
- **NOT classical (the crux):** step (2) "residue-unsafe ⟹ grading" — FALSE
  without non-symmetry (golden mean counterexample). Real content = non-symmetry
  forces primitive ⟹ cofinitely-unsafe. Wielandt-shaped, empirically confirmed
  L≤30 on all |A|≤3 non-symmetric primitives, NOT proved.
- **UNVERIFIED sub-claim:** "cofinitely-unsafe ⟹ not rich-safe." rich-safe = covers
  a K4-minor frame's circuit-lengths (the seed's no-fork argument was GIRTH-LOCKING,
  P47 — sparse safe sets can't cover diverse circuit lengths), which is SEPARATE
  from Wielandt finiteness. A finite safe set {3,4,7} is not obviously
  frame-non-covering; check whether Wielandt finiteness delivers not-rich-safe or
  still needs girth-locking.
- **OPEN:** the disjointness refinement; exact threshold; past |A|=3; the crux
  above; Joint 1's k≥3 pruning (separate open piece).

## Mechanism independence — RESOLVED 2026-07-09: the triple collapses

The seed's Joint-2 attack names three forcing mechanisms: grading/potential/phase-code.
Do potential and phase-code carry content independent of grading? **No — verified by
building.**
- **phase-code = grading.** A phase-code is a labelling c: states → ℤ_d advanced by
  every arc (c(b)=c(a)+1). That is exactly `is_graded` = fibered over ℤ_d =
  imprimitivity. Identical by definition.
- **potential collapses.** A monotone ℤ-valued potential (p(b)≥p(a) along arcs,
  non-constant) does not exist on a strongly-connected digraph — it must be constant
  (0 of 347 strongly-connected languages admit a non-constant one; structurally,
  increments sum to 0 around any cycle ⟹ all equal). So "potential" is either
  constant (no information) on the irreducible core, or mod-d valued = grading, or —
  for the reducible part — the already-catalogued monotone-collapse (taming 8).

**⟹ no new third mechanism. Joint 2 has ONE crux (sources-of-residue-safety), not
three.** This sizes the problem: the whole exchange-blocking classification reduces to
the single question "the tamings are the only sources of residue-safety," with grading
(imprimitivity) and signability (TU on bipartite residues, per golden-mean) as the two
confirmed sources so far.

## "Rich-safe" PINNED (2026-07-09) — the frame-covering / residue condition

The girth-locking subtarget's key object, made precise. A FORK = a language L + a
K4-minor frame F such that every circuit length of F lies in Safe(L), yet L is
genuinely contextual (escapes all tamings). A subdivided-K4 has 3 independent
cycles; to make all its circuits safe one subdivides edges so circuits land in an
arithmetic progression d·ℤ (the ρ₂₀ pattern: circuits 18, 24 ∈ 6ℤ = Safe(ρ₂₀)).

**So the sharp necessary condition for a fork: safe on a FULL residue class d·ℤ
(d≥2), not merely finitely many lengths.** This is the filter the fork-hunt needs —
and it is exactly the girth-locking claim's contrapositive: if no untamed language
is safe on a full residue class, no fork exists.

**First deep adversarial sweep (`scratchpad/fork_hunt_scale.py`):** 1500 primitive,
strongly-connected, non-symmetric, NON-bipartite (⟹ signability excluded), |A|=5
languages — i.e. candidates NOT tamed by grading (primitive) or signability
(non-bipartite) — probed for safety on residue classes d·ℤ up to L=30 (past the
Wielandt index 17, and past the L=9 window that produced 6 false "rich-safe"
positives earlier). **ZERO survived.** Every untamed 5-state candidate goes unsafe
on every residue class past the artifact window. Real evidence for UI (not a window
artifact); the hunt should widen (|A|=6, denser branching, more d) — a hit at any
scale kills UI.
