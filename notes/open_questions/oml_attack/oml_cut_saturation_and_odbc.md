# Lattice cut-saturation versus ODBC

*Campaign 2, 2026-07-13. This note records exact positive scopes and the
failure of bare cut-saturation to control eligible state loci.*

## 1. Event-profile cut-saturation

Let `r_t : L -> P(Omega_t)` be a finite family of concrete restrictions and
let `Q = { (r_t(E))_t : E in L }` with coordinatewise inclusion. Define
`PCS(r)` to mean: for every finite nonempty `A,C subset Q` with `a <= c`
for all `a in A,c in C`, the inherited interval
`Q intersect [union A, intersection C]` is nonempty. Define `DM-PCS(r)` to
mean that every finite family has its inherited least upper and greatest
lower bounds in `Q`.

For finite `Q` containing top and bottom, `DM-PCS` is equivalent to `Q`
being a lattice in the inherited order. In the finite-typed,
countable-exception setting of `oml_typed_graph_closure_calculus.md`, where
every profile is uniformly realized and every type survives the exceptional
ideal, concrete latticehood implies `DM-PCS`. This is the profile-interval
theorem already proved there. **Evidence class: hand proved.**

Neither condition is a sufficient event-realization theorem outside that
scope, and neither mentions states.

## 2. Cut-saturation does not imply subsystem sections

Take an abstract face space `C_p={0,1}` and two block labels. Let the first
eligible fibre be nonempty exactly at `mu=0`, and the second exactly at
`mu=1`. Each singleton block subsystem has a common-witness section, but the
two-block subsystem has none. Independently choose the event-profile
relation `{(0,0),(1,1)}`, a complemented inherited lattice satisfying
`DM-PCS`.

Thus even maximal finite profile cut-saturation does not imply ODBC-S,
rectangularity, or a Helly property for eligible common-state loci.
**Evidence class: refuted.** This is an abstract separation, not an OML.

For a concrete control, let `B=P(N)`. Its event order is a complete Boolean
lattice and its point sigma-states separate order. A nonprincipal
ultrafilter `mu` has every finite family of truth equations reproduced by a
point state, but no sigma-additive two-valued state agrees with `mu` on all
of `B`. Hence concreteness, all lattice cuts, and sigma-state order separation
do not upgrade finite event agreement to a whole-boundary lift for a fixed
`mu`. **Evidence class: hand proved.** The Boolean control is not an
admissible counterexample. Product with a finite non-Boolean concrete OML
retains the obstruction and order separation but is centrally reducible.

## 3. Exact finite-atlas quantifier warning

If the full maximal-block atlas `I` is finite or countable, the countable
subsystem family contains `J=I`. Therefore CODBC is tautological on that
atlas, and ODBC-S already asks for the global section. Proving ODBC for a
finite tree or cycle means proving Phi directly.

For a finite proper subatlas inside an uncountable atlas, `X_p(J)` must still
match each block's full boundary, including its overlaps with blocks outside
`J`. An induced incidence tree discards load-bearing equations. **Evidence
class: hand proved.**

## 4. Positive finite scopes

### Theorem 4.1 (exact two-block, trivial-centre atlas)

Suppose the full maximal-block atlas of a concrete OML is exactly
`{B_0,B_1}` and its centre is `{0,1}`. Then both generated boundaries are
`{0,1}`, and the OML satisfies Phi and ODBC.

*Proof.* Every event in `B_0 intersect B_1` is compatible with every event
of `L=B_0 union B_1`, hence is central. The centre hypothesis makes the
intersection, and therefore each boundary, trivial. Finite-interface
quarantine gives Phi; GSD gives the corresponding global section. **Evidence
class: hand proved.**

The repository's essential-irreducibility condition should not be silently
identified with literal trivial centre; Theorem 4.1 uses trivial centre
explicitly.

### Theorem 4.2 (finite interfaces, arbitrary incidence graph)

If every maximal block has finite generated boundary, then Phi and ODBC
hold, regardless of whether the atlas is a tree, acyclic hypergraph, cycle,
or arbitrary graph. **Evidence class: hand proved.** The raw-overlap version
of finite-interface quarantine is Lean verified; the finite
generated-boundary equivalence is hand proved.

### Theorem 4.3 (finite fine atlas under T4At)

If the maximal-block atlas is finite, every maximal block is countably
generated, and T4At holds, then Phi and ODBC hold. **Evidence class: hand
proved.** This is the reviewed countable-atlas theorem; T4At cannot be
dropped.

No unconditional result follows for coarse finite trees, acyclic atlases,
cycles, finite typed overlaps, or systems with infinite generated
boundaries.

## 5. Closed-eligibility compactness theorem

For fixed coherent `p`, put
`K_I = C_p times product_{B in I} St_fa(B)`.
The global finitely additive state space and every block ultrafilter space
are compact Stone spaces. Let `R_B` be the pairs `(mu,v)` for which `v`
charges `E_B(p)`, is sigma-additive on `B`, and agrees with `mu` on
`partial B`.

### Theorem 5.1 (relative closed eligibility)

If every `R_B` is closed in the corresponding compact factor and every
finite subsystem has a section, then `X_p(I)` is nonempty.

*Proof.* Pull each `R_B` back to a closed cylinder in `K_I`. Finite subsystem
solvability is exactly the finite-intersection property for these cylinders.
Compactness gives a common point. **Evidence class: hand proved.**

Surjectivity of bonding maps is unnecessary. The theorem proves
Finite-CODBC under relative closedness.

The hypothesis fails generically: in `St_fa(P(N))=beta N`, the
sigma-additive two-valued states are the principal ultrafilters `N`, which
are dense, nonclosed, and noncompact. **Evidence class: hand proved.**

## 6. Surjectivity, Mittag--Leffler, and soft-map audit

The map `rho_J^K` is surjective exactly when every already chosen common
`mu` and every family of `J`-lifts extends to all blocks in `K`. CSS only
permits a new witness `mu_K`, so it gives no surjectivity.

In the Cantor singleton control, take `C` compact zero-dimensional,
`I=C`, and let the `i`-constraint be `mu != i`. Then `X(J)=C\J`: every
countable subsystem is nonempty and the global space is empty. Restriction
maps are nonsurjective; their images never stabilize, so Mittag--Leffler
fails. Fibres are empty or singletons, proving that compact fibres alone do
not help. Flabbiness or softness would simply assume the missing extension
property. **Evidence class: hand proved.**

## 7. Cut-contradiction attempt and exact residue

No cut contradiction follows from a sectionless inverse system: lattice
cuts constrain event order, while the failure can live solely in the
nonclosed sigma-additive sublocus of the state space. Bare graph acyclicity
also addresses the wrong quantifier, since independently glued traces need
not arise from one global `mu`.

The next full-atlas cardinal after the exact centre-free two-block theorem is
a coarse, literally centre-free, three-block OML with infinite generated
boundaries. For a coherent `p`, put
`G_B(p)={mu in C_p : Y_B(p,mu) is nonempty}`.
The section hierarchy has three separate gates: every singleton `G_B` is
nonempty; every pair intersection is nonempty; and the triple intersection
is nonempty. None is proved generically. A failure may occur at any gate.
Conditional on the pair gates, the empty-triple case is a Helly-3 trap.
**Evidence class: open.**

## 8. Campaign verdict

Cut-saturation is necessary in the scoped profile calculus but insufficient
for ODBC-S even abstractly. The strongest generic positive theorem is
relative closed eligibility; its hypothesis is refuted in the unrestricted
Boolean setting. The Campaign-2 programme therefore stalls at one exact
class theorem:

> **Three-block relative-eligibility theorem.** In every admissible
> centre-free three-block concrete sigma-complete OML,
> `intersection_B G_B(p)` is nonempty for every coherent finite pattern `p`.

Its proof would establish the first new ODBC-S class beyond finite
interfaces. Its refutation supplies a realized failure architecture at the
first failed singleton, pair, or triple gate. Bare abstract PCS remains
insufficient, but an OML-coupled cut theorem is open.
