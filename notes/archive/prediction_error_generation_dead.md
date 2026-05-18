# Seed Note: Prediction Error ↔ σ-Algebra Generation

## Phase: DEAD (self-deflated before audit, 2026-05-17)

## The claim

There exists a theorem connecting the prediction-error-optimal
embedding parameters (Casdagli's method) to a measure-theoretic
quantity characterizing σ-algebra generation (Rokhlin distance or
conditional variance).

Specifically: for a stationary ergodic process observed via h,
the out-of-sample prediction error of the optimal local predictor
at embedding dimension d and lag L converges (in some sense) to a
function of δ(L) = sup_S E[Var(1_S | O_L)].

## Why it might matter

Casdagli (1991/92) gives an empirical method for selecting
reconstruction parameters (embedding dimension, smoothing) via
prediction error. It works in practice but has:
- No proof of what it converges to
- No connection to information-theoretic completeness
- No characterization of optimality beyond bias-variance heuristic
- No explanation of WHY the prediction-error profile has its shape

A theorem connecting prediction error to δ(L) would:
- Explain Casdagli's empirical observations measure-theoretically
- Provide a theoretical stopping criterion (not just empirical)
- Unify the geometric (FNN) and statistical (prediction error)
  approaches under a single algebraic principle
- Give the "probability from relations" framework a genuine
  applied consequence that changes practice

## What the theorem might look like

Candidate statement: For a stationary ergodic process (X, B, μ, T)
with observable h ∈ L^∞, let O_L = σ(h, h∘T, ..., h∘T^L) and let
ε*(L) = inf_f E[(X_{L+1} - f(X_0,...,X_L))²] be the Bayes-optimal
prediction error at lag L. Then:

  ε*(L) → 0  iff  δ(L) → 0  (under appropriate conditions)

Or more precisely: ε*(L) = E[Var(X_{L+1} | O_L)] = the conditional
variance of the next step given the observable σ-algebra. This IS
a standard identity if "prediction error" means Bayes risk.

Wait — is this just the definition of conditional expectation?

## The potential triviality

The Bayes-optimal prediction error at lag L IS:

  ε*(L) = E[Var(h∘T^{L+1} | O_L)]

This is literally the conditional variance — a SPECIFIC instance
of E[Var(1_S | O_L)] with S replaced by a function. And δ(L) is
the sup over all S of E[Var(1_S | O_L)].

So: ε*(L) ≤ δ(L) · ||h||² (or similar bound).

And: δ(L) → 0 ⟹ ε*(L) → 0 (trivially — if the σ-algebra
generates, ALL conditional variances vanish).

The converse: ε*(L) → 0 ⟹ δ(L) → 0? NOT obvious. The prediction
error for ONE function h going to zero doesn't mean the σ-algebra
generates (you might just be predicting h well without capturing
everything).

But if ε*(L) → 0 for ALL bounded observables f (not just h), then
δ(L) → 0. That's tautological.

## The real question

The non-trivial theorem would be:

> Under what conditions does optimal prediction of h (one observable)
> imply generation of the full σ-algebra?

This connects to: when is h a GENERATING observable? (Takens/
reconstruction theory). If h generates (Paper II's reconstruction
condition), then ε*(L) → 0 for h implies O_L → B, which implies
δ(L) → 0 for everything.

So the theorem is: "If h is generating, then Casdagli's method
(prediction error → 0) correctly identifies reconstruction."

But that's just: "if reconstruction holds, prediction works" —
which is obvious. The interesting direction would be: "prediction
error → 0 implies reconstruction" — which is FALSE in general
(you could predict h without reconstructing the full state).

## Assessment: DEAD

Case 1 + 2: The connection is definitional (Bayes risk = conditional
variance), and the interesting direction (prediction → generation)
is just Paper II's reconstruction theorem restated. No new content.

Casdagli's method detects reconstruction iff h generates — which is
the reconstruction theorem in prediction-error language. Not a new
theorem; a restatement.

## Key terms for audit

- Bayes risk and conditional expectation
- Prediction error in ergodic theory
- Casdagli method convergence guarantees
- Conditional variance and σ-algebra generation
- Generating observables and prediction sufficiency
- Ornstein theory (d-bar distance, finitely determined)

## Source context

- Casdagli (1991/92) J. Roy. Statist. Soc. B 54, 303-328
- Paper II reconstruction theorem (O_h = B iff h generates)
- Paper III canned experiments (prediction error diagnostics)
- Rokhlin distance: standard in ergodic theory since 1967
