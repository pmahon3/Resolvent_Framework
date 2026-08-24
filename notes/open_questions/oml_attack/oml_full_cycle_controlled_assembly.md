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

The saturated-trace intersection census specified here was completed in
Section 4. Its positive result permits the adjacent-union analysis below, but
does not authorize a direct limit, Zorn argument, or sigma-completeness claim
before NF and the three-copy locality/diamond obligation are resolved.

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

More explicitly, for retained old event `A` and opposite universal mask `U`,
let

`I_U(A)={D in L : trace_s(D) subset trace_s(A) for every s notin U}`.

These are exactly the old left events below the pulled mixed union, and its
kernel is `kappa_U(A)=join_L I_U(A)` precisely when that join still satisfies
the displayed trace inequalities. **Hand proved.** Coarse `(E,U)` data cannot
decide this because the partial restricted roots of `A,D` enter pointwise.

A useful sufficient class is also exact. If the cylinder on `U` has greatest
old lower `h`, and every old `D subset A union cylinder(U)` commutes with `A`,
then Boolean decomposition over `A` gives
`kappa_U(A)=A orthogonal_join h`. **Hand proved.** Compatibility is load-
bearing: in the concrete six-event `MO2 subset P(4)`, take
`A={1,2}` and the nonevent `H={3}`. Although the greatest old event inside
`H` is `0`, the old lower `{1,3}` lies in `A union H` and its old join with
`A` is the universe, which escapes. Thus `A join h` is not a kernel and the
core has no greatest old lower. **Hand refuted** by this explicit control.
The scanner should therefore serialize the first skew lower incompatible
with `A`, not merely cylinder-envelope data.

### 10.1 Bounded kernel discriminator and scalar stop

The first 100 symbolic kernels in deterministic scan order have now been
checked. Sixty cores are already old events; the other forty all have a
certified unique greatest old lower. There is no join-escape certificate in
this prefix. The initial all-event fold required 743671 exact subset tests.
The atomistic replay gives the identical verdict using the old OML's 91 atoms:
3625 exact atom tests, 137 old-lattice folds, and maximum fold length ten, a
205.15-fold test reduction. **Executable verified bounded evidence** from a
deterministic producer receipt, payload `7be059ff...`; there is no independent
implementation, and this is not exhaustive finite evidence for all first-
round kernels.

The safe same-`U` existential antichain quotient reduces the two orientations
from 277/307 `(E,U)` classes to 77/89 universal masks. The resulting 3100216
figure is only the rectangular pre-admissibility ceiling. Applying the required
disjoint-existential predicate leaves exactly 28023 left plus 27699 right, or
55722 distinct admissible kernels. This corrects the earlier ceiling
interpretation. The former 23.1-billion all-event and 282.1-million atom
projections are conservative rectangular-ceiling projections, not exact live
work estimates. The exact quotient has 5070702 possible atom visits and at
most 10141404 uncached atom-plus-accumulator bad-mask calls; the bottleneck is
building each 842-component core, so a measured larger atom prefix or the
horn atlas—not deeper all-event prefixes—is the live discriminator.

The next theorem must batch or invert the condition
`D subset A union cylinder(U)`. Define the bad-state mask
`Bad_A(D)={s: trace_s(D) not_subset trace_s(A)}`. Then `D` is an eligible old
lower exactly when `Bad_A(D) subset U`. Kernel failure is therefore a failure
of join closure of this mask predicate for an admissible universal mask. The
live target is a finite atlas of old non-set-union join defects and their bad-
mask propagation, not another scalar prefix. **Open.**

There are two exact non-scalar reductions. First, a finite OML is atomistic:
if the join of atoms below a nonzero event were proper, orthomodularity would
leave a nonzero difference containing another atom. Hence `J(c)` is the old
join of just the old atoms contained in `c`; the scanner need not test all
18676 events. **Hand proved.** Second, cumulative failure adds no witness
class beyond binary join horns. With
`b_A(D)=Bad_A(D)`, a failure exists exactly when some old `D1,D2`, their old
join `J`, and admissible `U` satisfy

`b_A(D1) union b_A(D2) subset U` but `b_A(J) not_subset U`.

If `J` is literal set union this is impossible, so only strict old join-
overshoot horns need enter the atlas. **Hand proved.** Atom-only scanning is
the immediate executable discriminator; the horn atlas is the fallback batch
proof if the remaining kernel count is still too large.

The horn atlas can itself be reduced to **atomic extension horns**
`(P,a,P join a)`, with `a` an old atom. If eligibility is preserved when one
eligible atom is joined to an eligible `P`, atomistic decomposition of any
second lower proves binary and hence finite join closure by induction.
Conversely a failing atomic extension is already an exact kernel witness.
Literal-union atomic horns can again be discarded. **Hand proved.** This is
the smallest complete provenance atlas currently known.

Admissible universal masks admit one further exact compression. For retained
existential type `E`, let `K_E` be the realized opposite `U` masks compatible
with `E`. For a horn put
`R=b_A(P) union b_A(a)` and `Q=b_A(P join a)`. Among masks in `K_E` containing
`R`, it suffices to check the inclusion-minimal ones. Equivalently define

`cl_E(R)=intersection {U in K_E:R subset U}`

on the live domain. The horn succeeds for every admissible `U` exactly when
`Q subset cl_E(R)`. The operator is extensive, monotone, idempotent, and
deduplicates verdicts by `(E,cl_E(R),Q)`. **Hand proved.** Checking only
globally minimal or maximal `U` masks is **Refuted** by finite trace/`MO2`
controls; conditional minima above `R` are load-bearing.

A naive atlas over all `(A,P,a)` triples has ceiling 63480321632 and is
rejected. The exact live quotient has 55722 kernels, hence 5070702 possible
atom visits and at most 10141404 uncached atom-plus-accumulator bad-mask calls.
The correct batching is
per retained `A`: process all admissible `U` simultaneously, group masks by
their current accumulator `P`, cache `b_A(a)` and `b_A(P join a)`, and retain
only horns with `Delta=Q minus R` nonempty. Deduplicate theorem verdicts by
`(orientation,E_A,cl_E(R),Q minus cl_E(R))`. **Hand proved** to be exhaustive.

The first representation gate is computing `b_A(J)` for strict joins; it is
not determined by the two input bad masks. A full event-pair containment table
would cost about 9.8 GB and is rejected. The representation selected here was
per-shared-state interning of restricted MDD roots and their containment
classes, followed by the bounded grouped and scale prototypes reported in
Sections 10.2--10.4. The complete nontrivial kernel quotient remains **Open**.

The first eager batching prototype confirms this representation boundary. It
attempted the complete descriptor
`(E_A,(b_A(a))_{a in 91 atoms})` for every retained `A`, but was explicitly
terminated at the 12-minute feasibility cap while still in that descriptor
census; peak observed RSS was 1060368 KiB and no receipt was emitted.
**Executable verified** feasibility observation (source
`adjacent_full_cycle_badmask_atomic_batch.py`, hash `e43ba1ae...`; no
mathematical verdict). This rules out eager complete
descriptor materialization as the next computation. Per-state restricted-root
class interning and sampled descriptor construction are required before any
atlas run.

After exact admissibility filtering, the live quotient is much smaller than
the rectangular ceiling: 28023 left plus 27699 right kernels. A bounded run of
`adjacent_full_cycle_badmask_atomic_batch.py` on eight stratified kernels per
orientation passes with no escape (payload `a85c5a3e...`) and reproduces under
`PYTHONHASHSEED=12345`. **Executable verified** (bounded) from one
producer; it does not replay the banked legacy prefix because this receipt was
run with `--legacy-prefix 0`, and it is not exhaustive.

The safe per-state representation census is now complete on 12
deterministically spread shared states in both orientations. Exhaustive
old-lattice enumeration finds 1566640 genuine atomic extensions and 1433764
strict non-set-union horns; their roles cover 18675 of 18676 old events. The
448200 per-state/orientation trace words compress to 2740 exact restricted-root
classes, 74--136 per sampled state/orientation (aggregate ratio 163.58).
**Executable verified** by one producer under two hash seeds, payload
`d8290f39...`; no independent verifier. This is not a bound on global
224-state trace vectors. The theoretical packed-root tally is 309552 bytes,
not measured process memory.

Hostile review refuted the initial atom-support-only overshoot test: join
`(P,a,J)=(1,18451,18431)` agrees on every atom-support macrofibre but differs
on 432 off-support macrofibres. The corrected producer checks all 842 macros,
uses the correct `a <= P` principal-upset direction, and asserts this regression.
The invalid earlier receipt was overwritten. **Refuted** optimization;
**Executable verified** corrected census.

The first cache-evicted grouped streaming differential now covers every
admissible `U` for 127 selected retained events in each orientation: 551 left
plus 682 right kernels. Grouped simultaneous-mask folds agree exactly with a
scalar replay on all 1233 kernels, and no atomic escape occurs. **Executable
verified** (bounded, single producer), payload `c8587f5b...`; canonical JSON
agrees under hash seeds 0 and 12345. This is 2.21 percent of the 55722 live
kernel quotient, not an exhaustive theorem.

The first read-only assigned-containment oracle was **Refuted** because it
used terminal-false shortcuts before eliminating the assigned coordinate. The
corrected oracle matches 128 deterministic exact residual tests and four
targeted former-bug cases. The measured streaming phase leaves the aggregate
MDD node/application/negation-cache snapshot exactly unchanged at
`(795720,937618,40604)`. It makes 15277539 assigned comparisons and 6471560
recursive-node visits; peak live groups are 56 and peak per-`A` bad caches are
188/159. Thus memory is flat under eviction, while containment runtime is the
current scaling risk.

The abstract fold implication is now **Lean certified** in
`QuerySystem/FiniteAtomFoldKernel.lean`. Theorems `foldl_sup_le`,
`fold_good_iff_exists_greatest`, and `exists_strict_escaping_extension` compile
without `sorryAx`. Their `#print axioms` outputs are `[propext]`, `[propext]`,
and `[propext, Classical.choice, Quot.sound]`. The atomistic-cover hypothesis
remains explicit: Lean does not prove finite-OML atomisticity or concrete
bad-mask eligibility completeness in this file.

### 10.2 Strategic decision-boundary audit

- **New structural pattern?** Yes: conservative assembly is controlled by the
  deflationary trace kernel, and its failures have strict atomic-extension
  horn certificates.
- **Genuinely new stage?** The 1000-retained-event scale sample introduces no
  new transition type, cache peak, or failure beyond the bounded checkpoint.
  The atom/horn reduction is theorem-new and changes the search space.
- **Finite grammar rule?** Candidate rule: eligibility ideals must be closed
  under every strict atomic extension. Coverage is **Hand proved**; closure
  for the current grammar is **Open**.
- **Well-founded invariant?** The incremental old join is monotone; its first
  escape from the trace core is permanent and certifies failure.
- **Collapse unavoidable?** No evidence yet. The bounded and scale samples
  pass, but neither exhausts the 55722 live kernels.
- **Infinite coherent grammar evidence?** None: only the two-copy first layer
  is under test.
- **Would deeper brute branching discriminate?** A complete scan would decide
  the first round, but the current oracle grows to 52602242 assigned
  comparisons for only 1640 scale kernels. Sparse containment-pair interning
  is required before exhaustion.

| Gate | Current status | Evidence | Remaining obligation |
|---|---|---|---|
| Repair grammar | OR/AND tags plus kernel horns | Hand + bounded executable streaming | compress containment pairs, then close atomic-horn atlas |
| Latticehood | Open for adjacent closure | none | construct/verify mixed extrema |
| Orthomodularity | Conditional on set-lattice closure | Hand lemma | prove latticehood |
| Same-side boundary preservation | Open in assembly | single-copy executable | audit mixed closure |
| Activation-event avoidance | Open in assembly | single-copy executable | audit mixed closure |
| Trivial centre | Open in assembly | single-copy executable | classify mixed commutation |
| State order separation | Open in assembly | factor carrier points | prove completed order reflection |
| `Phi` tameness or obstruction | Open | finite copies tame | build CSS/no-GS assembly |
| Infinite-limit viability | Open | none | coherent kernels and sigma-closure |
| Universal normalization | Open | ODBC reduction only | reduce arbitrary failure to architecture |

The stable order-theoretic implication is **Lean certified** in
`QuerySystem/FullCycleAssemblyKernel.lean`:
`map_sup_of_deflationary_retraction`,
`map_inf_of_inflationary_retraction`, and
`map_inf_of_complement_conjugate_deflationary_retraction`. The last theorem
constructs the upper shadow by complement conjugacy from the lower kernel.
All three `#print axioms` reports are empty. The formalization assumes the
shadow retraction; constructing it for the adjacent mixed grammar remains the
open mathematical gate.

### 10.3 Scale boundary and second-round calculus

A separate scale wrapper tests 500 endpoint-spread retained events per
orientation and all their admissible masks: 827 left plus 813 right kernels,
with grouped/scalar assertions passing and no escape. Peak group/cache sizes
remain unchanged and the measured MDD snapshots remain equal. **Executable
verified** as a bounded seed-0 producer observation, payload `9b1277f7...`.
The producer is `adjacent_full_cycle_streaming_atomic_scale.py`, wrapper hash
`1f6dbc98...`, importing engine `c6ff8065...`; the banked evidence command is
explicitly pinned to `PYTHONHASHSEED=0`, with no independent verifier.
The seed-12345 execution passed all mathematical assertions but failed whole-
receipt equality; its differing payload was not retained, so deterministic
receipt reproduction is **Open** and the scale artifact carries this caveat.

The run makes 52602242 assigned comparisons for only 1640 kernels. It adds no
new transition type, cache peak, collapse or failure. A full 55722-kernel scan
remains mathematically decisive, but this representation has reached
computational stop signal E. The next representation test interns only
restricted-root class pairs actually queried by `bad_A(D)` and differentially
reproduces the old oracle. Exhaustion resumes only if that sparse quotient
materially compresses comparisons.

For an old concrete lattice `A`, call a set `c` kernel-good when it has a
greatest old lower `kappa(c)`.

1. If `c,d` are kernel-good, then `c intersection d` is kernel-good with
   kernel `kappa(c) meet_A kappa(d)`. **Hand proved.**
2. The complement of arbitrary `c` is kernel-good exactly when `c` has a least
   old upper `lambda(c)`; its kernel is `lambda(c)`-complement. **Hand proved.**
3. In a finite atomistic old OML, for disjoint kernel-good `c,d`, join their
   kernels with every old bridge atom contained in the union but in neither
   operand. The union is kernel-good exactly when this old join remains inside
   the union; then it is the kernel. **Hand proved.**

Automatic complement and union preservation are **Refuted** by the concrete
four-point `MO2={0,1,01,23,02,13}`: `{2}` has kernel zero but its complement
has incomparable maximal lowers `01,13`; `{2}` and `{0,3}` have kernel zero
while their union has incomparable maximal lowers `02,23`. Thus even an
exhaustive first-round pass would not by itself prove closure. The second round
must classify canonical OR/AND children and bridge atoms; generated latticehood
remains a separate internal-intersection obligation.

The abstract stable portion is **Lean certified** in
`QuerySystem/KernelClosureCalculus.lean`. `greatest_intersection` has no axioms;
the complement-duality, intersection-cover-fold, and generic bridge-union-fold
theorems each report `[propext]`, with no `sorryAx`. The union wrapper keeps
base-join eligibility, bridge eligibility, and full atomistic coverage as
explicit hypotheses. It does not formalize the concrete bridge classification
or disjointness proof; those remain the hand-proved instantiation layer.

### 10.4 Sparse containment-pair boundary

The nominal 55722-kernel quotient contains a large exact tautological family.
For every retained event `A`, the empty mask `U=empty` is admissible, witnessed
by the opposite zero event, and its mixed core is exactly `A`. Its greatest old
lower is therefore `A` without any trace query. Hence 18676 kernels in each
orientation, 37352 total, discharge algebraically. The nontrivial first-round
target is 9347 left plus 9023 right, or 18370 kernels. **Hand proved.**

The deterministic sparse-pair census samples 64 endpoint-spread retained
events per orientation. All 355 sampled kernels pass; for all 11951 queried
bad masks the compressed immutable-DAG containment oracle agrees exactly with
the direct original-MDD oracle. It performs 6865615 short-circuit macro-
occurrence comparisons, 1764641 whole-state class-pair lookups, and 442834
distinct class-pair queries. **Executable verified** (bounded, single
producer), payload `b06e5ff0...`, producer SHA-256 `76796ae4...`; canonical
seed-0 and seed-12345 verification both pass. The artifact is
`adjacent_full_cycle_sparse_containment_pairs.py/.json`.

The orientation-global Python pair cache projects to 69508722 pairs on an
unpruned linear extrapolation. This is a negative result only for that
implemented cache: the sample includes 128 empty-mask tautologies, and it does
not rule out per-`A` eviction, algebraic discharge, or a different global
representation. The next bounded falsifier selects join-rich retained events,
discharges empty masks before tracing, and evicts containment tables per `A`.

### 10.5 Decision-boundary check

- **New structural pattern?** Yes: the empty-mask half of the quotient is
  tautological; no new mathematical escape pattern appears in the sparse run.
- **Genuinely new stage?** The oracle representation is new and differentially
  exact on its queried domain; the kernel verdict remains a bounded repetition.
- **Finite grammar rule?** Empty-mask discharge is an exact grammar rule.
  Arbitrary nonempty masks remain open.
- **Well-founded invariant?** Kernel count decreases from 55722 to 18370 after
  algebraic normalization; no further rank is proved.
- **Collapse unavoidable?** Not shown.
- **Infinite coherent grammar evidence?** None beyond the two-copy first layer.
- **Would more blind branching discriminate?** No. Join-rich per-`A` sampling
  is the smallest remaining representation test before an exhaustive shard
  decision.

### 10.6 Join-rich per-`A` gate

The deterministic top-128 retained events per orientation, ranked by the
product of nonempty admissible-mask count and distinct proper atomic-join
target count, test 2509 nonempty kernels. All pass with zero escape. Every one
of 27469 bad-event-pair queries agrees between the immutable compressed DAG
and direct original-MDD oracle. Peak per-`A` distinct class-pair counts are
13420 left and 12943 right. **Executable verified** (bounded, single
producer), payload `b47a55f8...`, producer SHA-256 `91de6c80...`; seeds 0 and
12345 agree and hostile review passes.

The representation gate supports a checkpointed exhaustive scan of all 18370
nonempty kernels. The roughly 101-minute serial figure is only conservative
stress planning from a deliberately join-rich sample, not a theorem or
expected runtime. First-round success would still leave complement/bridge
closure and generated latticehood open.

### 10.7 Bounded coordinate-child bridge census

Using six exact coordinate leaves per orientation, the bounded second-round
census generates `And`, `Neg`, and exact-disjoint `OrthoOr` children with
canonical physical-root provenance. All 21 `And` pairs per orientation have
kernel exactly the old meet, as predicted by the Lean-certified intersection
calculus.

The other tested operators do not close automatically. Only 6/10 left and
9/14 right complement targets are kernel-good. Of the exact-disjoint child
pairs whose goodness is either checked here or inherited from the committed
join-rich leaf receipt, 37/42 left and 66/73 right bridge folds remain inside
their physical unions. The first strict failure in the canonical atom
enumeration starts with an eligible old base join and eight bridge atoms; its
first enumerated bridge extension forces the old fold outside the union. Three
right-orientation coarse-shadow classes realize two different bridge
signatures. **Executable verified** (bounded, single
producer), payload `3fbf81c2...`, producer `b4894f4e...`; seed-0 and
seed-12345 whole-payload replay pass.

The tested operator alphabet is `{Leaf, And, Neg, OrthoOr}`, and `And` is
theorem-closed. Automatic complement/union closure fails, and coarse shadows
do not determine bridge signatures. This refutes a shadow-only grammar that
must carry bridge provenance, but does not by itself refute every shadow-level
kernel-verdict grammar. Exact physical roots and bridge provenance are
load-bearing for the present calculus. Alphabet completeness, full mixed
closure, and arbitrary-depth finiteness remain **Open**.

There is a sharper fixed-base consequence. Let `u` be any strict target whose
old contained atoms have old join `j` with `j` not contained in `u`, and let
`e0` be their set union. Every set `m` with `e0 subseteq m subseteq u` has the
same contained old atoms, hence the same escaping old join, so `m` is not
kernel-good over the old lattice. Any extension in which `u` acquires a new
greatest lower must place that lower in this interval. Therefore no adjunction
can repair the strict target while keeping the inclusion into the extension a
kernel retraction over the same old base. **Hand proved.** Re-basing may still
repair latticehood, but it abandons the conservative-embedding invariant.

The abstract exhaustive-fold obstruction and its transfer across extensionally
identical eligible-old predicates are **Lean certified** as
`no_greatest_of_exhaustive_fold_not_good` and
`no_greatest_of_same_eligible_old_set` in `KernelClosureCalculus.lean`.
Both report `[propext]` and no `sorryAx`; the concrete atom-saturation interval
identification remains the hand-proved instantiation.

### 10.8 Order-independent phantom-bridge audit

The 12 bounded strict `OrthoOr` failures contain 197 bridge atoms. Testing each
atom singly against its fixed base join gives 182 escapes. The canonical
eight-bridge failure is order-robust: all eight atoms individually escape,
have old descriptor `full17=0`, and land at old top.

That shape is not universal. Of the 182 escaping atoms, 181 have `full17=0`
and 176 land at top. One nonphantom atom (`full17=0x3000`) lands at a subtop,
and five further phantom atoms also land subtop. Thus a uniform
phantom-to-top repair law is **Refuted**. Here “phantom” means only zero
`full17` descriptor, not absence on every physical fibre.

For every failed target, the literal physical union `e0` of all contained old
atoms has an old-lattice fold escaping the target, verifying its fixed-base
kernel obstruction. But `e0` is proper in only 6/12 failures and equals the
target in the other 6/12. Universal strict saturation is therefore
**Refuted**. **Executable verified** (bounded, single producer), payload
`174fe4c5...`, producer `5861b75d...`; seed-0 and seed-12345 replay pass.

The next grammar state must at least record saturation equality, phantom
status, and top/subtop landing. These bounded types are not yet proved
complete for the full mixed closure.

### 10.9 Exhaustive first-round theorem

The canonical rank-mod-32 manifest contains exactly 4719 retained events in
each orientation and partitions all nonempty admissible masks into 9347 left
and 9023 right kernels. All 32 shards pass: 18370/18370 nonempty kernels have
greatest old lower shadows, with zero failure certificates and unchanged MDD
snapshots. The empty mask is admissible for every retained event and has
kernel equal to that event, contributing 37352 further kernels. Hence all
55722 first-round kernels pass.

**Evidence:** the nonempty census is **Executable verified**, the empty-mask
discharge is **Hand proved**, and the fold implication is **Lean certified**.
Master payload `bf3f7d29...`; manifest `423d6224...`; independent semantic
classification verifier `ff6cbeba...`. Hostile review recomputes every shard
hash, exact coverage, aggregate counter and chained digest. Shards 0 and 31
also reproduce under seed 12345.

**Theorem of record.** For either adjacent orientation, every retained old
event `A` and every admissible universal mask `U` have a greatest eligible old
lower for the first-round mixed core. By complement duality the corresponding
old-upper family has a least member.

This closes only the first-round conservative-shadow problem. It does not
prove complement/disjoint-union closure, generated latticehood, OML,
sigma-closure, MBRC, ODBC, or `Phi`; Sections 10.7--10.8 already give exact
bounded counterexamples to automatic fixed-base continuation.

### 10.10 Universal-shadow correction for later rounds

Let `Omega=X times_S Y` be a nonempty-fibre pullback and, for a relation
`R subseteq Omega`, write

`Forall_Y(R)={x : R_x=Y_s}` and `Exists_Y(R)={x : R_x nonempty}`.

Pointwise fibre calculation gives

- `Forall_Y(R intersection T)=Forall_Y(R) intersection Forall_Y(T)`;
- `Forall_Y(complement R)=X \ Exists_Y(R)`;
- for disjoint `R,T`,
  `Forall_Y(R union T)=Forall_Y(R) union Forall_Y(T) union H(R,T)`,
  where `H(R,T)` is the locus on which two proper disjoint sections jointly
  fill the whole fibre.

These identities are **Hand proved**. Universal shadows therefore commute
with intersection, but not generally with complement or disjoint union.
Complement transfers exactly when every section is empty or full. Disjoint
union transfers exactly when there is no complementary-partial-cover fibre.

For a first-round mixed leaf
`Z=pi_X^{-1}(A) union pi_Y^{-1}(B)`, the prior target is exact:

`Forall_Y(Z)=A union cylinder(U_B)`,

where `U_B` is the shared-state set on which the `B`-section is full.
Therefore the exhaustive first-round theorem remains unchanged.

The bounded second/third-round producer deliberately applies `Neg` and
`OrthoOr` to these one-coordinate targets. It does not recompute
`Forall_Y` after applying those operations to the actual two-copy relations.
Its 12 strict failures therefore refute automatic Boolean closure of the
coordinate-target calculus only. They are fixed-target obstruction controls,
but are not generated-event obstructions for the adjacent assembly. The
earlier re-based-repair interpretation is **Refuted** at that stronger scope.

The conditional obstruction remains exact: if an actual generated event `u`
has the certified old-below predicate and its eligible old atom fold escapes,
then the affected old copy cannot retain its old joins in any extension
containing `u`. This is **Hand proved**; the binary and finite-fold
escaping-upper-bound forms are **Lean certified** in
`KernelClosureCalculus.lean`.

The next exact grammar must retain canonical restricted relation-section roots
in every shared-state fibre, apply Boolean operations there, and only then
recompute universal shadows and old atom folds. The pair
`(Forall_Y(R),Exists_Y(R))` is insufficient: distinct proper sections can have
the same pair and different intersection or complementary-cover behaviour.

### 10.11 Bounded actual-relation discriminator

The corrected producer represents six canonical mixed leaves per orientation
as actual Boolean relations on the shared-state fibre product. It enumerates
the exact simultaneous truth patterns in each shared-state fibre, forms
Boolean terms on their Cartesian pattern product, universally quantifies the
opposite pattern, and composes the result back into an exact old-copy MDD.

Across 156 generated occurrences (72 left, 84 right), every actual universal
shadow has a greatest old lower. The coordinate-target calculus reports 22 bad
occurrences on the same generation. There are 55 unequal shadows: 20 `Neg`
and 35 `OrthoOr`; every `Leaf` and `And` shadow agrees exactly. Thus all 12
earlier strict `OrthoOr` coordinate failures disappear after actual relation
evaluation, as do the additional coordinate-complement failures.

**Executable verified** at bounded canonical-witness scope, payload
`3d6f97c8...`, producer `03601b2b...`. A seed-12345 recomputation returns the
same mathematical payload. The receipt binds retained/opposite roots,
existential/universal masks, fibre-product pattern vectors, semantic
signatures, parent provenance, universal-shadow tables and eligible old-atom
digests. Hostile source audit validates the quotient construction; there is no
independent producer.

The counts are separated deliberately: `Leaf/And` records are distinct
relation-signature classes, while `Neg/OrthoOr` totals are generated
occurrences (13/46 left and 14/56 right). The latter realize 13/34 and 14/41
distinct semantic signatures respectively.

This is positive evidence for coherent adjacent assembly, not an arbitrary-
depth theorem. Each `(A,U)` uses one canonical minimum-index witness from an
inclusion-minimal opposite existential class. Other witnesses with the same
coarse `(E,U)` may have different proper sections. The next discriminating
test varies exact opposite witnesses within fixed shadow classes; adding more
Boolean depth to one canonical quotient is lower value.

### 10.12 Exact section-context type

Fix one opposite fibre and let `K` be the Boolean algebra generated by all
fixed section constants available to a unary term context. For a candidate
section `b`, define

`Low_K(b)={k in K:k subseteq b}` and
`Up_K(b)={k in K:b subseteq k}`.

Every unary Boolean polynomial over `K` has normal form

`p(b)=(b intersection c) union (complement b intersection d)`

for `c,d in K`, and `p(b)=1` exactly when
`complement d subseteq b subseteq c`. Therefore two sections have identical
universal outcomes in every unary Boolean context over `K` iff their
`(Low_K,Up_K)` cut pairs agree. **Hand proved.**

Equal coarse `(E,U)` is not sufficient. On a two-point fibre, with fixed
constant `D={1}`, the proper nonempty sections `B={1}` and `B'={2}` have the
same `(E,U)`, but `B union D` is proper while `B' union D` is universal.
Thus the `(E,U)` witness quotient is **Refuted** for arbitrary continuation.

The unary cut quotient is finite, but it is not generally a congruence for
combining two dynamic witnesses. With constants only `{0,1}`, all proper
nonempty sections have one unary type, although unions of two representatives
can be proper or universal. A full term grammar must use the joint Boolean-
context congruence, equivalently the exact element of the Boolean section
algebra generated by all live section generators (or a proved quotient of
it).

The exact induction obligation is now:

1. choose a finite section algebra or quotient in every shared-state fibre;
2. prove the equivalence is a congruence for complement, intersection and
   union;
3. give well-defined transition tables for those operations;
4. prove the universal-output predicate is class-invariant;
5. map every generator occurrence to its class and induct on terms;
6. preserve orientation, fibre identity and attainable retained-side truth
   profiles.

The restricted-MDD section-root vector used in Section 10.11 is a valid
nonminimal congruence state for the fixed finite carrier. The next compression
problem is minimization/bisimulation of this finite Boolean transition
algebra, not another `(E,U)` aggregation.

### 10.13 Finite quotient coverage theorem

Let a finite state set `S` be a surjective quotient of the Boolean algebra
generated by a fixed section-generator family. If the quotient preserves
complement, intersection and union and its universal predicate detects exactly
the top section, then evaluation of every Boolean term commutes with the
quotient and its universal verdict is exact. **Hand proved** by structural
induction.

Associativity, commutativity, absorption, distributivity, complement laws and
evaluation-order independence transfer from the source Boolean algebra; they
need not be postulated separately once the quotient is a surjective Boolean
homomorphism. For a table certificate, these laws and transition totality can
instead be exhaustively checked on `S`.

This does not yet prove adjacent-pair closure. The additional exact section-
factorization theorem must show:

1. every generated relation section lies in the certified fibre algebra;
2. the full occurrence-indexed class vector determines the physical relation;
3. every reachable class has certified left/right old lower and upper shadows;
4. every exact disjoint-union bridge locus is covered by its atom fold;
5. an internal-cut theorem supplies all generated meets and joins.

Items 1--4 would give coherent conservative old-copy embeddings for the
Boolean term family. Item 5, plus separate block and state audits, is still
needed for generated latticehood and OML.

### 10.14 No global exact-universal congruence compression

Let `theta` be a Boolean-algebra congruence whose top class is the singleton
`{1}`. Then `theta` is equality. If `a theta b`, symmetric difference gives
`a triangle b theta 0`; complement gives
`complement(a triangle b) theta 1`; the singleton top class forces
`a triangle b=0`, hence `a=b`. **Hand proved**, without finiteness or
concreteness.

The fixed six-leaf section systems instantiate this theorem. In each
orientation the realized mixed words form nine Boolean atoms, hence generate
a 512-element section algebra. The executable pilot reconstructs 375 left and
416 right section occurrences, with 10 and 11 distinct realized sections, and
certifies that all 14 witness divergences have explicit Boolean contexts
distinguishing their universal output. Witness variants can enlarge the atom
alphabet to 10 or 11. **Executable verified — sampled finite scope**, payload
`2ebe78a9...`; hostile review passes.

Thus exact universal-output Myhill--Nerode minimization is a dead route: the
exact section element is already minimal under full Boolean contexts. The
one-step refinement count in the receipt is only a proof-step implementation,
not a canonical partition-refinement invariant.

The live compression question is weaker: do exact old lower/upper kernel
outcomes admit a typed transition congruence? If not, the grammar must be
parametric in symbolic exact-root/word generators rather than a fixed finite
reduced alphabet.
