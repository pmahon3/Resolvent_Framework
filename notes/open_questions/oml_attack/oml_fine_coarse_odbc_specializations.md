# Fine and coarse ODBC specializations

*Campaign 4, 2026-07-13. The unconditional fine and coarse objectives remain
open. This note records the strongest valid specializations and exact
controls.*

## 1. Fine locally-countable-defect theorem

Assume every maximal block is countably generated and T4At holds. For a
coherent finite face `C_p` and maximal block `B`, set

`N_B(p)={mu in C_p : mu|B is not sigma-additive}.`

Each `N_B(p)` is closed and nowhere dense in `C_p`: closedness is the banked
fine-block result, and hereditary T4At excludes nonempty finite-coordinate
interior.

### Theorem 1.1

If the family of nonempty `N_B(p)` is locally countable on every `C_p`,
then Phi holds.

*Proof.* Compactness of `C_p` turns a locally countable family into a
countable family: finitely many neighborhoods cover `C_p`, and each meets
only countably many loci. A countable family of closed nowhere-dense sets
cannot cover the Baire space `C_p`. A state outside their union is
sigma-additive on every maximal block, hence globally sigma-additive.
**Evidence class: hand proved.**

The same conclusion holds under the weaker explicit hypothesis that every
cover of `C_p` by the `N_B(p)` admits a countable subcover. **Evidence class:
hand proved.**

Point-countability is insufficient: Cantor singleton defects are point-one
and cover the face. Countable-support/elementary-submodel arguments fail
without a reflection theorem. The stated finite-face-only transfinite repair
scheme fails at limit stages because T4At applies only to finite faces; this
does not exclude every possible transfinite method. **Evidence class:
refuted.**

Thus fine block generation controls individual loci but not their atlas
incidence. The open OML-specific lemma is whether lattice cuts, essential
irreducibility, and global sigma-state order separation force the
countable-subcover property.

## 2. Coarse countable-intersection reflection

Let `A subset B subset P(Omega)` be a boundary Boolean algebra inside a
Boolean sigma-block, let `t` be a boundary ultrafilter, and let `E in B` be
the forced pattern event. Put

`F(t,E)={E} union {a in A:t(a)=1}.`

Say `(B,A,t,E)` has **countable-intersection reflection (CIR)** when empty
total intersection of `F(t,E)` is witnessed by a countable subfamily.

### Theorem 2.1 (CIR coherent-lift theorem)

Assume CIR and assume every countably generated sigma-subalgebra
`C subset B` has a sigma-state agreeing with `t` on `A intersect C` and
charging `E` whenever `E in C`. Then `F(t,E)` has nonempty total
intersection. Every point in that intersection defines a compatible Dirac
family on all countably generated envelopes, hence one coherent coarse lift.

*Proof.* If the total intersection were empty, CIR would supply a countable
chosen subfamily with empty intersection. Put its events and `E` in one
countably generated envelope. Its alleged sigma-lift charges each member and
therefore their countable intersection, contradiction. **Evidence class:
hand proved.**

For an atlas and fixed common global `mu`, CIR at every block plus separate
envelope solvability gives a pointwise compatible coarse section.
**Evidence class: hand proved.**

The club-field control violates CIR exactly: the total intersection of all
chosen sets is empty while the intersection of every countable chosen
subfamily contains a club and is nonempty. **Evidence class: hand proved.** It still supplies no
coherent lift and no finite pattern forcing the entire bad trace.

## 3. Coarse specialization is not logically separate

Coherent families over all countably generated subalgebras reconstruct
exactly one sigma-state on the full block. Therefore coarse ODBC, as defined
in Campaign 1, is canonically equivalent to ordinary ODBC and hence to Phi.
It is a two-level presentation, not an easier factor. **Evidence class: hand
proved.**

Any genuinely weaker coarse theorem must add CIR, compact witness closure, or
another OML coupling hypothesis. Objectwise envelope solvability is refuted
by the club field.

## 4. Joint hostile audit

- A common `mu` is required within `X_p(J)` but may vary with `J`. Fixing it
  coherently across all subsystems is already a global section.
- Local point states separating each Boolean block do not imply global OML
  order separation; extension must be proved.
- A nonclosed Borel correspondence block is countably generated and threatens
  fine ODBC only if maximal-block completion preserves countable generation.
- The singleton and club controls are not OML counterexamples.

All four statements are **evidence class: hand proved** as logical audits.

## 5. Campaign verdict

Fine ODBC remains open beyond the locally-countable/countable-subcover
defect-incidence theorem. Coarse ODBC is the full conjecture, but CIR gives
the strongest new local coherence criterion and the club field identifies
its exact failure.

The two sufficient-condition residues are not an exhaustive fine/coarse
bifurcation:

1. **Fine incidence theorem:** admissible fine OMLs force countable-subcover
   reflection for `{N_B(p)}`.
2. **Coarse coherent-lift theorem:** for each required common `mu`, OML
   hypotheses force both objectwise same-`mu` envelope solvability and CIR,
   or directly force an equivalent coherent full-block lift.

The fine theorem feeds ODBC in its regime; the coarse conjunction is already
a route to full ODBC. Failure of either condition alone is only an abstract
control unless finite forcing and all OML realization gates are supplied.
**Evidence class: open.**
