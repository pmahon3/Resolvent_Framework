# Independent mathematical review of the arbitrary-base q0 inflation

*Reviewed 2026-07-13. The arbitrary-base statement survives an independent
hand-proof audit at its stated scope. It remains a hand proof, not a Lean
certificate.*

## 1. Statement under review

Start with the certified 44-event concrete OML formed by the five blocks
`A00,A01,C01,A10,A11`, and let `q0` be the four-point event that is an atom
of exactly `A00,A01,C01`. For a nondegenerate concrete Boolean sigma-algebra
`A` on a set `D`, replace the interval below `q0` in those three blocks by
the common copy

\[
        \widehat A=\{a\times q0:a\in A\}
\]

on the carrier obtained by replacing each point of `q0` by a copy of `D`.
Lift every skeleton event by inverse image. Keep the lifted finite blocks
`A10,A11` unchanged. The claim is that the union is a concrete,
sigma-complete OML whose maximal Boolean blocks are exactly the five named
blocks, whose centre is trivial, and which is Phi-tame.

This is an arbitrary-base hand theorem. The finite receipts do not by
themselves widen to this statement.

## 2. Carrier and normal-form check

The construction is well-defined even though `A10,A11` split `q0`. A lifted
crossed skeleton event contains either all or none of the copy of `D` over
each original point. An event in one of the three inflated blocks has a
unique form `E(a,S)`: one coefficient `a in A`, repeated over all four
original points below `q0`, together with a subset `S` of its three outside
atoms. Thus crossed finite events and fibre-parameter events coexist as
subsets of one carrier; no quotient identification is being assumed.

For two coefficients `a,b`, every Boolean relation is determined on the four
regions

\[
 a\cap b,\quad a\cap b^c,\quad a^c\cap b,\quad a^c\cap b^c.
\]

Specializing `E(a,S)` and `E(b,T)` to zero or one on each nonempty region
reduces inclusion, disjointness, complement, the compatibility equation,
and candidate extrema to the 44-event skeleton. This justifies using the
`P(4)` binary control without assuming that `A` is atomic.

## 3. Lattice and maximal-block audit

The binary normal-form reduction gives closure under complement and disjoint
union, unique extrema, and the orthomodular equation from the certified
finite skeleton controls. It therefore gives a concrete OML at hand-proof
level.

Centralizer calculations alone would not classify its blocks. The separate
60-form audit closes that gap as follows.

1. A finite compatible family specializes, on every occurring coefficient
   truth vector, to a compatible family of skeleton events.
2. If it were contained in none of the five named blocks, an
   inclusion-minimal subfamily would have at most five events: choose one
   event excluding each block label. Repeated form signatures are redundant
   in such a minimal obstruction.
3. The exact truth-vector census finds no feasible minimal obstruction among
   the 60 forms through size five. Its independent four-region cross-check
   performs 47,070 form-instance comparisons.
4. For an arbitrary compatible family, the named-block signature sets have
   the finite-intersection property inside a fixed five-element set. Their
   total intersection is nonempty, since otherwise five events already
   witness failure.

Hence every compatible family lies in a named block, and the five displayed
blocks are exactly the maximal Boolean blocks. Steps 1 and 4 are hand
arguments; the finite census is executable evidence.

Their intersection is `{0,1}`, so the centre is trivial once the maximal
block classification is available.

## 4. Sigma-completeness audit

Let `(x_n)` be a countable disjoint family of nonzero events. Only finitely
many `x_n` can be crossed events from the two unchanged finite blocks. Among
the remaining inflated-block events, only finitely many have nonempty
outside support, because those supports are disjoint subsets of a fixed
finite set of skeleton points. The remaining tail lies in the common copy
of `A`, where its union exists. Binary closure joins the finite head and then
joins it to the tail union. Thus the concrete union is closed under
countable disjoint unions.

For a countable family in an OML, successive disjointization using finite
joins and orthocomplements converts this closure into existence of its
countable join. This proves sigma-completeness at hand-proof level. It is not
certified by the bounded approximants.

## 5. State and Phi audit

Point evaluations order-separate the concrete carrier. A coherent local
two-valued state charging `q0` supplies one common ultrafilter of `A` on the
three inflated blocks; its finite skeleton component extends across
`A10,A11` by the verified 44-event state census. The same construction is
sigma-additive when the local ultrafilter is sigma-additive.

Phi-tameness uses concreteness of `A`. Given a finite trace of an arbitrary
ultrafilter `U` of `A`, intersect the finitely many trace sets oriented by
`U`. This intersection belongs to `U`, hence is nonempty. Evaluation at a
point of that intersection is a sigma-additive two-valued state agreeing
with `U` on the trace. Combining it with the same finite skeleton extension
reproduces the requested global trace. If `q0` has value zero, the fibre is
invisible. This proves only Phi-tameness of this construction, not the
standing OML conjecture.

## 6. Evidence ledger and decision

- **Hand-proved, pending human acceptance:** arbitrary-base concrete OML,
  exact five-block classification, sigma-completeness, trivial centre,
  state extension, order separation, and Phi-tameness.
- **Executable finite evidence:** the 44-event survivor; `P(n)` fibre
  approximants for `n=2,3,4`; the 60-form obstruction census and 47,070
  four-region comparisons; the eight `P(2)` whole-interface twists.
- **Not proved:** an arbitrary classification of transverse inflations, a
  proper-interface twist theorem, a two-coordinate theorem, or the standing
  sigma-essential-state conjecture.
- **Not formalized:** every arbitrary-base assertion in this note.

No mathematical structural gate failed in this review. The first unresolved
gate is procedural and epistemic: the runbook requires human authorization
before the arbitrary-base hand theorem is banked. The strongest currently
available obstruction beyond the theorem remains the scoped `P(2)` result:
an odd whole-interface triangle twist is nonfaithful, while an even twist is
gauge-equivalent to the untwisted Phi-tame inflation.

After human acceptance, the next lemma-sized task is to test a twist on a
proper shared subalgebra of the inflated triangle. Maximal-block
classification and sigma-completeness are the first stop gates. If that
class is again gauge-trivial, test a second inequivalent coarse coordinate.

## Reproduction

```sh
python3 notes/open_questions/verification/exhaustive_boundary_properness_audit.py \
  --output notes/open_questions/verification/exhaustive_boundary_properness_schema.json
python3 notes/open_questions/verification/verify_exhaustive_boundary_properness.py
python3 notes/open_questions/verification/exhaustive_boundary_inflation_audit.py \
  --max-fibre-atoms 4 \
  --output notes/open_questions/verification/exhaustive_boundary_inflation_schema.json
python3 notes/open_questions/verification/five_block_global_compatibility_audit.py \
  --output notes/open_questions/verification/five_block_global_compatibility_schema.json
python3 notes/open_questions/verification/verify_five_block_global_compatibility.py
python3 notes/open_questions/verification/five_block_smallest_twist_audit.py \
  --output notes/open_questions/verification/five_block_smallest_twist_schema.json
python3 notes/open_questions/verification/verify_five_block_smallest_twist_schema.py
```
