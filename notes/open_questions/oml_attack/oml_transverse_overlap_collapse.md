# Minimal distinct-family transverse-overlap audit

*Completed 2026-07-12. Outcome C for the jointly-generating four-point
candidate: the two proper overlap families are genuinely transverse, but a
literal OML realization collapses the proposed endpoint blocks to one Boolean
block. This is a hand-proof mechanism exclusion with finite executable
evidence, not a Lean certificate or a general transverse-overlap theorem.*

## 1. Candidate and scope

Take two four-atom Boolean endpoints. On the left use the two proper
two-cell partitions

\[
 P=01|23,\qquad Q=02|13,
\]

and on the right use

\[
 P'=01|23,\qquad R'=03|12.
\]

The proposed overlap equations identify the `P` datum with `P'` and the
distinct `Q` datum with `R'`. Each edge is proper. Neither equation implies
the other, so this is a genuine distinct-event-family transverse control,
unlike the duplicate O2/O3 equations. However, each pair of partitions
separates all four endpoint atoms and hence generates the full endpoint
Boolean algebra.

The executable receipt is
[`../verification/four_point_transverse_overlap_schema.json`](../verification/four_point_transverse_overlap_schema.json),
produced by `four_point_transverse_overlap_audit.py` and independently
recomputed by `verify_four_point_transverse_overlap_schema.py`. Its scope is
exactly this finite four-point candidate. It does not classify transverse
families that generate only proper endpoint subalgebras.

## 2. Collapse lemma (hand proof)

**Joint-generation collapse lemma.** Let `M,N` be Boolean blocks of an OML
`L`, and let `D1,D2` be embedded Boolean subalgebras contained in `M ∩ N`. If
`D1 ∪ D2` generates `M` as a Boolean algebra and also generates `N`, then
`M=N`.

*Proof.* Complement, meet, and join are operations of `L`. Therefore every
finite Boolean expression in elements of `D1 ∪ D2` denotes the same lattice
element whether evaluated in `M` or in `N`. The two generated embedded
Boolean subalgebras coincide. By the two generation hypotheses they are `M`
and `N`, so `M=N`. ∎

This lemma is slightly broader than the finite receipt, but remains a hand
proof. It says nothing when the two overlaps jointly generate only proper
subalgebras of their endpoint blocks.

Applying it to `P,Q` and `P',R'` shows that the intended two-distinct-block
architecture cannot be realized literally in an OML. Its canonical collapsed
realization is the Boolean algebra `P({0,1,2,3})`.

## 3. State relation

The individual equations give two distinct eight-pair relations, with
neither relation contained in the other. Their intersection is

\[
 \{(0,0),(1,1),(2,3),(3,2)\},
\]

the graph of a permutation. Thus the two transverse restrictions determine
the entire endpoint ultrafilter. This is state-coordinate collapse, not
nontrivial two-edge transport or monodromy.

## 4. Structural gates, reported separately

| Gate | Intended two-block candidate | Collapsed finite realization | Evidence |
|---|---|---|---|
| Latticehood | no distinct-block candidate remains: intrinsic lattice operations force block collapse | yes, the 16-element Boolean algebra | hand lemma; executable finite check |
| σ-completeness | not reached for the intended architecture | yes, because finite | hand; finite check |
| Maximal blocks | refuted: the proposed two blocks are equal | exactly one | hand lemma; finite check |
| Centre / irreducibility | intended centre is not defined | centre is all 16 elements; not essentially irreducible | finite check |
| State extension | no separate two-block extension problem survives | all four compatible pairs extend as the four point evaluations | executable finite check |
| Order separation | not reached for a non-Boolean candidate | the four evaluations order-separate the power set | executable finite check |
| Φ / σ-essentiality | no candidate remains | trivially tame since finite additivity equals σ-additivity | hand consequence of finiteness |

The positive entries for the collapsed Boolean algebra do not rescue the
candidate: it misses non-Booleanity, two-block maximality, and essential
irreducibility.

## 5. Exact conclusion and next gate

The minimal jointly-generating transverse square is closed. Distinct event
families avoid the O2/O3 duplicate-edge defect, but in the four-atom case
they determine the whole coordinate and force Boolean block equality. This
does **not** exclude larger transverse architectures. The next candidate must
use two inequivalent overlap families whose joint Boolean closure is proper
in at least one endpoint block, then independently test mixed completion,
all maximal blocks, centre, σ-completeness, state extension, and order
separation.

## Reproduction

```sh
python3 notes/open_questions/verification/four_point_transverse_overlap_audit.py \
  --output notes/open_questions/verification/four_point_transverse_overlap_schema.json
python3 notes/open_questions/verification/verify_four_point_transverse_overlap_schema.py
```
