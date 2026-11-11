reviewed: false. 2026-11-10. Independent reversal check by a fresh agent, hostile to both sides.

> **Update 2026-11-10.** Since this check: steps 1–2 machine-checked in `formalization/QuerySystem/QuerySystem/TriangleFinitary.lean` (`no_infinite_clique`, `finite_cover`, sorry-free; commit 6598c02); steps 3–4 were `sorry` at first and are **proved since** (later the same day): the file has no `sorry`. The Lean proof of step 4 does not use Fixes 2–3 (it merges an inclusion-minimal class directly), and `mem_dfin` bypasses step 3 by a collapse along the cover. Propagated by a separate manual inventory the same day.

# Reversal check: D₃ = D_fin on the triangle (`TRIANGLE_5DE_CHECK.md` C6)

**Verdict: CONFIRMED WITH FIXES.** Every step was re-derived by hand ⟦HAND⟧; no step is wrong. Steps 1, 2 and 5
are correct as written. Steps 3 and 4 are correct in substance, but each states one thing without proof that
needs a short argument (Step 3: the residue is a pullback only after refining the partitions; Step 4: why an
all-K-related finite box set is an order set). Both arguments are supplied below and no new hypothesis is needed.
The only machine-checked inputs are Lean `box_of_mem` and `not_inP_of_mem` (read, not compiled); everything else
is hand proof by two agents, with finite-grid computations as evidence. No counterexample was found, and the
normal form contradicts no machine-checked fact. Status of the theorem after this check: ⟦HAND, independently
checked; not Lean⟧.

## Exact Lean statements (`formalization/QuerySystem/QuerySystem/TriangleCyclic.lean`, no `sorry` in file)

```lean
abbrev Ω := Fin 3 → ℕ
def gens : Set (Set Ω) := {E | ∃ w ∈ W₃, @MeasurableSet _ (windowSigma w) E}   -- W₃ = {{0,1},{1,2},{2,0}}
def D₃ : DynkinSystem Ω := DynkinSystem.generate gens
def Box (E : Set Ω) : Prop := ∀ a a' b b' c c' : ℕ,
    cnt E ![a, b, c] + cnt E ![a', b', c] + cnt E ![a', b, c'] + cnt E ![a, b', c'] =
      cnt E ![a', b, c] + cnt E ![a, b', c] + cnt E ![a, b, c'] + cnt E ![a', b', c']
theorem box_of_mem {E : Set Ω} (hE : D₃.Has E) : Box E
def Cyc (x : Ω) : Prop := (x 0 < x 1 ∧ x 1 < x 2) ∨ (x 1 < x 2 ∧ x 2 < x 0) ∨ (x 2 < x 0 ∧ x 0 < x 1)
def Acy (x : Ω) : Prop := (x 0 < x 2 ∧ x 2 < x 1) ∨ (x 2 < x 1 ∧ x 1 < x 0) ∨ (x 1 < x 0 ∧ x 0 < x 2)
def OnP (P : Set ℕ) (x : Ω) : Prop := x 0 ∈ P ∧ x 1 ∈ P ∧ x 2 ∈ P
def Dist (x : Ω) : Prop := x 0 ≠ x 1 ∧ x 1 ≠ x 2 ∧ x 0 ≠ x 2
def InP (Z : Set Ω) : Prop := ∃ P : Set ℕ, P.Infinite ∧ ((∀ x, OnP P x → Dist x → (x ∈ Z ↔ Cyc x)) ∨
    (∀ x, OnP P x → Dist x → (x ∈ Z ↔ Acy x)))
theorem not_inP_of_mem {E : Set Ω} (hE : D₃.Has E) : ¬ InP E
theorem estar_not_mem : ¬ D₃.Has Estar
```
- Alphabet: ℕ only. `gens` is every set depending on two coordinates (`window_mem`: any `S : Set (w → ℕ)`).
- `InP` uses ONE infinite P for all three coordinates and constrains only points with three distinct
  coordinates. The proof uses it with P = ℕ (`Set.univ`), second disjunct (Acy). That is what Step 1 produces.
- Bridge to arbitrary alphabets: only through a coordinatewise map g : ℕ³ → X₀×X₁×X₂. g⁻¹ commutes with
  complement and countable disjoint union and sends two-coordinate sets to two-coordinate sets, so
  F ∈ D₃(X) ⇒ g⁻¹F ∈ D₃(ℕ³) ⟦HAND; one-line induction; Lean has the analogue `mem_pre` for ℕ ↪ ℤ only⟧.
  `box_of_mem` over a general alphabet is the same pointwise argument ⟦HAND⟧, or follows from Lean by
  pulling back along a map hitting the eight corners.

## Steps

Notation as in C6: slices F_a ⊆ X₁×X₂; a ≃₁ b if F_a − F_b is a function of x₁ alone, a ≃₂ b if of x₂ alone,
K-related otherwise. Same at the other two coordinates, cyclically.

**Step 1.** "No infinite K-clique ... contradicting `not_inP_of_mem`." **CORRECT.**
- Slice difference. Box gives d = 1_{F_a} − 1_{F_b} = α(x₁) + β(x₂), α, β integer valued (α = d(·,z₀),
  β = d(y₀,·) − d(y₀,z₀)), with all sums in {−1,0,1}. So diam(α) + diam(β) ≤ 2. If one is constant, d is a
  function of one coordinate (it may take all three values; C4's "two-valued" is slightly loose, harmless).
  Otherwise both are two-valued with step 1 and d = [x₁∈U] + [x₂∈V] − 1 with U, V proper and nonempty. The
  sign ± in C6 is absorbed by complementing U and V.
- Chain. Clique C, base q, F_a = F_q + [U_a] + [V_a] − 1 for a ∈ C∖{q}. For a ≠ b,
  F_a − F_b = ([U_a] − [U_b]) + ([V_a] − [V_b]) must again be of K type: each bracket two-valued with step 1,
  and the two with opposite signs. So U_b ⊊ U_a and V_a ⊊ V_b, or the reverse. C∖{q} is thus totally ordered
  by inclusion of U; an infinite total order has an infinite monotone sequence. No more Ramsey than that is used.
- Sub-grid. Say U_{a_1} ⊊ U_{a_2} ⊊ …, V strictly decreasing. Pick u_j ∈ U_{a_{j+1}}∖U_{a_j},
  v_k ∈ V_{a_k}∖V_{a_{k+1}}. Then [u_j ∈ U_{a_i}] = [j<i], [v_k ∈ V_{a_i}] = [i≤k], and
  F(a_i,u_j,v_k) = F(q,u_j,v_k) + [j<i] + [i≤k] − 1. For j<k take i = k: the correction is +1, so
  F(q,u_j,v_k) = 0. For k<j take i = j: correction −1, so F(q,u_j,v_k) = 1. Hence for j ≠ k,
  F(a_i,u_j,v_k) = [k<j] + [j<i] + [i≤k] − 1. On distinct (i,j,k): value 1 exactly for i<k<j, k<j<i, j<i<k,
  which is Lean `Acy` at x = (i,j,k); value 0 on the three `Cyc` orders. (Checked all six orders.)
- Contradiction. g(i,j,k) = (a_i,u_j,v_k) is coordinatewise, so g⁻¹F ∈ D₃(ℕ³), and it satisfies `InP` with
  P = ℕ. If instead U decreases along the sequence (V increases), the same computation gives
  [j<k] + [i<j] + [k<i] − 1 on distinct triples, which is `Cyc`; `InP` covers both.
- Other coordinates: no rotation lemma is needed. For a clique b_i at coordinate 1 (slices in (x₂,x₀)), the
  map (n₀,n₁,n₂) ↦ (v_{n₀}, b_{n₁}, u_{n₂}) gives [n₀<n₂] + [n₂<n₁] + [n₁≤n₀] − 1, again Acy on distinct
  triples. Same at coordinate 2.

**Step 2.** "A clique is a matching ... no infinite matching ⇒ a finite maximal one ⇒ its classes cover Xᵢ."
**CORRECT.** The statement used is: a bipartite multigraph with no infinite matching has a finite vertex cover.
- Vertices: ≃₁-classes and ≃₂-classes of X₀. Each value a is one edge (its ≃₁-class, its ≃₂-class). a, b are
  K-related iff they are in different ≃₁-classes and different ≃₂-classes iff their edges share no endpoint.
  So K-clique = matching, exactly.
- A maximal matching M exists (Zorn; greedy if X₀ countable) and is finite by Step 1. Every edge meets an
  edge of M, so every value lies in one of the 2|M| classes touched by M. Assign each value to one of them.
- Result: a finite partition of X₀ into parts, each inside a single ≃₁-class (label →1) or a single
  ≃₂-class (label →2). The general worry (no infinite clique does not bound the number of classes) does not
  apply: the number of ≃₁-classes may be infinite, and only a finite cover by classes of either kind is
  claimed. Example: {x₀ ≤ x₁} has infinitely many distinct slices, all in one ≃₁-class: one part.

**Step 3.** "Columns ... what is left is a one-coordinate product in every cell, so it is g⁻¹(F̂)."
**CORRECT WITH FIXES.** Nothing in it uses finiteness of the parts. Derivations (a, b ∈ P; y, y′ ∈ Q; fixed a₀, y₀):
- P→1, Q→0: F(a,y,z) = F(a₀,y₀,z) + k(a₀;y) + h(a;y) = φ(z) + ψ(a,y). If φ is not constant, ψ ≡ 0 and the
  column is P×Q×R′; if φ is constant it is A×X₂. ✓.
- P→1, Q→2: F(a,y,z) − F(a₀,y,z) = h_a(y), and F(a,y,z) − F(a,y₀,z) = m_y(z) does not depend on a, so
  h_a(y) = h_a(y₀) =: c_a. If F(a₀,·,·) is not constant on Q×X₂, all c_a = 0: column P×W. Otherwise P′×Q×X₂. ✓.
  The mirror case P→2, Q→0 gives W′×Q or P×Q′×X₂ the same way.
- P→2, Q→2 columns are not described in C6 and have no product form (for each z the section is P_z×Q or
  P×Q_z). They are not needed: see the cell count next.
- Cells. A cell P×Q×R has labels P→{1,2}, Q→{2,0}, R→{0,1}: a map on three vertices without fixed points,
  so it has a 2-cycle (mutual pair) or is a 3-cycle. **At most one mutual pair per cell** (two would need two
  labels on one part). In a cyclic cell the three column lemmas say: F∩cell is independent of xᵢ or depends
  on xᵢ only, for each i; hence it depends on one coordinate only. ✓.
- Removals. W₀₁ = union of the mutual {0,1}-columns (P→1, Q→0) of the form A×X₂; W₁₂, W₂₀ likewise. They
  are window events inside F. They are pairwise disjoint because they use parts with different labels
  (Q→0 against Q→2, P→1 against P→2, R→1 against R→0). A cell with a mutual pair is either removed whole or
  is P×Q×R″ (R″ = R′∩R) and is untouched by the other two removals.
- **Fix 1.** The residue F′ = F∖(W₀₁⊔W₁₂⊔W₂₀) is, cell by cell, P′×Q×R or P×Q′×R or P×Q×R″ with P′ ⊆ P etc.
  arbitrary subsets. It is a pullback from a finite grid only after refining each partition by the finitely
  many subsets that occur (one per cell). After refining, F′ = g⁻¹(F̂), g surjective. F′ is box (difference of
  box indicators), and g has a section, so F̂ is box.
- Smallest infinite example checked by hand: F = A ⊔ B ⊔ C ⊔ K(S₀, evens, S₂) over ℕ³ with
  A = {x₀∉S₀, x₁ even, x₀ ≤ x₁}, B = {x₁ odd, x₂∈S₂, x₁ < x₂}, C = {x₂∉S₂, x₀∈S₀, x₂ < x₀}, S₀, S₂ infinite
  and co-infinite. Parts: S₀ᶜ→1, S₀→2; evens→0, odds→2; S₂→1, S₂ᶜ→0, all infinite. The mutual columns are
  exactly A, B, C; the two cyclic cells S₀×evens×S₂ and S₀ᶜ×odds×S₂ᶜ are full; all other cells empty after
  removal. Residue = pullback of K on 2³. ✓.

**Step 4.** "Finite grids: every box set is a carrier set." **CORRECT WITH FIXES.**
- Merge. If a ≃₁ b with F_a − F_b = h(x₁): let F^ be the pullback of F|_{X₀∖{a}} along a ↦ b (in D₃ by
  induction and pullback). Then {x₀=a, h=−1} ⊆ F^ and {x₀=a, h=1} ∩ F^ = ∅ (F_b is full, resp. empty, on those
  lines), and F = (F^ ∖ {x₀=a, h=−1}) ⊔ {x₀=a, h=1}. Removing a contained member and adding a disjoint one
  stay in a Dynkin system. ✓. Base: some |Xᵢ| = 1 ⇒ F is a window event.
- **Fix 2 (the all-K case is asserted, not proved, in C6).** Let all pairs at coordinates 1 and 2 also be
  K-related, X₀ = {a₀ = q, a₁, …, a_n} with the chain U₁ ⊊ … ⊊ U_n, V₁ ⊋ … ⊋ V_n. Put
  λ(y) = min{i : y ∈ U_i} ∈ {1..n+1}, μ(z) = 1 + max{i : z ∈ V_i} ∈ {1..n+1}. Then
  F(a_i,y,z) = G(y,z) + [λ(y) ≤ i] + [i < μ(z)] − 1 for i = 0..n, with G = F_q. As in Step 1,
  G(y,z) = [μ(z) < λ(y)] whenever λ(y) ≠ μ(z), and G is unconstrained where λ(y) = μ(z). If λ(y) = λ(y′) the
  two x₁-slices differ by G(y,·) − G(y′,·), a function of x₂ alone, so not K-related: λ is injective, and
  likewise μ. λ is onto (the U_i are n strictly increasing proper nonempty sets). So |X₀| = |X₁| = |X₂| = n+1
  and F = E_< := {[z<y] + [y<a] + [a<z] = 2} for the total order a₀ < {y₁,z₁} < a₁ < … < a_n < {y_{n+1},z_{n+1}}
  on the disjoint union of the alphabets, the order inside each pair {y_j,z_j} being z before y iff G(y_j,z_j) = 1.
- Swap. For any total order on the disjoint union, E_< is 0/1 valued, and exchanging two adjacent elements of
  different coordinates (say a and y) changes only [y<a] for that one pair: the indicator shifts by ±1 on the
  whole line {x₀=a, x₁=y}, so the line was entirely inside or entirely outside. So one window event is added
  or removed. **Fix 3:** the swap must be with the neighbour in the order (z₁ if G(y₁,z₁) = 1, else y₁); two
  swaps bring a₀ next to a₁, where their slices are equal, and the merge case applies to that (box) set. This
  replaces "sorting ends at a 1×1×1 grid" by one more use of the induction hypothesis.
- Consistency: "D₃ ⊊ B over ℕ" (gate file §2) is not contradicted; the induction is on finite size.
- Own recount (`reversal_check_step4.py`, own closure and own enumeration): |B| = |D₃| = 2350 on 2×3×3 and
  15,914 on 3×3×3, equal as sets. The reduction above, run as a procedure with assertions (equal sizes, chain,
  bijections, F = E_<, single-line swap) on every box set of 2×3×3, 3×3×3 and 3×3×4 (131,290): no failure.
  Evidence only.

**Step 5.** "F = W₀₁ ⊔ W₁₂ ⊔ W₂₀ ⊔ g⁻¹(F̂) ∈ D_fin." **CORRECT.** F̂ ∈ D₃(finite grid) = finitary closure
there; g⁻¹ preserves the finitary closure; a finite disjoint union of D_fin sets is in D_fin. Conversely
D_fin ⊆ D₃. Also {box, no infinite K-clique at any coordinate} ⊆ D_fin by Steps 2–4, and D₃ ⊆ that set by
`box_of_mem` and Step 1. So the three classes coincide.

**Final inference (same window family ⇒ same state).** **CORRECT.** T = {F : s(F) = Λ(1_F)} contains the window
events, Ω, complements and finite disjoint unions (Λ linear, s finitely additive). Λ is well defined on bounded
integer pair-sums: f₀₁ + f₁₂ + f₂₀ = 0 forces f₀₁ = h(x₀) + g(x₁), f₁₂ = −g + m(x₂), f₂₀ = −m − h, and the
marginals of the three window ultrafilters agree because a one-coordinate event lies in two windows. So s = Λ
on D_fin = D₃, and Λ depends only on the family.

## Sanity checks against machine-checked facts

- E*: for a < b, F_a − F_b = [a ≤ x₁ < b] − [a ≤ x₂ < b], K type. All of ℕ is a K-clique: excluded. ✓ `estar_not_mem`.
- `triangle_pointless_state`: sstar is a signed sum of three ultrafilters, additive on all sets, so sstar = Λ on
  D₃ trivially. The theorem only says no other state shares its window family. No conflict; pointless states remain.
- σ-additivity is not forced: the theorem fixes s from its family, it does not make the family principal.
- D¹ normal form (R0 ⊔ one antipodal pair) is the case F̂ = K on 2³. ✓.

## Counterexample attempts (countable disjoint union of finitary sets, not finitary)

1. Finite shells of E*: each lies in a product of proper subsets, so is not a carrier set (box identity).
2. Capped sets Ẽₙ: carrier sets, but neither nested nor disjoint, and their set differences are confined to
   proper products. No disjoint family built from them reaches E*.
3. Infinitely many disjoint antipodal pairs K({n}, A, ℕ∖{n}): disjoint and aligned at coordinate 1; the union
   is {x₀ ≠ x₂}, a window event.
4. Staircase pieces {x₀=n, x₁>n} ⊔ {x₁=n, x₂>n} ⊔ {x₂=n, x₀>n}: not disjoint across n; disjoint window events
   from two windows must use disjoint sets of values of the shared coordinate, which lands in R0.
5. Structural: by Steps 2–4 a non-finitary box set must contain an infinite K-clique, hence a sub-grid copy of
   the strict cyclic or anticyclic order, which Lean excludes for every member of D₃. So a counterexample
   would have to break Step 2, 3 or 4; the infinite-part example in Step 3 and the all-K derivation in
   Step 4 were the places tried, and both held.

## Gap

None. No missing lemma. For formalisation the natural order is: (i) pullback lemma for D₃ along coordinatewise
maps; (ii) the K-type dichotomy of slice differences; (iii) Step 1 via `not_inP_of_mem`; (iv) finite cover
(Step 2); (v) column lemmas and the residue (Step 3, with Fix 1); (vi) finite grids B = D₃ (Step 4 with
Fixes 2–3). Items (v) and (vi) are the long ones.

## Repaired proof (self-contained)

**Theorem.** For any sets X₀, X₁, X₂, D₃ = D_fin. Every F ∈ D₃ is W₀₁ ⊔ W₁₂ ⊔ W₂₀ ⊔ g⁻¹(F̂) with W_ij window
events, g a coordinatewise map onto a finite grid and F̂ a box set there.

1. (Box.) Every F ∈ D₃ satisfies the eight-corner identity; so every slice difference is α + β with the
   dichotomy of Step 1: one-coordinate, or [U] + [V] − 1 with U, V proper nonempty (K type).
2. (No infinite clique.) Infinitely many pairwise K-related values at one coordinate give, by the chain and
   sub-grid of Step 1, a coordinatewise g : ℕ³ → X with g⁻¹F equal to Acy or Cyc on all distinct triples;
   g⁻¹F ∈ D₃(ℕ³) contradicts `not_inP_of_mem`.
3. (Finite cover.) Step 2 above: each Xᵢ is a finite union of labelled parts.
4. (Columns and residue.) Step 3 above with Fix 1: F = W₀₁ ⊔ W₁₂ ⊔ W₂₀ ⊔ g⁻¹(F̂), F̂ box on a finite grid.
5. (Finite grids.) Step 4 above with Fixes 2–3: F̂ is in the finitary closure of the grid's window events.
6. (Conclusion.) g⁻¹(F̂) ∈ D_fin, so F ∈ D_fin. ∎

**Corollary.** Two finitely additive two-valued states on D₃ with the same window family are equal (s = Λ).

## What was not verified

- Lean was read, not compiled; `#print axioms` not run. The whole proof rests on `not_inP_of_mem` being as stated.
- Nothing in Steps 1–5 is in Lean. Two agents have now checked them by hand; that is not machine verification.
- The pullback lemma and `box_of_mem` over arbitrary alphabets are hand arguments (routine).
- C6's side remark "D_fin sets have finite clique number, independently of Lean (mixed clique at most 5
  values)" was not checked; it is not used.
- Prior art for D₃ = D_fin was not searched (out of scope here). It must pass the prior-art gate before being
  claimed, and the reversal must be propagated by a separate inventory.

## Bearing on WHY.md

Loop: the triangle's loop hides nothing beyond its window family. Unaskable joint question: the infinite cyclic
order is the one question the carrier cannot ask. Composition, not a circle. A lens only.
