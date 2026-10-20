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

## 10. Philosophical horizon (only after the classification earns its keep)

Plato (worlds as given forms), Aristotle (potential infinite; finite adding), Kant (totality as a
task; global information "aufgegeben"). The hope is that H2 and H3 say something precise about
each.
