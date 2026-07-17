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

`ARR-CYL` (**Open**): in every admissible concrete OML completion containing
the specific actual `left_retained_position11-Neg-023` occurrence and both
old cylinder copies, the join of the physical-right old lower cut is
physical-right cylindrical.

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

Thus the first load-bearing full-old contexts do not force cylindricity:
they reopen lattice repair. The next exact object is the two-upper repair
interval created by `109/18322` and `100/18331`.

## Campaign gate table

| Gate | Current status | Evidence | Remaining obligation |
| --- | --- | --- | --- |
| Repair grammar | Open | 256-prefix is a seeded shadow control only | realize the actual cut join |
| Latticehood | Open | actual old lower cut has no greatest old member | construct its join in an ambient completion |
| Orthomodularity | Open | no completed rebase OML | audit after lattice closure |
| Same-side boundary preservation | Open | `G ⊆ h ⊆ R` | determine the sections of `h` |
| Activation-event avoidance | Open | not tested for actual `h` | test every generated rebase event |
| Trivial centre | Open | not tested for actual `h` | classify blocks/commutation after closure |
| State order separation | Open | point-state persistence applies only once events are concrete | audit the completed event family |
| `Phi`-tameness or obstruction | Open | no admissible completed assembly | classify all relevant states |
| Infinite-limit viability | Open | actual finite rebase unresolved | prove finite embeddings first |
| Universal normalization | Open | this is one architecture | no promotion beyond the fixed occurrence |
