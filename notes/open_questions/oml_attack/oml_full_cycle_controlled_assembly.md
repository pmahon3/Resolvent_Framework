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

The horn gate admits a sharper context formulation. Let `Gamma` be the
aligned-pair relation on old maximal blocks, indexed by Boolean contexts `K`
of the shared cell, and let `C_R(X)` (respectively `C_S(Y)`) be the contexts
admitting an aligned old block containing the finite set `X` (respectively
`Y`). If aligned pairs factor completely inside each context, then a `2x1`
horn `x1,x2;y` amalgamates exactly when

`C_R({x1,x2}) intersect C_S({y})` is nonempty.

Inside one OML, finite pairwise-compatible events together with `K` lie in a
common Boolean block, so for compatible `x1,x2`,
`C_R({x1,x2})=C_R(x1) intersect C_R(x2)`. Thus the horn question reduces to
an exact finite 2-Helly test on context-availability sets. **Hand proved.**
Pairwise aligned containers alone do not suffice: three old blocks can
separately contain `(x1,y)` and `(x2,y)` while the only block containing
`x1,x2` is not aligned with the `y` block. **Hand refuted** by this abstract
block-incidence control; it is not asserted realizable in the current OML.
The load-bearing open hypothesis is completeness of the cross-copy aligned
relation within each shared context. This can be tested from context
commutation signatures before a global maximal-block census.

## 9. Coarse shared-state shadow checkpoint

For a local event `A` in the left copy, write `E_A` for the shared-cell
states on which its section is nonempty and `U_A` for those on which its
section is the whole local fibre; define `E_B,U_B` on the right similarly.
Because the adjacent carrier is the full fibre product over each of the 224
shared states, two pulled cylinders are disjoint exactly when
`E_A intersect E_B` is empty. For such a pair the coarse three-valued
classification of their union is exactly

`(E_A union E_B, U_A union U_B)`.

The completed left and right copies realize respectively 277 and 307 such
coarse types. All 2257 disjoint cross-copy type pairs have a union type
realized by an actual local descriptor in at least one copy; complement
types are also locally realized. **Executable verified** by
`adjacent_full_cycle_boolean_envelope_shadow.py`; the calculation replays the
exact MDD grammar but has no independent implementation. The fibre-product
equivalence and the formulas above are **Hand proved** and were hostile
reviewed.

Deterministic payloads are `b893c79f...` for the coarse census and
`4fb1d4c4...` for the tagged-grid census; both were reproduced field-for-field
under `PYTHONHASHSEED=0` and `12345`.

This closes only the coarsest obstruction. A partial section is forgotten
entirely by `(E,U)`, so a local event with the same type need not equal the
mixed union or supply its greatest-old-lower or least-old-upper shadow. For
`z=A_L union B_R`, the exact left-cylinder lower core has section `X_s` when
`B_s` is full and `A_s` otherwise; its least set-theoretic left-cylinder hull
has section `X_s` when `B_s` is nonempty and `A_s` otherwise. The symmetric
right formulas also hold. **Hand proved.**

The discriminating computation was exact MDD realizability of these four
piecewise cores/hulls over every actual local descriptor and relevant
opposite coarse class. Its first failure and the repaired criterion follow.

That exact-envelope criterion already fails in deterministic scan order. For
retained left event `0` and right event `full17=0x22`, the latter is possible
on 71 shared states and full on none. Its exact left-coordinate cylinder has
root hash `14d35945...` and is absent from the left 18676-event family after
only five descriptor/class pairs and ten core/hull tests. **Executable
verified** by symbolic MDD equality and independently corroborated from the
formal `0x22` state table plus the banked 56-trace intersection theorem. This
refutes exact coordinate-cylinder-envelope realizability, not conservative
embedding: absence of the set-theoretic hull does not exclude a strictly
larger least actual old-event upper bound. Deterministic replay passed with
payload `2cfca54f...`.

The distinction is real. Among all 18676 old left events, that cylinder has
1152 upper bounds and a unique least one, event `full17=0x505` (index 645,
root hash `7c99f15e...`). It has four old lower bounds and a unique greatest
one, `full17=0x404` (index 516, root hash `84444aa3...`). **Executable
verified** by exhaustive reduced-MDD subset tests and the certified principal
upsets. Thus the first missing exact hull is repaired by a nontrivial local
envelope operator; it is not a conservative-embedding obstruction. Final
emit/replay payload `49159f2b...` passed under `PYTHONHASHSEED=12345`.

The first-round tagged-grid census contains 172787 disjoint event pairs:
123440 are genuinely mixed-shaped, 24540 are left-cylinder-shaped only,
24540 right-cylinder-shaped only, and 267 shared-state-saturated-shaped.
These are shape classifications, not membership assertions. A disjoint union
has an OR-tag `(A times all) union (all times B)`; its complement is the
AND-rectangle `A^c times B^c`. Therefore OR-tags alone are not a closed
grammar, and the next exact alphabet must contain both OR and AND tags with
canonical restricted-root provenance. **Executable verified** for the
first-round census; arbitrary-depth closure remains **Open**.

## 10. Conservative embeddings are kernel retractions

Let `A subset C` be finite concrete OMLs with the same `0,1` and complement.
The inclusion preserves all old binary joins and meets exactly when there is
a monotone deflationary order retraction

`rho_A:C -> A`, with `rho_A(a)=a` and `rho_A(c) <= c`.

For sufficiency, if `j=x join_C y`, then `rho_A(j)` is an old upper bound of
`x,y` below `j`; comparison with `x join_A y` gives equality, and complements
give meets. For necessity define
`rho_A(c)=join_A {a in A:a<=c}`. Finiteness and preservation of old joins
make this join remain below `c`; monotonicity and retraction are immediate.
**Hand proved.** Thus greatest-old-lower shadows alone are the exact finite
criterion; least-old-upper shadows follow by complement.

Surjective or even bijective state restriction does not imply this kernel.
On four points, embed the six-event concrete `MO2` generated by
`p={1,2},q={1,3}` into the full powerset. All four point states restrict
bijectively and order-separate, but `p join q` changes from the universe to
`{1,2,3}`. **Hand refuted** by this explicit finite control.

The state version uses, for a new event `c`, the old states all of whose
extensions charge `c`. When the chosen new states and their restrictions
order-determine `C` and `A`, old events below `c` are exactly those whose old
supports lie in this safe-state set; the kernel exists exactly when those
supports have a largest representing old event. **Hand proved.** For the
pulled event producing the first missing hull, the true left lower core is
`0` because the opposite universal mask is empty, while its least old upper
is `0x505`. Thus this mixed event supports the weaker kernel criterion despite
refuting literal hull realizability. The separate `0x404` result is the
greatest old event inside the 71-state cylinder, not the lower shadow of the
original pulled event.

The decisive finite-support test is now exact: for every one-step mixed
disjoint union, certify a unique greatest old lower shadow on both sides.
Complement supplies upper shadows. A first multiplicity refutes conservative
embedding at that step; exhaustive success gives the first transition layer
of the kernel grammar. **Open.**

For a candidate set `c`, let `L(c)` be the old events contained in it and let
`J(c)` be their join in the finite old lattice. A greatest old lower exists
exactly when `J(c) subset c`, in which case it is `J(c)`. During an incremental
join fold, the first partial join escaping `c` is already a permanent
certificate of failure: every later join dominates it. **Hand proved.** This
turns the kernel scan into a falsification-first join fold rather than a full
maximal-bound census.

The stable order-theoretic implication is **Lean certified** in
`QuerySystem/FullCycleAssemblyKernel.lean`:
`map_sup_of_deflationary_retraction`,
`map_inf_of_inflationary_retraction`, and
`map_inf_of_complement_conjugate_deflationary_retraction`. The last theorem
constructs the upper shadow by complement conjugacy from the lower kernel.
All three `#print axioms` reports are empty. The formalization assumes the
shadow retraction; constructing it for the adjacent mixed grammar remains the
open mathematical gate.
