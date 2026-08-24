# OML distributed-boundary compactness: exact formulation

*Campaign 1, 2026-07-13. Unless marked otherwise, claims in this note are
hand proved. This note replaces the deliberately conceptual ODBC paragraph in
`oml_endgame_selection_residue.md`.*

## 1. Fixed data

Let (L\subseteq\mathcal P(\Omega)) be an admissible concrete
sigma-complete OML, with maximal Boolean sigma-block atlas
(I=\mathfrak B(L)). Admissible has exactly the repository meaning:
non-Boolean where relevant, essentially irreducible where relevant, and with
sigma-additive two-valued states separating order. No hypothesis is dropped
below.

Fix a finite complement-closed pattern (p) and write

\[
C_p=\{\mu\in\operatorname{St}_{fa}(L):\mu|_{\operatorname{dom}p}=p\}.
\]

The pattern is *coherent* when (C_p\ne\varnothing). For (B\in I), let
(\partial B\) and (E_B(p)) be exactly those of
`relational_boundary_descent.md` Sections 3--4. Define the eligible lift fibre

\[
Y_B(p,\mu)=\{v\in\operatorname{St}_\sigma(B):
 v(E_B(p))=1,
 v|_{\partial B}=\mu|_{\partial B}\}.
\]

The full global state (mu), rather than only an independently chosen
boundary trace, is load-bearing.

## 2. Index system and sections

Let

\[
\mathcal J_{\le\omega}(I)=\{J\subseteq I:|J|\le\aleph_0\}
\]

ordered by inclusion. It is directed: (J,K\le J\cup K), and countable
unions of its objects remain objects. Finite subsystems form
(\mathcal J_{<\omega}(I)). A subsystem is a set of maximal blocks, not a
finite set of boundary events.

For arbitrary (J\subseteq I), define

\[
X_p(J)=\{(\mu,(v_B)_{B\in J}):
 \mu\in C_p,\ v_B\in Y_B(p,\mu)\text{ for every }B\in J\}.
\]

An element of (X_p(J)) is a *(J)-section*. For (J\subseteq K), the
bonding map

\[
\rho^K_J:X_p(K)\to X_p(J)
\]

keeps (mu) and forgets the (v_B) with (B\notin J). Hence
(\rho^J_H\rho^K_J=\rho^K_H). A compatible family over a collection
\(\mathcal D) of subsystems is a tuple (s_J\in X_p(J)) with
(\rho^K_J(s_K)=s_J) whenever (J\subseteq K) lie in \(\mathcal D).
Because restriction keeps (mu), every compatible family uses one common
global finitely additive state.

A *global section* is an element of (X_p(I)). Equivalently it is one
(mu\in C_p) and one eligible local sigma-lift for every maximal block,
all matching that same (mu) on their boundaries.

### Lemma 2.1 (inverse-limit identification)

The natural map

\[
X_p(I)\longrightarrow
\varprojlim_{J\in\mathcal J_{\le\omega}(I)}X_p(J)
\]

is a bijection. The same holds with all finite subsystems.

*Proof.* Restriction gives the forward map. Conversely, compatibility makes
the retained (mu) independent of (J). For (B\in I), read (v_B) from
the singleton subsystem ({B}); compatibility with two-element
subsystems gives the same coordinate in every larger subsystem. These data
form an element of (X_p(I)). The two constructions are inverse. ∎

This lemma does **not** say that nonemptiness of every (X_p(J)) produces a
compatible inverse-limit family.

## 3. Three distinct assertions

For fixed (L,p), distinguish:

1. **Pointwise local nonemptiness (PLN):**
   (Y_B(p,\mu_B)\ne\varnothing) for each (B), with (mu_B) allowed to
   depend on (B).
2. **Countable subsystem solvability (CSS):**
   (X_p(J)\ne\varnothing) for every countable (J\subseteq I). Each
   section has one common (mu_J), but (mu_J) may depend on (J).
3. **Global solvability (GS):** (X_p(I)\ne\varnothing).

Then GS implies CSS implies finite subsystem solvability. Neither PLN nor
singleton (X_p(\{B\})\ne\varnothing) is CSS. Moreover CSS is not the
existence of a compatible family of choices (s_J\in X_p(J)); by Lemma 2.1
the latter is already GS.

## 4. Exact principles

### Definition 4.1 (conditional ODBC compactness, CODBC)

(L) satisfies **CODBC** when, for every coherent finite pattern (p),

\[
[\forall J\in\mathcal J_{\le\omega}(I),\ X_p(J)\ne\varnothing]
\quad\Longrightarrow\quad X_p(I)\ne\varnothing.
\]

Finite-CODBC is the stronger principle (with the weaker antecedent) using
\(\mathcal J_{<\omega}(I)\) in place of countable subsystems. CSS is stronger than its
finite version, so finite-CODBC implies CODBC.

### Definition 4.2 (ODBC)

(L) satisfies **OML distributed-boundary compactness (ODBC)** when every
coherent finite pattern (p) satisfies both:

- **ODBC-S (subsystem sections):** (X_p(J)\ne\varnothing) for every
  countable (J\subseteq I);
- **ODBC-G (globalization):** CSS implies (X_p(I)\ne\varnothing).

Thus ODBC is ODBC-S plus CODBC. This two-clause statement is intentional.
The earlier conceptual statement suppressed ODBC-S; hostile review showed
that CODBC alone cannot imply Phi. Finite coherence of (p) solves finite
sets of event equations, not all overlap equations in even two whole
blocks.

### Theorem 4.3 (ODBC implies finite-trace sigma-liftability)

Every admissible (L) satisfying ODBC satisfies (Phi(L)).

*Proof.* Fix coherent (p). ODBC-S gives CSS and ODBC-G gives an element
((\mu,(v_B))\in X_p(I)). By definition, every (v_B) charges (E_B(p))
and agrees on (\partial B) with the same (mu). The boundary-compatible
sigma-surgery theorem glues the (v_B) to one global sigma-additive
two-valued state realizing (p). This is GSD, and Theorem 4.3 of
`relational_boundary_descent.md` proves GSD iff Phi. ∎

In fact ODBC as a whole is extensionally equivalent to GSD/Phi, because GS
implies both clauses. Its value is not logical weakening but the exact
factorization of the open proof obligation into subsystem solvability and
globalization. CODBC is the nontrivial compactness component; ODBC-S is a
separate OML theorem obligation.

## 5. Fine ODBC

Assume every maximal block is countably generated. For a block (B), every
local sigma-state is principal on a nonempty atom (D\in B). Hence one may
replace (Y_B(p,\mu)) by

\[
A_B(p,\mu)=\{D:\ D\text{ is a nonempty atom of }B,
 D\subseteq E_B(p),\ \delta_D|_{\partial B}=\mu|_{\partial B}\},
\]

where (delta_D) is the common point state of points in the block atom.
The resulting section spaces (X_p^{\rm fine}(J)) are canonically
bijection-equivalent to (X_p(J)). **Fine ODBC** is ODBC-S plus ODBC-G for
these atomic section spaces. T4At supplies hereditary one-block atomic
escape after each finite face refinement; it does not supply fine ODBC-S
for a two-block or countable subsystem.

## 6. Coarse ODBC

For arbitrary (B), let \(\mathcal C(B)) be the directed poset of
countably generated Boolean sigma-subalgebras (C\subseteq B). For fixed
(mu), define (Z_{B,C}(p,\mu)) to be the sigma-additive two-valued states
on (C) agreeing with (mu) on (C\cap\partial B), and charging
(E_B(p)) whenever (E_B(p)\in C). Restriction along (C\subseteq D)
gives the bonding maps.

An *eligible coarse lift* is a compatible family
((u_C)_{C\in\mathcal C(B)}) in these spaces. Section 4 of
`oml_endgame_selection_residue.md` proves that eligible coarse lifts are
canonically equivalent to elements of (Y_B(p,\mu)): the union is a
sigma-state on (B), and every countable additivity test lies in one
countably generated envelope.

Define (X_p^{\rm coarse}(J)) by replacing every (v_B) in (X_p(J)) by
an eligible coarse lift, while retaining the same global (mu).
**Coarse ODBC** is ODBC-S plus ODBC-G for these two-level section spaces.
Mere nonemptiness of every (Z_{B,C}) is not eligibility. The club-field
example gives all separate local lifts but no compatible family and is the
standing control.

## 7. Failure data and realization gates

An actual failure of ODBC-G in an admissible (L) consists of a coherent
finite (p) such that every countable block subsystem has a common-witness
section but (X_p(I)=\varnothing). By GSD this is already a concrete
counterexample to Phi; no further realization gate remains.

An *abstract ODBC countermodel* consists only of an atlas (I), sets
(C_p,Y_B(p,\mu)), and restriction maps satisfying CSS but not GS. It is a
counterexample skeleton, not an OML. To become a counterexample it must
still pass, separately: Boolean sigma-field realization of blocks and
overlaps; cocycle-consistent noncentral transport; closure under complement
and countable disjoint unions; all binary meets and joins; orthomodularity;
maximal-block classification; sigma-completeness; the repository's centre
and essential-irreducibility conditions; concrete set realization;
sigma-state order separation; and identification of the abstract section
spaces with the actual boundary lift spaces of the realized OML.

Failure of ODBC-S inside an actual admissible OML supplies a coherent finite
pattern and a countable block subsystem with no common-witness section.
Restriction rules out a global section, so GSD already makes this an actual
Phi counterexample; it is not a failure of CODBC. Failure of abstract ODBC-S
supplies only a skeleton and still requires the realization gates above.

## 8. Evidence ledger and immediate theorem residue

| Claim | Evidence class |
|---|---|
| Definitions of (X_p(J)), restriction maps, sections | hand proved |
| Lemma 2.1 inverse-limit identification | hand proved |
| ODBC implies Phi via GSD | hand proved |
| Fine atomic reformulation | hand proved |
| Coarse two-level reformulation | hand proved |
| CODBC for admissible OMLs | open |
| ODBC-S for admissible OMLs | open |
| Full ODBC / Phi | open |

The exact positive task is now two theorems, not one silently ambiguous
one: prove ODBC-S and CODBC for every admissible OML. A refutation of either
inside an actual admissible OML yields a Phi counterexample; an abstract
refutation must pass all gates in Section 7.
