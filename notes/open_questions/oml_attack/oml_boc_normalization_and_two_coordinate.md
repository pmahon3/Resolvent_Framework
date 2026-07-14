# BOC normalization and two-coordinate selector tests

*Campaign 8, 2026-07-13. This campaign reaches the mandatory 60 meaningful
iterations but does not settle Phi.*

## 1. Locally countable component theorem

Consider a finite-arity constraint system and form its full bipartite
incidence graph, including every state, witness, envelope, coherence
coordinate, and constraint vertex. Assume each variable is incident with at
most countably many constraints. A countable subsystem here contains all
variables and constraint vertices in the induced connected component; it is
stronger than a block-label subsystem if hidden coordinates are suppressed.

### Theorem 1.1

Every connected component is countable. If every countable subsystem has a
section, the full system has a section.

*Proof.* Breadth-first closure from one variable adds at most countably many
vertices at each finite distance. Each component is therefore countable.
Use choice to select a section on each component and combine them; distinct components
share no constraint. **Evidence class: hand proved.**

### Corollary 1.2

In a locally countable finite-arity system, every no-global-section
obstruction is witnessed on one countable component. Genuine CSS-without-GS
requires an uncountable-incidence variable or an infinite-arity/global
constraint. **Evidence class: hand proved.**

The common finitely additive witness counts as a coordinate. Suppressing it
from the block-overlap graph invalidates any finite-degree claim. Duplicating
it with local equality constraints cannot impose equality across an
uncountable atlas while components remain countable. **Evidence class: hand
proved.**

## 2. Controls and revised normalization

The Cantor singleton system has one witness variable incident with continuum
many exclusion constraints. For the club/CIR control, local Dirac choices
vary; nevertheless Corollary 1.2 says any faithful finite-arity CSP encoding
of its CSS/no-GS defect must expose uncountable incidence, and the natural
envelope system has highly incident extension/coherence coordinates.
Neither is a finite-degree N-G example. **Evidence class: hand proved.**

Finite-degree N-S remains nonvacuous. On a ray, take variables in
`N times R` and the nonclosed standard-Borel edge relation

`((n,s),(m,t)) in R iff n>m and s!=t.`

Every finite path has a section, while the countable ray has none because it
would give an infinite descending sequence in `N`. **Evidence class: hand
proved.**

Any BOC normalization through finite-arity CSPs must therefore distinguish:

- **N-S-local:** locally countable finite-arity standard-Borel systems,
  whose failures are countably witnessed;
- **N-G-hub/coarse:** CSS-without-GS with an explicitly marked
  uncountable-incidence hub, infinite-arity constraint, or coarse
  inverse-limit coordinate.

This refutes finite-degree normalization of N-G; completeness of BOC
normalization itself remains open. **Evidence class: refuted.**

## 3. Exhaustive selector-pair proxy

The exact 44-event survivor has 10 lattice atoms and 32 non-atomic
selectors. All 496 unordered selector pairs were recomputed.

- 485 admit a joint concrete point state;
- 135 lie in a common certified block with all three regions
  `e meet f`, `e meet f^perp`, `e^perp meet f` nonzero;
- 28 have distinct overlapping nonnested propagation supports;
- exactly 24 pass all three tests;
- those 24 occupy 15 support types and two region-cardinality types;
- the four remaining nonnested-support candidates fail exactly at
  `e meet f^perp=0`.

**Evidence class: exhaustive finite evidence.** An independent direct-subset
verifier reproduces every count. **Evidence class: executable verified.**

These 24 non-atomic pairs are prerequisites only. They do not construct an
inflated event algebra or establish a nonrectangular state relation. The
atomic pair below is a separate structural control and does not instantiate
this proxy list.

## 4. Explicit independent selector pair

On the 16-point survivor choose

- `q=0x000f` with block support `{A00,A01,C01}`;
- `r=0x3300` with block support `{A01,A11}`.

They are disjoint lattice atoms, share exactly block `A01`, and occur
together in no repeated selector edge. For carriers `X_A,X_D`, replace the
points below `q` by `q times X_A` and those below `r` by
`r times X_D`, leaving the other points single; lift a skeleton event by
taking the full replacement fibre when it contains the corresponding atom.
Replacing the two intervals by Boolean sigma-algebras `A` and `D` gives
schematic form types:

- `E(a,S)` in `A00,C01`;
- `F(d,T)` in `A11`;
- `G(a,d,V)` in joint block `A01`;
- finite lifted forms in `A10`.

Both coefficient embeddings are injective for nondegenerate concrete
`A,D` by restriction to the disjoint replacement fibres. **Evidence class:
hand proved.** Exhaustiveness of the displayed form types under
arbitrary-base mixed closure is not established. **Evidence class: open.**

For fibre events `q times a` and `r times d`, the mixed join is
`G(a,d,empty)` in `A01`. Thus the obvious first mixed cut exists; the joint
block is the cut-saturation mechanism. **Evidence class: hand proved.**

## 5. Finite simultaneous substitutions

The literal finite substitutions independently verified are:

- `P(2) times P(2)`: 24 points, 116 events, exact block sizes
  32/64/32/16/32, trivial centre, complement/disjoint-union closure,
  latticehood, orthomodularity, and exactly the five named maximal blocks;
- `P(2) times P(3)`: 28 points, 196 events, complement/disjoint-union
  closure and latticehood;
- `P(3) times P(2)`: 28 points, 212 events, complement/disjoint-union
  closure and latticehood.

All three pass exact five-block classification and trivial centre. The
producer exhausts every event pair and enumerates maximal compatibility
cliques. **Evidence class: exhaustive finite evidence.** An independent
bit-mask implementation reconstructs the event systems, hashes, closure,
extrema, OML laws, centre, and maximality of each named block, but does not
independently enumerate every maximal clique. **Evidence class: executable
verified.**

The `P(2) times P(2)` certificate has 13,456 ordered pairs, 1,251 disjoint
pairs, and 6,544 compatible pairs; its hash is
`3bd494b6516ed7e42ebfc2a05994c9c121dbbde87488ca22285d82c97fde9e5b`.
The asymmetric hashes are
`718d472f87acd04b268747630ae70f952f0aec7e7b3d4cc23906de4698861123` and
`89da8988eeee0351c7e31830a473c7523eee67e103a3dfcd3aa54e03a4661958`.

These finite OMLs also pass concrete carrier, sigma-completeness by
finiteness, essential irreducibility via trivial centre, and global
sigma-state order separation via carrier point states. **Evidence class:
hand proved.** They are Phi-tame because finite and sigma additivity
coincide. **Evidence class: hand proved.** No forbidden finite pattern exists.

## 6. Campaign residue

Arbitrary-base complement and countable-disjoint-union closure have a
plausible two-coefficient normal form, but latticehood and exhaustive maximal
blocks require a global multi-coefficient truth-region audit. **Evidence
class: open.**

The next falsifiable step is a typed-form census over the 15 proxy support
types and the explicit `q,r` pair, followed by `P(2) times P(4)` and
`P(3) times P(3)`. Any surviving arbitrary-base candidate must expose its
uncountable-incidence hub: Theorem 1.1 rules out a locally countable
finite-arity N-G obstruction.
