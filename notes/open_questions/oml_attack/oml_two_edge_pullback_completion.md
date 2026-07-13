# Two-common-block pullback audit: O2 and O3

*Completed 2026-07-12. Outcome C at the intrinsic skeleton gate: both
two-common-block orbits repeat one quotient datum. No new mixed completion or
infinite sigma-complete model is asserted.*

## Result and scope

The proposed two-edge mechanism does not occur for either representative.
For a fixed pair `e,f` in an OML, the four regions

\[
 e\wedge f,\quad e\wedge f^\perp,\quad e^\perp\wedge f,
 \quad e^\perp\wedge f^\perp
\]

are lattice elements, independent of which Boolean block containing `e,f`
is used to compute them. Consequently a second common block repeats the same
embedded finite Boolean datum. It cannot create a second quotient edge merely
by being a second block. This kills the stated O2/O3 route before a coarse
substitution is chosen; it does not classify substitutions using additional
events or distinct embedded subalgebras.

The executable certificate is
[`../verification/seven_block_two_edge_pair_schema.json`](../verification/seven_block_two_edge_pair_schema.json),
produced by `seven_block_two_edge_pair_audit.py` and independently checked by
`verify_seven_block_two_edge_pair_schema.py`. The independent verifier
recomputes the duplicate-edge conclusion and every finite relation summary
from the skeleton and recorded edge relations; stabilizer and support-cycle
metadata remain producer-derived receipt data.

## Intrinsic comparison

| Orbit | Pair | Common blocks | Shared regions in block 1 | Shared regions in block 2 | Candidate edges | Result |
|---|---:|---:|---|---|---:|---|
| O2 | `(5,51)` | `B,D0` | `{1,4,50,0}` | `{1,4,50,0}` | 2 | duplicate |
| O3 | `(15,45)` | `B,D2` | `{5,10,40,0}` | `{5,10,40,0}` | 2 | duplicate |

The entries list shared, left-private, right-private, and outside regions.
The outside region is zero in both cases because the two selectors join to
top. Their generated sub-OMLs both have eight elements.

O2 has selector interval sizes `6,16`, support sizes `4,3`, and the five-cycle

`B-Ca-D0-D2-D3-B`.

Its region supports are: shared `1` on `B,D0,D1`; left-private `4` on
`B,D0,D3`; right-private `50` on `B,Ca,D0,D2`.

O3 has interval sizes `16,16`, support sizes `3,3`, and the four-cycle

`B-D1-D2-D3-B`.

Its region supports are: shared `5` on `B,Ca,D0,D2`; left-private `10` on
`B,D1,D2`; right-private `40` on `B,D2,D3`.

All overlap algebras along both cycles are recorded eventwise in the
certificate. The unordered-pair stabilizers have sizes 16 (O2) and 32 (O3).
Neither stabilizer exchanges the two common blocks. This asymmetry does not
make the induced datum different: both blocks contain the same lattice
elements and the same generated eight-element sub-OML.

O3 is therefore the minimal serious control by structural complexity: it has
the shorter support cycle, equal selector interval sizes, equal support sizes,
and the larger stabilizer. O2 is retained as the asymmetric control.

## What the two equations actually say

Let `D` be a proper coarse Boolean algebra used to refine the common generated
datum, and let `A,C` refine the endpoint information. Each common block would
write

\[
 u|_D=v|_D.
\]

But the two occurrences have the same embeddings `D -> A,C`: the embeddings
are induced by the same four skeleton regions. Thus `D1=D2=D` as embedded
subalgebras, not merely as abstract Boolean algebras, and

\[
 R=\{(u,v):u|_{D_1}=v|_{D_1},\ u|_{D_2}=v|_{D_2}\}
   =\operatorname{Ult}(A)\times_{\operatorname{Ult}(D)}\operatorname{Ult}(C).
\]

This is a single-pullback reduction. There is no transport cycle and hence no
monodromy. Full OML closure cannot turn two identical equations into
inequivalent equations; it can only retain the equation, add further
restrictions, or destroy the intended construction. No O2/O3 mixed family was
constructed here, so latticehood, maximal blocks, centre, and infinite
sigma-completeness are deliberately left unclaimed.

## Finite relation controls

The certificate computes four `4 x 4` Stone controls.

| Control | Relation size | Degrees | Components | Edge status |
|---|---:|---|---:|---|
| duplicate | 8 | `2,2,2,2` both sides | 2 | each copy implied |
| nested | 8 | `2,2,2,2` both sides | 2 | coarse edge implied by fine edge |
| jointly generating | 4 | all 1 | 4 | graph of identity |
| transverse proper | 4 | all 1 | 4 | neither edge implied |

The duplicate and nested controls reduce to the stronger single quotient.
The jointly generating control identifies the full endpoint coordinate. The
transverse control shows that two proper inequivalent edges are combinatorially
possible, but it is not realized by O2 or O3 event overlap. None of these
finite relation calculations proves an infinite selection statement.

## State-selection consequences

For O2/O3 there is no new two-edge state-selection problem. The eligible face
is governed by one pullback, so the exact extension hypothesis and
common-point repair theorem in
[`oml_nonatomic_pullback_completion.md`](oml_nonatomic_pullback_completion.md)
apply when their hypotheses hold. Nonrectangularity and noncompact eligible
sigma-state topology remain insufficient to refute `Phi`. Without a specified
coarse carrier and compatible endpoint sigma-extension property, complete
sigma-selection is open; it is not inferred from this finite audit.

## Reusable no-go lemma (hand proof)

**Repeated-common-block lemma.** Let `L` be an OML and let two Boolean blocks
`M,N` contain the same elements `e,f`. The Boolean subalgebras generated by
`e,f` in `M` and `N` coincide as embedded sub-OMLs of `L`.

*Proof.* Meets and orthocomplements are operations of `L`, hence the four
regions displayed above are the same elements whether evaluated in `M` or
`N`. Finite joins of those pairwise orthogonal regions are likewise lattice
joins in `L`. They are exactly the Boolean algebra generated by `e,f`. ∎

This is a hand proof, not a Lean certificate. It establishes only that
repeated containment of one selector pair cannot itself supply inequivalent
quotient embeddings.

## Answers to the handoff gates

1. O3 is the smaller candidate, with O2 as control.
2. Each of its two blocks imposes the same four-region restriction.
3. The constraints are already equivalent before completion.
4. No new completed family is asserted; the banked `(5,11)` family remains
   the only completed non-atomic pullback in this lane.
5. No new infinite model is asserted.
6. No new maximal-block classification is asserted.
7. No new centre calculation is asserted.
8. The intended relation reduces to one pullback.
9. There is no genuine monodromy.
10. No new finite face or noncompact topology is produced.
11. Finite controls are solvable, but do not imply infinite solvability.
12. Complete selection requires the banked common-extension hypothesis and is
    otherwise open.
13. The repeated-common-block lemma is the reusable no-go statement.
14. Next find a skeleton datum involving distinct event families whose
    overlaps induce transverse embedded subalgebras; counting common blocks of
    one pair is exhausted.

## Reproduction

```sh
python3 notes/open_questions/verification/seven_block_two_edge_pair_audit.py \
  --output notes/open_questions/verification/seven_block_two_edge_pair_schema.json
python3 notes/open_questions/verification/verify_seven_block_two_edge_pair_schema.py
```
