# Site regularity and orthomodular completions

*Audit date: 2026-08-02. Branch:
`oml-descent-sigma-essential-reduction`. This is an adjacent investigation;
no paper-of-record file or dependency-path file was changed.*

**Follow-up correction (2026-08-02).** The conjecture called C in this audit
is superseded. Its target incorrectly mixed abstract completion with
MacNeille completion. The active replacement is C′: if every site of a pasting
is regular in each containing block, its MacNeille completion is an OML. The
scope correction and follow-up verdicts are recorded in
[`site_regularity_prediction_ledger.md`](site_regularity_prediction_ledger.md)
and
[`site_regularity_intrinsic_and_state_coupling.md`](site_regularity_intrinsic_and_state_coupling.md).

## Verdicts

| Item | Verdict | Evidence |
|---|---|---|
| Phase 0 reconnaissance | **VERIFIED** | Repository and bundled Mathlib source read |
| Campaign 11 vacuity gate | **VACUITY THREAT REJECTED** | Campaign 11 only rules out a faithful shared sigma-boundary; Phase 2 supplies a non-regular site in an existing OML |
| Infinite-block Loop Lemma | **VERIFIED** | Greechie 1971 and Kalmbach 1983 state it for arbitrary Boolean blocks |
| Acyclicity as a necessary condition for completion | **REFUTED** | The five-loop finite/cofinite construction and its blockwise completion are valid |
| Phase 2 site computation | **VERIFIED** | An explicit site in the Amemiya-Araki OML is non-regular |
| Pre-registered Phase 2 falsifier | **SCOPE GAP** | Global MacNeille failure excludes a regular completion, not every completion allowed by literal Conjecture C |
| Conjecture C | **REPLACED - SCOPE ERROR** | Superseded by the MacNeille-specific C′ in the follow-up ledger |
| Phase 3 | **NOT RUN** | Deliberately descoped; the required Boolean MacNeille infrastructure is absent |

Here "regular" has the meaning stated in the investigation prompt: if a join
or meet of a family exists in the site, its image must have that join or meet
in the containing block, with the same value. Thus failure of the ambient join
is a failure of preservation, not a vacuous comparison. This is also the
meaning of regular order embedding in Harding-Wang Definition 3.7.

The word "completion" in Conjecture C is kept exactly as stated. In
particular, this audit does not silently strengthen it to "regular completion"
or "global MacNeille completion." That distinction matters in the Phase 2
verdict.

## 0. Reconnaissance

### Existing formal material

The following is already present and reusable.

- `formalization/QuerySystem/QuerySystem/OrthomodularMO2.lean` defines the
  corpus's minimal abstract `OrthomodularLattice` class and verifies `MO2`.
- `formalization/QuerySystem/QuerySystem/ConcreteOMLBlocks.lean` contains the
  concrete block layer for a `DynkinSystem`: `Compat`, maximal pairwise
  compatible families `IsMaxBlock`, Zorn extension to a maximal block,
  complement and disjoint-countable-union closure, the latticehood predicate
  `MeetsExist`, the concrete compatibility/meet bridge, commutant closure, and
  sigma-field packaging of maximal blocks and their pairwise intersections.
- `formalization/QuerySystem/QuerySystem/SigmaEssentialLocalization.lean`
  contains a different object named `Block`: a finite complement-closed local
  pattern. It is not a maximal Boolean subalgebra.
- `formalization/QuerySystem/QuerySystem/BoundaryDescent.lean` glues compatible
  local states across overlaps. It does not construct a pasting of event
  algebras.
- `formalization/QuerySystem/QuerySystem/UlamWitnessLatticeGap.lean` names
  `PsiOML` and proves, modulo its explicitly cited corpus axiom, that the Ulam
  witness fails `MeetsExist`. It does not supply completion machinery.
- Campaign 11's
  `notes/open_questions/oml_attack/oml_distributed_relation_cell_assembly.md`
  already contains the puncture-meet obstruction audited below.
- The W1/W2 isolation notes on branch `e5-banking-audit` isolate index-category
  and coefficient questions for the sigma-state programme. Their reusable
  contribution here is audit method, not an order-completion construction.

Bundled Mathlib has `BooleanSubalgebra`, its finitary
`BooleanSubalgebra.closure`, and the order-theoretic Dedekind-MacNeille type
`DedekindCut` in `Mathlib/Order/Completion.lean`. It does not provide a Boolean
or orthocomplemented structure on `DedekindCut B`, a notion of least complete
Boolean subalgebra, or the regular-subalgebra theorem proposed for Phase 3.

### Absent material

There is no generic formalization in the repository of:

- an algebraic pasting of Boolean algebras;
- sites as intersections of abstract OML blocks;
- regular inclusions of Boolean or orthomodular substructures;
- preservation of all existing `sSup`/`sInf` by such inclusions;
- Boolean, ortholattice, or OML structure on a MacNeille completion; or
- canonical completion of an orthostructure.

Accordingly, "block" and concrete compatibility are existing notions; "site"
is a useful rename of a block intersection in the concrete sigma-class setting;
site regularity and the completion theorem are new. A general pasting object is
also new, not a rename of state gluing.

## Campaign 11: what actually fails

Campaign 11 first constructs local cells

\[
  B_i=\operatorname{Borel}(C\setminus\{i\})
\]

with a common clopen boundary `Clop(C)`. The note explicitly says at that
point that the cells are not yet a pasted Boolean atlas, OMP, or OML.

For distinct punctures $i,j$, choose a decreasing clopen basis $U_n$ at
$i$. In the $i$-puncture cell the identified sequence has meet $0$, while
in the $j$-puncture cell it has meet $\{i\}$. The proved conclusion is:

> no concrete sigma-complete OML contains both cells as faithful sigma-closed
> Boolean blocks while identifying that full boundary.

This is not a finitary contradiction in an algebraic paste. A lower bound in
one block may lie outside the other block, and an OMP imposes no requirement
that a countable meet calculated in one non-complete block be visible in every
block containing the sequence. Campaign 11 therefore does **not** prove that
the transported algebraic paste fails to be an orthoposet or an OML. Its
Section 4 leaves those completion gates open.

**Verdict: SCOPE CORRECTION.** The puncture theorem is a faithful
sigma-embedding obstruction. It neither makes all actual sites regular nor
makes Conjecture C vacuous. Phase 2 below supplies an actual OML with a
non-regular site.

## 1. Infinite-block Loop Lemma

### Citation verdict

The finiteness caveat does not survive the primary sources.

1. Kalmbach, Chapter 1, Section 4, starts with a set of Boolean algebras,
   imposes Condition (A) on their pairwise intersections, and states Loop
   Lemma 9: the induced union is an OMP iff there is no loop of order 3, and an
   OML iff there is no loop of order 3 or 4. No finiteness assumption is made
   on the Boolean algebras. The discussion after the lemma separately invokes
   atomicity only to draw Greechie diagrams.
2. Greechie 1971, Convention 1 and Theorems 2-3, likewise begins with arbitrary
   Boolean lattices satisfying the bounds/shared-atom intersection condition.
   The text explicitly permits replacement by arbitrary atomic Boolean
   lattices, not necessarily of the same cardinality.
3. Bruns 1979 describes this exact intersection regime as the case completely
   solved by Greechie. It does not add a finite-block hypothesis.
4. Rogalewicz 1988 proves that the system of all blocks of every OMP is a
   pasted family in Dichtl's sense. This is the needed converse background,
   not a restriction on Greechie's Loop Lemma.

The full Dichtl paper was not available from the publisher endpoint during
this audit. Rogalewicz reproduces Dichtl's definition and Theorem 9. Dichtl is
not load-bearing for the infinite-block verdict, which is direct in Greechie
and Kalmbach.

### The five-loop completion

For $i\in\mathbb Z/5\mathbb Z$, let $X_i$ be a countably infinite set and
let

\[
  B_i=\operatorname{FinCofin}(X_i).
\]

Choose two distinct atoms in each $B_i$. Using abstract copies, identify one
of them with the designated atom in $B_{i+1}$, together with its complement;
make no other nontrivial identifications. Then adjacent intersections are
four-element Boolean algebras and non-adjacent intersections are the bounds.
The block diagram has exactly one loop, of order 5.

Condition (A) holds. The Loop Lemma therefore makes the union an OML. Each site
is finite, so every join and meet existing in it is finitary and is preserved
by both block inclusions: every site is regular.

The MacNeille completion of $\operatorname{FinCofin}(X_i)$ is
$\mathcal P(X_i)$: every subset of $X_i$ is the join of its singleton atoms.
Paste these powerset algebras using the same abstract four-element
identifications. Condition (A) and the loop orders are unchanged, so the Loop
Lemma again gives an OML. The original paste embeds as a subalgebra. For old
elements in one block, binary operations are preserved by the
finite/cofinite-to-powerset inclusion. For old elements not lying in a common
block, any common upper or lower bound must lie in the unchanged intersection
sites: a new element belongs to only one abstract block and cannot be
comparable to an element exclusive to another. Thus no new element changes an
old cross-block join or meet.
The completed powerset algebras are the maximal blocks, and all are complete.
Harding-Wang Remark 3.18 says that an OML is complete iff all its blocks are
complete. Hence the new OML is a complete OML containing the original one.

**Verdict: REFUTED.** A cycle in the block nerve is not an obstruction to
orthomodular completion. The infinite-block version of the proposed
counterexample is citation-valid; it is not merely conjectural.

## 2. The Amemiya-Araki site

### The ambient OML

Let

\[
 V=G\oplus H=c_{00}(\mathbb N;\mathbb C)\oplus
                   c_{00}(\mathbb Z;\mathbb C)
\]

with its standard inner product. Its Hilbert completion is
$\ell^2(\mathbb N)\oplus\ell^2(\mathbb Z)$, so $V$ is incomplete. Write
$(g_n)_{n\in\mathbb N}$ and $(e_k)_{k\in\mathbb Z}$ for the standard
orthonormal Hamel bases of $G$ and $H$.

Let $L$ be the ortholattice consisting of all finite-dimensional subspaces
of $V$ and their orthogonal complements. Equivalently, these are the finite
and orthogonally cofinite subspaces used in Harding's Amemiya-Araki example.
It is a modular ortholattice, hence an OML. Its MacNeille completion is the
complete ortholattice of biorthogonal subspaces of $V$, which is not
orthomodular because $V$ is incomplete.

### Two explicit orthonormal bases

On $H$, define orthogonal linear bijections $A,B$ by two staggered families
of $2\times2$ rotations:

\[
\begin{aligned}
 A e_{2k}&=(e_{2k}+e_{2k+1})/\sqrt2,&
 A e_{2k+1}&=(-e_{2k}+e_{2k+1})/\sqrt2,\\
 B e_{2k-1}&=(e_{2k-1}+e_{2k})/\sqrt2,&
 B e_{2k}&=(-e_{2k-1}+e_{2k})/\sqrt2.
\end{aligned}
\]

Both maps and their inverses preserve finite support. Put $f_j=BAe_j$. Then

\[
\begin{aligned}
 f_{2k}&=(-e_{2k-1}+e_{2k}+e_{2k+1}+e_{2k+2})/2,\\
 f_{2k+1}&=(e_{2k-1}-e_{2k}+e_{2k+1}+e_{2k+2})/2.
\end{aligned}
\]

Thus

\[
  \mathcal E=\{g_n:n\in\mathbb N\}\cup\{e_k:k\in\mathbb Z\},\qquad
  \mathcal F=\{g_n:n\in\mathbb N\}\cup\{f_k:k\in\mathbb Z\}
\]

are orthonormal Hamel bases of $V$.

For either basis $\mathcal U$, define its coordinate block by

\[
 B_{\mathcal U}=\{\operatorname{span}_{\mathcal U}(J):
                   J\text{ is finite or cofinite in }\mathcal U\}.
\]

These are maximal Boolean subalgebras of $L$. Indeed, if $X\in L$ is
compatible with every coordinate ray of $\mathcal U$, each basis vector lies
in $X$ or $X^\perp$. Expanding vectors in the Hamel basis then makes $X$
a coordinate subspace. Since $X$ or $X^\perp$ is finite-dimensional, its
coordinate set is finite or cofinite, so $X\in B_{\mathcal U}$.

### Computing the intersection

Form the bipartite overlap graph whose vertices are copies of the vectors in
$\mathcal E$ and $\mathcal F$, with an edge $u-v$ exactly when
$\langle u,v\rangle\ne0$.

If a subspace $X$ is coordinate in both bases, membership in $X$ is
constant on every graph component. To see this, suppose an $\mathcal E$-ray
is in $X$ and an adjacent $\mathcal F$-ray is not. Coordinatehood in
$\mathcal F$ puts the latter ray in $X^\perp$, contradicting the nonzero
inner product. The other direction is symmetric. Conversely, a union of
components spans the same subspace from either side: every basis vector has a
finite expansion supported on its neighbors, in both directions.

For the displayed bases the components are exactly:

- one two-vertex component $\{g_n^{\mathcal E},g_n^{\mathcal F}\}$ for each
  $n\in\mathbb N$; and
- one infinite component containing every $e_k$ and every $f_k$.

The second assertion follows from the four-term formulas: each $f_{2k}$ and
$f_{2k+1}$ meets the four consecutive $e$-coordinates
$2k-1,2k,2k+1,2k+2$, and consecutive windows overlap.

Write $G_D=\operatorname{span}\{g_n:n\in D\}$. A union of components belongs
to either finite/cofinite coordinate block only in one of two cases: it is a
finite union of the $g_n$-components, or it contains the infinite component
and omits only finitely many $g_n$-components. Therefore the site is

\[
 S=B_{\mathcal E}\cap B_{\mathcal F}
  =\{G_D:D\subseteq\mathbb N\text{ finite}\}
   \cup
   \{G_D^\perp:D\subseteq\mathbb N\text{ finite}\}.
\]

In particular, $S$ is abstractly the finite/cofinite Boolean algebra on the
atoms $G_{\{n\}}$.

### The non-regularity witness

Take the site family

\[
  \mathscr G=\{G_{\{n\}}:n\in\mathbb N\}\subseteq S.
\]

Its join in $S$ is $V$. No proper site element contains every $g_n$: a
finite $G_D$ misses some $g_n$, while $G_D^\perp$ misses every $g_n$
with $n\in D$.

The family has no join in $B_{\mathcal E}$. Every block upper bound must be
cofinite and has the form

\[
 U_K=\bigl(\operatorname{span}\{e_k:k\in K\}\bigr)^\perp,
 \qquad K\subseteq\mathbb Z\text{ finite}.
\]

For every finite $K$, choose $k\notin K$. Then $U_{K\cup\{k\}}$ is a
strictly smaller upper bound. Hence there is no least upper bound. Replacing
$e_k$ by $f_k$ gives the identical proof in $B_{\mathcal F}$.

Thus both inclusions

\[
  S\hookrightarrow B_{\mathcal E},\qquad
  S\hookrightarrow B_{\mathcal F}
\]

are non-regular: a join existing in $S$ is not carried to an existing join
in either block.

This is an actual site of two actual maximal blocks of the existing OML $L$.
By Rogalewicz, the blocks of $L$ form a pasting. Non-regularity therefore
does not prevent formation of a pasting; it can occur inside an OML and can
obstruct the proposed blockwise-completion datum.

### Why the prompt's alternatives were not exhaustive

Phase 2 requested either different computed joins or regularity of all sites.
The example gives a third outcome: the site join exists but the two ambient
joins do not.

For these two basis blocks, an unequal pair of computed joins is impossible.
Let $\mathscr A\subseteq S$.

- If $\mathscr A$ contains a cofinite site element, the union of its coordinate
  sets is cofinite, belongs to $S$, and is the join in both blocks.
- Otherwise all members are finite spans of $g_n$'s. Their coordinate union
  omits every $e_k$ and every $f_k$. It has a join in either finite/cofinite
  block only when the union of $g_n$-indices is finite; then that finite span
  lies in $S$ and is the same join in both blocks.

Meets have the dual property by orthocomplementation. Therefore whenever a
join or meet of site elements exists in either selected ambient block, the
corresponding operation exists in the other block and in the site with the
same result. The only possible failure here is existence, and
$\mathscr G$ exhibits it explicitly.

### What happens in the completed block

The MacNeille completion of $B_{\mathcal E}$ is the powerset of its basis
atoms. In it,

\[
  G_* = \bigvee_n G_{\{n\}}=G
\]

is a proper element, with nonzero complement $H$. The least complete Boolean
subalgebra containing the image of $S$ has atoms

\[
  G_{\{0\}},G_{\{1\}},\ldots,H
\]

and is isomorphic to $\mathcal P(\mathbb N\cup\{\infty\})$, where the residual
atom $H$ represents $\infty$. By contrast, the MacNeille completion of the
abstract site $S\cong\operatorname{FinCofin}(\mathbb N)$ is
$\mathcal P(\mathbb N)$, in which the join of its displayed atoms is top.
There can be no unital complete embedding of that site completion into the
completed block extending $S$: it would have to send the same join both to
$G$ and to $V$.

This is the exact failure of the rationale for Conjecture C when regularity is
absent.

### Phase 2 verdict

**EXPLICIT NON-REGULAR SITE; LITERAL CONJECTURE C NOT ADJUDICATED.** The two
maximal blocks above have a non-regular site. This rejects the vacuity threat
and matches the proposed local mechanism.

The pre-registered falsifier, however, has a scope gap. Harding-Wang Remark
3.4 says that this same $L$ embeds into a complete OML after passing to the
Hilbert completion of $V$. Definition 3.7 and Theorem 3.8 distinguish a
*regular* completion: such a completion factors through the MacNeille
completion, and Corollary 3.9 uses the non-orthomodular MacNeille completion to
exclude regular completions. Thus hypothetical regularity of every site would
immediately falsify a strengthened claim only if its completed paste were also
known to give a regular embedding of $L$, or to be the global MacNeille
completion of $L$.

Literal Conjecture C states only that the blockwise paste "yields a
completion." It does not assert either additional property, and no theorem in
this investigation derives global regularity from regularity of all site legs.
Consequently the registered falsifier was only conditionally valid. It did not
fire, but that is not a verdict-grade prediction hit for Conjecture C as it was
then written. That claim is now superseded by the MacNeille-specific C′ in the
follow-up ledger. The computation supplies mechanistic evidence, not a
necessary-condition theorem or a sufficiency proof.

## Concrete corpus consequence

`ConcreteOMLBlocks.lean` defines `IsMaxBlock` as a maximal pairwise-compatible
family. Under `MeetsExist`, the file proves closure under binary intersection,
union, complement, and arbitrary countable union, and packages each maximal
block and each pairwise overlap as a sigma-field. The identification with an
orthomodular block is not just terminological: `Compat.isGreatest_inter` makes
carrier intersection the lattice meet whenever `Compat` holds, while
`compat_of_commuting_decomp` gives the converse from the standard commuting
decomposition. Thus, under `MeetsExist`, `Compat` is lattice compatibility.
The `inter_mem`, `union_mem`, and `compl_mem` closure theorems make each
`IsMaxBlock` family a Boolean subalgebra, and maximal pairwise compatibility
makes it maximal among such subalgebras. These are therefore genuine maximal
Boolean blocks of the concrete OML, not merely finite local patterns;
`iUnion_mem'` strengthens them to sigma-fields.

Every `DynkinSystem` already has joins of countable pairwise-disjoint, hence
orthogonal, families: their set union is in the carrier and is the global least
upper bound. If `MeetsExist` holds, the carrier is an OML. Holland's theorem
for $m=\aleph_0$ states that every countably orthocomplete OML is countably
complete. Consequently:

> every concrete corpus carrier satisfying `MeetsExist` is automatically a
> sigma-complete OML.

This also follows by orthogonalizing the increasing sequence of finite joins.
It is stronger than merely saying that its maximal blocks are sigma-fields.

The Ulam witness fails `MeetsExist`, so it is not an OML. It is nevertheless
already sigma-complete in the OMP sense because it is a `DynkinSystem`. Thus
Harding-Wang Problem 2 is trivial for these carriers when read OMP-to-OMP, and
also for the `MeetsExist` carriers when read OML-to-OML. What remains at the
Ulam object is an OML-envelope/lattice-completion question, not the existence
of countable orthogonal joins.

**AUDIT WARNING.** `notes/open_questions/kits/oml_onboarding.tex`, around its
definition of completeness, says that sigma-orthocompleteness is strictly
weaker than sigma-completeness on an OML. Holland 1970 proves the opposite:
they are equivalent for OMLs. That source was not edited in this adjacent
thread.

## Phase 3

**NOT RUN.** Formalizing the proposed regularity lemma would first require a
Boolean structure on the Dedekind-MacNeille completion and a least complete
Boolean-subalgebra construction. Neither is in the repository or bundled
Mathlib. No Lean file was added and no claim was weakened to fit available
infrastructure.

## Sources and local literature files

- I. Amemiya and H. Araki, "A remark on Piron's paper," *Publ. RIMS* 2
  (1966), 423-427, [EMS Press](https://ems.press/journals/prims/articles/2377).
  Local: `../notes/literature_review/literature/amemiya_araki_1966_remark_piron.pdf`.
- G. Bruns, "Block-Finite Orthomodular Lattices," *Canad. J. Math.* 31
  (1979), 961-985, [Cambridge Core](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/blockfinite-orthomodular-lattices/3DEED7623DB279B6C19AA92A12E6C60D).
  Local: `../notes/literature_review/literature/bruns_1979_block_finite_orthomodular_lattices.pdf`.
- M. Dichtl, "Astroids and pastings," *Algebra Universalis* 18 (1984),
  380-385, [DOI](https://doi.org/10.1007/BF01203371). Full text was not
  obtained; no HTML landing page was retained as a PDF.
- R. J. Greechie, "Orthomodular lattices admitting no states," *J. Combin.
  Theory A* 10 (1971), 119-132,
  [publisher record](https://www.sciencedirect.com/science/article/pii/009731657190015X).
  The accessible web copy was read, but its host rejected direct download; no
  local file was created.
- J. Harding, "Orthomodular lattices whose MacNeille completions are not
  orthomodular," *Order* 8 (1991), 93-103,
  [author copy](https://math.nmsu.edu/people/personal-pages/files/1991-OMLs-whose-MacNeille-Comps-are-not-OML.pdf).
  Local: `../notes/literature_review/literature/harding_1991_omls_macneille_completions_not_orthomodular.pdf`.
- J. Harding and Z. Wang, "Logical aspects of quantum structures," 2021,
  [arXiv:2108.09819](https://arxiv.org/abs/2108.09819).
  Local: `../notes/literature_review/literature/harding_wang_2108.09819_completions.pdf`.
- S. S. Holland, Jr., "An $m$-orthocomplete orthomodular lattice is
  $m$-complete," *Proc. Amer. Math. Soc.* 24 (1970), 716-718,
  [DOI](https://doi.org/10.1090/S0002-9939-1970-0256949-8). The AMS record and
  abstract were checked; the AMS endpoint denied the local PDF download.
- G. Kalmbach, *Orthomodular Lattices*, Academic Press, 1983, Chapter 1,
  Section 4. Local:
  `../notes/literature_review/literature/kalmbach_1983_orthomodular_lattices.pdf`.
- V. Rogalewicz, "Any orthomodular poset is a pasting of Boolean algebras,"
  *Comment. Math. Univ. Carolin.* 29 (1988), 557-558,
  [EuDML](https://eudml.org/doc/17667). Local:
  `../notes/literature_review/literature/rogalewicz_1988_any_orthomodular_poset_pasting_boolean_algebras.pdf`.
