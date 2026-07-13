# Boundary regularity of genuine concrete OML overlaps

*Opened 2026-07-12. Status: mixed hierarchy, with an explicit negative
example. All new results below are ⟦HAND⟧. The construction is elementary
and is given at set level so that latticehood, σ-completeness, maximal
blocks, the boundary, and the two relevant topologies can be checked
directly. It is a boundary-regularity counterexample, not a counterexample
to `Phi`.*

**Essential-irreducibility follow-up.**
[`oml_irreducible_boundary_test.md`](oml_irreducible_boundary_test.md)
proves the two-block centrality obstruction, audits distributed
centre-killing architectures, and completes the failed raw crossed paste to
a 56-event centre-free concrete σ-complete OML. All seven maximal-block
boundaries saturate their blocks. The later distributed one-interval note
constructs an infinite centre-free topological inflation and proves it tame.

**Seven-block inflation follow-up.**
[`oml_seven_block_inflation.md`](oml_seven_block_inflation.md) proves that
the direct common-base inflation preserves the seven-block incidence and
the face-exposed dense-nonopen locus, but necessarily has centre equal to
the common Boolean base. It isolates distributed-base OML admissibility as
the remaining gate. That gate is passed for one orbit-local interval in
[`oml_distributed_sigma_selection.md`](oml_distributed_sigma_selection.md):
the closure is centre-free and retains noncompact face topology, but admits
fibrewise compatible σ-selection for every finite face.

## 1. Exact question

For a maximal Boolean block `B` of a concrete σ-complete OML `L`, put

\[
 \partial B=\operatorname{BA}_B\!\left(\bigcup_{C\ne B}(B\cap C)\right).
\]

For a finite coherent face `C_p`, localization needs only

\[
 K_{B,p}\cap T_B^\sigma(E_B(p))\text{ open in }K_{B,p},\qquad
 K_{B,p}=\{\mu|_{\partial B}:\mu\in C_p\}. \tag{RO-face}
\]

The question is whether the origin of `partial B` from actual maximal-block
overlaps forces this condition. It does not, even when there are only two
maximal blocks, their intersection is a σ-field, and `B` is generated over
the boundary by one Boolean event.

## 2. What OML overlap geometry really forces

The certified result `IsMaxBlock.overlapMeasurableSpace` in
`ConcreteOMLBlocks.lean` gives the main unconditional restriction:
every pairwise intersection `B cap C` is a σ-field of subsets of the common
carrier. Maximality also makes it a Boolean subalgebra of each block. It need
not be central in either block or complete as a Boolean algebra, and the
family `{B cap C : C ne B}` need not be directed. Its Boolean algebraic union
need not be σ-closed: `partial B` uses only finite Boolean operations.

Concreteness says that point evaluations are dense in the Stone space of
every represented Boolean algebra. It does not say that every ultrafilter is
point-realized, that the point image is open or closed, or that restriction
is proper. Essential irreducibility only removes elements common to all
blocks (the center); it does not presently control the atoms or topology of
the union of pairwise overlaps. The counterexample below is deliberately
central/reducible, so the corresponding irreducible realization problem
remains open.

| Property of arbitrary Boolean interfaces | Forced for OML overlap boundaries? | Proof/counterexample |
|---|---|---|
| arbitrary Boolean subalgebra | **open in full generality; no as an unrestricted pairwise site** | every actual `B cap C` is a σ-field; realization of an arbitrary finite-operation algebra as the union-generated boundary remains open |
| σ-subalgebra | **conditional** | each pairwise site is a σ-field; a boundary generated from many sites need not be σ-closed |
| complete Boolean subalgebra | **no** | σ-closure is only countable and does not imply arbitrary-join completeness |
| point-image closed | **no** | §3 has dense proper point image |
| point-image relatively open | **no** | §3 has empty interior in its closure |
| evaluation map proper | **no** | in §3 the preimage of the compact whole Stone component is the noncompact carrier (it projects continuously onto an infinite discrete `2^J`) |
| finite fibres | **irrelevant alone** | the earlier `Q -> 2^N` example has singleton fibres; openness still fails |
| compact carrier image | **conditional yes** | a compact image in a Hausdorff Stone space is closed; this is an extra hypothesis, not forced |
| Stone dual retraction | **no known general retraction** | maximality supplies no Boolean retraction `B -> partial B`; eventwise σ-sections are sufficient (§5) |

Thus actual OML sites are more algebraically regular than arbitrary Boolean
interfaces, but not topologically regular enough for localization.

## 3. A genuine OML boundary with dense nonopen σ-liftable locus

### 3.1 The coarse σ-field

Let `I` be uncountable, `X=2^I`, and let `A` be the σ-field of all subsets
of `X` depending on only countably many coordinates:

\[
 A=\{\pi_J^{-1}(H):J\subseteq I\text{ countable},\ H\subseteq2^J\}.
\]

Countable unions of countable supports are countable, so `A` is a σ-field.
Let `Y=Ult(A)`, and let `e:X -> Y` be point evaluation.

The image `e(X)` is dense: every nonempty basic clopen `[D]`, `D in A`,
contains `e(x)` for `x in D`. More strongly, the non-σ-additive
ultrafilters are also dense. Given nonempty `D in A`, choose a countable
support `J` for `D`, distinct coordinates `i_0,i_1,...` outside `J`, and set

\[
 H_n=D\cap\{x:x(i_k)=0\ (k<n)\},\qquad
 H_\infty=D\cap\{x:x(i_k)=0\ \forall k\}.
\]

The family `{H_n:n in N} union {D setminus H_infty}` has the finite
intersection property: after finitely many zero requirements, put a `1` at
a later coordinate. Extend it to an ultrafilter `u`. Then `u(H_n)=1` for
all `n`, `u(H_infty)=0`, and the disjoint partition of
`D setminus H_infty` according to the first `1` has union valued `1` while
every cell is valued `0`. Hence `u` is not σ-additive. This construction
works inside every nonempty `[D]`.

Consequently the σ-additive-ultrafilter locus `S_sigma(A)` contains the
dense point image but has empty interior (its complement is dense). In
particular both `e(X)` and `S_sigma(A)` are dense and nonopen in `Y`.

### 3.2 Product with `MO2`

On `F={0,1,2,3}`, take the concrete six-element `MO2`

\[
 M=\{\varnothing,F,\{0,1\},\{2,3\},\{0,2\},\{1,3\}\}.
\]

Its two maximal blocks are
`C_0={empty,F,{0,1},{2,3}}` and
`C_1={empty,F,{0,2},{1,3}}`. Cross-block atoms have meet `0` and join `1`,
so `M` is a finite concrete OML.

On the disjoint union `Omega=X disjoint_union F`, represent

\[
 L=A\times M,\qquad (D,m)\longmapsto D\sqcup m.
\]

All order, complement, meet, and join operations are coordinatewise.
Therefore `L` is a concrete σ-complete OML. Compatibility is coordinatewise;
since `A` is Boolean and `M` has exactly the two blocks above, the maximal
blocks of `L` are exactly

\[
 B_0=A\times C_0,\qquad B_1=A\times C_1.
\]

Their intersection, and hence the overlap-generated boundary of either, is

\[
 \partial B_0=B_0\cap B_1=A\times\{0,1\}.
\]

This is an actual σ-field site. Moreover `B_0` is generated as a Boolean
algebra by `partial B_0` and the single event `(0,{0,1})`.

Take the central event `E=(1,0)`, represented by the whole `X` summand.
The Stone space of the boundary is the disjoint union `Y disjoint_union {*} `.
The carrier shadow of `E` is exactly `e(X)` in the `Y` component. Hence

\[
 \operatorname{Sh}_{B_0}(E)\text{ is dense and nonopen in }
 \overline{\operatorname{Sh}_{B_0}(E)}=Y.
\]

A local ultrafilter of `B_0` charging `E` is σ-additive exactly when its
`A`-component is σ-additive. Thus

\[
 T_{B_0}^\sigma(E)=S_\sigma(A),
\]

which is also dense and nonopen in `Y`. This is stronger than failure of
point-shadow openness: the actual coarse-block σ-liftable trace locus fails
openness.

Finally take the one-event face `p(E)=1`. Every ultrafilter of `A` extends
to a global finitely additive two-valued state of `A times M` supported on
the central `A` summand. Therefore `K_{B_0,p}=Y`, and (RO-face) fails on the
actual finite observational face. This also shows that finite Boolean
extension over the boundary does **not** imply global or face-relative
openness.

The center contains `A times {0,1}`, so this example is not essentially
irreducible. It proves that OML origin, latticehood, σ-completeness,
maximality, a σ-field site, two-block finiteness, and finite private Boolean
complexity do not suffice. The smallest remaining realization question is
whether the same topology can occur with trivial center.

## 4. Failed controlled constructions and the obstruction they expose

Finite central/star pastings with finite sites fall under finite-interface
quarantine. Replacing the site by a countable atomic power set does not
work: its principal ultrafilters form an open dense subset of `beta N`.
The countable-coordinate σ-field is needed because every basic clopen still
contains both a point state and a deliberately non-σ ultrafilter.

Pasting Boolean blocks freely along a prescribed infinite subalgebra is not
automatically an OML: the pasted orthoposet can lose meets. The direct product
with `MO2` avoids this by making lattice operations coordinatewise, at the
cost of a large center. Tree/relay variants have no checked mechanism that
both removes this center and preserves the site topology and all meets.

## 5. Positive tame classes (corrected)

The following statements are elementary and sufficient for (RO-face).

1. If the restricted carrier event, with its boundary initial topology, is
   compact, its image in the Hausdorff boundary Stone space is closed and
   equals its closure `T_B^fa(E)`. Hence it also equals `T_B^sigma(E)`, and
   its intersection with every relevant `K_{B,p} subset T_B^fa(E)` is all of
   `K_{B,p}`, therefore open. This uses the closure identity, not the false
   inference that an arbitrary closed subset is open.
2. If the relevant shadow is open in `T_B^fa(E)` (in particular clopen),
   then (RO-face) holds for every face.
3. If `E in partial B`, then `T_B^fa(E)` is a boundary clopen, but the point
   shadow or σ-liftable locus need not equal it. Section 3 uses precisely an
   `E in partial B`; boundary membership alone is therefore insufficient.
4. A finite union of boundary atoms works only when every ultrafilter on the
   corresponding clopens has the required point/σ realization. Finiteness of
   the displayed union without this saturation is insufficient.
5. An eventwise continuous section
   `s_E:T_B^fa(E) -> [E] subset Ult(B)` whose values are σ-additive local
   states makes `T_B^sigma(E)=T_B^fa(E)`, hence gives descent for that event.
   A section of the unrestricted restriction map which does not preserve
   `[E]` is not enough.
6. Finite boundary algebras remain the strongest unconditional local class:
   finite-interface quarantine eliminates the defect rather than merely
   making it closed.

The proposed finite-extension theorem is refuted by §3: one private Boolean
generator does not control σ-additivity on an infinite coarse boundary.
No finite-fibre rescue survives either; fibre size concerns the Stone
restriction map, while the defect is nonclosedness of the σ-additive locus.

The finite-atlas localization theorem in `relational_boundary_descent.md`
§9.1 remains valid and is the clean banked statement:

> A finite atlas satisfying (RO-face) for every participating block admits
> boundary-defect localization after a coherent finite refinement.

## 6. Face-relative regularity

For every finite pattern, `C_p` is a clopen compact subspace of the global
finitely additive state space, and `K_{B,p}` is its compact continuous
image. Thus `K_{B,p}` is always compact and closed in the boundary Stone
space. It need not be clopen or constructible from finitely many boundary
coordinates: restriction can project a finite-cylinder face to an arbitrary
compact Stone image.

Finite coherence does not restore openness. In §3 the one-coordinate face
has `K_{B_0,p}=Y`, and its intersection with the σ-liftable locus is the
dense nonopen set `S_sigma(A)`. Minimality of a failing face does not alter
this topology, and no finite cluster normal form yields finitely many trace
types on an infinite boundary.

This negative example is reducible/coarse. Face-relative openness may still
hold in an essentially irreducible fine atlas, but it is not a consequence
of the currently banked OML equations.

## 7. Direct simultaneous selection

Pairwise agreement through one underlying `mu` removes higher cocycle
conditions: all chosen local states agree with `mu` on every pairwise
overlap, so `BoundaryDescent.glueBlockStates` glues them. The remaining
problem is existence, not a triple-overlap cocycle.

There is one useful compactness theorem, strengthened by resolving overlap
agreement event by event.

**Compact local σ-selection theorem.** Fix a finitely coherent `p`. For every
maximal block `B`, let

\[
 X_B=\{v\in St_\sigma(B):v(E_B(p))=1\}.
\]

If every `X_B` is compact in the pointwise topology, then `p` has a global
σ-state extension. No finite-subatlas hypothesis is required.

*Proof.* Choose a global finitely additive `mu in C_p`. Each `X_B` is
nonempty: the finite conjunction of the requirements of `p` lying in `B` is
valued one by `mu`, hence is a nonempty concrete event, and any carrier point
in it gives an eligible local Dirac state. In the compact product
`product_B X_B`, impose one closed equation `v_B(A)=v_C(A)` for each shared
event `A in B intersect C`. A finite family of these equations mentions only
finitely many events in each block. For every block, the finite conjunction
which also requires agreement with `mu` on those events is valued one by
`mu`; choose a carrier point in it. These local Dirac states satisfy the
selected equations because both sides equal `mu(A)`. The closed equations
therefore have the finite-intersection property. Compactness supplies a
fully compatible family, and compatible block-state gluing finishes. ∎

In particular, compactness of `St_sigma(B)` for every maximal block implies
`Phi`. Conversely, every face witnessing failure of `Phi` has a block for
which its eligible local σ-state slice is noncompact.

The compactness hypothesis is binding. Sets of σ-additive two-valued states
need not be closed in the full ultrafilter space: principal states of
`P(N)` converge along a nonprincipal ultrafilter, and §3 makes both σ and
non-σ loci dense locally. Therefore the unrestricted implication
“every finite subatlas σ-lifts => the whole atlas σ-lifts” remains open and
cannot be obtained by a bare Tychonoff argument. The theorem applies when
each eligible σ-state space is closed (hence compact), in particular for
finite blocks and other explicitly compact σ-state classes.

## 8. Strategic decision and status

The evidence gives **Outcome 3: mixed hierarchy**. Actual OML overlaps are
σ-field sites pairwise, but unrestricted OML boundary topology is already
as bad as needed to defeat localization. General strategy should therefore
pivot to direct simultaneous selection. Localization remains viable only in
the finite-interface, saturated/clopen, eventwise-section, or explicitly
(RO-face) classes. Rooting is not the next general priority.

| Claim | Scope | Status | Consequence |
|---|---|---|---|
| OML boundaries are arbitrary Boolean interfaces | full/general class | **open as a realization classification; pairwise sites refuted as arbitrary** | sites are σ-fields, but this gives no openness |
| Dense nonopen shadow realizable in concrete OML | `A times MO2`, coarse reducible class | **constructed** | localization not general |
| Finite extension over boundary implies openness | arbitrary coarse blocks, even one generator | **refuted** | no new tame class without σ-saturation |
| Face-relative openness from finite coherence | one-event face in the example | **refuted** | finite observation does not localize |
| Boundary localization | finite atlas plus (R) | **proved conditionally** | rooting becomes relevant only in that slice |
| Compact eligible local slices imply global lift | arbitrary block atlas | **proved; no finite-subatlas hypothesis** | every bad face has a noncompact local slice |
| Direct GSD selection theorem | full class | **open** | primary general route |
| Rooting is next priority | only if localization obtained | **no in general** | retain only for regular slices |

## 9. Receipts and next handoff

Existing executable receipts rerun this session:

- `python3 notes/open_questions/verification/three_block_completion_audit.py`;
- `python3 notes/open_questions/verification/distributed_trap_audit.py`;
- `python3 notes/open_questions/verification/census_2026-07-12_s38/classify_near_misses.py`;
- `python3 notes/open_questions/verification/census_2026-07-12_s38/sasaki_root_audit.py`;
- `lake build` in `formalization/QuerySystem`.

No Lean file was changed: formalizing the uncountable countable-coordinate
σ-field and its Stone ultrafilters would require substantial topology and
choice infrastructure without strengthening the construction proof.

The single best next task is the **coarse inflation problem**:

> Inflate the centre-free 56-event seven-block skeleton to a concrete
> σ-complete OML with a coarse maximal block whose full or proper boundary
> has a dense nonopen σ-liftable locus exposed by a finite face; or prove
> that the observed boundary saturation forces σ-tameness.

A negative theorem here would identify essential irreducibility as the exact
missing regularity. A positive construction would make direct simultaneous
selection decisively primary for the full programme. Do not start another
large relay census unless it implements this exact coarse-inflation test.
