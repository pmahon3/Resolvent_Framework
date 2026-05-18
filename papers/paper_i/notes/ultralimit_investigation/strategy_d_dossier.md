# Strategy D Dossier

*Created 2026-05-02*

Parent notes:

- `row5_candidate.md`
- `stone_geometric_translation.md`
- `notes/unsorted/foundations/ce_nonderivability/index.md`
- `notes/README.md`

## Purpose

This dossier is the launchpad for Strategy D.  It consolidates the equivalent
forms of the problem, known reductions, necessary conditions, conceptual stakes,
and honest attack modes.

Strategy D is currently the concrete mathematical frontier of the
coherence/completion programme.  The problem has moved beyond ordinary Boolean
algebra manipulation and into set-theoretic topology / Radon measure theory.

## Core Question

### Boolean Form

Does there exist a Boolean algebra $B$ such that:

1. $B$ is non-$\sigma$-complete;
2. $B$ is non-atomic;
3. $B$ admits no $\sigma$-additive probability?

Equivalently:

> Does there exist a non-$\sigma$-complete non-atomic measure-free Boolean
> algebra?

Here $\sigma$-additivity on a non-$\sigma$-complete Boolean algebra is understood
only for disjoint countable families whose join exists in $B$.

### Stone Form

Let

$$
K=\operatorname{St}(B).
$$

Strategy D is equivalent to asking whether there exists a compact totally
disconnected Hausdorff space $K$ such that:

1. $K$ has no isolated points;
2. $K$ is not basically disconnected;
3. $K$ carries no strictly positive Borel/Radon probability measure.

Translation:

| Boolean condition | Stone condition |
|---|---|
| $B$ non-atomic | $K$ has no isolated points |
| $B$ non-$\sigma$-complete | $K$ not basically disconnected |
| $B$ measure-free | $K$ carries no strictly positive Radon probability |

### Support Form

For a Boolean algebra $B$, define

$$
\operatorname{Supp}_\sigma(B)
\subseteq
\operatorname{St}(B)
$$

as the part of the Stone space visible to $\sigma$-additive probabilities.

The resolved hierarchy says:

- atomic regime: $\operatorname{Supp}_\sigma(B)=\operatorname{St}(B)$;
- concrete join-preserving subalgebra regime:
  $\operatorname{Supp}_\sigma(B)=\operatorname{St}(B)$;
- minimal-join regime, such as $\mathcal P(\mathbb N)/\mathrm{fin}$:
  $\operatorname{Supp}_\sigma(B)=\operatorname{St}(B)$ because
  $\sigma$-additivity is vacuous;
- $\sigma$-complete non-atomic regime:
  negative by Nikodym/Vitali-Hahn-Saks;
- intermediate non-$\sigma$-complete non-atomic regime:
  open, reduced to Strategy D.

Strategy D asks whether the intermediate regime contains a genuinely
measure-free factor.

## Why This Is the Frontier

Earlier strategies collapsed:

- $\mathcal P(\mathbb N)/\mathrm{fin}$ is not a negative example; it has too few
  joins, so every finitely additive probability is $\sigma$-additive.
- Direct-product attempts using positive factors collapse unless one factor is
  genuinely measure-free.
- Indecomposable row-5 strategies are impossible because every Boolean algebra
  splits canonically over each element:

$$
B
\cong
(B{\upharpoonright}A)\times(B{\upharpoonright}A^c).
$$

Any failure of full $\sigma$-additive support is witnessed by a measure-free
direct-product factor.  Hence the open row reduces to the existence of such a
factor.

## Necessary Conditions for a Counterexample

Any Strategy D counterexample must be:

- non-$\sigma$-complete;
- non-atomic;
- measure-free, i.e. admit no $\sigma$-additive probability;
- uncountably generated;
- outside the scope of the subalgebra embedding lemma;
- not join-preservingly embeddable into a measured $\sigma$-algebra with
  full-support measure;
- not a minimal-join algebra where $\sigma$-additivity is vacuous;
- not $\sigma$-complete, where the Nikodym/Vitali-Hahn-Saks obstruction already
  controls the case.

Known positive class:

> Every countably generated non-atomic Boolean algebra carries a strictly
> positive $\sigma$-additive probability.

Reason: its Stone space is a compact metrizable zero-dimensional space without
isolated points, hence Cantor-like, and the clopen algebra embeds
join-preservingly into a standard Borel measure space with full-support measure.

## Conceptual Stakes

Strategy D asks whether the Stone completion of a rich distinction system can
be structurally inhospitable to honest probability.

If Strategy D has a **positive** answer:

> some coherent non-atomic Stone horizons cannot host sigma-additive probability
> at all.

In the coherence/completion language, this would show more than failure of
automatic closure.  Some completed horizons would be structurally measure-free:
probability is not merely underdetermined; it is unavailable.

If Strategy D has a **negative** answer:

> sigma-additive probability is broadly available in the non-sigma-complete
> non-atomic regime.

Then the philosophical weight shifts from existence to selection:

> the central problem is not whether honest probability can live on such
> horizons, but which admissibility/support condition selects the relevant
> probability or ensures descent to realised states.

Either outcome informs the central theme:

- positive Strategy D: probability-inhospitable coherent horizons exist;
- negative Strategy D: probability is broadly available, and CE-like conditions
  govern admissible support/descent rather than bare existence.

## Key structural clarification (2026-05-17)

On the **clopen** algebra of a Stone space, σ-additivity is vacuous by
compactness: a clopen algebra has no nontrivial countable disjoint families
whose join is also clopen (such a join would give a partition of a compact
space into infinitely many clopens, contradicting compactness).

The real Strategy D question is therefore about **Radon measures on the Stone
space itself** — i.e., measures on the Borel/Baire σ-algebra generated by
the clopens, not on the clopens alone.  A "strictly positive σ-additive
probability on $B$" is a strictly positive Radon probability on $\text{St}(B)$.

This clarification matters: the problem is squarely in set-theoretic topology
(existence of strictly positive Radon measures on zero-dimensional compact
spaces), not in finitary Boolean algebra.

## Existing Evidence

Evidence toward "no" / open row vacuous:

- the subalgebra embedding lemma covers all concrete non-$\sigma$-complete
  non-atomic examples currently in hand;
- interval algebras and Borel subalgebras of standard measure spaces are
  positive;
- countably generated non-atomic algebras are positive;
- $\mathcal P(\mathbb N)/\mathrm{fin}$ is positive vacuously;
- **Argyros (1983):** constructed (under CH) a compact space with no
  strictly positive Radon measure that is totally disconnected and has
  no isolated points — but it is basically disconnected (i.e., the
  corresponding Boolean algebra is σ-complete).  This shows the known
  negative examples live in the *wrong* row of the hierarchy.

Evidence toward set-theoretic sensitivity:

- weak distributivity and related strictly-positive-measure theorems apply well
  in $\sigma$-complete settings but not in the non-$\sigma$-complete regime;
- compact Radon-measure-free spaces are known to interact with additional
  axioms such as MA and diamond;
- no ZFC construction or ZFC obstruction is currently known for the exact
  totally disconnected, non-atomic, non-basically-disconnected target;
- **Plebanek (2024 survey):** most current secondary source on strictly
  positive measures on compact spaces.  Confirms that the question for
  non-basically-disconnected zero-dimensional spaces remains wide open.
  Key results surveyed: Kelley condition (1959), Gaifman (1964),
  Džamonja-Plebanek (2006) on chain conditions, Fremlin's problem list.
  No result directly addresses Strategy D's exact parameter regime.

Current assessment:

> Strategy D is likely independent of ZFC, but this is not proved.
> The structural clarification (Radon on Stone, not σ-additive on
> clopens) positions the problem precisely in the landscape surveyed
> by Plebanek (2024).  The nearest known constructions (Argyros, Kunen,
> Fedorchuk) all miss at least one of the required conditions.

## Attack Modes

### A. ZFC Construction

Construct a non-$\sigma$-complete non-atomic measure-free Boolean algebra in
ZFC.

Equivalent target:

> construct a compact totally disconnected no-isolated-points
> non-basically-disconnected Radon-measure-free space in ZFC.

Current likelihood: low.  Existing notes suggest ordinary Boolean-algebra
methods are exhausted.

### B. ZFC Nonexistence Theorem

Prove that every non-$\sigma$-complete non-atomic Boolean algebra carries a
$\sigma$-additive probability.

Current likelihood: also low.  Would require a theorem extending positive
measure existence beyond known concrete/join-preserving classes.

### C. Consistency Construction

Under diamond, CH-like principles, or another combinatorial principle, construct
the required Stone space / Boolean algebra.

Current likelihood: plausible.  Known compact L-space and measure-free compact
space constructions under diamond are the natural first models to inspect.

### D. Consistency Nonexistence

Under MA + not CH or related axioms, prove no such space exists in relevant
weights/classes.

Current likelihood: plausible but needs precise matching to Fremlin-style
Radon-measure results.

### E. Reduction to Known Independence Result

Show Strategy D is equivalent to, or follows from, a known independent problem
in set-theoretic topology.

Current likelihood: plausible and probably the most efficient first target.

## Immediate Literature Targets

Prioritize exact constructions and obstructions for compact spaces carrying no
strictly positive Radon measures.

Primary:

- Fremlin, *Measure Theory*, especially sections 531-534 and 391D.
- **Plebanek (2024), survey on strictly positive measures on compact spaces.**
  Most current secondary source.  Covers Kelley condition, chain conditions,
  and open problems.  Essential orientation for attack modes C-E.
- Kelley, "Measures on Boolean algebras" (1959).
- Horn and Tarski, "Measures in Boolean algebras."
- Džamonja-Plebanek, "Strictly Positive Measures on Boolean Algebras" (2006).
- **Argyros (1983), compact Radon-measure-free spaces under CH.**
  Nearest negative example — check exact conditions against Strategy D.
- Kunen compact L-space constructions.
- Fedorchuk compact space constructions.

Secondary:

- Talagrand / Maharam problem, mainly to rule out sigma-complete distractions.
- Gaifman algebras with no finitely additive measure, mainly as a stronger but
  different obstruction.
- Literature on compact Radon-measure-free spaces under diamond, MA, CH, or
  related axioms.
- Plebanek, algebraic characterizations of measure algebras (earlier papers).

## First Concrete Tasks

1. Verify the topological equivalence:

   $$
   B\text{ non-}\sigma\text{-complete}
   \quad\Longleftrightarrow\quad
   \operatorname{St}(B)\text{ not basically disconnected}
   $$

   with exact hypotheses.

2. Verify the measure-free translation:

   $$
   B\text{ admits no strictly positive }\sigma\text{-additive probability}
   $$

   versus

   $$
   \operatorname{St}(B)\text{ carries no strictly positive Radon probability}.
   $$

3. Determine whether Strategy D requires no $\sigma$-additive probability at
   all, or no strictly positive $\sigma$-additive probability, in each usage of
   the notes.  This distinction must be kept exact.

4. Read Fremlin 531-534 for MA/not-CH measure-existence results and extract the
   exact hypotheses.

5. Inspect Kunen/Fedorchuk examples and check:

   - compact?
   - Hausdorff?
   - totally disconnected / zero-dimensional?
   - no isolated points?
   - not basically disconnected?
   - no strictly positive Radon measure?

6. Build a table of candidate spaces and which Strategy D conditions they meet.

## Known Terminology Risks

- "Measure-free" must be defined precisely:
  no $\sigma$-additive probability at all, or no strictly positive
  $\sigma$-additive probability?

- "Radon-measure-free" in topology may mean no nonzero Radon measure, no
  strictly positive Radon measure, or no Radon measure with full support,
  depending on source.  Verify source usage.

- "Non-atomic Boolean algebra" means no atoms in $B$; Stone-theoretically, no
  isolated points.

- "Non-atomic measure" is a different phrase and should not be confused with
  non-atomic Boolean algebra.

- "Basically disconnected" must be tied exactly to sigma-completeness of
  clopens; verify whether countable completeness or sigma-completeness is the
  exact dual condition.

## Status

Strategy D is the current front-runner for concrete mathematical work.

The next work is not another conceptual note.  It is a targeted
set-theoretic-topology investigation:

- exact definitions;
- exact equivalences;
- exact known consistency results;
- candidate examples under additional axioms.
