# Definitions draft: local information and its composition (2026-10-19)

reviewed: false. This is a DRAFT for reflective equilibrium. The definitions are to be tested against
results and cases, and revised. Nothing here is claimed beyond the status labels.

## 0. Scaffold

- A possibility space Ω = X^V. It is scaffold, not ontology.
- **Views** w ⊆ V. For now these are pairs: the queries of the theory.
- The **view graph** records which views overlap.

## 1. Local information

- A question Q ⊆ Ω is **local to a view w** if whether Q holds depends only on the coordinates in w.
- **Local information at w** is a consistent answer pattern on the questions local to w:
  - in the *two-valued* regime, a 2-type, i.e. an ultrafilter on X^w;
  - in the *probabilistic* regime, a probability (or charge) on X^w.
- A **family of local information** gives local information at every view.
- The family **agrees on overlaps** if neighbouring views give the same answers to the questions
  local to both.

## 2. Locally generated information

- A question is **locally generated** if it is built from local questions by "not" and "either one"
  (joining questions that never both hold). These questions form the *carrier* D: the questions you
  can ask.
- **Locally generated information** is a consistent answer pattern on D: a *state*, two-valued or
  probabilistic.
- Questions outside D are **global-only**. The cyclic question on the infinite triangle is the basic
  example.

## 3. Global information (a world)

- **Global information** is a consistent answer pattern on *all* questions about Ω:
  - in the two-valued regime, a point (Dirac) or an ideal point (an ultrafilter on Ω, a
    complete type);
  - in the probabilistic regime, a charge or probability on all subsets.
- Local or locally generated information **has a world** if some global information restricts to
  it.

## 4. Composition

- Given local information on views w and w′ that overlap, a **composite** on another pair of
  variables is what *every* world fitting both is forced to say about that pair, if it is forced at
  all.
- Composition is **rigid** when it is forced, i.e. a unique gluing:
  - forward two-valued queries (Lean: `glue_unique`);
  - forest gluing in general is not rigid.
- Composition is **flexible** when several gluings exist. It is then a *set* of possible
  composites, as with probabilistic couplings.

## 5. Holonomy, flat, twisted

- For a loop of views, the **holonomy** compares the closing view's local information with the
  composite of the others along the rest of the loop.
- The loop is **flat** if they are compatible (equal when rigid; a member of the set when flexible),
  and **twisted** otherwise.

## 6. Candidate classification

For a family of local information that agrees on overlaps:

| Class | Meaning |
|---|---|
| **Flat (W)** | a world exists |
| **Twisted–visible (Tv)** | no world, and the twist shows on some locally generated question (no coherent state) |
| **Twisted–hidden (Th)** | no world, yet a coherent state on all locally generated questions exists: *pointless coherence* |
| **Underdetermined (U)** | many worlds |

A pre-class sits outside the table:
- **Asynchronous (A):** the local information does not even agree on overlaps, because views that
  "share" a variable read it differently (different averaging, different clocks).

## 7. Existing results in these terms

| Result | Reads as | Status |
|---|---|---|
| Forests: every state has a world | locally generated info along trees is never Th | hand |
| Loop + infinite + finite adding ⟹ Th exists | hiding needs a loop, infinitely many values, finite adding | Lean (triangle, rings) + hand |
| Countable adding or finitely many values ⟹ no Th | completeness restored | hand |
| The cyclic question is not locally generated | global-only information exists | Lean |
| Two forward queries force the third | rigid composition; holonomy = closing view vs composite | Lean (triangle), hand (loops) |
| Finite triangle (3 values): every probabilistic twist is visible | Tv, never Th | exact computation |
| Rings ≥ 4: twists hidden even with finitely many values | Th | hand + certified example; OWNED (Choudhary–Barbosa Cor 5 + exclusivity check, §9b) |
| Case 1: asynchronous stations | A, then Tv in the finite reading; U for the long-run worlds | simulation |
| Case 2: one quantity in time windows | W | simulation |
| Case 4: Sagnac clocks | Th or Tv, i.e. the impossible-point question | design only |

## 8. Candidate theorems, as the definitions suggest them (hunch-shaped; to be earned)

- **H1 (local generation along trees is complete).** If the view graph is a forest, every coherent
  body of locally generated information has a world. *hand*
- **H2 (where hiding lives).** A twist can hide, i.e. there is coherent locally generated
  information with no world, exactly when the views form a loop, there are infinitely many values,
  and answers add up only finitely (two-valued). *Lean + hand*
- **H3 — WITHDRAWN 2026-10-19 (user): the "strangeness" framing is a trap ("I am a strange loop"
  genre) and leads nowhere. Keep only the plain mathematics (span vs carrier; Farkas witnesses).**
  Original text kept for the record:
- **H3 (global information is strange).** In the Th class, the global-only questions are exactly
  where a world would have to commit, and no consistent commitment exists. Local information is
  coherent and global information is impossible.
  - Candidate precise form, open: in Th, every extension of the state to the algebra generated by D
    fails at a global-only question whose "both"-decomposition runs round a loop.
- **H4 (rigid vs flexible).** Two-valued composition is rigid, so twists are forced. Probabilistic
  composition is flexible, and the flexibility is what lets the finite triangle's questions see
  every twist. *conjecture: the first test (§9)*

## 9. Next tests

1. **Probabilistic composition on the triangle.** Do the definitions *explain* why the finite
   triangle is Tv-only? That would turn a computed fact into understanding. Compare the rigid
   two-valued composition with flexible couplings.
2. **Case 4.** What "being local" means when the same relation is read from two perspectives (the A
   pre-class).
3. **Revisit "being local".** Is locality perspectival all the way down?

## 9a. Test 1 result (2026-10-19): two meanings of "made of local information"

- **Linearly local:** the indicator is a *sum* of local indicators, i.e. a 0/1 element of the span V.
- **Constructively local:** the question is *built* by "not" and "either one", i.e. lies in D.
- Always D ⊆ V₀₁. **Candidate H5 (unnamed until prior art is checked):** twists hide in the gap
  V₀₁ \ D, i.e. in information that *adds up* from local pieces but cannot be *built* from them.

**Data** (A = 2, D by direct closure; `verification/gap_linear_vs_constructive.py`):

| Graph | \|D\| | \|V₀₁\| | Gap |
|---|---|---|---|
| triangle | 70 | 70 | 0 |
| path P4 | 56 | 56 | 0 |
| C4 | 82 | 90 | **8** |
| diamond | 148 | 148 | 0 |
| K4 | 222 | 222 | 0 |

- Also: triangle at A = 3, gap 0 (machine count 15,914 = 15,914).
- The infinite triangle has a nonempty gap: E\* ∈ V₀₁ \ D (Lean).
- **Consistent with the finite chordal line:** the gap appears on the one non-chordal graph tested
  (C4) and not on the chordal ones. It is ONE non-chordal datum. The idea was formed after knowing
  that C4 hides twists, and the hiding status of the diamond and K4 is itself only sampled. A test,
  not a prediction.
- The C4 gap sets are half-cubes (8 of 16 points), selected by how many of the four edges disagree
  (0 or 2, or 2 or 4). They are counts round the loop, the 4-cycle analogue of the cyclic question.
- **(WITHDRAWN, see H3)** H3, sharpened (candidate): "global information is strange" = information that is a sum of
  local information but not locally constructible. Twists hide there and only there.
- **Still to connect.** The finite triangle being Tv-only also needed the extreme rays of the
  non-negative cone to be 0/1 (proved at A = 3). The full condition is probably: no gap AND 0/1
  extreme rays. Status: evidence on five small graphs plus two machine facts. Not a theorem.

## 9b. The solid piece, and the C4 mechanism (2026-10-19)

**Lemma (Farkas, finite Ω; hand, short).**
- A probability state μ on D is a mixture of points iff Λ_μ(g) ≥ 0 for every non-negative g in the
  span V.
- Every extreme ray of V ∩ ℝ₊^Ω is either a multiple of a 0/1 set (which lies in D or in the gap
  V₀₁ \ D) or a non-binary ray.
- μ ≥ 0 on D automatically, so **a hidden probabilistic twist is always witnessed by a gap set or
  by a non-binary extreme ray.**
- Hence **no gap + all-0/1 extreme rays ⟹ every state is a mixture of points.** That is what the
  A = 3 triangle proof used implicitly.
- **OWNED (verified 2026-10-20 from the primary source):** this is Maharam 1972, Thm 6.1(iv), p.137:
  consistent positive maps are positively extendable iff Σxᵢ ≥ 0 implies Σφ(xᵢ) ≥ 0. Her Example 2.1
  (p.129) is the triangle in linear form, with lines spanned by (1,0), (0,1), (1,1): consistent, yet no
  extension. Horn–Tarski 1948 (Thm 1.21–1.22) is the Boolean-algebra version. Cite them. What remains
  ours is the split of witnesses into gap sets and non-binary rays.

**C4 check (A = 2, `verification/c4_mechanism_check.py`).**
- The parity witness (≠, ≠, =, ≠) has forced value ≥ 0 on every buildable set: a hidden twist.
- On the 8 gap sets its values are −0.5, 0.5 (six times) and 1.5.
- All 24 extreme rays are 0/1: 16 in D and 8 in the gap.
- **So on C4 the gap IS the mechanism.** The twist is witnessed only by a gap set, not by a
  non-binary ray.

**Open.**
- Do non-binary extreme rays ever matter?
- Does a nonempty gap always carry a negative state?
- More data: a non-chordal graph containing a triangle (the house), and a 5-vertex chordal graph.
  These need anchor-expansion or MILP enumeration; check memory first.

**More data (2026-10-19, A = 2, exact; `verification/gap_five_vertex.py`, `c5_hidden_check.py`).**

| Graph | dim V | \|D\| | \|V₀₁\| | Gap |
|---|---|---|---|---|
| P5 (chordal) | 10 | 76 | 76 | 0 |
| fan, triangles 012/023/034 (chordal) | 13 | 234 | 234 | 0 |
| C4 + pendant (non-chordal) | 11 | 110 | 118 | 8 |
| house, C4 + roof (non-chordal) | 12 | 152 | 160 | 8 |
| **C5 (non-chordal)** | 11 | 102 | 102 | **0** |

**REVERSAL: "twists hide in the gap and only there" is FALSE.**
- C5 has no gap, yet it hides a twist. Take every edge "differ", each value evenly. That is
  non-negative on all 102 buildable sets (min 0), and no world exists (an odd loop can't
  disagree everywhere).
- By the Farkas lemma the witness must be non-binary, and it is: g = 4 − #disagreements round the
  loop. Its values are 0, 2, 4, and the twist gives it −1.
- **Same object, two parities.** On C4 the witness is a count round the loop that happens to be a
  0/1 set (a gap set). On C5 the same kind of count takes three values. The mechanism is the
  **loop count**: a sum of local facts that no single query sees. Whether it shows up as a gap
  set is parity bookkeeping.
- The gap also seems to persist when non-chordal C4 sits inside a bigger graph (pendant, house).
- **Revised candidate (H5′, unnamed):** hidden twists are witnessed by non-negative sums of local
  facts that cannot be assembled from buildable pieces with non-negative weights. Loop counts are
  the examples so far. The gap is the 0/1 special case. Status: 8 graphs at A = 2.

**Prior art, web pass (2026-10-19): the finite probabilistic side is largely OWNED.**
- **Witnesses.** The loop counts are the tight n-cycle noncontextuality inequalities
  Σ γᵢ⟨XᵢXᵢ₊₁⟩ ≤ n − 2, with an odd number of γᵢ = −1 (Araújo et al. 2013, Thm 1, read from the
  primary source). C5's g = 4 − #disagreements is the all-γ = −1 case; C4's is CHSH.
- **Hidden vs visible.** A state on D respects disjoint unions across contexts, so it satisfies the
  single-copy **exclusivity principle / local orthogonality** (Cabello; Fritz et al. 2013;
  Abramsky–Barbosa 2021, logical exclusivity). Known facts match ours: the PR box on C4 satisfies it
  (for two parties LO = no-signalling), and Specker's triangle violates it. **Search level only.**
- **Not yet checked:** whether "state on D" is *equivalent* to single-copy exclusivity, or strictly
  stronger. If equivalent, the finite Th/Tv split is owned outright.
- **Live lead:** Choudhary–Barbosa (arXiv:2411.09773) use **Ramsey theory** for multi-copy
  violations by n-cycle PR boxes. Our infinite side uses ultrafilter Ramsey on the triangle. Read
  it before going further.
- **(b) checked, 2026-10-19 (`verification/dstate_vs_exclusivity.py`, A = 2, exact LP).** On the
  triangle, C4, C5 and the house, the polytope of states on D **equals** the single-copy
  exclusivity polytope inside no-signalling. Both LP gaps are 0, and the span functional is
  well defined. So on these graphs "hidden vs visible" *is* single-copy exclusivity, and it is
  owned. Not proved in general.
- **(a) read, Choudhary–Barbosa (arXiv:2411.09773v2, full HTML).**
  - Cor 5: a single n-cycle PR box satisfies the E-principle for every n ≥ 4, because its
    exclusivity graph has no triangle. With (b), this OWNS our "rings ≥ 4 hide twists with finitely
    many values" at A = 2, at least for the PR-box vertices.
  - Thms 9–13: two copies break it for n = 4, 5; not two or three copies for n ≥ 6; not k copies for
    n ≥ 2^k + 2.
  - Their Ramsey is finite graph Ramsey (R(3,3) = 6; multicolour odd-cycle numbers) on
    copy-coloured exclusivity multigraphs. They conjecture finitely many copies always suffice.
  - No infinite copies, ultrafilters, finitely additive states or infinite outcome sets.
  - **Link to our side: an analogy, not a transfer (yet).** Copies are *products* of finite
    states, while our infinite side is one carrier with infinitely many values. A real bridge would
    need a reading of "k copies" as k independent coordinates of one infinite-valued variable.
    Unexplored. Do not claim.
- **What survives, provisionally:** the infinite two-valued side (E\*, pointlessness from
  ultrafilters). The finite twists are the known contextuality ones, in this programme's
  vocabulary.

**Regimes.**
- With finitely many values, two-valued states are always points, so the C4 gap matters only
  *probabilistically*.
- E\* in the infinite triangle's gap is the *two-valued* phenomenon.
- H3/H5 must state which regime each claim covers.

**Prior art, shelf first.** Navara 1984 ("…the additivity problem") and Dravecký–Šipoš ("On the
additivity of Gudder integral") are about exactly how sums of observables relate to the logic. Grep
them for statements relating 0/1 elements of the span to the σ-class before claiming anything.

**Shelf verdict, Navara 1984 (read 2026-10-19): ADJACENT, does not own.**
- Setting: f, g measurable on a σ-class C, *and summable*, i.e. f + g also measurable. Question:
  is ∫f + ∫g = ∫(f+g) for a state m?
- Proposition: for a two-valued m, additivity holds iff m restricted to C_{f,g} (the σ-class
  generated by the level sets of f, g, f+g) is concentrated in a point. Theorem: this holds when
  R_f is nowhere dense, R_g ≠ ℝ and one function is bounded on one side. Failure is witnessed by
  the sets K(a,b) ∈ C.
- Relation to the gap: a gap set G ∈ V₀₁ \ D is a 0/1 sum of local indicators that is *not* in
  the class, i.e. exactly a **non-summable** sum. Navara assumes summability and so excludes it.
  The shared idea is "sums of observables vs what the class can build"; the gap is the other side
  of his hypothesis.
- Dravecký–Šipoš 1980 is cited by Navara as part of the same additivity line (summable pairs). Not
  on the shelf.
- **Still owed before any claim (web pass):** finite results on when states on a concrete logic
  extend to the generated algebra / are mixtures of points (memory: work by Navara, Pták and
  coauthors on extending states on concrete logics; *unverified*). The Farkas lemma is likely
  folklore there.

## 10. Philosophical horizon (only after the classification earns its keep)

Plato (worlds as given forms), Aristotle (potential infinite; finite adding), Kant (totality as a
task; global information "aufgegeben"). The hope is that H2 and H3 say something precise about
each.

## 11. Why a test needs overlapping views (2026-10-20)

A twist is a property of a *family* of local answer patterns. Data can show one only if all three of
these hold:
1. **Each view sees two or more variables jointly.** Single-variable data (one marginal per
   variable) always fit a world: take the product.
2. **Views overlap.** Neighbouring views share a variable and agree on it.
3. **No view sees everything, and the overlaps form a loop.** One table of all variables is
   already a world. Along a tree, local agreement suffices (Vorob'ev).

Pairs are the smallest views that satisfy 1–3. Larger views work too, as long as the view
hypergraph has a loop. **Relations are not views.** A payoff matrix (lizards) or a dominance order
says how variables act on each other, not what an observer saw jointly. That is why the lizard data
cannot be tested.

**Candidate cases where clocks or scales are built in (lenses, unchecked):**
- **Trophic loops (omnivory / intraguild predation).** A eats B, B eats C, and A eats C: a triangle
  of interactions. Each interaction is observed on the timescale of its slower partner (plankton in
  days, fish in years), so each view has its own clock. Up and down the levels the clocks differ by
  orders of magnitude.
- **Critical behaviour.** At a critical point no characteristic scale exists. Views taken at
  different coarse-graining scales have no shared scale to synchronise to. This is possibly where
  "beyond" (scale separation) and asynchrony meet. Speculative.

## 12. Asynchrony, defined (2026-10-20) ⟦hand; definitions for equilibrium, not claims⟧

**Setting.**
- A process is a path x : T → Ω (T is time, or any index of observations).
- A **clock** is a mean m on T: a finitely additive probability on all subsets of T. Examples are an
  average over an epoch, a Banach limit, or (two-valued) an ultrafilter on times.
- View v with clock m_v reports μ_v = (π_v ∘ x)_* m_v, the law of what v sees, read with its own
  clock.

**Definitions.**
- The family is **synchronous** if all m_v are equal, and **asynchronous** otherwise.
- It **agrees on overlaps** if μ_v and μ_w give the same law on the variables v and w share.
- It is **synchronisable** if some single clock m reproduces every μ_v.

**Lemma A0 (synchrony forces a world).** If all clocks equal m, then x_*m is a charge on all of Ω
whose marginals are the μ_v. So a world exists. In the two-valued case (m an ultrafilter), x_*m is
an ideal point. *Proof: the marginals of a pushforward are the pushforwards of the marginals.*

**Hence:** a family that agrees on overlaps yet has no world is necessarily asynchronous, and not
even synchronisable. **Asynchrony is necessary.**

**It is not sufficient.** In case 1b, different ultrafilter clocks all factor through the
heteroclinic lap counter, and on the fixed-fraction class a world is forced. Working name
(unnamed until prior art): **clocks are comparable** when they factor through a common coarse
clock with finite fibres.

**Clock holonomy (candidate).**
- Sometimes clocks come with comparison maps between overlapping views. For example, translations
  t ↦ t + d_vw, which are clock offsets.
- Then synchronisability asks whether the offsets are a coboundary: d_vw = d_w − d_v.
- Round a loop the obstruction is Σ d, a holonomy of the clocks themselves. Case 4 (Sagnac) is the
  physical instance.
- So **a twist in the answers can be induced by a twist in the clocks.**
- Prior art to check: Čech cohomology of contextuality (Abramsky–Mansfield–Barbosa) and the
  "synchronisation gap" in rotating frames (Rizzi–Ruggiero). **Update 2026-10-20:** clock
  holonomy is OWNED in relativity: Minguzzi, arXiv:gr-qc/0501055, the holonomy of the simultaneity
  connection, whose curvature is vorticity (`case_relativistic_triangle.md`, check 1). Ours, if
  anything, is the step from clock holonomy to answer-level pointlessness.

## 13. The three-part triangle theorem (2026-10-20)

**Setting.** The triangle of pair queries on variables x₀, x₁, x₂ with values in X. The carrier D
consists of the questions built from pair questions by "not" and "either one". A state is a
two-valued or probabilistic, finitely or countably additive answer pattern on D. A world is a
point, an ideal point, or a mixture of these, as the regime requires.

**Two-valued regime: complete.**

| | Values | Adding | Every state has a world? | Status |
|---|---|---|---|---|
| (i) | finite | finite | yes, a point | hand (standard; `thm.sigma_forces_points`, finite case) |
| (ii) | countably infinite | finite | **no: pointless states exist** | **Lean** (`thm.triangle_pointless`) |
| (iii) | countable | countable (σ) | yes, a point | hand (Lean on rings) |

**Probabilistic regime: partial.**

| | Values | Adding | Every state a mixture of worlds? | Status |
|---|---|---|---|---|
| (i′) | finite | finite | yes | exact computation at 2 and 3 values; general open. Owned territory (exclusivity) |
| (ii′) | infinite | finite | open | the impossible-point question; also open whether a two-valued pointless state extends to a charge on X³ |
| (iii′) | countable | σ | not checked | — |

**What separates (i) from (ii): the finite intersection property.** ⟦hand, from the basic lemma⟧
- A two-valued state is an ideal point iff its true questions have the finite intersection
  property.
- So a pointless state makes **finitely many questions true which are pairwise compatible
  (additivity forbids two disjoint true questions) yet jointly impossible.** That is Specker's
  seer, realised at infinity.
- With finitely many values no state can do this. With infinitely many values and finite adding,
  the triangle's state can. Countable adding restores the property.
- How many questions the failing family needs on the triangle is not yet determined.

**Requisite behaviour, as the theorem sorts it:**
- **loop:** necessary (forests always have worlds);
- **infinitely many values:** necessary for (ii);
- **finite, not countable, adding:** necessary for (ii);
- **two-valued:** where it is proved;
- **asynchrony (§12):** necessary for any process to *produce* such a family, but not sufficient.

**Experience** (cases) must supply all of these at once. So far none has: case 1 lacks infinitely
many values; case 1b has a shared lap clock; case 3 has Newtonian time. Case 4 is next.
