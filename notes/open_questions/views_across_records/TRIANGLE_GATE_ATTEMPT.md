# Triangle gate attempt: does the window family fix the state on the infinite triangle?

reviewed: false. 2026-11-06. Machine-assisted. ⟦HAND⟧ marks arguments checked by neither Lean nor an independent agent.
Prior art for level 1: NOT FOUND, UNCLEAR (`TRIANGLE_LEVEL1_CHECK.md`); nothing here is claimed as new. Scripts: `../verification/triangle_gate/` (moved from the job tmp dir 2026-11-07)
(`checks.py`, `two_vertex.py`, `kform.py`, `altrank.py`). Gate source: `CONVEX_GLUING_T1_ATTEMPT.md` §7.

> **2026-11-07 update.** Level-1 rigidity is **⟦HAND, independently checked⟧** (`TRIANGLE_LEVEL1_CHECK.md`: correct with
> fixes, now applied in Steps 3–4). §3b gives a shorter proof that needs no ultrafilter and a normal form for D¹, also
> **independently checked** (`TRIANGLE_3B_CHECK.md`: correct). The restated L1 in §5 was first overstated as "the whole
> gate"; corrected the same day: it is the level-2 step only. A second round adds finite cyclic orders, possibly padded
> by window events (§5a, computed on three grids). Prior art for level 1: NOT FOUND (nearest Navara–Pták 1983 Thm 1, Navara 1984).

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
  - Reason: K(S)∩K(T) = ∅ needs four empty cube intersections, hence four coordinates (not necessarily distinct):
    i_a with Sᵢ∩Tᵢ = ∅ (S-cube vs T-cube), i_b with Sᵢ∪Tᵢ = Xᵢ (co-cubes), i_c with Sᵢ ⊆ Tᵢ (S-cube vs Tᶜ-cube),
    i_d with Tᵢ ⊆ Sᵢ. With three coordinates, two of the four conditions share one (pigeonhole). The six pairings:
    (a,b) ⇒ Tᵢ = Sᵢᶜ; (c,d) ⇒ Tᵢ = Sᵢ; (a,c) ⇒ Sᵢ = ∅; (a,d) ⇒ Tᵢ = ∅; (b,c) ⇒ Tᵢ = Xᵢ; (b,d) ⇒ Sᵢ = Xᵢ. The last
    four contradict nondegeneracy. No finiteness is used (check, 2026-11-07).
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
- **D₃(2×X×Y) ⊆ B(2×X×Y)** (fix 2026-11-07; this was used but not argued): B is the eight-corner identity, which is
  checked pointwise, and a countable disjoint union meets each 8-corner set in at most 8 pieces, so B is closed under
  countable disjoint unions and complements. This is Lean `box_of_mem` (`TriangleCyclic.lean`, over ℕ³); the argument
  works for any alphabet.
- So every set of D₃(2×X×Y) is either in R0 or of the form K(U,V) ⊔ ({1,2}-event); both are finitary, so
  **D₃(2×X×Y) ⊆ D_fin**, and every state's value there is fixed by its family.
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

## 3b. A shorter proof, and a normal form for D¹ ⟦HAND, 2026-11-07; independently checked, `TRIANGLE_3B_CHECK.md`⟧

- **No ultrafilter is needed in Step 5.** Fix any index m. Every n lies in [m]₀ ∪ [m]₁ ∪ [m]₂ (Step 3). Assign each n
  to the first class containing it. Each class is aligned at one coordinate i with one set Aᵢ (after replacing Sⁿ by
  its full complement where needed, which leaves Kₙ unchanged).
- So K* = K*₀ ⊔ K*₁ ⊔ K*₂, and each K*ᵢ = πᵢ⁻¹(L) with L ∈ D₃(2-point vertex at i), using πᵢ(x) = ([xᵢ ∈ Aᵢ], x_j, x_k).
  By Step 4, L is in R0 or is K(U,V) ⊔ (window event). Pulled back, K*ᵢ is a window-event union or one antipodal pair
  plus a window event.
- **Normal form.** D¹ = {R ⊔ K¹ ⊔ K² ⊔ K³ : R ∈ R0, at most three disjoint nondegenerate antipodal pairs}. In
  particular **D¹ ⊆ D_fin**, so rigidity on D¹ is the finitary forcing of §2, and Step 5's ultrafilter is not needed.
- **Sharper (checker's hand argument, not independently checked):** "at most three pairs" can be "at most one". Two
  disjoint pairs align, so their union pulls back from the two-point vertex, where Step 4 leaves at most one pair.
  Finite data agree (3³, 2×3×3, 2×3×4; unions of two pairs on 3×3×4 and 3×4×4, 0 failures).
- **Worked case.** Ω∖(A ⊔ K(S)), with A a {0,1}-event inside {x₀∉S₀, x₁∈S₁}, equals
  W′₀₁ ⊔ {x₀∉S₀, x₁∈S₁, (x₀,x₁)∉A} ⊔ K(S₀, S₁, S₂ᶜ), where W′₀₁ = {x₀∈S₀, x₁∉S₁}. That is again of the D¹ form: the
  complement trades one antipodal pair for another.

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

**L1, restated after §3b (2026-11-07; corrected after `TRIANGLE_3B_CHECK.md`).** Since D¹ ⊆ D_fin and D_fin is closed
under complements, D² ⊆ {countable disjoint unions of D_fin sets} (equality iff D_fin ⊆ D²; true on every tested grid,
unproved over ℕ). The **level-2 step** is therefore: **do two states with the same window family agree on countable
disjoint unions of finitary carrier sets?** (Not "does every state add up over them": that fails for every
non-principal family, since window singletons are already finitary.) Levels D³ and above are not touched by this.
A sufficient condition for the whole gate is "D_fin is σ-closed", i.e. D₃ = D_fin: then every state is fixed by its
family, and O1 holds on the triangle.

**§5a. What a second round adds: cyclic orders (computed 2026-11-07, `orbit.py`, `r2check.py`).**
- At 3×3×3 the Dynkin closure is reached at round 2 (R2 is closed under complement and disjoint union), so the "72 sets"
  claim is now verified, not dependent on `altrank`.
- The 72 sets outside the D¹ form are **exactly** the images of E*∩[3]³ under independent relabellings of the three
  coordinates (orbit size 72, equal as sets). Here E* is "exactly two of x₀ ≤ x₁, x₁ < x₂, x₂ < x₀", a cyclic order.
  Each has 9 points; their complements (18 points) are already of the D¹ form.
- So on the smallest grid the only thing a second round adds is **a finite cyclic order**.
- **Larger grids (`TRIANGLE_3B_CHECK.md`):** 2×3×4: nothing new (Step 4). 3×3×4: 1,296 new sets, all cyclic-order sets.
  3×4×4: 28,512 new sets; 26,784 are cyclic-order sets and the other 1,728 are a cyclic-order set ⊔ an R0 set. Here a
  "cyclic-order set" is the positive cyclic order of some interleaving of the labelled values, a wider family than
  relabelled E* (they coincide at 3³). Every finite cyclic-order set is in D₃; E* over ℕ is not. And the infinite cyclic
  order E* is in B but not in D₃ (Lean `estar_not_mem`).
- **Sharpened L1 question.** Over ℕ, can countably many disjoint finitary sets, for instance finite cyclic-order patches
  (possibly padded by window events), add up to a set on which two states with the same family disagree? A yes needs a union whose pieces sum to 0 while the
  union gets 1, which is exactly the shape of E* built as a limit of its finite truncations, except that E* itself is
  excluded from the carrier.

**§5b. Stacking probe: pre-registered 2026-11-07 (before running).**
- **Facts (⟦HAND⟧).** (1) Pullback along any coordinatewise map maps D₃ into D₃. Hence for finite A ⊆ [n]³:
  A ∈ D₃(ℕ³) ⟺ A ∈ D₃([n+1]³) (collapse values ≥ n; include [n+1] ⊂ ℕ), and A ∈ D₃(ℕ³) ⇒ A ∈ D₃(grid with a spare
  value on any one coordinate). (2) A Dynkin system is closed under increasing unions, E* = ⋃ₙ E*∩[n]³, and E* ∉ D₃
  (Lean). So **some finite truncation E*∩[n]³ is not in D₃(ℕ³)**, though E*∩[3]³ ∈ D₃([3]³).
- **Gate P-stack.** Is E₃ := E*∩[3]³ in D₃ of 4×3×3, 3×4×3 and 3×3×4 (one spare value)?
  - NO on some grid ⇒ E₃ ∉ D₃(ℕ³): finite cyclic orders are carriers only when they use every value; the shells of E*
    are not available, and the stacking route is blocked at its first piece. Affects: the sharpened L1 question
    (rephrase as "which finite sets are in D₃(ℕ³)?"), `conj.window_restriction_r` (level 2).
  - YES on all three ⇒ necessary condition passes; locate the first n with E*∩[n]³ ∉ D₃([n+1]³) (needs n ≥ 4).
- **FIRED 2026-11-07: NO on all three** (`pstack.py`: E₃ ∉ D₃ of 4×3×3, 3×4×3, 3×3×4; |D₃| = 131,290 each). So
  E₃ ∉ D₃(ℕ³), as pre-registered.
- **Control (`pstack_control.py`) tempers the reading.** On 3×3×4, only 2,744 of the 15,914 carrier sets of 3³ remain
  carrier sets when x₂ has a spare value; 13,170 are lost, of every size 3–24. So losing E₃ is generic, not special to
  cyclic orders, and "which finite sets are in D₃(ℕ³)" is not the informative rephrase.
- **What the gate does show.** Finite-grid carrier sets live in ℕ³ only as *collapse pullbacks*: the top value means
  "≥ that value". So the ℕ-sets available are Ẽₙ := {x : E* holds at (min(x₀,n−1), min(x₁,n−1), min(x₂,n−1))}, all in
  D₃(ℕ³). Ẽₙ → E* pointwise (not monotonically), and E* ∉ D₃. **Reformulated L1 probe:** E* is a pointwise limit of
  carrier sets that is not a carrier set. Do two states with the same window family agree on the Ẽₙ eventually, and
  can a countable disjoint rearrangement of pieces of the Ẽₙ stay in the carrier? Affects `conj.window_restriction_r`.
- §5a's counts are unaffected: they describe collapse pullbacks, which are legitimate ℕ-sets.

**§5c. What a state does on the capped sets: every finite shadow is a point ⟦HAND, 2026-11-07; not independently checked⟧.**
- **Worked case.** Free window family (all marginals pᵢ non-principal). 1_{Ẽₙ} = [c₀≤c₁] + [c₁<c₂] + [c₂<c₀] − 1 with
  cᵢ = min(xᵢ, n−1), each term a window event. On {xᵢ, xⱼ ≥ n−1}, a set of value 1 for u_ij, the caps tie: cᵢ = cⱼ.
  So u₀₁(c₀≤c₁) = 1, u₁₂(c₁<c₂) = 0, u₂₀(c₂<c₀) = 0, and Λ(Ẽₙ) = 0. Ẽₙ is finitary (a pullback of a finite-grid set),
  so s(Ẽₙ) = Λ(Ẽₙ) = 0 for **every** state with a free family, for every n. Capping sends all three coordinates to
  the corner (n−1, n−1, n−1), where everything is tied and E* fails.
- Compare E* itself: Λ(E*) = u₀₁(x₀≤x₁) + u₁₂(x₁<x₂) + u₂₀(x₂<x₀) − 1 reads the *order at infinity* in each window,
  and is 2 for a cyclically oriented (staircase-type) family, which is why E* cannot be a carrier set. The capped
  approximations see none of this, so **the route "approximate E* by carrier sets" yields no disagreement.**
- **General form.** For any coordinatewise map g into a finite grid G and any A ∈ D₃(G): s(g⁻¹A) = [g(p) ∈ A], where
  g(p) = (g₀₊p₀, g₁₊p₁, g₂₊p₂) is the image point. Reason: g⁻¹A is finitary, so s = Λ; each window value is the
  pushforward of u_ij to a finite set, a point fixed by the marginals; and the pair-sum of 1_A evaluated there is 1_A(g(p)).
- **Reading.** Every state, pointless or not, looks like a point on every finite coarse-graining: the point
  (p₀, p₁, p₂) of βℕ×βℕ×βℕ. What the windows add is the *order between* coordinates at infinity (which tensor
  product, p⊗q or q⊗p), and that is exactly the gap between βℕ×βℕ×βℕ and β(ℕ³) (owned: Hindman–Strauss §11.1, read).
  So a disagreement, if any, is invisible at every finite resolution. (Corrected same day: it does *not* follow that it
  must live in sets that are not finite-grid pullbacks, since window events such as {x₀ ≤ x₁} are not pullbacks yet are
  forced. What follows is that any disagreement must use the order at infinity carried by window events, combined by
  countable unions into a set outside D_fin, which §2 already requires.)

**L1 (level-2 step, as first stated).** Pairwise disjoint complements of D¹ sets (equivalently, co-covering Hₙ ∈ D¹) admit an alignment
lemma like Step 3. Then a 𝒰-large subfamily is a pullback along a coordinatewise map with one finite coordinate.
- This needs a normal form for co-D¹ sets. Finite evidence that they are genuinely new: at 3×3×3, the closure of window
  events and antipodal pairs under disjoint unions misses 72 sets of D₃ (`kform.py`); §5a identifies them.
- Literature that might supply it (neither book is on the shelf; both are pinned hardcopy checks, `pinned_book_checks.md`):
  - Pták–Pulmannová 1991, the concrete-logic chapters: σ-classes generated by several sub-σ-algebras, disjoint-union
    normal form. Exact location unverified.
  - Bhaskara Rao, *Theory of Charges*, Ch. 3 (esp. §3.2): {0,1}-charges on complement- and disjoint-union-closed
    domains, and the extension criterion. Exact theorem unverified.
- Read in full, and not supplying it: Gudder 1984, Zerbe–Gudder 1985, DNP 2015.
- DNP 2007 has been read only from Ex 2.2 to Thm 2.3 (its index entry is abstract-only).

**L2 (one finite vertex).** For finite m ≥ 3, every state on D₃(m×X×Y) is determined by its window family (proved for
m = 2, Step 4). With L1 this closes level 2. The transfinite step needs L1 at every level, stated uniformly.

**L1′ (first labelled a shortcut; the check shows it is not).** On ℕ³ it *is* the principal sub-gate (σ-additive
marginals on a countable set are principal), so it opens no new route (`TRIANGLE_LEVEL1_CHECK.md` (b)). "A two-valued state on the Dynkin join of three σ-algebras, σ-additive on
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
