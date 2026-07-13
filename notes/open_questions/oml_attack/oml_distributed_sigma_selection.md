# Distributed one-interval inflation and simultaneous σ-selection

*Opened 2026-07-12. Baseline commit: `8f627f5` (`Strengthen compact OML
state selection`). Status: Outcome B at hand-proof level, with exhaustive
finite approximants. No counterexample to `Phi` is claimed.*

## 1. Statement of record

The conjecture is unchanged:

> Every concrete σ-complete non-Boolean essentially irreducible OML satisfies
> the finite-trace σ-lifting property `Phi`.

Noncompactness below is necessary for a bad face, not sufficient. It is kept
separate from dense nonopenness, finite-face exposure, failure of compatible
selection, and failure of `Phi`.

## 2. Compact local σ-selection, exact scope

All states in this note are **two-valued**. Let `p` be a finite
complement-closed pattern with a global finitely additive extension
`mu in C_p`. For every maximal Boolean block `B`, put

\[
 X_B(p)=\{v\in\operatorname{St}_\sigma(B):v\text{ satisfies the
 local requirements of }p\}.
\]

Give it the subspace topology from the Stone cube `{0,1}^B`. For every
`A in B cap C`, put

\[
 F_{B,C,A}=\{(v_M)_M:v_B(A)=v_C(A)\}.
\]

**Theorem (compact local σ-selection).** For an arbitrary maximal-block
atlas, if every `X_B(p)` is compact, then `p` has a global σ-additive
two-valued extension.

*Proof.* First, each `X_B(p)` is nonempty. Orient the finitely many local
pattern events according to `mu`. Since `mu` is two-valued, their Boolean
conjunction has value one and is therefore a nonempty concrete event. A
carrier point in it gives a local Dirac σ-state.

The product `X(p)=product_B X_B(p)` is compact by Tychonoff. Each
`F_{B,C,A}` is clopen: the two evaluation maps are continuous into the
discrete two-point space and equality is clopen there. For a finite family
of these equations, only finitely many events occur in each block. Orient
those events according to the same `mu` and conjoin them with the local
requirements of `p`. The conjunction again has `mu`-value one. A carrier
point in it supplies a local Dirac state which agrees with `mu` on every
mentioned event. Thus both endpoints of each selected equation have the
same value `mu(A)`, proving the finite-intersection property. Compactness
gives a point in the intersection of all eventwise equations.

The resulting block states agree on every overlap. The Lean-certified
`BoundaryDescent.glueBlockStates` glues them. Its proof puts every countable
disjoint family in one maximal block, so blockwise σ-additivity gives global
σ-additivity. The glued state satisfies `p` by construction. ∎

The use of a **two-valued** `mu` is load-bearing: a single Dirac state need
not match a general real-valued finitely additive probability on finitely
many events. The theorem uses full Choice twice in an arbitrary atlas:
Tychonoff for an arbitrary product and carrier choices for the finite
conjunctions. No finite-atlas or fine-block hypothesis is used.

### Formalization receipt

`BoundaryDescent.lean` already proves finite-trace Dirac realization,
overlap-compatible gluing, and the blockwise-to-global σ step. The remaining
Lean abstractions are:

1. the indexed type of eligible block states with its pointwise topology;
2. compactness of the arbitrary dependent product;
3. the clopen eventwise equality predicates;
4. the closed-set finite-intersection compactness theorem in that dependent
   product.

The current infrastructure has no such topology on `BlockState`. Building it
would be a topology-library detour, so the compact theorem remains an exact
hand proof. No Lean file is changed for it.

## 3. Necessary topology of an offending face

The contrapositive is immediate and precise:

> If `p` is finitely coherent but has no global σ-additive extension, then
> `X_B(p)` is noncompact for at least one maximal block `B`.

Let `St_fa(B)` be the full Stone space of finitely additive two-valued block
states. It is compact Hausdorff. The finite pattern cylinder is clopen.
Hence a noncompact `X_B(p)` cannot be closed in `St_fa(B)`. There is a net
in `X_B(p)` converging to a point of its closure outside `X_B(p)`. Because
the pattern cylinder is closed, the limit satisfies the same finite local
requirements; because it lies outside `X_B(p)`, it is non-σ. If the relevant
ambient state space is metrizable, the net may be replaced by a sequence.
No sequential claim is valid without such a countability/metrizability
hypothesis.

The bad block need not contain a nontrivial event named by `p`: the theorem
only detects a noncompact eligible slice somewhere in the atlas, and on a
remote block that slice may be the full local σ-state space.

| Condition | Necessary for `not Phi`? | Scope | Proof |
|---|---:|---|---|
| noncompact eligible local σ-slice | yes | arbitrary atlas | contrapositive of compact selection |
| nonclosed eligible σ-slice | yes | compact ambient Stone space | closed subsets are compact |
| net converging to a non-σ state with the same finite pattern | yes | compact ambient Stone space | closure/net characterization; pattern cylinder closed |
| sequential nonclosure | yes only in metrizable/first-countable slices | metrizable case | sequences characterize closure |
| dense-nonopen locus | no | special coarse architectures | noncompactness does not imply density |
| noncompactness on a pattern-named block | no known implication | arbitrary atlas | the detected block may be remote |

## 4. Smallest distributed one-interval datum

Use the substitution-ready skeleton notation from
`oml_seven_block_inflation.md`. In the distinguished block `B`, choose the
atom `q_0`. Exactly three certified maximal blocks contain `q_0` as an atom:

\[
 B,\quad D0,\quad D1.
\]

The other four (`D2,Ca,D3,Cb`) cross the selector and do not contain it.
Let `A` be a concrete Boolean σ-algebra on `X`. Replace the interval
`[0,q_0]` by `A` in `B`; mixed closure propagates precisely the same interval
into `D0` and `D1`, and nowhere else. Thus the completed seven blocks are

\[
 A\oplus 2^3\quad\text{at }B,D0,D1,
 \qquad 2^4\quad\text{at }D2,Ca,D3,Cb.
\]

This is distributed, not a common direct factor: no nontrivial event of `A`
lies in the four crossed blocks.

### Concrete representation

In the 16-point carrier `(q,r,s)`, replace the four points below `q_0` by
`X times {0,1} times {0,1}`. Lift every skeleton event by inverse image.
For `D in A`, the new interval event is

\[
 \widehat D=D\times\{0,1\}\times\{0,1\}\subseteq q_0.
\]

Take the union of the three inflated and four lifted finite blocks above.
The raw family obtained by inflating only `B` is not closed under mixed
disjoint unions. Its Dynkin closure is exactly this seven-block family.

## 5. Mixed closure and OML structure

The following is presently a hand theorem backed by the parametric block
description and exhaustive finite schemas.

**Distributed interval-inflation theorem.** For every concrete Boolean
σ-algebra `A`, the displayed family `L_A(q_0)` is a concrete σ-complete OML.
Its maximal blocks are exactly the seven displayed blocks. Its centre is
trivial and every overlap-generated boundary is the whole corresponding
block.

Proof structure:

1. In each of `B,D0,D1`, `q_0` is an atom. Replacing that atom by `A`
   gives the Boolean σ-field `A oplus 2^3`.
2. Complement is blockwise. For a mixed countable disjoint family, the
   portions below `q_0` form a disjoint family in `A`; outside `q_0` only
   the finite skeleton shapes remain. The certified skeleton disjoint-union
   table places their union in one of the same seven shapes. This is exactly
   why closure propagates to all three `q_0`-blocks.
3. Binary extrema have the certified skeleton extrema outside `q_0`. Below
   `q_0`, pairs in a common inflated block use the Boolean extrema of `A`;
   a proper fibre event and a crossed-block event have the same zero/top
   extremal behaviour as `q_0` against that crossed skeleton event. The
   finite shape table therefore supplies unique extrema and the
   orthomodular law.
4. Compatibility gives exactly the three inflated Boolean blocks and four
   finite blocks. Thus there are no additional maximal blocks.
5. The four crossed finite blocks have common intersection `{0,1}`.
   Therefore the intersection of all seven exhaustive maximal blocks, hence
   the centre, is `{0,1}`.
6. The old overlap generators still generate every finite part. In each
   inflated block, its two inflated neighbours share the whole `A` interval,
   so the overlaps also generate the new part. Hence every boundary
   saturates.

The finite shape argument in steps 2--4 should eventually be promoted to a
small symbolic theorem or Lean lemma; finite approximants alone do not prove
the arbitrary-`A` statement.

## 6. Finite approximants

`../verification/seven_block_interval_inflation_audit.py` substitutes
`A_n=P(n atoms)`, computes the canonical complement/disjoint-union closure,
then exhaustively checks all binary extrema, orthomodularity, compatibility
cliques, the centre, and generated boundaries. Its stable receipt is
`../verification/seven_block_interval_inflation_schema.json`.

| `A_n` | raw events | after mixed closure | maximal block sizes | centre | boundaries |
|---:|---:|---:|---|---:|---|
| `P(2)` | 72 | 88 | `16^4,32^3` | 2 | all saturated |
| `P(3)` | 104 | 152 | `16^4,64^3` | 2 | all saturated |
| `P(4)` | 168 | 280 | `16^4,128^3` | 2 | all saturated |

For all three approximants there are exactly seven maximal blocks with names
`B,D0,D1,D2,Ca,D3,Cb`; precisely `B,D0,D1` inflate. The raw family is
complement-closed but fails mixed disjoint-union closure. One closure round
stabilizes. These counts are evidence for the finite shape theorem only;
they do not establish infinite σ-completeness or noncompactness.

## 7. Local state topology and face exposure

Take `A` to be the countable-coordinate σ-field on `2^I` for uncountable
`I`. In each inflated block, the local states charging `q_0` are exactly the
ultrafilters of `A`, and the eligible σ-states are exactly
`St_sigma(A)`. The latter is dense and nonopen in `Ult(A)`, hence nonclosed
and noncompact. The one-event face

\[
 p(q_0)=1
\]

projects onto the full `A` component, so it exposes this noncompact eligible
slice while the global centre remains trivial.

This establishes the topology and face gates. It does not establish a
selection obstruction.

## 8. Complete compatibility system and tameness

For a finite pattern `p`, the system is

\[
 v_M(E)=v_N(E)\qquad(E\in M\cap N)
\]

over the seven local eligible σ-state spaces. In the present construction
the only infinite equations are agreement on the common `A` interval among
`B,D0,D1`; every equation involving a crossed block is one of the finite
skeleton equations. Thus the inverse-limit problem separates into one
`A`-ultrafilter coordinate and a finite skeleton state.

**Tameness theorem.** `L_A(q_0)` satisfies `Phi` for every concrete Boolean
σ-algebra `A`.

Let `mu` be a global finitely additive two-valued state realizing a finite
pattern.

- If `mu(q_0)=0`, every event below `q_0` has value zero. The only possible
  countable additivity defect lies in the `A` interval, so `mu` is already
  blockwise and hence globally σ-additive.
- If `mu(q_0)=1`, its restrictions to `B,D0,D1` select one common
  ultrafilter `u` of `A`; compatibility on the finite overlaps selects a
  finite skeleton state charging `q_0`. Only finitely many events of `A`
  occur in the pattern. Their `u`-oriented conjunction is a nonempty
  concrete `A`-event. Choose `x` in it. Replacing `u` by the point state at
  `x`, while retaining the finite σ-additive skeleton choice, gives a
  compatible global σ-state with the same finite trace. It need not be a
  carrier Dirac state for the whole OML.

Hence every finite eventwise fragment is satisfiable, but so is the full
system. There is no escaping net with empty inverse limit and no threat to
`Phi`.

## 9. Outcome and status

This is **Outcome B — centre-free inflation, but σ-tame**. It refutes the
suggested one-interval no-go statement if that class permits propagation to
the two other blocks containing the selected atom. What remains open is a
more distributed substitution in which at least two inequivalent coarse
coordinates are demanded around a compatibility cycle, so the local inverse
system does not separate into one Boolean fibre and a finite skeleton state.

| Claim | Scope | Status | Consequence |
|---|---|---|---|
| Compact local σ-selection | arbitrary atlas, finite pattern | proved at hand level; Lean gluing certified | compact slices imply `Phi` |
| Offending face requires noncompact local slice | full stated scope | proved | necessary condition |
| One-interval coarse substitution is admissible | `q_0` datum above | constructed at hand level; finite exhaustive receipts | inflation gate passed |
| Mixed σ-complete closure exists | arbitrary Boolean σ-algebra `A` | hand proof; symbolic formalization pending | valid OML candidate |
| Centre remains trivial | completed candidate | proved from exhaustive block family | essentially irreducible |
| New maximal blocks classified | completed candidate | complete: exactly seven | centre/boundary valid |
| Finite face exposes noncompact slice | countable-coordinate `A`, `p(q_0)=1` | proved | topology survives centre removal |
| All finite eventwise fragments satisfiable | every coherent finite face | proved | FIP holds |
| No global σ-selection exists | candidate | refuted | no GSD obstruction |
| One-interval substitutions are always tame | this explicit orbit-local class | proved; broader class open | reusable tame mechanism |
| Broader distributed substitution remains | multiple inequivalent fibres/cycle twists | open | next frontier |

## 10. Acceptance audit and handoff

1. The compact theorem is correct for two-valued states, arbitrary atlases,
   and finite patterns; Choice/Tychonoff and the pointwise topology are
   explicit.
2. Every offending face has a noncompact, hence nonclosed, eligible slice
   with a same-pattern net converging to a non-σ state.
3. The smallest datum is the `q_0` interval substitution propagated through
   `B,D0,D1`.
4. Its mixed closure is a concrete σ-complete OML at hand-proof level.
5. Exactly seven maximal blocks arise: three inflated and four finite.
6. The centre is trivial.
7. The face `q_0=1` exposes the noncompact slice for countable-coordinate
   `A`.
8. Every finite compatibility fragment is satisfiable.
9. Complete compatible selection is not impossible; it always exists.
10. The candidate does not threaten `Phi`.
11. The reusable result is tameness of this orbit-local one-fibre class,
    not a no-go theorem for every conceivable interval embedding.
12. The residual class must use at least two inequivalent coarse fibres or a
    genuine cycle twist after full mixed closure.
13. **Single best next task:** inflate two crossed skeleton atom orbits by
    distinct coarse algebras and compute whether mixed closure identifies
    them into a common factor or leaves a nonseparable inverse system.

## 11. Validation receipt

Passed on 2026-07-12:

```sh
python3 notes/open_questions/verification/seven_block_skeleton_data.py \
  --output notes/open_questions/verification/seven_block_skeleton.json
python3 notes/open_questions/verification/three_block_interface_audit.py
python3 notes/open_questions/verification/three_block_completion_audit.py
python3 notes/open_questions/verification/distributed_trap_audit.py
python3 notes/open_questions/verification/census_2026-07-12_s38/classify_near_misses.py
python3 notes/open_questions/verification/census_2026-07-12_s38/sasaki_root_audit.py
python3 notes/open_questions/verification/seven_block_interval_inflation_audit.py \
  --max-fibre-atoms 4 \
  --output notes/open_questions/verification/seven_block_interval_inflation_schema.json
cd formalization/QuerySystem && lake build
```

Both updated registries and the new schema pass `python3 -m json.tool`;
`git diff --check` passes. No Lean theorem was added, so no new `sorry`,
`sorryAx`, axiom, or `#print axioms` obligation arises. The build succeeds
with the repository's pre-existing dependency and linter warnings.
