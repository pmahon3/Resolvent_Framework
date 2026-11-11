reviewed: false. 2026-11-10. Hostile check by a fresh agent.

> **Update 2026-11-10.** C6 has since been independently checked (`TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`: CONFIRMED WITH FIXES 1–3 to steps 3–4); steps 1–2 are machine-checked in `TriangleFinitary.lean` (commit 6598c02), steps 3–4 `sorry`. The reversal was propagated the same day. "Unverified" below is the record at the time of writing.

# Independent check of TRIANGLE_GATE_ATTEMPT.md: fired gate (end of §5), §5d Reading, §5e

⟦HAND⟧ = checked by hand here, not Lean. Scripts in `../verification/triangle_gate/`: reran `factor_gate.py`;
new `count_box_sets.py`, `check5e_structure.py` (each under 20 s, memory trivial). Lean read, not compiled.

**Headline (a reversal, UNVERIFIED: checker's own hand proof, needs an independent check before anything is
propagated).** §5e's sharp question seems to have the answer YES: **D₃ = D_fin over any alphabets**, so
D₃∖D_fin is empty, every state on D₃ is fixed by its window family, and **O1 holds on the triangle**
(outcome (B)). The proof (C6) is ⟦HAND⟧ plus Lean `not_inP_of_mem` and `box_of_mem`. Three by-products:
(i) on every finite grid every box set is a carrier set (hand proof; counts agree on five grids);
(ii) E*|[n]³ ∈ D₃([n]³) for every n, closing §5b's "unverified for n ≥ 4"; (iii) the fired gate's NO was
forced by Step 4 on every grid, not only 3×3×3.

## A. The fired gate and the corrected gate

**A1.** "None of the 72 factors through a 2-class partition at any coordinate ... 0 of 10,944 disjoint pairs".
**CORRECT WITH FIXES.**
- Rerun: 15,842 / 15,842 / 72 / 15,914; 0 factoring; 180 pairs; 24 tripartitions, one with E₃; sum-mod-3
  level sets not in D₃. All as stated.
- Swap invariance in xᵢ under a↔b is exactly "pullback through the partition merging a, b"; on three values
  these are all the 2-class partitions. The code is not tautological (`inv` is computed for all co-R1 sets).
- Fix 1: 10,944 counts new–new pairs twice; unordered pairs = 10,944 − 180 = 10,764.
- Fix 2: the script tests only pairs with a new member; the pre-registration said every disjoint pair.
- **Forced in advance** ⟦HAND⟧: a carrier set that factors through a 2-class partition at i is π⁻¹(L) with
  L ∈ D₃(2×X×Y) (restrict along a section), so by Step 4 it has the D¹ form. Hence no set outside D¹ factors
  with m ≤ 2, on any grid and over ℕ. The lesson of §5b applied here too.

**A2.** "the three pre-registered outcomes do not discriminate here; 'O1 leans false' is not drawn". **CORRECT**,
and it holds on every grid (A1), not for the 3-value reason alone.

**A3.** "two disjoint cyclic-order sets share their (≤ 3-class) partition at some coordinate, or one refines
the other". **UNCLEAR as posed; not forced; uninformative if C6 holds.**
- Ill-posed: a cyclic-order set on 4 values with four distinct slices has the identity as its coarsest
  partition, so "share" is trivial there; "≤ 3-class" must mean pullbacks of the 72 sets of 3³. Between two
  3-class partitions "refines" means "equals". And "refines" is not an equivalence relation, so the Step 3–5
  pattern (three equivalence relations covering all pairs) would not run on it. Keep "share" only.
- Not forced by `box_of_mem`, Step 3 or Step 4: a disjoint union of box sets is box, with no alignment needed.
- Feasible without any closure: 72 × 6³ = 15,552 pullbacks on 4³, about 1.2·10⁸ bitmask tests. Not run.
- The inference "No ⇒ finite template for (A)" fails if C6 holds: every finite box set is a carrier set and
  every carrier set over ℕ is finitary, so a non-aligned pair proves nothing about O1.

## B. §5d Reading

**B1.** "the three window events x₀≤x₁, x₁<x₂, x₂<x₀ have indicator sum ≤ 2 pointwise and value sum 3".
**CORRECT WITH FIX.** Sum is in {1,2}. Lean has the strict `C₀ = {x₀ < x₁}` (`sstar_C₀/C₁/C₂` = 1, p
non-principal), not x₀ ≤ x₁. For x₀ ≤ x₁ ⟦HAND⟧: o012 gives 1, o120 = (w,u,v) gives 0, o102 = (v,u,w) gives 0,
so sstar = 1. Cite the strict triple (sum in {0,1,2}) or mark the ≤ value as hand.

**B2.** "The staircase family on window events is a real partial charge (Λ well defined) and not a positive
one". **CORRECT**, and general ⟦HAND⟧: any three ultrafilters with matching marginals form a real partial
charge on the window events. Group an identity by window: f₀₁+f₁₂+f₂₀ = 0 with bounded integer f; fixing
x₂ and then x₀ gives f₀₁ = h+g, f₁₂ = −g+m, f₂₀ = −m−h, and Λ = 0. Not positive: 3 > 2·μ(Ω).

**B3.** "the positive extensions of a two-valued state form a face of the charges on F, so an extreme one is
two-valued". **CORRECT WITH FIXES.** Face of the *probability* charges on F (μ(Ω) = 1 since Ω ∈ C): if
ν = tν₁+(1−t)ν₂ extends μ then νᵢ = μ on C because μ(A) ∈ {0,1}. Also needed: the set is nonempty (this is
3.2.10, so μ must be a *positive* partial charge; false for the staircase), compact in [0,1]^F, Krein–Milman,
and that extreme probability charges on a field are two-valued (conditioning).

**B4.** "if the pair-sum representation of each D₃ indicator can be taken bounded (a finite combination of
window indicators), the window family fixes the state". **CORRECT; the caveat is not needed.** The box
identity with a base point (a′,b′,c′) writes every 1_F, F ∈ D₃, as three slice-cylinder indicators minus
three one-coordinate cylinders plus a constant: seven window indicators, always (Lean `box_of_mem`).
"This renames L1" is inexact: it is s = Λ on all of D₃, which implies O1 and is a priori stronger.

## C. §5e

**C1.** "{F : s(F) = Λ(1_F)} holds the window events and is closed under complement and finite disjoint
union; Λ is well defined on bounded pair-sums". **CORRECT** ⟦HAND⟧ (well-definedness as in B2; s(Ω) = 1).

**C2.** "if some s(Fₙ) = 1 then s(F) = 1. If all are 0, additivity leaves s(F) free, unless F is itself
finitary". **CORRECT WITH FIX.** First half: F∖Fₙ = ⊔_{m≠n}Fₘ ∈ D₃, so s(F) ≥ 1. "Free" is not proved
(only "not forced by this step"); by C6 the case does not arise.

**C3.** "two same-family states can differ only on a set of D₃∖D_fin". **CORRECT**; it follows from C1 alone.

**C4.** "Level 1 gives D¹ ⊆ D_fin". **CORRECT**; it was proved (§3b, `TRIANGLE_3B_CHECK.md`), re-derived
here. Step 3's six pairings; Step 4's sumset bound (α, β each two-valued with step 1, or one constant), which
classifies *every* box set of 2×X×Y, so the infinite union of an aligned class is one pair plus a window
event. An infinite disjoint family of nondegenerate pairs can exist; its union is always finitary.

**C5.** "is D_fin closed under countable disjoint unions? Yes ⇒ D₃ = D_fin and O1 holds". **CORRECT**
(D_fin is then a Dynkin system holding the generators). It is equivalent to D₃ = D_fin, and only sufficient
for O1; "sharp form of the gate" overstates.

**C6.** "No member of D₃(ℕ³)∖D_fin is known." **CORRECT, and (checker's claim) there is none.**
Notation: slices F_a ⊆ X₁×X₂; by the box identity F_a − F_b = α(x₁)+β(x₂) with values in {−1,0,1}. Write
a ≃₁ b if it is a function of x₁ alone, a ≃₂ b if of x₂ alone (two equivalence relations), and call a, b
*K-related* otherwise; then it is ±([U]+[V]−1) with U, V proper. Same at the other two coordinates.
1. **No infinite K-clique** ⟦HAND + Lean⟧. In a clique with base q the pairs (U_a, V_a) are strictly
   anti-ordered (else a value ±2), so some sequence has U increasing, V decreasing (or the reverse). Pick
   u_j ∈ U_{a_{j+1}}∖U_{a_j}, v_k ∈ V_{a_k}∖V_{a_{k+1}}. Then F(a_i,u_j,v_k) = [k<j]+[j<i]+[i≤k]−1 for j ≠ k,
   which is Acy (reverse case: Cyc) on all distinct triples. The pullback to ℕ³ is in D₃ and satisfies `InP`
   with P = ℕ, contradicting `not_inP_of_mem`.
2. **Finite type** ⟦HAND⟧. A clique is a matching in the bipartite graph (≃₁-classes, ≃₂-classes, one edge
   per value). No infinite matching ⇒ a finite maximal one ⇒ its classes cover Xᵢ. So each Xᵢ has a finite
   partition into parts lying in one class, each part labelled by the coordinate it couples to.
3. **Columns** ⟦HAND⟧. P→1, Q→0: F∩(P×Q×X₂) is A×X₂ or P×Q×R′. P→1, Q→2: it is P×W or P′×Q×X₂ (and
   rotations). Every cell has a mutual pair or is cyclic; cyclic cells carry one-coordinate products.
   Remove, window by window, the columns that are whole window events (three legitimate removals). What is
   left is a one-coordinate product in every cell, so it is g⁻¹(F̂) for a box set F̂ on a finite grid.
4. **Finite grids: every box set is a carrier set** ⟦HAND⟧. Induct on |X₀|+|X₁|+|X₂|. If a, b are not
   K-related, F is the pullback of F minus slice a (merge a into b), changed by two window events. If every
   pair at every coordinate is K-related, step 1's chain forces F to be the cyclic-order set of a circular
   arrangement of the values. Swapping two adjacent values of different coordinates toggles exactly one
   window line {xᵢ=p, xⱼ=q}; adjacent values of one coordinate merge; sorting ends at a 1×1×1 grid.
   Evidence: |B| = |D₃| on 2×3×3, 3×3×3, 2×3×4, 3×3×4, 3×4×4 (2350; 15,914; 17,878; 131,290; 1,299,250);
   swap certificates for E*|[n]³, n ≤ 6; column and residue claims on 12,000 sampled box sets, 0 failures.
5. **Conclusion.** F ∈ D₃ ⇒ F = W₀₁ ⊔ W₁₂ ⊔ W₂₀ ⊔ g⁻¹(F̂) ∈ D_fin. So **D₃ = D_fin = {box sets with no
   infinite K-clique}**, over any alphabets.
- The sub-questions. Not every D_fin set is a finite-grid pullback ({x₀ ≤ x₁} has infinitely many slices);
  the normal form is "three window events ⊔ one finite-grid pullback" (D¹ is the case F̂ = K on 2³).
  Same-window countable unions are trivial; mixed windows are handled by steps 1–3.
- Independently of Lean ⟦HAND⟧: D_fin sets have finite clique number (Ramsey on pair types; a mixed clique,
  x₁-only in F and x₂-only in F′ with F, F′ disjoint, has at most 5 values).
- **Not verified:** nobody has checked steps 1–5; Lean was not compiled (file has no `sorry`); step 1 leans
  on the exact form of `InP` (read: agreement with Cyc or Acy on distinct points of P³, one infinite P);
  finite evidence covers steps 3–4 only on small grids, where parts are mostly single values.

## Fixes to apply to TRIANGLE_GATE_ATTEMPT.md

1. Fired gate: "0 of 10,944" → "0 of 10,764 unordered pairs"; add "forced by Step 4 on every grid: a set
   outside D¹ never factors through a 2-class partition".
2. Corrected gate: drop "or one refines the other"; say the sets are pullbacks of the 72 sets of 3³; drop
   "No ⇒ finite template for (A)" pending C6. Mark the gate as superseded if C6 survives its check.
3. §5d Reading: use the strict events (Lean) or mark x₀ ≤ x₁ as hand; "face of the probability charges,
   nonempty by 3.2.10 for positive μ, Krein–Milman"; delete the boundedness caveat (seven-term box formula);
   "renames L1" → "is s = Λ on D₃, sufficient for O1".
4. §5e: "leaves s(F) free" → "does not force s(F) by this step"; "sharp form" → "sufficient form, equivalent
   to D₃ = D_fin"; add a pointer to C6 as an unverified claim that the answer is yes.
5. §5b/§5c: "unverified for n ≥ 4" → "E*|[n]³ ∈ D₃([n]³) for all n (swap argument, hand; script n ≤ 6)".
6. Do not change the verdict line or any taxonomy entry until C6 has its own independent check
   (`*_REVERSAL_CHECK.md`), ideally with steps 1–4 formalised.

## Bearing on WHY.md

If C6 holds, three queries arranged in a loop hide nothing at any number of rounds: every question you can
ask is three window questions plus one question on a finite coarse-graining, and consistent answer patterns
that agree query by query agree everywhere. The only non-finitary object, the infinite cyclic order, is
exactly what the carrier excludes. Composition, not a circle; a hidden idealisation removed. A lens only.
