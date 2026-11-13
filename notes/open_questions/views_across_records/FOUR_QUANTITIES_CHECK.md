reviewed: false. 2026-11-13. Independent hostile check by a fresh agent.

# Check of `FOUR_QUANTITIES_GATE.md`: D₄ = V₀₁ at every finite size (four quantities, every pair seen)

## Verdict
**CONFIRMED WITH FIXES.** Every step (T1–T4, Lemma A, Lemma B, both Propositions, the induction) was re-derived by
hand ⟦HAND⟧ and no step is wrong in substance. Three statements are misworded and one is false as literally stated
(Lemma A without the hypothesis "a and c are K-related"); the proof uses them only where the missing hypothesis holds,
so the theorem stands. All five scripts were rerun and reproduce the recorded numbers. Own code, written from scratch,
recounts 2×2×2×2 and 2×2×2×3 exactly over all subsets, and counts irreducible sets exhaustively at six further sizes
up to 4×4×4×4 (54 million sets, 142 s, peak 0.85 GB): none. No counterexample found. Status of the theorem after this check: hand, two readers, not Lean;
it rests on the finite triangle theorem (Lean over ℕ plus a short hand transfer). Prior art not searched (not my task).

## Items

**1. T1 (dichotomy).** "d = h₁+h₂+h₃ with values in {−1,0,1} … exactly one of: simple; K-type via {j,k}: d = [x_j∈U] +
[x_k∈V] − 1 with U, V proper and nonempty." **CORRECT.**
- g_j(x) = h_j(x) − h_j(x_j*) with x_j* a minimiser; this equals d(…x…) − d(…x_j*…) with the other two arguments
  fixed, so it is an integer in {0,1,2}. The minimum exists because h_j takes at most three values (no finiteness of
  the alphabet is needed).
- d = c + g₁+g₂+g₃ with c = d(x₁*,x₂*,x₃*) ∈ {−1,0,1}; max d = c + Σ max g_j ≤ 1, so Σ max g_j ≤ 1 − c ≤ 2.
- Sorted maxima: (0,0,0), (1,0,0), (2,0,0), (1,1,0); nothing else sums to ≤ 2. In (1,1,0), c + 2 ≤ 1 forces c = −1;
  g_j = [x_j∈U] with U = {g_j = 1} nonempty, and proper because min g_j = 0. (U, V) are determined by d
  (d = 1 exactly on U×V, −1 exactly on Uᶜ×Vᶜ). The two alternatives exclude each other.
- Machine evidence: enumerating all c + Σ g_j directly (no shape list) gives 183, 547, 825 differences on 3³, 3×4×4, 4³,
  equal to the shape counts (simple 75/183/237, K-type 108/364/588).

**2. T2 (merge).** "F_a is obtained from F_b by removing a contained set {x_j ∈ U₊} and adding a disjoint set
{x_j ∈ U₋} … So F ∈ D₄ iff the set with a merged into b is in D₄ of the smaller grid." **CORRECT WITH FIXES** (roles of
a and b swapped in the sentence; the argument is not written out).
- With d = 1_{F_a} − 1_{F_b} = δ(x_j), U₊ = {δ = 1}, U₋ = {δ = −1}: {x_j∈U₊} ⊆ F_a and misses F_b; {x_j∈U₋} ⊆ F_b and
  misses F_a. So **F_b** is obtained from **F_a** by removing the contained {x_j∈U₊} and adding the disjoint {x_j∈U₋}
  (this is what `k4_3333_stage2.py` verifies), not the other way round.
- Written out: F̂ := F restricted to (X₀∖{a})×X₁×X₂×X₃. It is a pair-sum 0/1 set there (restrict the six pair
  functions). π: a ↦ b, identity elsewhere. F′ := π⁻¹(F̂) has slice F_b at a and the old slices elsewhere. If
  F̂ ∈ D₄(small) then F′ ∈ D₄(big): the preimage of a pair event under a coordinatewise map is a pair event, and
  preimages commute with complement and disjoint union. Then F = (F′ ∖ {x₀=a, x_j∈U₋}) ⊔ {x₀=a, x_j∈U₊}. First move:
  the removed event lies in F′ because F′_a = F_b ⊇ {x_j∈U₋}; A∖B = (Aᶜ ⊔ B)ᶜ. Second move: after the removal the slice
  at a is F_b∖{x_j∈U₋}, still disjoint from {x_j∈U₊}. Both events belong to the query {0,j}. The order of the two moves
  is immaterial (U₊ ∩ U₋ = ∅). The converse ("only if") holds by restriction to the subgrid and is not used.
- Merged coordinate left with one value: allowed; the smaller grid then falls under case (i). d constant ±1: F_a is
  everything and F_b empty (or the reverse), any j works, the event is {x₀=a}. d = 0: no move.

**3. T3 / case (i).** "If some coordinate has one value left, F is a pullback from a triangle and the triangle theorem
applies (`TriangleFinitary.box_iff_mem_of_finDet` + the hand grid transfer)." **CORRECT**, with the split stated exactly:
- Hand: if X₃ = {∗}, then f₀₃, f₁₃, f₂₃ are functions of one coordinate and are absorbed; F is a pair-sum set on
  X₀×X₁×X₂. Pair events of the triangle's three queries are pair events of Ω, so the triangle closure sits inside D₄.
- Lean (read, not compiled; header says no `sorry`): over Ω = ℕ³, for R determined by finitely many labels
  (`FinDet`), `Box R ↔ Dfin R` (`box_iff_dfin_of_finDet`) and `Box R ↔ D₃.Has R` (`box_iff_mem_of_finDet`). `Dfin` is
  the closure under complement and binary disjoint union, which is the form needed.
- Hand transfer to finite alphabets of any sizes (three elementary steps, none in Lean): (α) pair-sum 0/1 ⇒ the
  eight-corner identity `Box` (each pair function cancels); (β) inject X_i into ℕ, choose retractions g_i, put
  R = g⁻¹(F): R is `FinDet` and `Box`, so `Dfin R`; (γ) restrict along the injection ι (g∘ι = id): ι⁻¹ maps window
  events to pair events of the grid and commutes with complement and disjoint union, and ι⁻¹(R) = F.
- Independent hand derivation of the finite triangle theorem exists (`TRIANGLE_D3_DFIN_REVERSAL_CHECK.md` Step 4,
  `TRIANGLE_CONSEQUENCES_CHECK.md` C2(c)); I did not re-derive it.

**4. T4 and the (I)/(II) dichotomy.** **CORRECT.**
- d = [x₁∈U]+[x₂∈V]−1 gives: on U×V×X₃, F_a full and F_b empty; on Uᶜ×Vᶜ×X₃ the reverse; on the mixed cells F_a = F_b.
- Box identity for A = 1_{F_b} (a triangle pair-sum set on coordinates 1,2,3), at y∈U, y′∈Uᶜ, z∈V, z′∈Vᶜ:
  A(y,z,t)+A(y′,z′,t)+A(y′,z,t′)+A(y,z′,t′) = A(y′,z,t)+A(y,z′,t)+A(y,z,t′)+A(y′,z′,t′). The left corners have 0,2,2,2
  primes, the right ones 1,1,1,3: these are the right eight points. With A(y,z,·) = 0 and A(y′,z′,·) = 1 this is
  s(t′) = s(t) for s := A(y′,z,·) + A(y,z′,·).
- If some A(y₀′,z₀,·) is not constant, put T = {t : A(y₀′,z₀,t) = 1}, proper and nonempty. For every (y,z′) ∈ U×Vᶜ:
  A(y,z′,·) = s − 1_T is 0/1 valued, so s = 1 and A(y,z′,·) = 1_{Tᶜ}. Then for every (y′,z) ∈ Uᶜ×V, against one fixed
  (y,z′): A(y′,z,·) = 1_T. Same T everywhere; the symmetric start gives the same conclusion. Otherwise A is constant
  in t on every mixed cell, and on the diagonal cells anyway: (II).
- Nothing about |X₀| is used. For |X₀| = 2 (II) gives "F independent of x₃". In (I), F = pullback of A₄ along
  p = [x₀=a], u = [x₁∈U], v = [x₂∈V], t = [x₃∈T]; C and K are disjoint (u ≠ v on C, u = v on K).
- Note: a single cell {011} is not a carrier set; the antipodal pairs are. Explicitly, with seven pair events:
  C = ({u=0,v=1} ⊔ {u=1,t=0}) ∖ {v=1,t=0},  K = ({p=0,u=0} ⊔ {p=1,v=1}) ∖ {u=0,v=1}. So A₄ ∈ D₄ without the triangle theorem.

**5. Lemma A.** "Let a, b be K-related via {1,2} in case (I), and c a third value K-related to b. Then contradiction."
**CORRECT WITH FIXES** (false as stated; true with "a, b, c pairwise K-related").
- (b,c) via {1,2}, d_bc = [x₁∈U′]+[x₂∈V′]−1: F_b is full on U′×V′×X₃ and empty on U′ᶜ×V′ᶜ×X₃. In form (I), T proper
  and nonempty makes the mixed cells neither full nor empty across x₃, so "full for all x₃" happens exactly on Uᶜ×Vᶜ
  and "empty for all x₃" exactly on U×V. Hence U′ = Uᶜ, V′ = Vᶜ, d_bc = −d_ab, d_ac = 0, F_c = F_a. That is **not a
  contradiction by itself** (c may duplicate a); it contradicts "a, c K-related".
- (b,c) via {1,3}, (U′,W): F_b full on U′×X₂×W, empty on U′ᶜ×X₂×Wᶜ. From (I): for x₁∈Uᶜ the x₂-line contains Vᶜ always
  and V iff t∈T; for x₁∈U it misses V always and contains Vᶜ iff t∈Tᶜ. So full for all x₂ iff (x₁∈Uᶜ, t∈T); empty for
  all x₂ iff (x₁∈U, t∈T). Then W ⊆ T and Wᶜ ⊆ T, so T = X₃, against T proper. A contradiction with no extra hypothesis.
- (b,c) via {2,3}, (V′,W): full for all x₁ iff (x₂∈Vᶜ, t∈Tᶜ); empty for all x₁ iff (x₂∈V, t∈Tᶜ). So Tᶜ = X₃. Same.
- The statement for a third value K-related to a follows by the symmetry (a,b,U,V,T) ↔ (b,a,Uᶜ,Vᶜ,Tᶜ).

**6. Lemma B.** "The three types are all equal or all different." **CORRECT.** Each of d_ab, d_bc, d_ac is ± a
combination of the other two. If two have type {1,2}, the third is a function of (x₁,x₂) and, being K-type, has type
{1,2}. So two equal types force three equal. Types {1,2} with (U,V) and {1,3} with (U′,W):
d_ac = ([U]+[U′])(x₁) + [V](x₂) + [W](x₃) − 2 depends on x₂ and on x₃, so by T1 it does not depend on x₁:
[U]+[U′] is constant, and the constants 0 and 2 are excluded by properness, so U′ = Uᶜ and d_ac = [V]+[W]−1. No
possibility is overlooked: "the third difference simple" is excluded by the hypothesis pairwise K-related, used correctly.

**7. Proposition (irreducible ⇒ two values everywhere).** **CORRECT** (one sentence can be sharpened).
- Lemma A applies to every pair at coordinate 0 because a third value exists and all pairs are K-related (this is
  where the repaired hypothesis is available). So every pair is in case (II) for its own type.
- (a) One type {1,2} throughout: every value lies in a pair, so every slice, hence F, is independent of x₃; X₃ has ≥ 2
  values by the definition of irreducible; two of them have equal slices (d = 0). ✓
- (b) Complete graph on X₀, edges coloured by type, every triangle one-coloured or three-coloured (Lemma B). Two edges
  of different colours sharing a vertex span a three-coloured triangle. If they are disjoint, ab and ce, the edge bc
  differs in colour from ab or from ce, which gives the first situation. ✓
- (c) Types ab {1,2}, bc {1,3}, ac {2,3}; case (II) three times: F_a is independent of x₃ and x₁, F_b of x₃ and x₂,
  F_c of x₂ and x₁. So F_a = {x₂∈S_a}, F_b = {x₁∈S_b}, F_c = {x₃∈S_c}, each S proper and nonempty. For a further e:
  type {1,3} for (a,e) gives 1_{F_e} = [x₂∈S_a] − [x₁∈U] − [x₃∈W] + 1 = 2 at x₂∈S_a, x₁∉U, x₃∉W. ✓ Type {1,2}:
  1_{F_e} = ([S_a]−[V])(x₂) + [x₁∈Uᶜ]; the second term takes both values, so the first vanishes and F_e = {x₁∈Uᶜ};
  type {2,3} likewise gives F_e = {x₃∈Wᶜ}. ✓
- Sharper (not needed): no further e exists. From a: F_e reads x₁ or x₃ only; from b: x₂ or x₃ only; from c: x₁ or x₂
  only; F_e is not constant; impossible. So in the three-type case |X₀| = 3 and the selector reads three different
  coordinates.
- (d) For a selector F = ⊔_e {x₀=e}×{x_{σ(e)}∈S_e} and two values y, y′ of x₁, the slice difference is
  Σ_{e: σ(e)=1} [x₀=e]([y∈S_e] − [y′∈S_e]), a function of x₀ alone (zero if no e reads coordinate 1). So **every** pair
  at coordinate 1 is simple, whatever the patterns; X₁ has ≥ 2 values. The statement in the note is right as it stands.

**8. Proposition (the atom).** **CORRECT.** On 2×2×2×2 the one pair at coordinate 0 is K-related via some {j,k}; case
(II) would make F independent of the third coordinate ℓ, and then the two values of x_ℓ have equal slices: reducible.
So case (I), with U, V, T singletons: F is A₄ after a permutation of coordinates 1,2,3 and relabelling. (Case (I) at
coordinate 0 alone suffices; "at each coordinate" is true but not needed.) A₄ ∈ D₄: item 4.
- `k4_irreducible_small.py`: its test "no coordinate has two values whose difference depends on at most one other
  axis" is the definition (all sizes run have ≥ 2 values everywhere). It compares the 24 sets with the orbit as sets
  (`orbit==irr2` on byte strings). Rerun: 222/24, 1,006/0, 5,134/0, 23,206/0, orbit equal. Its header comment says
  "16-world pattern"; the pattern has 8 worlds (the script prints 8).
- Own recount: item 10.

**9. The induction.** **CORRECT.** Statement P(N): on every grid with N values in total, every pair-sum 0/1 set is in
D₄. Cases: (i) some coordinate has one value: triangle theorem, no induction; (ii) all coordinates ≥ 2 values and some
pair is simple (d = 0 included: identical slices are shape (0,0,0)): merge, N drops by exactly 1; (iii) all ≥ 2 and no
simple pair: this is the definition of irreducible, so the grid is 2×2×2×2 and F is an image of A₄. Exhaustive and
disjoint. No step assumes ≥ 3 values. The symmetry of K₄ is used (every coordinate can play coordinate 0; every pair
{j,k} is a query): the argument does not transfer to a window graph with a missing pair.

**10. Scripts.** All five do what the note says; all rerun in a scratch copy (so no file in the repo was rewritten).
- `k4_closed.py`: square 82/90 gap 8; K₄ 222, 1,006, 5,134, 23,206, gap 0, D ⊆ V₀₁ True; 2×3×3×3 in 41 s, peak 1.2 GB
  (the note says 1.1). Caveats: float32 tolerance (as the note says); the closure loop stops when |D| reaches |V₀₁|,
  so it certifies D = V₀₁ only together with D ⊆ V₀₁ (printed), not closedness independently.
- `k4_3333_stage1.py`, `_sanity.py`, `_stage2.py`: 15,914; 183; 67,742 all reducible; 23,206; 144; certificates verified
  for 67,742 and 466,630. Caveat: the list of slice differences is built from T1's shapes, so the enumeration of V₀₁
  depends on T1 (correct; and my shape-free enumeration gives the same 183).
- **Own recount** (`../verification/four_quantities/check_bruteforce_2222_2223_exact.py`; all 65,536 and all 16,777,216
  subsets; span membership by exact integer orthogonality to a sympy nullspace; closure run to a fixpoint):
  2×2×2×2: rank 11, |V₀₁| = 222, |D₄| = 222, equal as sets, 24 irreducible = orbit of A₄ (24 with or without
  complement). 2×2×2×3: rank 15, |V₀₁| = 1,006 = |D₄| as sets, 0 irreducible. Agrees with the table.

**11. Attempt to refute.** No counterexample. Given items 2, 3 and 9, D₄ ≠ V₀₁ at some size would require an
irreducible set that is not an image of A₄, so I searched for irreducible sets.
- `check_exhaustive_irreducible_3344_4444.py` (own slice enumeration: first slice any triangle pair-sum set, itself
  built from an arbitrary 2-D slice; differences from the normal form, not from T1's shapes; every tuple of distinct
  nonzero differences tested; equal slices are reducible by definition). Validated: 222/24, 67,742/0, 466,630/0.

  | size | \|V₀₁\| (count by slices) | irreducible |
  |---|---|---|
  | 2×2×4×4 | 393,870 | 0 |
  | 2×3×4×4 | 1,584,478 | 0 |
  | 2×4×4×4 | 12,997,662 | 0 |
  | 3×3×4×4 | 3,166,270 | 0 |
  | 3×4×4×4 | 17,406,718 | 0 |
  | 4×4×4×4 | 53,994,750 | 0 |

- `check_random_certificates_3344_4444.py`: full certificate procedure (verified merges down to a one-valued
  coordinate or an irreducible set) on sampled sets: 3×3×4×4, 11,415 sets; 4×4×4×4, 51,489 sets (approximately
  uniform stratum plus two strata with distinct, resp. K-type, slice differences). Every run ended at a one-valued
  coordinate (62,836) or at an image of A₄ on 2×2×2×2 (68). No other irreducible endpoint.
- Not covered: any size with a coordinate ≥ 5; the endpoints "one-valued coordinate" were not re-checked against a
  triangle closure (that is the triangle theorem). Computation is evidence only for the all-sizes statement.

**12. Scope and wording.** **CORRECT WITH FIXES.**
- The theorem needs: four coordinates, all six pairs as queries, finite nonempty alphabets. Nothing else. Finiteness
  enters only through the induction and the finite triangle theorem; T1, T4, Lemmas A, B and the Proposition hold for
  any alphabets.
- "Reading": "A₄ … exists only with two values and vanishes as soon as any quantity has a third" is true only of
  **irreducible** sets. Pullbacks of A₄ occur at every size (T4 case (I) with any U, V, T); they are reducible because
  values inside U, V, T duplicate each other. "Two kinds of atom" mixes two notions: A₄ is irreducible in the
  four-coordinate sense; the cyclic orders are irreducible on a triangle and, seen on four coordinates, reducible
  (the fourth coordinate has equal slices). Accurate version: the reduction ends either at a triangle pair-sum set
  or at A₄.
- Gate 1 "Reading" and the "Consequence for the gate (tempering)" are accurate. Gate 2's "no irreducible set at all"
  is accurate for 3333 and 3334 and was already corrected for 2222. The 3×3×3×4 base remark is accurate.
- Setup, "Criterion for V₀₁: the eight-corner identity on every three coordinates with the fourth held fixed": correct
  ⟦HAND⟧ (it kills all three-way terms, and the four-way term is a difference of three-way terms of slices; dimension
  check 16 − 11 = 4 + 1 on 2⁴). The proof uses only the easy direction.
- Not addressed by the theorem: infinite alphabets (D₄ vs. a finitary closure; which box sets are shut out); whether an
  additive function on D₄ is determined by its values on the queries (S2₄) and whether compatible couplings extend to a
  state; S3₄; five or more quantities; window graphs other than K₄.

## Fixes to apply (exact, minimal)
1. T2, first sentence: "F_b is obtained from F_a by removing the contained set {x_j ∈ U₊} and adding the disjoint set
   {x_j ∈ U₋}" (U₊ = {d = 1}, U₋ = {d = −1}); add the three-line argument of item 2 (F̂, π, the two moves).
2. Lemma A, hypothesis: "Let a, b, c be pairwise K-related at coordinate 0, with a, b via {1,2} in case (I)." First
   bullet ends "…so F_c = F_a, against a, c K-related."
3. Proposition (atom): replace "is in case (I) at each coordinate, hence" by "is in case (I) at coordinate 0 (case (II)
   makes F independent of a coordinate, hence reducible), hence".
4. T4(I): add the explicit decompositions of C and K (item 4), so that A₄ ∈ D₄ does not lean on the triangle theorem.
5. T3: name the three hand steps (α)–(γ) of item 3 as what "hand grid transfer" means.
6. "Reading": replace by the accurate version in item 12.
7. Optional: in the Proposition, note that the three-type case forces |X₀| = 3. `k4_irreducible_small.py` header:
   "16-world" → "8-world". Gate 1: peak 1.2 GB.

## The repaired proof (hand source for a later formalisation) ⟦HAND⟧
**Setting.** Ω = X₀×X₁×X₂×X₃, alphabets finite and nonempty. A *pair event* is a set depending on two coordinates.
D₄ = closure of the pair events under complement and disjoint union. F is a *pair-sum set* if 1_F is a sum of six
functions of two coordinates each. **Theorem.** Every pair-sum set is in D₄ (so D₄ = V₀₁).

**L0 (maps).** For a coordinatewise map φ between grids, φ⁻¹ sends pair events to pair events, pair-sum sets to
pair-sum sets, and D₄ to D₄. D₄ is invariant under permuting coordinates. A∖B ∈ D₄ for B ⊆ A in D₄.
**L1 (slice differences).** For values a ≠ b of x_i, d_ab := 1_{F_a} − 1_{F_b} is a sum of one-coordinate functions of the
other three coordinates with values in {−1,0,1}. Either d_ab depends on at most one coordinate (*simple*), or
d_ab = [x_j∈U]+[x_k∈V]−1 with U, V proper nonempty (*K-related via {j,k}*). (Item 1.)
**L2 (merge).** If d_ab = δ(x_j) and F restricted to X_i∖{a} is in D₄ of that grid, then F ∈ D₄. (Item 2.)
**L3 (triangle).** If some coordinate has one value, F ∈ D₄. (Item 3: Lean over ℕ³ + steps (α)–(γ).)
**L4 (K-pairs).** Let a, b at coordinate 0 be K-related via {1,2} with (U,V). Then F_a ⊇ U×V×X₃, F_b ∩ (U×V×X₃) = ∅,
F_b ⊇ Uᶜ×Vᶜ×X₃, F_a ∩ (Uᶜ×Vᶜ×X₃) = ∅, F_a = F_b on the mixed cells, and either (II) F_a, F_b do not depend on x₃, or
(I) there is a proper nonempty T ⊂ X₃ with F_a = F_b = Uᶜ×V×T ⊔ U×Vᶜ×Tᶜ on the mixed cells. (Item 4.) Same for any
coordinate and any pair {j,k}, with ℓ the remaining coordinate.
**L5 (A₄).** A₄ := {(u,v,t) ∈ {011,100}} ⊔ {(p,u,v) ∈ {000,111}} ⊆ {0,1}⁴ is in D₄ (seven pair events, item 4). In case
(I) with X₀ = {a,b}, F is the preimage of A₄ under p = [x₀=a], u = [x₁∈U], v = [x₂∈V], t = [x₃∈T].
**L6 (no third value in case (I)).** If a, b, c are pairwise K-related and a, b are via {1,2}, then a, b are in case
(II). (Item 5: in case (I), d_bc via {1,2} forces F_c = F_a; via {1,3} forces T = X₃; via {2,3} forces Tᶜ = X₃.)
**L7 (types).** For a, b, c pairwise K-related the three types are equal or pairwise different. (Item 6.)
**L8.** Call F *irreducible* if every coordinate has ≥ 2 values and no pair of values at any coordinate is simple.
Then every coordinate has exactly two values. Proof: suppose |X₀| ≥ 3. By L6 every pair at coordinate 0 is in case (II).
If all types equal {j,k}, F does not depend on x_ℓ, and two values of x_ℓ are a simple pair. Otherwise (L7 and the
colouring argument of item 7(b)) some a, b, c have types {1,2}, {1,3}, {2,3}; case (II) gives F_a = {x₂∈S_a},
F_b = {x₁∈S_b}, F_c = {x₃∈S_c}; any further value e has F_e depending on one coordinate (in fact there is none), so
F = ⊔_e {x₀=e}×{x_{σ(e)}∈S_e}, and any two values of x₁ differ by a function of x₀: a simple pair. Contradiction.
**Proof of the theorem.** Induction on N = |X₀|+|X₁|+|X₂|+|X₃|. If some coordinate has one value: L3. Else if some pair
is simple: the restriction is a pair-sum set on a grid with N−1 values, in D₄ by induction, so F ∈ D₄ by L2. Else F is
irreducible; by L8 the grid is 2×2×2×2; the pair at coordinate 0 is K-related via some {j,k}; case (II) would make F
independent of x_ℓ, a simple pair; so case (I), and F is a relabelled A₄ with coordinates 1,2,3 permuted: in D₄ by L5, L0. ∎
**Formalisation notes.** L1 and L4–L8 are finite case analyses on integer-valued functions and need no finiteness of
the alphabets. L3 is the only import. The natural Lean statement is over ℕ⁴ for sets determined by finitely many
labels, mirroring `FinDet`/`DetN` and `merged_dfin`/`step0` in `TriangleFinitary.lean`.

## Not verified
- Lean was read, not compiled; the triangle theorem's proof (Lean or hand) was not re-derived here.
- Prior art: not searched. Kellerer 1964 Satz 1.1 and the Ranta–Lundberg–Kaitala lens: not checked against sources.
- "Positivity fails / pentagonal facet takes the value 3" (forcedness paragraph): not checked.
- "72 = the relabelled cyclic orders on the 3×3×3 face" (gate 1): not checked (the note says so too).
- Exhaustive V₀₁ counts above 2×2×2×3 are by the slice construction (mine and the author's are separate code but the
  same idea); only 2×2×2×2 and 2×2×2×3 are confirmed by brute force over all subsets with exact arithmetic.
- Sizes with a coordinate ≥ 5; infinite alphabets; S2₄, S3₄; five quantities; other window graphs.
