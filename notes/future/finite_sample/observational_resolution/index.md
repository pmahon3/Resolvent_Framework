# Observational Resolution Dimension

*Seed note — 2026-05-02*

## Purpose

Paper III proves rate statements in the smooth dynamical regime, but the
appearance of the exponent $d$ should be understood more generally.  The rate
does not depend on topological dimension as such.  It depends on the scaling of
faithful observational refinement: how many distinguishable alternatives are
created per unit of scale, divergence, or refinement cost.

This note records the technical sketch behind that interpretation and marks the
scope of what should and should not be inserted into Paper III.

For the current note map and consolidation policy, see
`notes/README.md`.

Related notes:

- `notes/future/finite_sample/observational_resolution/theorem_spec.md` — formal theorem
  target;
- `notes/future/finite_sample/observational_resolution/failure_modes.md` — guardrails;
- `notes/future/finite_sample/observational_resolution/paper_iii_integration.md` — editorial
  boundary for Paper III;
- `notes/literature/finite_sample/observational_resolution/dimension_lit_review.md` —
  literature placement;
- `notes/literature/finite_sample/observational_resolution/claim_map.md` — safe/unsafe claim
  map.

## Basic principle

Let $(\mathcal G_k)$ be an increasing sequence of finite observable algebras,
or more generally finite observational partitions, and let $H(\mathcal G_k)$
measure the number of distinguishable alternatives at level $k$.  Examples:

- atom-count entropy: $H(\mathcal G_k)=\log|\mathrm{At}(\mathcal G_k)|$;
- Shannon entropy: $H_\mu(\mathcal G_k)$;
- collision entropy: $H_2(\mathcal G_k)=-\log\sum_{A\in\mathrm{At}(\mathcal G_k)}\mu(A)^2$;
- type entropy, spectral counting entropy, or Kolmogorov complexity in
  non-geometric settings.

A refinement sequence alone gives no dimension.  To obtain a dimension-like
exponent, one also needs a valuation of refinement

$$
\Lambda(k),
$$

which records the scale, cost, divergence, proof depth, description length, or
information distance associated with level $k$.

The general object is

$$
D_\Lambda
= \limsup_{k\to\infty}
\frac{H(\mathcal G_k)}{\Lambda(k)}.
$$

This is the framework-native form of "dimension as distinguishability growth
per unit valuation."

## Relation to the nonparametric rate

Suppose the target has $s$ units of regularity with respect to the valuation
scale.  At resolution $\varepsilon$, the approximation error is

$$
\mathrm{bias} \sim \varepsilon^s.
$$

If the number of distinguishable cells at scale $\varepsilon$ satisfies

$$
N(\varepsilon)\asymp \varepsilon^{-D},
$$

then the stochastic fluctuation scales as

$$
\mathrm{variance}^{1/2} \sim \sqrt{\frac{N(\varepsilon)}{n}}
\sim \sqrt{\frac{\varepsilon^{-D}}{n}}.
$$

Balancing bias and fluctuation gives

$$
\varepsilon^s \sim \sqrt{\frac{\varepsilon^{-D}}{n}},
\qquad
\varepsilon^{2s+D}\sim n^{-1},
$$

and therefore

$$
\mathrm{error}\sim n^{-s/(2s+D)}.
$$

For squared-risk loss the corresponding exponent is $n^{-2s/(2s+D)}$.

The exponent $D$ is therefore a resolution dimension, not necessarily a
topological dimension.

## Smooth and Cantor cases

In a smooth $d$-dimensional manifold regime, metric covering dimension,
Hausdorff dimension, Fisher/local Euclidean dimension, and topological
dimension all agree:

$$
D_T = D_H = D_{\mathrm{box}} = d.
$$

The classical rate writes $d$ because all relevant dimensions collapse to the
same number.  The rate uses the covering/resolution exponent, not topology
alone.

For the middle-thirds Cantor system, the topological dimension is zero, but the
honest cylinder refinement has

$$
|\mathrm{At}(\mathcal G_L)|=2^{L+1},
\qquad
\varepsilon_L=3^{-(L+1)}.
$$

Thus

$$
\frac{\log|\mathrm{At}(\mathcal G_L)|}{\log(1/\varepsilon_L)}
\longrightarrow
\frac{\log 2}{\log 3}.
$$

With the uniform Cantor measure, the atoms are balanced, so atom-count entropy,
Shannon entropy, and collision entropy all give the same exponent.  The rate
therefore has the same formal shape

$$
n^{-s/(2s+\log 2/\log 3)}.
$$

This is the precise sense in which the rate detects nontopological form: many
Cantor sets are topologically equivalent, but their refinement valuations and
scaling dimensions may differ.

## Collision entropy and Paper III

Paper III is especially close to the collision version.  For a finite algebra
$\mathcal G$,

$$
\operatorname{Coll}_\mu(\mathcal G)
=
(\mu\otimes\mu)\{(x,y): x \sim_{\mathcal G} y\}
=
\sum_{A\in\mathrm{At}(\mathcal G)}\mu(A)^2.
$$

The collision entropy is

$$
H_2(\mathcal G)=-\log\operatorname{Coll}_\mu(\mathcal G).
$$

Given a valuation $\Lambda(k)$, the observational collision dimension is

$$
D_{2,\Lambda}
=
\limsup_{k\to\infty}
\frac{-\log\operatorname{Coll}_\mu(\mathcal G_k)}{\Lambda(k)}.
$$

In balanced finite refinements this agrees with the atom-count exponent.  In
nonuniform settings it becomes measure-sensitive, which is often the right
object for empirical sampling.

## Important caution: continuous fibres

Exact collision probability is not a dimension by itself in continuous
injective settings.  If a delay map $\Phi_L$ is continuous and injective against
an atomless measure, then

$$
(\mu\otimes\mu)\{(x,y):\Phi_L(x)=\Phi_L(y)\}=0.
$$

To define a resolution dimension in such settings, one must use one of:

- a finite observable algebra $\mathcal G_k$;
- an $\varepsilon$-coarse-grained collision probability;
- covering numbers for an observational metric;
- entropy of a discretized observable law;
- an information divergence such as KL, Hellinger, Jensen-Shannon, or Fisher
  distance between observational laws.

Thus the general expression should be formulated at the level of valued
refinements, not as the exact collision probability of a continuous map.

## Information-geometric form

If the observation induces a family of laws $x\mapsto P_x$, choose a symmetric
information divergence $D_{\mathrm{sym}}$ and define an observational
pseudometric

$$
d_{\mathrm{obs}}(x,y)
=
\sqrt{D_{\mathrm{sym}}(P_x,P_y)}.
$$

Then

$$
D_{\mathrm{obs}}
=
\limsup_{\varepsilon\downarrow 0}
\frac{\log N(X,d_{\mathrm{obs}},\varepsilon)}{\log(1/\varepsilon)}.
$$

In smooth identifiable models this is locally the Fisher metric and recovers
the manifold/Fisher rank.  In fractal or singular models it recovers the
scaling dimension of the observable law.  If observations collapse states, it
recovers the dimension of the observable quotient rather than the hidden state
space.

This is the clean information-geometric version of the same principle:
dimension is the metric-entropy exponent of observable distinguishability.

## Valuation zoo

The valuation $\Lambda$ is the denominator map translating raw refinement into
the scale native to a mathematical domain.  Different fields instantiate it
differently:

| Realm | Refinement object | Numerator $H$ | Valuation $\Lambda$ |
|---|---|---|---|
| Cantor / self-similar geometry | cylinders | $\log 2^k$ | $\log 3^k$ |
| Smooth geometry | balls / charts | $\log N(\varepsilon)$ | $\log(1/\varepsilon)$ |
| Hyperbolic dynamics | orbit partitions | entropy $h$ | Lyapunov expansion $\lambda$ |
| Information geometry | observational laws $P_x$ | distinguishable laws | KL/Fisher/Hellinger scale |
| Logic | finite fragments / types | $\log|\mathrm{Types}_n|$ | formula depth / quantifier rank |
| Computation | prefixes / programs | Kolmogorov complexity | prefix length / description scale |
| Spectral theory | eigenmodes | counting function $N(\lambda)$ | energy scale $\lambda$ or heat time $t$ |
| Category theory | refinement category | enriched hom / cost | Lawvere distance |

The repeated pattern is

$$
\text{dimension}
\;=\;
\frac{\text{growth of distinguishable alternatives}}
{\text{growth of scale/cost/divergence}}.
$$

For systems with asymptotically multiplicative refinement,

$$
\varepsilon_k \sim e^{-ak},
$$

the valuation is $\Lambda(k)=ak$.  Then

$$
D_\Lambda
=
\frac{\limsup_k H(\mathcal G_k)/k}{a}.
$$

This is the general form behind familiar entropy-over-expansion formulas such
as $D \sim h/\lambda$ in dynamical and fractal settings.  The exponential
conversion is common but not universal.  Nonuniform, polynomial, multifractal,
or nonstationary refinements require the full limsup ratio
$H(\mathcal G_k)/\Lambda(k)$ rather than a single constant $a$.

## What belongs in Paper III

Do not reframe Paper III around $D_\Lambda$.  The paper's spine is already:

$$
\delta(\mathcal G)
\;\longrightarrow\;
\widehat{\delta}(\mathcal G,n)
\;\longrightarrow\;
\text{dynamical reconstruction witnesses}
\;\longrightarrow\;
\text{entropy witness}.
$$

The broader perspective should enter, if at all, as a short remark near the
Cantor example or the information-horizon remark:

- the exponent $d$ in $n^{-s/(2s+d)}$ is a resolution exponent;
- in smooth regimes it coincides with manifold dimension;
- in the Cantor example it is $\log 2/\log 3$ despite topological dimension
  zero;
- the general principle is scaling of faithful observational refinement, not
  topology alone.

Avoid introducing the full information-geometric machinery in Paper III unless
it supports a theorem there.

Candidate restrained remark:

> The exponent $d$ in the rate $n^{-s/(2s+d)}$ should be read here as a
> resolution exponent: the exponent governing the growth of distinguishable
> observable cells at scale $\varepsilon$.  In the smooth regime this coincides
> with the manifold dimension, because metric covering, local Euclidean
> dimension, and topological dimension agree.  In non-smooth examples they need
> not agree.  For the middle-thirds Cantor system, the honest cylinder
> refinement has $2^L$ cells at scale $3^{-L}$, giving the resolution exponent
> $\log 2/\log 3$ despite topological dimension zero.  Thus the rate is governed
> by the scaling of faithful observational refinement, not by topology alone.

## Future theorem shape

A later technical note could prove a general valued-refinement rate theorem:

Let $(\mathcal G_k)$ be an honest refining sequence and let $\Lambda(k)$ be an
admissible valuation.  Suppose:

1. $H_2(\mathcal G_k)/\Lambda(k)\to D_{2,\Lambda}$;
2. atoms of $\mathcal G_k$ are comparable to observational balls at scale
   $\varepsilon_k=e^{-\Lambda(k)}$;
3. the target class is $s$-Hölder with respect to the observational scale;
4. empirical collision/concentration estimates hold at the needed resolution.

Then the optimal resolution balance gives the rate

$$
n^{-s/(2s+D_{2,\Lambda})}
$$

or squared-risk rate

$$
n^{-2s/(2s+D_{2,\Lambda})}.
$$

This would make the smooth and Cantor cases instances of one
valued-refinement theorem.
