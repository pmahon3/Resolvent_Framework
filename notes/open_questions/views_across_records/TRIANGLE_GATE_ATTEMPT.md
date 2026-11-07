# Triangle gate attempt: does the window family fix the state on the infinite triangle?

reviewed: false. 2026-11-06. Machine-assisted. ⟦HAND⟧ marks arguments checked by neither Lean nor an independent agent.
No prior-art pass has been run, so nothing here is claimed as new. Scripts: `~/.claude/jobs/26482d7b/tmp/tri/`
(`checks.py`, `two_vertex.py`, `kform.py`, `altrank.py`). Gate source: `CONVEX_GLUING_T1_ATTEMPT.md` §7.

**Verdict: neither (A) nor (B) closed.** One rung of (B) is proved ⟦HAND⟧: the first countable level of the carrier
cannot carry a disagreement. The remaining step is reduced to two named lemmas (§5).

## Puzzle

Three windows look at a triangle, and each shows a pair. Every question built in *one* round (a countable patchwork of
window answers and their negations) already has its answer fixed by what the windows say. Could a question built in
*two* rounds still be answered differently by two consistent answer patterns that agree on every window?

## 1. The statement, in the carrier's own terms

- Ω = X₀×X₁×X₂, with the Xᵢ infinite (ℕ is the case of interest).
- D₃ is the Dynkin closure of the window events of {0,1}, {1,2} and {2,0} (`TriangleCyclic.D₃`).
- A state is a finitely additive s : D₃ → {0,1}. Its window family (u₀₁, u₁₂, u₂₀) consists of ultrafilters with
  matching marginals.
- **Gate (O1 on the triangle):** do two states with the same window family agree on D₃? The flat sub-case: if the family
  is W|windows, is s = W|D₃? Every principal family is flat.
- **Principal reduction ⟦HAND⟧.** Take a principal family at a.
  - Each window block is all of P(Xᵢ×Xⱼ), and s is principal on it, hence σ-additive there.
  - Run a Dynkin induction on {F : s(F) = [a∈F]}. It gives **s = δ_a|D₃ ⟺ s is σ-additive on D₃.**
  - So (A) at a point is a state that is σ-additive on each of the three σ-algebras but not on their Dynkin join. Its
    failure is always some F = ⊔Fₙ with s(F) = 1, every s(Fₙ) = 0, and a ∉ F. Such a state is automatically pointless.

## 2. Facts fixed first

- **D₃ ⊊ B over ℕ.** Here B = {E : Box(E)}, the sets whose indicator is a sum of pair functions.
  - Witness: 1_{E*} = [x₀≤x₁] + [x₁<x₂] + [x₂<x₀] − 1, a 0/1 pair-sum (`checks.py` (1), n ≤ 8). Yet E* ∉ D₃ (Lean
    `estar_not_mem`).
  - So "carrier = box sets ⇒ linear" is not a route.
- **Finitary closure is forced.** s = Λ_u on the finitary Dynkin closure D_fin, by induction: both sides are additive
  and agree on the generators.
  - Any disagreement therefore needs a countable union that s does not respect.
- **Finite grids cannot decide the gate.** Every two-valued state there is a point.
  - They only show that the rank grows: rank 1 on 2×n×m, rank 2 on 3×3×3, where 72 sets need it (`altrank.py`).
  - All 72 have 9 points, and E*∩[3]³ is one of them (`kform.py`).

## 3. Theorem (level-1 rigidity) ⟦HAND⟧

Define the countable hierarchy:
- D⁰ = R0 = {A₀₁ ⊔ B₁₂ ⊔ C₂₀}, the disjoint unions of window events, one from each window.
- Dᵏ⁺¹ = the countable disjoint unions of members of Dᵏ and their complements.
- D₃ = ⋃_{k<ω₁} Dᵏ.

**Theorem.** Over any alphabets, two two-valued states with the same window family agree on D¹. In particular, a
principal family at a gives s = δ_a on D¹.

**Step 1. R0 is closed under countable disjoint unions.** Regroup the pieces window by window. Each block is a σ-algebra.
The value of s on R0 is u₀₁(A) + u₁₂(B) + u₂₀(C).

**Step 2. Normal form of R0-complements.**
- Disjointness of A and B means no x₁ value is used by both. The same holds cyclically for the other two pairs.
- Set α₁ = π₁(A), α₂ = π₂(B), α₀ = π₀(C). Then A ⊆ {x₀∉α₀, x₁∈α₁}, B ⊆ {x₁∉α₁, x₂∈α₂} and C ⊆ {x₂∉α₂, x₀∈α₀}.
- These three regions cover six of the eight classes of (xᵢ ∈ αᵢ). Hence
  Ω∖R = K(α) ⊔ (three window events), where K(S) := S₀×S₁×S₂ ⊔ S₀ᶜ×S₁ᶜ×S₂ᶜ is an **antipodal cube pair**.
- K(S) is the complement of an R0 set. It is a window event unless every Sᵢ is proper.
- Consequently every F ∈ D¹ has the form F = R* ⊔ K*, with R* ∈ R0 and K* = ⊔ₙ Kₙ a disjoint family of nondegenerate
  pairs. So s(F) is fixed once s(K*) is.

**Step 3. Alignment.**
- Let K(S) and K(T) be disjoint and nondegenerate. Then for some i, Tᵢ = Sᵢ or Tᵢ = Sᵢᶜ.
  - Reason: the four cube intersections need a disjoint coordinate, an S ⊆ T coordinate, a T ⊆ S coordinate and a
    covering coordinate. Three coordinates can supply four conditions only if one coordinate is equal or complementary.
  - Exhaustive check: 0 violations among 17,784 / 64,104 / 215,880 disjoint pairs on 3×3×4, 3×4×4 and 4×4×4
    (`checks.py` (2)).
- The relation m ~ᵢ n ⟺ Sᵢᵐ ∈ {Sᵢⁿ, Sᵢⁿᶜ} is an equivalence relation, and ~₀ ∪ ~₁ ∪ ~₂ covers all pairs.
- So for any ultrafilter 𝒰 on the index set, one class [m]ᵢ is 𝒰-large: fix m, and ℕ∖{m} ∈ 𝒰 is a union of three
  classes.
- Since K(S) = K(Sᶜ), we may normalise to Sᵢⁿ = A on that class.

**Step 4. The two-point vertex is rigid.**
- On 2×X×Y, Box makes the slice difference d = 1_{E¹} − 1_{E⁰} equal α(x₁) + β(x₂) with values in {−1,0,1}.
- The sumset bound leaves two cases:
  - d depends on one coordinate, and then E ∈ R0;
  - d = [x₁∈U] + [x₂∈V] − 1, and then E = K(U,V) ⊔ (a {1,2}-event).
- So D₃(2×X×Y) = B(2×X×Y) ⊆ D_fin, and **every state there equals Λ of its family.**
- Check: all box sets on 2×2×2, 2×3×3 and 2×3×4 (70 / 2350 / 17,878) have one of these two forms (`two_vertex.py`).

**Step 5. Collapse.**
- Suppose s(K*) = 1 but s′(K*) = 0. Put 𝒰 = {I : s(K_I) = 1}, using K_I := ⊔_{n∈I} Kₙ ∈ D₃; it is an ultrafilter on the
  indices.
- If 𝒰 is principal at n, then s′(Kₙ) = s(Kₙ) = 1, since Kₙ ∈ R0ᶜ. That contradicts s′(K*) = 0.
- Otherwise, take the 𝒰-large class I₁ from Step 3, where Sᵢⁿ = A. Put π(x) = ([xᵢ∈A], other coordinates).
  - Then K_{I₁} = π⁻¹L with L ∈ D₃(2×X×Y). The map π⁻¹ sends D₃(2XY) into D₃ and window events to window events.
  - So s∘π⁻¹ and s′∘π⁻¹ are states on D₃(2XY) with the same family. By Step 4 they are equal, which gives s′(K_{I₁}) = 1.
    That contradicts s′(K*) = 0.
- Neither flatness nor countability of X is used. ∎

**Scope.** This is O1 at level 1: same family ⇒ same values on D¹. It is not T1′ at level 1. It gives s = Λ_u on D¹
only when Λ_u|D₃ is itself a state, i.e. for flat families (W|D₃), principal families (δ_a) and the staircase (sstar).

**Consequence (shape of any counterexample).**
- Let k+1 ≥ 2 be the least level on which two same-family states differ, and F a set at that level where they differ.
- Then F = H ⊔ ⊔ₙ(Ω∖Hₙ), where H, Hₙ ∈ Dᵏ, the Hₙ are pairwise co-covering (H_m ∪ Hₙ = Ω), and infinitely many Ω∖Hₙ
  lie outside Dᵏ.
- k = 1 is the first case. In the principal case, s(F) = 1, s(Ω∖Hₙ) = 0 and a ∉ F.

## 4. The DNP Example 2.2 transport collapses into the same blocker

- Flat family W: on D¹ every state equals W|D₃, which is linear. So an MO₄ copy (1_A + 1_{Bᶜ} + 1_C + 1_{Dᶜ} = 2) can be
  violated only if it uses sets outside D¹.
- Pointwise limits of linear states are linear, so "an ultrafilter for the flat part" cannot produce the violation.
- What remains is compactness:
  - the two-valued states with a given family form a closed subset of {0,1}^{D₃};
  - (A) holds ⟺ some F is finitely satisfiable with the opposite value;
  - (B) holds ⟺ every F has a finite certificate.
  - Check the exact hypotheses of DNP 2015 Thm 1 before citing it as the tool.

## 5. Named blockers (what would settle the gate)

**L1 (level-2 step).** Pairwise disjoint complements of D¹ sets (equivalently, co-covering Hₙ ∈ D¹) admit an alignment
lemma like Step 3. Then a 𝒰-large subfamily is a pullback along a coordinatewise map with one finite coordinate.
- This needs a normal form for co-D¹ sets. Finite evidence that they are genuinely new: at 3×3×3, the closure of window
  events and antipodal pairs under disjoint unions misses 72 sets of D₃ (`kform.py`).
- Literature that might supply it (neither book is on the shelf; both are pinned hardcopy checks, `pinned_book_checks.md`):
  - Pták–Pulmannová 1991, the concrete-logic chapters: σ-classes generated by several sub-σ-algebras, disjoint-union
    normal form. Exact location unverified.
  - Bhaskara Rao, *Theory of Charges*, Ch. 3 (esp. §3.2): {0,1}-charges on complement- and disjoint-union-closed
    domains, and the extension criterion. Exact theorem unverified.
- Read in full, and not supplying it: Gudder 1984, Zerbe–Gudder 1985, DNP 2015.
- DNP 2007 has been read only from Ex 2.2 to Thm 2.3 (its index entry is abstract-only).

**L2 (one finite vertex).** For finite m ≥ 3, every state on D₃(m×X×Y) is determined by its window family (proved for
m = 2, Step 4). With L1 this closes level 2. The transfinite step needs L1 at every level, stated uniformly.

**L1′ (shortcut that would replace L1 + L2).** "A two-valued state on the Dynkin join of three σ-algebras, σ-additive on
each, is σ-additive." This is the principal case only, so it would answer (B) only at points.
- It is the two-valued, finite-V analogue of the per-level versus glued σ-additivity gap (Andersen–Jessen;
  `papers/paper_i/notes/PAPER_I_REVERSAL_CHECK.md`). There, it fails for infinitely many levels.
- A counterexample (A) is exactly a witness that it fails for three σ-algebras arranged in a triangle.

**Pre-registered next gate (not run).** This is a pairwise test, mirroring `checks.py` (2).
- On 3×3×3 (3×3×4 if it fits in 2 GB), take every disjoint pair of complements of R1-sets. A pair *factors at i with m
  classes* if some partition of Xᵢ into at most m classes makes both sets pullbacks through it.
- Does every disjoint pair factor at some i with m ≤ 2?
  - Yes ⇒ attempt L1 by the Step 3–5 pattern (affects O1 positively, and L2 is not needed).
  - Yes, but only with m ≥ 3 ⇒ L2 becomes the live blocker.
  - No ⇒ the non-factoring pair is the finite template for (A), and O1 leans false.

## Bearing on WHY.md

- **Loop and hidden idealisation.** On the triangle, questions patched in one round cannot hide a disagreement between
  views that agree window by window. Anything hidden sits in patchworks of patchworks.
- **Circle, or composition?** Composition: each σ-algebra behaves well, and a disagreement is collapsed one vertex at a
  time onto a two-point vertex. L1 asks whether that keeps working up the levels.
- This is a lens on data merging, not an application.
