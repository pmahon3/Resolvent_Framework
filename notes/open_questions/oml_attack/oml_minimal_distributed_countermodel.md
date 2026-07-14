# Minimal distributed countermodels and realization gates

*Campaign 3, 2026-07-13. No construction below is claimed to be an
admissible OML counterexample.*

## 1. Exact compact-ambient relational countermodel

Let `C=2^N` and index constraints by `I=C`. Put `G_i=C\{i}` and let the
eligible fibre at `i` be a singleton exactly when `mu in G_i`. Then

`X(J) = C\J`

for every `J subset I`, and the bonding maps are the inclusions
`C\K -> C\J` for `J subset K`.

Every countable subsystem has a section, while `X(I)=empty`. Every nonempty
finite-coordinate cylinder has cardinal continuum, so after any such
refinement it still escapes every countable family of defects. Eligibility
is open and nonclosed, and `X(J)` is generally noncompact; only the ambient
face and its finite-coordinate cylinders are compact zero-dimensional
spaces. This is precisely why compact FIP does not apply and why the
requested compact eligible-system gate is not met.
**Evidence class: hand proved.**

Any singleton-cover CSS-without-GS model needs an uncountable index set.
Cardinality `aleph_1` suffices abstractly, but the Cantor model supplies the
compact zero-dimensional homogeneous finite-coordinate structure. **Evidence
class: hand proved.**

Finite gate controls are:

- singleton failure: `C={0}, G_0=empty`;
- pair failure: `C={0,1}, G_0={0}, G_1={1}`;
- conditional Helly-3 failure:
  `C={0,1,2}, G_i=C\{i}`.

These are abstract controls only. **Evidence class: hand proved.**

## 2. Standard-Borel relation realization

Let `X` be Cantor space, let `d<omega`, and let `R` be a Borel subset of
`X^d` equipped with its trace sigma-algebra. Dense coordinate projections
ensure local nonemptiness but are not needed for the equality below. Let
`B_R=Borel(R)` and embed each
`Clop(X)` boundary by coordinate preimage.

### Theorem 2.1 (relation realization)

The image under restriction to the `d` coordinate clopen algebras is `R`
for sigma-additive two-valued states, while for finitely additive states it
is `closure(R)` in `X^d`.

*Proof.* A sigma-additive two-valued state on the countably generated
separating Borel algebra is evaluation at one point of `R`. A tuple of
coordinate traces extends finitely additively exactly when every finite
clopen cylinder around it meets `R`, equivalently when it belongs to
`closure(R)`; the Boolean ultrafilter lemma completes the state.
**Evidence class: hand proved.**

Thus the punctured relation `X\{x}` realizes the singleton defect locally.
More generally, local sigma-lift relations are not arbitrary: their
finitely additive loci are forced to be their closures.

## 3. First exact Boolean realization obstruction

### Theorem 3.1 (singleton exposure)

Let `A` be a countably generated sigma-field separating points of `C`. For
every `i in C`, the restriction map `A -> P(C\{i})` is not injective.

*Proof.* Choose a countable separating generator `(A_n)`. The intersection
of the chosen sides `A_n` or `A_n^c` containing `i` is `{i}`, hence
`{i} in A` and restricts to the empty set. **Evidence class: hand proved.**

Therefore the Cantor singleton trap cannot use a countably generated
separating sigma-boundary as an injectively embedded overlap. It must use an
uncountably generated or nonseparating boundary, or distribute coordinates
so that no one overlap measures the forbidden singleton.

## 4. Noncentral transport audit

Invertible deterministic transport does not distribute the boundary. If a
homeomorphism `h` enforces `y=h(x)`, the two embedded clopen boundary ranges
inside the transport block coincide. Along a connected coherent cocycle
network, all copies therefore identify with one common boundary. A coherent
invertible cocycle has trivial cycle holonomy and its edge labels can be
gauged away. Nontrivial cycle holonomy is incompatible with faithful literal
identification. **Evidence class: hand proved.**

Noninjective deterministic maps can yield proper nested ranges, but transport
only a quotient; placing the singleton defect on that quotient recreates a
common quotient boundary. Genuine noncentral transport must use
nondeterministic, nonclosed Borel correspondences with proper coordinate
subalgebras. **Evidence class: hand proved.**

## 5. Lattice-cut audit

The raw crossed three-block union fails complement/disjoint-union closure.
Its canonical finite completion has 56 events, seven maximal blocks,
all binary meets and joins, trivial centre, sigma-completeness, and
point-state order separation, but every boundary saturates. **Evidence
class: exhaustive finite evidence.**

The 44-event five-block subcompletion disproves any general claim that mixed
OML completion forces saturation: it is a centre-free sigma-complete OML
with exhaustive maximal blocks, order separation, and a proper boundary.
Its arbitrary-base one-coordinate inflation remains Phi-tame by common-fibre
point replacement. **Evidence class: exhaustive finite evidence** for the
finite gates; **evidence class: hand proved** for arbitrary-base structure
and tameness.

### Theorem 5.1 (repeated-selector invariance)

If two Boolean blocks contain the same events `e,f`, the Boolean
subalgebras generated by `e,f` coincide as embedded sub-OMLs: their four
regions are the intrinsic lattice elements
`e meet f`, `e meet f^perp`, `e^perp meet f`, and
`e^perp meet f^perp`. Consequently repeated containment of one selector pair
cannot create inequivalent quotient edges or monodromy. **Evidence class:
hand proved.**

## 6. Campaign verdict and narrow realization theorem

The compact-ambient relational model is complete and its local relations have exact
Boolean realizations, but the common-boundary paste centralizes, countably generated
sigma-boundaries expose the omitted singleton, and invertible transports
identify their ranges. The 44-event control shows that lattice completion
alone does not force saturation.

The narrowest live realization problem is:

> **Nondeterministic transported-boundary realization theorem.** Determine
> whether a finite-degree network of nonclosed standard-Borel
> correspondences with proper coordinate subalgebras, CSS on every countable
> subsystem and no global solution, can be completed to a concrete
> sigma-complete centre-free OML while preserving the correspondence
> relations and sigma-state order separation.

A positive realization counts only if it also supplies a fixed finite
pattern `p`, one global compatible finitely additive state realizing `p`,
sigma-sections on every required finite/countable subsystem, no global
sigma-section realizing `p`, and the exact GSD identification between
global sections and global sigma-states. A negative theorem must identify
the mixed cut that forces a functional quotient, boundary enlargement, or
loss of order separation. **Evidence class: open.**

The first concrete test is a two-coordinate inflation of distinct
non-atomic selector families in the 44-event survivor, with gates ordered:
faithfulness, complement/disjoint-union closure, meets/joins, maximal blocks,
centre, boundary relation, sigma-completeness, and order separation.
