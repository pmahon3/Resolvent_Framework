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

Campaign 17 exhausts that stripped problem. Interval-complete branching over
nine symmetry classes and twenty candidate edges reaches no lattice before a
literal same-side atom is forced. Hence every OML subfamily of `P(2^4)`
containing all four K22 edge algebras reconstructs `Bool(q0,q1)` or
`Bool(r0,r1)`. This is an exhaustive finite theorem, not a theorem about the
full conditional carrier: an event may have the required macro trace while
splitting auxiliary points inside an ambiguous profile. The frontier is the
smallest such fine-fibre repair and whether mixed cuts saturate it back to a
macro boundary.

Campaign 18 refutes immediate saturation through two depths. The first
ambiguous interval has 672,800 free points. A one-sided 64-point whole-class
repair closes to 310 events, while the symmetric 128-point repair closes to
256; both preserve the distributed boundaries and activation escape but stay
nonlattices. The symmetric branch's smallest secondary whole class has four
points. Adding it closes to 492 events with the same controls still intact,
but the next interval widens to 1,666,232 points. Blind branching is therefore
replaced by the exact Campaign-19 question: find a recurrence/monotone
invariant for factor-type repairs, or a finite grammar leading to a terminal
OML.

Campaign 19 refutes the proposed recurrence state. The third gap has
1,666,232 points in 346 proper Cartesian pieces; a two-point repair closes
492 to 558 events, after which the fourth gap shrinks to 205,248 points and
again has whole-class minima. The nonisomorphic 468- and 492-event sibling
families have identical complete next-gap masks, so even the exact gap is not
a Markov state. All selected closures remain nonlattices while preserving
both distributed boundaries and activation escape.

Because the full-grid carrier is finite, every unrestricted fine-repair
chain terminates and countable orthogonal closure is already finite closure.
Every same-carrier concrete OML completion contains a terminal repair family.
The exact finite question is therefore T-FIN: must every terminal reconstruct
one same-side Boolean boundary or create a nonzero activation-supported
event? Separately, every coordinate-closed completion reconstructs a side by
the exhaustive `P(16)` theorem; its only larger-carrier escape uses a
non-profile-measurable join. Neither result closes larger representations or
the uncountable sigma-assembly gate.

The first theorem-extraction census at 558 events finds 90
profile-measurable events and 127 unordered join-failing pairs among them;
all three selected joins remain least. One inherited join has both fibre
hulls and their difference as events while splitting twelve profiles, so
hull availability alone does not force reconstruction. Every preserving
completion nevertheless needs some proper fibre splitter. The live invariant
is no longer simple hull incidence: seventeen split signatures are
nonlaminar, and the nine event-valued hull gaps never differ by one fibre.
Instead the stage contains a 336,404-point same-side lattice meet equal to a
whole `0101` profile fibre plus the four-point second repair escape. The next
exact gate is the admissible interpolation interval above this irreversible
fattened-fibre meet core—not another selected repair depth.

That enlargement interval is now executable-certified as the disjoint union
of 160 whole activation/local-state macrofibres (55 in profile `0100`, 49 in
`0110`, 56 in `0111`). This yields a unique 160-bit normal form only under an
explicit macrofibre-saturation hypothesis. It is not a terminal repair
grammar: future non-profile repairs may split those pieces, and the
unrestricted interval has `2^1019276` subsets. The next discriminating gate
is therefore saturation preservation versus an explicit partial-macrofibre
splitter.

The existing fourth-gap control cannot decide that gate: all of its profiles
have `q0=1`, so its unique minimum selector and the entire gap are disjoint
from the `(q0,q1)=(0,1)` fattened-meet interval. A fourth selected repair is
therefore suspended unless its closure is tied to a stated cross-interval
provenance theorem.

The terminal theorem-extraction layer is now stronger. On each side the four
literal-cylinder residues have event-valued row, column, and total unions;
gate A is equivalent to any residue being an event, so an avoiding terminal
has no event singleton or triple residue union. Both sides together give 32
ternary meet-trace symbols, but no lifting theorem makes that shadow signature
a complete terminal CSP. The live exact alternatives are residue-shadow
lifting versus a coupled-residue-square collapse theorem using the edge cells
and a necessary non-profile join.

The named stage-558 provenance stabilizer has order four and 84 orbits on the
160 pieces. Exact single-cell incidence exhaustion proves there are no hidden
cell-level automorphisms under the relevant colours. Full-grid promotion still
requires intrinsic recognition of the four embedded cell copies.

Bare residue-square collapse is refuted by the carrier-minimal six-event
`MO2` control. A sharper sufficient condition survives: if joins of saturated
events have event-valued existential profile hulls (PJH), saturated events
form an OML quotient on the sixteen profiles, so the exhaustive core theorem
forces a same-side boundary. Any preserving terminal must fail PJH. The next
exact test is certificate-local hull eventhood along the finite `P(16)`
forcing DAG, not another selected repair.

That certificate-local test is now an explicit first-defect atlas. The
exhaustive DAG has 31 internal states, 24 interval types, 64 candidate hull
edges, and 17 reconstructing terminals. A self-auditing replay certifies an
actual failed pair and family hash at every internal node and resolves every
edge. Hence any preserving same-carrier terminal must sustain a first
nonevent hull of one recorded type. Realizability or collapse of those defect
types in a gate-B-avoiding terminal is open.

The lower endpoint of an interval cannot be a first defect, leaving 33
candidate occurrences: three at the root and thirty one-fibre upper choices.
An exact post-hoc action audit finds the lex atlas has trivial stabilizer in
the full 128-element coordinate group, even after forgetting witness pairs.
All sixteen profile fibres occur among the one-fibre candidates. Thus neither
coordinate symmetry nor profile location compresses the remaining atlas.

Every possible first-defect join contains the full pullback of a lower word
with at least three profiles. Exact state counts show that every profile fibre
has points outside each row activation cylinder. Hence the first defect join
itself cannot fire gate B. This does not control later events derived from the
split fibre, so terminal gate-B avoidance remains open.

The minimal split-profile census changes the frontier. Of the thirty binary
defects, four yield terminal seventeen-point concrete OMLs without repairing
the nonevent hull or reconstructing either boundary. Each is
`B_9 x MO2 x MO2`, with `18432` events and centre size `2048`; the other
twenty-six initial closures remain nonlattices. Profile-only collapse is
false, but the surviving controls are not admissible and omit the original
conditional-cell couplings. Restoring those couplings is the next gate.

The first physical coupling rung also survives. Restoring every event of cell
00 on an exact 892-point quotient gives an 18496-event concrete OML with
trivial centre, separating point evaluations, row-0 activation escape, both
same-side boundaries unreconstructed, and the node-6 PJH defect intact. Thus
essential irreducibility plus one conditional cell is insufficient. The
finite OML is `Phi`-tame and omits three cells; cell 01 is the next gate.

Cell 01 also passes. The exact same-row marginal has 9928 points, faithfully
embeds both 56-event cells, and closes to a centre-free 18554-event concrete
OML. The PJH defect, both boundary gaps, and row-0 activation escape persist.
Same-row coupling is therefore not the collapse mechanism. Transverse cell
10, which introduces row-1 activation through shared `r0`, is next.

A parallel T-FIN impossibility ledger is now active. Existing controls refute
profile-only collapse, one-cell/centre forcing, same-row coupled collapse,
automatic PJH repair, and point-separation obstructions. T-FIN itself is not
refuted because no control contains the full four-cell root. Any live proof
must use transverse/full-grid coupling, maximal-block incidence, or genuinely
global state data.

The transverse pair also survives. The exact cells-00/10 marginal has 49730
points and closes to a centre-free 18560-event OML with both activation
escapes, both boundary gaps, and the unchanged PJH defect. Thus neither
same-row nor transverse two-cell coupling supports a T-FIN proof. The first
unresolved coupling is the three-cell corner `{00,01,10}`.

The exact same-row node-6 meet is now serialized. On the 9928-point quotient,
`q0^c meet q1` is the pullback of `{0100,0101,0110}` and has 2130 points;
the remaining whole `0111` fibre has 352 points and is not an event. Restoring
cell 01 leaves the meet unchanged. This refutes forced strict same-row
advance, not weak monotonicity and not a transverse/three-cell growth theorem.
**Executable verified**, payload `2367e72c...`.

The transverse meet is equally stable: on the 49730-point quotient it is the
`8560`-point `0x70` pullback, while the entire `2880`-point `0111` fibre is a
nonevent. Cell 10 adds no increment. Therefore neither second-cell incidence
orientation forces strict advance; the three-cell corner is the first live
growth configuration. **Executable verified**, payload `75f69aab...`.

The three-cell corner survives every audited finite gate. The exact
cells-00/01/10 quotient has 553648 points and closes through a canonical
17-atom normal form to a centre-free 18618-event concrete OML. Both
activation escapes and boundary gaps persist, as do the PJH defect and the
`0x70` meet; its whole 25344-point `0111` residue remains a nonevent. All
3462948 new-versus-all cuts pass. **Executable verified**, payload
`0957dde3...`; OML and centre reductions use recorded **Hand proved** lemmas.
Cell 11 is only existentially completable, not embedded. Its actual event
algebra is the next and final finite coupling gate.

That final finite gate passes. On the exact 6186568-point full four-cell
carrier, interned macro-fibre MDD closure completes at 18676 events and is a
centre-free concrete sigma-complete OML. It contains the independently
constructed 230-event root; all 4556944 new-versus-all cuts pass. Neither
boundary reconstructs, no nonzero event lies in either activation cylinder,
and the PJH defect plus the `0x70/0x80` meet-residue pattern persist. Point
states order-separate. **Executable verified** plus MDD/OML/centre bridges
**Hand proved**, payload `7dc91cd1...`.

Therefore fixed-carrier T-FIN is **Refuted**. The finite OML remains
`Phi`-tame, so the programme now takes the counterexample route: controlled
finite-support and sigma-complete assembly, not further finite repair depth.

Campaign 20's first assembly gate passes. Two adjacent full-cycle rectangles
sharing the entire conditional cell have an exact 211897540016-point
compatible carrier with onto projections. Exhaustive MDD saturation proves
that each completed copy has exactly the 56 original shared-cell traces;
hence their images intersect exactly in the declared cell and no extra event.
**Executable verified**, payload `d51b57b8...`. Closure/latticehood of their
union remains **Open** and is the next test.

The exact union carrier has seven cells, 23998 nonempty macro fibres and
211897540016 points. A naive global MDD lift costs about 7.17 GB before
closure, so blind computation is stopped. First-round symbolic analysis finds
172787 disjoint cross-copy pairs, including 123440 genuinely mixed shapes;
OR-tags require AND-rectangle complements. The coarsest 2257 shadow types
close, but literal coordinate-hull realizability fails on the 71-state trace
of event `0x22`. The missing cylinder has the sharp unique old bracket
`0x404 < C < 0x505`; for the original pulled event the left lower shadow is
`0` and the least old upper is `0x505`. **Executable verified** with hostile
review. The exact theorem is now the kernel-retraction criterion: a finite old
OML embeds conservatively iff every new event has a greatest old lower shadow.
**Hand proved.** Exhausting this kernel condition for one-step mixed events is
the live finite-support gate. The first 100 symbolic kernels pass (60 old
cores, 40 absent cores with unique greatest lower). The 91-atom replay agrees
and cuts exact tests 205.15-fold. The former 23.1-billion and 282.1-million
projections used the rectangular pre-admissibility ceiling. Exact
disjoint-existential filtering leaves 55722 live `(A,U)` kernels, with 5070702
possible atom visits and at most 10141404 uncached atom-plus-accumulator
bad-mask calls. Equivalently the complete inverted target is the strict
atomic-extension `Bad_A(D)` join-defect atlas. **Open**;
arbitrary-depth closure is also **Open**.

An eager complete retained-event-by-91-atom bad-mask descriptor census was
stopped at a 12-minute feasibility cap after reaching roughly 1 GiB RSS,
without a receipt or mathematical verdict. **Executable verified** operational
observation only. The next discriminating representation is per-shared-state
interning of exact restricted-root trace classes for the strict atomic horns,
first on 8--16 deterministically spread states; no complete atlas run is authorized until
that compression is measured.

That bounded class census now passes after hostile repair. Across 12
deterministically spread shared states and both orientations, 448200 exact
horn-role trace words intern to 2740 per-state classes (74--136 each). The
fixed old OML has 1433764 strict atomic overshoot horns. **Executable
verified** by a single producer under two hash seeds, payload `d8290f39...`.
This is not a global-vector compression theorem. The next discriminating run
is the grouped-versus-scalar streaming differential over every admissible `U`
for 64 prefix plus 64 spread retained events per orientation.

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
