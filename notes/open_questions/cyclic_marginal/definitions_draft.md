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
| Rings ≥ 4: twists hidden even with finitely many values | Th | hand + certified example |
| Case 1: asynchronous stations | A, then Tv in the finite reading; U for the long-run worlds | simulation |
| Case 2: one quantity in time windows | W | simulation |
| Case 4: Sagnac clocks | Th or Tv, i.e. the impossible-point question | design only |

## 8. Candidate theorems, as the definitions suggest them (hunch-shaped; to be earned)

- **H1 (local generation along trees is complete).** If the view graph is a forest, every coherent
  body of locally generated information has a world. *hand*
- **H2 (where hiding lives).** A twist can hide, i.e. there is coherent locally generated
  information with no world, exactly when the views form a loop, there are infinitely many values,
  and answers add up only finitely (two-valued). *Lean + hand*
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
- **H3, sharpened (candidate):** "global information is strange" = information that is a sum of
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
