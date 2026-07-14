# Arbitrary-base inflation at two orthogonal atoms

*Campaign 9, 2026-07-14. Exact construction and reductions; arbitrary-base
latticehood remains open.*

## 1. Exact event family

Let `L_*` be the certified 44-event five-block skeleton with named maximal
blocks `A00,A01,C01,A10,A11`. Let

\[
 q=0x000f,\qquad r=0x3300.
\]

These are disjoint lattice atoms. The blocks containing `q` are
`A00,A01,C01`; those containing `r` are `A01,A11`. Let
`A subset P(X)` and `D subset P(Y)` be nondegenerate concrete Boolean
sigma-algebras. Replace every old point below `q` by its product with `X`,
every old point below `r` by its product with `Y`, and leave the other eight
old points rigid. For each named skeleton block substitute `A` for its atom
`q` when present, substitute `D` for its atom `r` when present, and lift all
other block atoms rigidly. Denote the union of the five resulting Boolean
sigma-blocks by `L(A,D)`.

This defines a concrete family of subsets. The theorem below now proves that
it is a sigma-complete OML. **Evidence class: hand proved.**

Every complement is taken in the same substituted block as its event, so
`L(A,D)` is complement closed. **Evidence class: hand proved.**

## 2. Outsider extremality and arbitrary-base latticehood

Two input events mention at most two `A` coefficients and two `D`
coefficients. Their generated Boolean algebras have at most four nonempty
truth regions in each coordinate. Consequently any proposed Boolean-form
meet or join can be found and checked against bounds whose coefficients lie
in those input-generated subalgebras by a finite `P(k) x P(l)` control with
`k,l <= 4`. **Evidence class: hand proved.**

### Outsider-extremality lemma (OE)

For every two forms `u,v` in `L(A,D)`, the candidate lower and upper forms
obtained in their input-generated coefficient subalgebras remain respectively
greatest and least against every bound in `L(A,D)`, including forms with
coefficients outside those subalgebras.

*Proof.* Put `C=u intersect v`. For each named substituted block `B`, form
its block floor `F_B(C)`: include every rigid `B`-atom wholly contained in
`C`; on a flexible `q` slot use the intersection of all `q`-fibre sections
of `C`, and analogously on `r`. Those sections are Boolean expressions in
the coefficients of `u,v`, so the resulting coefficient remains in `A` or
`D`. This is the greatest `B`-event below `C`. Dually, the block ceiling over
`u union v` includes a rigid atom exactly when it meets the span and uses
the union of the flexible fibre sections.

Every outsider bound belongs to at least one of the five named blocks. A
lower bound in `B` is below `F_B(C)`, regardless of its own coefficient;
dually every upper bound is above its block ceiling. Thus a greatest one of
the five floors is the global lattice meet, and a least ceiling is the join.
No third-coefficient truth regions enter this domination argument.

Partition `X` and `Y` by membership in the at-most-two input coefficients.
There are `k,l<=4` nonempty truth regions, and all five floor/ceiling
comparisons transport exactly to `L(P(k),P(l))`. The finite kernel verifies
that a winning floor and ceiling exist in every case. Complement,
disjoint-union closure, and the orthomodular identity transport through the
same generated finite coefficient algebras. The winning floor need not be
the concrete set intersection. **Evidence class: hand proved**, with the
finite kernel **executable verified**.

The durable kernel checks all 16 models `L(P(k),P(l))`, `1<=k,l<=4`.
The binding `P(4)xP(4)` case has 40 points, 1220 events, 16,964 distinct
intersection cuts, and 744,810 unordered input pairs. Every pair has a
winning block floor and ceiling, and complement, binary disjoint-union
closure, unique extrema, and the OML law pass. **Evidence class: exhaustive
finite evidence.** A separate reconstruction verifies all 16 receipts.
**Evidence class: executable verified.**

### Arbitrary-base two-atom theorem

> For every nondegenerate pair of concrete Boolean sigma-algebras `A,D`,
> `L(A,D)` is a concrete orthomodular lattice closed under binary disjoint
> union.

**Evidence class: hand proved**, using the independently executable-verified
finite kernel.

## 3. Sigma closure

Discard zero events from a countable
pairwise-disjoint family. Only finitely many members can have nonempty
support on the fixed finite set of rigid points outside `q union r`. Set
those aside in the finite head. Inspection of the five exact block templates
shows that `A10` contributes only zero to the remaining tail, which consists
exactly of

\[
 q\mathbin{\times}a,\qquad r\mathbin{\times}d,\qquad
 (q\mathbin{\times}a)\cup(r\mathbin{\times}d),
\]

all of which lie in the joint sigma-block `A01`. The coefficient unions
exist in `A,D`, so the tail union lies in `A01`.
Binary closure combines it with the finite head. Therefore `L(A,D)` is
closed under countable disjoint unions. Standard successive disjointization
in an OML then gives every countable join, so it is sigma-complete.
**Evidence class: hand proved.**

## 4. Maximal-block residue

For an event `e`, define its named-block signature to be the subset of the
five substituted blocks containing it. If lattice compatibility is proved
equivalent to simultaneous membership in a named block, then any compatible
family not contained in one named block has a subfamily of size at most five:
choose one event excluding each block label. Hence exact maximal-block
classification reduces to feasibility of compatible substituted-form
families of size at most five with empty total signature intersection.

The signature characterization and its coefficient-feasibility census are
both open. Five coefficients may create 32 truth atoms, so the binary
controls do not settle this gate. **Evidence class: conditional.** These
gates are no longer needed for latticehood or sigma-completeness, but remain
needed for the stated maximal-block and conditional state theorem.

## 5. State classification conditional on the displayed block family

Assume the five substituted blocks are the displayed exhaustive block cover,
their shared `A` and `D` intervals agree literally on overlaps, and the
standard compatible-block-state gluing lemma applies. Restriction of a
global finitely additive two-valued state to lifted skeleton events gives a
global skeleton state `s`. Since `q` and `r` are orthogonal in `A01`, exactly
one of the following holds:

1. `s(q)=1,s(r)=0`: the state has one ultrafilter `U` on `A`, shared across
   `A00,A01,C01`, and kills every event below `r`;
2. `s(q)=0,s(r)=1`: symmetrically it has one ultrafilter `V` on `D`, shared
   across `A01,A11`, and kills every event below `q`;
3. `s(q)=s(r)=0`: both fibre intervals are killed and no coefficient datum
   remains.

Conversely, a global skeleton state together with the single ultrafilter
required by its charged branch defines compatible block ultrafilters. The
crossing finite block `A10` constrains only `s`; it does not introduce a new
coefficient. On a charged branch the state is sigma-additive exactly when
its sole charged-fibre ultrafilter is sigma-additive, because each substituted
block is a finite Boolean direct sum and the other pieces are finite. On the
third, uncharged branch it is automatically sigma-additive.

For a finite trace, orient its finitely many charged-fibre coefficients by
`U` or `V`. Their Boolean conjunction belongs to that ultrafilter and is a
nonempty concrete set. Point evaluation at a point of the conjunction is a
sigma-additive replacement preserving the trace; retain the same skeleton
state. Therefore `L(A,D)` satisfies `Phi` whenever the displayed
arbitrary-base block/form theorem holds.

**Evidence class: hand proved, conditional on the exhaustive block/form and
gluing hypotheses.** Orthogonality makes the coordinates alternatives, not
a product, so this construction cannot realize simultaneous distributed
boundary transport.

## 6. Enlarged finite controls

The producer exhaustively enumerates maximal compatibility cliques; an
independent bit-mask verifier reconstructs the event family, hashes,
closure, extrema, OML law, centre, and maximality of each named block but
does not independently enumerate every maximal clique.

| Fibre atoms | Points | Events | Block sizes | Hash prefix |
|---|---:|---:|---|---|
| `2 x 4` | 32 | 356 | `32/256/32/16/128` | `0069db62` |
| `3 x 3` | 32 | 356 | `64/256/64/16/64` | `c79cf02` |
| `4 x 2` | 32 | 404 | `128/256/128/16/32` | `83283a39` |

Together with `2 x 2`, `2 x 3`, and `3 x 2`, all six cases pass complement
and disjoint-union closure, latticehood, orthomodularity, exact five-block
classification, and trivial centre. **Evidence class: exhaustive finite
evidence.** The independent reconstruction passes all six certificates.
**Evidence class: executable verified.**

The observed event-count formula is

\[
 |L_{n,m}|=2^{n+m+2}+2^{m+2}+2^{n+3}+4.
\]

The normal forms give the same formula by inclusion-exclusion, but that
derivation is not used in the arbitrary-base lattice proof.

## 7. Verdict and next test

OE, arbitrary-base latticehood, and sigma-completeness are proved. Exact
maximal blocks, centre, state classification/order separation, and the
unconditional Phi consequence remain open. Conditional on those block/state
gates, the construction is Phi-tame because a state charges at most one
fibre. The next bounded action in this class is the at-most-five-form
signature census.
