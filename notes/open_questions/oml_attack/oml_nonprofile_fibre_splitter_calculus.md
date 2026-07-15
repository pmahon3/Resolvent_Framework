# Non-profile fibre-splitter calculus

*Campaign 19 theorem-extraction continuation, 2026-07-15. Exact escape from
coordinate-closed reconstruction.*

## 1. Fibre hulls

Let `pi : Omega -> {0,1}^4` be the full-grid coordinate-profile map. For an
arbitrary subset `e` define

\[
 \operatorname{int}_\pi(e)=\bigcup\{F:F\text{ is a }\pi\text{-fibre},F\subseteq e\},
 \qquad
 \operatorname{sat}_\pi(e)=\bigcup\{F:F\cap e\ne\varnothing\}.
\]

These are subsets of the carrier, not automatically events.

For the displayed crossed pair

\[
 x=\{q_0=0,r_1=1\},\qquad y=\{q_1=1,r_0=0\},
\]

write `M=x union y` and let `W` be the intersection of all current upper
bounds. The exact extrema certificate gives

\[
 W\setminus M=A\mathbin{\dot\cup}B,
 \quad A=\pi^{-1}(0110),\quad B=\pi^{-1}(1001).
\]

Hence every join `j` of this pair in any same-carrier concrete extension has
the unique set normal form

\[
 j=M\mathbin{\dot\cup}S_A\mathbin{\dot\cup}S_B,
 \qquad S_A\subseteq A,\quad S_B\subseteq B.
\]

Its fibre interior contains an ambiguous fibre exactly when the corresponding
`S` is full, while its fibre saturation contains that fibre exactly when the
corresponding `S` is nonempty. **Hand proved.** The displayed extrema are
separately **Executable verified** by the full-grid certificate.

## 2. Necessary splitter theorem

**Theorem 2.1.** Every same-carrier concrete OML completion preserving both
distributed same-side boundaries has some profile-measurable failed pair
whose join properly splits at least one ambiguous profile fibre.

Otherwise every such join would be profile-measurable. The
coordinate-closed completion theorem would then descend the completion to
the exhaustive `P(16)` core and force a same-side Boolean reconstruction.
Thus the minimal escape is a binary colouring `empty != S != F` of a profile
fibre, retained by an event and its complement. **Hand proved.** The finite
core covering premise is separately **Executable verified**.

The verified 256-, 492-, and 558-event nonlattice stages demonstrate that
such splitters can survive complement/disjoint-union closure without
immediate reconstruction or activation support. They do not demonstrate a
terminal OML. **Executable verified** for exactly the stated stages.

## 3. Conditional hull extraction and correction

**Lemma 3.1.** Suppose both `int_pi(j)` and `sat_pi(j)` are events and exactly
one of `A,B` is properly split by `j`. Then their nested event difference is
that entire ambiguous profile fibre.

Indeed, nested differences exist in every complement/disjoint-union-closed
family:

\[
 v\setminus u=(u\cup v^c)^c\qquad(u\subseteq v).
\]

If both ambiguous fibres are properly split, the hull difference is `A union
B`; this argument does not separate the two. **Hand proved** under the
displayed hull and one-split-fibre hypotheses.

The formerly asserted next implication was false and is retracted: a whole
four-coordinate profile fibre is not a same-side literal macro cylinder.
The latter fixes only `q0,q1` and contains four profile fibres. On the
stripped core, adjoining any one profile singleton to the 82-word edge core
closes to 204 words and produces no nontrivial same-side-measurable word.
Thus Lemma 3.1 is an extraction lemma, not a boundary-reconstruction lemma.
**Executable verified** for all sixteen singleton profiles by the existing
independent word-closure audit
`notes/open_questions/verification/core16_single_profile_noncollapse.py`,
payload
`a85c5b89b0ceb5a1d0aa09cf6ca25ad1ac0e4fe3b7a060aa3eb1466ad0305415`.
Whether further lattice cuts from an
extracted profile fibre eventually force a side boundary is **Open**.

The hull hypotheses are substantial. Fibre interiors and saturations need
not be events; the trace family on a fibre need not inherit global lattice
extrema; point-state order separation imposes no fibre invariance; and a
fibre permutation need not preserve the completed lattice. No unconditional
saturation theorem follows from concreteness or orthomodularity alone, and
even their availability may yield only a four-coordinate fibre event.

## 4. Surviving architecture and next test

The surviving escape is an overlapping family of nontrivial partitions of
ambiguous fibres such that:

- the relevant fibre interiors and saturations remain unavailable;
- complements retain every split;
- differences of globally nested repair events never isolate a whole profile
  fibre;
- overlapping crossed joins glue consistently without reconstructing a
  same-side Boolean algebra;
- the completed family becomes a lattice without an activation-supported
  event.

The next falsifiable computation is the splitter-incidence graph of the
558-event branch: for each crossed-cut orbit representative, record the
ambiguous fibres it splits, whether either hull is already an event, and
whether two repair hulls are globally nested or orthogonal so that a
difference isolates a whole fibre. A positive isolation closes that branch;
a negative census supplies the first explicit compatible splitter graph.

## 5. Exact symmetry quotient

Let `G` be the group of carrier permutations preserving the 230-event base
family and the two gate families setwise. `G` acts on the unrestricted repair
tree, commutes with closure and admissible intervals, and preserves T-FIN.
Quotienting complete event families by `G` therefore gives a finite rooted
DAG whose terminal orbits decide T-FIN. The complete invariant is the
canonical coloured incidence/operation structure of the entire event
family, not its next gap.

Because the base events separate carrier points, `G` is equivalently the
automorphism group of the realized 230-coordinate point-signature code with
complement, disjoint-union, and gate colours. Named grid/cell symmetries give
only a subgroup until equality is executable-certified. The group-action and
quotient claims are **Hand proved**. Computational tractability is **Open**.

## 6. Stage-558 hull checkpoint

The discriminating census stops before a fourth repair. In the exact
558-event family there are 90 profile-measurable events and 127 unordered
join-failing pairs among those 90 events. This is not a census of every
lattice failure, meet failure, or symmetry orbit.

All three selected joins remain least at the final stage. The first has
neither fibre hull as an event. The second has its fibre interior but not its
saturation. The third has its interior, saturation, and hull difference as
events, while the whole join properly splits twelve profile fibres. Much of
that twelve-fibre pattern is inherited through its forced lower bound; the
two-point repair increment must be recorded separately.

Thus availability of both hulls does not by itself cause immediate
reconstruction: their difference may be a union of many whole profile fibres
rather than one literal macro cylinder. This does not refute Lemma 3.1,
whose one-split-fibre hypothesis fails, and it proves nothing about terminal
OMLs. It changes the next invariant from individual hull availability to
incidence among several hull gaps: nested or compatible differences must
progressively isolate one fibre.

**Executable verified:**
`notes/open_questions/verification/full_grid_stage558_splitter_incidence.py`
on the single certified 558-event branch; payload
`6b12e4a9ea7bafd4abc67e08dbc9a53ec6cd01487056f548d17e8f65a8aa39f5`.
The computation reuses the banked
carrier construction and is not an independent implementation.

**Hand proved:** the finite-family criterion used by the census: a pair has
a join exactly when the set intersection of all its current upper bounds is
itself an event.

**Open:** whether overlapping hull gaps in any terminal necessarily isolate
a same-side macro fibre or activation subset.

An independent implementation sharpens this checkpoint. Across all 558
events it finds seventeen distinct split-fibre signatures with 81
nonlaminar pairs. Exactly nine distinct nonempty hull gaps are themselves
events; one is the whole carrier. Among their 36 unordered pairs, exactly
eight are nested, every resulting event difference contains four whole
profile fibres, and no pair has one-fibre symmetric difference. No whole
profile fibre is an event, and no nonzero event is contained in a single
profile fibre. Thus laminar refinement and one-fibre hull isolation are both
refuted as stage invariants. **Executable verified** on this one nonlattice
stage by the partially independent audit
`notes/open_questions/verification/full_grid_stage558_hull_gap_isolation_audit.py`,
payload
`eeb79b8531ab80e44d8a8a091f8d2683d319b0526d944c4840af1acf3e644d62`.
The audit independently implements closure, order tables, failure and hull
censuses, but shares the defining carrier constructor and the three selected
repair descriptions.

The companion audit
`notes/open_questions/verification/full_grid_stage558_meet_witness_audit.py`
(payload
`4cd553be1d4cd5187c4afb36fc340a9bd573b147651bd5507897611a1446a55d`)
exposes a more informative provenance object. The sole
nonzero same-side literal-pair lattice meet at this stage is

\[
 q_0^\perp\wedge_L q_1,
\]

an event of 336,404 points equal to the entire 336,400-point `0101` profile
fibre disjoint-unioned with the four-point second repair selector. It is not
the literal set intersection of the two coordinates. It has four activated
row-0 points and many off-activation points, so neither reconstruction nor
gate `B` follows. This refutes the stage-level implication “nonzero
same-side literal meet implies its literal macro cylinder is an event.”
**Executable verified** on the exact 558-event stage. Persistence of this
exact equality in a terminal extension is **Open**, but its event core is
irreversible: in every extension, any new meet of the same two coordinates
must contain the old meet because the old event remains a lower bound.
**Hand proved.**

The next T-FIN object is therefore a *fattened-fibre meet*: a lattice meet
consisting of a whole profile fibre plus a finite repair escape. The
discriminating interval is above this meet and below the literal set
intersection (dually below the corresponding same-side join): classify
whether every terminal repair fills the four-fibre same-side cylinder or
stabilizes at a larger fattened-fibre meet. Killing or shrinking the meet is
impossible.

For this witness the literal same-side intersection has 1,355,680 points,
so the irreversible enlargement gap has 1,019,276 points. It consists of the
remaining 341,436 points of profile `0100` after removing the four-point
selector, together with the whole `0110` and `0111` fibres of 336,400 and
341,440 points. Every meet in a terminal extension lies set-theoretically in

\[
 e_*\ \subseteq\ q_0^\perp\wedge_{L_{\rm terminal}}q_1
 \ \subseteq\ \{q_0=0,q_1=1\}.
\]

This is a genuine provenance-sensitive monotone interval, but its raw
`2^1019276` subset space is another computational stop signal. Any next
computation must quotient candidate enlargements by a stated trace/provenance
rule rather than enumerate them.

**Theorem 6.1 (fattened-meet bifurcation).** In every same-carrier terminal
OML extending the 558-event family, either this meet equals the full
four-fibre cylinder `{q0=0,q1=1}`, in which case one same-side literal macro
atom is an event and the same-side forcing lemma reconstructs
`Bool(q0,q1)`; or the terminal contains a proper fattened-fibre meet `m`
satisfying

\[
 e_*\subseteq m\subsetneq\{q_0=0,q_1=1\}.
\]

**Hand proved.** This is an exact terminal bifurcation, but its second branch
is realizability architecture rather than a counterexample: latticehood,
the other same-side meets, centre, and later assembly gates remain **Open**.

## 7. Exact macrofibre interval normal form

The enlargement gap in Theorem 6.1 has a useful but sharply limited finite
coordinate description. Relative to the activation/local-state macrofibres
used by the full-grid producer, it is the disjoint union of exactly 160 whole
macrofibres and contains no partial macrofibre. Their four-coordinate profile
counts are

\[
 55\text{ in }0100,\qquad 49\text{ in }0110,\qquad
 56\text{ in }0111.
\]

The gap has 1,019,276 points and the smallest constituent macrofibre has four
points. **Executable verified** by
`notes/open_questions/verification/full_grid_stage558_fattened_meet_gap.py`
on the single exact stage-558 interval, payload
`a9fac75913dbd5d35cdfe6ff0f28357da41ecd84e56180fc32bdaf51f4f11264`.
The verifier reconstructs the 558-event stage and recomputes the factor
decomposition, but it reuses the banked carrier/stage and factor-projection
modules and is therefore not an independent implementation.

**Lemma 7.1 (stage-558 macro-saturated candidates).** Let
`M_1,...,M_160` be those disjoint macrofibres. Every candidate enlargement
of `e_*` inside its literal cylinder which is saturated for this particular
macrofibre partition has the unique form

\[
 e_*\ \mathbin{\dot\cup}\!\bigcup_{i\in S}M_i,
 \qquad S\subseteq\{1,\ldots,160\}.
\]

Conversely every such expression is a set lying in the literal interval.
**Hand proved** from disjointness and exhaustion of the verified partition.
Eventhood, admissibility as a lattice meet, and preservation of the two gates
are not asserted.

This supplies an exact 160-bit grammar for one *macrofibre-saturated
interval*, not a repair grammar for future stages. Whether every terminal
meet is saturated for this partition is **Open**. Later non-profile repairs
may cut a macrofibre, and neither complement/disjoint-union closure nor the
current provenance calculus has been proved to exclude that possibility.
Accordingly arbitrary branching over `2^160` subsets is also suspended: a
next computation is discriminating only if it classifies partial splitters
or quotients the 160 bits by a proved gate-preserving provenance action.

The activation categories of the 160 pieces are exact: 147 lie off both row
activation cylinders, six lie only in row 0's activated cylinder, seven lie
only in row 1's, and none lie in both. For any realized candidate meet, its
remainder above `e_*` is an event by nested difference. A nonempty saturated
remainder then fires gate B exactly when all its selected pieces lie among
the six row-0 pieces or all lie among the seven row-1 pieces. There are

\[
 (2^6-1)+(2^7-1)=190
\]

such nonzero remainders. Gate A adds only the all-160 choice. Thus
`2^160-191` saturated candidates avoid both gates when the unchanged meet is
included, and `2^160-192` proper saturated enlargements avoid both gates.
**Hand proved** from the disjoint activation partition; the 6/7/147/0 census
is **Executable verified** by the same shared-builder receipt. Gate checks
alone therefore do not materially compress even the conditional saturated
search.

### 7.1 Named provenance stabilizer

The exact named semantic group generated by row and column swaps, simultaneous
`q/r` complement, and independent rowwise `a1/a2` arm swaps has order 32 and
acts faithfully on the macro descriptors. Stabilizing the three chosen repair
markers, `C`, the two components of `e_*`, and the enlargement pieces leaves
the order-four group generated by the two row-arm swaps. It has 84 orbits on
the 160 pieces: 32 singleton, 40 size-two, and 12 size-four orbits.
**Executable verified** by
`notes/open_questions/verification/full_grid_stage558_named_stabilizer.py`,
payload
`90034307105591ccb92801b57d2d922e97bcd59d0701b1abbd93d000e18a2c72`.
The script verifies the named atom permutations on all 224 cell states and
the stated descriptor action; it is not an independent construction of the
carrier.

This is not the full automorphism group of the 6,186,568-point set system.
Equality of the named subgroup with the full gate/provenance-preserving
stabilizer is **Open**; hidden permutations inside local-state fibres are the
first suspected failure. Moreover 84 orbits do not mean that arbitrary
candidates use 84 invariant bits: symmetry quotients require canonicalizing
orbits of subsets, while restricting to unions of group orbits would discard
noninvariant candidates. The smallest faithfulness test is the exact coloured
automorphism group of the 224-state/56-event cell incidence code.

That single-cell test is now closed. With `{a1,a2}` preserved setwise and
`a3,q,r` fixed, the exact coloured incidence automorphism group has order two:
identity and the named arm swap. Fixing the third-selector provenance events
`n1,s1` does not shrink it. There is no hidden local-state-fibre automorphism
at cell level under these colours. **Executable verified** by the intrinsic
atom/orthogonality exhaustion
`notes/open_questions/verification/h4_cell_incidence_automorphism.py` and the
independent declared-block verifier
`notes/open_questions/verification/verify_h4_cell_incidence_automorphism.py`,
payload
`7b1223bfcb55de3d7d9178b25cf2cc7727c1be1e0a1be18674fa4fb61bb97eb2`.
The remaining full-grid faithfulness question is intrinsic recognizability:
must every gate/provenance-preserving automorphism of the 558-event family
preserve or named-permute its four embedded 56-event cell subfamilies? This is
**Open**; an emergent global automorphism could still violate the named-group
model.

Burnside's lemma makes the computational conclusion exact. The four named
stabilizer elements have 160, 116, 116, and 96 cycles on the pieces, so their
action on all saturated subsets has

\[
365375409332767267945596527428665083283002884096
\]

orbits. **Executable verified** by the same receipt; the Burnside division is
**Hand proved**. Named symmetry therefore leaves a 48-digit quotient and does
not rescue saturated-subclass enumeration.

The already banked fourth-gap control does not supply that test. Every one
of its 116 nonempty macrofibre intersections has `q0=1` (profiles `1000`,
`1010`, `1100`, or `1110`), whereas every one of the 160 pieces above `e_*`
has `(q0,q1)=(0,1)`. Hence the whole 205,248-point fourth gap—and in
particular its unique four-point minimum selector—is disjoint from the
fattened-meet enlargement interval. **Hand proved** by the coordinate-profile
partition; the two profile classifications are separately **Executable
verified** by `full_grid_third_repair_fourth_gap_audit.py` and
`full_grid_stage558_fattened_meet_gap.py`. Adding that fourth selector might
create later closure interactions, but the selector itself cannot distinguish
macrofibre saturation from partial splitting. Routine extension along it is
therefore stopped.

## 8. Terminal residue architecture

Let `T` be any same-carrier terminal OML extending the full-grid base. For
one side `s in {q,r}`, let `l_{i,e}` be the event saying that coordinate
`s_i` has value `e`, and put

\[
 C_{e f}=l_{0,e}\cap l_{1,f},\qquad
 m_{e f}=l_{0,e}\wedge_T l_{1,f},\qquad
 \rho_{e f}=C_{e f}\setminus m_{e f}.
\]

Only `m_{ef}` is automatically an event; `C_{ef}` and `rho_{ef}` are initially
subsets of the carrier.

**Theorem 8.1 (one-side residue calculus).** For each side:

1. `m_{ef}` is contained in `C_{ef}` and is the set complement of the
   lattice join of the complementary signed literals, by De Morgan.
2. `rho_{ef}` is an event if and only if `C_{ef}` is an event. Thus gate A
   holds on that side if and only if some residue is an event. This includes
   the empty-residue case, since the empty set is an event and then
   `C_{ef}=m_{ef}`.
3. For each fixed row or column of the `2 by 2` residue square, the disjoint
   union of its two residues is an event. The union of all four residues is
   also an event.
4. If gate A is avoided, every residue is nonempty and no singleton or
   three-residue union is an event. Eventhood of one diagonal pair is
   equivalent to eventhood of the complementary diagonal pair, but neither
   is forced or excluded by these identities.

**Hand proved.** For (2), if the cylinder is an event then its nested
difference by `m` is an event; conversely `m dotcup rho=C` is an orthogonal
join. For (3), the two relevant meets are disjoint events below one signed
literal, so subtracting their disjoint union from that literal gives the row
or column residue union. Subtracting all four disjoint meets from `Omega`
gives the total. For (4), a singleton event triggers (2), while an event
triple can be subtracted from the event total to make the complementary
singleton an event. The proof uses concreteness, complement closure, and
orthogonal-union closure; it never forms `C minus m` as an event before
eventhood of `C` has been established.

Applying this to both sides gives eight meet events and eight non-event
residues in every gate-A-avoiding terminal. The stage-558 certificate pins
one of these meets from below by `e_*`; the other seven have no nonzero
stage-level core. Together with the coordinate-closed reconstruction theorem,
every terminal avoiding A and B must additionally contain a join of
profile-measurable events which properly splits some profile fibre. **Hand
proved** over the separately **Executable verified** stripped-core covering
theorem.

The eight meet shadows give a finite *necessary descriptor*: each of the
eight meets has four `pi`-fibre traces, recorded as `empty`, `proper`, or
`full`, for 32 ternary entries. In the order `0100,0101,0110,0111`, the
`q01` meet is pinned `proper-or-full, full, *, *` by `e_*`. This is not yet a
complete finite repair grammar. The descriptor forgets the actual
within-fibre subsets and their provenance; no theorem presently shows that
it determines eventhood, closure, compatibility, later extrema, or even the
existence/gate outcome of a terminal. The nonisomorphic 468/492-event controls
with identical next-gap geometry are **Executable verified** cautionary
evidence against coarse Markov descriptors, not a refutation of this specific
CSP. Completeness of a residue-signature CSP is **Open**.

The narrow missing positive equivalence is residue-shadow lifting: every
finitely consistent assignment of the 32 ternary traces and the two residue
square identities lifts to coherent within-fibre subsets forming a terminal
OML. Its proof would make the finite CSP decisive. The narrower collapse
alternative is a coupled-residue-square theorem: the two residue squares,
the four edge-cell algebras, and one required non-profile join force either a
residue singleton event (gate A) or an activation-supported event (gate B).
Both statements are **Open**; bare line-union identities do not imply either.

### 8.1 Minimal bare residue-square countermodel

The failure of bare residue identities to collapse is exact and minimal. Let
`Omega={00,01,10,11}` and take

\[
 E=\{\varnothing,\Omega,R_0,R_1,C_0,C_1\},
\]

where `R_i` and `C_j` are the two rows and two columns. Ordered by inclusion
with set complement, this is the six-element horizontal sum `MO2`: distinct
noncomplementary line events have lattice meet zero and join one. It is a
concrete complement/disjoint-union-closed orthomodular lattice. Its four
residues are the singleton intersections `R_i cap C_j`, none of which is an
event; all row and column pairs and the total are events, while singleton,
triple, and diagonal residue unions are not.

**Hand proved.** Closure and all extrema follow from the displayed six-set
inclusion order. Minimality is cardinal: four nonempty disjoint residues
require at least four carrier points, and on four points the required line
events give this model up to relabelling. Thus no theorem using only one
residue square's identities can force gate A or B. The next theorem must use
the coupling of both squares through the four edge Boolean algebras and a
non-profile join; profile-measurable coupling alone is already closed by the
exhaustive `P(16)` reconstruction theorem.

### 8.2 Profile-join-hull closure theorem

There is a clean coupling axiom strictly weaker than requiring non-profile
joins themselves to be profile-measurable. For the profile map `pi`, define
the existential fibre hull

\[
 H(z)=\pi^{-1}\{p:z\cap\pi^{-1}(p)\ne\varnothing\}.
\]

**PJH:** for every two `pi`-saturated events `a,b`, the hull
`H(a join_T b)` is an event.

**Theorem 8.2.** Every same-carrier terminal satisfying PJH reconstructs
`Bool(q0,q1)` or `Bool(r0,r1)` and therefore fires gate A. **Hand proved**
over the separately **Executable verified** exhaustive `P(16)` completion
theorem.

Indeed, saturated events are closed under complement and orthogonal union.
For saturated `a,b`, put `z=a join_T b`. The PJH event `H(z)` is saturated,
contains `a,b`, and is contained in every saturated upper bound `u`: leastness
gives `z subseteq u`, and saturation of `u` gives `H(z) subseteq u`. Thus the
saturated events form a complement/disjoint-union-closed lattice, hence a
concrete OML. Quotienting its fibres by `pi` gives an OML subfamily of
`P(16)` containing the four edge Boolean algebras. The exhaustive core theorem
reconstructs one same-side Boolean algebra, whose pulled-back cylinders are
events of `T`.

PJH is **Open** for arbitrary terminals and is false as an automatic
nonterminal closure property: the stage-558 hull audit already contains
joins for which the relevant hull is absent. A gate-A/B-avoiding terminal
must fail PJH on at least one saturated pair. The certificate-local next test
is not another repair depth: replay the finite `P(16)` forcing DAG and, for
each saturated failed pair it uses, determine whether every corresponding
full-grid join has an event-valued existential hull. The first failure is the
exact hull-defect architecture a preserving terminal must sustain.

### 8.3 Finite first-defect atlas

The exhaustive stripped-core search has 48 distinct forcing states: 31
internal nodes and 17 terminal nodes. The internal nodes use only 24 distinct
failed intervals and have 64 candidate hull edges (one four-way root and
thirty binary nodes), with maximum depth six. Every terminal reconstructs a
same-side boundary. **Executable verified** by the receipt extractor
`notes/open_questions/verification/full_grid_core16_pjh_defect_atlas.py`,
payload
`12eefe07a077a8ec64d497d6616e165ffa36de33c987d98e428191093ae0fe6e`.
The verifier independently replays every node family from its first-seen
path, serializes an actual failed witness pair and complete-family hash,
recomputes every upper interval, resolves all 64 child closures including
memo targets, and binds every terminal hash to its reconstruction receipt.
It still takes the banked exhaustive path list as its search coverage input;
it does not independently rediscover that the 48-node list is exhaustive.

**Theorem 8.3 (first-PJH-defect bifurcation).** Let `pi` be the surjective
sixteen-profile map and let `T` be any same-carrier concrete OML containing
the four pulled-back edge algebras. Either `T` reconstructs a same-side
Boolean boundary, or there is a first internal node *along the deterministic
`T`-descent path* at which the join `z` of the node's saturated witness pair
has a nonevent existential hull `H(z)`. All earlier path hulls are saturated
events of `T`, and `H(z)=pi^{-1}(h)` for exactly one of the node's recorded
64 node/candidate words `h`. **Hand proved** over the exhaustive search
certificate.

Induct along the finite DAG. At a current node its profile family is contained
in `T` by the prior hull choices and complement/disjoint-union closure. The
generator's chosen failed lower word is the union of a certified pair `a,b`
in that family. For `z=a join_T b`, leastness puts `z` below every current
saturated upper bound, hence

\[
 \operatorname{low}\subseteq H(z)\subseteq\operatorname{upper}.
\]

Thus the profile word of `H(z)` is one of the recorded candidates. If the
hull is an event, it is the least saturated upper bound and the corresponding child profile family
is contained in `T`; continue. If it is not an event, this is the first PJH
defect. Finite continuation otherwise reaches a reconstructing terminal.

This is a genuine finite grammar of *first hull defects*, not of arbitrary
repairs or terminal events. It neither proves that any defect type is
realizable in a terminal nor excludes gate B. The exact fixed-carrier T-FIN
residue is now: prove that none of these certificate-relevant first defects
can persist in a gate-B-avoiding terminal, or realize and audit one.

The proof requires both interval endpoints among the recorded children: the
actual hull word may equal `low` or `upper`. It also requires binary joins in
`T`; an OMP is insufficient. Surjectivity of `pi` is load-bearing for
reflecting the lower word. These hypotheses and endpoint assertions are
explicit in the replay receipt. Symmetry pruning of the DAG is not part of
the theorem.

**Lemma 8.4 (lower-endpoint exclusion).** The lower child at every internal
node cannot be a first PJH defect. Consequently only 33 of the 64 atlas edges
are possible first defects: three nonlower root choices and the upper choice
at each of thirty binary nodes. **Hand proved**, with the 33-edge count
separately **Executable verified** by the replay receipt.

If `low=a union b` and `z=a join_T b`, then `z` contains the entire saturated
pullback of `low`. If `H(z)` also has profile word `low`, it is contained in
that pullback, hence `z` equals the pullback of `low`; since `z` is an event,
its hull is an event. Thus a nonevent hull must strictly enlarge `low`. At a
binary node it must have word `upper` and properly split the unique gap
profile fibre. At the root it must use one of the three nonlower words and
properly split at least one newly entered fibre.

Here a profile word is a subset of the sixteen-point set `{0,1}^4`, and word
union is ordinary set union of those profile points. It is not bitwise OR of
two four-bit profile tuples and not an intersection of coordinate-letter
cylinders. Under the certified semantics,
`pi^{-1}(A union B)=pi^{-1}(A) union pi^{-1}(B)` exactly. The lemma proves no
candidate defect realizable or persistent in a terminal.

### 8.5 Symmetry-route exhaustion

The completed lexicographic atlas has no nontrivial post-hoc coordinate
symmetry. Inside the full 128-element unlabelled `K22` coordinate group, the
setwise stabilizer of the 48 node families is trivial. The stabilizers of the
64 selector-free family/interval/candidate edges, the 64 witness-decorated
edges, and the 33 possible first-defect occurrences are also all trivial.
Thus the 33 possible occurrences form 33 singleton orbits. **Executable
verified** by
`notes/open_questions/verification/full_grid_core16_pjh_symmetry_audit.py`,
payload
`1025c13fa037a3509a74f637e29f12e74958d67758b18bdac452022e03ba61a1`.
The verifier reconstructs the atlas families and checks the complete
128-element action twice; it shares the atlas replay constructor and is not
an independent core search.

All sixteen individual profile fibres occur as the newly entered fibre of at
least one candidate defect occurrence; the remaining root occurrence enters
the pair of profiles `3,12`. Coordinate profile alone therefore excludes no
defect. The symmetry result is about this completed selector-dependent atlas,
not the full intrinsic closure graph. A symmetry-reduced intrinsic defect
enumeration would require a new canonical-selector or full-closure search;
the present atlas must not be pruned or quotient-identified.

### 8.6 Defect-join normal form and activation escape

For a possible first defect with lower word `low`, hull word `h`, and terminal
join `z`, there are subsets `S_p` of the entered profile fibres such that

\[
 z=\pi^{-1}(\operatorname{low})\mathbin{\dot\cup}
   \bigcup_{p\in h\setminus\operatorname{low}}S_p,
 \qquad \varnothing\ne S_p\subseteq\pi^{-1}(p),
\]

and at least one `S_p` is proper. At a binary node there is exactly one
entered fibre and its `S_p` is proper. **Hand proved** from the hull definition,
lower-endpoint exclusion, and the receipt-certified interval sizes.

The join `z` itself never fires activation gate B. Each of the sixteen full
profile fibres contains points off row 0's activation cylinder and points off
row 1's. Every atlas lower word contains at least three full profile fibres,
and `z` contains their complete pullbacks. Hence `z` is contained in neither
activation cylinder. **Hand proved** over the exact profile count, which is
**Executable verified** for all sixteen profiles and all 33 occurrences by
`notes/open_questions/verification/full_grid_pjh_defect_activation_escape.py`,
payload
`ce11def275441aff7de5609404adefa4678ef0645d807d8ab95044c3b38932c6`.
The producer recomputes fibre cardinalities directly from the 224 cell-state
table without constructing the full carrier bitsets; it is not an independent
cell-state producer.

Thus any gate-B contradiction must arise from some later derived event or
cut; it is not witnessed by the first defect join itself. Isolation of an
activation-supported part of an `S_p` is one possible mechanism, not a proved
exhaustive one. Terminal realizability of the normal forms and gate-B
avoidance under later closure remain **Open**.
