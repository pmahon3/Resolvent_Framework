# Paper III Integration Boundary: Observational Resolution Dimension

*Seed note - 2026-05-02*

## Purpose

This note fixes the editorial boundary between Paper III and the broader
observational resolution dimension programme.

The short version:

> Paper III may mention observational resolution dimension as an interpretation
> of the exponent $d$, but it should not absorb the full valued-refinement
> programme unless a new theorem is proved and inserted.

## Current Paper III Spine

Paper III is already organized around:

- finite-sample reconstruction;
- separation defect $\delta(\mathcal G)$;
- empirical collision probability;
- information horizon / occupancy limits;
- smooth nonparametric rates;
- algebraic and dynamical certification;
- fibre mixing as the major technical frontier.

This spine should remain intact.

## What Can Be Added Now

A restrained remark can be added near the information-horizon or Cantor
discussion:

> The exponent $d$ in these rates should be read as the exponent governing the
> growth of distinguishable observable cells at resolution $\varepsilon$.  In
> the smooth setting considered here this exponent agrees with manifold
> dimension.  In singular or fractal settings, the same bias-variance balance
> would involve the corresponding observable resolution exponent; for example,
> the standard Cantor refinement has exponent $\log 2/\log 3$ rather than
> topological dimension $0$.

This is an interpretive clarification, not a new theorem.

## What Should Not Be Added Yet

Do not add:

- a general definition of $D_\Lambda$ in the main theorem flow;
- a full valuation zoo;
- information geometry as a new structural layer;
- spectral/zeta analogies;
- algorithmic or logical dimensions;
- claims that Paper III proves the general valued-refinement theorem.

Those belong in future notes unless the paper is deliberately expanded.

## Threshold for Real Integration

The broader programme should enter Paper III only if we can prove and use a
theorem of the following form:

Given a finite observable refinement sequence $(\mathcal G_k)$, entropy
$H(\mathcal G_k)$, valuation $\Lambda(k)$, approximation regularity $s$, and
empirical concentration at entropy scale $H(\mathcal G_k)$, the reconstruction
error satisfies

$$
n^{-s/(2s+D)}
$$

where

$$
D=\limsup_k \frac{H(\mathcal G_k)}{\Lambda(k)}.
$$

Even then, integration should be limited to the cases actually proved.

## Recommended Placement

Best location:

- immediately after the existing Cantor/information-horizon discussion; or
- as a short paragraph in the effective-dimension/rate section.

Avoid placing it:

- in the abstract;
- in the introduction as a programme-level claim;
- inside a theorem statement unless the general theorem is proved;
- in the fibre-mixing section, where it would distract from the main technical
  obstruction.

## Editorial Policy

Paper III should say:

> The smooth dimension in the displayed rates is a resolution exponent.  Smooth
> geometry makes this exponent equal to manifold dimension.  Other observable
> refinement geometries may lead to other exponents.

Paper III should not say:

> We unify topological, fractal, information-geometric, algorithmic, and
> spectral dimensions.

That stronger unification is a programme note, not a Paper III result.

