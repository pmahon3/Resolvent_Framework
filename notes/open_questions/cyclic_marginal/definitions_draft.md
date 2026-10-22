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
| Finite triangle (3 values): every probabilistic twist is visible | Tv, never Th | exact computation; **holds at 2, 3 values only; Th exists at 4 (§16)** |
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
- **(§16: the chordal line fails at A = 4 even on the triangle.)** **Consistent with the finite chordal line:** the gap appears on the one non-chordal graph tested
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
| (i′) | finite | finite | **yes for 2 and 3 values; NO from 4 values** (non-binary extreme ray, 2026-10-20) | exact computation; Maharam 6.1 + separation |
| (ii′) | infinite | finite | gauge (renaming) families: **visible on the full carrier** (mod-n witnesses), **hidden on the gauge-invariant single-difference carrier** (D–Š); order families: open | fork recorded in `case_relativistic_triangle.md` (CORRECTION + FORK); which carrier is physical is open |
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

## 14. Relations and relata (user, 2026-10-20) ⟦framing + what is proved; not a claim⟧

**User:** "obviously both. It depends on what information you are after. This is getting down to
the duality between relations and relata."

**What the clock case proves, read this way.**
- **Relational questions** concern only how clocks stand to each other, one relation at a time.
  This is the carrier generated by single differences, A_u ∪ A_v ∪ A_w.
  - On it the clock answers are **coherent and pointless**: a two-valued, even σ-additive state with
    no world (Dravecký–Šipoš 1980, applied).
- **Relata questions** also allow a clock's own reading, a gauge quantity, as the subject of a
  question. This is the full carrier D₃.
  - On it the same answers are **visibly inconsistent**: the parity question gets −½ (mod-2
    witness).
- **Same answers, two question algebras, opposite verdicts.** Visibility of a twist is relative to
  the information sought. It is not a property of the answers alone.

**Reading against the stance (answers first, points derived).**
- Asking about relata presupposes relata: a definite reading for each clock.
- When no world exists, that presupposition is exactly what turns a hidden twist into a visible
  contradiction.
- Relations without relata can cohere where relations-with-relata cannot.
- This is a reading, not a theorem. It needs cases beyond clocks.

**Candidate statement (unnamed; prior art owed: Stone/Gelfand point–algebra duality,
gauge-invariant observables in contextuality and quantum reference frames, residual finiteness).**
- For a loop of renaming (gauge) queries with non-zero holonomy in ℤ, the forced state is
  - a state on the relational carrier (hidden), and
  - not a state on the relata carrier (visible, via a finite quotient).
- Status:
  - hand + exact computation for the triangle over ℤ;
  - general groups and loops not checked;
  - order ("beyond") families not checked on the relational carrier.

**Next tests (pre-register before running).**
1. **Order twists on the relational carrier.** The Lean staircase is pointless on D₃. Is it
   still a state on the relational sub-carrier? Presumably yes, since restriction preserves states.
   The informative question is the *converse direction*: are there order families that are visible
   on D₃ but hidden relationally?
2. **A second natural case with a relata/relations choice:** an ecological or social one, where
   "who is above whom" (relations) and "each one's own rank or score" (relata) are both
   observable.

**Test 1 result (gate.order_relational, fired (a), 2026-10-20; exact computation).**
- The relational carrier for order on the triangle (built from pairwise comparisons {<, =, >} on
  the 13 weak orders) has only **20 sets**: the union of the three pair-comparison algebras.
  Non-empty comparison events from different pairs always meet, which is D–Š condition (2), so
  nothing can be built across pairs.
- Hence **every pairwise-consistent comparison family is a relational state**, including the strict
  Condorcet cycle (P(x₀<x₁) = P(x₁<x₂) = P(x₂<x₀) = 1). Relational questions are blind to rank cycles
  at every strength.
- **Relata side:** the rotation family x_{i+1} = x_i + 1 mod 4 has q = 3/4 > 2/3 and no random
  ranking. Allowing values makes it **visible** (mod-2 parity witness, by transport). The strict
  staircase over ℕ stays hidden even with values (Lean).
- **So the duality extends from gauge to order, but cheaply on the relations side.** On a triangle,
  a "relations only" algebra is a union of pair algebras whenever cross-pair events always meet,
  and then it sees nothing. All the content is on the relata side: which value structures let
  questions about the relata expose the cycle (finite quotients do; "beyond" at infinity does not).
- **Refined candidate:** a twist is hidden from relations whenever the relational algebra is a union
  class. It is visible to relata exactly when some quotient of the values carries it finitely.
  Unproved beyond these instances.
- **Lens for test 2 (social ranking):** majority comparisons (relations) cannot pose a question
  exposing a Condorcet cycle. Scores (relata) can, when they exist. Condorcet's paradox and the
  linear-ordering polytope are owned; this reading of them is ours to test.

**A critical test of the partition (2026-10-20; exploratory, NOT pre-registered; exact computation
mod 2 and mod 3 + hand argument for ℤ).** User: the duality needs a case that fails on either
account, or is incommensurate with the partition.

Four question algebras for the clock core Z₁ (`verification/relata_relations_join*.py`):

| Algebra | What may be asked | Clock twist |
|---|---|---|
| R | relations only (one difference at a time) | hidden |
| S | relata only (one clock's reading at a time) | hidden |
| J = closure(R ∪ S) | relations and relata, combined by "not" and "either one" | **hidden** (mod 2: 14 sets; mod 3: 38 sets = just the union) |
| F | **views**: what a *pair* of clocks shows *together* | **visible** (−½ mod 2; −2/3 mod 3) |

- **Why J sees nothing (hand, holds over ℤ too).** Any non-empty relatum event ({x_i ∈ A}) and any
  non-empty relation event ({x_j − x_k ∈ B}) intersect, as do any two from different families. So,
  by D–Š's condition (2), J is just the *union* of the six one-variable algebras. The forced
  answers restrict to a consistent probability on each, so they form a state on J.
- **What F adds.** Joint questions such as "are clocks 1 and 2 *both* even?". That is the
  *conjunction* of a relatum (clock 1 even) with a relation (clock 2 agrees with clock 1). A
  carrier built only by "not" and "either one" can never form that conjunction from R and S. It
  exists only if the **view itself, the pair seen together, is primitive**.
- **Reading (not a claim).** Neither account, nor their sum, sees the twist. Only the *local
  perspective* does: a joint observation of two things, irreducible to their relation plus their
  separate states. The partition into relations and relata is incommensurate with where detection
  lives. The third term is the **view**, which is the programme's own primitive (queries / windows,
  "answers first").
- **Scope:** the triangle; the clock (gauge) family; finite quotients computed, ℤ by the hand
  union argument. Order families and other graphs are not checked. Prior art owed: the
  measurement-scenario literature (Abramsky–Brandenburger contexts as primitive), Kochen–Specker
  partial Boolean algebras (contexts as primitive), structural realism (relations vs relata in
  philosophy of physics).

## 15. Candidate invariant: detection rank (2026-10-20; user: "perfect") ⟦candidate, unnamed until prior art⟧

**Definition (working).**
- Take a family of pair laws (the views) that agree on overlaps. Let Λ be the forced functional on
  the span V of pair functions.
- D_k is the carrier generated by all events depending on at most k variables, closed under "not"
  and "either one".
- The **detection rank** is the least k such that Λ < 0 on some set in D_k ∩ V. A twist is
  *visible at rank k*.
- Rank 2 means visible to pair views.

**Organising principle (to be equilibrated):** *idealisation raises the detection rank exactly for
twists that no finite reduction (quotient) of the values preserves.* Gauge twists keep rank 2 at
infinity (finite quotients carry them). Order ("beyond") twists jump: the finite triangle has rank
2, the infinite staircase rank 3 (Lean: pair views blind).

**Pre-registered predictions (2026-10-20, before running):**
- P1. Rings with finitely many values (C4 parity, C5 all-differ, A = 2) have rank exactly 3.
- P2. Condorcet with scores running to infinity (order types) has rank 3, like the staircase.
- P3. Any gauge twist whose holonomy survives some finite quotient has rank 2, at infinity too.

**Falsifiers:** a rank jump at infinity for a twist that survives a finite quotient, or no jump
for one that survives none.

**Ownership risk:** the finite rank is near local consistency / k-consistency (CSP) and the
Sherali–Adams hierarchy, which are owned, finite and conjunction-closed. The candidate new space is
the **jump at infinity**, with no free "and", tied to finite-quotient survival. A prior-art pass is
needed before any claim.

**Repair needed (2026-10-20, before any result).**
- The set-based definition (Λ < 0 on some set of D_k ∩ V) cannot see twists whose only witnesses
  are *many-valued*. The C5 twist is the example: no gap set, and its witness is the loop count
  0/2/4 (§9b).
- At full rank it also breaks, because Λ is defined only on the span V.
- **Repaired definition (Maharam form):** visible at rank k iff there is **no state on D_k whose
  restriction to the pair events reproduces the pair laws**. At k = number of variables this is
  "no world", so every genuine twist has a finite rank.
- **Computation:** an LP over the elements of D_k. Direct Dynkin closure on rings (16 or 32
  points) blew up and was stopped (`verification/detection_rank.py`, not completed). Needs either
  a check that D_k is the full power set (then rank k = "no world"), symmetry reduction, or
  sampling of D_k.
- **Prediction status:**
  - P3 is supported by existing results (clocks: rank 2 at infinity via parity).
  - P2's mechanism is supported by Lean (pair views blind on the staircase). The infinite Condorcet
    version itself is not run.
  - P1 is not run.

**Prior art on the needle (2026-10-20; scout + my own reading of the two primary sources).**
- **Owned in model theory (NEIGHBOUR, close).**
  - The triangle problem is the *3-amalgamation problem for types*: complete types p₁₂, p₂₃, p₁₃
    agreeing on single variables ("coherence"), with no common 3-type.
  - Goodrick (BIRS 2009 slides) gives both of our kinds as counterexamples: an order cycle
    x₁<x₂<x₃<x₁, and a two-class equivalence relation with ¬E in every pair (a ℤ/2 gauge twist).
  - Hrushovski (JAMS 2012), Remark 2.19(3): bounded-class equivalence relations make
    3-amalgamation fail, and "it is possible that this is the only obstruction" over boundedly
    closed bases.
  - Hrushovski §2.20: the order obstruction exists, "but in a measured setting … this obstruction
    has effect only on a measure zero set" (definable, countably additive measures).
- **Alignment with our theorem.**
  - Hrushovski's measured result matches our cell (iii) (countable adding gives a world).
  - Bounded equivalence relations match our gauge / finite-quotient twists.
  - His order obstruction is our staircase.
  - So the needle narrows: **the finitely additive (charge, Dynkin-carrier) version of type
    amalgamation.** There the order obstruction becomes a coherent pointless state (Lean). It sits
    between his syntactic failure and his measured almost-sure success.
- **Not found:**
  - detection rank via Dynkin systems of k-variable events;
  - the finitely additive state version;
  - the principle "idealisation raises the rank exactly for twists no finite quotient preserves".
  Hrushovski 2.19(3) is the nearest anticipation in spirit: bounded quotients as *the* obstruction.
  It must be cited.
- **Leads not read:** Goodrick–Kim–Kolesnikov homology of types (their H₂ measures 3-uniqueness /
  4-existence failures and starts above our level); Kolesnikov n-amalgamation; NSOP₁ / Kim-
  independence (3-amalgamation holds there); Hansel–Troallic 1986 and Shortt 1983 (marginal
  problem for charges).
- **Finite rank:** Sherali–Adams / k-consistency (owned background; Wainwright–Jordan; Kolaitis–
  Vardi; Abramsky–Gottlob–Kolaitis k-robust satisfiability).

**P1 result (2026-10-20; `verification/ring_rank_sa3.py`, LP).**
- **Method.** A state on D_3 restricts to consistent laws on every 3-subset (Sherali–Adams level 3).
  So SA₃ infeasibility means visible at rank ≤ 3.
- **Pair views on rings are blind:** D_2 is the union of the pair algebras, so every consistent
  family is a state there.
- **Result: P1 HOLDS.** Rank is exactly 3 for:
  - C4 parity (P = 1, 0.85, 0.8, 0.76);
  - C5 all-differ (P = 1, 0.9, 0.85, 0.81).
  Controls inside the local range (C4: P ≤ 0.75 by CHSH; C5: P ≤ 0.8 by the 5-cycle bound) are
  SA₃-feasible, as they should be.
- **Ownership.** "Rank ≤ 3 on rings" is the treewidth bound: Sherali–Adams level tw + 1 is exact,
  and cycles have treewidth 2 (Wainwright–Jordan; owned). So P1 confirms the definition behaves
  correctly; it is not a new fact.
- **Sharper reading of the needle.**
  - On *finite* chordal graphs (the triangle), the Dynkin carrier D_2 does **better** than the
    local-consistency bound (**at A ≤ 3 only; §16**). Its cross-pair constructions see every twist at rank 2, where SA₂
    (the local polytope) does not.
  - At **infinity**, for order twists, that advantage is lost: the rank falls back to the
    treewidth bound 3 (Lean staircase).
  - Gauge twists keep the advantage through finite quotients.
  - **Candidate restatement:** *idealisation removes the question carrier's advantage over local
    consistency exactly for twists that no finite quotient preserves.*
  - Unproved beyond instances. Prior art: Sherali–Adams for Dynkin systems was not found (block A
    scout).

**(a) GKK homology of types, read (2026-10-20; scout + my spot-checks).**
- Goodrick–Kim–Kolesnikov work with **independent** amalgamation problems. 3-existence then holds
  in every simple theory (2013, p.1, verified: "3-existence holds in all simple theories").
- Their obstructions start at 4-existence / 3-uniqueness. H_n(p) ≅ Γ_n(p) is a profinite abelian
  automorphism group (2017 Thm 2.1): "finite quotients carry the obstruction", but **one level up**
  (non-uniqueness of 3-types, not non-existence).
- No measures, charges, Dynkin systems or ranks (grep).
- **Verdict:** NEIGHBOUR (2013, 2017), nothing (2015). They do not own our level.
- The bare 3-existence failure examples are Goodrick's slides (order cycle) and Hrushovski 2.19(3)
  (bounded quotient), as already recorded.
- Kolesnikov "n-simple theories" (APAL 2005): simple theories only, so nothing at our level
  (abstract only).

## 16. Problem 1 resolved NEGATIVELY: the finite triangle can hide a twist at four values (2026-10-20)
⟦exact computation + owned criterion; REVERSAL of "finite triangle sees every twist"⟧

- **Statement.** On the triangle with values {0,1,2,3}, there is a consistent family of pair laws
  which is a state on the carrier D (non-negative on every buildable question) but is not a mixture
  of points.
- **Proof.**
  - (i) `verification/triangle_A4_ray_verify.py` exhibits g = Σ c·[pair cell], with values 0, 1, 2
    on the 64 points: value 2 at (0,3,2), (3,2,1), (3,2,3).
  - (ii) Exact rational check: g ≥ 0, g lies in the span, and rank M = 37 while rank M_Z = 36 on
    g's zero set. So g spans an extreme ray of V₊ = {non-negative sums of pair functions}.
  - (iii) g is extreme and not a multiple of a 0/1 vector, so g ∉ cone(V₀₁). Separation gives a
    functional Λ ≥ 0 on cone(V₀₁) with Λ(g) < 0.
  - (iv) Λ ≥ 0 on the cells gives pair laws, which are consistent because Λ is linear on the span,
    and normalised. D ⊆ V₀₁, so Λ is a state on D. Λ(g) < 0 with g ≥ 0, so it is not a mixture
    (Maharam 1972, Thm 6.1).
- **Sizes checked** (random-objective LP with an exact extremality filter): (3,3,3), (2,2,4),
  (2,3,4), (3,3,4) showed none; (4,4,4) showed 11.
  - A sampled "none" is NOT a proof for those sizes. Only A = 3 is exact (earlier).
  - First appearance: between 3×3×4 and 4×4×4 (search-level).
- **Consequences, already propagated:**
  - The note §7 is corrected.
  - The three-part theorem's probabilistic cell (i′) is false from four values.
  - §15: the finite triangle's rank is 2 only for small alphabets. This hidden twist has rank 3 at
    A = 4.
  - "Infinity alone blinds the triangle" now holds **for yes/no answers only**: two-valued finite
    states are points, and the Lean result stands.
  - Explicit witnesses (clocks mod 2 and 3, Specker, Condorcet transport) are unaffected.
- **Prior art owed:**
  - facets of the marginal polytope of K₃ with 4 labels (no-three-way-interaction / 3-way
    transportation polytopes; Vlach; De Loera–Onn), where coefficient-2 facets are probably known;
  - the exclusivity principle for larger outcome sets (does it fail to characterise the classical
    set at A = 4?).
- **Open:** which twist family does g witness: order-like, gauge-like, or neither? Does the
  minimal hiding alphabet equal 4 exactly? (3×3×4 needs an exact check.)

**Restating §15 after the reversal (pre-registered candidate, 2026-10-20).**
- "Idealisation raises the rank" is FALSE as stated: a finite triangle at A = 4 already has a rank-3
  twist.
- **Transport fact (hand).** Push a carrier state through any per-coordinate map onto ≤ 3 values.
  The result is a carrier state on the small triangle, which has a world, since ≤ 3 values is exact.
  So every *hidden* twist has untwisted small quotients.
- **Candidate (converse, falsifiable):** *on the triangle, a twist is visible iff some
  coordinatewise quotient onto ≤ 3 values is still twisted.*
- It fits clocks (mod 2), Specker, Condorcet (mod-2 transport), the Lean staircase (two-valued; no
  small quotient keeps "beyond") and the A = 4 hidden twist (its small quotients are untwisted by
  the transport fact).
- **The infinite two-valued regime is separate:** there, hiding needs infinity (finite two-valued
  states are points).
- **Problem 2 reframed:**
  - (a) the minimal hiding alphabet: 4 by search, with 3×3×4 sampled only;
  - (b) which families hide;
  - (c) the construction-depth version.

## 17. Pinned question (user, 2026-10-20): does the twist make separating syntactic and semantic requirements for truth impossible? ⟦reading; owned ingredients flagged⟧

**Short answer.** They can still be defined separately. What fails is their *agreement*, and the
twist locates the disagreement exactly.
- **Syntactic side:** coherence, i.e. no contradiction derivable from the answers using the
  connectives one is allowed (here "not" and "either one" on askable questions; additivity, no
  Dutch book).
- **Semantic side:** a model, i.e. a world (point or ideal point) making the answers true
  compositionally.
- **Classically they coincide (completeness, Gödel 1930).** That coincidence depends on every "and"
  being askable. In a partial logic it can fail. Kochen–Specker partial Boolean algebras and
  Abramsky–Barbosa's logic of contextuality own this in the finite / quantum setting.
- **The twist is the witness of non-coincidence.** A pointless coherent state is syntactically
  impeccable and semantically empty. The failure sits at the conjunction that cannot be formed:
  truth stops being compositional exactly where "A and B" is not a question.
- **The classification sharpens it:**
  - visible twist (Tv): syntax catches the semantic failure (some askable question gets a negative
    value);
  - hidden twist (Th): the semantic failure is *invisible to syntax*;
  - world (W): they agree.
- **Today's results say where they part:**
  - yes/no answers: only with infinitely many values (Lean);
  - probabilities: already at 4 values on a triangle (§16);
  - relations-only questions: blind even where joint views see (§14).
- **So:** separation is possible; *alignment* is what can be lost. The twist forces a choice
  between keeping every locally sanctioned truth (coherence) and keeping compositional truth (a
  world).
- **Prior art to check:** Tarski's compositional truth vs partial logics; Kochen–Specker; the
  programme's earlier Paper I note on CE non-derivability (completeness failures for coherence).

**Problem 2(a): minimal hiding alphabet (2026-10-20).**
- **Exact (verified ray + Maharam/separation):**
  - hiding exists at sizes **3×4×4** (rank 30 vs 29; value 2 at (0,0,0) and (2,3,1)) and 4×4×4;
  - no hiding at 3×3×3 (exact, earlier).
- **Search-level only** (40k random-objective LPs, extremality filter): no non-binary ray at 3×3×4,
  2×4×4, 2×2×6 or 2×3×5. Not a proof.
- **Reading:** hiding seems to need at least two variables with four values, together with a third
  variable of three or more values. Not the total size.
- **Exact closure of 3×3×4 and 2×4×4** needs facet enumeration (pycddlib); installation awaits the
  user's permission.
- Script: `verification/triangle_ray_verify_sizes.py`.

**Follow-up (user, 2026-10-20): a sentence written on a twisted strip, readable perpetually.**
⟦reading; owned ingredients flagged⟧
- **The object.** A cyclic text where every local window of consecutive words reads correctly, and
  one circuit returns you transformed: reversed, negated, or with two roles swapped. That is a loop
  of local views whose composition has a **holonomy**.
- **Semantics.** A global meaning is an assignment to every token that fits every window. It exists
  iff the holonomy is trivial.
  - With an order-2 twist (Möbius-like) there is no meaning on the strip itself.
  - There *is* one on the **double cover**: read twice round, and meaning returns after two
    circuits.
  - Perpetual reading on the strip oscillates with period 2. The content lives on the cover, not on
    the page.
- **The negation case is owned.** A cycle of sentences each asserting the next, with an odd number
  of "not"s, is a **liar cycle**. Abramsky et al. 2015 ("Contextuality, cohomology and paradox",
  shelved) treat liar cycles as cohomological obstructions to a global section. Each window is fine
  and no global truth assignment exists. Kripke-style truth-value gaps are the classical repair.
- **What our results add, read this way.**
  - A three-sentence liar cycle with the twist on one link is our **mod-2 clock core** (same, same,
    flip).
  - With probabilistic readings (each sentence true half the time), every window is consistent.
  - **Relations-only questions** ("do sentences i and j agree?") cannot detect the twist.
  - The **joint question** ("are sentences 1 and 2 both true?") can, with forced value −½.
  - So a reader who only tracks agreement between adjacent sentences can read perpetually without
    noticing anything wrong. A reader who holds two sentences' truth values together sees the twist.
  - With finer readings (four or more shades on two links), even the joint questions on a triangle
    can miss it (§16).
- **On the syntax/semantics question:** the strip text is syntactically perfect everywhere, so
  "readable perpetually" is a syntactic property. Its semantic content exists only on the cover,
  which is a richer space than the page. Truth is recovered by changing *where* the text lives, not
  by changing the text.

**Problem 2(a) exact status (2026-10-20, cdd double description; `verification/triangle_rays_exact.py`,
`triangle_gap_pullback.py`).**
- **No non-binary extreme rays (exact):** 3×3×3 (207 rays), 3×3×4 (717), 2×4×4 (228).
- **Non-binary rays, hence hiding (exact):** 3×4×4, 4×4×4.
- **The remaining source of hiding is a gap.** A 0/1 extreme ray that is not buildable *and* not in
  cone(D).
  - Pullback test: rays that are pullbacks of buildable sets from smaller triangles are buildable.
  - 3×3×4: 465 of 717 rays shown buildable this way; 252 undecided (they use all four values).
  - 2×4×4: 224 of 228 shown; 4 undecided (their merged versions failed the small-size membership
    test).
  - Direct closure at 32 to 36 points is too large to run naïvely. A first targeted script had a
    target-selection bug (vacuous output) and was removed.
- **So:**
  - minimal hiding sizes are ≤ 3×4×4;
  - 3×3×4 and 2×4×4 are open, pending the gap question;
  - 3×3×3 does not hide (exact).
- **Method still needed:** targeted construction search for the undecided sets (e.g. guided
  disjoint-union decompositions), or a structural argument.

**Problem 2(a) RESOLVED at the boundary (2026-10-21; `verification/cone_D_pullback_lp.py`).**
- **Method.** No hidden twist at size sz iff cone(D) = V₊ (Maharam). Sufficient: every extreme ray of
  V₊ (exact cdd enumeration) is a non-negative combination of D-sets. The supply is pullbacks
  (coordinatewise value merges, which are buildable by transport) of the *exact* carriers one size
  down. LP feasibility uses a residual check below 1e-7.
- **Results:**
  - **3×3×4: no hidden twist** (717 rays, supply 105,801).
  - **2×4×4: no hidden twist** (228 rays, supply 161,613).
  - 3×3×3: none (earlier, exact).
  - **3×4×4 and 4×4×4: hiding** (non-binary extreme rays, exact).
- **So the smallest triangle that hides a probabilistic twist is 3×4×4** among all sizes with
  coordinatewise sizes ≤ (3,4,4). In words: one variable with three values and two with four.
  2×3×5 and 2×2×6 are being checked.
- **Bug note.** The value-merge map in `triangle_gap_pullback.py` / `cone_D_pullback_lp.py` sent
  w ↦ w−1 instead of w ↦ v (found and fixed 2026-10-21).
  - The earlier "465/717" and "224/228 shown buildable by pullback" counts may contain false
    positives and are WITHDRAWN.
  - The LP conclusions use only genuine pullbacks under the fixed map.
  - A preimage assertion is now in place.
- **Also exact (2026-10-21):** 2×3×5 (211 rays) and 2×2×6 (152 rays) hide no twist.
- **Pattern** (a candidate, not a theorem): hiding needs **two variables with ≥ 4 values and the
  third with ≥ 3**. Total size does not decide it: 2×2×6 (24 points) and 2×3×5 (30) are safe;
  3×4×4 (48) hides.
- **Untested:** 2×K×K for K ≥ 5, and 2×2×K for large K.

## 18. Problem 2(b): what the 3×4×4 hidden twist looks like (2026-10-21) ⟦candidate; certified on a supply, not on all of D⟧

**Computation** (`verification/hidden_twist_344.py`; output saved alongside).
- Minimise Λ(g) for an exact non-binary extreme ray g, over consistent pair laws with Λ ≥ 0 on a
  supply of **592,185 buildable sets**. The supply is pullbacks of the exact carriers at 3×3×3,
  2×3×4, 3×2×4 and so on, through every coordinatewise coarsening up to relabelling. Solved by
  cutting planes, converging in 3 rounds.
- Result: **Λ(g) = −1/9.**

**The pair laws are uniform on allowed pairs.** Each pair carries an allowed/forbidden relation (a
bipartite graph with 9 edges), and every allowed pair has probability 1/9:
- (x₀,x₁): x₀=0 → x₁∈{0,1,2}; x₀=1 → {0,1,3}; x₀=2 → {1,2,3}. Each x₀ value forbids one x₁ value.
- (x₁,x₂): x₁=0 → {1,2}; 1 → {0,1,3}; 2 → {0,2}; 3 → {2,3}.
- (x₂,x₀): x₂=0 → {0,1}; 1 → {0,2}; 2 → {0,1,2}; 3 → {1,2}.
- Marginals agree on overlaps: x₀ is uniform; x₁ is (2,3,2,2)/9; x₂ is (2,2,3,2)/9.

**Reading.**
- **Neither gauge nor order.** Gauge twists have *bijective* supports (renamings) and are caught by
  finite quotients. Order twists need "beyond" at infinity. This one is a **many-to-many relational
  constraint pattern**: each pair says which combinations are *possible*, with no preference among
  them.
- So a third kind of twist appears at finite resolution. It is *possibilistic*: built from what is
  allowed, spread evenly.
- It is consistent with the coarse-graining candidate. Hidden twists coarsen to untwisted ≤3-value
  pictures, by transport.

**Caveats and next checks.**
- Certified only against the supply. Full D-positivity of *this* Λ is not verified, although some
  hidden Λ exists (§16).
- Does the bare *support* pattern (the three allowed relations as yes/no constraints) admit a joint
  support? That is, is the pattern logically consistent but probabilistically twisted?
- **Prior art:** possibilistic vs probabilistic contextuality (Abramsky–Brandenburger's hierarchy:
  probabilistic, logical (possibilistic), strong). This candidate is probabilistic-only. Check
  whether "uniform on a support" families are studied there.

**§18 CERTIFIED (2026-10-21; `verification/certify_344.py`).**
- **The pair laws Λ** are uniform 1/9 on the allowed pairs (§18). They are well defined on the span:
  Λ kills every null vector, checked exactly.
- **Λ ≥ 0 on every 0/1 vector of the span (V₀₁ ⊇ D).**
  - MILP: 48 binary variables, span membership as exact integer constraints; minimum 0, re-evaluated
    exactly at the optimum.
  - So Λ is a state on the whole carrier, i.e. non-negative on every askable question.
  - Rigour: the minimum relies on the MILP solver's optimality certificate (float). The values are
    multiples of 1/9.
- **Not a mixture.** An explicit integer g ≥ 0 in the span with **Λ(g) = −1/9**, exact. g has value
  2 at (1,2,1) and (2,0,0), and 1 on 17 other points.
- **Hence an explicit hidden twist on the 3×4×4 triangle**, of the third kind (relational /
  possibilistic). Logically consistent: all 27 allowed pairs extend to the 16 allowed triples.
  Probabilistically impossible. Invisible to every askable question.

**Prior art for §16–18 (2026-10-21; scout plus my reading of both primary sources).**
- **OWNED: the non-binary-ray threshold.**
  - "All extreme rays of V₊ are 0/1" means the triangle's marginal polytope is **compressed**
    (Sullivant 2006, Thm 2.4: each facet takes at most one non-zero value on lattice points;
    verified).
  - Ohsugi–Hibi 2010 table (verified): r₁×r₂×2 unimodular; r₁×3×3 compressed; **4×4×3 "normal, not
    compressed"**.
  - So our exact results (no non-binary rays at 3×3×K and 2×r×s; non-binary at 3×4×4) are a
    restatement. Cite them.
  - Note: compressed ≠ normal. 3×4×4 is normal (Bruns et al. 2011) but not compressed.
- **NOT found (candidates):**
  - (i) The **carrier reading**. Questions built by "not" and "either one" see every probabilistic
    twist iff the polytope is compressed *and* there is no gap (non-buildable 0/1 rays outside
    cone(D)). Our cone(D) checks at 3×3×4 and 2×4×4 settle the gap half there.
  - (ii) The **explicit relational hidden family** at 3×4×4 (uniform on 9-edge allowed relations;
    logically consistent, probabilistically twisted, invisible to every askable question).
  - (iii) The link to Abramsky–Brandenburger's logical/probabilistic gap. That gap is owned as a
    phenomenon; the triangle with outcomes 3,4,4 as an instance was not found.
- **Consequence for the lived reading.** "Fineness needed for hiding" is, in owned language, "the
  smallest non-compressed three-way table". What is ours is that this is the threshold at which
  *every askable question goes blind* to some incoherence.

## 19. Problem 4: probabilistic composition (2026-10-21; `verification/composition_R_vs_C.py`)

**Question.** Fix P₀₁ and P₁₂. Which closing laws P₀₂ are
- **R**: realizable (some joint world produces all three)?
- **C**: carrier-compatible (all three together are a state on the questions you can ask)?

**R is classical.** R = Σ_y P₁(y) · Coupling(P(x₀|y), P(x₂|y)), a weighted sum of Fréchet coupling
polytopes.
- It contains the Markov composite Σ_y P(x₀|y)P(x₂|y)P₁(y).
- **R is a single point iff for every y one of the two conditionals is a point mass.** That is the
  probabilistic analogue of the rigid two-valued composition law (forward types, Lean). Owned:
  Fréchet classes.
- So probabilistic composition is flexible, and **twisted means P₀₂ ∉ R**.

**C ⊇ R.**
- At compressed, gap-free sizes C = R (exact: 3×3×3, 3×3×4, 2×4×4, 2×3×5, 2×2×6). There every
  twist is visible.
- **At 3×4×4, C ⊋ R.** Using the hidden family's P₀₁, P₁₂ (uniform on allowed pairs) and an inner
  approximation C′ ⊆ C (non-negative on all 0/1 span vectors, via MILP cutting planes):
  - the hidden family's own P₀₂ lies in C′ \ R. Farkas certificate b·y = −1/6. L∞ distance to R is
    1/27 (≈ 0.037; cell masses are 1/9);
  - along the Farkas direction the support functions are h_R = −1/2 and h_C′ = −1/3, a **gap of
    1/6**;
  - in **25 random directions the support functions agree** (gap < 1e-9).
  - So the hidden region C \ R sticks out of R in few directions. (Corrected below: it is
    full-dimensional and about 29% of R by volume, so it is not thin.)
- **Reading.**
  - At finite resolution the questions you can ask compose to a slightly *larger* set of closing
    laws than any world allows.
  - The excess is the hidden twists.
  - Seen from most directions the askable and the realizable compositions coincide. The
    difference is detectable only along special directions, which correspond to non-binary
    witnesses (§16).
- **Open:** the dimension and shape of C \ R. Is it lower-dimensional, or a thin full-dimensional
  cap? Does it grow with resolution (4×4×4, 5×4×3)?

## 20. Problem 3: why relations plus relata stay blind for comparisons (2026-10-21; `verification/problem3_J_pairlocal.py`)

**Result (exact, triangle, n = 3 and n = 4 values).**
- Every set in J (the closure of single-variable events and comparison events {<, =, >} under
  "not" and "either one") is **pair-local**: a function of one pair (x_i, x_j). |J| = 146 for both
  n = 3 and n = 4.
- **Hence J is blind to every twist, for every family.** On a pair-local set the forced value is a
  probability under that pair's law, which is ≥ 0.
- **n = 2 is the exception.** J = D (70 sets) and contains non-pair-local sets such as "all equal".
  Comparisons of binary values determine the pair, so relations plus relata rebuild the full
  carrier and twists are visible.

**Why (hand, sketch; not proved for general n).**
- Disjoint unions are the only way to build across pairs. Cross-pair disjointness needs two
  non-empty built sets on different pairs to miss each other.
- With ≥ 3 values, comparison and relatum events on different pairs always meet. Examples:
  {x₀<x₁} ∩ {x₁<x₂} needs three distinct values; {x₀ = top} ∩ {x₁ < x₂} is non-empty.
- The only disjointness is *within* a pair, e.g. {x₀ = top} and {x₀ < x₁}. So every union stays
  pair-local. This is a D–Š-type mechanism, but relative to pairs, not single functions.
- Open: a proof for all n ≥ 3, and a check whether |J| stays 146.

**Reading.**
- For orderings, relations (comparisons) and relata (individual values) can only ever be combined
  *within* one pair. No askable question links three things.
- That is why rankings, scores and comparisons, without joint pair records, cannot expose a
  Condorcet-type incoherence at any resolution beyond two values.
- It sharpens §14: the joint view is needed because these question kinds cannot cross pairs.

**§20 continued (2026-10-21): hand work and formalisation.**
- **Exact for n = 3–7:** J is pair-local, with |J| = 146, 146, 218, 338, 554. (n = 3 and n = 4 share
  146 by coincidence: 20 + 126 and 44 + 102.)
- **Proof structure:**
  - (a) Any two pairs of the triangle share one variable.
  - (b) If a built set on pair e depends only on the shared variable, it also lies in pair f's
    family, and the union stays pair-local.
  - (c) **Cross-pair step, Lean-checked** (`TransportGeneral.pairLocal_meet`). If both depend on
    their non-shared variables and each projection onto the shared variable misses at most one
    value, they meet when n ≥ 3, so they cannot be disjoint.
  - (d) **Invariant, open.** Every built pair-set depending on both variables misses at most one
    value in each projection. Verified exactly for n = 3, 4, 5 on the pair closure. It survives the
    generators and "either one" with a single-variable set (hand). Complement control needs finer
    bookkeeping: the sets are comparison patterns with whole rows or columns flipped, and the row
    and column flips must be bounded.
- **Transport lemma, general form, Lean-checked** (`TransportGeneral.mem_pre`): for arbitrary
  coordinatewise maps between arbitrary value types. This covers the mod-n witnesses and the
  pullback supplies used in §16–18.

**§19 continued: the shape of C \ R at 3×4×4 (2026-10-21; `verification/sliver_shape.py`, output saved).**
- **Volume (hit-and-run, 1,500 samples of T,** the 6-dim polytope of closing laws with the right
  marginals):

  | Region | Samples | Share |
  |---|---|---|
  | R (realizable) | 334 | 22% |
  | C′ \ R (hidden) | 97 | 6.5% |
  | visibly twisted | 1,069 | 71% |

  So the hidden region is roughly 29% of R's size, and at least that (C′ ⊆ C is an inner
  approximation).
- **Dimension.** Of the feasible random perturbations (step 0.004) of the hidden law, 28 stay in
  C′ \ R and 33 leave C′. The hidden region is **full-dimensional**, not a lower-dimensional face.
- **Correction to "thin sliver".** In volume it is not thin. It *is* invisible to almost every
  linear audit: support functions agree in 25 random directions, while along the Farkas direction
  the gap is 1/6.
  - Consistent picture: a full-dimensional layer over part of R's boundary that pokes out beyond R
    only near a few face normals.
- **Lived reading (lens).** Merged pairwise data that are askable-consistent but correspond to no
  world are *common* at this resolution: about 1 in 4 of the askable-consistent closings. Yet a
  random summary-statistic check against realizable ranges almost never flags them. Detection
  needs the special (non-binary witness) directions.
- **Caveats:** hit-and-run samples are correlated; C′ is an inner approximation; one family (P₀₁,
  P₁₂) only.

**§20 PROVED for all n ≥ 3 (hand, 2026-10-21; the gap is closed).**

*Setting.* Fix a pair; write its variables (x, y) ∈ X², X = {0, …, n−1}. Generators: rows R_a = {x = a},
columns C_b = {y = b}, and the comparison classes L = {x < y}, Eq = {x = y}, G = {x > y}. P is the
Dynkin closure. 𝒦 is the 8 unions of {L, Eq, G}.

**Lemma 1 (normal form).** P ⊆ F := {K Δ R_α Δ C_β : K ∈ 𝒦, α, β ⊆ X}, where R_α = ⋃_{a∈α} R_a and
C_β likewise.
- *Proof.* F contains every generator. A complement is a Δ with X², which lies in 𝒦. A disjoint union
  is a Δ, and 𝒦, the row sets and the column sets are each closed under Δ. So F is a Dynkin system
  containing the generators. □

**Lemma 2 (at most one empty row).** Let A = K Δ R_α Δ C_β depend on both variables. Then A has at
most one empty row and at most one empty column (and likewise at most one full row and column).
- *Proof.*
  - Row a of A is {y : [K(a,y)] ⊕ [a∈α] ⊕ [y∈β]}. It is empty iff β = T_K(a) when a ∉ α, or
    β = X \ T_K(a) when a ∈ α, where T_K(a) = {y : K(a,y)}.
  - If K ∈ {∅, X²}, then T_K(a) ∈ {∅, X}, so an empty row needs β ∈ {∅, X}. But then A depends on x
    only, a contradiction.
  - Otherwise, for distinct a ≠ a′, the sets T_K(a), T_K(a′), X \ T_K(a) and X \ T_K(a′) cannot
    coincide across a and a′:
    - K ∈ {L, G, L∪Eq, G∪Eq}: the T_K(a) are threshold up-sets or down-sets of distinct thresholds.
      An up-set equals a down-set only if both are ∅ or both are X, which these thresholds exclude.
    - K ∈ {Eq, L∪G}: T_K(a) = {a} or X \ {a}, and {a} = X \ {a′} forces n = 2.
  - So β determines at most one empty row. Columns are symmetric. Full rows are empty rows of the
    complement, which also lies in F. □

**Lemma 3 (cross-pair meeting, Lean: `TransportGeneral.pairLocal_meet`).** Pair-local sets on two
different pairs, each missing at most one value of the shared variable, meet when n ≥ 3.

**Theorem.** For n ≥ 3, J = P₀₁ ∪ P₁₂ ∪ P₂₀. Every question built from relata and comparisons is
pair-local, hence blind to every twist.
- *Proof.* U = ⋃ P_e contains the generators and is closed under complement. Take A ∈ P_e and
  B ∈ P_f disjoint and non-empty, with e ≠ f sharing variable x_j:
  - if A or B depends only on x_j, it lies in both families and the union is in one P;
  - if A depends only on its non-shared variable, then A ∩ B ≠ ∅ (independent coordinates), which is
    impossible; likewise for B;
  - otherwise both depend on both variables. By Lemma 2 each misses at most one value of x_j, so by
    Lemma 3 they meet, which is impossible.
  - Hence U is closed under disjoint union (finite Ω; induct on the number of pieces), so J ⊆ U. □
- **n = 2** fails exactly at K = Eq ({a} = X \ {a′}), matching the computed exception (J = D).
- **Formalisation status (2026-10-21).**
  - Lemma 2 is Lean-checked: `TransportGeneral.PairNormalForm.indep_of_two_empty_rows`. With
    3 ≤ n, two distinct empty rows of k(cmp)⊕α⊕β force independence of y.
  - Lemma 3 is Lean-checked: `pairLocal_meet`.
  - Lemma 1 (P ⊆ normal form) and the final induction are hand-written and routine.
    Formalising them needs the countable-disjoint-union case of Dynkin systems on a finite type.

**§18 extended: hidden twists at 4×4×4 (2026-10-21; `verification/hidden_twist_search.py`).**
- **Search.** Cutting planes with MILP separation over all 0/1 span vectors, so the result is a
  certified carrier state. Objective: minimise Λ(g) for a non-binary ray g. Four seeds, four
  different starting rays (all with values 0/1/2).
- **Every run returns the same form:**
  - each pair law is **uniform 1/9 on a 9-edge allowed relation**;
  - min Λ(g) = −1/9;
  - in the run printed in full (seed 0), one value of x₀ goes unused. That is the 3×4×4 pattern
    embedded in 4×4×4.
- **Reading (candidate):** at these sizes the relational, uniform-on-support pattern looks like the
  *extremal* hidden twist, the atom of hiding. Hidden twists that push a non-binary witness
  furthest negative are possibilistic patterns spread evenly.
- **Not shown:** that every hidden twist is a mixture of such patterns; the behaviour at larger
  sizes (5×4×3, 5×5×3).

## 21. Toward "hiding ⇔ non-compressed" (2026-10-21)

**Non-compressed ⇒ hides (proved).**
- Sullivant Thm 2.4: non-compressed ⇔ some facet of the marginal polytope has width ≥ 2 ⇔ V₊ has a
  non-binary extreme ray.
- Maharam 6.1 and separation then give a hidden twist (§16).
- So every non-compressed size hides, e.g. 4×4×3 and 5×4×3, 5×5×3 (Ohsugi–Hibi), and everything
  larger.

**Theorem (hand; uses the Lean transport lemma).** For sizes r×s×2 (one variable binary, any r and
s), **D = V₀₁**: every 0/1 vector in the span of pair indicators is buildable. Hence (unimodular ⇒
compressed ⇒ all extreme rays 0/1) **every carrier state is a convex combination of point masses:
no r×s×2 triangle hides a twist.**
- *Proof.* Let S ⊆ X₀×X₁×{0,1} have 1_S in the span, with slices S₀ and S₁ at x₂ = 0 and 1.
  Span membership gives 1_{S₀} − 1_{S₁} = h(x₀) + k(x₁), taking values in {−1, 0, 1}. So h and k
  are integer-valued after a shift, and spread(h) + spread(k) ≤ 2.
  - **(a)** If h or k is constant, the difference regions {h+k = ±1} are cylinders in one variable.
    The two slice pieces {x₂=0, h+k=1} and {x₂=1, h+k=−1} are pair events on (x₁,x₂) or (x₂,x₀).
  - **(b)** Otherwise h ∈ {a, a+1} and k ∈ {b, b+1} with a + b = −1. Then {h+k=1} = A×B and
    {h+k=−1} = Aᶜ×Bᶜ. The union of the two slice pieces is the pullback of the 2×2×2 set
    {u=v=w}, which is buildable on 2×2×2 (D = V₀₁ there, 70 sets), under the coarsening
    (x₀, x₁, x₂) ↦ ([x₀∈A], [x₁∈B], [x₂=0]). By transport (`TransportGeneral.mem_pre`) it is
    buildable.
  - In both cases S = (S₀ ∩ S₁) ⊔ pieces, with S₀ ∩ S₁ a pair event on (x₀,x₁) and all pieces
    disjoint. A Dynkin system is closed under finite disjoint unions. □
- **Cross-check (exact):** |D| = |V₀₁| at 2×3×4 (17,878), 3×4×2 (17,878), 2×2×5 (9,826).

**Status of "hiding ⇔ non-compressed".**
- Proved for every size with a binary variable, and for all non-compressed sizes.
- Exact for 3×3×3 and 4×3×3.
- **Open only for r×3×3 with r ≥ 5** (compressed per Ohsugi–Hibi; the gap half unproved).

**Conjecture 2 test (coarsening criterion), 3×4×4** (`verification/conj2_coarsening.py`, output saved).
- 150 sampled families: 104 have worlds; of the 46 twisted, 23 are visible via a twisted
  coarsening onto 3×3×3, 23 are certified hidden, and **0 are visible without a twisted
  coarsening**.
- Consistent with "visible ⇔ some ≤3-value coarsening twisted". The samples are biased toward the
  hidden family by mixing.

**Conjecture 3 (the atom), evidence at 3×4×4** (2026-10-21; `verification/atom_vertices*.py`).
- **Random objectives** over S′ = {consistent pair laws ≥ 0 on all 0/1 span vectors} reach only the
  **48 point masses**. The hidden region is invisible to generic directions, consistent with §19.
- **Targeted objectives** (minimise Λ(g) for 120 of the 1,728 non-binary extreme rays) reach **120
  distinct hidden vertices, all uniform 1/9 on a 9-cell support in every pair** (88 + 2,300 MILP
  cuts).
- **Reading:** at 3×4×4, every hidden vertex of S′ found is a relational "allowed pairs, evenly
  spread" pattern. The atom candidate survives a targeted test.
- **Still open:**
  - whether these 120 are relabellings of one pattern (orbit count under 3!·4!·4! value
    permutations; vertices not saved this run);
  - whether S′ has hidden vertices not reachable this way;
  - whether S′ = S (the carrier-state set itself).

**r×3×3 (the remaining case of "hiding ⇔ non-compressed"): reduction recorded.**
- Slices along x₀ pairwise differ by additive {−1,0,1} patterns on 3×3. Merging x₀-values with
  equal slices makes a 0/1 span vector a pullback from m×3×3, where m is the number of distinct
  slices.
- m ≤ 14: the largest additive-difference class of 3×3 binary patterns has 14 members (class sizes
  1:102, 2:36, 3:36, 6:12, 8:18, 14:1).
- So D = V₀₁ at all m×3×3 with m ≤ 14 would settle every r×3×3. That is computationally out of
  reach (up to 126 points). A structural argument is needed: e.g. a decomposition like the r×s×2
  slice proof, using the explicit 14-member class.

**Updates (2026-10-21).**
- **Lean:** the rectangle step of the r×s×2 theorem is checked (`TransportGeneral.rect_mem`; 0
  sorry). It contains an explicit construction of {all equal} on 2×2×2: E = ((A ⊔ B)ᶜ ⊔ C)ᶜ with
  A = {x₀=0, x₁=0}, B = {x₁=1, x₂=1}, C = {x₀=0, x₂=1}. Transport handles any value type. The
  cylinder step and the span algebra remain hand.
- **The atom is one pattern:** the 120 hidden vertices found at 3×4×4 form **a single orbit** under
  value relabelling (S₃×S₄×S₄) and the x₁↔x₂ swap (`verification/atom_orbits.py`, output saved).
  Every extreme hidden twist found is the same "allowed pairs, evenly spread" pattern up to
  renaming.
- **Why one orbit (checked 2026-10-21):** all **1,728 non-binary extreme rays at 3×4×4 form one
  orbit** under S₃×S₄×S₄ and the x₁↔x₂ swap (orbit size 1,728 = 6,912/4). So at the threshold
  there is exactly one kind of non-compressed facet, and the single-orbit atom is largely forced
  by symmetry.
- What is *not* forced: the extremal hidden twist is uniform on its support. The atom claim
  becomes substantive only at larger sizes (4×4×4, 5×4×3), where several ray orbits may exist:
  do all their extremal hidden twists reduce to embedded copies of this pattern?
