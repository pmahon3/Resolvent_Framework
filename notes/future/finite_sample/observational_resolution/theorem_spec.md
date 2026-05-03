# Theorem Spec: Valued Observational Refinement Rates

*Seed note - 2026-05-02*

## Purpose

This note isolates the first theorem target behind observational resolution
dimension.  The goal is not to prove a new dimension theory at once.  The goal
is to prove a clean rate theorem showing exactly what Paper III-style
finite-data reconstruction needs from a refinement sequence:

- entropy growth;
- a valuation of refinement;
- approximation regularity;
- empirical concentration.

If these four inputs are explicit, the usual rate

$$
n^{-s/(2s+D)}
$$

becomes a theorem about valued observable refinements rather than an informal
analogy with smooth or fractal geometry.

## Basic Objects

Let $(X,\mathcal A,\mu)$ be the observable probability space obtained from the
framework, and let

$$
\mathcal G_0\subseteq \mathcal G_1\subseteq\cdots\subseteq\mathcal A
$$

be an increasing sequence of finite observable algebras.

Let $H(\mathcal G_k)$ be a distinguishability entropy.  Candidate choices:

- atom-count entropy:

$$
H_0(\mathcal G_k)=\log |\operatorname{At}(\mathcal G_k)|;
$$

- Shannon entropy:

$$
H_1(\mathcal G_k)
=-\sum_{A\in\operatorname{At}(\mathcal G_k)}
\mu(A)\log\mu(A);
$$

- collision entropy:

$$
H_2(\mathcal G_k)
=-\log\sum_{A\in\operatorname{At}(\mathcal G_k)}\mu(A)^2.
$$

Let

$$
\Lambda(k)\to\infty
$$

be the valuation of refinement.  In geometric cases
$\Lambda(k)=\log(1/\varepsilon_k)$.  In dynamical cases it may be accumulated
expansion.  In logical or computational cases it may be proof depth,
description length, or resource cost.

Define the effective observational dimension

$$
D_\Lambda
=
\limsup_{k\to\infty}
\frac{H(\mathcal G_k)}{\Lambda(k)}.
$$

## Target Theorem: Generic Rate

Let $f$ be an observable target and let $f_k=\mathbb E[f\mid\mathcal G_k]$ or
another canonical $\mathcal G_k$-measurable approximation.

Assume:

1. Entropy growth.  There is $D<\infty$ such that

$$
H(\mathcal G_k)\le D\Lambda(k)+C
$$

for all sufficiently large $k$.

2. Approximation regularity.  There is $s>0$ such that

$$
\|f-f_k\|\le C e^{-s\Lambda(k)}.
$$

3. Empirical concentration.  From $n$ samples, the empirical estimate
$\widehat f_k$ satisfies

$$
\|\widehat f_k-f_k\|
\le
C\sqrt{\frac{e^{H(\mathcal G_k)}}{n}}
$$

with high probability, possibly up to logarithmic factors.

Then

$$
\|\widehat f_{k(n)}-f\|
\le
C'
n^{-s/(2s+D)}
$$

up to logarithmic or lower-order factors, for a choice of $k(n)$ satisfying

$$
e^{\Lambda(k(n))}
\asymp
n^{1/(2s+D)}.
$$

## Proof Skeleton

The error decomposes as

$$
\|\widehat f_k-f\|
\le
\|\widehat f_k-f_k\|+\|f_k-f\|.
$$

By assumptions,

$$
\|\widehat f_k-f\|
\lesssim
\sqrt{\frac{e^{D\Lambda(k)}}{n}}
+e^{-s\Lambda(k)}.
$$

Balance the two terms:

$$
e^{-s\Lambda}
\asymp
n^{-1/2}e^{D\Lambda/2}.
$$

Equivalently,

$$
e^{-(2s+D)\Lambda}
\asymp
n^{-1},
$$

so

$$
\Lambda
\asymp
\frac{\log n}{2s+D}.
$$

Substitution gives

$$
\operatorname{error}_n
\lesssim
n^{-s/(2s+D)}.
$$

This proof is deliberately elementary.  The mathematical work is in justifying
the three assumptions in framework-native cases.

## First Specialization: Balanced Finite Algebras

Assume $\mathcal G_k$ has $M_k$ atoms and all atoms have comparable mass:

$$
cM_k^{-1}\le \mu(A)\le C M_k^{-1}.
$$

Then

$$
H_0(\mathcal G_k)
\asymp
H_1(\mathcal G_k)
\asymp
H_2(\mathcal G_k)
\asymp
\log M_k.
$$

If

$$
\log M_k
\sim
D\Lambda(k),
$$

all three entropy choices give the same resolution dimension.

This covers the uniform middle-thirds Cantor example with

$$
M_k=2^{k+1},
\qquad
\Lambda(k)=\log 3^{k+1},
\qquad
D=\frac{\log 2}{\log 3}.
$$

## Second Specialization: Collision Version

For Paper III, the most native version uses

$$
\operatorname{Coll}_\mu(\mathcal G_k)
=
\sum_{A\in\operatorname{At}(\mathcal G_k)}\mu(A)^2
$$

and

$$
H_2(\mathcal G_k)
=-\log\operatorname{Coll}_\mu(\mathcal G_k).
$$

The target dimension is

$$
D_{2,\Lambda}
=
\limsup_k
\frac{-\log\operatorname{Coll}_\mu(\mathcal G_k)}
{\Lambda(k)}.
$$

The theorem should use $H_2$ only when the empirical fluctuation term really is
controlled by effective support/collision size.  In nonuniform settings,
$H_2$ can be much smaller than $H_0$ and may describe sampling difficulty better
than worst-case covering difficulty.

## Third Specialization: Observational Metric

If observations induce a pseudometric $d_{\mathrm{obs}}$, one may replace
finite algebras by covers:

$$
N_{\mathrm{obs}}(\varepsilon)
=
N(X,d_{\mathrm{obs}},\varepsilon).
$$

Then

$$
D_{\mathrm{obs}}
=
\limsup_{\varepsilon\downarrow0}
\frac{\log N_{\mathrm{obs}}(\varepsilon)}
{\log(1/\varepsilon)}.
$$

The same proof applies if the empirical approximation uses a cover at scale
$\varepsilon$ and satisfies

$$
\operatorname{fluctuation}
\lesssim
\sqrt{N_{\mathrm{obs}}(\varepsilon)/n}.
$$

This specialization is closest to metric entropy and information geometry.

## What Must Be Proved, Not Assumed Forever

The generic theorem is useful only if later notes prove the assumptions in
actual observational settings.

Needed lemmas:

- observable regularity implies
  $\|f-f_k\|\lesssim e^{-s\Lambda(k)}$;
- empirical occupation or collision estimates concentrate at the stated
  effective entropy scale;
- the chosen valuation $\Lambda$ is canonical or at least natural for the
  observation class under study;
- the finite algebras $\mathcal G_k$ are generated by admissible queries, not
  externally imposed partitions with no observational meaning.

## Relation to Paper III

Paper III already contains smooth finite-sample rates and collision/separation
diagnostics.  This theorem spec should not be inserted wholesale into Paper III.
At most, Paper III should include a remark that the smooth dimension $d$ is the
resolution exponent of the observable refinement in the smooth case.

The theorem above belongs either in a future Paper III extension or a separate
technical note once the assumptions can be verified in at least two nontrivial
examples:

- smooth manifold observations;
- uniform Cantor/self-similar observations;
- nonuniform or multifractal observations;
- symbolic/generating partition observations.

