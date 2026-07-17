# Actual rebase realization

## Scope

This note corrects the interpretation of `AR-REB-001`. The certified actual
two-copy event is the `Neg-023` relation `R`. Its physical-right universal
shadow `z` is a one-copy subset. The cylinder over `z`, the literal-envelope
cylinder `G`, and the 256 roots obtained after seeding `z` and `g` are not
thereby certified as generated events of the two-copy logic.

## Basic cut theorem

Let `P` be the actual fibre-product carrier, let `M subseteq P(P)` be a
concrete lattice ordered by inclusion, and let `R in M` be the actual
two-copy relation event. Let `i : L_X -> M` be the faithful cylinder/order
embedding of the finite old concrete OML, induced by a surjective coordinate
projection. Put

`C_z = {a in L_X : i(a) subseteq R}`

and suppose this cut has no greatest member. Let `h` be the join in `M` of
this finite embedded cut, let `g` be the literal union of the old subsets in
`C_z`, and let `G = i_set(g)` be the corresponding set-theoretic cylinder,
whether or not it is an event.
Then:

1. `G subseteq h subseteq R`;
2. `g subseteq forall(h) subseteq z`;
3. `h` is not in the embedded old copy;
4. `h = G` iff `G in M` (this is what “represented” means here);
5. if `h` is cylindrical, its unique trace `k` satisfies
   `g subseteq k subseteq z`.

Evidence: **Hand proved.** Every old cut member is below both `h` and `R`.
Literal union gives `G subseteq h`; since `R in M` is an upper bound,
leastness gives `h subseteq R`. If `h` were an old cylinder, faithfulness
would make its trace a greatest cut member. If `G in M`, it is an upper bound,
so `h subseteq G`, while the reverse inclusion was already proved. Conversely
`h = G` and `h in M` give `G in M`. Surjectivity makes cylinder traces unique,
and universal projection gives their inclusions.

No orthomodularity, state, or sigma-completeness conclusion is contained in
this theorem.

## Why cylindricity is not order-theoretic

Take `X = {0,1,2}`, `Y = {0,1}`,
`A = {0} x Y`, `B = {1} x Y`,
`G = A union B`, and
`H = G union {(2,0)}`. In the inclusion lattice

`{empty, A, B, H, X x Y}`

the join of the two cylinders `A` and `B` is the noncylindrical set `H`,
because the literal union `G` is absent.

Evidence: **Hand proved.** This is a bounded-lattice control, not a
complement-closed orthomodular lattice. It refutes only a proof from lattice
order alone.

## Decisive theorem

`ARR-CYL` (**Open, same-carrier form**): fix the actual fibre-product carrier,
its two surjective projections, both faithful old cylinder copies, and the
specific actual `left_retained_position11-Neg-023` event. In every admissible
concrete OML event-family completion on that same carrier containing these
fixed data, the join of the physical-right old lower cut is physical-right
cylindrical.

For a larger-carrier representation, this statement is not invariant until a
carrier map to the fixed fibre product and saturated pullback hypotheses for
the old copies and distinguished event are supplied. No such version is
claimed here.

- If `ARR-CYL` holds, the trace is a genuine new effective-base event between
  `g` and `z`. The existing 256-prefix applies literally only in the stronger
  branch `h = G`; otherwise it must be rerun from the exact trace.
- If `ARR-CYL` fails, the refuting `h` is the first genuine nonlocal mixed
  repair. Its partial-fibre sections, block incidence, and state effects
  become the next grammar seed.

Pure one-step cylindrical reflection does not prove the base case: it applies
after the relevant cylinders are known to be events.

## Restricted-generator control

Take only the cylinders of the two maximal old lowers `15250`, `16786`, their
complements, and the actual `Neg-023` relation; do not seed `g`. On the exact
14-atom truth-signature quotient:

- target-side complement/disjoint-union closure stabilizes at 12 events;
- adjoining the corresponding generators from both copies stabilizes at 16;
- both families are concrete orthomodular lattices;
- the two-copy family has trivial centre;
- in both families the least upper bound of the two maximal lower cylinders
  is exactly the noncylindrical `Neg-023` relation;
- their literal union is exactly the recorded `g` cylinder and is not
  generated.

Evidence: **Executable verified — sampled finite scope**,
`arr_cyl_critical_sublattice_pilot.py/.json`, producer `dec02775...`,
payload `f1df1685...`. Emit and verify independently recompute the same
producer payload; there is no independent implementation.

This is not an ambient completion of the full old copy. It therefore does not
refute `ARR-CYL`, but it refutes every proposed local proof using only the two
maximal lowers, both orientations, latticehood, orthomodularity, and trivial
centre. Any positive proof must use additional old events or global
admissibility/state data.

## Next discriminating action

Classify one-old-event extensions of the 16-event control: for each old event
`e`, adjoin both cylinders of `e` and its complement, close exactly, and test
whether the cut join remains `R`, becomes cylindrical, or the family becomes
nonlattice. This isolates the first genuinely load-bearing full-old-copy
witness without closing the 8,852-event critical sublattice blindly.

### Exact extension-type theorem

For an old event `e`, let `Q_e` be its realized refined truth carrier with
labelled base seeds, the two cylinders of `e`, and the left/right fibre
equivalence relations. If a bijection `Q_e -> Q_f` preserves all labelled
base seeds, sends the two `e` cylinders to the two `f` cylinders, and
preserves both fibre equivalences, then it induces an isomorphism between the
least complement/disjoint-union closures. Hence closure size, inclusion
order, the distinguished cut join, latticehood, orthomodularity, centre, and
cylindricity verdicts agree.

Evidence: **Hand proved.** Induction on finite expression trees transports
the generated closure; the remaining properties are invariants of the
labelled orthocomplemented-poset isomorphism, with fibre equivalences
load-bearing only for cylindricity.

The 14-atom control quotient is not a universal cache: an added old event may
split its atoms. The correct coverage descriptor is the canonical isomorphism
type of

`(realized refined carrier, labelled base predicates, L_e, R_e, eq_L, eq_R)`.

Literal equality of masks on a common refined carrier is sufficient but,
because cylinder embeddings are faithful, usually gives only the same old
event. Coarse existential/universal incidence is not a coverage theorem.

### Four-context discriminator

An exact refined-carrier pilot tested four complement-pair extensions:

- `7679/10752`: closure has 40 events, is a centre-free OML, and keeps
  noncylindrical `R` as the distinguished join;
- `109/18322`: closure has 38 events and is nonlattice; the distinguished cut
  has two minimal upper bounds;
- `100/18331`: closure has 32 events and is nonlattice with the same
  two-upper form;
- one shared disjoint control: closure has 20 events, is a centre-free OML,
  and keeps `R`.

No case generates the literal `g` cylinder. The two negative cases carry
hashes for both distinguished minimal upper bounds and for a first failed
lattice pair.

Evidence: **Executable verified — sampled finite scope**,
`arr_cyl_one_context_extensions.py/.json`, producer `f8201ff4...`, payload
`e88b81f0...`. Emit/verify recompute one implementation; the master-refinement
exactness is the preceding hand theorem, not an independent executable
implementation.

Thus the first load-bearing single old complement-pair contexts do not force cylindricity:
they reopen lattice repair. The next exact object is the two-upper repair
interval created by `109/18322` and `100/18331`.

### Selector-stability theorem

For either failed cut, write `l = x union y`, let `u,v` be its two minimal old
upper bounds, and put `G = (u intersection v) minus l`. Every same-carrier
candidate join is uniquely

`z = l union S`, with `S subseteq G`.

Let `C_z` be the complement/disjoint-union closure after adjoining `z`. Then

`z = x join y in C_z`

iff every generated upper `w` of `l` contains `S`.

Evidence: **Hand proved.** An upper `w` contains `z` exactly when it contains
the selector `S`. The same condition repairs the complement-dual meet.

This is the exact repair grammar obligation (`UP-S`). Interval membership at
the seed stage is insufficient: a later complement or complementary-cover
union may produce an upper omitting part of `S`.

More precisely, put

`K_S = intersection {w in C_z : l subseteq w}`

as a literal set and `kappa(S)=K_S minus l`. Since `z` is itself an upper,
`kappa(S) subseteq S`, and `UP-S` is equivalent to `kappa(S)=S`.
The empty selector is always stable. **Lean certified** on a finite carrier:
`forcedSelector_subset`, `isLeastSelectorUpper_iff_forcedSelector_eq`,
`forcedSelector_ssubset_of_not_least`, and
`forcedSelector_card_lt_of_not_least` in
`QuerySystem/KernelClosureCalculus.lean`; each reports
`[propext, Classical.choice, Quot.sound]` and no `sorryAx`.

These Lean theorems concern the literal current upper-core set, which need
not be an event. Separately, if `D` is a same-carrier concrete
inclusion-lattice family containing `C_z`, `x`, `y`, and `z`, then its join
`j=x join_D y` is uniquely `l union T` for a proper subset `T` of `S` whenever
`z` was not least in `C_z`: literal inclusion gives `l subseteq j subseteq z`,
and a generated upper witnessing failure of leastness persists in `D` and
forces `j != z`. Consequently, along nested same-carrier concrete lattice
enlargements, every later loss of leastness for this fixed pair strictly
decreases the represented join-selector cardinality, so it occurs only
finitely often. **Hand proved.** This corollary is not Lean certified and is
not asserted for abstract lattice embeddings or larger carriers.

Safe finite reduction is by the proved full stabilizer of the pointed family
acting on actual carrier subsets. A known subgroup only identifies cases
within its orbits. Any coarser descriptor must be a congruence for complement,
disjointness, union, selector containment, old cuts, and transition outputs.

For selectors saturated in the current 37-atom refined quotient:

- `109/18322`: one gap atom, hence two rooted candidates;
- `100/18331`: four provenance-distinct gap atoms, hence sixteen rooted
  candidates.

The first cube is a face of the second, giving sixteen distinct masks across
eighteen rooted cases. The generator-labelled truth atoms are singleton
automorphism classes inside that quotient, so no further quotient-level
symmetry reduction is justified. Neither interval contains `R` or any
existing event; `g` is the nonevent lower endpoint. **Executable verified —
sampled finite scope** on the 37-atom quotient.

This does **not** make the 18 cases exhaustive among same-carrier joins: an
arbitrary selector may split a refined truth atom. Exhaustive coverage requires
either a selector-saturation theorem or the proved full pointed automorphism
action on actual carrier subsets. The 18-case census is therefore a
saturated-selector local falsifier. Its failures are permanent negative
certificates; its survivors remain only local candidates because later
full-old/global events may introduce new uppers.

### Generic split-atom control

Selector saturation is false for finite concrete OMLs in general. On an
eight-point carrier, duplicate each of four old truth profiles, retain the
six-event old `MO2`, and adjoin `H = A union B union {0}`. The generated
12-event family is a concrete OML with `A join B = H`; the literal union is
absent and `H` splits the duplicated truth atom `{0,1}`. All point states are
additive and order-separating.

Evidence: **Executable verified — exhaustive finite scope**,
`split_truth_atom_oml_control.py/.json`, producer `9dd8f203...`, payload
`413e46df...`; one implementation, with deterministic two-seed replays.

The centre is four-element, not trivial. Thus generic OML axioms,
concreteness, finite sigma-completeness, and point order separation do not
force saturation, but centre-free/assembly-specific saturation remains
**Open**.

The centre cannot be killed on this carrier. The control contains singleton
event `{1}`. In every same-carrier complement/disjoint-union-closed extension
it remains central: events omitting it are disjoint from it, while for an
event `x` containing it, `x minus {1}` is again an event by complement and a
disjoint union. **Hand proved.**

An exhaustive census of all 256 one-subset adjunctions yields 43 distinct
closed OMLs and no family that both preserves `A join B = H` and has trivial
centre. **Executable verified — exhaustive finite scope**,
`split_truth_atom_centre_killing_no_go.py/.json`, producer `03b3f1bb...`,
payload `dd15096e...`; one implementation, with deterministic two-seed
replays.

Thus the next construction must inflate or re-represent the carrier so the
old central singleton pulls back to a multi-point event that a transverse
block can cross.

That inflation succeeds. Duplicate the central point once, pull back all
12 events, and adjoin one crossing event `K`. Exhausting all 512 subsets
gives 252 crossing seeds and 128 distinct closed families. Seventy are
centre-free concrete OMLs preserving `A join B = H`, literal-union absence,
the split truth atom, and point order separation.

The clean representative `K = 0x8a` has 16 events, three 8-event maximal
blocks, and exactly eight abstract two-valued states, equal to its eight
distinct point states.

Evidence: **Executable verified — exhaustive finite scope**,
`split_truth_atom_one_point_inflation_census.py/.json`, producer
`5c42fd94...`, payload `16c70914...`; one implementation with deterministic
two-seed replays.

Therefore centre-free finite concrete OML laws plus exhaustive two-valued
state classification still do not force selector saturation. Any positive
`ARR` theorem must use the actual adjacent-assembly/full-old-copy coupling.

### Cylindrical interpolation is the exact sufficient coupling

Let `a,b` be the two maximal old lower cylinders, let `R` be the actual
`Neg-023` target, and suppose their join `h` exists in a same-carrier
concrete lattice `M`.  Consider:

`CI_R`: for every noncylindrical `w in M` with
`a,b subseteq w subseteq R`, there is a cylindrical `c in M` with
`a,b subseteq c subsetneq w`.

Then `CI_R` implies that `h` is cylindrical.  Indeed, `R` is an upper bound,
so leastness gives `h subseteq R`; applying `CI_R` to a noncylindrical `h`
would produce a strictly smaller upper bound. **Lean certified** as
`KernelClosureCalculus.leastUpper_cylindrical_of_interpolation` in
`QuerySystem/KernelClosureCalculus.lean`. Its printed axioms are
`[propext, Classical.choice, Quot.sound]`. The application of `CI_R` to the
actual assembly remains **Open**.

Equivalently, every minimal upper of `{a,b}` in the interval below `R` is
cylindrical. This is weaker and more accurate than commutant rigidity:
`R` itself is noncylindrical and, being comparable with `a` and `b`, is
compatible with both.

Mere containment of full old OML copies does not supply `CI_R`. Horizontally
sum the clean `K=0x8a` centre-free split-selector control with any finite
two-valued-state-order-separated old OML (or two labelled copies). The
split join persists, the sum has trivial centre, and independently chosen
two-valued states order-separate it. **Hand proved**, using the
**Executable verified — exhaustive finite scope** properties of the clean
control. This schematic countercontrol deliberately has no actual
fibre-product mixed incidence. Consequently, genuine mixed coupling rather
than full-old containment is load-bearing.

### Exact transplant eligibility gate

The clean control must split an atom of the existing right-only twelve-event
family, not merely one of the fourteen generator-labelled truth words. The
current receipt records those fourteen nonempty words but not their physical
multiplicities. The first exact test is therefore:

1. construct every pointed isomorphism from the right-only twelve-event
   control to the generic twelve-event split-selector base, preserving the
   two lower generators and `R`;
2. locate the atom corresponding to the generic duplicated point;
3. refine it by the complete labelled full-old-cylinder signatures;
4. determine whether an eligible refined fibre has at least two physical
   realizations.

The restricted five-profile comparison has a unique pointed permutation
`[1,0,3,2,4]`. Hostile review **Refuted** and repaired the first one-atom
receipt: `K=0x8a` splits three generic representation atoms, whose actual
images are atoms `0,3,4` with word multiplicities `3,3,4`. The v2 receipt
transports all five atoms and fourteen words; the three split atoms give
`6*6*14 = 504` restricted selector combinations.
**Executable verified — exhaustive finite scope**,
`arr_k8a_transplant_eligibility.py/.json`, producer `f932e5f7...`, payload
`f666a2cb...`; one implementation reusing the exact quotient producer.
None is yet a certificate of physical or full-old-refined multiplicity.

The physical gate now passes. **Hand proved:** for a complete realized
signature map, one set can simultaneously realize prescribed
empty/full/proper-split behaviour on disjoint signature fibres iff every
fibre marked split has at least two points. Sufficiency chooses one point in
each split fibre and takes all full fibres; necessity is immediate. This is
only a set-existence theorem, not an event-generation or closure theorem.

The pair of full-old signatures is complete in the actual adjacent carrier:
each old copy contains the four embedded cell-cylinder families, whose 56
predicates separate all 224 cell labels, so the two four-coordinate
signatures recover the seven-coordinate adjacent point. **Hand proved over
executable premises.**

A weighted MDD census accounts for all `211897540016` adjacent points. The
three transported split atoms contain respectively `33458986624`,
`11773740160`, and `101985908824` complete signatures. Hence one physical
subset with the full transported `K=0x8a` empty/proper orientation exists.
**Executable verified — exhaustive finite scope**,
`arr_k8a_full_old_signature_gate.py/.json`, producer `e2ef399e...`, payload
`1e65c4c7...`; one implementation, with the total independently anchored to
the union-factor receipt and deterministic cross-seed replay.

The selector is not asserted to be generated or admissibly adjoinable.
The next exact gate is its compact-MDD adjunction to both full old copies and
`R`, followed first by old-cut and distinguished-join preservation, then
lattice, centre, block, and state audits.

That raw bounded adjunction fails latticehood at the distinguished cut.
For the deterministic three-point selector `S`, the family consisting of
both full old copies and `R,R^c,S,S^c` has:

- `R` and the right-old join `18322` as incomparable uppers of
  `15250,16786`;
- 31 of 32 right-old uppers not containing `R`;
- eight opposite-copy old uppers, none below `R`;
- neither `S` nor `S^c` an upper;
- no displayed-family interpolant below both `R` and `18322`.

Thus this bounded family has no least upper for the cut. **Executable
verified — exhaustive finite scope**, `arr_k8a_deterministic_selector_cut_audit.py/.json`,
producer `8ce29969...`, payload `4ce40c3d...`; final seed-0 run, with an
earlier pre-strengthening version but not the final cross-upper scan replayed
under a second hash seed.

Independently, `S^c` has no greatest old lower on either side: the left copy
has 2389 old lowers with 23 maxima, and the right has 2402 with 26; explicit
atom-fold escapes are serialized. This is not an impossibility theorem for
completion. It identifies the exact repair: any completion must adjoin a new
upper below `R` and old join `18322`, while simultaneously re-basing the
`S^c` lower kernels. Broad unstructured selector closure is stopped.

The forced interval top is now explicit:

`T = R intersection cyl_right(18322)`.

It contains both old lowers, and every repair join lying below the two
incomparable bounded uppers lies below `T`. **Hand proved** by set
intersection. `T` is noncylindrical on both sides, unequal to `R` and
`cyl_right(18322)`, and equal to no current single seed.

Its left old lower kernel is principal: 16 lowers with greatest element
`13848`. Its right kernel has 192 lowers with maximal elements exactly
`15250,16786`; the eight-atom fold escapes `T` at atom `10752`, reaching
old join `18322` after prior fold `15250`. **Executable verified —
exhaustive finite scope**, `arr_forced_interval_top_audit.py/.json`,
producer `ead0b9df...`, payload `9d024359...`; seed-0, one implementation,
no cross-seed replay.

No closure round was run, and generation of `T` remains **Open**. The exact
next theorem is whether adjoining `T,T^c` gives a valid provenance-sensitive
rebase transition: `T` must become the distinguished join, old cuts must be
transported, and its complement kernels must repair without creating a
higher-rank target.

### Forced-top descent calculus

The phrase “forced interval top” means the greatest set-theoretic envelope
of a repair below the displayed uppers, not a uniquely forced repair event.
Smaller represented joins below `T` remain possible.

Fix source events `x,y`, put `l=x union y`, and at stage `n` let `U_n` be the
represented uppers of the fixed source cut below an initial upper. Define
`tau_n = intersection U_n` and `r_n = |tau_n minus l|`. For every newly
represented upper `w`, either `tau_n subseteq w` and the upper is redundant
for this cut, or the new forced top is `tau_n intersection w`, a proper
subset with strictly smaller rank. If a forced top is represented and every
later upper contains it, it is the join. **Hand proved.** This is a cut-local
well-founded rank, not a global repair rank: mixed closure may create new
source cuts.

Complement gives an exact kernel duality. For an
orthocomplement-preserving old embedding `i`, `i(a) subseteq W^c` iff
`W subseteq i(a^perp)`. Hence maximal old lowers of `W^c` correspond to
minimal old uppers of `W`. **Hand proved.** Moreover, adjoining a seed
`k subseteq T^c` cannot by itself cut `T`, because its complement contains
`T`; destabilization requires a genuinely mixed bridge.

For finitely many fixed source cuts, if no transition creates a new source
cut and every nonterminal transition strictly cuts at least one forced top,
the sum of the ranks strictly decreases. This gives a finite grammar under
those hypotheses. **Hand proved.** Closure of the obligation set is the
exact missing theorem; a new-source-cut witness refutes it and defines the
next provenance type.

An attempted `T,T^c` executable audit was not banked. Its source and receipt
hashes diverged after an interrupted optimization, and two nonemptiness flags
used the universal rather than existential shadow. Both untracked artifacts
were excluded. No provisional count or transition verdict is evidence.

### Exact immediate literal-bridge layer

Enumerating every disjoint union of `T,T^c` or the four distinguished old
events with an old cylinder on the opposite side gives 498 occurrences and
488 distinct physical MDD roots. Two roots are already distinguished seeds;
486 are new. Of all 488 roots, 474 cannot be represented by the frozen five
parents plus one old cylinder. Thus the fixed-five grammar is **Refuted**.

The roots form 27 coarse provenance/signature buckets, but the largest bucket
contains 189 exact roots. This partition is not a transition congruence. No
root in the layer is cylindrical on either side, a singleton, or supported in
one of the seven coordinate activation cylinders. **Executable verified —
exhaustive finite scope**, `arr_forced_T_literal_bridge_census.py/.json`,
producer `631756c1...`, payload `af993bf5...`; hostile source review passes,
but the verifier is a deterministic replay rather than an independent
implementation.

This census covers only immediate literal complement/difference and disjoint-
bridge transitions. It proves no kernel principality, later closure,
latticehood, orthomodularity, centre, state separation, sigma-completion,
ODBC, or `Phi`.

An eight-root provenance-diverse pilot already refutes closure of the current
obligation set. Five roots create right-copy source-cut obligations: three
have incomparable minimal old uppers and two have incomparable maximal old
lowers with explicit atom-fold escape. Three controls remain principal on
both sides. **Executable verified — sampled finite scope**,
`arr_forced_T_bridge_kernel_pilot.py/.json`, producer `3f584956...`, payload
`c1cdbb8b...`. Rootwise exhaustion cannot prove closure because it omits
cross-root pairs; a positive result needs a locality theorem or transition
congruence.

The simplest such locality theorem has now been isolated. If every generated
event has a one-half normal form (`NF`), same-half source joins are total and
represented (`SS`), the complement/difference dual rules are total (`SD`),
and opposite-half pairs reduce to containment, top, or old-new pairs (`X`),
then every two-new-parent cut is resolved. **Hand proved** by the four normal-
form cases. These hypotheses are sufficient, not established.

In fact one-new-parent locality fails for the current immediate family. New
roots `[8,106]` have a missing intersection with incomparable maximal current
lowers `old_left(1024)` and `old_right(2)` and no interpolant. **Executable
verified — sampled finite scope**, `arr_forced_T_same_half_cross_root_pilot`
`.py/.json`, payload `f67f8531...`. The exact next repair root is a meet above
those two lowers and below both new parents, together with its complement-
dual join. This is a new binary provenance cell, not another unary kernel
type.

## Campaign gate table

| Gate | Current status | Evidence | Remaining obligation |
| --- | --- | --- | --- |
| Repair grammar | Open; unary obligation set and one-new-parent locality refuted | `[8,106]` is a binary same-half repair cell | classify its forced meet and prove/refute `NF+SS+SD+X` coverage |
| Latticehood | Open | actual old lower cut has no greatest old member | construct its join in an ambient completion |
| Orthomodularity | Open | no completed rebase OML | audit after lattice closure |
| Same-side boundary preservation | Open | `G ⊆ h ⊆ R` | determine the sections of `h` |
| Activation-event avoidance | passes immediate literal layer only | zero of 488 classes lies in a coordinate activation cylinder | test later kernel repairs and closure |
| Trivial centre | Open | not tested for actual `h` | classify blocks/commutation after closure |
| State order separation | Open | point-state persistence applies only once events are concrete | audit the completed event family |
| `Phi`-tameness or obstruction | Open | no admissible completed assembly | classify all relevant states |
| Infinite-limit viability | Open | actual finite rebase unresolved | prove finite embeddings first |
| Universal normalization | Open | this is one architecture | no promotion beyond the fixed occurrence |
