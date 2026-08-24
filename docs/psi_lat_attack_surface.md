# Attack surface for `Psi_lat`

*Scouting audit, 2026-08-06, branch
`oml-descent-sigma-essential-reduction`. Hand mathematics and literature only:
no Lean run, no finite census, and no attempt to decide `Psi_lat`. The paper of
record and its dependency path were read but not edited. Ledger:
[`psi_lat_attack_surface_ledger.md`](psi_lat_attack_surface_ledger.md).*

## Executive verdict

**ROUND KILLED AS FRAMED; THE OPEN QUESTION SURVIVES.**
`[TYPE-CHECK — DECISIVE]` Vorob'ev's universal marginal-extension theorem is
classical and directly present in the contextuality literature, but it applies
to a hypergraph whose vertices are random variables/measurements and whose
hyperedges are joint-marginal contexts. The proposed trace hypergraph has
carrier cells as vertices and events as hyperedges. These are different
objects. Moreover, the paper's `Phi` concerns **two-valued** sigma-additive
states, which need not be Dirac, whereas the proposed cell polytope describes
mixtures of carrier points. Thus

> visibility = cell-realizability

is not a finite-trace formulation of `Phi` without a separate theorem saying
that all relevant sigma-additive two-valued states are Dirac. That theorem is
available for the product-Ulam witness and false for concrete OMLs in general.

`[REPO + HAND — VERIFIED]` The useful residue is exact. Latticehood eliminates
missing countable monotone limits, and singleton quarantine eliminates the
product-Ulam rigidity mechanism. Concreteness eliminates absolute
stateless/Kochen--Specker obstructions. What remains is the already-banked GSD
problem: a coherent global finitely additive state for which independently
available local sigma-replacements cannot be selected to agree with one common
boundary trace. Calling that *probabilistic holonomy* is harmless only if it is
defined to mean this GSD obstruction; a cell-polytope gap is not an exhaustive
characterisation.

`[OPEN]` Generic “sigma-closure triangulates” is false even for complete OMLs:
the banked five-loop completion retains its cyclic block pasting. Whether an
**admissible concrete** flat/coarse pasting exists remains open. Finite sites
are quarantined, so any live carrier must use an infinite coarse boundary whose
information survives the quotient by countable sets.

## Evidence grades and level firewall

Every substantive result below carries one of these grades.

- **`[LITERATURE — VERIFIED]`**: checked in a primary source, or explicitly
  identified as a modern restatement when the primary uses older vocabulary.
- **`[REPO — VERIFIED]`**: already proved or audited in the linked repository
  source. A Lean theorem is described as such, but no Lean work was done here.
- **`[HAND — PROVED]`**: elementary proof supplied in this note.
- **`[CONDITIONAL — PROVED]`**: theorem proved with its missing bridge stated as
  a hypothesis.
- **`[REFUTED]`**: an explicit counterexample or prior banked result fires.
- **`[TYPE/SCOPE ERROR]`**: the proposed theorem changes its mathematical
  object, codomain, or quantifiers.
- **`[SEARCH-NEGATIVE]`**: no source was located in the bounded search; this is
  not a nonexistence theorem.
- **`[OPEN]`**: neither direction is established.

Three combinatorial objects occur, not two.

1. The **block nerve** has maximal Boolean blocks as vertices and nontrivial
   overlaps as edges. Connectedness and cycles here describe the atlas.
2. The prompt's **event--cell incidence hypergraph** for a finite family `F`
   has realized Venn cells (or points) as vertices and the events of `F` as
   hyperedges. Event probabilities are sums of weights over these vertices.
3. The **Vorob'ev marginal-scenario hypergraph** has random variables or
   measurements as vertices and jointly distributed contexts as hyperedges.
   Its data are probability distributions on products of outcome sets.

`[TYPE-CHECK — VERIFIED]` The first and third are already distinguished in the
corpus. The second is not the third merely because both are called
hypergraphs. Any bridge used below is displayed explicitly.

## Definition anchors

`[REPO — VERIFIED]` The following are the definitions used in this audit; none
is replaced by a prompt-level paraphrase.

| Object | Exact repository anchor |
|---|---|
| concrete sigma-class, state, sigma-state, Dirac | [`sigma_essential_body.tex`](../papers/sigma_essential/sigma_essential_body.tex), Introduction, lines containing the first display and the paragraph after it |
| finite coherence | same file, `def:coherence` |
| sigma-essential contextual state and essential irreducibility | same file, `def:sigma-essential` |
| segregation | same file, `rem:segregated` |
| `Adm`, `Phi`, finite trace quantifiers | same file, Discussion immediately before `rem:strength` |
| `Psi_lat` | same file, `q:oml` |
| witness mechanism | same file, `def:carrier`, `lem:table`(IV), `cor:incompat`, `thm:rigidity`, `rem:coherence-location` |
| exact descent formulation | [`relational_boundary_descent.md`](../notes/open_questions/oml_attack/relational_boundary_descent.md), Theorems 4.2--4.3; [`oml_global_integration.md`](../notes/open_questions/oml_attack/oml_global_integration.md), section 1 |

The paper's exact finite-trace statement is

\[
 \forall B\in\operatorname{Fin}_{\perp}(L)\ \forall s\in\operatorname{St}(B),
 \quad
 (\exists\mu\in\operatorname{St}_{fa}(L),\ \mu|_B=s)
 \Longrightarrow
 (\exists\nu\in\operatorname{St}_{\sigma}(L),\ \nu|_B=s).
 \tag{Phi}
\]

The two global states may differ; only their values on the finite,
orthocomplement-closed `B` are fixed.

## Phase 0 — kill checks and the exclusion lemma

### 0a. Literature

#### Vorob'ev and Kellerer

`[LITERATURE — VERIFIED]` Vorob'ev's exact finite theorem is stronger and more
precise than the slogan in the prompt. Let `K` be a finite complete complex,
attach a finite outcome set to each vertex, and prescribe probability measures
on the coordinate sigma-fields indexed by the faces, agreeing on every common
coordinate sigma-field. Vorob'ev calls `K` *regular* when it can be reduced to
the empty complex by repeatedly deleting the private vertices of an extreme
maximal face. His main theorem says:

\[
 K\text{ is regular}
 \quad\Longleftrightarrow\quad
 \text{every consistent family of those probability marginals extends}.
\]

This is the universal statement: a nonregular complex has at least one bad
compatible family, not that every family on it is bad. The statement and the
original reduction definition are on the
[primary MathNet record](https://www.mathnet.ru/eng/tvp4710); the English DOI is
[10.1137/1107014](https://doi.org/10.1137/1107014).

`[LITERATURE — VERIFIED AS MODERN TRANSLATION]` Modern terminology identifies
Vorob'ev regularity with alpha-acyclicity, equivalently a running-intersection
ordering; for reduced clique hypergraphs this is the chordal/triangulated
condition. The contextuality review of Budroni *et al.* states the acyclic
sufficiency theorem, identifies vertices with measurements and hyperedges with
contexts, and credits Kellerer's two 1964 papers as independent proofs; see
[Kochen--Specker Contextuality, section V.B.2](https://arxiv.org/abs/2102.13036).
So the acyclic context-marginal engine is already folklore in precisely the
literature named by the prompt.

`[LITERATURE — VERIFIED; SLOGAN CORRECTED]` Kellerer's
[`Maßtheoretische Marginalprobleme`](../notes/literature_review/literature/kellerer_1964_mass_theoretic_marginal_problems.pdf)
is broader than the clean combinatorial slogan and its signed and positive
theorems must not be interchanged.

- Page 169 says that, for the unrestricted problem in **general measures**,
  compatibility is sufficient.
- Satz 2.2 (page 178) constructs a bounded general measure with prescribed
  compatible bounded general marginals by an inclusion--exclusion formula.
  Here “general” permits signed measures; this is not by itself a probability
  gluing theorem.
- Satz 4.5 (page 197), for finite products of separable sigma-fields, gives a
  necessary-and-sufficient integral inequality for a bounded positive measure
  dominated by a rectangular-normal upper measure and having the prescribed
  marginals.

The bibliographic record is [EuDML](https://eudml.org/doc/161128). Kellerer's
second 1964 paper is *Verteilungsfunktionen mit gegebenen
Marginalverteilungen*, volume 3, pages 247--270,
[DOI 10.1007/BF00534912](https://doi.org/10.1007/BF00534912). Thus it is fair,
following the modern review, to credit Kellerer with an independent acyclic
positive-extension result. It is not fair to cite Satz 2.2 alone as
“compatible probability marginals always glue.” The exact universal `iff` was
verified directly in Vorob'ev.

`[LITERATURE — VERIFIED]` Abramsky--Brandenburger formulate contextuality as
failure of a compatible family of distributions on a measurement cover to
have a global section; see
[The Sheaf-Theoretic Structure of Non-Locality and Contextuality](https://arxiv.org/abs/1102.0264).
This is a modern home for Vorob'ev's engine, but its contexts are measurement
sets, not maximal OML blocks automatically and not event--cell incidence
hyperedges.

`[SEARCH-NEGATIVE]` Searches for combinations of `Vorob'ev`, `Kellerer`,
`decomposable`, `orthomodular`, `concrete logic`, and state extension located no
paper applying the decomposable-marginal theorem to the paper's `Phi`, nor a
published meet-as-chord theorem for concrete sigma-complete OMLs. De
Simone--Navara--Pták study genuine state extension questions in
[Extending states on finite concrete logics](https://arxiv.org/abs/math-ph/0311012),
but their finite concrete-logic results are not this sigma-level `Phi` problem
and do not provide the proposed bridge. This bounded negative agrees with the
earlier [`latticehood_prior_art.md`](latticehood_prior_art.md) audit; it is not
a claim that no such source exists.

#### Countable orthocompleteness

`[LITERATURE — VERIFIED]` Holland's theorem is the exact citation:

> S. S. Holland, Jr., “An `m`-orthocomplete orthomodular lattice is
> `m`-complete,” *Proc. Amer. Math. Soc.* 24 (1970), 716--718,
> [DOI 10.1090/S0002-9939-1970-0256949-8](https://doi.org/10.1090/S0002-9939-1970-0256949-8).

The repository already checked it against Kalmbach, Chapter 1 section 4; see
[`site_regularity_orthomodular_completions.md`](site_regularity_orthomodular_completions.md),
the paragraph immediately before Phase 3 and its source list.

`[HAND — PROVED]` For the countable case there is also a direct proof. If
`x_1 <= x_2 <= ...`, put

\[
 d_1=x_1,\qquad d_{n+1}=x_{n+1}\wedge x_n'.
\]

Orthomodularity gives `x_{n+1}=x_n join d_{n+1}` and the `d_n` are pairwise
orthogonal. Sigma-orthocompleteness supplies `x=join_n d_n`. Each `x_n` is the
corresponding finite join, so `x` is an upper bound; every common upper bound of
the `x_n` bounds every `d_n`, hence bounds `x`. Thus `x=sup_n x_n`. Complements
give decreasing infima. Applying this to the increasing finite joins of an
arbitrary countable family yields its supremum, and complements yield its
infimum. Therefore a sigma-orthocomplete OML is countably complete.

### 0b. Exclusion accounting

#### Countable missing limits, and the actual s11 mechanism

`[HAND + LITERATURE — PROVED]` Latticehood plus the paper's countable
orthogonal-join closure excludes missing countable monotone suprema and infima
by the preceding argument. The concrete formulation is already banked in
[`state_of_play_2026-08.md`](state_of_play_2026-08.md), “Concrete OML
carriers.”

`[REFUTED AS A DERIVATION; REPO CORRECTION]` This is **not** the reason s11
excludes the product-Ulam kill mechanism. The actual witness already has all
countable orthogonal joins. Its failure is the binary meet of `A_1,A_2`: by
`cor:incompat`, their lower bounds are all countable subsets of
`M times {1}`, with no maximum. No countable subfamily is cofinal, since the
union of countably many such lower bounds is countable and misses another
singleton. Countable monotone completeness therefore never reaches the absent
meet.

`[REPO — VERIFIED]` The banked s11 theorem is **T1, singleton quarantine**, in
[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md),
section 9c. If every point of `A intersection B` lies in some carrier element
below both `A` and `B`—in particular, if all those singletons are events—then
the lattice meet contains every point of the set intersection and hence equals
that intersection. The pair is compatible. The product-Ulam engine needs the
opposite conjunction: singleton-level Ulam rigidity below an incompatible
overlap. T1 proves that conjunction unavailable on lattices. This is the honest
corollary; the monotone-limit proof and T1 are distinct mechanisms.

#### Absolute statelessness

`[HAND + REPO — PROVED, NARROW SCOPE]` Every concrete logic carries every
point evaluation `delta_omega`, and each is a sigma-additive two-valued state.
Hence a stateless Greechie/Navara lattice cannot itself be concrete. This is
exactly the distinction made near `rem:quotient`: the quotient artifact may
have no sigma-state, but it is not concrete.

`[REFUTED IF READ BROADLY]` Concreteness excludes only the **absolute**
Kochen--Specker mechanism “there is no two-valued state.” It does not exclude a
relative finite-pattern obstruction: there may be many Diracs while none
matches a prescribed trace. The product-Ulam carrier is the repo's example.
Accordingly, “no KS-type obstruction can operate” is safe only with
“stateless” made explicit.

#### Segregation and the block nerve

`[REFUTED]` Non-segregation does not imply that the nontrivial-overlap block
nerve is connected. The definition at `rem:segregated` has no nerve
quantifier. Its exact negation is operational: some countable orthogonal family
has no single containing block whose sigma-additive two-valued states rescue
all of the required finite traces. It excludes that blockwise rescue
mechanism—nothing more graph-theoretic.

`[HAND — COUNTERMECHANISM]` Attaching a horizontal-sum component to a carrier
with an existing non-segregated family leaves the bad family and all blocks
that can contain it in its original component, while adding an isolated
component to the nontrivial-overlap nerve. Thus the rescue failure can coexist
with a disconnected nerve. Separately, `MO_omega` in
[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md),
section 9a, already shows that even trivial centre does not force that nerve to
be connected: its blocks meet only at the bounds.

### Phase-0 verdict: what genuinely survives

`[REPO — VERIFIED]` In the lattice scope, every failure can be put in the
cluster/GSD form already proved in
[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md),
sections 9b and 11:

- a finite orthocomplement-closed trace has an actual global finitely additive
  two-valued witness `mu`;
- after in-block finite meets, its value-one data reduce to at least three
  pairwise incompatible, pairwise set-intersecting events (two blocks are
  Dirac-rescued by `2BR`);
- sigma-additivity is already a blockwise property, but no family of blockwise
  sigma-states both realizes the prescription and agrees on overlaps; in the
  exact GSD formulation, no choice matches one common global `mu` on all block
  boundaries.

`[OPEN]` The exclusions do not prove that every such cluster is rescued. They
also do not prove that the only remaining mechanism is a cell-polytope gap.
The proved survivor is **distributed boundary descent failure**. “Probabilistic
holonomy” is a useful name for that exact obstruction, not yet a theorem with
independent content.

## Phase 1 — `Phi` failure is not block-local

### Local finite trace lemma

`[HAND — PROVED IN THE `Psi_lat` SCOPE]` Let `L` be a concrete sigma-class
which is a lattice, let `M` be a maximal block, let `mu` be a finitely additive
two-valued state on `L`, and let `F subset M` be finite. By the block theorem in
[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md),
section 9c (A2), `M` is a sigma-field of subsets of `Omega`. Form the finite
Boolean algebra generated by `F` inside `M`. The restriction of `mu` is an
ultrafilter on this algebra, so it charges exactly one of its nonzero atoms.
Choose `omega` in that atom. Then

\[
 \delta_\omega(A)=\mu(A)\qquad(A\in F),
\]

and `delta_omega|M` is sigma-additive. Equivalently, intersect the
`mu`-value-one side of every member of `F`; finite additivity makes the
resulting Boolean atom nonempty.

`[SCOPE NOTE]` If “block” means the paper's maximal **Boolean** subalgebra, the
same finite-algebra proof needs no ambient latticehood. If it means the formal
`IsMaxBlock` object—maximal pairwise-compatible family—then `MeetsExist` is the
proved hypothesis that turns it into a Boolean sigma-field. This is why the
formal theorem below carries that hypothesis. The two readings must not be
silently exchanged.

### Descent, not independent local existence

`[REPO — VERIFIED]` The blockwise-sigma theorem says that a global state is
sigma-additive exactly when every block restriction is. The local lemma
therefore removes independent local feasibility as an obstruction. It does
**not** let independently selected Diracs glue: they may disagree on block
overlaps. The remaining problem is to select local sigma-states that all match
one common boundary trace.

`[REPO — ALREADY EXACTLY GSD]` This is not a new decomposition. Theorem 4.3 of
[`relational_boundary_descent.md`](../notes/open_questions/oml_attack/relational_boundary_descent.md)
proves

\[
 \Phi(L)\quad\Longleftrightarrow\quad \operatorname{GSD}(L),
\]

where GSD quantifies over a coherent finite prescription, chooses one global
`mu`, and requires at every block a local sigma-lift matching `mu` on that
block's entire boundary. The integrated equivalences

\[
 \Phi\iff\mathrm{GSD}\iff(\mathrm{ODBC\!\!-S}\wedge\mathrm{CODBC})
 \iff\text{coarse ODBC}
\]

are recorded in
[`oml_global_integration.md`](../notes/open_questions/oml_attack/oml_global_integration.md).
Separate local lifts are explicitly listed there as insufficient.

`[REPO — LEAN-VERIFIED, READ ONLY THIS ROUND]`
[`BoundaryDescent.lean`](../formalization/QuerySystem/QuerySystem/BoundaryDescent.lean)
already contains the positive kernel:

- `finite_trace_dirac` proves the local point-realisation theorem under
  `MeetsExist`;
- `glueBlockStates` glues an overlap-compatible family of block sigma-states;
- `finite_interface_quarantine` proves `Phi` when every raw overlap interface
  is finite.

No formal file was changed or executed.

## Phase 2 — visibility and the witness calibration

### The cell polytope

`[HAND — DEFINITION]` Enumerate a finite event family
`F={A_1,...,A_n} subset L`. For `epsilon in {0,1}^n`, put

\[
 C_\epsilon=\bigcap_{i=1}^n A_i^{\epsilon_i},\qquad
 A_i^1=A_i,\quad A_i^0=A_i',
\]

where this is the set-theoretic intersection in `Omega`, whether or not it is
an element of `L`. Let

\[
 S_F=\{\epsilon:C_\epsilon\ne\varnothing\}.
\]

The **cell polytope** is

\[
 P_{cell}(F)=\operatorname{conv}(S_F)
 =\left\{\left(\sum_{\epsilon_i=1}p_\epsilon\right)_{i=1}^n:
 p_\epsilon\ge0,\ \sum_{\epsilon\in S_F}p_\epsilon=1\right\}.
\]

It is exactly the set of `F`-traces of finitely supported ordinary probability
measures on `Omega`. Representatives may be chosen one per nonempty cell.

`[HAND — PROVED]` For a zero--one vector `x`,

\[
 x\in P_{cell}(F)\quad\Longleftrightarrow\quad C_x\ne\varnothing.
\]

Indeed, an average of zero--one vertices can have an extreme coordinate `0` or
`1` only if every positively weighted vertex has that same coordinate. Thus a
zero--one cell-realizable trace is exactly a trace realized by a carrier Dirac.

### What “visibility polytope” can honestly mean

`[TYPE-CHECK — CORRECTED DEFINITION]` “Every constraint expressible in `L`” is
not generally a finite list, so it does not canonically define a polytope. Two
objects must be separated.

For a chosen finite coordinate set `E subset L`, let `Q_E` be the finite linear
relaxation with coordinates `y_a in [0,1]` and every applicable relation

\[
 y_0=0,\quad y_1=1,\quad y_{a'}=1-y_a,\quad
 y_{a\vee b}=y_a+y_b\ (a\perp b),\quad
 y_a\le y_b\ (a\le b),
\]

whenever all displayed coordinates are in `E`. Meet and join augmentations add
their order relations; for a compatible pair the Boolean disjoint
decompositions add the familiar equalities. Its projection to `F` is a genuine
finite **visibility polytope** `P_vis(E;F)`. Requiring every `y_a` to be zero or
one gives a finite feasibility set, not a convex polytope.

The exact, all-of-`L` objects relevant to the paper are instead

\[
 T_{fa}^{01}(F)=\{(\mu(A_i))_i:\mu\in\operatorname{St}_{fa}(L)\},\qquad
 T_{\sigma}^{01}(F)=\{(\nu(A_i))_i:\nu\in\operatorname{St}_{\sigma}(L)\}.
\]

The analogous traces of `[0,1]`-valued finitely additive states form a convex
visibility body, but it need not be a finitely described polytope. An actual
global finitely additive state is stronger evidence than feasibility in any
finite relaxation.

`[HAND — PROVED]` Cell-realizability implies every sound form of visibility.
A cell weighting, represented by finitely many carrier points, defines a
global finitely supported sigma-additive `[0,1]`-valued state on `L`; hence it
satisfies all finite state, order, complement, orthogonality, meet, and join
constraints. Therefore

\[
 P_{cell}(F)\subseteq P_{vis}(E;F)
\]

for every sound finite `E`, and its exact trace lies in the global real-valued
state body. For zero--one traces, every realized cell gives a global Dirac and
hence belongs to both `T_fa^{01}` and `T_sigma^{01}`.

### Correct finite-trace quantifiers

`[HAND — EXACT REFORMULATION]` The paper's finite-trace property is

\[
 \Phi(L)\quad\Longleftrightarrow\quad
 \forall B\in\operatorname{Fin}_{\perp}(L),\quad
 T_{fa}^{01}(B)\subseteq T_{\sigma}^{01}(B).
 \tag{1}
\]

Since every sigma-state is finitely additive, inclusion in (1) is equality.
It is **not** the assertion that every visible vector lies in `P_cell(B)`.

`[CONDITIONAL — PROVED]` If a particular carrier has the separate rigidity
property that every sigma-additive two-valued state is Dirac, then
`T_sigma^{01}(B)=S_B`, and (1) becomes cell-realizability of every coherent
zero--one trace. This is why the cell language is exact for the product-Ulam
witness.

`[REFUTED IN GENERAL]` Let
`Omega_7={+,-}^3 minus {(+,+,+)}` as in the paper's `rem:amendment`, and let

\[
 H=\{0,1,A_i,A_i':i=1,2,3\}
\]

rather than the full powerset. All cross-coordinate sides intersect, so `H` is
the horizontal sum of three four-element Boolean blocks: a finite concrete
sigma-complete OML. The assignment `s(A_1)=s(A_2)=s(A_3)=1` is itself a global
sigma-additive two-valued state on `H`, but no point realizes it because the
`+++` cell was removed. Thus

\[
 (1,1,1)\in T_\sigma^{01}(F)\setminus P_{cell}(F).
\]

This carrier is segregated and not a candidate for `Psi_lat`; it is a decisive
type counterexample to the claimed equivalence on concrete lattices. No clause
in `Adm` says that all sigma-states are Dirac, and the coarse-block audit even
constructs essentially irreducible concrete OMLs with global nonprincipal
sigma-states; see
[`oml_coarse_inhabitation_and_defect.md`](../notes/open_questions/oml_attack/oml_coarse_inhabitation_and_defect.md),
Theorem 5.

### Required calibration: the product-Ulam witness

`[HAND + REPO — VERIFIED]` Take `F=(A_1,A_2,A_3)` from `def:carrier`. The four
fibres give exactly the following realized cells.

| fibre | membership in `(A_1,A_2,A_3)` |
|---|---|
| `M times {1}` | `110` |
| `M times {2}` | `101` |
| `M times {3}` | `011` |
| `M times {4}` | `000` |

Consequently

\[
 P_{cell}(F)=\operatorname{conv}\{110,101,011,000\}
 \subseteq\{x:x_1+x_2+x_3\le2\}.
\]

The banked vote state `m` is a genuine global finitely additive two-valued
state and has trace `(1,1,1)`. Its trace is therefore visibility-feasible in
the strongest possible sense, but it is cell-infeasible.

`[REPO — VERIFIED MECHANISM]` The invisibility is exactly where
`rem:coherence-location` puts it. The set intersections
`A_1 intersection A_2=M times {1}` and its two cyclic companions are absent as
carrier meets; `cor:incompat` computes the missing lower bounds, and
`lem:table`(IV) says that no linking disjointness constraints between distinct
weight-two core types occur. Adding the first intersection to a same-base
lattice refinement creates the three disjoint pieces whose finite-additivity
equations destroy coherence, as recorded in
[`site_regularity_prediction_ledger.md`](site_regularity_prediction_ledger.md),
entry `ULAM-B-1`.

**Calibration verdict.** `[PASSED AS WITNESS ANATOMY; FAILED AS A GENERAL
REFORMULATION]` The polytopes reproduce the known witness without adjustment.
They diagnose its Dirac-support gap. They do not characterise `Phi` outside
the rigidity slice, so the proposed Phase-3 implication cannot be used as
stated.

## Phase 3 — what meets do, and do not, supply

### Meet augmentations

`[HAND — DEFINITION]` For finite `F` in a lattice define the one-round
augmentation

\[
 F^{(1)}=F\cup\{a\wedge b:a,b\in F\}
\]

and the full finite meet closure

\[
 F^{\wedge}=\{\bigwedge G:\varnothing\ne G\subseteq F\}.
\]

If complements are needed for membership cells, first replace `F` by
`F union F'`. One round contains pair chords only. Full closure is the one
needed even to discuss every higher-order membership pattern; it has at most
`2^|F|-1` elements before coincidences. Neither closure asserts that a lattice
meet equals the carrier set intersection.

`[HAND — PROVED]` For `c=a meet b`, comparability makes `c` compatible with
each of `a,b`. It does not make `a` compatible with `b`, and the three need not
lie in one Boolean context. In a concrete OML,

\[
 a\wedge b\subseteq a\cap b,
\]

possibly strictly. Equality would put `a intersection b` in `L` and hence make
the pair compatible by the repo's L0 theorem.

### The proposed chord conditional

`[TYPE/SCOPE ERROR — BROKEN]` The statement

> if the constraint hypergraph of `F^meet` is decomposable, visibility equals
> cell-realizability

has no valid proof from the stated hypotheses, for three independent reasons.

1. The event--cell incidence hypergraph is not a Vorob'ev marginal-scenario
   hypergraph. Weights summed over event hyperedges are not coordinate
   marginals on joint contexts.
2. Re-encoding events by indicator variables gives a distribution on the full
   cube `{0,1}^F`. Vorob'ev gluing does not force it onto the realized support
   `S_F`. A separate **lossless-support** condition is needed:

   \[
   S_F=\mathop{\Join}_{C\in\mathcal C}\pi_C(S_F).
   \tag{2}
   \]

   Without (2), local supports admit phantom assignments. The product-Ulam
   assignment `111` is the calibrated phantom.
3. OML states are not lattice homomorphisms. In the concrete `MO_2` on
   `{1,2,3,4}`, take `a={1,2}`, `b={1,3}`. Their lattice meet is `0`, while the
   Dirac at `1` gives `delta_1(a)=delta_1(b)=1`. Thus even a sigma-additive
   two-valued state need not satisfy
   `s(a)=s(b)=1 implies s(a meet b)=1`. This is the banked refutation of
   Skeleton C in
   [`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md),
   section 7c.

Nonzero meets therefore need not transmit the charged value. Zero or strict
meets are not the only way a proposed chord can carry no state constraint.

### A type-correct conditional theorem

`[CONDITIONAL — PROVED; CLASSICAL, NOT A NEW OML THEOREM]` Let `X` be a finite
set of indicator variables, let `C` be a family of joint-coordinate scopes,
and let `S subset product_{x in X} O_x` be the set of carrier-realized
assignments. Suppose:

1. the marginal-scenario hypergraph `(X,C)` is alpha-acyclic;
2. compatible local probability distributions `q_C` are supplied on every
   scope, each supported on `pi_C(S)`; and
3. the realized support is lossless as in (2).

Then the `q_C` have a global probability distribution supported on `S`.

*Proof.* Vorob'ev/running-intersection gluing gives a global distribution `q`
with the prescribed marginals. If `q(z)>0`, then every restriction `z|C` has
positive local marginal and hence lies in `pi_C(S)`. Thus `z` lies in their
natural join, which is `S` by (2). So `q` is a cell weighting. `square`

This theorem states exactly what the proposed proof would need. The missing
OML work is not the classical gluing step; it is proving that `L`-visibility
supplies the joint local distributions and that meet augmentation supplies
the lossless-support identity. Latticehood alone supplies neither, as `MO_2`
shows.

### Flatness and loops

`[REFUTED AS AN EXHAUSTIVE CHARACTERISATION]` For the intended mechanism, a
meet is ineffective whenever it fails to transmit the state/support condition
needed by the gluing argument. `a meet b=0` and strict
`a meet b subsetneq a intersection b` are two ways this happens. A third is a
non-Jauch--Piron state with `mu(a)=mu(b)=1` but `mu(a meet b)=0`. Any exhaustive
“flat” definition must include the state as well as the order geometry.

`[REFUTED]` “Loops of order at least five are exactly flat, finitely” slides
between levels and is false. The order-five condition belongs to the Greechie
**block nerve** Loop Lemma. In the Greechie pentagon, adjacent blocks share a
nonzero atom, so selected cross-block meets need not be zero. Conversely a
horizontal sum has zero off-block meets without possessing a five-loop.
Nothing here identifies the event--cell incidence hypergraph or the indicator
marginal hypergraph with that nerve.

### Falsifier registered before any hunt

`[REGISTERED; NOT HUNTED]` The prompt's legitimate finite probe is:

> an infinite concrete sigma-complete OML `L` and a finite trace `F` such that
> the full complement-and-meet augmented indicator-scope hypergraph is
> non-acyclic, while some actual global finitely additive zero--one trace lies
> outside `P_cell(F)`.

This would refute any universal claim that meet closure triangulates finite
supports. To bear on `Psi_lat`, strengthen it to `L in Adm` and require the
trace also to lie outside `T_sigma^{01}(F)`; the cell condition alone is
insufficient. No exhaustive finite-logic search, and no search for this
falsifier, was performed.

**Phase-3 verdict.** `[BROKEN AT THE BRIDGE]` The classical conditional is
available, but the proposed meet-as-chord theorem is not proved conditionally
from lattice visibility. Its missing premises are joint-context typing,
lossless support, and value transmission. These are mechanisms, not
terminology.

## Phase 4 — the flat/coarse habitat

### Does sigma-closure force chords?

`[REFUTED AT ABSTRACT OML SCOPE]` The completion thread already supplies a
counterexample to generic triangulation. In
[`site_regularity_orthomodular_completions.md`](site_regularity_orthomodular_completions.md),
section 1, five infinite finite--cofinite Boolean blocks are pasted in a
five-cycle over four-element sites. The Loop Lemma makes the paste an OML.
Replacing every block by its powerset completion and retaining the same sites
again gives an OML; all blocks are complete, hence the OML is complete. New
elements remain block-private, so they create no new cross-block upper or
lower bounds and do not add nerve chords. Therefore sigma-completion does not
triangulate a pasting merely because it is cyclic.

`[SCOPE LIMIT]` That banked construction is an abstract complete-OML result;
the cited note did not verify that its completed infinite paste is a concrete
`Adm` carrier with the state properties required here. It refutes the generic
order-theoretic slogan, not the concrete lattice conjecture.

`[REPO — VERIFIED SCOPE CORRECTION]` Campaign 11's puncture theorem in
[`oml_distributed_relation_cell_assembly.md`](../notes/open_questions/oml_attack/oml_distributed_relation_cell_assembly.md),
section 3, says that two faithful sigma-closed puncture blocks cannot identify
one full countably generated boundary: the same decreasing sequence would
have meet `0` in one leg and a nonzero singleton in the other. The follow-up
completion audit distinguishes arbitrary amalgamation from regular or
sigma-homomorphic amalgamation. This is an obstruction to one **specific
faithful shared boundary**, not a theorem that sigma-closure manufactures
cross-block chords.

### `Adm` gates

`[REFUTED]` Essential irreducibility alone does not exclude flat pastings.
`MO_omega`, explicitly represented in
[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md),
section 9a, is an infinite concrete sigma-complete lattice with trivial centre
and zero off-block meets. It is excluded as a witness because it is a
horizontal, segregated, Polish-representable tame carrier—not because it lacks
irreducibility.

`[REFUTED AS AN INFERENCE]` Non-segregation also does not ban flat geometry;
it bans the blockwise trace-rescue property at `rem:segregated`. No repo theorem
derives nonzero mixed meets, block-nerve connectedness, or marginal-hypergraph
acyclicity from it.

`[REPO — VERIFIED]` Finite interfaces are dead. Under `MeetsExist`, the formal
`finite_interface_quarantine` theorem gives `Phi` whenever every raw block
overlap is finite. Thus the five-loop with four-element sites, even if supplied
with all remaining concrete hypotheses, has the wrong boundary scale. A live
flat pasting needs an infinite overlap/boundary and a genuinely distributed
failure of common-`mu` descent.

`[REPO — VERIFIED FENCE]` Coarseness must also survive essential
irreducibility. Proposition 4 of
[`oml_coarse_inhabitation_and_defect.md`](../notes/open_questions/oml_attack/oml_coarse_inhabitation_and_defect.md)
shows that a fibre whose distinctions are all countable/co-countable is erased
by the countable ideal and leaves a central quotient. Its Theorem 5 shows that
coarse blocks can inhabit essentially irreducible concrete OMLs, but the
constructed carrier is `Phi`-tame. For countable-type coarse fields the defect
reduces to free-on-countable atom killing, the already-closed relay territory;
the genuinely new resource would have to be non-countable-type over its atoms.

### Habitat verdict and concrete hand target

`[OPEN, SHARPLY LOCATED]` The remaining habitat is not merely “an infinite
flat loop.” It must combine all of:

- an infinite concrete sigma-complete OML;
- an infinite coarse boundary, because finite interfaces quarantine;
- mixed meets which are strict or state-null and therefore do not transmit the
  charged trace;
- a non-countable-type state defect, or another rigidity mechanism not reduced
  to the T4 relay;
- quotient structure surviving the countable ideal; and
- a common-`mu` GSD obstruction, plus the remaining `Adm` conditions.

No repo result excludes this conjunction, and no candidate is known to satisfy
it.

`[SPECIFIC NEXT HAND ATTEMPT — NOT A RESULT CLAIM]` Work on exactly the
three-cell conditional-diagonal star named at the end of
[`oml_distributed_relation_cell_assembly.md`](../notes/open_questions/oml_attack/oml_distributed_relation_cell_assembly.md),
using three distinct proper nonseparating quotient supports. Choose the
interface sigma-fields outside the countable-type-over-atoms class and require
their quotient by countable sets to be nontrivial, as fenced by
[`oml_coarse_inhabitation_and_defect.md`](../notes/open_questions/oml_attack/oml_coarse_inhabitation_and_defect.md),
sections 2--3. The first lemma to attempt is:

> **Coherence-preserving flat-realisation lemma for the three-cell star.** The
> fixed three-cell diagram has a faithful concrete sigma-complete OML
> realisation preserving the three quotient legs in which the designated
> three-face trace still has a global finitely additive two-valued extension,
> and every mixed meet introduced by closure is strict and null for that
> extension.

Name the falsifier before the calculation: a mixed-cut identity forced in
every faithful realisation whose finite-additivity equations contradict the
three prescribed value-one faces. If the lemma holds, the concrete flat
habitat has been located for the subsequent `Adm` audit; if it fails, the
first forced identity is the sought sigma-triangulation mechanism. This is one
hand calculation on one banked carrier architecture, not a finite census and
not an attempt at `Psi_lat` itself. It deliberately does not presuppose a
canonical or least OML completion; the completion thread supplies no such
object.

## Phase 5 — one-page memo

| Question | Verdict | Evidence |
|---|---|---|
| What survives the exclusion lemma in `Adm intersect lattices`? | An actual global finitely additive two-valued state with a finite cluster spanning at least three incompatible blocks, but no common-boundary-compatible selection of local sigma-states. This is GSD/distributed boundary descent. The further description as a cell-polytope obstruction is conjectural and false without rigidity. | **REPO-VERIFIED** for cluster/GSD; **REFUTED** for the general cell equivalence |
| Are missing countable limits live? | No. A sigma-orthocomplete OML is countably complete. | **LITERATURE-VERIFIED + HAND proof** |
| Is the product-Ulam mechanism live on lattices? | No, but the reason is T1 singleton quarantine, not countable monotone completeness. | **REPO-VERIFIED; prompted derivation corrected** |
| Is absolute KS/statelessness live in `Adm`? | No: concreteness supplies Diracs. Relative failure to match a finite trace remains live. | **HAND/REPO-VERIFIED** |
| Does non-segregation connect the block nerve? | No. It excludes a blockwise rescue condition, not disconnectedness. | **REFUTED** |
| Is the chord mechanism already known? | Ordinary acyclic marginal gluing is classical Vorob'ev--Kellerer and explicit in contextuality. No OML meet-to-marginal bridge was located. | **LITERATURE-VERIFIED + SEARCH-NEGATIVE** |
| Was the proposed chord conditional proved? | No. It is mistyped and lacks lossless support and value transmission. A corrected conditional with those hypotheses is proved above. | **BROKEN; corrected theorem CONDITIONAL-PROVED** |
| Are order-five loops exactly flat? | No; this conflates the block nerve with trace/marginal hypergraphs, and adjacent pentagon blocks share nonzero atoms. | **REFUTED** |
| Does sigma-closure triangulate flat pastes? | Not in general: the completed five-loop retains its cycle and cross-block operations. | **REFUTED at abstract OML scope** |
| Does `Adm` exclude the remaining flat/coarse habitat? | Essential irreducibility and non-segregation do not. Finite interfaces and countable-ideal-vanishing coarse fibres are excluded. The full concrete habitat remains open. | **PARTLY REFUTED / PARTLY REPO-VERIFIED / OPEN** |

**First pen-and-paper task.** Attempt the stated coherence-preserving
flat-realisation lemma on the
banked three-cell conditional-diagonal star with non-countable-type,
countable-quotient-visible interfaces. Do not begin with a general
Vorob'ev theorem: the classical gluing step is already owned, and the only
load-bearing question is whether every faithful sigma-closed lattice
realisation forces a mixed-cut identity that kills the prescribed coherent
trace.

## Source record

Primary and survey sources used for the fresh literature component:

- N. N. Vorob'ev, “Consistent Families of Measures and Their Extensions,”
  *Theory Probab. Appl.* 7 (1962), 147--163,
  [primary record and theorem](https://www.mathnet.ru/eng/tvp4710).
- H. G. Kellerer, “Maßtheoretische Marginalprobleme,” *Math. Ann.* 153
  (1964), 168--198, [EuDML record](https://eudml.org/doc/161128),
  [local renamed scan](../notes/literature_review/literature/kellerer_1964_mass_theoretic_marginal_problems.pdf).
- H. G. Kellerer, “Verteilungsfunktionen mit gegebenen
  Marginalverteilungen,” *Z. Wahrscheinlichkeitstheorie* 3 (1964), 247--270,
  [DOI](https://doi.org/10.1007/BF00534912).
- C. Budroni *et al.*, “Kochen--Specker Contextuality,” *Rev. Mod. Phys.* 94
  (2022), 045007, [arXiv](https://arxiv.org/abs/2102.13036).
- S. Abramsky and A. Brandenburger, “The Sheaf-Theoretic Structure of
  Non-Locality and Contextuality,” *New J. Phys.* 13 (2011), 113036,
  [arXiv](https://arxiv.org/abs/1102.0264).
- A. De Simone, M. Navara, and P. Pták, “Extending states on finite concrete
  logics,” [arXiv:math-ph/0311012](https://arxiv.org/abs/math-ph/0311012).
- S. S. Holland, Jr., “An `m`-orthocomplete orthomodular lattice is
  `m`-complete,” *Proc. Amer. Math. Soc.* 24 (1970), 716--718,
  [DOI](https://doi.org/10.1090/S0002-9939-1970-0256949-8).
