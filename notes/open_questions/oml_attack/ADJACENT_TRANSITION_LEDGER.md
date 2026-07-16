# Adjacent exact-root transition ledger

*Campaign 20, Level-1 controller. Coordinate controls and actual generated
relations are deliberately separate.*

## Closed first-round gate

For either adjacent orientation, every first-round mixed leaf has a greatest
old lower shadow.

- Nonempty kernels: `18370/18370`, 32 frozen shards, zero failures.
- Empty-mask kernels: `37352`, discharged algebraically.
- Total: `55722/55722`.
- Evidence: **Executable verified — exhaustive finite scope** for the nonempty
  kernels; **Hand proved** for empty masks; hostile review passed.
- Commit: `e523098` (`Establish exhaustive adjacent first-round kernels`).
- Manifest producer:
  `notes/open_questions/verification/adjacent_full_cycle_exhaustive_manifest.py`
- Shard producer:
  `notes/open_questions/verification/adjacent_full_cycle_exhaustive_shard.py`
- Aggregator/verifier:
  `notes/open_questions/verification/aggregate_adjacent_full_cycle_exhaustive_shards.py`
- Independent semantic manifest verifier:
  `notes/open_questions/verification/verify_adjacent_full_cycle_exhaustive_manifest_semantic.py`
- Master:
  `notes/open_questions/verification/adjacent_full_cycle_exhaustive_first_round_master.json`
- Master payload: `bf3f7d297e6fdbf273273af06ffbd99bd560a5e5e7203e41f3f39c8a7124749e`.
- Manifest payload: `423d62245cd87ef395482cc7d4d3da512b65604dbe82446eb18628e7e22d18f4`.
- Semantic verifier payload:
  `ff6cbeba828da3d191220e0edf5986cb5282c60c8a6bfce399312806e6f963e3`.

This proves first-round conservative shadows only. It does not prove Boolean
closure of later actual relations, latticehood, orthomodularity,
sigma-completion, MBRC, ODBC, or `Phi`. Do not rerun this census as a new
mathematical workload.

## Transition record schema

Every row uses:

`id; layer; orientation; term; parents; exact_section_state; forall_shadow;
exists_shadow; old_lower; old_upper; bridge_atoms; atom_saturation; escape;
successor; evidence; scope`.

For `layer=coordinate_control`, `exact_section_state` is only a one-copy target
root and `successor` has no actual-event meaning. For
`layer=actual_relation`, it is the canonical restricted-MDD section class in
each shared-state fibre. Missing shadows or successors are recorded as
`missing`, never inferred.

## Coordinate-control escape classes

The bounded coordinate-target producer applies `Neg/OrthoOr` to one-copy
universal-shadow targets. It finds:

- complement-good counts: left `6/10`, right `9/14`;
- disjoint bridge-good counts: left `37/42`, right `66/73`;
- strict disjoint-union failures: 12 total, left 5 and right 7;
- 197 bridge-atom incidences, 182 single-atom escapes;
- 181/182 escaping incidences phantom (`full17=0`);
- 176/182 land at old top;
- atom saturation is kernel-bad in 12/12, equals the target in 6/12 and is
  proper in 6/12.

Evidence: **Executable verified — sampled finite scope**, payloads
`3fbf81c28e099fe353266fa6f4592b86e4e151660f88202b8743ebf675c66363`
and
`174fe4c5fae1a4b0fd140e33321fe2a5babe8ce0cde3311f8f9331bab20a1d84`.

The four aggregate bounded escape signatures are:

| Type | Saturation | Bridge status | Landing | Count |
|---|---|---|---|---:|
| `CC-PPT` | proper | all phantom | all top | 1 |
| `CC-ENS` | equals target | includes nonphantom | includes subtop | 1 |
| `CC-EPT` | equals target | all phantom | all top | 5 |
| `CC-PPS` | proper | all phantom | includes subtop | 5 |

For each row, the actual-relation transition is `not_evaluated`. These are
fixed-target obstruction controls, not certified generated-event escapes.
The earlier promotion of them to forced re-basing transitions is **Refuted**.

The complete 12-row serialization is now banked in
`notes/open_questions/verification/adjacent_coordinate_escape_ledger.json`.
Every row includes stable ID, orientation, child provenance, exact target
root and `E/U`, bridge atom indices and hashes, base and first escaping join,
single-atom landing records, saturation status, aggregate signature, and the
complement-derived old upper certificate.

For all 12 rows:

- `greatest_old_lower_exists=false`;
- the serialized `old_atom_fold` lies outside the target and is the escape
  certificate, not an old lower;
- `least_old_upper_exists=true`, certified as the complement of the greatest
  old lower of the target complement;
- actual successor, centre, state, boundary, activation and `Phi` consequences
  are `not_evaluated`.

**Executable verified — sampled finite scope**, producer/receipt
`adjacent_coordinate_escape_ledger.py/.json`, payload `12c6f217...`, producer
`5cc508ad...`, row-chain `00db935f...`; hostile review passed after correcting
the escaping-fold label and adding the receipt-local complement-kernel
certificate.

Conditional theorem: if an actual generated event has the same certified old-
below predicate and its old atom fold escapes, then the affected old copy
cannot preserve its old finite joins. **Hand proved + Lean certified** through
`no_sup_preservation_of_escaping_upper_bound` and
`no_foldl_sup_preservation_of_escaping_upper_bound` in
`KernelClosureCalculus.lean`.

## Actual-relation transitions

The exact state is

`AR(orientation, attainable retained truth profile,
joint section-congruence class, old lower, old upper, provenance)`.

Boolean transitions are computed on exact restricted sections before
recomputing universal/existential shadows and old kernels.

The canonical six-leaf quotient tests 156 actual relation occurrences:

- left: 72; right: 84;
- actual bad kernels: `0`;
- coordinate-target bad occurrences: `22`;
- universal-shadow mismatches: `55` (`20 Neg`, `35 OrthoOr`);
- `Leaf/And` mismatches: `0`.

Evidence: **Executable verified — sampled finite scope**, hostile source audit
passed, commit `3e26da7`, producer/receipt
`adjacent_full_cycle_actual_event_shadow.py/.json`, payload
`3d6f97c80ff21de11da3d748acb1d7635fa926386bf376ae921c0b7c1cdab6e9`.

## Descriptor refutations

1. Universal shadow alone is not closed under complement or union.
2. `(forall,exists)` is not a full Boolean transition state.
3. Coarse `(E,U)` witness data do not determine the exact simultaneous
   section grammar.

For item 3, every structurally distinct inclusion-minimal exact-root
single-slot substitution available in the 12 sampled leaf slots is tested.
There are 17 substitutions; 14 change the full 224-state simultaneous six-bit
opposite-pattern vector. The first divergent substitution is left slot 0,
`A=0`, `U=1`, opposite witness `9 -> 11`. Its exact semantic rerun changes the
true universal-shadow-table and audited-term digests. Baseline and variant
both retain zero bad actual kernels.

Evidence: **Executable verified — exhaustive within the declared sampled
single-slot scope**, producer/receipt
`adjacent_full_cycle_witness_diversity.py/.json`, payload `39bd3fe0...`;
hostile review passed. This refutes an `(E,U)`-only exact grammar, not
conservative-shadow existence or a richer finite grammar.

## Smallest adequate descriptor

For unary contexts over fixed section constants `K`, the exact type of a
section `b` is its pair of lower and upper `K`-cuts. This is **Hand proved**.
It is not a congruence for binary operations between dynamic witnesses.

The smallest currently justified full descriptor is the joint Boolean-context
congruence in each shared-state fibre. The exact restricted-MDD section root
is a valid nonminimal representative. A finite grammar theorem must prove:

1. finite classes per orientation, state and attainable retained profile;
2. well-defined complement/intersection/union transition tables;
3. a class-invariant universal-output predicate;
4. exact generator interpretation and induction on terms;
5. associative, order-independent transport of old lower/upper shadows.

## Re-basing operation

Status: **Open; conditional only**.

If an actual generated event `u` first has no greatest old lower in an
effective base `K`, define the minimal concrete-logic successor candidate

`K[u]=closure_under_complement_and_disjoint_union(K union {u})`.

Any actual certificate `P,a <= u` with `P join_K a` not below `u` forces that
old join and its complement-dual meet to change in every lattice successor.
What remains undefined until such an actual escape appears:

- the replacement extrema;
- closure size and rounds;
- maximal blocks and centre;
- state extensions and order separation;
- boundary/activation gates;
- conditional relation and `Phi` status;
- canonicity, commutation and associativity.

Coordinate-control escapes do not instantiate this operation.

## Collapse-gate status

| Gate | Current adjacent exact-relation status |
|---|---|
| same-side boundary reconstruction | not detected by bounded shadow audit; not separately evaluated |
| activation-supported event | not evaluated for a re-based successor |
| nontrivial centre | not evaluated for a re-based successor |
| loss of state order separation | not evaluated for a re-based successor |
| altered conditional relation | not evaluated for a re-based successor |
| `Phi`-tameness | open |

## First Fir workload

Do not repeat the first-round kernel census. Submit an exact section-congruence
classification:

1. **Parameter set:** both orientations; exact restricted section roots by
   shared state and attainable retained truth profile; depth-one actual
   `Leaf/And/Neg/orthogonal-Or` transitions; all 91 old atoms.
2. **Shard verdict:** stable congruence class and transition hashes, or the
   first actual universal-shadow kernel escape.
3. **Negative witness:** orientation, state/profile, parent classes, exact
   roots, term, old eligible atoms, escaping fold and target.
4. **Positive coverage proves:** the minimized transition table is exact for
   the declared depth-one generator family and every audited class has old
   lower/upper shadows.
5. **It does not prove:** arbitrary depth, associativity across three
   rectangles, OML closure, sigma-completion, MBRC, ODBC, or `Phi`.
6. **Hand-theorem contribution:** provides the finite alphabet and transition
   table needed for an induction/coverage theorem; if classes fail to compress,
   record that boundary instead of extending depth.

Require cross-seed replay and an independent Boolean-context verifier. Stop at
the first actual escape; only then launch a capped re-basing closure.

Before production, freeze:

- the generator universe and hash;
- the exact generation rule (which nodes admit `Neg`, and which disjoint pairs
  admit `OrthoOr`);
- the equivalence specification and canonical representative rule;
- total transition coverage and collision-free root binding;
- universal/existential and old lower/upper invariance within every class;
- conflicting-transition and unreachable-class counts;
- three-term critical-pair/path-independence tests.

A minimized class count alone is not a grammar theorem. Outputs must return to
the declared class domain and all construction paths to one semantic class
must give the same transitions and shadows.

### Congruence-minimization verdict

The global exact-universal-output minimization route is now closed
negatively. Each canonical six-leaf orientation has nine realized mixed-word
atoms, so its generated section algebra is the 512-element powerset algebra.
Any Boolean congruence preserving the exact predicate `section=top` is
equality. **Hand proved** in arbitrary Boolean algebras; the bounded producer
reconstructs the two 9-atom algebras and explicit distinguishing contexts.

- left: 375 section occurrences, 10 distinct sections;
- right: 416 section occurrences, 11 distinct sections;
- full generated algebra: 512 elements in each orientation;
- all 14 witness divergences change the section system and have an explicit
  universal-output distinguishing context;
- witness variants realize atom alphabets of size 9, 10 or 11.

Evidence: **Executable verified — sampled finite scope**, producer/receipt
`adjacent_section_congruence_minimization.py/.json`, payload `2ebe78a9...`;
hostile review passed.

This rules out nontrivial global Boolean-congruence compression preserving
exact universal shadows. It does not rule out:

1. a weaker congruence preserving only old lower/upper kernel outcomes;
2. a typed partial-context quotient;
3. symbolic DAG sharing without semantic identification;
4. a parametric provenance normal form with witness-dependent atom alphabets.

Do not send a Fir workload to enumerate the 512-element transition table:
symbolic Boolean laws already decide it. The next smallest workload is the
kernel-observational congruence:

- observations include the exact old lower index and complement-dual old upper
  index, not merely good/bad;
- equivalent parents must have equivalent complement/intersection/disjoint-
  union children under every declared typed transition;
- the first conflicting transition is the negative certificate;
- if the kernel quotient also collapses to equality, stop finite minimization
  and pivot to parametric exact-root normal forms.

### First certified actual escape

The two-sided audit corrects the earlier one-sided headline. The prior
`actual_kernel_bad_terms = 0` counted only the retained universal projection.
For the same 156 reachable actual-relation occurrences, the opposite
projection has seven genuine lower-kernel escapes:

- left-retained orientation, opposite physical-right side:
  2 `Neg`, 5 exact-disjoint `OrthoOr`;
- right-retained orientation, opposite physical-left side: 0.

The first is `left_retained_position11-Neg-023`, generated from `And-010`.
Its retained physical-left bracket is the singleton old event `14557`; its
opposite physical-right shadow has no greatest old lower and has least old
upper `18331`. This is an **actual_relation** transition, not a coordinate
control.

Evidence: **Executable verified — sampled finite scope** over the fixed
six-generator reachable family,
`adjacent_kernel_observational_congruence.py/.json`. The receipt serializes
physical-side mappings, every endpoint failure and stable occurrence
provenance. Hostile review and independent mapping audit pass. It does not
cover the full 512-element algebra, alternative witnesses, arbitrary depth,
successor closure, OML, sigma, ODBC, or `Phi`.

### Forced re-basing theorem

Let `z` be an actual generated target and `L` an old rectangle. If
`{a in L : a subset z}` has no greatest member, then:

1. no monotone deflationary retraction fixing `L` exists at `z`;
2. every specified finite lattice extension containing `L` and `z` contains
   a genuinely new join of all old events below `z`;
3. therefore the effective side must be re-based before subsequent
   transitions are classified.

This is **Hand proved**. The cut and its literal union/intersection envelopes
are canonical. A subset-valued repair is not canonical until an ambient
completion is fixed.

The next transition is `AR-REB-001`: re-base the physical-right side at
`Neg-023`, recompute both endpoint tables, then test the join-association
diamond through its parent `And-010` and the complement-dual meet diamond.
All collapse gates remain `unevaluated_pending_rebase_closure`.

### AR-REB-001 bounded realization

On the physical-right old carrier, the first target has:

- 192 old lowers with incomparable maximal elements `15250`, `16786`;
- 8 old uppers with least element `18331`;
- 8 eligible old atoms;
- explicitly seeded literal lower envelope `g = 5f067021...`, proper below the target and
  dominating every old lower;
- old atom fold `18322`, which is outside the target.

The strict changed join is `(15250, 10752)`: its old join is `18322`, while
its literal union is `g`. This is the first exact re-basing transition.

The capped concrete-logic closure explicitly seeded by target, complement, `g`, and
complement reaches 256 new events in its first round and does not stabilize.
Evidence: **Executable verified — sampled finite scope**,
`adjacent_ar_reb_001.py/.json`. This proves neither terminal closure nor a
finite/unbounded grammar.

The computation does not prove that `g` is generated without being seeded or
that every ambient lattice contains `g`; its forced ambient cut join may
strictly overshoot the literal envelope. Precisely, every finite ambient
lattice extension containing the old copy and target has a new cut join `h`
with `g subseteq h subseteq target`, and `h = g` if `g` is represented. The
descriptor must include the exact target root, lower-cut maxima,
eligible-atom incidence, literal cut union, changed old join provenance, and
generation parentage. A larger undirected cap is prohibited until these 256
events are classified into transition types.

### Frozen-prefix descriptor boundary

The first proposed prefix descriptor partitions the 256 new roots into 240
classes: 224 singletons and 16 doubletons. All 16 doubletons have distinct
restricted complement/disjoint-union behavior. The smallest is descriptor
`014c703b...`, containing roots `4d4062cd...` and `2572f79e...`.
**Executable verified — sampled finite scope** by
`adjacent_ar_reb_001_prefix_classification.py/.json`, producer
`92a0a18a...`, payload `7f98fcc1...`. A seed-12345 scratch replay is
fieldwise identical; there is no independent producer.

Thus scalar generation depth, parent-depth multiset, target/envelope
incidence, old endpoints and the recorded changed-cut flags are insufficient.
Some finer descriptor is required. Complete parent-root/provenance incidence
is the first sufficient candidate exposed by the witnesses, not a proved
minimal invariant.

For fixed seeds, schedule independence itself is settled: the omega-union of
the finitary complement/disjoint-union operator is the unique least closed
family, and every fair schedule reaches it. **Hand proved.** This does not
settle finite termination, grammar finiteness, or associativity of assemblies
with different seed sets.
