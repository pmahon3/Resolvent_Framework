# Current handoff: two-common-block pullback architecture

## Repository state

- Repository: `pmahon3/Resolvent_Framework`
- Branch: `oml-descent-sigma-essential-reduction`
- Relay accepted commit: use `.agent-relay/CURRENT.json`; do not override it manually.
- Mathematical baseline: `e9fde9f` — `Complete non-atomic pullback OML audit`

The relay runbook and compact state are authoritative for stable programme-wide rules. This handoff supplies only the next mathematical task.

## Mission

Determine whether the seven-block centre-free OML skeleton can support the first **genuine two-edge coarse compatibility relation**.

The completed `(5,11)` construction is banked:

\[
A \longleftrightarrow_D C
\]

survives full mixed completion as a concrete, σ-complete, centre-free seven-block OML. Its endpoint relation is nonrectangular and nonfunctional, and its countable-coordinate realization exposes noncompact eligible σ-state topology. Nevertheless, it is \(\Phi\)-tame because there is only one quotient edge and the explicit carrier has the finite common-point extension property.

The next target must leave this one-edge class.

The 42 qualifying non-atomic selector pairs split into six automorphism orbits. Two orbits have two common maximal blocks and are the first candidates for inequivalent shared-quotient constraints:

- `O2`: representative `(5,51)`, orbit size 8, two common blocks, five-cycle support type;
- `O3`: representative `(15,45)`, orbit size 4, two common blocks, four-cycle support type.

The central question is:

\[
\boxed{
\text{Do either O2 or O3 produce two inequivalent quotient edges after full OML completion?}
}
\]

A second copy of the same restriction equation is redundant and does not count as monodromy.

## Required initial audit

Read at least:

- `CLAUDE.md`
- `.agent-relay/RUNBOOK.md`
- `.agent-relay/STATE.md`
- `notes/open_questions/oml_attack/oml_nonatomic_pullback_completion.md`
- `notes/open_questions/oml_attack/oml_nonatomic_pair_classification.md`
- `notes/open_questions/oml_attack/oml_two_fibre_monodromy.md`
- `notes/open_questions/oml_attack/oml_distributed_sigma_selection.md`
- `notes/open_questions/oml_attack/relational_boundary_descent.md`
- `notes/open_questions/oml_attack/oml_lattice_taxonomy.json`
- `notes/programme/frontier_map.md`
- the existing seven-block skeleton, non-atomic-pair, and pullback verification scripts and schemas.

Reproduce the current certificates before modifying them.

Do not repeat the completed `(5,11)` one-edge audit except as a control.

## Part I — Compare O2 and O3 intrinsically

For representatives `(5,51)` and `(15,45)`, compute and record:

1. the two common maximal blocks;
2. all Boolean regions determined by the selector pair in each common block;
3. the meet and complement-region events;
4. interval sizes and generated sub-OML size;
5. propagation supports of shared and private regions;
6. the support cycle and all overlap algebras along it;
7. whether the two common blocks see the same shared finite datum or genuinely different data;
8. the automorphism stabilizer and any symmetry exchanging the two common blocks;
9. which representative has the smaller substitution and closure complexity.

Choose the minimal serious candidate by structural complexity, not by event-ID order. Preserve the other orbit as a control.

Produce a finite architecture table:

| Orbit | Pair | Common blocks | Shared regions in block 1 | Shared regions in block 2 | Candidate quotient edges | Redundant/inequivalent |
|---|---|---:|---|---|---|---|

## Part II — Define the two-edge substitution datum

For the chosen pair, define coarse Boolean σ-algebras \(A,C\) and two proper shared subalgebra constraints:

\[
A \longleftrightarrow_{D_1} C,
\qquad
A \longleftrightarrow_{D_2} C.
\]

Each edge must arise from actual event overlap in one common maximal block. Do not impose a state relation externally.

Specify:

- embeddings \(D_i\hookrightarrow A,C\);
- the carrier maps or concrete region refinements;
- how every original skeleton event lifts;
- which blocks see full \(A\), full \(C\), \(D_1\), or \(D_2\);
- whether \(D_1,D_2\) are distinct as embedded subalgebras;
- whether the two restriction equations jointly reduce to one common quotient.

The endpoint relation is

\[
R=\{(u,v):
u|_{D_1}=v|_{D_1},
\quad
u|_{D_2}=v|_{D_2}\}.
\]

Classify it as:

- one redundant edge;
- graph of a full isomorphism;
- pullback over \(D_1\vee D_2\);
- genuinely two-edge but acyclic after coordinate reduction;
- genuine cyclic/monodromy datum.

## Part III — Finite controls before infinite fibres

Construct the smallest finite Boolean controls that distinguish:

1. duplicate identical edges;
2. nested edges \(D_1\subseteq D_2\);
3. jointly generating edges \(D_1\vee D_2=A\) or \(C\);
4. transverse proper edges;
5. a nonfunctional relation with more than one partner on both sides;
6. a relation whose two-edge composite is nontrivial.

For each control, calculate:

- endpoint ultrafilters;
- relation size and degree sequence;
- whether the relation is rectangular or functional;
- whether either edge is logically implied by the other;
- connected components;
- fixed-point/monodromy representation if meaningful.

Do not introduce noncompact infinite algebras until a finite control exhibits a genuinely new relation.

## Part IV — Full mixed OML closure

For every serious finite control:

1. construct the concrete raw event family;
2. close under complement and disjoint union;
3. compute every binary meet and join;
4. verify orthomodularity;
5. enumerate all maximal Boolean blocks;
6. compute all overlap-generated boundaries;
7. compute the global centre using all maximal blocks;
8. determine whether the finite quotient onto \(L^\ast\) survives;
9. determine whether additional maximal blocks create, identify, or destroy quotient edges;
10. determine whether closure propagates a shared coarse factor into the centre.

The result must distinguish:

- raw two-edge intent;
- completed relation graph;
- redundant constraints introduced by extra blocks;
- genuinely inequivalent constraints.

Exactly seven maximal blocks are not required, but every resulting maximal block must be classified.

## Part V — State-selection analysis

If completion leaves two inequivalent edges, determine whether they create an actual obstruction or remain tame.

For a finite coherent face \(p\), analyze:

\[
X_A(p)\times X_C(p)
\]

subject to both restriction equations.

Establish separately:

1. existence of a finitely additive compatible pair;
2. σ-solvability of every finite set of eventwise equations;
3. existence or nonexistence of a complete compatible σ-pair;
4. whether a common-point or common-σ-extension argument repairs the full finite face;
5. whether the relation reduces to a single pullback over \(D_1\vee D_2\);
6. whether a true cycle transport map exists;
7. whether the eligible σ-locus is noncompact.

A finite nonrectangular relation is not a failure of GSD. A claimed obstruction must exclude all compatible σ-states.

## Part VI — Positive theorem route

In parallel, seek the strongest correct tameness theorem.

Candidate hierarchy:

\[
\text{duplicate or nested quotient edges}
\Longrightarrow
\text{single-pullback reduction};
\]

\[
\text{two edges generated by one common carrier projection}
\Longrightarrow
\text{common-point repair};
\]

\[
\text{acyclic quotient network with compatible endpoint extension}
\Longrightarrow
\Phi;
\]

\[
\text{genuine cyclic quotient network}
=
\text{first unresolved class}.
\]

A theorem showing that every O2/O3 completion collapses to one pullback, becomes central, or remains point-repairable is a successful outcome.

## Part VII — Infinite model only after the finite gate

If a valid centre-free completed two-edge architecture survives, instantiate it with countable-coordinate σ-fields or another explicit coarse σ-complete Boolean system.

Prove independently:

- concreteness;
- σ-completeness;
- latticehood and orthomodularity;
- maximal-block classification;
- trivial centre;
- noncompact eligible σ-state topology;
- finite-fragment σ-solvability;
- complete σ-selection or its failure.

Do not infer the infinite result from finite approximants.

## Required outputs

Create:

- `notes/open_questions/oml_attack/oml_two_edge_pullback_completion.md`
- `notes/open_questions/verification/seven_block_two_edge_pair_audit.py`
- a stable JSON certificate and independent verifier if a substantial finite completion is produced.

Cross-link the new note from the existing non-atomic pullback, pair-classification, monodromy, descent, taxonomy, and frontier files only where the result changes status.

Do not add a Lean theorem unless it certifies a reusable mathematical step rather than merely restating a strong hypothesis.

## Outcome classification

Use one of:

- **Outcome A — genuine σ-selection obstruction:** a valid centre-free σ-complete OML has a coherent finite face with finite-fragment σ-solvability but no complete σ-selection.
- **Outcome B — two-edge but tame:** a genuine two-edge completion exists but every coherent finite face σ-lifts.
- **Outcome C — edge collapse:** completion reduces both common-block constraints to one pullback over a generated quotient.
- **Outcome D — central propagation:** mixed closure forces a nontrivial common central factor.
- **Outcome E — OML completion obstruction:** the intended two-edge substitution loses latticehood, σ-completeness, or orthomodularity.
- **Outcome F — orbit-specific split:** O2 and O3 behave differently; state exact results for each.
- **Outcome G — minimal unresolved datum:** state the exact embeddings, closure obligation, and selection question that remain open.

## Acceptance criteria

The task is complete only if it answers:

1. Which of O2 or O3 is the minimal two-common-block candidate?
2. What two quotient constraints do the common blocks actually impose?
3. Are the constraints inequivalent after full completion?
4. Does the completed family form a concrete OML?
5. Does an infinite version remain σ-complete?
6. What maximal blocks arise?
7. Is the centre trivial?
8. Does the completed relation reduce to a single pullback?
9. If not, is there genuine monodromy or only a larger acyclic pullback?
10. Does a finite face expose noncompact topology?
11. Are all finite compatibility fragments σ-solvable?
12. Does complete compatible σ-selection exist?
13. What reusable tameness or no-go theorem is obtained?
14. What is the single best next task?

## Epistemic constraints

- Do not count two common blocks as two quotient edges without computing the induced restrictions.
- Do not count repeated copies of the same equation as monodromy.
- Do not impose abstract ultrafilter relations not realized by concrete overlaps.
- Do not infer infinite σ-completeness from finite closure.
- Do not infer trivial centre from the finite quotient.
- Do not infer failure of \(\Phi\) from nonrectangularity or noncompactness.
- Do not treat state-space pullbacks, carrier pullbacks, and σ-state pullbacks as interchangeable.
- Preserve the distinction between executable certificate, hand theorem, and Lean theorem.
- A proof that both two-common-block orbits collapse to the tame hierarchy is a successful result.

## Decisive question

\[
\boxed{
\text{Can two common maximal blocks enforce inequivalent coarse restrictions
without OML completion collapsing them, centralizing them, or restoring }\Phi\text{-tameness?}
\]
