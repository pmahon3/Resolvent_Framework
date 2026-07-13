# Proper boundary surviving exhaustive maximal completion

*Completed 2026-07-13. Outcome A for the bounded search: among all 127
nonempty subfamilies of the seven labelled maximal blocks of the certified
56-event OML, four centre-free finite OMLs retain a proper full maximal-block
boundary and a proper-closure transverse triangle. The smallest have 44
events. This is exhaustive finite evidence for that fixed block-subfamily
class, not a classification of arbitrary completions, an infinite theorem,
or a Lean certificate.*

## 1. The 44-event survivor

Use the labelled blocks from
[`oml_three_block_noncentral_transverse_candidate.md`](oml_three_block_noncentral_transverse_candidate.md)
and retain

\[
             A00,\quad A01,\quad C01,\quad A10,\quad A11.
\]

Their union has 44 events on the same 16-point carrier. Exhaustive
compatibility-clique enumeration shows that these are exactly its five
maximal Boolean blocks, all of size 16. The union is closed under complement
and disjoint binary union, has unique meet and join for every ordered pair,
satisfies the orthomodular law for every comparable pair, and has centre
`{0,1}`. Finiteness therefore gives a concrete sigma-complete OML.

The full overlap-generated boundary sizes are

| block | `A00` | `A01` | `C01` | `A10` | `A11` |
|---|---:|---:|---:|---:|---:|
| boundary size | 16 | 16 | 8 | 16 | 16 |

Thus `C01` retains a proper eight-element boundary even after every maximal
block of this completion has been classified and included. The triangle
`A01,C01,A10` has three distinct four-element pairwise interfaces and
eight-element proper incident joint closure at every vertex. Since the
ambient centre is trivial, all its nontrivial interface events are
noncentral.

## 2. State and regularity gates

The exhaustive block-ultrafilter census finds 12 global two-valued states.
They are exactly the 12 distinct point-evaluation signatures. They
order-separate the 44-event carrier, and their restrictions give all 12
locally coherent two-valued block-ultrafilter triples on the transverse
triangle. Hence the finite completion loses no triangle state.

The candidate remains Phi-tame and has no sigma-essential state: on a finite
carrier, finite and countable additivity coincide. It passes the finite
proper-boundary gate but does not address the required noncompact local
sigma-state slice. The next step is therefore an infinite inflation of the
44-event incidence pattern, with maximal blocks, latticehood,
sigma-completeness, centre, global state extension, order separation, and
noncompactness re-audited rather than inherited from the finite control.

## 3. Exhaustive scope

The census checks all `2^7-1=127` nonempty labelled block subfamilies. Of
these, 100 fail concrete-logic closure and 27 are OMLs. Exactly four satisfy
all of: trivial centre, exact named maximal-block classification, a proper
full boundary, and a proper-closure transverse triangle. All four have 44
events. This minimality is only inside the fixed seven-block subfamily
universe; no claim is made about all finite OMLs or all transverse
completions.

## Reproduction

```sh
python3 notes/open_questions/verification/exhaustive_boundary_properness_audit.py \
  --output notes/open_questions/verification/exhaustive_boundary_properness_schema.json
python3 notes/open_questions/verification/verify_exhaustive_boundary_properness.py
```

