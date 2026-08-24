# Latticehood prior-art audit

*2026-08-04. Literature search only; no new mathematics. The source statement is
[`frontier_map.md`](../notes/programme/frontier_map.md), §1, with the exact
regularity problem in
[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md),
§1. The two lead verdicts are recorded separately in
[`latticehood_prior_art_ledger.md`](latticehood_prior_art_ledger.md).*

## Verdict in one paragraph

**NO SINGLE OWNER; TWO COMPONENTS ARE CLASSICAL TRANSLATIONS; THE REGULARITY
PROBLEM REMAINS.** The advertised family is not yet one mathematically typed
dichotomy. The corpus defines *liftability* exactly only at regularity, as the
finite-trace property `Phi`. Pasting is a compatible-marginal extension problem;
sharpness is existence of a dispersion-free state. Classical measure-algebra
lifting is an unrelated right-inverse problem which already starts with a
countably additive measure. Bohrification does not identify the three arrows:
Kochen--Specker sharpness is exactly absence of a global element of the spectral
presheaf; probabilistic pasting is exactly a global-section problem for a
different, distribution-valued presheaf; and regularity is local sigma-additivity
of a measure on clopen subobjects, not preservation by restriction maps. The
formal completing target that survives is therefore the OML regularity question
`latticehood => Phi`; the three-way slogan needs a definition before it can be a
theorem.

## 0. Exact search target

### 0.1 The three arrows are not instances of one defined arrow

| transition | exact input and output | exact tame predicate | hypotheses of the corpus result/question |
|---|---|---|---|
| **Pasting** | compatible local probability tables `EA` -> one global realization `PR(R)` | the protocol is **commensurable**, equivalently its coherence and realization polytopes satisfy `C = R` | a finite alphabet, a finite family of finite-coordinate contexts, and a declared realization class `R` (all, stationary, subshift-supported, or finite-memory measures) |
| **Regularity** | a finite two-valued trace having some global finitely additive extension -> the same trace having some global sigma-additive extension | `Phi(L)` below | for the lattice question: `L` is a concrete, sigma-complete, non-Boolean, essentially irreducible OML |
| **Sharpness** | probabilistic statehood -> existence of a value-definite state | `S_df(A) != empty` | a complemented lattice/OML `A`; distributivity is sufficient, while `A = L(H)`, `dim H >= 3`, fails by Kochen--Specker |

There is no corpus definition of a common object called “liftability” covering
all three rows. In particular, pasting extends a family of marginals, regularity
may replace one global state by another while retaining only a finite trace, and
sharpness is stated as non-emptiness rather than as an extension of a specified
sigma-additive state. The symbols `EA` and `PR` are also overloaded across the
reconstruction and realism papers; their source-specific definitions should not
be identified without an explicit translation.

### 0.2 Pasting, exactly

Fix a finite alphabet `A`. A context is a partition of `A^F` for finite
`F subset Z`, a protocol is a finite family of contexts, and window-data assigns
a probability to every cell. The datum is **empirically adequate** (`EA`) when
any two context distributions agree on every common event. For a declared class
`R` of global processes, it is **realisable** (`PR(R)`) when some member of `R`
induces all those distributions. Thus

`pasting-tame(protocol, R)  <=>  for every p, EA(p) implies PR(R)(p)  <=>  C = R`.

For the unrestricted finite marginal problem, Vorob'ev's “regular” (running-
intersection/acyclic) complexes are exactly those on which every consistent
family extends. This is already the corpus's acyclic tame theorem, not a new
latticehood theorem. See the exact definitions in
[`reconstruction_skeleton.tex`](../papers/reconstruction/reconstruction_skeleton.tex)
and [Vorob'ev's primary abstract and theorem](https://www.mathnet.ru/eng/tvp4710).

### 0.3 Regularity and *liftability*, exactly

For a carrier `L`, let `St(B)` be the two-valued states on `B`,
`St_fa(L)` the global finitely additive two-valued states, `St_sigma(L)` the
global sigma-additive two-valued states, and `Fin_perp(L)` the finite
orthocomplement-closed suborthoposets. The corpus's **finite-trace
sigma-liftability** predicate is

\[
\Phi(L) :\Longleftrightarrow
\forall B\in\operatorname{Fin}_{\perp}(L)\;\forall s\in\operatorname{St}(B),
\quad
\bigl(\exists\mu\in\operatorname{St}_{fa}(L),\ \mu|_B=s\bigr)
\Rightarrow
\bigl(\exists\nu\in\operatorname{St}_{\sigma}(L),\ \nu|_B=s\bigr).
\]

The sigma-additive state `nu` need not be the finitely additive state `mu`; only
their finite trace is fixed. Equivalently, `St_sigma(L)` is dense in `St_fa(L)`
for the product topology. The question of record is whether every concrete,
sigma-complete, non-Boolean, essentially irreducible OML satisfies `Phi`. Here
“concrete” means a set logic `L subset P(Omega)`, sigma-completeness is closure
under countable disjoint unions, and **latticehood means binary meets and joins**.
It does not mean arbitrary completeness. “Essentially irreducible” means that
the quotient by the sigma-ideal of countable sets has centre `{0,1}`. The `Adm`
display in the paper also lists non-segregation and non-Polish-representability,
but explicitly identifies those as consequences of witnesshood, not additional
prior hypotheses; the attack note therefore uses the four-condition class just
stated. The spine's generic regularity arrow speaks about states in general,
whereas the exact open predicate `Phi` is two-valued and finite-trace-relative.
See
[`sigma_essential_body.tex`](../papers/sigma_essential/sigma_essential_body.tex),
§Discussion, and
[`relational_boundary_descent.md`](../notes/open_questions/oml_attack/relational_boundary_descent.md),
§1.

### 0.4 Sharpness, exactly

A state on an OML `A` is a map `s : A -> [0,1]`, with `s(1)=1`, additive on
orthogonal pairs. A sigma-additive state is additive on every countable
orthogonal family whose join exists. A state is **dispersion-free** when `s(a)`
is in `{0,1}` for every `a`. The corpus's operative sharpness predicate is

\[
\operatorname{VDR}(A) \quad\Longleftrightarrow\quad
\mathcal S_{df}(A)\ne\varnothing.
\]

On Boolean algebras these are ultrafilter states; on a general OML a
dispersion-free state need not be a lattice homomorphism. The filtration section
stipulates `S_df(A) subset S_sigma(A)`, while the standalone VDR definition asks
only for a dispersion-free state. Those formulations require an explicit
sigma-additivity clause to agree on infinite carriers; they should not be treated
as silently identical in a unification theorem. The exact definitions and this
general-OML caveat are in
[`distributivity_and_realism_body.tex`](../papers/paper_ii/distributivity_and_realism_body.tex).

There is also a decisive type check: `L(H)` for `dim H >= 3` is already a complete
orthomodular **lattice**, yet has no dispersion-free state. Consequently literal
OML latticehood cannot imply sharpness. Distributivity implies sharpness; ordinary
latticehood does not.

## 1. Classical lifting and completeness analogues

### 1.1 Measure-algebra lifting: an unrelated homonym

For a complete measure space `(X, Sigma, mu)` with null ideal `N`, let
`A = Sigma/N` and `q : Sigma -> A` be the quotient. A classical lifting is a
Boolean homomorphism `theta : A -> Sigma` satisfying `q theta = id_A`: it chooses
one measurable representative of every equivalence class modulo null sets while
preserving finite Boolean operations. The von Neumann--Maharam lifting theorem
gives such a right inverse for every nontrivial complete strictly localizable
measure space, hence for every complete probability space. This is Fremlin's
Definition 341A and Theorem 341K; the historical development and the 1969
monograph are recorded by [Ionescu Tulcea and Ionescu Tulcea](https://link.springer.com/book/10.1007/978-3-642-88507-5).
See also [Fremlin, *Measure Theory*, Chapter 34](https://www1.essex.ac.uk/maths/people/fremlin/chap34.pdf).

The mismatch is exact:

- classical lifting starts with a fixed **countably additive** measure and a null
  quotient, then chooses representatives;
- `Phi` starts with a finitely additive two-valued state on a non-Boolean carrier
  and asks for a possibly different sigma-additive state matching finitely many
  values;
- completeness in the lifting theorem means completion by subsets of null sets
  (plus localizability), not lattice completeness, sigma-orthocompleteness, or OML
  latticehood.

No fixed null ideal, quotient map, or representative-selection problem occurs in
`Phi`. Classical lifting therefore does not supply the missing middle step.

**Verdict: CLOSED -- UNRELATED HOMONYM; NO TECHNIQUE TRANSFER LOCATED.**

### 1.2 AW* versus W*: the same warning shape, not the same theorem

The prompt's formulation needs one correction. An AW*-algebra is not defined by
projection-lattice completeness alone. One equivalent definition requires both
that the right annihilator of each element be projection-generated **and** that
`Proj(A)` be a complete lattice; equivalent formulations use annihilators of
arbitrary subsets or suprema of orthogonal projection families. W*-algebras form
a full subcategory and additionally possess a Banach predual. These definitions
are stated in Heunen--Reyes,
[“Active lattices determine AW*-algebras,” Definition 2.1](https://arxiv.org/pdf/1212.5778).
The inclusion is strict: Saito records both Dixmier's commutative non-W* AW*
example and the Takenouchi--Dyer non-W* AW* factors in
[“AW*-algebras with monotone convergence property and examples by Takenouchi
and Dyer”](https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_31/_pdf/-char/en).

In the commutative case, complete projection Boolean algebras correspond to
Stonean spaces. The W* case is hyperstonean: normal measures must have supports
whose union is dense. Pavlov makes this added measure-theoretic condition exact
and identifies normal functionals with directed-supremum-preserving functionals;
see [“Gelfand-type duality for commutative von Neumann algebras”](https://arxiv.org/pdf/2005.05284),
Lemma 2.71 and Definition 3.3.

This **does** own the negative shape “order completeness alone does not produce
measure-theoretic normality.” It does **not** prove the corpus implication. AW*
uses arbitrary projection completeness and C*-algebraic annihilators, much
stronger data than binary OML latticehood plus countable orthogonal joins.
Noncommutative projection lattices also leave the corpus's concrete class in the
Kochen--Specker regimes; commutative AW* projection lattices are Boolean, where
`Phi` is already known.

**Verdict: OWNED AS A NEGATIVE ANALOGUE; NOT AN INSTANCE OF `Phi`.**

### 1.3 The three other completeness comparisons

| source | actual implication | comparison with the corpus |
|---|---|---|
| Kaplansky, [“Any orthocomplemented complete modular lattice is a continuous geometry”](https://doi.org/10.2307/1969811) | arbitrary lattice completeness + orthocomplementation + **modularity** imply lattice-theoretic continuity | a genuine completeness-to-continuity theorem, but its continuity is continuity of lattice operations, not sigma-additivity of states; general OMLs need not be modular |
| Amemiya--Araki, [“A remark on Piron's paper”](../notes/literature_review/literature/amemiya_araki_1966_remark_piron.pdf) | `L(V)` is already an irreducible complete OAC lattice; it is orthomodular iff the pre-Hilbert space `V` is metrically complete | the roles are reversed: order completeness holds on both sides, while orthomodularity detects analytic completeness; it is not “lattice completeness implies tameness” |
| Abramsky--Jung, [“Domain Theory”](https://www.cs.ox.ac.uk/files/298/handbook.pdf), §§2.1--2.2 | every complete lattice is a dcpo, but continuity requires way-below approximation; even distributive complete lattices can be non-continuous | directed completeness does not imply the approximation property. This is another counterpattern, not a corpus-shaped implication |

Across these comparisons the word “complete” denotes four different properties:
measure-space null completeness, arbitrary projection completeness, arbitrary
lattice completeness, and directed completeness. None equals the corpus's
conjunction of binary latticehood with countable orthogonal completeness.

## 2. Bohrification and presheaf translations

### 2.1 Three related constructions, not one presheaf

The literature uses at least three context-indexed objects that must not be
identified:

| task | context object | section/measure condition |
|---|---|---|
| sharp values | the contravariant spectral presheaf over commutative/Boolean contexts | a global element is a compatible family of characters |
| probabilistic pasting | the event sheaf and its distribution presheaf | a global distribution restricts to the compatible local distributions |
| regular quantum states | measures on clopen subobjects of the spectral presheaf, or valuations on the internal Bohrified spectrum | normality is local sigma-additivity / valuation continuity |

Heunen--Landsman--Spitters use the covariant topos on commutative C*-subalgebras
and an internal commutative C*-algebra whose Gelfand spectrum is a distributive
locale; Döring--Isham use a contravariant spectral presheaf and daseinisation.
They are closely related approaches, but not literally the same presheaf. See
[HLS, “A topos for algebraic quantum theory”](https://arxiv.org/pdf/0709.4364)
and [Döring--Isham, *A Topos Foundation ... II*](https://arxiv.org/abs/quant-ph/0703062).

### 2.2 Sharpness: yes, exactly a section-existence condition

For a von Neumann algebra `N`, let `V(N)` be its poset of unital abelian von
Neumann subalgebras. The spectral presheaf sends a context `V` to its Gelfand
spectrum and an inclusion `V' subset V` to restriction of characters. A global
element is therefore a family `(lambda_V)` of characters compatible under every
restriction. It yields a context-independent valuation obeying the spectrum and
functional-composition rules; conversely such a valuation yields the family.

For `B(H)`, `dim H > 2`, no such family exists. Isham--Butterfield state the
equivalence explicitly in
[“A topos perspective on the Kochen--Specker theorem I”](https://arxiv.org/pdf/quant-ph/9803055).
Döring's [von Neumann algebra generalization](https://arxiv.org/pdf/quant-ph/0408106)
covers algebras with no type-I1 or type-I2 summand. In the corpus's language this
is the sharpness obstruction: no global value assignment / dispersion-free
valuation in the Kochen--Specker scope.

**Answer to Phase 2(1): YES -- ALREADY OWNED, WITH THE USUAL TYPE-I2 CAVEAT.**

### 2.3 Pasting: yes as gluing, but on a different presheaf

Abramsky--Brandenburger define an empirical model as a compatible family of
local distributions on a measurement cover. A global section of the distribution
presheaf is exactly a distribution on all measurements whose marginals are the
given local distributions; see
[their §3](https://arxiv.org/pdf/1102.0264). This is the corpus's
`EA -> PR` extension shape. Vorob'ev proves the exact acyclic theorem: a finite
complex is regular iff every consistent family of measures extends.

It is not a global element of the spectral presheaf. A spectral global element is
deterministic and encodes sharpness; a distribution-presheaf global section is a
probability distribution over global assignments and encodes pasting. Reusing
“global section” does not make the two objects identical.

**Answer to Phase 2(2): YES IN THE SHEAF IDIOM; NO ON THE SAME PRESHEAF. THE
ACYCLIC CASE IS OWNED BY VOROB'EV/AB.**

### 2.4 Regularity: translated, but restriction maps do not detect it

Döring proves that states of a von Neumann algebra without a type-I2 summand
correspond to finitely additive measures on clopen subobjects of the spectral
presheaf. A measure is **locally sigma-additive** when countable families that
are pairwise disjoint at one context satisfy countable additivity there; these
measures correspond exactly to normal states. See
[Döring, equations (42) and Corollary IV.2](https://arxiv.org/pdf/0809.4847).
HLS similarly turn states into probability valuations on the internal Gelfand
spectrum, a frame/locale.

This answers the translation question but not `Phi`. Naturality under context
restriction is already built into both finitely additive and normal cases.
Normality is an extra countable-additivity condition **inside** Boolean fibres,
not preservation by the restriction maps. Nor do these results say that every
finite trace realized by an arbitrary finitely additive two-valued state has a
normal/sigma-additive two-valued realization.

**Answer to Phase 2(3): YES AS LOCAL SIGMA-ADDITIVITY OF A PRESHEAF MEASURE;
NO AS RESTRICTION-PRESERVATION; `Phi` IS NOT SUPPLIED.**

### 2.5 Latticehood does not become one presheaf condition

Bohrification makes the internal spectrum distributive by construction: its opens
form a frame. Source noncommutativity is relocated to variation over the context
poset and to coarse-graining/daseinisation. Thus the construction does not expose
a presheaf property equivalent to the corpus's binary OML latticehood which
forces all three transitions.

There is a direct obstruction to any literal claim: projection lattices of von
Neumann algebras are complete OMLs, while their spectral presheaves can have no
global elements. Hence lattice completeness and sharpness coexist on opposite
sides in the flagship example. The earlier full-text audit reached the same
boundary and graded it **SAME-WALL-WITH-MACHINERY**; see
[`topos_route_read_2026-06-19.md`](../notes/open_questions/verification/topos_route_read_2026-06-19.md).

**Answer to Phase 2(4): NO SINGLE RECOGNISABLE CONDITION WAS LOCATED.**

## 3. Phase 4 memo

**Is the latticehood dichotomy owned elsewhere?** Not as one dichotomy. Pasting
is owned as compatible-family extension (Vorob'ev) and as a distribution-
presheaf global-section problem (Abramsky--Brandenburger). Sharpness is owned as
absence of global elements of the spectral presheaf (Isham--Butterfield,
Döring--Isham). Regularity has a standard topos translation—normal states are
locally sigma-additive presheaf measures—but the corpus's finite-trace density
property `Phi` is not obtained. AW*/W* owns the cautionary analogue that complete
projection order is weaker than measure-theoretic normality; it points against,
not toward, an automatic completeness theorem.

**Is corpus liftability classical lifting?** No. The classical theorem splits a
quotient map from measurable sets to a measure algebra after sigma-additivity and
null completeness are already present. Corpus `Phi` replaces a finitely additive
two-valued state by a sigma-additive one while preserving a finite trace. The
domains, hypotheses, maps, and outputs differ.

**Does Bohrification collapse the transitions?** It translates all three into a
common context-indexed idiom, but uses different objects and different predicates.
Sharpness is a point/global-element question; pasting is a distribution/global-
section question; regularity is a measure-continuity question. At most two are
literal section-existence statements, and not for the same presheaf. Regularity
is not section existence at all in the cited formulation.

**What remains?** The exact OML regularity target still needs a genuinely new
idea or a theorem imported from some further state-extension literature. The
three-way completing target has not become a translation exercise: as presently
written it is not a single well-typed conjecture, and its sharpness reading is
false for complete Hilbert lattices. The honest programme update is therefore:
retain `latticehood => Phi` as the formal open target; credit the pasting and
sharpness translations as owned; and demote “one latticehood dichotomy across
all three” to a heuristic until a common liftability predicate and its precise
lattice hypothesis are stated.

## Source and evidence note

This audit used primary/full-text sources for the operative definitions and
theorems: Fremlin; Heunen--Reyes; Saito; Pavlov; Kaplansky; Amemiya--Araki;
Abramsky--Jung; Isham--Butterfield; Döring; Döring--Isham; HLS;
Abramsky--Brandenburger; and Vorob'ev. It also reconciled the findings with the
repo's prior full-text Bohrification audit and the existing Czech-school prior-
art record in the OML attack note. “No owner located” is a bounded literature
verdict, not a theorem of nonexistence.
