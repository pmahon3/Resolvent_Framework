# Independent check of TRIANGLE_GATE_ATTEMPT.md §3b, §5 (restated L1), §5a

reviewed: false. 2026-11-07. Hostile check. Scripts in `../verification/triangle_gate/`:
`check3b.py`, `check5a.py`, `check5a_cyc.py`, `look344.py`, `look344b.py` (new); `orbit.py`, `r2check.py` (rerun).
Every job peaked under 0.7 GB.

**1. Ultrafilter-free argument: CORRECT** ⟦HAND⟧.
- ~ᵢ is an equivalence relation, because {A, Aᶜ} partitions the subsets of Xᵢ into classes.
- ~ᵢ is well defined. Nondegenerate K(S) fixes S up to full complement: the slice of K through any point of the
  S-cube recovers each Sᵢ. Machine check: the tuple-to-mask map is exactly 2:1 (216→108, 504→252, 1176→588).
- Normalising by the full complement leaves Kₙ unchanged.
- Aᵢ is proper, so πᵢ is onto and πᵢ⁻¹ is injective on sets. Hence disjoint Kₙ give disjoint Lₙ = K(Uₙ,Vₙ), which lie
  in co-R0(2XY). So L = ⊔Lₙ ∈ D¹(2XY).
- πᵢ⁻¹ preserves complements and disjoint unions and sends window events to window events. So
  {L : πᵢ⁻¹L ∈ D₃} is a Dynkin system containing the generators.
- Step 4 classifies all of B(2XY) ⊇ D₃(2XY) by a pointwise argument, so it applies to the infinite union L.

**2. Normal form: CORRECT.**
- "=" holds, read as a disjoint union.
  - ⊆: the R0 pieces and the degenerate pairs regroup into one R0 set (Step 1). The window events from the pulled-back
    Lᵢ are disjoint pieces of F, so they are absorbed as well.
  - ⊇: R is in R0, and each pair is co-R0, so a disjoint union of them is in D¹.
- D¹ ⊆ D_fin: CORRECT.
- **Sharpens to "at most one"** ⟦HAND, checker's own; not independently checked⟧.
  - Two disjoint pairs align (Step 3), so their union is πᵢ⁻¹ of a D₃(2XY) set. Step 4 leaves R0, or one pair plus a
    window event.
  - Two such merges take three pairs down to one. So D¹ = R0 ∪ {R ⊔ K(S)}.
  - Data: the least number of pairs needed is ≤1 for every D¹ set on 3³, 2×3×3 and 2×3×4.
  - Data: K⊔K′ ∈ N1 for every disjoint pair, with 0 failures on 3×3×4 and 3×4×4 (N1 = R0 ∪ {R⊔K}).
  - Data: N1 = R1 on 3³ (15,842 sets), and R1 is computed independently by closure.

**3. Worked case: CORRECT.**
- ⟦HAND⟧ Write bᵢ = [xᵢ∈Sᵢ].
  - Ω∖K(S) is the six mixed patterns. A sits in 01*.
  - What is left: (01*∖A) ⊔ 10* ⊔ {110, 001}, and 10* = W′₀₁.
  - The leftover {110, 001} is exactly K(S₀,S₁,S₂ᶜ).
- `check3b.py` (A): 2000 random instances on grids 2..5 per side, 0 failures, disjointness included.

**4. Restated L1: CORRECT WITH FIXES (one sentence WRONG as written).**
- "D² = σ-disjoint unions of D_fin sets" is only ⊆ as proved.
  - D² is closed under countable disjoint unions, so "=" holds ⟺ D_fin ⊆ D².
  - Every tested grid has D₃ = D¹ ∪ co-D¹, which is stronger. That is evidence, not proof over ℕ.
- "The whole gate is therefore…": WRONG twice.
  - (i) Read literally (s(⊔Fₙ) = Σs(Fₙ)), it fails for every nonprincipal family: window singletons are already D_fin.
    Fix: "states with the same family agree on σ-disjoint unions of D_fin sets".
  - (ii) Even then it is the **level-2 step**, not the whole gate: D³ and the levels above are untouched.
- "D_fin σ-closed ⇒ D₃ = D_fin ⇒ O1": CORRECT.
  - §2's forcing holds: the agreement class inside D_fin contains the windows and is closed under complements and
    finite disjoint unions.
  - Drop "every state = Λ of its family". Λ_u need not be a well-defined state (same fix as `TRIANGLE_LEVEL1_CHECK.md`).
    Say "is fixed by its family".

**5. §5a: CORRECT at 3³; the generalisation needs scoping.**
- Rerun at 3³: |D| = 15,914, |Q| = 15,842, 72 new; R2 complement-closed (disjoint unions built in); orbit = new (72).
- Not tautological: `new` comes from the closure, and the orbit from the E* formula.
- Also at 3³: new = co-D¹∖D¹, and N1 ∪ new is Dynkin, so it equals D₃.
- Larger grids (`check5a.py`, `check5a_cyc.py`):

| grid | \|D₃\| | new = co-D¹∖D¹ | closure at round 2 | new sets that are cyclic-order sets |
|---|---|---|---|---|
| 2×3×4 | 17,878 | 0 | yes | n/a (Step 4) |
| 3×3×4 | 131,290 | 1,296 (12 or 15 pts) | yes | all 1,296 |
| 3×4×4 | 1,299,250 | 28,512 (15–24 pts) | yes | 26,784; the other 1,728 (21 pts) = cyclic new set ⊔ R0 set |

- Here "cyclic-order set" means {x : (σx₀, σx₁, σx₂) positively cyclic} for an interleaving σ. This family is wider
  than "relabelled E*", and the two coincide only at 3³.
- On every grid, every cyclic-order set is in D₃. That is the contrast with E* ∉ D₃ over ℕ.
- So §5a's "only a finite cyclic order" holds at 3³. On larger grids it reads "a finite cyclic order, possibly padded
  by window events". This tempers, but does not block, the sharpened L1 question.

**6. Prior art (light): NOT FOUND on the shelf.**
- `SHELF_INDEX.json` has no hit on antipodal, cyclic order, or a normal form for a Dynkin join.
- The taxonomy hits are programme-internal, not `owned_regions`:
  - `thm.triangle_level1_rigidity` and `conj.window_restriction_r` (own entries; "respect" needs fix 4);
  - `oml.construct.cyclic_order_coupling` (a related internal construct).
- Nearest neighbours, not owners: Navara–Pták 1983 Thm 1, and the Gudder σ-class survey Ex 6.1 (a union of three
  σ-algebras, not their Dynkin join).

## Bearing on WHY.md

The first round of patching, where window answers are combined and negated, hides nothing. Up to window events, every
such question is (if the ≤1 sharpening holds) one "all agree or all disagree" pair of cubes. Cubes interact only through a two-point vertex, so the
round collapses to a picture you can draw. This is composition, not a circle. What a second round adds on finite grids
is a cyclic order: three local comparisons, each fine on its own, that close into a loop. Every finite loop is still a
legitimate question. The infinite loop E* is not. So the question of whether local views add up to one world now sits
exactly where finitely many loop patches are pushed to a limit. A lens, not an application.
