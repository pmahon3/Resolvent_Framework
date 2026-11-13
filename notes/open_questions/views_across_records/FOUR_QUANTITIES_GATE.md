# Four quantities, every pair seen: does the triangle theorem survive one more quantity?

reviewed: false. 2026-11-13. Pre-registration; nothing run yet. ⟦HAND⟧ marks unchecked hand arguments.
Motivation and choice of move: chat 2026-11-13 (turn one dial at a time; the shape dial first). Lens only: four-player
rock–paper–scissors (Ranta–Lundberg–Kaitala 2005, ch. 11).

## Setup
Ω = X₀×X₁×X₂×X₃. Six observers, one per pair of coordinates (window graph K₄). D₄ = closure of the six families of
pair events under complement and (countable) disjoint union. V₀₁ = sets whose indicator is a sum of six pair functions.
Always D₄ ⊆ V₀₁. Criterion for V₀₁ ⟦HAND⟧: the eight-corner identity on every three coordinates with the fourth held
fixed (Kellerer 1964 Satz 1.1 for the family of pairs).

## The three sentences, restated for four quantities
- **S1₄ (questions).** Every carrier set is finitely built. Finite form: at every finite size, D₄ = V₀₁ (the logic is
  closed, Ovchinnikov). Infinite form: D₄ = D_fin, with some description of what is shut out.
- **S2₄ (answer patterns).** An additive function on D₄ is fixed by its values on window events; every compatible
  family of six couplings (matching one-coordinate profiles) is the window family of exactly one two-valued state.
- **S3₄ (worlds).** That state is induced by an ultrafilter on Ω iff the six couplings are pushforwards of one.

## Already on record (do not re-run)
`definitions_draft.md` §9a (2026-10-19, `verification/gap_linear_vs_constructive.py`), two values per coordinate:

| window graph | |D| | |V₀₁| | gap |
|---|---|---|---|
| triangle | 70 | 70 | 0 |
| path on 4 | 56 | 56 | 0 |
| square (4-cycle, adjacent pairs only) | 82 | 90 | **8** |
| diamond | 148 | 148 | 0 |
| K₄ | 222 | 222 | 0 |

So the finite form of S1 already **fails on the square** with two values (the 8 gap sets are half-cubes counting
disagreements round the loop), and **holds on K₄ with two values**. The triangle holds at every size (Lean core,
2026-11-10). Unknown: K₄ beyond two values; K₄ over infinite alphabets; S2₄, S3₄.

## Is the outcome forced? (lesson of 2026-11-07 and 2026-11-10)
- Not by positivity: with two values K₄ is already not compressed ⟦HAND⟧ (the pentagonal facet (b·x)(b·x−1)/2 ≥ 0,
  b = (1,1,1,−1), takes the value 3), so Ovchinnikov's "positive ⇒ closed" does not apply.
- Not by the triangle theorem: slices at a fixed x₃ are triangle carrier sets, which constrains D₄ but does not give
  D₄ = V₀₁.
- No Lean lemma covers four coordinates. Verdict: not forced, as far as checked.

## Gate `gate.four_quantities_closed` (pre-registered 2026-11-13, not run)
**Probe.** Compute |D₄| by closure and |V₀₁| by direct enumeration on 2×2×2×3, then 2×2×3×3, then 2×3×3×3 if the
previous step stayed under 1 GB and 5 minutes. One size at a time.
- **(a) Equal at every size run** ⇒ supports S1₄ in finite form. Next: try to transfer the triangle proof (slice,
  compare, merge non-K-related values) by hand. Affects: `conj.window_restriction_r` (graphs containing a triangle),
  a new conjecture "closed at every size ⟺ every long loop has a shortcut (chordal)".
- **(b) A gap at some size** ⇒ S1₄ fails in finite form. Record the gap sets and describe them (which loop do they
  count round?). The boundary of the theory then lies between the triangle and K₄. Affects the same entries, negatively.
- Either way S2₄ and S3₄ are not decided by this gate.
**Prior guess (unvalidated, for calibration only):** (a) about 65%.

## FIRED 2026-11-13: outcome (a), equal at every size run
Script `../verification/four_quantities/k4_closed.py` (V₀₁ by an information set of the span, D by closure). Validated
first on the two recorded cases: square 2⁴ gives 82 / 90 (gap 8), K₄ 2⁴ gives 222 / 222.

| K₄ size | points | span dimension | \|D₄\| | \|V₀₁\| | gap | rounds of closure |
|---|---|---|---|---|---|---|
| 2×2×2×2 | 16 | 11 | 222 | 222 | 0 | 4 |
| 2×2×2×3 | 24 | 15 | 1,006 | 1,006 | 0 | 4 |
| 2×2×3×3 | 36 | 20 | 5,134 | 5,134 | 0 | 4 |
| 2×3×3×3 | 54 | 26 | 23,206 | 23,206 | 0 | 5 |

- Largest run: 38 s, peak 1.1 GB (just over the 1 GB step rule; it was the last registered size, so no further step).
- D ⊆ V₀₁ confirmed as sets at each size; equality is equality of sets.
- At 2×3×3×3 the fifth round adds exactly 72 sets. 72 is the number of relabelled cyclic orders on 3×3×3 (§5a of
  `TRIANGLE_GATE_ATTEMPT.md`); whether these are the same objects on the 3×3×3 face is **not checked**.
- **Reading.** Supports S1₄ in finite form on four sizes. It is evidence, not proof: the triangle also agreed on small
  grids long before the general statement was known. Not tested: any size with all four coordinates ≥ 3; the
  infinite form; S2₄, S3₄.
- **Caveat on the method.** V₀₁ membership uses float32 with a 1e-3 tolerance on a rational reduced basis; it
  reproduces both known counts. An exact-arithmetic recount has not been done.
- **Conjectures touched (not auto-propagated).** `conj.window_restriction_r` (graphs containing a triangle): mild
  support. New candidate, unnamed: "closed at every finite size ⟺ every loop of length ≥ 4 has a shortcut (chordal)",
  with data: triangle (all sizes, Lean core), K₄ (four sizes), diamond and path (two values), square fails (two values).
- **Next (pre-registered direction, from outcome (a)).** Try to transfer the triangle proof by hand: fix x₃, compare
  slices (now triangle carrier sets whose difference is a sum of three one-coordinate functions), merge values.

## Hand transfer, first session (2026-11-13) ⟦HAND, unchecked by a second reader⟧

Finite alphabets. F ⊆ Ω with 1_F a sum of six pair functions. Fix coordinate 0 and two values a, b. Slices
F_a, F_b ⊆ X₁×X₂×X₃ are pair-sum sets on the triangle of the other three coordinates, and

  d := 1_{F_a} − 1_{F_b} = h₁(x₁) + h₂(x₂) + h₃(x₃),  with values in {−1, 0, 1}.

**T1 (dichotomy; replaces "α + β").** Write h_j = min h_j + g_j with g_j ≥ 0 integer-valued (differences of d).
Then max g₁ + max g₂ + max g₃ ≤ 2, so exactly one of:
- *simple*: d depends on at most one coordinate x_j (shapes (0,0,0), (1,0,0), (2,0,0));
- *K-type via {j,k}*: d = [x_j ∈ U] + [x_k ∈ V] − 1 with U, V proper and nonempty, independent of the third coordinate.
d never depends on all three coordinates. New relative to the triangle: a K-related pair has a **type**, the pair
{j,k} ⊂ {1,2,3}.

**T2 (merge of a simple pair; transfers verbatim).** If d depends only on x_j, then F_a is obtained from F_b by
removing a contained set {x_j ∈ U₊} and adding a disjoint set {x_j ∈ U₋}. With x₀ = a these are events of the window
{0, j}. So F ∈ D₄ iff the set with a merged into b is in D₄ of the smaller grid.

**T3 (reduction).** By T2 and induction on the total number of values, it suffices to treat sets in which, at every
coordinate, any two distinct values are K-related. If some coordinate has one value left, F is a pullback from a
triangle and the triangle theorem applies (`TriangleFinitary.box_iff_mem_of_finDet` + the hand grid transfer).

**T4 (one two-valued quantity: closed).** Let X₀ = {a, b} with a, b K-related via {1,2}: d = [x₁∈U] + [x₂∈V] − 1.
Then F_b is empty on U×V and full on Uᶜ×Vᶜ. The triangle box identity for F_b at y∈U, y′∈Uᶜ, z∈V, z′∈Vᶜ, t, t′ gives
1_{F_b}(y′,z,t) + 1_{F_b}(y,z′,t) independent of t. Hence either
- (II) F_b, and so F, does not depend on x₃: F is a pullback from the triangle {0,1,2}, in D₄; or
- (I) there is a proper T ⊂ X₃ with F_b = Uᶜ×Vᶜ ⊔ (Uᶜ×V×T) ⊔ (U×Vᶜ×Tᶜ). Then, with bits p = [x₀=a], u, v, t,
  F = C ⊔ K where C = {(u,v,t) ∈ {011, 100}} (a triangle carrier set on coordinates 1,2,3) and
  K = {(p,u,v) ∈ {000, 111}} (an antipodal pair on coordinates 0,1,2). Both are in D₄ and they are disjoint.
So **for K₄ with one two-valued coordinate and the other three finite of any size, D₄ = V₀₁.**

**Consequence for the gate (tempering).** All four sizes run had a two-valued coordinate. If T1–T4 are right, the
gate's outcome on those sizes was forced, and it is **no evidence for the case where every quantity has ≥ 3 values**.
The smallest untested case is 3×3×3×3 (81 points; outside the present script, N ≤ 62).

**Where the transfer is not done.** The all-K case with ≥ 3 values per coordinate. New phenomenon: types can mix.
With a, b, c at coordinate 0: a–b via {1,2} with (U, V), b–c via {1,3} with (Uᶜ, W) gives a–c via {2,3} with (V, W).
Same-type triples are chains as in the triangle. The triangle's "inclusion-minimal class" merge does not go through as
it stands, because the common value on the cell U×Vᶜ can depend on the third coordinate. Next: classify the all-K
sets (the analogue of "all-K ⇒ order set"), or find an all-K set with every quantity ≥ 3 that is not buildable.

## Gate `gate.four_quantities_3333` (pre-registered 2026-11-13, before running; "compute, explain, relocate" beat 3)
**Why here.** T4 explains every size already run (each had a two-valued coordinate). 3×3×3×3 is the smallest case it
does not reach.
**Forcedness check.** No Lean lemma covers four coordinates. T1–T4 need a two-valued coordinate. Positivity fails.
The triangle theorem constrains slices only. Not forced, as far as checked.
**Method (certificates, no closure on 81 points).**
1. Enumerate V₀₁ exactly as triples of slices at x₃ = 0, 1, 2: a triangle pair-sum set on 3³ (15,914 of them) plus two
   slice differences that are sums of one-coordinate functions with values in {−1, 0, 1}.
2. Call a set *reducible* if at some coordinate two values have a simple slice difference (T1). A reducible set is in
   D₄: merging the two values is a pair of Dynkin moves with window events (T2), and lands on a grid with a
   two-valued coordinate, where D = V₀₁ was computed as sets (2×3×3×3).
3. For each irreducible set, search for one Dynkin move (remove a contained window event, or add a disjoint one) to a
   reducible set; then two moves.
**Outcomes.**
- (a) every V₀₁ set certified ⇒ D₄ = V₀₁ at 3×3×3×3. Supports S1₄ beyond the hand result. Then: describe the
  irreducible sets (orders? selectors? other?), which is the input the hand proof needs.
- (b) some sets uncertified after two moves ⇒ not a verdict; they are the candidates for a gap. Describe them, then
  decide membership by a targeted argument.
Affects: the unnamed "closed ⟺ chordal" candidate; `conj.window_restriction_r` (graphs containing a triangle).
**Prior guess (unvalidated):** (a) about 70%.
