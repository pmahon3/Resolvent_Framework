# Relational boundary descent for the OML σ-lifting problem

*Opened 2026-07-12. Status: sharpen-in-place research note. The exact
descent equivalence and finite-boundary theorem below are ⟦HAND⟧, assembled
from the Lean-certified block facts cited in §2 and elementary Stone/Boolean
arguments given here. The Baire and uniform-tail results are conditional
theorem-lets with every extra hypothesis displayed. The rooting and relay
steps remain open or architecture-specific. Nothing here proves
$\Psi_{\mathrm{OML}}$.*

## 1. Statement of scope and statement of record

The unchanged question is:

> Does every concrete, σ-complete, non-Boolean, essentially irreducible
> orthomodular lattice satisfy the finite-trace σ-lifting property $\Phi$?

Equivalently, can such an OML carry a finite pattern which has a finitely
additive two-valued extension but no σ-additive two-valued extension?

The existing split is retained:

- **B′(i):** all maximal Boolean blocks are countably generated;
- **B′(ii):** the residual coarse-block problem.

No countability of the block set, countable atomic master, common tail,
relay normal form, or point realization of arbitrary σ-states is assumed.
The boundary language is an exact reformulation in full generality only
when it uses local **σ-additive states**, not carrier points.

Throughout, $L\subseteq\mathcal P(\Omega)$ is a concrete σ-class OML and
$\mathfrak B(L)$ is its set of maximal Boolean blocks. The repository's
notion of σ-completeness is closure under countable disjoint set unions;
latticehood upgrades every maximal block to a σ-field.

## 2. Banked infrastructure

The following are already Lean-certified in
`ConcreteOMLBlocks.lean`/`ConcreteOMLPatterns.lean`:

1. maximal pairwise-compatible families exist and cover $L$;
2. maximal blocks are Boolean σ-fields of subsets of $\Omega$;
3. $B\cap C$ is a σ-field for maximal blocks $B,C$;
4. a finitely additive two-valued state is σ-additive globally iff it is
   σ-additive on every maximal block
   (`isSigmaOn_carrier_iff_maxBlocks`);
5. on a countably generated block, every two-valued σ-additive local state
   is carrier-point/atom realized (`dirac_realization_of_countablyGenerated`
   and `IsMaxBlock.dirac_realization`);
6. $\Phi$ is equivalent to density of $\operatorname{St}_\sigma(L)$ in
   $\operatorname{St}_{\mathrm{fa}}(L)$ (`phi_iff_dense`).

The fourth item avoids an unnecessary stronger assertion. One need not
first prove that every countable orthogonal family is contained in one
block: for a disjoint family $(A_n)$, maximality extends the compatible
family $\{A_n:n\in\mathbb N\}$ to a maximal block, and the Lean theorem
packages exactly this argument.

## 3. Boundary algebras and local pattern events

For $B\in\mathfrak B(L)$ define

\[
 \partial B=\operatorname{BA}_B\!\left(
   \bigcup_{C\ne B}(B\cap C)\right).
\]

This is the Boolean subalgebra generated *inside $B$* by applying finite
Boolean operations to all shared events. It need not be finite or a
σ-subfield; taking σ-closure here would change the interface and is not
needed for compatibility.

Let $p$ be a finite $\perp$-closed pattern. For each block, put

\[
 E_B(p)=\bigcap\{A\in B:p(A)=1\}\cap
        \bigcap\{A^\perp\in B:p(A)=0\},
\]

with empty intersections equal to $1$. These are finite intersections in
the Boolean block, so $E_B(p)\in B$. This packaging is legitimate for the
repository's finite patterns. If patterns are presented without
$\perp$-closure, first close them under complements as in
`ConcreteOMLPatterns.lean`.

For $E\in B$, define

\[
T_B^{\mathrm{fa}}(E)=
 \{u|_{\partial B}:u\in\operatorname{St}_{\mathrm{fa}}(B),\ u(E)=1\},
\]
\[
T_B^\sigma(E)=
 \{v|_{\partial B}:v\in\operatorname{St}_\sigma(B),\ v(E)=1\},
\qquad
\Delta_B^\sigma(E)=T_B^{\mathrm{fa}}(E)\setminus T_B^\sigma(E).
\]

Here a local state is a Boolean ultrafilter, with σ-additivity interpreted
inside the σ-field $B$.

## 4. Exact full-general formulation and proved boundary lemmas

### Lemma 4.1 (compatible block states glue) ⟦HAND, proved⟧

Suppose $u_B$ is a finitely additive two-valued state on each maximal
block and

\[
 u_B|_{B\cap C}=u_C|_{B\cap C}\quad(B,C\in\mathfrak B(L)).
\]

Then $u(A):=u_B(A)$ for any block $B\ni A$ is a well-defined global
finitely additive two-valued state. If every $u_B$ is σ-additive, then
$u$ is globally σ-additive.

*Proof.* Well-definedness is exactly overlap agreement. Every complement
and finite orthogonal join is contained with its operands in a maximal
compatible family, so the local Boolean law proves the global state laws.
The σ-claim is `isSigmaOn_carrier_iff_maxBlocks`. ∎

### Theorem 4.2 (boundary-compatible σ-surgery) ⟦HAND, proved⟧

Let $p$ have a global finitely additive extension $\mu$. Suppose that for
every maximal block $B$ there is $v_B\in\operatorname{St}_\sigma(B)$ with

\[
 v_B(E_B(p))=1,
 \qquad v_B|_{\partial B}=\mu|_{\partial B}.
\]

Then the $v_B$ glue to a global σ-additive two-valued state extending $p$.

*Proof.* If $A\in B\cap C$, then $A\in\partial B\cap\partial C$, hence
$v_B(A)=\mu(A)=v_C(A)$. Lemma 4.1 glues the family. If $p(A)=1$ and
$A\in B$, then $E_B(p)\subseteq A$, so Boolean monotonicity gives
$v_B(A)=1$; the complement clause handles $p(A)=0$. ∎

This uses maximal blocks for coverage and the certified block theorem.
The same proof works for any block cover which contains every relevant
finite/countable compatible family and on which the σ-globalization
lemma has been established.

### Theorem 4.3 (GSD is exactly $\Phi$) ⟦HAND, exact reformulation⟧

For every concrete σ-class OML,

\[
\Phi(L)\quad\Longleftrightarrow\quad
\forall p\text{ finitely coherent}\ \exists\mu\in C_p\ \forall B,
\ \mu|_{\partial B}\in T_B^\sigma(E_B(p)). \tag{GSD}
\]

*Proof.* GSD supplies, for every $B$, a local σ-state witnessing membership
in $T_B^\sigma$; Theorem 4.2 gives a global σ-extension. Conversely, if
$\nu$ is a global σ-extension, take $\mu=\nu$ and
$v_B=\nu|_B$. ∎

There is no missing compatibility condition because every local witness is
required to match the **same** global $\mu$ on its boundary. The weaker
condition “for every $B$ some boundary trace in $T_B^\sigma$ exists” is
not enough: independently chosen traces need not agree on overlaps.

## 5. The private interior as relative background

Let

\[
 \beta_B:\operatorname{St}_{\mathrm{fa}}(B)
       \longrightarrow\operatorname{St}_{\mathrm{fa}}(\partial B)
\]

be restriction. “Outside $B$” cannot mean the set-theoretic complement of
$B$ in $L$, since an event can belong to several blocks. The correct
statement is coordinate-relative.

### Proposition 5.1 (vertical replacement) ⟦HAND, proved⟧

In a compatible block family $(u_C)_C$, replace $u_B$ by $u'_B$ with
$\beta_B(u'_B)=\beta_B(u_B)$. Then all overlap compatibility equations
remain true. Consequently all coordinates assigned through blocks other
than $B$ are unchanged, and shared coordinates receive the same value as
before.

*Proof.* For each $C\ne B$, $B\cap C\subseteq\partial B$, so $u'_B$ and
$u_B$ agree on $B\cap C$. ∎

Thus the fibre $\beta_B^{-1}(t)$ is “vertical”: its members are globally
indistinguishable **with respect to compatibility with the fixed other
block coordinates**. The private interior is not intrinsically irrelevant.
It determines which boundary traces can coexist with $E_B(p)$ and which
σ-local replacements exist.

## 6. Finite-interface quarantine

### Theorem 6.1 (finite-interface quarantine) ⟦LEAN for finite raw overlaps; finite generated-boundary equivalence HAND⟧

If $\partial B$ is finite for every maximal block $B$, then $L$ satisfies
$\Phi$. No irreducibility, non-Booleanness, countability of blocks, or
finiteness of the blocks is required.

*Proof.* Fix a coherent finite pattern and $\mu\in C_p$. The Boolean
algebra

\[
 A_B=\operatorname{BA}_B(\partial B\cup\{E_B(p)\})
\]

is finite. The ultrafilter $\mu|_{A_B}$ selects a unique atom $Q_B$.
Because $Q_B\ne0$ and the representation is concrete, $Q_B$ is a
nonempty subset of $\Omega$. Choose $\omega_B\in Q_B$. Then
$\delta_{\omega_B}|_B$ agrees with $\mu$ on $A_B$ and charges $E_B(p)$.
It is σ-additive. Theorem 4.2 glues these replacements. ∎

Adjoining one (or finitely many) pattern events preserves finiteness.
Agreement on $A_B$ includes every shared event. Simultaneously choosing a
point for an arbitrary set of blocks uses the ordinary Axiom of Choice;
the repository works in ZFC, and Lean's analogous nonconstructive choices
report `Classical.choice`. For a fixed finite or countable block family,
finite or countable choice respectively suffices.

Receipt precision: `BoundaryDescent.lean` directly proves the result when
the raw overlap-event family is finite (or is contained in a finite family).
The displayed formulation uses the Boolean algebra generated under finite
operations by that family.  Raw-overlap finiteness is equivalent to
finiteness of this generated Boolean algebra, but that elementary equivalence
is presently a hand step rather than a Lean theorem.

Finiteness is not necessary. The exact weaker local hypothesis is:

> for every coherent $p$, some $\mu\in C_p$ has, at every block $B$, a
> σ-additive local lift of $\mu|_{\partial B}$ charging $E_B(p)$.

That is GSD itself. A uniform sufficient slice is that every relevant
boundary ultrafilter has such a σ-lift after every finite local
augmentation. The finite-boundary theorem proves this automatically.

## 7. Stone shadows and the fine-block closure defect

Let $X_B=\operatorname{Ult}(B)$, $Y_B=\operatorname{Ult}(\partial B)$,
and let $r_B:X_B\to Y_B$ be restriction. For $E\in B$, define

\[
 \operatorname{Sh}_B(E)=
 \{\delta_\omega|_{\partial B}:\omega\in E\}.
\]

### Proposition 7.1 (boundary-shadow closure) ⟦HAND, proved⟧

For every concrete Boolean block, without countable generation,

\[
 T_B^{\mathrm{fa}}(E)=\overline{\operatorname{Sh}_B(E)}
 \quad\text{in }Y_B.
\]

*Proof.* The clopen $[E]\subseteq X_B$ is compact and $r_B$ is continuous,
so $r_B([E])=T_B^{\mathrm{fa}}(E)$ is compact, hence closed. For density,
take $t=r_B(u)$ with $E\in u$ and a basic neighbourhood $[A]$ of $t$,
$A\in\partial B$. Then $E\cap A\in u$, so $E\cap A\ne\varnothing$.
Any $\omega\in E\cap A$ has boundary trace in
$[A]\cap\operatorname{Sh}_B(E)$. ∎

No extra “carrier separates boundary events” assumption is needed beyond
concreteness: a nonzero Boolean event is literally a nonempty set.

### Corollary 7.2 (fine-block defect) ⟦HAND + Lean dependency⟧

If $B$ is countably generated, then

\[
 T_B^\sigma(E)=\operatorname{Sh}_B(E),\qquad
 \Delta_B^\sigma(E)=
 \overline{\operatorname{Sh}_B(E)}\setminus
 \operatorname{Sh}_B(E).
\]

*Proof.* Proposition 7.1 gives the finitely additive side. The certified
Dirac-realization theorem gives the first equality. ∎

This is a relational reinterpretation of T4/Stone projection, not yet a
new escape mechanism. T4 asks whether a finite global face reaches the
point-shadow at one fine block. Boundary descent identifies precisely
which portion of the local ultrafilter must be point-realized and yields
the finite-interface theorem, but it does not solve simultaneous
selection across infinitely many blocks.

## 8. Countable specializations: scope audit and Baire simultaneous escape

The following hypotheses are distinct:

| Hypothesis | What it controls | Does not imply |
|---|---|---|
| every block countably generated | local σ-state = atom/point state | countably many blocks |
| countably many blocks | number of simultaneous good loci | fine blocks |
| every boundary countably generated **as a Boolean algebra under finite operations** | countability, hence metrizability, of boundary Stone spaces | point realization on the whole block |
| one countably atomic master | one architecture's tail coordinates | a normal form for $L$ |
| common countable tail for a face | uniform obstruction for all states in that face | follows from individual bad tails |

### Theorem 8.1 (conditional Baire simultaneous escape) ⟦HAND, proved⟧

Assume that $L$ has countably many maximal blocks $B_0,B_1,\ldots$, each
countably generated. Let $C_p\subseteq\operatorname{St}_{\mathrm{fa}}(L)$
be a nonempty finite face. For each $n$, suppose:

> every nonempty relatively basic clopen $U\subseteq C_p$ contains a
> state whose restriction to $B_n$ is σ-additive (equivalently,
> point/atom realized).

Then $C_p$ contains a state σ-additive on every block, hence a global
σ-additive extension of $p$.

*Proof.* $\operatorname{St}_{\mathrm{fa}}(L)$ is a closed compact subspace
of the Cantor cube and $C_p$ is clopen in it, hence compact Hausdorff and
Baire. If $\operatorname{At}(B_n)$ is the (possibly uncountable) set of
atoms of $B_n$, the good locus is

\[
 G_n=\bigcup_{D\in\operatorname{At}(B_n)}
       \{\mu\in C_p:\mu(D)=1\},
\]

which is relatively open. The displayed hereditary hypothesis is exactly
density of $G_n$. Baire gives $\bigcap_nG_n\ne\varnothing$. The certified
blockwise-pointed implication gives global σ-additivity. ∎

This theorem does not handle uncountably many blocks. Failure in full
generality can be a cover

\[
 C_p\subseteq\bigcup_{B\in\mathfrak B(L)}
 \{\mu:\mu|_{\partial B}\in\Delta_B^\sigma(E_B(p))\}
\]

with no single defect locus covering the face.

## 9. Local versus distributed traps and uniform tails

Write

\[
 D_B(p)=\{\mu\in C_p:
   \mu|_{\partial B}\in\Delta_B^\sigma(E_B(p))\}.
\]

Failure of GSD gives only $C_p\subseteq\bigcup_BD_B(p)$.

- **local trapping:** $C_p\subseteq D_B(p)$ for one $B$;
- **distributed trapping:** the union covers but no individual $D_B(p)$
  does;
- **state-dependent tail:** each bad trace has its own descending witness;
- **uniform tail:** one descending family is charged by every trace in a
  specified restriction image.

No implication from distributed to local trapping is banked.

### Proposition 9.0 (finite fine-atlas full-block localization after face refinement) ⟦HAND, proved⟧

Suppose the atlas has finitely many fine blocks, $C_p$ is nonempty, and
$C_p$ contains no global σ-state.  Put

\[
 N_B(p)=\{\mu\in C_p:\mu|_B\text{ is not σ-additive}\}.
\]

Then some $N_B(p)$ contains a nonempty relatively clopen finite-cylinder
subface.  Equivalently, after adjoining finitely many coordinates to $p$,
every remaining state is non-σ on one fixed full block.

*Proof.*  The state space is the intersection in $\{0,1\}^L$ of the closed
finite state-law constraints, hence is closed and compact.  A finite face is
its intersection with finitely many coordinate cylinders, hence clopen,
compact Hausdorff, and Baire.  On a countably generated Boolean σ-field every
two-valued σ-state is principal at a signature atom (the repository's Dirac
realization theorem), so the full-block σ-locus is

\[
 G_B(p)=\bigcup_{D\in\operatorname{At}(B)}
        \{\mu\in C_p:\mu(D)=1\}.
\]

This is relatively open, regardless of the cardinality of the atom family;
therefore $N_B(p)$ is relatively closed.  The certified blockwise criterion
and the absence of a global σ-state give $C_p=\bigcup_BN_B(p)$.  A finite
closed cover of a Baire space has a member with nonempty relative interior.
The product topology has a finite-coordinate clopen base, so that interior
contains $C_p$ intersected with one finite cylinder.  Removing inconsistent
or redundant coordinates and complement-closing them gives a nonempty
coherent finite refinement $C_q\subseteq C_p$ contained in $N_B(p)$.
Since $N_B(q)=N_B(p)\cap C_q$, $C_q\subseteq N_B(q)$. ∎

This does **not** localize the boundary defect loci $D_B(p)$.  Boundary-good
means only that $\mu|_{\partial B}$ admits some σ-additive local replacement
charging $E_B(p)$; the given $\mu|_B$ may itself be non-σ.  In the fine case
the boundary-good trace set is the point shadow $\operatorname{Sh}_B(E_B(p))$,
which need be neither open nor closed.  Thus $D_B(p)$ has not been shown
closed, and distributed boundary trapping remains live even for a finite
fine atlas.

Precisely, $D_B(p)\subseteq N_B(p)$: if $\mu|_B$ were σ-additive, it would
itself be a boundary-matching σ-representative charging $E_B(p)$.  Inclusion
can be strict.  For $B=\mathcal P(\mathbb N)$, trivial boundary
$\{\varnothing,\mathbb N\}$, $E=\mathbb N$, and a nonprincipal ultrafilter
$\mu$, the full restriction is non-σ while its boundary trace is replaced by
every point state.  This block example establishes the logical distinction;
it is not asserted to be a maximal-block boundary in an irreducible OML.

### Theorem 9.1 (conditional finite-atlas boundary localization) ⟦HAND, proved⟧

Let the atlas be finite and suppose $C_p=\bigcup_BD_B(p)$.  Write
$R_{B,p}:C_p\to T_B^{\mathrm{fa}}(E_B(p))$ for boundary restriction and
$K_{B,p}=R_{B,p}(C_p)$.  If

\[
 K_{B,p}\cap T_B^\sigma(E_B(p))
 \quad\hbox{is relatively open in }K_{B,p}
 \tag{RO$_{p,B}$}
\]

for every block in the cover, then some nonempty coherent finite refinement
$C_q\subseteq C_p$ satisfies $C_q\subseteq D_B(q)$ for one fixed $B$.

*Proof.*  Under (RO$_{p,B}$), the boundary-good locus in $C_p$ is the
continuous preimage of a relatively open subset of $K_{B,p}$, so $D_B(p)$
is relatively closed.  Apply the finite closed-cover/Baire argument above
and choose $C_q\subseteq D_B(p)$.  Since $E_B(q)\subseteq E_B(p)$, a σ-lift
charging $E_B(q)$ would charge $E_B(p)$, so $D_B(p)\cap C_q\subseteq D_B(q)$.
∎

This face-image condition is the weakest convenient topological version: it
is needed only for the pattern event $E_B(p)$, only on $K_{B,p}$, and only
for blocks retained in a finite subcover.  Global relative openness in all of
$T_B^{\mathrm{fa}}(E)$ for every $E$ is a stronger uniform hypothesis.  More
generally the proof needs only that each participating defect locus is closed
(or has the weaker property “empty interior implies nowhere dense”); the
Baire property alone is insufficient, since two sets with the Baire property
and empty interior can cover a Baire space.

In the fine case (RO$_{p,B}$) says precisely that
$K_{B,p}\cap\operatorname{Sh}_B(E_B(p))$ is open in $K_{B,p}$.  Requiring
$\operatorname{Sh}_B(E)$ open in its full closure is sufficient but not
necessary.

### Proposition 9.2 (interface classes and limits of relative openness) ⟦HAND⟧

The relative-openness condition holds in the following useful cases:

1. finite boundary algebra (indeed the finite-interface theorem gives no
   defect at all);
2. finite/discrete boundary Stone space;
3. the relevant carrier shadow is clopen or open in its closure;
4. the relevant carrier image is compact in the Hausdorff boundary Stone
   space (hence closed and equal to its closure), for example when the
   carrier event is compact and its evaluation map is continuous;
5. the restricted evaluation map has closed image (in particular, is
   proper).  An open image also suffices directly.

None of the following alone implies (RO): finite-to-one evaluation;
compact fibres; a closed or open image for the *whole* evaluation map rather
than the relevant event; extremal disconnectedness/Stoneanness of the
codomain; or merely locally compact/Polish domain and continuous evaluation.
Countable generation of either Boolean algebra gives metrizability/Dirac
realization where appropriate, not openness.

For a counterexample with compact boundary Stone space, let
$Y=2^{\mathbb N}$, choose a countable dense
subset $Q\subseteq Y$, take carrier $\Omega=Q$, full block
$B=\mathcal P(Q)$ (countably σ-generated by its singletons), and let
$\partial B$ be the Boolean algebra of traces on $Q$ of clopens of $Y$.
Then $\operatorname{Ult}(\partial B)\cong Y$ and for $E=\Omega$ the evaluation
map is the inclusion $Q\hookrightarrow Y$.  Its fibres are singletons and
its image is dense but not open, so the shadow is not relatively open in its
closure.  This is a concrete Boolean block/interface counterexample to
automatic openness, not by itself an overlap boundary of a concrete OML.
Replacing $Q$ by a dense nonopen Polish subspace gives the analogous warning
against Polish-domain hypotheses.

The original face need not itself be locally trapped.  The finite relational
trace table $C_p=\{0,1,2\}$ with $D_{B_i}=\{i\}$ is an irredundant distributed
cover; `../verification/distributed_trap_audit.py` is its executable receipt.
That table is **not** claimed realizable by a concrete σ-class OML.  It shows
only that one block need not trap the *unrefined* face.  All its defect loci
are clopen, and every singleton refinement localizes, so it is not a
counterexample to Theorem 9.1 or to finite-refinement localization.  It models
abstract boundary-defect loci, not full-block bad loci and not an OML.

### Lemma 9.3 (uniform tail under a countable-base hypothesis) ⟦HAND, proved⟧

Let $Y=\operatorname{Ult}(\partial B)$ be compact metrizable (for example,
$\partial B$ is countable), and let
$K\subseteq T_B^{\mathrm{fa}}(E)$ be compact with
$K\cap\operatorname{Sh}_B(E)=\varnothing$. Then there are
$H_0\ge H_1\ge\cdots$ in $\partial B$ such that every $t\in K$ charges
every $H_n$, while

\[
 E\cap\bigcap_nH_n=\varnothing.
\]

*Proof.* In a zero-dimensional compact metric space, a closed set is the
intersection of a decreasing sequence of clopen neighbourhoods. Choose
$[H_n]\downarrow K$. If $\omega\in E\cap\bigcap_nH_n$, its boundary trace
belongs to every $[H_n]$, hence to $K$, contradicting the hypothesis. ∎

Compactness without a countable base yields an intersection of clopen
neighbourhoods, but not necessarily a **countable** sequence. Also, the
lemma applies to a compact trapped restriction image, not automatically to
a distributed cover.

If $F_n=E\cap H_n$ and the ambient block contains their countable
intersection, put $Q_n=F_n\setminus F_{n+1}$. Every relevant local state
which charges $E$ and whose trace lies in $K$ has value $1$ on each $F_n$
and value $0$ on every $Q_n$, while

\[
 \bigsqcup_nQ_n=F_0\setminus\bigcap_nF_n=F_0
\]

when $F_0=E$ and the intersection is empty. Thus it assigns $0$ to every
ring but $1$ to their disjoint union: the boundary form of the
finite-cofinite/Ulam tail.

## 10. Sasaki consequence filters

Fix the **right Sasaki projection** convention

\[
 a\& b:=b\wedge(a\vee b^\perp).
\]

### Proposition 10.1 (state-one sets are Sasaki filters) ⟦HAND, proved⟧

For a finitely additive two-valued state $\mu$ on an OML,
$F_\mu=\{a:\mu(a)=1\}$ contains $1$, excludes $0$, is upward closed, and
is closed under $\&$.

*Proof.* Only Sasaki closure needs comment. If $\mu(a)=\mu(b)=1$, then
$\mu(a\vee b^\perp)=1$ by monotonicity. Since
$b^\perp\le a\vee b^\perp$, orthomodularity gives

\[
 a\vee b^\perp=b^\perp\vee
   (b\wedge(a\vee b^\perp)),
\]

an orthogonal join. Finite additivity and $\mu(b^\perp)=0$ force
$\mu(a\&b)=1$. ∎

For a finite cluster $\mathcal C$, define

\[
 \operatorname{Cn}(\mathcal C)
 =\bigcap_{\mu\in C_{\mathcal C}}F_\mu.
\]

Intersections preserve the displayed axioms, so this is legitimately a
semantic Sasaki consequence filter (provided the face is nonempty, as
coherence requires). It is **defined by finite premises**. Nothing here
shows it is finitely generated as a Sasaki filter.

### Proposition 10.2 (countably atomic master translation) ⟦HAND, proved⟧

Let a complete master block $M$ have atoms $(D_n)$ with
$\bigvee_nD_n=1$. For a coherent cluster $\mathcal C$, T4 fails at $M$
iff

\[
 D_n^\perp\in\operatorname{Cn}(\mathcal C)\quad\forall n,
 \qquad \bigwedge_nD_n^\perp=0.
\]

*Proof.* T4 at $M$ says that some state in the face charges some atom.
Its failure says every state in the face kills every $D_n$, equivalently
charges every $D_n^\perp$. The meet identity is Boolean De Morgan applied
to $\bigvee_nD_n=1$. ∎

This is a one-master specialization of local T4 failure, not a
reformulation of the full conjecture.

## 11. Architecture-specific slices: minimality, rooting, and strong-state equations

An inclusion-minimal locally trapped finite cluster guarantees only:

- the full face remains finitely coherent and trapped at the named block;
- deleting any premise produces at least one boundary-σ-liftable
  continuation at that block;
- any such continuation must falsify the deleted premise, otherwise it
  would escape the full trap.

This yields an essential $m$-ary **boundary truth table**. It does not by
itself yield a global σ-state after deletion: the continuation may remain
bad at another block. The two-block rescue theorem says only that the
first possible unsupported cluster needs at least three blocks/value-one
groups; it does not reduce higher arity to ternary.

The proposed rooting arrow remains open:

\[
 \text{minimal boundary defect}\ \not\Rightarrow_{\rm proved}\
 \exists x\nleq y\text{ whose separating face is trapped}.
\]

The invalid shortcut $\mu(E_i)=1$ for all $i$ implies
$\mu(\bigwedge_iE_i)=1$ is blocked already by $MO_2$. Sasaki terms are
legitimate members of the semantic consequence filter by Proposition
10.1, but no completeness theorem says that one of them roots every
finite semantic defect.

The s36--s38 rooted deaths are therefore evidence about the searched
relay architectures. No checked argument currently identifies one
Godowski, Mayet--Godowski, or other finite strong-state equation violated
by every all-remainder survivor. Nor is there a counterexample proving
that no common equation exists. This is an explicit exploratory task, not
a theorem claim.

## 12. Relation to the relay census

| Census failure | Boundary classification | What boundary descent adds |
|---|---|---|
| face not free / not σ-live | local σ-liveness failure | identifies absence of a liftable boundary trace |
| all-remainder master trace | boundary trace non-realizability | exact closure-defect language on a fine master |
| short Berge cycle / missing meet | lattice-geometry failure | outside local trace theory; gluing atlas is invalid |
| target spacing or master-cycle failure | master-distance/attachment failure | architecture-specific, not a general descent obstruction |
| root or cross-cell order witness lost | rooted order-separation failure | candidate final contradiction if a rooting theorem exists |
| coarse σ-state not point-realized | not captured by point shadows | requires the general $T_B^\sigma$, hence belongs to B′(ii) |

The “liveness/separation tradeoff” is not one theorem. Boundary descent
splits it into local trace liftability, simultaneous compatibility,
lattice geometry, and σ-state order separation. The census establishes
bounded exclusions only for its named faces, widths, and periods.

## 13. Failed claims and counterexamples

The conversation PDF is a proposal, not a receipt. The audit corrects the
following claims.

| Proposed inference | Verdict | Witness/reason |
|---|---|---|
| Independently σ-liftable boundary traces glue | **false without common compatibility** | witnesses chosen independently can disagree on $B\cap C$; GSD is exact because all match one $\mu$ |
| Every local σ-state is a carrier point | **false outside the fine-block slice** | coarse blocks are precisely B′(ii); the repository records non-point σ-states on non-countably-generated fields |
| Point shadows are closed | **false in general** | Proposition 7.1 identifies their closure with all finitely additive extendible traces; a nonempty defect is exactly nonclosedness |
| Compact trapped image always gives a countable tail | **insufficiently justified** | compact nonmetrizable Stone spaces need not have countable neighbourhood bases; Lemma 9.3 adds metrizability |
| Individual local escape gives simultaneous escape over arbitrary blocks | **false as an inference** | Baire uses countably many dense open loci; an uncountable intersection need not be nonempty |
| Failure traps the whole face at one block | **false as an inference** | GSD failure gives only a possibly uncountable defect cover; distributed trapping remains possible |
| Minimal local escape after deleting a premise is a global σ-extension | **false as an inference** | the continuation may be defective at another block |
| Value one on incompatible premises passes to their meet | **false** | $MO_2$ has a two-valued state charging two cross-block atoms while their meet is $0$ |
| A one-master relay is a normal form | **unsupported** | the census assumes periodic/bounded-width relay and master attachment data; no reduction theorem exists |

No new explicit OML counterexample to $\Phi$ is claimed. The table records
counterexamples to proof moves and missing implications, which is the
relevant adversarial output.

## 14. Dependency diagram

```text
Lean: blocks/overlaps are σ-fields
             + blockwise σ <=> global σ
                         |
                         v
common-μ boundary compatibility ---> exact GSD <=> Φ
                                       |
                                       v
                              not-Φ => distributed
                              boundary-defect cover
                                 /             \
                                v               v
                    boundary regularity      direct simultaneous
                                |             selection theorem
                                v               |
                    finite-refinement           v
                    localization               GSD
                                |
                                v
                    local rooting/contradiction

common-μ boundary compatibility
             |
             v
finite boundaries ------------> finite-interface quarantine
             |
             v
Stone restriction + concreteness ---> Tfa = closure(point shadow)
             + fine-block Dirac theorem
                         |
                         v
                 fine closure defect
                         |
       countably many blocks + hereditary density
                         |
                         v
                 Baire simultaneous escape

local compact trap + metrizable boundary ---> uniform countable tail
minimal trap ---> essential boundary gate -?-> rooted nonorder
                                           (OPEN)
```

## 15. Claim/status table

| Claim | Scope | Status | Dependency |
|---|---|---|---|
| Finite-interface quarantine | arbitrary atlas, finite raw/generated interfaces | **Lean for finite raw overlap families; generated-boundary form hand** | boundary point realization |
| Full-block non-σ localization | finite fine atlas | **proved ⟦HAND⟧** | closed non-σ loci |
| Boundary-defect localization | finite atlas | **proved conditionally ⟦HAND⟧** | relative openness on each face restriction image |
| Boundary shadow relatively open | finite/discrete, clopen, compact-image, or proper-image classes | **proved in those classes; refuted in general** | interface topology |
| Distributed-trap countermodel | three-point discrete abstract trace atlas | **executable; unrefined only** | clopen loci; singleton refinements localize |
| GSD equivalence | full generality | **exact reformulation ⟦HAND⟧** | compatible σ-local gluing |
| Rooting local traps settles $\Phi$ | full generality | **false without localization** | quantifier reversal |

## 16. What would settle what

| Result | Consequence |
|---|---|
| Prove GSD directly for all fine blocks | settles B′(i), hence the fine half only |
| Prove hereditary one-block escape with countably many fine blocks | Baire theorem gives that countable-block slice |
| Extend simultaneous descent to uncountably many block-good loci | attacks the principal selection gap left by Baire |
| Characterize $T_B^\sigma(E)$ intrinsically for coarse blocks | attacks B′(ii) without falsely using points |
| Produce a local compact boundary trap | gives a uniform tail only with a countable-base hypothesis |
| Prove every *localized* minimal trap admits a rooted nonorder | kills localized traps; proving $\Phi$ still needs localization or direct simultaneous selection |
| Find a minimal OML trap with no possible binary root | refutes the proposed rooting programme, not necessarily $\Phi$ |
| Find one strong-state equation violated by every census survivor | gives an architecture-level symbolic kill; requires a reduction to affect full $\Phi$ |

## 17. Next computational and formal tasks

1. **Primary theoretical task:** prove useful face-image openness/closed-defect
   criteria for actual OML overlaps, or replace localization by a direct
   simultaneous-selection theorem.  Local rooting is downstream of this
   quantifier step, not presently the global priority.
2. Compute boundary algebras and trace maps explicitly for the named
   pentagon and 7-loop cells. Separate local trace non-realizability from
   later master geometry and order-separation failures.
3. Search for a distributed finite face in a finite block atlas: every
   state bad at some chosen block but no block trapping the whole face.
   This tests the most dangerous silent strengthening in the PDF picture.
4. For coarse blocks, seek examples where $T_B^\sigma(E)$ is strictly
   larger than the carrier shadow. This guards the B′(ii) scope boundary.
5. A future Lean file should formalize local Boolean state restriction,
   overlap-compatible block families, and the gluing construction. Do this
   only after choosing representations that reuse `IsMaxBlock` and
   `IsSigmaOn`; encoding boundary Stone spaces now would be a substantial
   infrastructure detour, not the requested small certificate.

## 18. Explicit handoff status

Actually proved here: compatible local gluing, boundary surgery,
finite-interface quarantine, the Stone closure formula, conditional Baire
escape, metrizable uniform-tail extraction, and Sasaki-filter closure.
GSD is an exact reformulation, not progress on its universal truth.

Fine/countable only: σ-trace = carrier shadow, the closure-defect reading,
Baire simultaneous escape, the countable-tail lemma, and the atomic-master
semantic-filter equation. **B′(i)** retains both local point-liftability
and simultaneous selection over possibly uncountably many fine blocks.
**B′(ii)** adds the problem of characterizing and selecting non-point
σ-lifts on coarse boundaries. The global arbitrary-atlas selection issue
cuts across both factors; it does not belong exclusively to B′(ii).

The framework supplies one genuinely new lever—the finite-interface
quarantine theorem—and an unconditional localization theorem only for
full-block non-σ failure.  The audit criticism is correct: boundary
non-liftability is strictly weaker, and its distributed cover localizes only
under additional face-image regularity.  The next priority is therefore
**topological boundary regularity or direct simultaneous selection**.
Rootability remains valuable only after a genuine boundary trap has been
localized; larger relay censuses do not bridge this quantifier gap.
