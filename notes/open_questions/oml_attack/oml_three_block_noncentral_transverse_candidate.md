# Three-block noncentral transverse triangle

*Completed 2026-07-13. Outcome B for the finite search: the existing
56-event centre-free completion contains a three-block triangle whose two
incident overlap algebras have proper joint closure at every vertex. All
coherent triangle states extend and point states order-separate the
completion. The seven-block maximal completion nevertheless saturates every
full overlap-generated boundary, and finiteness makes the example Phi-tame.
This is executable finite evidence, not a new infinite theorem or Lean
certificate.*

## 1. Labelled completion

Use the 16-point carrier and 56-event OML from
[`oml_irreducible_boundary_test.md`](oml_irreducible_boundary_test.md#42-the-56-event-centre-free-completion).
Its two `MO2 x MO2` halves have a common Boolean block. Label the four
maximal blocks of the first half `A00,A01,A10,A11`, according to which of
the two decompositions is selected in each factor. Label the second half
similarly by `C00,C01,C10,C11`, with `C00=A00`. These are exactly the seven
maximal Boolean blocks of the completion, each with 16 events.

The bounded search over all labelled triples selects

\[
                 A01,\qquad C01,\qquad A10.
\]

Every pairwise intersection has four elements. At each of the three
vertices, the two incident intersections are distinct and generate an
eight-element Boolean algebra, properly contained in the 16-element vertex
block. Since the centre of the whole 56-event OML is `{0,1}`, every
nontrivial interface event is noncentral. Thus this is a literal finite
three-block noncentral proper-joint-closure triangle.

This does not make the selected three-block union a standalone OML. The
mixed closure is the full seven-block, 56-event completion.

## 2. Structural and state gates

The exhaustive set calculation checks the following facts for that mixed
completion.

| Gate | Result |
|---|---|
| Pairwise triangle interfaces | `4,4,4`, distinct at every vertex |
| Incident joint closures | `8 < 16` at every vertex |
| Interface centrality | all nontrivial interface events are noncentral |
| Mixed completion | 56 events on 16 points |
| Latticehood / orthomodularity | yes, all ordered pairs / comparable pairs checked |
| Sigma-completeness | yes, by finiteness |
| Maximal blocks | exactly seven, each of size 16 |
| Centre | `{0,1}` |
| Triangle state extension | all 12 coherent two-valued block-ultrafilter triples extend |
| Global two-valued states | 16, exactly the point evaluations |
| Order separation | yes, by point evaluations |
| Phi / sigma-essentiality | Phi-tame; no sigma-essential state, by finiteness |

The state census enumerates all `4^7` choices of a block atom and retains
the 16 choices coherent on every pairwise block intersection. These are
exactly the 16 point evaluations. Restricting them to the selected triangle
gives exactly its 12 locally coherent triples, so no local triple is lost in
the seven-block completion.

## 3. Saturation obstruction

The local three-block gate is therefore passed: neither a central-factor
obstruction nor state-extension failure follows from proper joint closure.
The positive existence statement is finite executable evidence; what this
refutes is only the proposed local obstruction that proper joint closure
must become central.
But the completion creates four additional maximal blocks. Once interfaces
with *all* maximal blocks are included, the overlap-generated boundary of
each block is its full 16-element Boolean algebra.

Hence this finite survivor does not supply the still-needed proper maximal
boundary, noncompact sigma-state slice, or failure of Phi. It sharpens the
next gate: retain a proper joint closure after the exhaustive maximal-block
completion, rather than only on a selected transverse triangle.

## Reproduction

```sh
python3 notes/open_questions/verification/three_block_noncentral_transverse_audit.py \
  --output notes/open_questions/verification/three_block_noncentral_transverse_schema.json
python3 notes/open_questions/verification/verify_three_block_noncentral_transverse.py
```

The JSON receipt records only this finite carrier and its labelled triangle.
The pre-existing independent structural receipt
`three_block_completion_audit.py` separately reconstructs the 56-event OML,
its seven maximal blocks, trivial centre, and saturated full boundaries.
