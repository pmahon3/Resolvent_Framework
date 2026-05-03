# Failure Modes: Observational Resolution Dimension

*Seed note - 2026-05-02*

## Purpose

This note records the main ways the observational resolution dimension programme
can go wrong.  These are not objections to the programme; they are constraints
that should be explicit before theorem-writing begins.

## 1. Exact Collisions Vanish in Continuous Atomless Settings

For a continuous injective observation map $\Phi:X\to Y$ and an atomless
measure $\mu$,

$$
(\mu\otimes\mu)\{(x,y):\Phi(x)=\Phi(y)\}=0.
$$

Thus exact collision probability is not a dimension in such settings.  It is a
finite-resolution or coarse-grained diagnostic.

Correct replacements:

- finite observable algebras $\mathcal G_k$;
- $\varepsilon$-coarse collisions;
- covering numbers in an observational metric;
- discretized entropy of the observable law;
- divergence balls between observational laws.

Guardrail:

> Never define the general dimension as exact collision probability of a
> continuous map.  Define it through finite/coarse valued refinements.

## 2. Refinement Alone Does Not Define Dimension

A sequence

$$
\mathcal G_0\subseteq\mathcal G_1\subseteq\cdots
$$

has no dimension by itself.  It needs a valuation

$$
\Lambda(k)
$$

that says what level $k$ costs or what scale it represents.

Examples:

- Cantor cylinders: $\Lambda(k)=\log 3^k$;
- smooth covers: $\Lambda(\varepsilon)=\log(1/\varepsilon)$;
- hyperbolic dynamics: $\Lambda(t)\sim \lambda t$;
- logic: formula depth or quantifier rank;
- computation: description length or resource bound.

Guardrail:

> Any claim of dimension must specify both numerator and denominator.

## 3. Topology Does Not Determine the Rate Exponent

Topological dimension may agree with the rate exponent in smooth manifolds, but
that agreement is not structural.

Examples:

- Smooth $d$-manifold:

$$
D_T=D_H=D_{\mathrm{box}}=d
$$

under ordinary regularity.

- Middle-thirds Cantor set:

$$
D_T=0,
\qquad
D_H=D_{\mathrm{box}}=\frac{\log 2}{\log 3}.
$$

The rate sees the scaling/refinement exponent, not topology as such.

Guardrail:

> Do not write that the theory uses topological dimension except in cases where
> topology and metric scaling are known to coincide.

## 4. Different Entropies Can Give Different Dimensions

For balanced refinements,

$$
H_0\asymp H_1\asymp H_2.
$$

For nonuniform measures these can differ sharply:

- atom-count entropy $H_0$ is worst-case and support-sensitive;
- Shannon entropy $H_1$ is typical-code-length sensitive;
- collision entropy $H_2$ is sample/collision sensitive and emphasizes heavy
  atoms;
- higher or lower Renyi dimensions may detect different multifractal strata.

Guardrail:

> State which entropy is being used and why that entropy matches the empirical
> or reconstruction task.

## 5. Empirical Collision May Measure Sampling Resolution

With finite data, observed collisions can reflect the sample size and binning
scheme rather than the underlying observable geometry.

Risks:

- bins too fine: most empirical cells are empty or singleton;
- bins too coarse: geometry is washed out;
- adaptive bins: entropy estimates may inherit selection bias;
- dependent data: naive occupancy concentration can fail.

Guardrail:

> Empirical collision estimates require a declared resolution schedule and a
> concentration theorem appropriate to the sampling process.

## 6. Smooth Fisher Geometry Requires Identifiability

If an observation induces a family of laws $x\mapsto P_x$, information geometry
is useful only after quotienting out observational equivalence.

Failure modes:

- nonidentifiability: $P_x=P_y$ for distinct states;
- singular models: Fisher rank drops or changes;
- boundary phenomena: local quadratic approximations fail;
- misspecification: the empirical law is not in the model family.

Guardrail:

> Information geometry should be applied to the observable quotient or factor,
> not blindly to the hidden state space.

## 7. Local and Global Dimensions May Disagree

In multifractal or nonuniform systems, there may be no single useful exponent.

Possible dimensions:

- global upper box/capacity dimension;
- Hausdorff dimension of full-measure sets;
- local pointwise dimension;
- Renyi-$q$ dimensions;
- essential supremum/infimum of local exponents;
- task-specific effective dimension.

Guardrail:

> A global $D$ theorem needs uniformity assumptions.  Without uniformity, expect
> local rates or multifractal spectra.

## 8. Valuation May Not Be Intrinsic

The deepest conceptual risk is that $\Lambda$ is externally chosen rather than
forced by the object or observation system.

Examples:

- Cantor construction supplies $\Lambda(k)=k\log 3$ by construction.
- Smooth metric observations supply $\log(1/\varepsilon)$ from the metric.
- Hyperbolic dynamics may supply $\lambda t$ from expansion.
- Zeta/logical examples may not supply a unique valuation without a declared
  query horizon or naturality class.

Guardrail:

> When $\Lambda$ is not canonical, say so.  The theorem is then conditional on a
> chosen valuation, not a derivation of one.

## 9. Observable Dimension May Be Quotient Dimension

Observation can collapse states.  The relevant dimension is then the dimension
of the observable factor, not the hidden space.

If

$$
x\sim y
\quad\Longleftrightarrow\quad
\text{all admissible observations agree on }x,y,
$$

then the correct geometric object is often

$$
X/{\sim}.
$$

Guardrail:

> Rates should be stated for the observable factor unless faithfulness of the
> observation map has been proved.

## 10. Paper III Scope Creep

Paper III already has a theorem spine: finite-sample reconstruction,
separation defect, collision diagnostics, smooth rates, and fibre mixing.  The
observational dimension programme can clarify the exponent but should not
replace the paper's main structure.

Guardrail:

> Until there is a proved valued-refinement theorem with verified assumptions,
> Paper III gets only a remark.  The full programme remains in future notes.

## Checklist Before Proving Anything

For each proposed theorem, answer:

- What are the refinements $\mathcal G_k$?
- What entropy $H$ is used?
- What is the valuation $\Lambda$?
- Is $\Lambda$ assumed, observed, or derived?
- What regularity gives the bias term?
- What empirical theorem gives the fluctuation term?
- Is the result global, local, or multifractal?
- Is the theorem about the hidden state space or the observable quotient?
- Does collision mean exact, finite-algebra, or coarse-grained collision?
- Which existing literature already proves the closest version?

