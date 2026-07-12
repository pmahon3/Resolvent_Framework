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

### Theorem 6.1 (finite-interface quarantine) ⟦LEAN, `BoundaryDescent.lean`; independent review cleared⟧

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

### Proposition 9.0 (finite fine-atlas localization after face refinement) ⟦HAND, proved⟧

Suppose the atlas has finitely many fine blocks and $C_p$ is nonempty.  If
their defect loci cover $C_p$, then some defect locus contains a nonempty
relatively clopen finite-cylinder subface.  Equivalently, after adjoining
finitely many coordinates to $p$, one obtains a nonempty locally trapped
face.

*Proof.*  In the fine-block slice the good locus is the union of the clopen
cylinders charging a block atom (equivalently, realized by a point), so each
defect locus is relatively closed.  The compact Hausdorff face $C_p$ is
Baire.  A finite closed cover cannot consist entirely of sets with empty
interior, hence one defect locus has nonempty relative interior.  The Cantor
cube topology has a clopen finite-cylinder base, and intersecting such a
cylinder with $C_p$ is exactly a coherent finite pattern refinement. ∎

The original face need not itself be locally trapped.  The finite relational
trace table $C_p=\{0,1,2\}$ with $D_{B_i}=\{i\}$ is an irredundant distributed
cover; `verification/distributed_trap_audit.py` is an executable receipt.
That table is **not** claimed realizable by a concrete σ-class OML.  It shows
that the cover equation alone cannot prove localization.  The proposition
shows, conversely, that a finite fine-block counterexample minimal also under
finite face refinement must be locally trapped.  Coarse blocks and arbitrary
uncountable atlases remain outside this reduction.

### Lemma 9.1 (uniform tail under a countable-base hypothesis) ⟦HAND, proved⟧

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
| Compact trapped image always gives a countable tail | **insufficiently justified** | compact nonmetrizable Stone spaces need not have countable neighbourhood bases; Lemma 9.1 adds metrizability |
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
             |                         |
             v                         v
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
| Boundary-compatible σ-local replacements glue globally | Full generality for concrete σ-class OMLs | **proved ⟦HAND⟧** | certified block coverage and blockwise σ theorem |
| GSD is equivalent to $\Phi$ | Full generality | **exact reformulation ⟦HAND⟧** | gluing theorem |
| Finite-interface quarantine | Arbitrary maximal blocks, every $\partial B$ finite | **⟦LEAN, `BoundaryDescent.lean`; independent review cleared⟧** | boundary surgery + choice |
| Boundary closure-defect characterization | closure equality: any concrete block; σ=shadow: countably generated block | **proved ⟦HAND⟧ + certified point realization** | Stone compactness, concreteness, T3 |
| Baire simultaneous escape | Countably many countably generated blocks | **proved conditionally** | hereditary local density on every finite refinement |
| Uniform countable tail extraction | compact trapped image in compact metrizable boundary Stone space | **proved conditionally** | countable clopen base; not distributed trapping |
| Sasaki-filter formulation | Any OML two-valued f.a. state; master equivalence only in countably atomic slice | **proved at stated scope** | orthomodularity + finite additivity |
| Rooted-tail dichotomy | Full conjectural architecture | **open** | missing rooting theorem |
| Relay/master normal form | Periodic/bounded-width one-master searches | **architecture-specific; not a full reduction** | extra relay/master hypotheses |

## 16. What would settle what

| Result | Consequence |
|---|---|
| Prove GSD directly for all fine blocks | settles B′(i), hence the fine half only |
| Prove hereditary one-block escape with countably many fine blocks | Baire theorem gives that countable-block slice |
| Extend simultaneous descent to uncountably many block-good loci | attacks the principal selection gap left by Baire |
| Characterize $T_B^\sigma(E)$ intrinsically for coarse blocks | attacks B′(ii) without falsely using points |
| Produce a local compact boundary trap | gives a uniform tail only with a countable-base hypothesis |
| Prove every minimal trap admits a rooted nonorder | concreteness/order separation kills every trap, proving $\Phi$ |
| Find a minimal OML trap with no possible binary root | refutes the proposed rooting programme, not necessarily $\Phi$ |
| Find one strong-state equation violated by every census survivor | gives an architecture-level symbolic kill; requires a reduction to affect full $\Phi$ |

## 17. Next computational and formal tasks

1. **Best next falsification task:** on the existing s35--s38 finite
   survivors and killed candidates, enumerate candidate roots generated by
   bounded-depth Sasaki terms and test whether the full separating face is
   contained in the computed all-remainder defect. A counterexample to
   rootability is as valuable as a common root.
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
quarantine theorem—and a clean localization of the obstruction. Beyond
that tame slice it is primarily a better description of T4 and the
selection problem. The single best next task is to **prove or falsify
rootability of minimal boundary defects on the existing finite cells**;
without such a theorem, larger relay censuses do not bridge to the full
conjecture.
