# Archived: `directedness-interpolation` Branch Sketches

These three documents were exploratory work from the `directedness-interpolation`
branch, which has since been merged into `main` and superseded.

## Files

**`directedness_interpolation.md`**
Explored whether a single "mutual aid" condition MI(ι) could replace both SUD and
LCD as primitives, and whether CE could be relocated from the valuation layer to
the structural layer. Concluded: only a non-first-order (topological/covering)
condition has any hope, pointing toward the Grothendieck topology direction.

**`query_system_as_site.md`**
Developed the query system as a site with a σ-algebraic witnessing topology J.
Showed J is a legitimate Grothendieck topology iff SUD holds (needed for stability).
Explored whether CE ↔ charge presheaf being a sheaf for J. Tentative conclusion:
the CE irreducibility argument has a gap in the site-theoretic setting because J
uses second-order (σ-algebraic) witnessing not preserved by ultraproducts.

**`q4_finite_cofinite_sheaf_check.md`**
Answered Q4 explicitly: the finite-cofinite content ℓ IS a sheaf for J (Boolean
witnessing topology), because J is too coarse to detect CE failure at the Boolean
level. CE is invisible to Boolean-algebraic structure. Positive reformulation: CE
is a sheaf condition for the projective system of Stone spaces, not Boolean algebras
— which is exactly the Stone duality picture now being developed in
`stone-duality-extension`.

## Key conclusions absorbed into active documents

- CE is invisible at the Boolean level → confirmed and absorbed into
  `ce_irreducibility.md` and `step_a_step_b_analysis.md`
- CE is a sheaf/support condition at the Stone space level → now the central
  claim of the Step B analysis in `step_a_step_b_analysis.md`
- The correct site is the projective system of Stone spaces → this is exactly
  what `StoneDualityExtension.lean` formalizes
