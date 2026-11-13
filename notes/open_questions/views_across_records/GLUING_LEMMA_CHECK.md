reviewed: false. 2026-11-13. Independent hostile check by a fresh agent.

# Check of the diamond proof and the gluing lemma (`FOUR_QUANTITIES_GATE.md`, section "The diamond K₄⁻ …")

Notation: crosswalk §A″. ⟦HAND⟧ = hand argument by this checker, not Lean. Computation is evidence only for
all-sizes statements. Inputs taken on trust, not re-checked here: D(K₃(n)) = V₀₁(K₃(n)) (Lean core + hand grid
transfer) and D(K₄(n)) = V₀₁(K₄(n)) (hand, two readers).

## Verdict
**CONFIRMED WITH FIXES.** The diamond proof is correct; one justification is incomplete (the correction θ on P cells)
and is repaired in two lines. The gluing lemma is true once stated precisely: the shared set S must be seen **inside
each piece**, not only in G. Read literally ("G₁ and G₂ closed, glued along a pair seen in G") it is false: P₄ plus the
single pair 03 gives C₄. The proof gives more than the note claims: S may be any set of quantities seen together by one
observer of each piece (any size), and S may be empty (disjoint union). Scope: with pair observers the class reached
from K₂, K₃, K₄ is exactly the chordal graphs with no K₅ and no induced K₅⁻. The two smallest undecided shapes have
gap 0 at the sizes computed here.
**One finding outside the brief:** the pentagon C₅ has gap 0 at (2,2,2,2,2) and (2,2,2,2,3). So "a loop with no
shortcut always leaves a gap" is false at those sizes; the chordal guess needs care in its converse direction.

## Item 1. Diamond: D(K₄⁻(n)) = V₀₁(K₄⁻(n)) for finite n. **CORRECT WITH FIXES** ⟦HAND⟧
Quote: "Let 1_F = f₀₁ + f₁₂ + f₀₂ + f₂₃ + f₀₃. Fix a cell (x₀,x₂) = (a,c). On it, 1_F = α(x₁) + β(x₃) …"
- (a) Correct: every summand, restricted to the cell, depends on x₁ only, on x₃ only, or on neither.
- (b) "cannot have both parts non-constant". Correct: if α takes α₁ < α₂ and β takes β₁ < β₂, then
  α₁+β₁ < α₁+β₂ < α₂+β₂ are three values. The argument does not care what kind of sets x₁, x₃ range over.
- (c) P / Q / R exhaust and exclude each other. Correct.
- (d) F_R is a union of cells of the pair 02, which is seen. Correct.
- (e) **Incomplete as written.** The note justifies θ only off the P cells ("g is constant in x₁ on every cell not in
  P"). That part is right: on a Q or R cell α is constant, so g = α + f₀₂(a,c) is constant in x₁, and θ(a,c) := −g.
  On a P cell one needs θ(a,c) := 1_F − g = f₂₃(c,x₃) + f₀₃(a,x₃), and this is a legitimate value only because it
  does not depend on x₃ there: on a P cell α is non-constant, so β is constant by (b). The note does not say this.
  Also note θ on a P cell is β − f₀₂(a,c), not β: in the note's notation f₀₂(a,c) sits in both g and β.
  With this, G = g + θ(x₀,x₂) = 1_{F₁} is 0/1-valued and is a sum of pair functions of the triangle 012 (θ is a
  function of the pair 02, a pair of that triangle). So F₁ ∈ V₀₁(K₃(n₀,n₁,n₂)) = D(K₃(n₀,n₁,n₂)).
- (f) Correct, by the usual argument: {A ⊆ X₀×X₁×X₂ : A×X₃ ∈ D(K₄⁻(n))} contains the triangle's pair events and is
  closed under complement and disjoint union, so it contains D(K₃).
- (g) Correct: the three pieces live on different cells; F_R ∪ F₁ ∪ F₃ = F since empty R cells contribute nothing.

## Item 2. Gluing lemma. **CORRECT WITH FIXES (statement must be sharpened)** ⟦HAND⟧
Quote: "If G is G₁ and G₂ glued along one quantity or one seen pair, and D = V₀₁ at every finite size for G₁ and for
G₂, then D = V₀₁ at every finite size for G."

**Precise statement.** A shape is a finite set V of quantities with a family 𝒪 of observers (subsets of V, any width).
Let V = V₁ ∪ V₂, S = V₁ ∩ V₂, and suppose
 (i) every observer of G lies inside V₁ or inside V₂;
 (ii) S ⊆ O₁ for some observer O₁ ⊆ V₁, and S ⊆ O₂ for some observer O₂ ⊆ V₂ (for S = ∅: each side has an observer).
Let Gᵢ be the shape on Vᵢ whose observers are the observers of G inside Vᵢ. If D(Gᵢ(n|Vᵢ)) = V₀₁(Gᵢ(n|Vᵢ)) for
i = 1, 2, then D(G(n)) = V₀₁(G(n)). (Size by size; no bound on |S|.)

**Proof.** Write x = (s, y, z): s the values on S, y on V₁∖S, z on V₂∖S. Let 1_F = Σ_O f_O. Put g₁ = sum of the f_O
with O ⊆ V₁ (observers inside S counted here), g₂ = the rest. So 1_F = g₁(s,y) + g₂(s,z).
1. On an S-cell {s}, 1_F = α(y) + β(z). By item 1(b), which holds verbatim for tuples, at most one of α, β is
   non-constant. Cells are of kind P (α non-constant, so β constant), Q (β non-constant, α constant), R (both constant).
2. F_R := union of the full R cells. A union of S-cells; S ⊆ O₁, so F_R is an event of the observer O₁. In D(G).
3. F₁ := F on the P cells. Define θ(s) := g₂(s,·) (constant in z) on P cells and θ(s) := −g₁(s,·) (constant in y) on
   Q and R cells. Then g₁ + θ = 1_{F₁}, a 0/1 function of (s,y). θ is a function of the values on S ⊆ O₁, so it is an
   O₁-function, and 1_{F₁} is a sum of observer functions of G₁. Hence F₁ ∈ V₀₁(G₁(n|V₁)) = D(G₁(n|V₁)).
4. Cylinders: {A ⊆ Ω(V₁) : A × Ω(V₂∖S) ∈ D(G(n))} contains the events of G₁'s observers (they are observers of G) and
   is closed under complement and disjoint union. So F₁ ∈ D(G(n)).
5. F₃ := F on the Q cells: symmetric, with θ′(s) := g₁(s,·) on Q cells, −g₂(s,·) elsewhere, and O₂ in place of O₁.
6. F = F_R ⊔ F₁ ⊔ F₃. ∎

**Points probed.**
- *Tuples.* "A 0/1-valued α(y)+β(z) has at most one non-constant part" is true for arbitrary sets of y's and z's.
- *θ as a summand.* This is the only place hypothesis (ii) is used, and it is used on **both** sides (O₁ for F₁ and
  F_R, O₂ for F₃). S a single quantity: fine as long as each piece has an observer containing it. S a seen pair: fine
  when the pair (or a wider observer containing it) is an observer of both pieces.
- *The literal statement fails without (ii).* G₁ = P₄ = [01][12][23], G₂ = the single pair [03], S = {0,3}: both
  pieces are closed (P₄(2): 56 = 56), S is a seen pair of G, and G = C₄ is not closed (82 against 90). The pair 03 is
  not seen in G₁. The repair: add S as an observer to the piece that lacks it; here that turns G₁ into C₄.
- *Harmless variant.* If S lies inside an observer of G₁ but G₂ lacks it (e.g. G = [012][23][03], S = {0,2}), take
  G₂′ = G₂ plus the observer S. G₁ ∪ G₂′ has the same D and V₀₁ as G, so the lemma applies with G₂′ = K₃.
  Computed: [012][23][03] gives 454 = 454 at (2,2,2,2) and 6,874 = 6,874 at (2,3,2,3).
- *Wider hinge, seen.* [012][023]: 1,296 = 1,296 at (2,2,2,2). Two K₄'s on 0123 and 0124 **plus the triple observer
  [012]**: 1,088 = 1,088 at (2,2,2,2,2). Consistent with the lemma for a seen triple.
- *S empty (disjoint union).* One cell; F depends on the quantities of one side only, or is ∅ or Ω; θ is a constant,
  which is in the span as soon as the side has one observer. The lemma holds. Computed: [01][23] at (2,2,2,2): 30 = 30
  (= 16 + 16 − 2).
- *A side with no private quantity* (V₁ = S): no P cells, F₁ = ∅; G = G₂ up to observers inside S. Nothing to prove.
- *A quantity seen by nobody* on one side: (ii) fails for S = that quantity; add the one-quantity observer.
- *Finiteness.* The proof above never uses that alphabets are finite; it needs only the hypothesis for the pieces at
  the restricted sizes. Whether it matches the repository's infinite-alphabet definitions was not checked.
- Extra evidence: K₄ glued with K₃ along the pair 01 (observers 01,02,03,12,13,23,04,14): 324 = 324 at (2,2,2,2,2),
  1,156 = 1,156 at (2,2,3,2,2), 1,688 = 1,688 at (3,2,2,2,2). Two triangles and a third chained
  (01,12,02,23,24,34): 168 = 168.

## Item 3. Gluing along a triangle that no observer sees. **Argument fails; statement UNKNOWN; gap 0 where computed**
With pair observers and S = {0,1,2}: steps 1 (three kinds of cell) and 6 still hold. Steps 2 and 3 fail.
- Step 2: F_R is a cylinder over an arbitrary set of S-cells; it is an event of no observer and need not be in D.
- Step 3: θ is a function of three quantities that no observer sees together, so g₁ + θ is not shown to be a sum of
  pair functions; F₁ is not shown to be in V₀₁(K₄).
The decomposition F = F_R ⊔ F₁ ⊔ F₃ still exists; what is lost is that the pieces are pair-sum sets.
Whether D = V₀₁ holds for K₅⁻ (all pairs but one) and K₅ at every finite size: **unknown**. Computed (own code, exact
integer arithmetic, closure run to a fixed point):

| shape | sizes | span dim | \|D\| | \|V₀₁\| | gap |
|---|---|---|---|---|---|
| K₅⁻ (pair 34 unseen) | (2,2,2,2,2) | 15 | 422 | 422 | 0 |
| K₅⁻, an unseen-pair quantity 3-valued | (2,2,2,2,3) | 19 | 1,302 | 1,302 | 0 |
| K₅⁻, a shared quantity 3-valued | (3,2,2,2,2) | 20 | 1,930 | 1,930 | 0 |
| K₅ | (2,2,2,2,2) | 16 | 552 | 552 | 0 |
| K₅ | (2,2,2,2,3) | 21 | 2,220 | 2,220 | 0 |

No gap sets. Every size has two-valued quantities, so by the lesson of T4 this is weak evidence for larger sizes.

## Item 4. Scope of "built from K₃'s, K₄'s and single pairs by such gluings". **CORRECT WITH FIXES (class stated)**
For pair observers, hypothesis (ii) forces S to be empty, one quantity, or one seen pair. Starting from K₁, K₂, K₃, K₄
the lemma reaches exactly the graphs obtained by repeated clique-sums of order ≤ 2 **without deleting the shared
pair**, and disjoint unions. In graph terms ⟦HAND; the two standard facts about chordal graphs are quoted from memory,
not from a source on the shelf⟧:
- = chordal graphs with no clique of size 5 in which every minimal separator has at most 2 quantities;
- = chordal graphs with no K₅ and no induced K₅⁻ (in a chordal graph a minimal separator of size ≥ 3, together with
  one fully attached vertex on each side, is an induced K₅⁻; conversely the three common neighbours of the unseen pair
  lie in every minimal separator of that pair).
So the user's description is right. Facts used: a chordal graph is a clique-sum of its maximal cliques along a clique
tree, and its minimal separators are the intersections of neighbouring cliques in that tree.
Covered: forests, K₃, K₄, the diamond, fans, triangulated polygons (2-trees), K₄'s chained along pairs.
**Not covered** (chordal): on five quantities exactly K₅⁻ and K₅; on six, every chordal graph containing one of them
as an induced subgraph, e.g. K₆ minus a triangle (three K₄'s on one common triangle), K₆⁻, K₆, 3-trees in general.
The lemma itself is wider than this class: any closed pieces may be glued, should closed non-chordal shapes exist
(see C₅ below).

## Item 5. The test table. **CONFIRMED**
Script read: `diamond` = pairs (0,1),(1,2),(2,3),(3,0),(0,2). These are the note's pairs; 13 is the unseen pair and
02 the shared one. Its closure stops early only when |D| reaches |V₀₁|, which is sound because D ⊆ V₀₁ is asserted.
Reruns of `k4_closed.py`, and independently of my exact-arithmetic script (which removes the float32 caveat for
these rows):

| run | `k4_closed.py` | own script (exact) |
|---|---|---|
| diamond (2,3,2,3) | 892 / 892 | 892 / 892 |
| diamond (2,2,3,3) | 3,304 / 3,304 | 3,304 / 3,304 |
| diamond (3,2,3,2) | 4,740 / 4,740 | 4,740 / 4,740 |
| square (2,2,3,3) | 1,546 / 1,618, gap 72 | 1,546 / 1,618, gap 72 |
| square (2,3,2,3) | 570 / 642, gap 72 | 570 / 642, gap 72 |

Own script also reproduces K₃(2) 70, P₄(2) 56, C₄(2) 82/90, K₄⁻(2) 148, K₄(2) 222. Not rerun: diamond (3,3,3,2),
(2,3,3,3), (3,2,3,3).

## Item 6. The square's 72 gap sets. **Nothing new: all are pullbacks** (evidence + one hand remark)
At (2,2,3,3) and at (2,3,2,3) the 72 gap sets are exactly the pullbacks of the 8 gap sets of C₄(2) along
coordinatewise maps that merge values: 72 distinct pullbacks, all 72 are gap sets, no gap set is not a pullback.
72 = 8 × 3 × 3 (three ways to split a three-valued quantity in two, at each of the two three-valued quantities).
Sizes of the gap sets: 17 and 19 points (36 each) at (2,2,3,3); 18 points (all 72) at (2,3,2,3).
⟦HAND⟧ That a pullback of a gap set is a gap set is forced: a coarsening has a section, and restriction along the
section sends D of the large grid into D of the small one. So 72 is the minimum; the computation says it is also all.

## Outside the brief: the pentagon
C₅ = [01][12][23][34][04]: 102 = 102 at (2,2,2,2,2) and 314 = 314 at (2,2,2,2,3). **Gap 0.** With the chord 02 added
(triangle 012 + square 0234) the gap is 8 at (2,2,2,2,2) (152 against 160). So at these sizes the square leaves a gap
and the pentagon does not. Not tested: any C₅ with two or more three-valued quantities (72 points and up, outside
the script). Evidence only; it bears on the converse half of the chordal guess, which the note already calls untouched.

## Fixes to apply
1. Diamond proof, F₁ bullet: replace "this is possible because g is constant in x₁ on every cell not in P" by
   "possible because off the P cells g is constant in x₁ (α is constant there), and on a P cell
   1_F − g = f₂₃(c,·) + f₀₃(a,·) is constant in x₃ (α non-constant forces β constant)".
2. Gluing lemma: replace the statement by the precise one in item 2. Minimum change: "glued along a set S of
   quantities that is seen by one observer **in each of G₁ and G₂**" (for pair observers: one quantity, or a pair
   that is a pair of both pieces), and "every observer of G lies in one piece". Add: S empty is allowed.
3. "What the proof really uses": say the hinge may be any jointly seen set, not only a quantity or a pair; with pair
   observers that means size ≤ 2.
4. Scope sentence: add "= chordal, no K₅, no induced K₅⁻ (clique-sums of order ≤ 2 of K₂, K₃, K₄)".
5. "Smallest undecided shapes": add the counts of item 3 (gap 0 at five sizes) as evidence, with the two-valued caveat.
6. "Where this leaves the chordal guess": record C₅ gap 0 at (2,…,2) and (2,2,2,2,3), and that the 72 square gap sets
   are pullbacks of the 8.
7. Crosswalk §A″ results list, if the lemma is entered there: status "hand, two readers, not Lean; prior art not searched".

## Scripts (`notes/open_questions/verification/four_quantities/`; every run under 1 minute, far below 1 GB)
- `gluing_check_exact_D_vs_V01_any_shape.py SIZES OBSERVERS [--save F]`: any shape and observer width, ≤ 62 worlds;
  V₀₁ by an integer extension matrix on information points; D by closure to a fixed point.
- `gluing_check_square_gap_pullbacks.py`: item 6. Data: `gluing_check_gap_square_2233.npy`, `…_2323.npy`.

## Not verified
- The triangle theorem and the K₄ theorem themselves (inputs). No Lean compiled.
- K₅⁻ and K₅ beyond the five sizes in item 3; any five-quantity size with two or more three-valued quantities.
- C₅ beyond two sizes; C₆ and longer loops; the converse direction of the chordal guess.
- The two chordal-graph facts in item 4 against a primary source. Prior art for the gluing lemma (clique-sum /
  decomposable-model literature is the obvious place to look) was not searched: no web search in this task.
- The infinite-alphabet reading of the gluing lemma against the repository's definitions of D and V₀₁.
- Three rows of the note's diamond table were not rerun (listed in item 5).
