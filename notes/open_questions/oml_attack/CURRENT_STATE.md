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
CIR-plus-same-`mu` envelope solvability are sufficient and not proved exhaustive
conditions. No current statement satisfies stopping condition 3:
normalization of every Phi failure to the nondeterministic transported
architecture and realization-or-mixed-cut-collapse completeness are both
open. The combined boundary-obstruction completeness programme is recorded
in `oml_global_integration.md`. `ODBCRegimes.lean` verifies only the
conditional regime-packaging implications.

Campaign 7 finds no mathematical retraction but confirms that no
counterexample gate has passed beyond finite tame controls and that BOC is
not yet a decisive theorem. The linked chain had 44 meaningful iterations
before the audit, so the mandatory 60-iteration threshold requires
continuation.

Campaign 8 proves that locally countable finite-arity CSS always globalizes;
genuine N-G needs an uncountable-incidence hub, infinite-arity constraint, or
coarse coordinate. An exhaustive 44-event selector proxy leaves 24 of 496
pairs. The explicit selectors `0x000f` and `0x3300` yield independently
verified `P(2)xP(2)`, `P(2)xP(3)`, and `P(3)xP(2)` centre-free
five-block OMLs. The smallest has 24 points and 116 events. All finite state
gates pass and the models are Phi-tame. Arbitrary-base two-coordinate
latticehood and maximal-block classification remain open.

Campaign 9's outsider-extremality gap is now closed. Per-block floor/ceiling
domination removes outsider coefficients, and all 16 truth-region kernels
through `P(4)xP(4)` pass independently; the binding model has 1220 events
and 744,810 unordered input pairs. Hence the arbitrary orthogonal two-atom
family is a concrete sigma-complete OML for every concrete Boolean
sigma-algebra pair. Exact maximal blocks, centre, state classification/order
separation, and unconditional Phi remain open. Conditional on those state
gates, global states have three alternative branches (`q`, `r`, neither),
so the class is Phi-tame.

Campaign 10 tests that pair. The literal binary substitution has 648 events
but misses an explicit disjoint union and has two incomparable upper bounds.
Canonical closure gives an independently verified 1128-event centre-free
nine-block OML; four new mixed blocks fill its coordinate relation, so it is
Phi-tame. A diagonal-overlap variant closes from 264 to 392 events and also
gives a centre-free nine-block OML, but its jointly charged conditional
relation remains exactly diagonal. Thus mixed cuts need neither centralize
nor rectangularize conditional relations. A single edge with
`R_fa=closure(R_sigma)` is nevertheless Phi-tame by density. The frontier is
distributed assembly over an explicit uncountable-incidence hub.

Campaign 11 writes the minimal hub exactly as the punctured-Cantor star:
every countable subnetwork has a sigma-section, the full network has none,
and each local sigma relation is dense in its finitely additive relation.
Local diagonal Borel edge cells realize these traces. A shared faithful
countably generated hub cannot enter a concrete sigma-complete OML: two
puncture cells give different intrinsic countable meets for one shrinking
clopen basis. The exact assembly gate is MBRC over all maximal blocks using
L-relative sigma-states; its failure need not be finitely witnessed. Live
escapes are distributed nonseparating quotients or an uncountably generated
separating boundary without a countable puncture basis.

Campaign 12 closes the countably generated quotient escape: every sigma-state
on a faithfully sigma-embedded countably generated boundary extends to an
order-separated sigma-complete OML. In contrast, the product sigma-algebra
on `2^{omega1}` has only countable-support events and admits faithful
puncture embeddings into `P(H\{i})`; evaluation at `i` extends finitely but
not sigma-additively by Ulam's ZFC theorem. This gives an exact Boolean
CSS/no-GS atlas with compatible fa tuples. Its common boundary is central in
the raw and finite algebraic OML closure, but an arbitrary sigma-completion
may introduce de-centralizing joins and remains unaudited. Compatible-face
state equality identifies literal cuts; incompatible activation patterns
remain the viable transport mechanism.

Campaign 13 closes only the unconditional omega-one completion route. If the
hub and puncture blocks are state-normal there are no sigma-states; partial
normality creates charged ambient join defects; loss of hub normality destroys
global point classification. A forbidden finite cylinder necessarily has
meet zero, and every nonzero event must admit an off-cylinder sigma escape
state, so no event can activate it. Face-local MBRC remains open because all
nonnormal escape states may lie off the cylinder. The exact next gate is a
finite order-separated OML cell directly enforcing the incompatible state
implication `111 => q=r` without an activation event.

Campaign 14 closes that finite semantic gate: the five odd atoms of the
centre-free concrete 5-loop pentagon give exactly the activated rows
`11100,11111`, all aggregate off-activation output profiles, no activation
event, and an off-activation point charging every nonzero event. The model has
22 events, 11 states, and five maximal blocks. It is finite and Phi-tame. The
new frontier is preservation under two-cell mixed-cut completion and then
uncountable assembly; a literal embedded-H4 presentation is not claimed.

Campaign 14 then supplies the stronger literal presentation. A 56-event,
24-atom centre-free concrete OML contains the horizontal `MO3` generated by
three activation events and realizes every five-bit profile except the two
activated mismatches. Two cells pasted over the fixed ten-event interface
need eight concrete orthogonal repairs and close to a 110-event centre-free
OML. At three cells the verified counts are 148 raw events, 24 repairs, 172
completed events, 42 maximal blocks, and 136,556 fibre points; the joint
activated relation stays diagonal and no pairwise joint private boundary is
reconstructed. The polynomial formulas are verified only for k<=3. The live
frontier is their arbitrary-k proof and the countable-disjoint-union closure,
where new infinite-support events may reconstruct the boundary.

Campaign 15 proves the stronger one-hub conclusion: for every nonempty index
set, the normal-form union is already a concrete sigma-complete OML, every
orthogonal family has finitely many nonzero terms, and every finitely additive
two-valued state is sigma-additive. Thus `St_fa=St_sigma` and Phi holds for the
entire support-two architecture. The puncture construction necessarily needs
the two-dimensional family `r_{i,alpha}` with fixed-i commuting columns. Its
stripped K22 coordinate core closes from 50 to 82 events but remains a
nonlattice at an explicit crossed rectangle; K23 and K32 fail likewise. The
next exact gate is the full four-cell 2x2 conditional grid and an explicit
rectangle-repair calculus.

Campaign 16 shows that the full conditional grid does not repair the cut:
its 198 raw events close orthogonally to 230 events on 6,186,568 compatible
points and still have the same two incomparable rectangle upper bounds.  The
cell relations, activated diagonal, activation nonevents, and off-cylinder
escape all survive.  On the stripped sixteen-profile core, all four possible
first rectangle traces remain nonlattices.  Two explicit iterated branches do
reach 1296- and 3456-event concrete OMLs, but both reconstruct
`Bool(q0,q1)` and all four edge coordinate-pair algebras.  These branches do
not prove reconstruction unavoidable.  The exact finite frontier is the
symmetry-reduced completion search subject to keeping both same-side Boolean
boundaries absent; a surviving branch must then be lifted to the full cell
carrier.

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
