# How much heterogeneity can hide a twist? (ε* on cycles of pair views)

reviewed: false. 2026-11-04. Scripts: `notes/open_questions/verification/eps_star_{triangle,cycle,committees}.py`.

## Puzzle
L friends in a ring, each neighbouring pair reports whether they agree on a yes/no question. Every pair's
report is fine. Suppose no single classical world fits the reports. How much would the population have to
differ from one pair-survey to the next before an ordinary classical story explains them anyway?

## Setting
Binary variables x_1..x_L on a cycle; context k observes (x_k, x_{k+1}); margins consistent.
d_k = P(x_k ≠ x_{k+1}). Heterogeneity null H_ε: some classical joint Q has every pair margin within total
variation ε of the observed table. ε*(P) = least such ε (an LP).

## Results
1. **Reduction** ⟦HAND, proved⟧: H_ε ⟺ each context sampled a classical world within TV ε of a common one.
2. **Lower bound, all L** ⟦HAND, proved⟧: ε* ≥ V/L, where V is the largest violation of the rim cycle
   inequalities Σ_{e∈F} d_e − Σ_{e∉F} d_e ≤ |F| − 1 (F odd; Barahona–Mahjoub). Proof: TV ε moves each d_e by
   ≤ ε; each such inequality has L coefficients ±1.
3. **Upper bound, L = 3** ⟦HAND, proved⟧: ε* ≤ V/3 by an explicit move (`ecology_contextuality_prior_art_DEEP.md`,
   theorem 2026-11-04). Hence for triangles ε* = V/3 and sup ε* = 1/3.
4. **Upper bound, general L** — numerically ε* = V/L for L = 3..6 (800 families each, error ≤ 2e-16), so
   sup ε* = 1/L. Hand status: OPEN. By duality ε* (with margins fixed) = sup over valid inequalities
   a·d ≤ β of (a·d − β)/‖a‖₁. The missing lemma: *no positive combination of the wheel's cycle inequalities
   (rim cycles, apex cycles that encode the margins, Fréchet bounds) has a larger violation-to-‖a‖₁ ratio
   than the best rim inequality.* For L = 3 this follows from the explicit move; for L ≥ 4 the apex cycles
   through rim paths are genuinely new constraints and the cancellation lemma is unproved.
5. **Hidden twists are fragile**: the 3×4×4 committees example has ε* = 1/27 (LP), against 1/3 for the
   visible parity twist on a triangle. Hidden twists rest on exact zeros; small heterogeneity dissolves them.

## Status and owners
The computation is likely owned in substance (distance to the marginal polytope; Berrett–Samworth 2022 test
statistic, metric unchecked; contextual fraction is a different measure). Not claimed. The use as a
heterogeneity budget against a biologically calibrated ε is the lens (see `ecology_test_design_sketch.md`).
