# Full-cycle controlled assembly

*Campaign 20, 2026-07-15. Counterexample-route scaling after the exact
fixed-carrier refutation of T-FIN.*

## 1. Input object

Let `K` be the certified 18676-event full-cycle OML on 6186568 points from
`oml_nonprofile_fibre_splitter_calculus.md`. It is finite, concrete,
sigma-complete, centre-free and order-separated; it contains the exact four
conditional cells, avoids both activation gates, reconstructs neither
same-side boundary, and preserves the node-6 PJH defect. It is `Phi`-tame.

Campaign 20 does not seek another finite repair. It asks whether copies of
`K` admit a coherent finite-support/direct-limit grammar which can then carry
the omega-one CSS/no-global-section obstruction through sigma-completion.

## 2. Assembly category

Fix an incidence hypergraph `H`. Its overlap category has rectangle objects
`e`, nonempty finite incidence faces `sigma`, and monic port maps
`j_{sigma,e}:A_sigma -> K_e` satisfying the face cocycle equalities. For
finite `F`, let `Omega_F` be the compatible fibre product of the point-state
carriers over every declared face. For `F subset G`, coordinate restriction
is `pi_GF:Omega_G -> Omega_F`.

The desired finite assemblies are concrete OMLs `L_F subset P(Omega_F)` such
that pullback along `pi_GF` is an injective OML homomorphism and, inside every
common `L_H`,

`L_F intersection L_G = L_{F intersection G}`

after the declared face identifications. Surjectivity and functoriality of
the carrier projections are explicit hypotheses, not consequences of local
state nonemptiness.

## 3. Finite-support conservative normal-form theorem

**NF.** Adjoining a fresh grammar copy to any finite assembly has a
terminating and confluent reduction system with:

1. a unique reduced normal form and unique minimal finite support;
2. no identifications beyond the declared overlap faces;
3. for every new event `z`, a greatest old lower shadow `lambda_F(z)` and a
   least old upper shadow `upsilon_F(z)`;
4. complement preserving support and extrema supported in the union of the
   operand supports;
5. every critical overlap accounted for by a declared port rule or a
   certified full-cycle repair rule.

If NF holds, pullback maps preserve all OML operations, common-stage
intersections are exact, and the finite-support colimit is a concrete OML of
cylinder events. If every finite stage is centre-free and activation-escaping
and all carrier projections are onto, then the colimit has centre `{0,1}` and
escape persists: any central or nonzero event has finite support and can be
tested at that stage. **Hand proved conditional on NF.** The colimit is not
thereby sigma-complete.

The narrow falsifiable lemma is the **two-copy critical-pair theorem**:
every legal overlap of two `K` copies has joinable reductions, no undeclared
intersection, no old-extremum drift, and no centre or escape failure. Together
with termination and a proof that all critical pairs have support at most
two, Newman's lemma yields NF. Pairwise success alone is insufficient without
that locality theorem; a three-copy diamond can fail first. **Open.**

## 4. Adjacent-rectangle factor checkpoint

Take rectangles `R={0,1}x{0,1}` and `S={1,2}x{1,2}`. They share exactly the
conditional cell `D11`. The declared overlap is the full 56-event cell—not
only its `q,r` coordinate events—so the ten-event activation interface,
coordinate block, mediators and auxiliaries are all identified.

The exact compatible carrier is

`X_R times_{St(D11)} X_S`

and has `211897540016` points. Each projection is onto. For every one of the
224 shared-cell states, each side fibre has size between 1322 and 45324.
Pullbacks of shared-state predicates agree iff their 224-bit predicates
agree, so the declared 56-event interface is faithful and order-reflecting.
**Executable verified** by
`full_cycle_adjacent_rectangle_factor_checkpoint.py`, payload `0920a19b...`.

This does not yet prove completed-grammar intersection. A completed copy may
contain additional events saturated over its shared cell. The exact next test
enumerates position-11-saturated events in `R` and position-00-saturated
events in the reoriented `S`, converts them to 224-state traces, and compares
the two trace families. Equality with the 56 cell traces proves the
intersection gate; an extra common trace is the smallest countermodel to NF.

The census passes exactly. In the `R` orientation (shared cell at local
position 11) and the reoriented `S` copy (shared cell at local position 00),
each 18676-event completion has exactly 56 shared-coordinate-saturated
traces. Both trace families equal the original 56-event cell family; their
intersection has 56 members and no extra trace. Surjectivity of the compatible
carrier projections then gives

`image(K_R) intersection image(K_S) = image(D11)`.

**Executable verified** exhaustively over every completed event and macro
fibre by `full_cycle_adjacent_rectangle_intersection.py`, payload
`d51b57b847707dc8dd79397662c3dbbac72243d9a5e867cbf139bb76d9f8ec69`.
This proves the two-copy intersection gate, not closure/latticehood of the
union of both images.

## 5. State relation and MBRC gate

On the finite activation pattern charging both row triples, every point state
of `K` has profile `0000` or `1111`. The same holds for every abstract
two-valued state: restriction to each faithful 56-event cell is one of the
224 certified cell states, and each activated cell forces its incident bits
equal. Both diagonal values occur. Because `K` is finite,

`R_point = R_fa = R_sigma = {0000,1111}`

on this face. **Hand proved using executable single-cell state exhaustiveness
and faithful embeddings.** This is not an off-face classification of all
states.

For any two-copy completion, finite MBRC must be checked against the actual
completed event algebra and full maximal-block atlas:

- no-gain: no activated mismatch is introduced;
- no-loss: both diagonal values extend;
- raw compatible abstract states extend through every completion-created
  block.

Finite success remains `Phi`-tame. The fa/sigma gap can arise only after the
countable or uncountable assembly.

For the full-cell overlap there is already an exact activated state theorem.
Every abstract two-valued state on any faithful common completion assigns one
bit to every external coordinate of both rectangles: each copy is internally
diagonal and the restrictions agree on the identified cell. Both values occur
on the compatible-pair carrier because the activated cell state with fixed
`q=r=b` is unique for each `b`, so the two unique activated rectangle points
glue over the entire shared cell. Hence every faithful finite concrete
completion on that carrier has no-gain and no-loss on the activated
projection. **Hand proved** from executable cell-state and embedding premises.

This finite global-state statement does not replace maximal-block MBRC. The
actual completed atlas must still be classified enough to show how new blocks
restrict to both copies and the shared cell, and that the two point witnesses
give compatible families over every new block.

## 6. Current decision boundary

The full-cell adjacent overlap is the coherent-grid test. A paste identifying
only one four-element boundary bit is a distinct transport experiment and
re-enters the known nonmaximal-subalgebra crossed-cut obstruction; it may be
useful for puncture transport but cannot substitute for the full-cell
intersection theorem.

Repeated full-cell sharing may itself be too faithful for the eventual
uncountable puncture hub: it makes activated transport deterministic and risks
the previously proved shared-boundary rigidity. The likely final architecture
uses full-cell overlaps only inside finite rectangle complexes and transported
proper nonseparating quotient interfaces between uncountably many complexes.

The first next action is the saturated-trace intersection census in Section
4. Do not form a direct limit, invoke Zorn, or claim sigma-completeness before
NF and the three-copy locality/diamond obligation are resolved.

## 7. Adjacent-union factor boundary

The union carrier has seven distinct conditional cells
`00,01,10,11,12,21,22`. Its macro index is
`(a0,a1,a2,q0,q1,q2,r0,r1,r2)`. Exactly 23998 macro fibres are nonempty, with
sizes from 1 to 2494357888, and the total carrier has 211897540016 points.
All seven cell projections contain all 224 states. **Executable verified** by
`adjacent_full_cycle_union_factor_checkpoint.py`, payload `2f402b77...`.

Naively pulling the two 18676-event MDD tuples to all global macro fibres
would require 896373296 root references, about 7.17 GB before a single mixed
closure step. This is a natural computational boundary; no mixed cut was
searched and no closure claim is made.

The exact missing compression theorem is:

> **Fibre-product rectangle normal form (FRNF).** Every event/bound needed for
> the adjacent closure is a finite disjoint union of rectangles
> `A(u) times_D B(v)`, tagged by a shared 224-state trace, with a uniformly
> controlled rank; complement and orthogonal union preserve that class and
> its rank bound, and extrema admit old-side shadows.

Here `u,v` are canonical local-copy descriptors. FRNF would provide the
smallest exact mixed-closure engine and feed the two-copy critical-pair
theorem. Its failure must supply a finite sequence whose required disjoint
rectangle rank grows, or a first mixed bound with no local shadows. **Open.**

The strongest unconditional substitute is the **Boolean-envelope rectangle
theorem**. For shared state `s`, let `B_s^L,B_s^R` be the Boolean algebras of
fibre subsets generated by restrictions of all 18676 local events. The mixed
complement/disjoint-union closure lies in
`direct_sum_s (B_s^L tensor B_s^R)`, so every event has a finite disjoint
atom-rectangle normal form. If `p_s,q_s` are the envelope-atom counts, rank is
at most `sum_s min(p_s,q_s)`; the crude singleton bound is 6186568. **Hand
proved.** No cardinal-independent bound exists: the Boolean diagonal on
`{1,...,n}^2` has rectangle rank exactly `n`; `n=2` is the first nontrivial
control. **Hand proved.**

Boolean-envelope sides need not be actual local OML-event traces. The
narrower load-bearing lemma is **shadow realizability**: every generated
mixed event's universal fibre core and least local envelope of its existential
hull are restrictions of coherent local events. These are respectively the
greatest-old-lower and least-old-upper shadows, hence preserve old extrema.
A failure gives one explicit generated word and its missing local trace.
**Open.**

## 8. Maximal-block factorization and the horn gate

Exact intersection and activated diagonal composition do not force mixed
maximal blocks to factor. An abstract completion can adjoin a horizontal
Boolean block without altering either property. **Hand refuted** at that
hypothesis level; this does not refute factorization for the least adjacent
closure.

A sufficient criterion is that every maximal block `C` be
`Bool(B_R union B_S)` for maximal old blocks which agree on a Boolean context
of the shared cell and commute crosswise. Then ultrafilters on `C` are exactly
compatible old ultrafilter pairs and blockwise finite MBRC factors. **Hand
proved** by Boolean amalgamation.

The smallest coherence obstruction is a `2x1` horn: compatible
`x1,x2 in R` and `y in S` such that each `(xi,y)` has an aligned old-block
container but no single aligned pair contains all three. If every such horn
amalgamates, the next obstruction is a `K2,2` container cycle. Exact one-copy
block/container data is a prerequisite. **Open.**
