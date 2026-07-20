# EPV 2025 primary-source verification receipt (E4, full-PDF read)

**Date:** 2026-07-19 (E-thread unit 2, E4). **Source:** Escolano–Peralta–Villena,
*A Mackey–Gleason–Bunce–Wright theorem for JBW\*-algebras*, arXiv:2509.03213
(3 Sep 2025), full PDF read via `pdftotext` (600 KB, 65 pp). **Charter:**
seed §4 / handoff item-7 step 1 — settle the two UNVERIFIED W-P load-bearing
claims against the body (not the abstract). **Verdict: BOTH CONFIRMED, with
one mechanism caveat that WEAKENS W-P's structural reading (see §4).**

## 1. The positive theorem (already verified against abstract — re-confirmed)

**Theorem 6.1** (p. 61): *Let J be a JBW\*-algebra with no type I₂ direct
summand. Then every bounded finitely additive measure µ: P(J) → ℝ extends to
a bounded linear functional on J_sa … every bounded fa measure µ: P(J) → ℂ
extends to a bounded linear functional on J.*
**Theorem 6.2** (vector-valued, via Hahn–Banach from 6.1): same hypothesis,
X a Banach space ⇒ every bounded fa µ: P(J) → X extends to a bounded linear
operator J → X.

## 2. Claim (i): the type-I₂ non-extension DUAL — CONFIRMED (discrepancy resolved)

**The dual is real and in the primary text**, resolving the flagged
discrepancy (chat "verified" vs repo abstract-fetch "positive only"). It is
NOT in the abstract; it is announced in the intro (*"We devote the final
paragraphs of this paper to show that for every type I₂ JBW\*-algebra J, there
exists a positive finitely additive measure µ: P(J) → ℝ which does not admit
an extension to a bounded linear functional on J."*) and proved in Section 6's
closing paragraphs (arXiv PDF pp. 62–63). So the no-I₂ hypothesis is **SHARP**:
extension holds off I₂, fails on every I₂ summand.

**RESOLUTION of the EPV-dual discrepancy flag** (ladder note §Integrity;
CURRENT_STATE): the chat handoff was CORRECT that the dual is stated flatly;
the repo's own abstract-only WebFetch simply could not see it (it lives in the
body). Both records were honest about what they saw. Dual now VERIFIED from
primary text. **Flag CLEARED.**

## 3. Claim (ii): Prop 3.5 = uniform continuity via halving + isoclinic — CONFIRMED

**Proposition 3.5** (p. 18): *Let J be a JBW\*-algebra without type I₂ summand.
Then every bounded finitely additive measure µ: P(J) → ℝ is uniformly
continuous on P(J).* Its proof (read in full) uses EXACTLY the mechanism W-P
attributed to it:
- **Projection halving:** "this projection can be halved, there exist two
  orthogonal projections … p_{mod,1}=p_{mod,1,1}+p_{mod,1,2} with
  p_{mod,1,1} ∼ₙ p_{mod,1,2}."
- **Small-motion symmetry exchange:** "there exist a symmetry s_mod, depending
  on p_mod and q_mod, such that U_{s_mod}(p_mod)=q_mod" with the
  ‖p−U_s(p)‖ ≤ 2‖p−q‖^{1/2} Lipschitz-in-√δ estimate (Lemma 3.4).
- **Isoclinic interpolation:** "there exist projections h_{mod,j} … h_{mod,j}
  is isoclinic with certain angle θ to both p_{mod,1,1} and p_{mod,1,j}",
  bridging two nearby projections by a third isoclinic to both; linearity of
  the quasi-linear extension on W\*(1,h,p) (Lemma 3.1 + Thm 3.2) then gives the
  uniform-continuity bound (3.5): |µ(p_{mod,1})−µ(q_{mod,1})| ≤
  4(2α_µ(1)−µ(1))(2δ)^{1/2}.
The lattice engine is **Bunce–Wright projection equivalence** (weaker than
Jordan equivalence) + halving + isoclinic bridge. W-P §2's "halving + isoclinic
interpolation" reading of the engine is textually accurate.

## 4. ⚠ The mechanism caveat that WEAKENS W-P (new, decision-relevant)

The confirmation of the POSITIVE engine (§3) is the perspectivity-richness =
tameness side, and it does upgrade the ⟦HAND⟧ Bunce–Wright/Φ-tameness comparison
to a real citation (EPV Prop 3.5 + Thm 6.1). BUT the I₂ DUAL's mechanism is
NOT what W-P's structural picture predicts:

- **The non-extending I₂ measure is KADISON-ELEMENTARY, not a transport/lim¹
  phenomenon.** EPV construct it as: the smallest spin factor is S₃(C) (3×3
  complex symmetric matrices, = the rank-2 I₂ factor); *"Kadison's original
  counterexample for M₂(C) also works in this case."* Explicitly
  µ(1)=1=µ(p₁), µ(0)=0=µ(p₂), µ(p)=½ for every other rank-one projection.
  Non-extension is a **finite-dimensional linear-algebra contradiction** (a
  linear φ matching µ forces 1/3 = 1/2). It then lifts to a general spin factor
  S (rank 2, contains S₃(C)) and to any type-I₂ JBW\* algebra J (which has an
  L^∞(Ω,ν,S) summand) by pullback along a Jordan \*-homomorphism.
- **Consequence for W-P.** EPV's non-extension is a FINITE, rank-two,
  single-summand obstruction — the I₂ summand carries a bad measure for
  Kadison-elementary reasons. It is NOT a countably-connected-but-ω₁-obstructed
  perspective-transport lim¹ (W-P §3). So EPV confirms *that* non-extension
  lives in the I₂/spin corner, but its *shape* is the opposite of W-P's
  conjectured witness shape (finite & elementary vs infinite & cohomological).
  W-P's "twist-carrying perspectivity / Hausdorff-gap" mechanism gets NO
  corroboration from the dual's actual proof; only the LOCATION (I₂-rich
  corner) matches, and that location match is heuristic (W-P §1 already conceded
  it as corroboration-of-direction, not a proven constraint).

## 5. Standing gap EPV does NOT close (unchanged, re-affirmed)

EPV is a **JBW\*-algebra** theorem throughout; every step uses Jordan structure
theory (halving via modular projections, centre-valued traces, Bunce–Wright
Jordan equivalence, Shirshov–Cohn). Our concrete σ-class Ulam-type carriers are
NOT projection lattices of any JBW\* algebra (no Jordan U-operators). So:
- EPV neither forces tameness on nor forbids anything on our carriers.
- A Jordan-free lattice analogue of Prop 3.5 reaching non-JBW\* concrete OMLs
  remains OPEN (the E3 scout's residual charter). W-P is a conjecture ABOUT
  such an analogue.

## 6. Net effect on W-P (feeds the E4 verdict, W-P side)

- The two ⟦HAND⟧ tags on W-P's EPV reading are DISCHARGED: I₂ dual (real,
  sharp) and Prop 3.5 (uniform continuity via halving + isoclinic) both hold.
- BUT the discharge does not strengthen W-P's *witness-shape* conjecture: the
  dual's Kadison-elementary mechanism actively mismatches the lim¹/Hausdorff-gap
  picture. W-P advancing past "design heuristic" therefore rests ENTIRELY on
  rung 1 (perspectivity = the ODBC bond?), not on EPV. EPV cannot promote W-P;
  it only lets the ⟦HAND⟧ comparison become a citation and removes the "is the
  dual even real" doubt.
- ⭑ Citation now usable: EPV 2025 (arXiv:2509.03213), Prop 3.5 + Thm 6.1/6.2
  for the positive (perspectivity-rich ⇒ fa-measure tameness) side; Kadison
  1957 / EPV §6 closing for the I₂ non-extension (elementary, spin-factor).
