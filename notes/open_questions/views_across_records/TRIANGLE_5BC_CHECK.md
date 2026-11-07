# Independent check of TRIANGLE_GATE_ATTEMPT.md §5b–§5c

reviewed: false. 2026-11-07. Hostile check by a fresh agent. ⟦HAND⟧ = checked by hand here, not Lean.
Script: `../verification/triangle_gate/check5b_box.py` (new). Reran `pstack.py`, `pstack_control.py`.

**Headline.** The P-stack gate's NO was forced in advance by Lean `box_of_mem`. **No nonempty set inside a product
of proper subsets (so no nonempty finite set) is in D₃(ℕ³).** ⟦HAND⟧: pick (a,b,c) ∈ F and a',b',c' outside its
projections. In the box identity the left side is 1 and the right side is 0. Check: on 3³, no nonempty carrier set
avoids value 2 on all three coordinates (`check5b_box.py`). So §5b's YES branch could not happen, and its "needs
n ≥ 4" is wrong. The rephrase "which finite sets are in D₃(ℕ³)?" has the answer: only ∅.

**1. §5b facts: CORRECT WITH FIXES.**
- (1) Correct ⟦HAND⟧: {E : g⁻¹E ∈ D₃} is Dynkin and holds window events; collapse min(v,n) and inclusion ι both fix
  A ⊆ [n]³; spare-value grid via ι.
- (2) Correct. Lean `D₃ = DynkinSystem.generate gens` (∅, complements, ℕ-indexed disjoint unions; `iUnion hd` case
  of `box_of_mem`); increasing union = disjoint union of differences (`has_diff`).
- Fix: "some truncation ∉ D₃(ℕ³)" is vacuous: every nonempty one is out.

**2. §5b computations: CORRECT. Reading justified, and understated.**
- Reran: 4×3×3, 3×4×3, 3×3×4: |D₃| = 131,290, E₃ (9 pts) ∉ D₃; 3³: 15,914, E₃ ∈ D₃. Control: 2,744 kept, 13,170 lost, sizes 3–24 as stated, E₃ lost.
- Not tautological: closure reaches a fixpoint; E₃ mask = Lean `Estar`; control compares point-sets correctly.
- "Generic" holds; even 3-point window events of 3³ are lost, and on ℕ³ loss is universal.

**3. Reformulation: CORRECT WITH FIXES.**
- Ẽₙ → E* pointwise (eventually constant once n−1 > max x), and not monotone. Example: (5,3,0) ∉ E* but is in Ẽ₂–Ẽ₄;
  (5,0,3) ∈ E*, not in Ẽ₁–Ẽ₄.
- **Gap: "all in D₃(ℕ³)".** The capping map has a section, so **Ẽₙ ∈ D₃(ℕ³) ⟺ E*|[n]³ ∈ D₃([n]³)**. Holds for n ≤ 3;
  UNVERIFIED for n ≥ 4 (4³ non-compressed; cyclic-order data stop at 3×4×4; 4³ closure too heavy here). Scope the claim to "those Ẽₙ in D₃". §5c's
  conclusion survives either way (see 5).
- "§5a's counts are unaffected": CORRECT, since they are statements about grids. But §5a's phrase "finite cyclic-order
  patches" in ℕ³ must mean their pullbacks: finite patches are never carrier sets.

**4. §5c worked case: CORRECT. One causal overstatement.**
- (a) If E*|[n]³ ∈ D₃([n]³), which equals D_fin there because the grid is finite, then Ẽₙ ∈ D_fin(ℕ³): pullback
  commutes with complement and finite disjoint union.
- (b) s = Λ on D_fin by Dynkin induction (both sides additive). Λ is well defined as a functional on *bounded* pair-sums
  (D_fin indicators have such; not a claim that Λ is a state on D₃, cf. `TRIANGLE_3B_CHECK.md`) ⟦HAND⟧.
  Suppose f₀₁+f₁₂+f₂₀ = 0. Fix x₂ to get f₀₁ = h(x₀)+g(x₁); then f₁₂ = −g(x₁)+m(x₂) and f₂₀ = −m(x₂)−h(x₀). With
  matching marginals, Λ = p₀h + p₁g − p₁g + p₂m − p₂m − p₀h = 0.
- (c) The pair-sum identity holds everywhere: the count is always 1 or 2. Off a u_ij-null set the caps tie, giving
  window values 1, 0, 0 and Λ(Ẽₙ) = 0. Only non-principal pᵢ are used.
- Λ(E*) = 1+1+1−1 = 2 for the staircase family (= Lean `sstar` E*: W₀₁₂ = W₁₂₀ = 1, W₁₀₂ = 0). But "**which is why**
  E* ∉ D₃" overstates. Lean `estar_not_mem` uses no ultrafilter (box identity + far-point lift + induction). Λ = 2 gives
  a *second* proof only through `sstar_mem` (sstar ∈ {0,1} on D₃), which itself rests on `not_inP_of_mem`. Say
  "consistent with; an alternative witness via `sstar_mem`".

**5. §5c general form: CORRECT ⟦HAND⟧. Reading: CORRECT WITH FIXES.**
- A ∈ D₃(G) ⊆ B(G), so 1_A = Σ a_ij, and Λ(g⁻¹A) = Σ (gᵢ,gⱼ)₊u_ij(a_ij). An ultrafilter on a finite set is
  principal, at (qᵢ,qⱼ) with qᵢ = gᵢ₊pᵢ. Matching marginals make q consistent across the windows, so the value is
  Σ a_ij(q) = 1_A(q). This holds for principal marginals too, with no freeness needed. The worked case is
  q = (n−1, n−1, n−1).
- Fix 1: "which tensor product, p⊗q or q⊗p" is one example only. u_ij can be any ultrafilter on ℕ² with marginals
  (pᵢ,pⱼ), and there are many more.
- Fix 2: "exactly the gap between (βℕ)³ and β(ℕ³)" overclaims. Families map onto (βℕ)³ non-injectively, and receive a
  map from β(ℕ³) that is neither injective (three-way data) nor surjective (pointless families, Lean
  `triangle_pointless_state`). HS §11.1 (`own.hindman_strauss_tensor`) owns tensors, β(ℕ²) ≠ (βℕ)², not "exactly".
- Fix 3: for the gate, "invisible at every finite resolution" adds nothing beyond §2. Pullbacks lie in D_fin, where
  states with the same family already agree. What *is* new: states with *different* families but equal marginals agree
  on all pullbacks. The corrected tail ("must leave D_fin, as §2 requires") is accurate.
- "Coarse-graining" must mean coordinatewise; for arbitrary finite carrier partitions it is trivial.

**6. Prior art (light): folklore.**
- Ultrafilter images on finite sets are principal; βX = inverse limit of finite partitions (Stone). No shelf/`owned_regions` hit. §5c general form = bookkeeping.

## Bearing on WHY.md

- **Hidden idealisation.** A question true at only finitely many outcomes is never one you can ask on ℕ³. The questions you can ask
  "see" only up to a finite resolution through coarse-grainings that cap values at a top value meaning "≥ that value".
  At each, every consistent answer pattern is the point of its marginals; window order at infinity, and any
  disagreement, live only in countable patchworks. Sharper idealisation reading, not composition. A lens only.
