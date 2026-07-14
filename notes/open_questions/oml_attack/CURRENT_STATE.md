# σ-essential-state problem: current mathematical state

This is the compact starting index for further work. Git history and the cited notes remain authoritative for proofs and computations.

## Problem and evidence boundary

The open question is whether a concrete σ-complete orthomodular lattice can carry a σ-essential state. The programme conjectures no. Hand proofs, executable finite checks, bounded censuses, and Lean certificates are distinct evidence classes; none of the current finite results resolves the infinite problem.

## Accepted baseline

The endgame continuation began at
`5a412563f7c1c348c3fbf0e261650a54cb7f452b`; earlier baselines and the full
evidence ledger are retained in `CAMPAIGN_LOG.md`.
Lean verifies Stone density, blockwise σ-additivity, two-block rescue, and
the fine-block Dirac/pointed results. The newer coarse, cyclic-coupling, and
type-partition results are hand proofs at the scopes stated in their notes.

## Integrated candidate results

1. The smallest binary proper-joint-closure completion is the finite 48-event OML `MO2 × P(3)`. It has a 16-element centre and is Φ-tame.
2. A three-block noncentral transverse triangle exists inside a centre-free 56-event completion, but every full maximal-block boundary saturates and the finite model is Φ-tame.
3. Exhausting all 127 subfamilies of the fixed seven labelled blocks leaves exactly four centre-free OMLs with a proper exhaustive maximal-block boundary and proper-closure transverse triangle. The selected 44-event survivor refutes the proposed local-centrality obstruction, not the main conjecture. Its 12 point states give the full coherent finite relation, hence it is Φ-tame.
4. Inflating the `q0` interval of the five-block survivor by an arbitrary concrete Boolean σ-algebra gives, at hand-proof level, a concrete σ-complete centre-free OML with exactly five maximal blocks, a surviving proper boundary, and a face-exposed noncompact eligible local σ-state slice. Finite-fibre receipts cover two through four fibre atoms, and a global 60-form truth-vector audit checks the compatibility classification. Common-fibre point replacement still proves Φ-tameness.
5. The eight smallest whole-interface `P(2)` triangle twists are closed: odd parity is nonfaithful and collapses the shared interval; even parity is gauge-trivial. This is only a bounded classification of that twist class.
6. Literal independent atom-interval substitutions and the completed single-pullback non-atomic route are Φ-tame under their stated extension hypotheses. Proper-interface twists and inequivalent coarse-coordinate systems remain open.

## Known tameness mechanisms

- central common-base decomposition;
- full-boundary saturation;
- independent point replacement;
- common-point pullback extension;
- compact simultaneous selection;
- trivial monodromy;
- gauge-trivial whole-interface twists.

Nearby constructions governed by one of these mechanisms should not be repeated without an explicit structural distinction.

## Resolved rotating route and current frontier

Gate N for `oml_rotating_small_piece_candidate.md` **passed**. The
fixed-column six-cell trace has 24 events and passes
its independently verified finite census. New arbitrary-base upper invariants
now prove that no nonzero generated event is supported in the unresolved `W`
regions, no set intersection `Σ_i∩Σ_j` is generated, and no collector can be
restricted with uncountable variation modulo countable column support. The
three-type transversal algebra has 88 profiles; balanced finite-core closures
of lengths 3, 6, 9, 12 have 88, 180, 700, 4428 events and pass a separate
recomputation. The finite relation has mode counts 44/36/0/8 by number of
binary coordinates. Universal transversal membership supplies an anchor
profile, one disjoint cylinder supplies all varying binary supports, and the
certified local trace events patch the countable exceptional columns. Thus
every generated event is a countable-column modification of an explicit
parameterized core. See `oml_typed_graph_closure_calculus.md` §8.

Gate L then **failed**. The generated events `cyl(T₁)` and `G₁₂` have two
explicit upper bounds, but the universal transversal relation has no profile
in the interval required of their join. This is an arbitrary-base proof, not
a finite-quotient extrapolation. The rotating σ-class is not a lattice; Gates
M, C, Z, F, and Φ were not entered. The reusable output is the finite-profile
interval obstruction theorem. The active frontier returns to B′(i)/T4 and
boundary selection, informed by this graph-network closure result. A new
theorem now proves `Φ⇔T4At` whenever the maximal-block atlas is countable and
every block is countably generated. Hence the surviving fine-block residue
requires an uncountable, genuinely distributed atlas.

## Endgame selection reduction

T4At hand-proves hereditary one-block boundary escape on every finite face
refinement, but this does not yield simultaneous selection. Cantor space
admits a point-indexed singleton defect cover in which every countable
subfamily is escapable; each local defect is realized by
`Clop(2^N) -> Borel(2^N\{x})` for a countably generated fine block. The
naive common-interface paste is central and has no separating global
sigma-states.

For coarse blocks, sigma-liftability is exactly a coherent inverse system of
lifts on all countably generated block subalgebras. Local nonemptiness
without coherence fails in ZFC on the club field over `omega_1`. The exact
remaining theorem package is now formalized exactly in
`oml_distributed_boundary_compactness.md`. For a coherent finite pattern
`p`, `X_p(J)` retains one full global finitely additive witness and eligible
sigma-lifts on every block in `J`. ODBC has two load-bearing clauses:
ODBC-S (every countable subsystem has a section) and CODBC (those sections
globalize). Their conjunction implies GSD and `Phi`. CODBC alone does not:
finite eventwise satisfiability does not even give a section over two whole
blocks. The abstract implication layer is Lean verified in
`ODBCSections.lean`.

Campaign 2 defines finite profile cut-saturation and proves it necessary in
the scoped typed calculus, but refutes its implication to ODBC-S even
abstractly. Complete Boolean lattice cuts and sigma-state order separation
do not upgrade finite equations to a whole-boundary lift (`P(N)` control).
Positive scopes are finite generated boundaries, exact two-block atlases
with literal trivial centre, and finite fine atlases under T4At. Relative
closed eligibility plus finite subsystem sections gives a compact-FIP proof
of a global section, but sigma-state loci are generically nonclosed. Bare
tree/cycle incidence, surjectivity, Mittag--Leffler, compact fibres, and
softness yield no further theorem. The next class is a centre-free coarse
three-block atlas, with singleton, pair, and triple section gates all open.

Campaign 3 completes the compact-ambient abstract countermodel: on Cantor space,
`X(J)=C\J` has sections on every countable subsystem and none globally,
hereditarily on finite-coordinate refinements. Standard-Borel relations
`R` have exact Boolean realization with sigma trace `R` and f.a. trace
`closure(R)`; the eligible spaces are noncompact. Realization fails at three precise mechanisms: an injective
countably generated separating sigma-boundary cannot omit one point;
invertible deterministic transport identifies the boundary ranges; repeated
selector pairs define the same intrinsic subalgebra. The 44-event OML
refutes a universal completion-saturation theorem. The live realization
theorem therefore requires nondeterministic nonclosed correspondences with
proper coordinate subalgebras, or a proof that OML mixed cuts collapse them.

Campaign 4 adds two conditional positive theorems. In the fine regime,
T4At plus local countability—or merely countable-subcover reflection—of the
closed nowhere-dense block-bad loci implies Phi by compactness and Baire.
Point-countability and transfinite finite-face repair fail. In the coarse
regime, countable-intersection reflection (CIR) upgrades separately solvable
countably generated envelopes to one coherent Dirac lift; the club field
violates CIR exactly. Coarse ODBC itself is canonically ordinary ODBC/Phi,
not an easier independent factor. The unconditional fine incidence and
coarse CIR consequences of OML hypotheses remain open.

Campaign 6 integrates the stable chain:
`Phi iff GSD iff ODBC iff coarse ODBC`. Fine CSR and coarse
CIR-plus-same-`mu` envelope solvability are sufficient, nonexhaustive
conditions. No current statement satisfies stopping condition 3:
normalization of every Phi failure to the nondeterministic transported
architecture and realization-or-mixed-cut-collapse completeness are both
open. The combined boundary-obstruction completeness programme is recorded
in `oml_global_integration.md`. `ODBCRegimes.lean` verifies only the
conditional regime-packaging implications.

## Primary sources

- `notes/programme/frontier_map.md`
- `notes/programme/program_overview.md`
- `notes/open_questions/oml_attack/oml_lattice_taxonomy.json`
- `notes/open_questions/oml_attack/oml_exhaustive_boundary_survivor.md`
- `notes/open_questions/oml_attack/oml_arbitrary_base_inflation_review.md`
- `notes/open_questions/oml_attack/CAMPAIGN_LOG.md`
- `notes/open_questions/oml_attack/oml_rotating_small_piece_candidate.md`
- `notes/open_questions/oml_attack/oml_lattice_regularity_attack.md`
- `notes/open_questions/oml_attack/oml_endgame_selection_residue.md`
- `notes/open_questions/verification/`
- `formalization/QuerySystem/`
