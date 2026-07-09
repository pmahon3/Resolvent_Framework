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

## THE CRUX (named): what does non-symmetry do?

Golden mean (symmetric, primitive) gets a residue-structured unsafe set from
PARITY. The 4 non-symmetric primitives go cofinitely UNSAFE (finite safe set).
So the load-bearing open question of Joint 2 is:

  **Why does NON-SYMMETRY force [primitive ⟹ cofinitely unsafe], when symmetric
  primitives (golden mean) instead get a residue-structured unsafe set from the
  parity/winding mechanism?**

This is currently the invisible crux. The 4 finite-safe non-symmetric candidates
are evidence FOR it, but what non-symmetry is doing structurally is not isolated.
Needs a real idea; not closed this session.

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
