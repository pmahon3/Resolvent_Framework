# Inflation of the centre-free seven-block OML

*Opened 2026-07-12. Status: Outcome D. The finite skeleton now has a
substitution-ready certificate. The common-base inflation is completely
audited: it preserves the seven blocks and their saturated boundaries and
realizes the coarse topology, but necessarily restores a large centre. No
centre-free infinite inflation or failure of `Phi` is claimed.*

## 1. Statement of record

The conjecture remains unchanged:

> Every concrete σ-complete non-Boolean essentially irreducible OML
> satisfies the σ-lifting property `Phi`.

Full boundary saturation does not imply `Phi`. If `partial M=M`, boundary
σ-liftability is just σ-additivity of the whole block restriction, and a
coarse Boolean block can still have a dense nonopen σ-state locus. Any
positive theorem here must use the complete seven-block incidence.

## 2. Intrinsic form of the 56-event skeleton

Let `MO2` denote the six-element OML obtained from two four-element Boolean
blocks meeting in `{0,1}`. There are two sub-OMLs

\[
 L_a\cong MO_2\times MO_2,\qquad
 L_b\cong MO_2\times MO_2,
\]

with

\[
 L_a\cap L_b=B\cong 2^4,
 \qquad L^*=L_a\cup_B L_b.
\]

In `B`, label the atoms `q_0,q_1,q_2,q_3`. The first chart uses the
complementary interface

\[
 a=q_0\vee q_1,qquad a^\perp=q_2\vee q_3,
\]

and replaces the two decompositions under `a` and `a^perp` by two `MO2`
intervals. The second chart does the same for the crossed interface

\[
 b=q_0\vee q_2,qquad b^\perp=q_1\vee q_3.
\]

Thus the generator rule is

\[
 L_a=\langle B,C_a\rangle=MO_2[0,a]\times MO_2[0,a^\perp],
\]

\[
 L_b=\langle B,C_b\rangle=MO_2[0,b]\times MO_2[0,b^\perp],
\qquad L^*=L_a\cup L_b.
\]

This is intrinsic: the 16-point representation certifies concreteness but is
not needed to define the two interval-product charts or their amalgam.
The twelve displayed atoms of `B,C_a,C_b` generate the entire completion.

Each `MO2` factor has two maximal Boolean blocks. Hence each product chart
has four maximal 16-element Boolean blocks. The charts share exactly `B`,
so their maximal-block sets have sizes `4+4-1=7`. This explains the four
additional blocks forced by lattice completion: they are the three other
choices of one Boolean decomposition in each of the two `MO2` factors of
each chart, with `B` counted in both charts. They are not optional pasted
blocks.

The complete weighted incidence is not a tree. Pairwise intersection sizes,
in the stable certificate's block order, are:

| left | right | size | left | right | size |
|---|---:|---:|---|---:|---:|
| `B` | `D0` | 8 | `B` | `D1` | 8 |
| `B` | `D2` | 8 | `B` | `Ca` | 4 |
| `B` | `D3` | 8 | `B` | `Cb` | 4 |
| `D0` | `D1` | 4 | `D0` | `D2` | 4 |
| `D0` | `Ca` | 8 | `D0` | `D3` | 4 |
| `D0` | `Cb` | 2 | `D1` | `D2` | 4 |
| `D1` | `Ca` | 2 | `D1` | `D3` | 4 |
| `D1` | `Cb` | 8 | `D2` | `Ca` | 8 |
| `D2` | `D3` | 4 | `D2` | `Cb` | 2 |
| `Ca` | `D3` | 2 | `Ca` | `Cb` | 2 |
| `D3` | `Cb` | 8 |  |  |  |

The original crossed overlaps are therefore still
`|B intersect Ca|=4`, `|B intersect Cb|=4`, and
`|Ca intersect Cb|=2`, but the completion adds many 8-event overlaps.
Exhaustive search through all labelled trees on the seven block vertices
finds no running-intersection join tree. Consequently standard acyclic
database/junction-tree gluing does not apply to this atlas.

For every block `M`, the union of its six pairwise overlaps contains enough
two-atom partitions to generate its four atoms. Therefore

\[
 \partial M=\operatorname{BA}_M\!\left(\bigcup_{N\ne M}M\cap N\right)=M.
\]

Nevertheless no nontrivial event belongs to all seven maximal blocks:

\[
 Z(L^*)=\bigcap_M M=\{0,1\}.
\]

There is no conflict. Boundary generation uses different overlap events for
different neighbours; centrality requires literal membership in every block.

### Machine-readable certificate

`../verification/seven_block_skeleton_data.py` emits schema
`seven-block-skeleton-v1`. Its checked-in receipt
`../verification/seven_block_skeleton.json` contains:

- stable event IDs and 16-bit set masks;
- the `La` and `Lb` charts and their intersection;
- atom generators;
- all seven maximal blocks and their atoms;
- all pairwise intersections and generated boundaries;
- complement and complete `56 x 56` meet/join tables;
- the centre and orthomodularity checks.

This is the substitution-ready description; the set masks are a concrete
certificate rather than the definition.

## 3. General inflation datum

An inflation datum for this skeleton consists of:

1. seven Boolean σ-algebras `M_i` with finite quotient maps
   `pi_i:M_i -> 2^4`;
2. for every pair, a σ-subalgebra `A_ij subset M_i` and an isomorphism
   `theta_ij:A_ij -> A_ji` lifting the certified finite intersection;
3. cocycle agreement on triple intersections;
4. faithful representations of all `M_i` as σ-fields on one carrier, in
   which every `theta_ij` is literal equality of subsets;
5. a family `L` containing their union and closed under complement,
   countable disjoint union, and the binary extrema forced by cross-block
   pairs.

The following are obligations, not consequences of the datum:

- **complements:** every represented block complement must be the same
  ambient set complement;
- **σ-completeness:** every countable disjoint family from different blocks
  must have its union in `L`;
- **latticehood:** all cross-block lower and upper sets must have unique
  extrema;
- **orthomodularity:** `x<=y` must imply `x join (y meet x^perp)=y`;
- **maximality:** the maximal compatibility cliques must be exactly the
  intended blocks, or all additional blocks must be classified;
- **centre:** only the intersection of the exhaustive maximal-block family
  computes `Z(L)`;
- **saturation:** the actual, possibly enlarged maximal-block family must be
  used to recompute every boundary.

Finite quotients prove none of the first three infinite obligations.

## 4. Common coarse-base inflation: exact audit

Let `A` be any nontrivial concrete Boolean σ-algebra and take the direct
product

\[
 L_A=A\times L^*.
\]

Represent it on a disjoint union of carriers, so `(D,x)` is the disjoint
union of the set representing `D` and the set representing `x`. Operations
are coordinatewise.

### Algebraic audit

- `L_A` is concrete, a lattice, orthomodular, and σ-complete.
- Compatibility is coordinatewise. Since `A` is Boolean, the maximal
  blocks are exactly `A times M` for the seven maximal blocks `M` of `L*`.
  Thus no new maximal blocks appear and the incidence quotient is preserved.
- Intersections are
  `(A times M) intersect (A times N)=A times (M intersect N)`.
- Since the finite overlaps generate `M`, the inflated overlaps generate
  `A times M`; hence every boundary again saturates:

\[
 \partial(A\times M)=A\times M.
\]

- The centre of a product is the product of centres:

\[
 Z(L_A)=Z(A)\times Z(L^*)=A\times\{0,1\}.
\]

Therefore every nontrivial common-base product is reducible. More generally,
any inflation that embeds the same nontrivial Boolean algebra into every
maximal block with the same represented events is reducible, independently
of whether the embeddings are renamed before gluing. In a concrete OML,
glued events are literal subsets; an abstract automorphism does not stop
their common image from lying in every block.

This rules out the uniform common-base, direct-integral-with-constant-base,
and untwisted Boolean-valued blow-up routes as centre-killing constructions.
It does not rule out genuinely distributed bases that occur in only some
blocks.

### Local state topology and face exposure

Take `A` to be the countable-coordinate σ-field on `2^I`, for uncountable
`I`. The σ-ultrafilter locus of `A` is dense and nonopen in `Ult(A)`; both
σ and non-σ ultrafilters occur in every nonempty basic clopen.

A two-valued state on the Boolean product block `A times M` chooses one of
the two central summands. On the `A` summand, σ-additivity is precisely
σ-additivity of the chosen ultrafilter of `A`. Hence every inflated block
contains a clopen Stone component whose σ-state locus is dense and nonopen.
Because its boundary is the whole block, this is also its boundary
σ-liftable locus.

The one-event face charging the central selector `(1,0)` has restriction
image the whole `Ult(A)` component, so it exposes the dense-nonopen locus.
Thus the common-base model passes the topology and finite-face gates exactly
where it fails essential irreducibility.

It does not threaten GSD. Every nonempty finite face in a concrete Boolean
σ-field contains a carrier point realizing its finite trace; pairing this
with a σ-state of the finite factor supplies a global σ-state in the face.
Equivalently, alternative σ-states repair the displayed non-σ states.

## 5. Other controlled candidates

### Uniform point-fibre blow-up

Replacing each of the 16 carrier points by a fibre and replacing only a
finite event `E` by the union of its whole fibres changes neither the
abstract 56-event OML nor its finite state topology. Adding the same internal
σ-algebra in every block is the common-base product above and is central.
Adding internal events at only selected sites is not closed under the
cross-block meets and joins unless further events are added; no infinite
closure theorem identifies the resulting maximal blocks.

### Blockwise quotient blow-up

Seven coarse blocks with the right finite quotients do not define an OML.
The raw finite three-block paste already demonstrates the missing step: all
individual blocks and quotient identifications exist, yet a disjoint
cross-block union is absent and another pair has two maximal lower bounds.
Infinite blockwise substitution inherits this obligation rather than solving
it.

### Intervalwise `A times MO2`

Replacing all four `MO2` interval factors by products with one common `A`
again leaves `A` in every one of the seven product blocks, hence central.
Using distinct bases on the two charts avoids a displayed common factor but
does not yet specify the cross-chart extrema or countable mixed unions.

### Twisted bases

Conjugating a common embedding by automorphisms changes its coordinates but
not the fact that its identified image is contained in every block. A useful
twist must instead distribute different proper σ-subalgebras among different
overlaps. Such a diagram may kill the common intersection, but it is not yet
a concrete σ-complete lattice construction. The finite completion warns that
closing it can force additional maximal blocks.

## 6. Seven-block selection geometry

For a finite pattern `p`, simultaneous σ-selection is the constraint set

\[
 \{(v_M)_M:v_M\in S_M(p),\quad
 v_M|_{M\cap N}=v_N|_{M\cap N}\}.
\]

Every eventwise equality constraint is closed in the pointwise topology.
Decomposing overlap agreement into these individual constraints removes the
earlier finite-subatlas hypothesis entirely.

**Compact local σ-selection theorem.** Let `p` be finitely coherent and put

\[
 X_M(p)=\{v\in\operatorname{St}_\sigma(M):v
 \text{ satisfies every requirement of }p\text{ lying in }M\}.
\]

If every `X_M(p)` is compact in the pointwise topology, then `p` has a
global σ-additive extension. This holds for an arbitrary maximal-block atlas,
not only the seven-block atlas.

To prove it, choose a global finitely additive extension `mu in C_p`.
Every `X_M(p)` is nonempty: the finitely many oriented pattern events in
`M` have a conjunction valued one by `mu`; concreteness supplies a carrier
point in that conjunction, whose Dirac state lies in `X_M(p)`.

The product `X=product_M X_M(p)` is compact. For every `M,N` and every
`A in M intersect N`, let

\[
 F_{M,N,A}=\{(v_Q)_Q:v_M(A)=v_N(A)\}.
\]

These sets are closed and have the finite-intersection property. Indeed, a
finite collection mentions only finitely many overlap events in each block.
For each block choose a carrier point whose local Dirac state matches `mu`
on those events and on the local requirements of `p`; the same finite
conjunction argument supplies it. Both endpoints of every selected equation
then equal `mu(A)`. Compactness gives a family satisfying every eventwise
equation, and compatible block-state gluing gives the global σ-state.

Consequently,

\[
 \bigl(\forall M,\ \operatorname{St}_\sigma(M)\text{ compact}\bigr)
 \quad\Longrightarrow\quad \Phi(L).
\]

Thus any face witnessing failure of `Phi` must have at least one block with
a **noncompact eligible local σ-state slice** `X_M(p)`. Dense nonopenness of
an ambient σ-state locus is relevant only insofar as such noncompactness
survives the chosen finite face.

The certified incidence has no join tree, so pairwise consistency is not a
complete local-consistency algorithm. No Helly number below seven has been
proved. Full-boundary saturation makes local surgery more rigid: agreement
with one underlying finitely additive state fixes the entire block state.
It does not propagate σ-additivity by itself.

For the common-base product, selection separates into the `A` coordinate and
the finite `L*` coordinate, and carrier-point states solve every coherent
finite face. For a distributed-base inflation, separability is precisely the
open issue.

## 7. GSD and `Phi`

No candidate here fails GSD. The dense-nonopen locus says only that some
global finitely additive states are non-σ on an inflated block. It does not
say that a finite face contains no compatible global σ-state. In the only
fully valid infinite candidate, every coherent finite face has a σ-additive
repair.

The strongest positive result obtained is therefore conditional and exact:

> **Common-base dichotomy.** The direct common-base inflation preserves
> concreteness, σ-completeness, orthomodularity, the seven maximal blocks,
> boundary saturation, and face-exposed dense-nonopen local σ-topology; but
> every nontrivial common base lies in the centre. Hence this entire natural
> class cannot be an essentially irreducible counterexample to `Phi`.

This uses the whole maximal-block calculation. It is not a claim that
boundary saturation forces tameness.

## 8. Smallest incidence-preserving inflation datum

The smallest incidence-preserving problem is one explicit
diagram-realization gate. Choose seven Boolean σ-algebras `M_i` with
four-atom finite quotients and lift the 21 certified pairwise intersection
algebras so that:

1. their common literal intersection is `{0,1}`;
2. at least one `M_i` contains a countable-coordinate σ-field component
   whose σ-ultrafilters are dense nonopen;
3. the lifted overlaps generate every `M_i` (inflated saturation);
4. the seven represented blocks, after closure under mixed countable
   disjoint unions and binary extrema, form a concrete OML with no new
   maximal blocks.

Conditions 1--3 are Boolean-diagram conditions. Condition 4 is the unresolved
**incidence-preserving** OML admissibility gate. It is not an exhaustive
normal form: mixed closure may necessarily create additional maximal blocks,
just as completion of the original raw three-block family created four new
ones. Such a candidate remains valid if all resulting maximal blocks are
classified, its centre is trivial, and a finite face exposes the coarse
topology.

The broader inflation gate is therefore:

> Mixed closure is a concrete σ-complete OML; every resulting maximal block
> is classified; the centre is trivial; and some finite face exposes a
> noncompact eligible local σ-state slice.

Even these conditions do not obstruct `Phi`. A counterexample must further
make the complete family of eventwise compatibility constraints have no
global σ-selection.

The smallest promising specialization assigns coarse structure to one
`MO2` interval in `La` and transports only the overlap-required proper
subalgebras into the three neighbouring product blocks, while `Lb` crosses
the corresponding finite quotient selector. Unlike a common-base product,
no coarse algebra is stipulated to occur in all seven blocks. Its mixed
meet/join and σ-union closure is open.

## 9. Status table

| Claim | Scope | Status | Consequence |
|---|---|---|---|
| Intrinsic substitution description of `L*` | finite skeleton | **proved; executable** | inflation framework |
| Infinite centre-free inflation exists | distributed-base class | **open** | irreducible topology |
| Maximal-block incidence preserved | common-base product | **proved** | valid but reducible |
| `partial B=B` after inflation | common-base product blocks | **proved** | local defect is full-block σ-defect |
| Dense-nonopen σ-state locus exists | common-base coarse block | **proved** | topology survives |
| Finite face exposes locus | central one-event face | **proved** | topology is globally visible |
| GSD fails | common-base product | **refuted** | no threat to `Phi` |
| Compact eligible local slices imply σ-selection | arbitrary block atlas | **proved** | any bad face has a noncompact local slice |
| Finite-subatlas compatibility needed | compact eligible local slices | **refuted as unnecessary** | eventwise FIP is automatic from a global `mu` |
| Inflation or saturation theorem is next | strategic decision | **yes: distributed inflation gate** | next session |

## 10. Receipts and outcome

Run:

```sh
python3 notes/open_questions/verification/seven_block_skeleton_data.py \
  --output notes/open_questions/verification/seven_block_skeleton.json
python3 notes/open_questions/verification/three_block_interface_audit.py
python3 notes/open_questions/verification/three_block_completion_audit.py
python3 notes/open_questions/verification/distributed_trap_audit.py
python3 notes/open_questions/verification/census_2026-07-12_s38/classify_near_misses.py
python3 notes/open_questions/verification/census_2026-07-12_s38/sasaki_root_audit.py
cd formalization/QuerySystem && lake build
```

No Lean file was changed. The new result uses elementary product-OML and
centre calculations; formalizing it before a distributed inflation exists
would not advance the admissibility gate.

The strategic classification is **Outcome D**, with a substantial ruled-out
subclass: common-base inflation realizes every requested feature except
essential irreducibility, and fails it necessarily.

The single best next task is to bank the eventwise compact-selection theorem
and then implement the one-interval distributed-base specialization on
finite/countable approximants. Extra maximal blocks are permitted, but must
be exhaustively classified. The target is a trivial-centre mixed closure with
a finite face retaining a noncompact eligible slice; only then test whether
the full eventwise compatibility system nevertheless has no σ-selection.
