# Terminology fence for the coherence corpus

*Status: active terminology note, 2026-08-04. This note records distinctions
already exposed by the latticehood prior-art audit; it introduces no new
mathematics.*

## `EA` and `PR` are source-local symbols

| source | `EA` | `PR` |
|---|---|---|
| [Reconstruction](../papers/reconstruction/reconstruction_skeleton.tex) | A finite family of local probability tables agrees on every event shared by two contexts. | `PR(R)`: one global process in the declared class `R` induces all the local tables. |
| [Distributivity and realism](../papers/paper_ii/distributivity_and_realism_body.tex) | A measure/set-function on the relevant dual representation agrees with the observational charges, with the paper's stated OML scope caveat. | Descent to a probability measure on an underlying realisation space; in the OML discussion this separates into `PR_lat` and `PR_dual`. |

The two pairs have a common local-to-global motivation but different domains,
maps, and codomains. No equivalence or translation between them is currently
established. Accordingly:

- write `PR(R)` when the reconstruction realisation class matters;
- write `PR_lat` or `PR_dual` in the realism paper's OML setting;
- never use an unqualified cross-paper implication `EA => PR` without first
  restating the source-specific definitions.

## Standalone `VDR` and the filtration endpoint are different predicates

For an observation algebra `A`, let:

- `S(A)` be all finitely additive states;
- `S_sigma(A)` be the sigma-additive states;
- `S_df(A)` be all dispersion-free states; and
- `S_df^sigma(A) := S_df(A) intersect S_sigma(A)`.

The canonical standalone meaning is

`VDR(A) <=> S_df(A) is nonempty`.

When the sigma-additive endpoint is intended, write

`VDR_sigma(A) <=> S_df^sigma(A) is nonempty`.

The typed filtration is

`S(A) superset S_sigma(A) superset S_df^sigma(A)`.

Thus the filtration endpoint carries an explicit sigma-additivity clause that
standalone VDR does not. The predicates agree on finite carriers and whenever
sigma-additivity has been established separately; they must not be silently
identified on an arbitrary infinite carrier. Distributivity supplies
standalone VDR through ultrafilters, but that fact alone is not a regularity
theorem. Kochen--Specker empties `S_df`, and hence also `S_df^sigma`, for
`L(H)` in dimension at least three.

This convention preserves the operative VDR definition in Paper II while
making every sigma-additive use visible as `VDR_sigma` or `S_df^sigma`.
