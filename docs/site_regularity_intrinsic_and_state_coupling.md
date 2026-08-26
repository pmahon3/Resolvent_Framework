# Puncture repair and the Ulam completion test

*Audit date: 2026-08-02. No Lean file or sigma-essential dependency-path file
was changed.*

Decision: [`site_regularity_decision_memo.md`](site_regularity_decision_memo.md).

## Verdicts

| Check | Verdict |
|---|---|
| Phase A, ordinary ambient embeddings | **ARTIFACT — FALSIFIER FIRED** |
| Phase A, regular or sigma embeddings | **IMPOSSIBLE** |
| Phase A claimed equivalence | **REFUTED** |
| Phase B family identity | **DERIVED FROM THE SAME CORE FAMILY** |
| Phase B fixed-candidate effect | **FINITE COHERENCE DESTROYED** |
| Phase B effect on `PsiOML` | **CO-LOCATED — OPEN, NOT ADJUDICATED** |

## A. The two puncture legs

Let $C=2^{\mathbb N}$, let

\[
 A=\operatorname{Clop}(C),\qquad
 G_k=C\setminus\{k\},\qquad
 D_k=\operatorname{Borel}(G_k),
\]

and write

\[
 \alpha_k:A\longrightarrow D_k,\qquad
 \alpha_k(U)=U\cap G_k.
\]

The diagonal edge cell in Campaign 11 is isomorphic to $D_k$, so this loses no
interface data. Fix distinct $i,j$ and a decreasing clopen local basis
$(U_n)$ at $i$ with intersection $\{i\}$.

The three internal meets are

\[
 \bigwedge_A U_n=0,\qquad
 \bigwedge_{D_i}\alpha_i(U_n)=0,\qquad
 \bigwedge_{D_j}\alpha_j(U_n)=\{i\}.
\]

The first equality holds because a clopen lower bound is contained in $\{i\}$
and Cantor space has no isolated points. The other two are the corresponding
set intersections in the Borel sigma-algebras.

Each $\alpha_k$ is injective: the symmetric difference of two distinct clopen
sets is a nonempty clopen set, hence contains a point other than $k$.

### A.1 An exact complete Boolean amalgam

For $k=i,j$, let

\[
 X_k=\operatorname{Ult}(D_k)
\]

be the Stone space of Boolean ultrafilters. Restriction along $\alpha_k$ gives a
continuous surjection

\[
 r_k:X_k\longrightarrow\operatorname{Ult}(A)\cong C.
\]

Surjectivity is the Boolean ultrafilter extension theorem. Put
$X_{k,x}=r_k^{-1}(x)$. Since $i$ belongs to $G_j$, evaluation at $i$ is a
principal ultrafilter $\delta_i$ in $X_{j,i}$.

Define

\[
 Z=
 \bigl(X_{i,i}\times\{\delta_i\}\bigr)
 \;\cup\!
 \bigcup_{x\ne i}\bigl(X_{i,x}\times X_{j,x}\bigr)
\]

and take the complete Boolean algebra

\[
 \mathcal B=\mathcal P(Z).
\]

For $E\in D_i$ and $F\in D_j$, set

\[
\begin{aligned}
 \eta_i(E)&=\{(u,v)\in Z:E\in u\},\\
 \eta_j(F)&=\{(u,v)\in Z:F\in v\}.
\end{aligned}
\]

These are unital Boolean homomorphisms. They are injective:

- the first projection of $Z$ is all of $X_i$, so Stone ultrafilters separate
  distinct elements of $D_i$;
- the second projection contains the principal ultrafilter at every point of
  $G_j$: $\delta_i$ covers $i$, and the full fiber product covers every other
  point. Point evaluations already separate distinct Borel subsets of $G_j$.

Let $q:Z\to C$ send $(u,v)$ to their common restriction point. For every
clopen $U$,

\[
 \eta_i(\alpha_i(U))=q^{-1}(U)=\eta_j(\alpha_j(U)).
\]

Thus the two legs agree on the given abstract interface.

They have no accidental common elements. Suppose
$\eta_i(E)=\eta_j(F)$. For any two ultrafilters $u,u'$ in the same
$r_i$-fiber, the definition of $Z$ pairs them with a common second coordinate.
Equality of the two images therefore makes membership in the Stone clopen
$\widehat E$ constant on every $r_i$-fiber. Hence

\[
 \widehat E=r_i^{-1}(K)
\]

for some $K\subseteq C$. The map $r_i$ is a closed quotient map. Both
$\widehat E$ and its complement are saturated and compact, so $K$ and its
complement are closed. Therefore $K$ is clopen,
$E=\alpha_i(K)$, and injectivity of $\eta_j$ gives $F=\alpha_j(K)$.
Consequently, writing $\eta(A)$ for the common interface image,

\[
 \eta_i(D_i)\cap\eta_j(D_j)=\eta(A).
\]

This is a strong amalgam over exactly the prescribed clopen interface.

### A.2 The reconciled ambient meet

In $\mathcal B$, completeness gives

\[
\begin{aligned}
 \bigwedge_n\eta_i(\alpha_i(U_n))
 &=\bigcap_n q^{-1}(U_n)\\
 &=q^{-1}(\{i\})\\
 &=X_{i,i}\times\{\delta_i\}\\
 &=\eta_j(\{i\})>0.
\end{aligned}
\]

Here $X_{i,i}$ is nonempty because $r_i$ is surjective. An ultrafilter of
$D_j$ contains the atom $\{i\}$ exactly when it is the principal ultrafilter
$\delta_i$, which proves the last equality.

The singleton is not identified with zero. Instead, $\eta_i$ does not preserve
the countable meet that already existed in $D_i$:

\[
 \eta_i\!\left(\bigwedge_{D_i}\alpha_i(U_n)\right)=0
 \quad\text{but}\quad
 \bigwedge_{\mathcal B}\eta_i(\alpha_i(U_n))=\eta_j(\{i\})>0.
\]

**Phase A ambient verdict: ARTIFACT — FALSIFIER FIRED.** Ordinary Boolean
embeddings reconcile the family without collapsing distinct elements. The
non-existence/disagreement species distinction is false for arbitrary
enlargements.

### A.3 Why this does not make the site regular

The same computation proves that the prompt's asserted equivalence is false.
In the displayed strong amalgam the site is exactly $\eta(A)$, where the meet
is zero, while its meet in the $j$-leg is $\eta_j(\{i\})$.

The obstruction is independent of the construction. In any common realization
of the fixed legs, let

\[
 S=\eta_i(D_i)\cap\eta_j(D_j).
\]

Every $S$-lower bound of the shared sequence lies in the $i$-leg. Since the
sequence has meet zero in that leg, zero is its only $S$-lower bound. Hence the
meet exists in $S$ and equals zero. Its meet in the $j$-leg remains the nonzero
element $\eta_j(\{i\})$. The inclusion of $S$ into the $j$-leg is non-regular in
every realization.

If both leg embeddings into a complete ambient were regular or preserved the
displayed countable meet, the common ambient meet would have to be both zero
and $\eta_j(\{i\})$, contradicting injectivity.

**Phase A regularity verdict: IMPOSSIBLE.** No realization of these fixed legs
makes every site regular. The complete Boolean construction embeds the legs as
faithful ordinary Boolean subalgebras, but not sigma-homomorphically,
sigma-closedly, or as maximal blocks. The Campaign 11 sigma-boundary
obstruction remains valid at that stronger scope.

**Equivalence verdict: REFUTED.** Having one ambient meet is not equivalent to
regularity of the incident site inclusions.

## B. The Ulam witness

All Lean files were read only. Use the notation

\[
\begin{aligned}
 \Omega&=M_1\times\operatorname{Fin}(4),\\
 A&=\operatorname{coreA}=M_1\times\{0,1\},\\
 B&=\operatorname{coreB}=M_1\times\{0,2\},\\
 C&=\operatorname{coreC}=M_1\times\{1,2\},\\
 D_k&=M_1\times\{k\}.
\end{aligned}
\]

### B.1 Family identity

The lattice-gap family is the pair $\{A,B\}$. Every singleton in $D_0$ is an
$L_1$ lower bound of that pair. Therefore any greatest lower bound must contain
all of $D_0$; since every lower bound is contained in $A\cap B=D_0$, it must
equal $D_0$. The cited normal-form result gives $D_0\notin L_1$, so the meet
does not exist.

On `coreBlock`, the state pattern assigns one exactly to the three cores
$A,B,C$ and zero to their complements. Its finite-intersection obstruction is

\[
 A\cap B=D_0,\qquad
 A\cap C=D_1,\qquad
 B\cap C=D_2,\qquad
 A\cap B\cap C=\varnothing.
\]

Thus the structural pair $\{A,B\}$ is literally a two-member subfamily of the
state-side value-one triple $\{A,B,C\}$.

The Ulam row families are different. For each row they form a countable
disjoint family with co-countable union; the row selection and same-column
pigeonhole argument prove that every sigma-additive two-valued state on `L_1`
is Dirac. Rigidity combined with the empty core kernel proves that no such
state extends the core pattern. The missing meet belongs to the finite-core
coherence mechanism, not to the row-rigidity family.

**Family verdict: DERIVED FROM THE SAME CORE FAMILY.**

### B.2 The least same-base completion

There are two relevant completion notions.

First, let

\[
 \widehat L_{\mathrm{lat}}=\sigma(L_1)
\]

be the sigma-algebra generated by the sets of $L_1$, viewed as a Dynkin system.
It is the least same-base Dynkin extension satisfying `MeetsExist`. Indeed,
$L_1$ contains every singleton. Any same-base Dynkin extension with
`MeetsExist` still contains them, so
`ConcreteOMLBlocks.interClosed_of_singletons` makes it intersection-closed and
hence a sigma-algebra. It must therefore contain `sigma(L_1)`. Conversely,
set intersection supplies every binary meet in $\sigma(L_1)$.

Second, the underlying-poset MacNeille completion is

\[
 \widehat L_{\mathrm{MN}}=\mathcal P(\Omega).
\]

Every subset $X$ of $\Omega$ is both the join of its singleton subsets and the
meet of the co-singletons indexed by $\Omega\setminus X$. All those singletons
and co-singletons already lie in $L_1$, so $L_1$ is join- and meet-dense in
$\mathcal P(\Omega)$.

Both completions contain $D_0$ and give $A\wedge B=D_0$. The six-event finite
complement-closed object called `coreBlock` remains a `Block` after either
completion; it is not a maximal Boolean block. The same majority truth
assignment remains a well-defined `LocalState`. Completion does not affect
statability.

### B.3 Adjoining the first missing meet destroys coherence

The full completions are not needed. Let $L^+$ be the Dynkin system generated
by $L_1$ and $D_0$. Difference closure supplies

\[
 D_1=A\setminus D_0,\qquad D_2=B\setminus D_0,
\]

and the following are disjoint decompositions in $L^+$:

\[
 A=D_0\sqcup D_1,\qquad
 B=D_0\sqcup D_2,\qquad
 C=D_1\sqcup D_2.
\]

Suppose a finitely additive two-valued state $\mu$ on $L^+$ extended the core
pattern. Then

\[
 \mu(A)=\mu(B)=\mu(C)=1.
\]

There are two cases.

- If $\mu(D_0)=1$, disjointness forces $\mu(D_1)=\mu(D_2)=0$, contradicting
  $\mu(C)=1$.
- If $\mu(D_0)=0$, additivity on $A$ and $B$ forces
  $\mu(D_1)=\mu(D_2)=1$, impossible because $D_1$ and $D_2$ are disjoint.

Therefore the transported pattern is not `FinitelyCoherent` on $L^+$, and the
same is true on every further same-base concrete completion. In an
intersection-closed completion the shorter calculation is

\[
 \mu(A)=\mu(B)=1
 \Longrightarrow \mu(A\cap B)=\mu(D_0)=1,
 \qquad D_0\perp C,
\]

which contradicts $\mu(C)=1$.

The no-sigma-extension conjunct persists: a sigma-additive state on any
same-base concrete supercarrier extending the pattern would restrict to one on
$L_1$, contrary to `s_0_no_sigma_extension`. What changes is finite coherence.
Hence

| Carrier | `MeetsExist` | `IsSigmaEssential` for the core pattern |
|---|---:|---:|
| $L_1$ | false | true |
| $\sigma(L_1)$ or $\mathcal P(\Omega)$ | true | false |

**Fixed-candidate verdict: FINITE COHERENCE DESTROYED.** The forced meet is a
direct obstruction to transporting this state witness to a lattice
completion.

### B.4 This completion does not adjudicate `PsiOML`

The premise that `PsiOML` is a proposition about the Ulam witness is false. Its
definition is

\[
 \exists (\Omega,d,\mathcal K,s_0),\qquad
   \operatorname{MeetsExist}(d)\ \wedge
   \operatorname{IsSigmaEssential}(s_0).
\]

It contains no reference to `L_1`, `U_1`, or the Ulam core pattern. The same
finite block and local pattern remain statable after completion. The original
Ulam tuple fails the `MeetsExist` conjunct; each completed tuple fails the
`IsSigmaEssential` conjunct. None is a `PsiOML` witness, so this calculation
neither proves nor refutes the closed existential.

**Phase B verdict: CO-LOCATED FOR `PsiOML`; OPEN — NOT ADJUDICATED.** The
fixed candidate has a direct completion/state interaction, but that fact does
not decide the global proposition named `PsiOML`.

## Sources inspected

- `notes/open_questions/oml_attack/oml_distributed_relation_cell_assembly.md`
- `formalization/QuerySystem/QuerySystem/UlamWitnessLatticeGap.lean`
- `formalization/QuerySystem/QuerySystem/UlamWitnessCore.lean`
- `formalization/QuerySystem/QuerySystem/UlamWitnessOmega1.lean`
- `formalization/QuerySystem/QuerySystem/UlamWitnessState.lean`
- `formalization/QuerySystem/QuerySystem/SigmaEssentialWitness.lean`
- `formalization/QuerySystem/QuerySystem/ConcreteOMLBlocks.lean`
