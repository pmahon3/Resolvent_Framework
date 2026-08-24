# Andersen–Jessen: the citation, and what still needs a human check

Written 2026-08-22 as the deliverable of task C1. Purpose: the claim that
`stone_observational_extension` was FALSE under its original hypothesis rests
on the Andersen–Jessen counterexample, and that rested in turn on my reading of
a single compressed exposition in which I also found a probable gap. This is
the second-source check.

## The classical statement is confirmed

Two independent sources agree, and they agree on the distinction that matters.

**Washington, Stat 521 handout, *Product Measures and Extension Theorems*:**

> existence of consistent marginal distributions alone does not imply existence
> of a probability measure on the product measurable space in general.
> Apparently the first counterexample was given by Andersen and Jessen (1948a).

citing **Dudley, *Real Analysis and Probability* (2002), p. 256 and §12.1
problem 2, p. 448** — a better reference than Border for the paper, being a
standard textbook rather than lecture notes.

**The distinction to state carefully.** The very next section of that handout is
"Existence of infinite product probability measures without topology", and it
delivers exactly that: *product* measures over arbitrary probability spaces
exist with no topological hypothesis (Łomnicki–Ulam 1934, von Neumann 1935/1950,
Kakutani 1943, Jessen 1939, Andersen–Jessen 1946). So the failure is NOT that
infinite products are delicate. It is specific to **consistent families that are
not products** — which is precisely the projective setting a query system is.

Get this wrong in the prose and a referee will say infinite product measures are
fine without topology, and be right.

## What this settles, and what it does not

Settled: consistent σ-additive marginals plus no regularity does not imply a
limit measure. That is the mathematical content the paper needs, and it is
classical and citable.

NOT settled by the citation, and still needing a human pass:

1. **The `EvalSurjective` instantiation.** Our theorem carries a hypothesis the
   classical statement never mentions: every `eval_i : Ω → Outcome_i` is
   surjective. In Border's presentation of A–J the bonding maps are projections
   and `Ω = ∏ₖ Xₖ`, so `eval_n` is a projection onto an initial segment and is
   surjective provided each `Xₖ` is nonempty (they are — thick sets have outer
   measure 1). That is the step I verified by hand and it is the one worth a
   second pair of eyes, because it is the only hypothesis that could have
   rescued the original statement.

2. **The gap in Border's Proposition 13.** He asserts
   `λ*(E ∩ Mₖ) = λ(E) = λ*(E ∩ Mₖᶜ)` for every `k`, proving the second half and
   disposing of the first with "a similar argument interchanging the roles of
   `Bₖ` and `Cₖ`". For `k = 0` that works, since `A = B₀ ⊔ C₀` and
   `M₀ᶜ = V + C₀` exactly. For `k > 0` it does not obviously work: `Bₖ` and `Cₖ`
   both omit everything with `|n| < k`, so `V + Bₖ` and `V + Cₖ` do not cover
   `ℝ` and `Mₖᶜ` is strictly larger than `V + Cₖ`.

   This does not threaten the classical result — it is one line of one
   expository document. Our own formalization sidesteps it entirely: see
   `staging/AndersenJessen.lean`, which builds the thick tower from FINITENESS
   rather than parity (`V_add_finite_measurable_null`), giving thickness at every
   `k` with no analogue of that step.

## Recommended citation for the paper

Sparre Andersen, E. and Jessen, B. (1948), *On the introduction of measures in
infinite product sets*. Secondary: Dudley, *Real Analysis and Probability*
(2002), p. 256, and §12.1 problem 2, p. 448. Halmos, *Measure Theory*,
pp. 68–70, for the thick-set machinery.

Do not cite Border for the mathematics; cite it, if at all, only as an
exposition, and not for Proposition 13 at general `k`.
