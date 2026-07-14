# Distributed relation-cell assembly

*Campaign 11, 2026-07-14. The punctured-Cantor hub is realized as an exact
Boolean CSP but cannot be pasted through one faithful shared sigma-boundary.
Distributed nonseparating quotient copies remain open.*

## 1. Minimal dense-edge star

Let `C=2^N` and index constraints by `I=C`. There is one hub variable
`x in C`. For `i in I` put

\[
 G_i=C\setminus\{i\},\qquad F_i=\overline{G_i}=C.
\]

Adding a singleton dummy leaf makes the sigma and finitely additive edge
relations

\[
 R_i^\sigma=G_i\times\{*\},\qquad R_i^{fa}=C\times\{*\}.
\]

For `J subset I`, the sigma-section space is `C\J`. Hence every countable
subnetwork has a section, the full network has none, and every `x in C` is a
global finitely additive section. Every global sigma-section locus is empty,
so it misses every finite cylinder containing a chosen finitely additive
section. **Evidence class: hand proved.**

This system has finite arity but one hub of uncountable incidence. By the
locally-countable component theorem, no locally countable finite-arity
CSS-without-GS system exists. Thus one hub variable is minimal and an
uncountable index is necessary (`aleph_1` suffices abstractly), while Cantor
space supplies homogeneous finite-coordinate cylinders. **Evidence class:
hand proved.**

## 2. Exact local Boolean edge-cell realization

Let `A=Clop(C)`. For `i in C` set

\[
 R_i=\{(x,x):x\in C\setminus\{i\}\},\qquad
 B_i=Borel(R_i).
\]

Embed each endpoint copy of `A` by the corresponding coordinate preimage.
The embedding is injective because every nonempty clopen set contains a
point other than `i`. Sigma-additive two-valued states on `B_i` are point
evaluations, so their hub trace is `C\{i}`. Finitely additive traces are its
closure `C`, by the Boolean ultrafilter extension theorem. Thus each local
Boolean edge cell realizes the required punctured hub trace (with a private
Cantor endpoint rather than the optional singleton dummy). Identifying the
hub copies is exactly the gluing operation ruled out below. **Evidence
class: hand proved.** The cells are not yet a pasted Boolean atlas, OMP, or
OML.

## 3. Shared-boundary countable-cut obstruction

### Puncture meet theorem

No concrete sigma-complete OML can contain two distinct puncture cells
`B_i,B_j` as faithful sigma-closed Boolean blocks while identifying their
full clopen hub boundary.

*Proof.* Choose distinct `i,j` and a decreasing clopen basis `(U_n)` at `i`
with intersection `{i}`. In the `i`-puncture block,

\[
 \bigwedge_n (U_n\cap G_i)=0.
\]

In the `j`-puncture block the same identified boundary sequence has meet

\[
 \bigwedge_n (U_n\cap G_j)=\{i\}\ne0.
\]

In a concrete sigma-complete event lattice, the meet of a decreasing
sequence is intrinsic (equivalently, use complements and the countable
orthogonal-join closure). One sequence cannot have both values. **Evidence
class: hand proved.**

Equivalently, any faithful shared countably generated point-separating
sigma-envelope contains every singleton. Its preimage in the matching
puncture cell is empty, contradicting injectivity. This obstruction is
independent of centrality. Starting from `Clop(C)` does not help: sigma
closure generates the Borel singletons. **Evidence class: hand proved.**

Thus the common-boundary and common-envelope Cantor stars fail already at
two cells. Allowing embeddings that do not preserve these countable meets
would discard the intended sigma-state semantics.

## 4. Transported-cell paste and completion gates

For an incidence hypergraph `H=(V,E)`, choose Boolean sigma-algebras `A_v`,
concrete sigma-complete OML cells `M_e`, and incidence embeddings

\[
 j_{ev}:A_v\hookrightarrow M_e.
\]

The algebraic transported paste identifies `j_ev(a)` and `j_fv(a)` for
cells incident at the same vertex, and makes no other identifications.
Connectedness alone does not make distinct vertex algebras central.

An admissible completion must separately pass:

1. faithful cell and boundary embeddings;
2. all mixed lattice cuts and the orthomodular law;
3. countable orthogonal-join closure;
4. exhaustive maximal-block classification;
5. maximal-block relational conservativity;
6. trivial centre/essential irreducibility;
7. order separation by sigma-additive two-valued states.

**Evidence class: exact definition.** Existence for arbitrary index systems
is open.

## 5. Full-block inverse-limit theorem

A maximal block of a sigma-complete OML need not itself be sigma-complete.
For a maximal block `B`, define an **L-relative sigma-state** to be a
finitely additive two-valued state on `B` that is countably additive for
every orthogonal sequence in `B` whose join computed in `L` also belongs to
`B`.

For a sigma-complete OML `L`, restriction gives a bijection between global
sigma-additive two-valued states and compatible L-relative sigma-states on
the complete maximal-block atlas. A compatible tuple defines the value of
an event in any containing block. For a global orthogonal sequence `(x_n)`
with L-join `x`, the jointly compatible family `{x_n:n in N} union {x}` is
contained in a maximal Boolean block. Relative additivity in that block
gives the global equation. Restriction and gluing are inverse. The finitely
additive analogue omits the relative countable condition. **Evidence class:
hand proved.** No sigma-completeness of maximal blocks is asserted.

Consequently the original cell atlas never suffices for the state audit:
every maximal block created by mixed-cut completion is load-bearing.

## 6. Maximal-block relational conservativity

Let `R` be an abstract boundary system and let `U` be the pullback of a
finite event-evaluation cylinder on actual events of `L`.
For an admissible transported-cell completion `L`, define **MBRC on `U`** to
mean that projection of the compatible sigma-state inverse limit over the
full maximal-block atlas is exactly the intended global sigma-solution set
inside `U`.

If:

1. there exists a state in `St_fa(L)` projecting to a global finitely
   additive solution in `U`;
2. the intended sigma system has no global solution in `U`; and
3. MBRC holds on `U`,

then `L` fails Phi. **Evidence class: hand proved.**

Failure of MBRC need not be witnessed by one new block: an uncountable
family of new blocks can be separately compatible on every small subsystem
but fail globally. The safe discrepancy classification is only:

- intended solutions may fail to extend through the complete new-block
  inverse system; or
- the completed inverse system may project additional boundary profiles.

**Evidence class: hand-audited correction.** No finite-witness claim is
made.

## 7. Activation and concreteness lemmas

If an event belongs to every maximal block, it commutes with every event and
is central. Thus a centre-free assembly has no proper universal-block
activation event. **Evidence class: hand proved.**

Suppose a finite pattern lies in one finite Boolean subalgebra and is
represented by its nonzero face event `c`. If every sigma-state charging
`c` charges a cell activator `a_e`, then sigma-state order separation gives
`c<=a_e`: otherwise a separating state charges `c` and kills `a_e`.
**Evidence class: hand proved.** This lemma does **not** apply to a general
finite pattern containing incompatible events; no single face event may
represent such a pattern.

An abstract sigma-complete OML with order-separating sigma-additive
two-valued states has the canonical concrete representation

\[
 x\mapsto\{\mu:\mu(x)=1\}.
\]

It preserves order, complement, and countable orthogonal joins and is
injective. Hence construction may proceed abstractly if the full state gate
is subsequently proved. **Evidence class: hand proved.**

## 8. Exact residue

The minimal abstract uncountable-hub obstruction and its local Boolean
relations are complete. The shared faithful sigma-boundary realization is
closed by the puncture meet theorem. The principal remaining construction
class must:

- distribute only proper nonseparating quotient coordinates;
- use conditional noncommuting selector faces rather than one shared
  shrinking basis;
- reconstruct global hub coherence at state level without reconstructing a
  faithful common sigma-boundary at event level;
- pass MBRC over the complete maximal-block atlas.

The puncture theorem closes shared countably generated separating
sigma-boundaries. It does not exclude an uncountably generated separating
sigma-boundary with no measurable singleton or countable puncture basis;
that remains a second logical escape alongside distributed nonseparating
quotient copies.

The smallest falsifiable control is a three-cell star made from conditional
diagonal cells with distinct quotient supports. Its canonical completion
must be audited for new cuts, maximal blocks, centre, and the charged
three-coordinate relation. Pairwise preservation is insufficient.

Admissible Hub Compactness is exactly ODBC in hub language, so its universal
truth is equivalent to Phi and either clause's failure *inside an admissible
OML* supplies a counterexample. This equivalence is an integration check,
not a new solution or a legitimate stopping condition. **Evidence class:
hand proved.**
