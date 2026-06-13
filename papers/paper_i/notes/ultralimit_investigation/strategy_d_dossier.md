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
- **Plebanek (2024 survey):** survey on $P(K)$ spaces, not on
  strictly positive measure existence.  Covers Kelley intersection
  numbers, calibers, Corson compacta, tightness, Grothendieck.
  Does not discuss Argyros (1983) or the measure-free BA problem.
  No result directly addresses Strategy D's parameter regime.
  The relevant Plebanek work for Strategy D is Džamonja-Plebanek
  (2008), JSL 73 — already read.

New evidence (2026-05-20):

- **Džamonja-Plebanek (2008), Theorem 3.1 / Todorčević (2000),
  Theorem 8.4:** The subalgebra 𝔄 of P(T)/fin generated by
  {T_a : a ∈ A} is ccc, not σ-centred, and measure-free (ZFC).
  However, **𝔄 has atoms**: the generators form a chain (A is
  totally ordered under ⊆\*, and a ⊆\* b ⟹ T_b ⊆\* T_a), making
  𝔄 an interval algebra. Immediate-successor pairs a ≺ a' in A
  produce atoms [T_a] \ [T_{a'}]. **Not a Strategy D counterexample.**
  Still significant: first ZFC measure-free example outside the
  σ-complete regime.

Fremlin §531–§539 systematic read (2026-05-21):

- **§531–§532 (Maharam types, completion regularity):** Machinery for
  classifying Radon measures by Maharam type.  Relevant background but
  no direct Strategy D results.  Key fact: Maharam-type-homogeneous
  measures on Stone spaces are completion regular (532D).

- **§533H (MA consequence):** Under $\operatorname{cov}\mathcal{N}_{\omega_1}
  > \omega_1$ (follows from MA), every Radon measure on a perfectly normal
  compact Hausdorff space is uniformly regular.  Strategy D relevance:
  indirect — shows additional axioms constrain which measures can
  exist, not whether they exist at all.

- **§534 (Hausdorff measures, strong measure zero):** Metric constructions.
  Not relevant to Strategy D (no metric structure on Stone spaces).

- **§539 (Maharam submeasures — the critical section):**
  All results address the **Dedekind σ-complete** regime, not Strategy D's
  non-σ-complete target.  But the structural findings transfer as evidence
  for axiom-sensitivity:

  - **539N (Balcar-Jech-Pazák 2005, Veličković 2005):** Under
    Todorčević's p-ideal dichotomy (PID), every Dedekind σ-complete
    ccc weakly (σ,∞)-distributive BA is a Maharam algebra (hence
    carries a strictly positive Maharam submeasure).  Needs PID.
  - **539P (Souslin algebras):** Under ◇, Souslin algebras are Dedekind
    complete, ccc, weakly (σ,∞)-distributive, but carry only the zero
    Maharam submeasure — consistent counterexamples to 539N without
    PID.
  - **539Q(g) (Farah-Veličković 2006):** Under $2^\kappa = \kappa^+$
    and $\square_\kappa$, there exists a Dedekind complete BA where every
    order-closed subalgebra of cardinal $\le\kappa$ is measurable but
    the whole algebra is not.  Reflection failure: local measurability
    does not propagate globally.
  - **Talagrand (2008), per §394/§539 Notes:** Solved the Control
    Measure Problem — not every Maharam algebra is measurable.
    Even having a strictly positive submeasure does not guarantee a
    strictly positive measure.
  - **§539 Notes synthesis:** "A Dedekind complete ccc weakly
    (σ,∞)-distributive BA is 'nearly' a Maharam algebra."  Extra
    conditions (e.g., σ-finite chain condition) or extra axioms (PID)
    push it to measurable.

  **Transfer to Strategy D:** Even in the cleaner σ-complete regime,
  measurability is axiom-sensitive (PID vs ◇ vs □).  Strategy D's
  non-σ-complete regime has *less* structure to work with, making
  ZFC resolution even less likely.  This is the strongest indirect
  evidence that Strategy D is ZFC-independent.

Argyros (1983) — direct reading (2026-05-21):

- **Construction:** $X_n = \beta Y_n$ where $Y_n$ is a subspace of
  $\{0,1\}^\omega$ with topology generated by product clopens and
  branch-determined sets $V_\Sigma$.  The space $X_n$ is compact
  Hausdorff and zero-dimensional (basis of clopen sets preserved
  under Stone-Čech compactification of a zero-dimensional completely
  regular space).
- **Theorem 1.9:** For each $n \ge 2$, $X_n$ has property (*),
  hence ccc, and does not carry a strictly positive measure.
  Under MA, $X_n$ fails $K_{n+1}(2^\omega)$.
- **σ-completeness status: VERIFIED — σ-complete (extremally disconnected).**
  Comfort-Negrepontis (1982), Theorem 6.25 states the Argyros
  example explicitly as "an extremally disconnected, compact Hausdorff
  space."  The construction works in two steps: (1) build a completely
  regular space $X$ with property (*) but not (**); (2) pass to
  the Gleason space $G(X)$, which is extremally disconnected by
  definition and inherits (*) / ¬(**) by Lemma 6.2(c),(d).
  The 1983 Pacific J. Math. paper constructs $X_n = \beta Y_n$
  (step 1); the "Argyros example" in the literature is $G(X_n)$
  (step 2).  **Argyros's example is σ-complete — wrong row.**
- **Isolated points:** $Y_n$'s basic opens $V_\Sigma$ are products
  with infinitely many unconstrained coordinates
  ($\{0,1\}^{\omega\setminus\bigcup\Sigma}$), so no singleton is
  open in $Y_n$ — $Y_n$ has no isolated points.  Free ultrafilters
  in $\beta Y_n \setminus Y_n$ are not isolated either.  So $X_n$
  has no isolated points.
- **Axiom dependence:** Construction is ZFC (no additional axioms
  needed for the existence of the tree and the compactification).
  The failure of $K_{n+1}(2^\omega)$ uses MA.
- **Pre-Gleason observation (unverified — not resolved by literature):**
  Both Argyros and Gaifman construct a compact space $X$ with (*)
  and ¬(**), then pass to the Gleason space $G(X)$ to get extremal
  disconnectedness (Comfort-Negrepontis Lemma 6.2).  The pre-Gleason
  space $\beta Y_n$ already satisfies (*), ¬(**), is compact,
  zero-dimensional, and has no isolated points.  Its clopen algebra's
  σ-completeness is not explicitly stated in either Argyros paper.
  Whether $\beta Y_n$ is basically disconnected requires direct
  analysis — non-discreteness of $Y_n$ does not settle this (non-discrete
  spaces can be basically disconnected).
  **If $\beta Y_n$ is NOT basically disconnected, it would satisfy
  all three Strategy D conditions.**  However, the prior probability
  is low: experts in this area (Argyros, Comfort, Negrepontis,
  Plebanek, Fremlin) have worked on this neighborhood for 40+ years.
  **Plebanek (2024) does not discuss this question** — it surveys
  $P(K)$ spaces, not the measure-free BA problem.  Džamonja-Plebanek
  (2008) also does not address $\beta Y_n$ specifically.
  Resolution requires direct topological analysis of $Y_n$'s cozero
  sets, or locating a remark in Comfort-Negrepontis or Fremlin that
  $\beta Y_n$ is (or is not) basically disconnected.

  **UPDATE 2026-06-12 (GJ-grounded — supersedes the "requires direct analysis"
  framing above, and corrects one claim):** Gillman–Jerison gives the lever (1H,
  6M.1, 6W — see "Next concrete steps" and `argyros_sigma_completeness_handoff.md`),
  reducing the question to two precise sub-questions (the limit-branch witness; the
  strong-zero-dim sub-lemma). NOTE the bare "$\beta Y_n$ … zero-dimensional" above
  is imprecise: Argyros gives only $\operatorname{ind}=0$ (a clopen base); strong
  zero-dimensionality ($\dim=0$, needed for $\beta Y_n$ zero-dim) is an OPEN
  sub-lemma. The witness direction routes around it by working in
  $\operatorname{Clop}(Y_n)$ directly.

Current assessment (revised 2026-05-21):

> Strategy D is likely independent of ZFC.  The systematic read of
> Fremlin §531–§539 and direct reading of Argyros (1983) confirm:
>
> 1. Every known measure-free construction that is non-atomic
>    (Argyros 1983, Souslin algebras under ◇) is σ-complete.
> 2. The only known ZFC measure-free construction outside the
>    σ-complete regime (Todorčević/D-P 2000/2008) has atoms.
> 3. Even in the σ-complete regime, measurability is axiom-sensitive
>    (539N vs 539P: PID gives positive, ◇ gives negative).
> 4. No ZFC atomless non-σ-complete measure-free example is known.
> 5. No ZFC proof that such examples cannot exist is known.
>
> The problem sits at the intersection of two independent
> difficulties: removing atoms (moving beyond Todorčević/D-P) and
> removing σ-completeness (moving beyond Argyros/Souslin).  Neither
> has been achieved.

## Near-Miss Table

Known constructions checked against Strategy D's three conditions:
non-σ-complete, non-atomic, measure-free.

| Construction | Non-σ-complete? | Non-atomic? | Measure-free? | Axiom | Why not Strategy D |
|---|---|---|---|---|---|
| Argyros (1983) $G(X_n)$ | **NO** (extremally disconn., per C-N 6.25) | Yes | Yes (no s.p. measure) | ZFC | σ-complete (wrong row) — verified |
| Souslin algebras (539P) | **NO** (Dedekind complete) | Yes | Yes (zero submeasure) | ◇ | σ-complete (wrong row) |
| Gaifman (1964) | **NO** (σ-complete) | Yes | Yes (no f.a. measure!) | ZFC | σ-complete; even stronger: no finitely additive measure |
| Todorčević/D-P (2000/2008) 𝔄 | Yes | **NO** (has atoms) | Yes (measure-free, ccc) | ZFC | Has atoms (interval algebra) |
| $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ | Yes | Yes | **NO** (σ-add. vacuous) | ZFC | Too few joins; every f.a. prob. is σ-additive |
| Farah-Veličković (539Q(g)) | **NO** (Dedekind complete) | ? | Yes (not measurable) | $2^\kappa=\kappa^+$, $\square_\kappa$ | σ-complete (wrong row) |
| Countably gen. non-atomic BA | Yes | Yes | **NO** (carries s.p. σ-add. prob.) | ZFC | Stone space metrizable → embeds into measured σ-algebra |
| Talagrand (2008) | **NO** (Maharam algebra, σ-complete) | Yes | Partial (submeasure but no measure) | ZFC | σ-complete; submeasure ≠ measure but still wrong row |
| Kunen (1981) L-space | ? (not addressed) | Yes (no isolated pts) | **NO** (carries s.p. Baire measure) | CH | Has a strictly positive measure — opposite side |
| Fedorchuk (1977) $D(X)$ | ? (not addressed) | Yes (no isolated pts) | ? (not addressed) | PH (cons. w/ ZFC) | Paper is about sequential compactness; σ-completeness and measure-freeness both unresolved |

**Pattern:** Every known non-atomic measure-free example is
σ-complete.  Every known non-σ-complete measure-free example has
atoms.  The two conditions have never been achieved simultaneously.

## Attack Modes

### A. ZFC Construction

Construct a non-$\sigma$-complete non-atomic measure-free Boolean algebra in
ZFC.

Equivalent target:

> construct a compact totally disconnected no-isolated-points
> non-basically-disconnected Radon-measure-free space in ZFC.

Current likelihood: **very low**.  The near-miss table shows that removing
atoms from the Todorčević/D-P construction (the only non-σ-complete
measure-free example) while preserving measure-freeness has no known
technique.  And the Fremlin §539 evidence shows that even in the
σ-complete regime, ZFC alone cannot resolve measurability questions.

### B. ZFC Nonexistence Theorem

Prove that every non-$\sigma$-complete non-atomic Boolean algebra carries a
$\sigma$-additive probability.

Current likelihood: **very low**.  Would require a theorem extending positive
measure existence beyond known concrete/join-preserving classes.  The
§539 evidence (axiom-sensitivity even for σ-complete BAs) suggests no
such ZFC theorem exists.

### C. Consistency Construction

Under diamond, CH-like principles, or another combinatorial principle, construct
the required Stone space / Boolean algebra.

Current likelihood: **plausible, probably the best first target**.  The
template exists: Souslin algebras (539P) under ◇ give σ-complete
non-atomic measure-free BAs.  A variant construction that produces a
non-σ-complete quotient or subalgebra while preserving measure-freeness
and atomlessness is the natural approach.  Argyros's tree-based
technique (ZFC, but producing σ-complete spaces) might adapt.

### D. Consistency Nonexistence

Under MA + not CH or related axioms, prove no such space exists in relevant
weights/classes.

Current likelihood: **plausible**.  539N (PID → measurability for
σ-complete ccc weakly distributive BAs) is the model result.  An
analogue for non-σ-complete BAs under PID or MA would give a
consistency nonexistence result.  Džamonja-Plebanek (2008) Cor. 2.8
and 2.11 give MA+¬CH results for σ-centred and small-weight BAs.

### E. Reduction to Known Independence Result

Show Strategy D is equivalent to, or follows from, a known independent problem
in set-theoretic topology.

Current likelihood: **plausible and probably the most efficient path**.
The §539 landscape (PID vs ◇ for Maharam algebras) and the Souslin
hypothesis are natural candidates for reduction targets.

## Literature Targets

### Read

- **Fremlin, *Measure Theory*, §531–§534, §538–§539.** READ (2026-05-21).
  §531–§532: Maharam types, completion regularity.  §533: MA consequences
  for Radon measures.  §534: Hausdorff measures (not relevant).
  §539: Maharam submeasures — the critical section.  BJP/Veličković (539N),
  Souslin algebras (539P), Farah-Veličković (539Q(g)), Talagrand.
  All σ-complete regime.  Axiom-sensitivity confirmed.
- **Džamonja-Plebanek, "Strictly Positive Measures on Boolean Algebras,"
  JSL 73(4), 2008.** READ (2026-05-20).  Todorčević example (Theorem 3.1,
  measure-free but has atoms), MA+¬CH results (Cor. 2.8, 2.11), Strassen
  amalgamation technique (Theorem 2.3).
- **Argyros (1983), "On compact spaces without strictly positive measure,"
  Pacific J. Math. 105(2).** READ (2026-05-21).  Constructs $X_n = \beta Y_n$,
  compact ccc zero-dimensional, no strictly positive measure.  σ-complete
  (extremally disconnected).  Near-miss: wrong row.
- **Comfort-Negrepontis (1982), *Chain Conditions in Topology*, CUP,
  Chapter 6: "Strictly Positive Measures."** READ (2026-05-21).
  Theorem 6.25 confirms Argyros example is the Gleason space $G(X_n)$
  (extremally disconnected).  Theorem 6.23 is Gaifman's example
  (also extremally disconnected).  Theorem 6.4 = Kelley's theorem.
  Corollary 6.17 = s.p. measure ⟹ $K_{\alpha,n}$ for all $\alpha$
  with $\text{cf}(\alpha)>\omega$, all $n$.
- **Gillman–Jerison, *Rings of Continuous Functions*, §1H, §6M, §6W.**
  READ (2026-06-12; page scans in
  `notes/literature_review/literature/gillman_jerison_pages/`). 1H: basically
  disconnected ⟺ every cozero-set has open closure. 6M.1: $\beta X$ b.d. ⟺ $X$
  b.d. 6W: in $\beta\mathbb N\setminus\mathbb N$ the closure of a strictly
  increasing sequence of clopens is never open (the non-b.d. witness template).
  This is the lever for the step-1 reduction (see "Next concrete steps").
- **Argyros (1982), "Boolean algebras without free families,"
  Algebra Universalis 14.** READ (2026-05-21).  Theorem A: no free
  family of cardinality $\lambda$ under filter conditions.
  Theorem B (GCH): constructs $B_\alpha$ with $\beta^+$-chain
  condition and no free family.  §2 constructs examples under GCH
  via Gleason spaces of tree-based spaces.  Corollary 2.4 = the
  Argyros example (Ω = Gleason space, extremally disconnected).
- **Plebanek (2024), "A survey on topological properties of $P(K)$
  spaces," arXiv:2312.14755v3.** READ (2026-05-21).  Survey on
  $P(K)$ = space of Radon probability measures with weak*
  topology.  Covers Kelley intersection numbers (§2.5), calibers
  (§3.2), Corson compacta (§5), tightness (§7), Grothendieck/Efimov
  (§9).  **Does NOT discuss Argyros (1983) or the strictly positive
  measure existence problem directly.**  Argyros cited only as [3]
  (the 1988 Corson compacta paper).  No mention of pre-Gleason
  spaces, basically disconnected spaces, or the Gleason construction.
  Džamonja-Plebanek [30] = the 2008 JSL paper (already read) is
  the relevant Plebanek paper for Strategy D.  This survey does not
  resolve the pre-Gleason question.
- **Kunen (1981), "A compact L-space under CH," Topology and its
  Applications 12(3), 283–287.** READ (2026-05-21).  Under CH,
  constructs a compact 0-dimensional HL non-separable space $X$
  carrying a strictly positive Baire probability measure $\mu$
  (Lemma 1.3(ii): $\mu(K) > 0$ for all non-empty clopen $K$).
  **Not a Strategy D candidate** — fails condition (3) outright.
  The space has a s.p. measure; it is on the opposite side of
  the measure question.  Measure algebra isomorphic to the usual
  measure algebra of $2^{\omega_1}$ (Maharam's theorem, p. 287).
- **Fedorchuk (1977), "A compact space having the cardinality of
  the continuum with no convergent sequences," Math. Proc. Camb.
  Phil. Soc. 81(2), 177–181.** READ (2026-05-21).  Under
  Con(ZFC + PH), constructs $D(X)$: compact, cardinality $\mathfrak{c}$,
  zero-dimensional, no isolated points, no convergent sequences.
  **Strategy D conditions unresolved by this paper.**
  σ-completeness of $\operatorname{Clop}(D(X))$ not addressed
  (the no-convergent-sequences property is consistent with
  extremal disconnectedness, cf. Frolík).  Measure-freeness
  not addressed — the paper concerns sequential compactness,
  not measures.  Would require secondary literature to determine
  whether $D(X)$ carries a strictly positive Radon measure.

### Still to read

- Kelley, "Measures on Boolean algebras" (1959).
- Horn and Tarski, "Measures in Boolean algebras" (1948).
- Fremlin §391D (Kelley's theorem and its consequences).

### Resolved / deprioritized

- Talagrand / Maharam problem: resolved by Talagrand (2008).  Not every
  Maharam algebra is measurable.  σ-complete regime; no direct Strategy D
  bearing.
- Gaifman algebras: σ-complete, no finitely additive measure.  Stronger
  obstruction than Strategy D needs; wrong row.

## Concrete Tasks

### Completed

- [x] Read Fremlin §531–§534, §538–§539 for MA/not-CH/PID results.
      (2026-05-21.  §539 is the critical section; all σ-complete regime.)
- [x] Read Argyros (1983) directly and verify σ-completeness.
      (2026-05-21.  Confirmed: βY is extremally disconnected → σ-complete.)
- [x] Read Džamonja-Plebanek (2008) for Todorčević example and MA results.
      (2026-05-20.  Atoms confirmed; not Strategy D.)
- [x] Build near-miss table of candidate spaces.  (2026-05-21.  See above.)
- [x] Verify Argyros σ-completeness.  (2026-05-21.  Confirmed via
      Comfort-Negrepontis Theorem 6.25: the "Argyros example" is $G(X_n)$,
      the Gleason space, which is extremally disconnected by definition.
      σ-complete — wrong row.)

### Open

1. Verify the topological equivalence:

   $$
   B\text{ non-}\sigma\text{-complete}
   \quad\Longleftrightarrow\quad
   \operatorname{St}(B)\text{ not basically disconnected}
   $$

   with exact hypotheses.  (Likely Fremlin §314 or Koppelberg §6.)

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

4. ~~Obtain and read Plebanek (2024 survey).~~  DONE (2026-05-21).
   Survey covers $P(K)$ spaces, not Strategy D directly.  See
   "Read" section above.

5. ~~Inspect Kunen/Fedorchuk examples against Strategy D conditions.~~
   DONE (2026-05-21).  Kunen (1981): carries a s.p. measure — not
   a candidate.  Fedorchuk (1977): paper addresses sequential
   compactness only; σ-completeness and measure-freeness both
   unresolved.  Neither closes the gap.  See "Read" section above.

6. Investigate attack mode C: can Souslin-algebra or Argyros-type
   techniques produce a non-σ-complete non-atomic measure-free BA
   under ◇ or CH?

7. **NEW (2026-05-21): Investigate the pre-Gleason space.**
   Argyros's $\beta Y_n$ (before passing to $G(\beta Y_n)$) already
   satisfies (*), ¬(**), is compact, zero-dimensional, ccc, and has
   no isolated points.  If $\beta Y_n$ is NOT basically disconnected,
   it is a Strategy D example in ZFC.  Determine whether
   $\operatorname{Clop}(\beta Y_n)$ is σ-complete.  Since
   $\operatorname{Clop}(\beta Y_n) \cong \operatorname{Clop}(Y_n)$,
   this reduces to: does every countable disjoint family of clopens
   in $Y_n$ whose join exists have a clopen join?

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

### Lit-map verdict (2026-05-21, finalized)

The systematic read of Fremlin §531–§539, Argyros (1983),
Džamonja-Plebanek (2008), Comfort-Negrepontis Ch. 6, and
Plebanek (2024) is complete.  The near-miss table confirms:

**Among the constructions surveyed — Argyros (1983), Gaifman (1964),
Souslin algebras, Todorčević/D-P (2000/2008), Farah-Veličković (2006),
Talagrand (2008), $\mathcal{P}(\mathbb{N})/\mathrm{fin}$, countably
generated BAs, Kunen (1981), Fedorchuk (1977) — none achieves all
three Strategy D conditions simultaneously.**  Kunen's space carries
a strictly positive measure (wrong side).  Fedorchuk's paper doesn't
address the measure question (σ-completeness also unresolved).

- The σ-complete regime is well-mapped: Argyros (ZFC, verified
  extremally disconnected via Comfort-Negrepontis 6.25), Souslin
  algebras (◇), Gaifman (ZFC, even stronger), Farah-Veličković
  (□_κ) all produce measure-free non-atomic BAs, but all are
  σ-complete.
- The non-σ-complete regime has exactly one measure-free construction
  (Todorčević/D-P), and it has atoms.
- Even in the σ-complete regime, measurability is axiom-sensitive
  (PID vs ◇).  This makes ZFC resolution of Strategy D unlikely.

**Likely status: ZFC-independent**, with the specific independence
not yet established.

**Unresolved sub-question:** The pre-Gleason space $\beta Y_n$ in
Argyros's construction already has property (*), ¬(**), is compact,
zero-dimensional, ccc, and has no isolated points.  If its clopen
algebra is NOT σ-complete, it is a Strategy D example in ZFC.
None of the sources read (Argyros 1983, Argyros 1982,
Comfort-Negrepontis Ch. 6, Fremlin §531–§539, Džamonja-Plebanek
2008, Plebanek 2024) address whether $\beta Y_n$ is basically
disconnected.  The Gleason-space step is standard in the literature
for ensuring extremal disconnectedness, but whether it is
*necessary* for the measure-theoretic properties is unresolved.
Prior probability of a positive resolution (i.e., $\beta Y_n$ NOT
basically disconnected) is low — 40+ years of expert work in this
neighborhood makes an overlooked ZFC example unlikely — but the
question is mathematically precise and can be settled by direct
analysis of $Y_n$'s cozero structure.

**Next concrete steps:**

> **PEN-AND-PAPER KIT:** `problemset_strategy_d.{tex,pdf}` — self-contained working
> problem-set (definitions, Stone duality, GJ lever, the Argyros construction, the
> open target, the obstruction, the sub-tasks). Start there to work it by hand.
>
> **STEP 1 ADVANCED 2026-06-12 (GJ-grounded reduction).** "Is
> $\operatorname{Clop}(Y_n)$ σ-complete?" is now reduced via Gillman–Jerison
> (1H: b.d. ⟺ every cozero has open closure; 6M.1: $\beta X$ b.d. ⟺ $X$ b.d.;
> 6W: the strictly-increasing-clopen non-b.d. witness template) to **two precise
> sub-questions**, full working in `argyros_sigma_completeness_handoff.md` +
> `..._scratch.md`:
> - **(witness, unconditional, intrinsic)** Find strictly increasing $\mathfrak{T}$-clopens
>   $G_1\subseteq G_2\subseteq\cdots$ in $Y_n$ with **no least clopen upper bound**
>   (closure of union not open) ⟹ $\operatorname{Clop}(Y_n)$ non-σ-complete ⟹ **ZFC
>   Strategy D example**. **UPDATE 2026-06-12 — THREE families now killed by one
>   mechanism** (single-branch; coordinate/all-zeros; and the $V_\Sigma$-accumulation
>   to a limit branch): the overshoot points are themselves *subbasic open* $V_\Sigma$,
>   hence **interior** to the closure, so the closure stays open and the sup exists. A
>   witness needs a closure point that is **not interior** — a true boundary point in
>   *no* $V_\Sigma$ — and the abundance of open $V_\Sigma$ makes that hard. This is a
>   strong structural obstruction (not yet a formalized theorem) and **shifts the prior
>   toward "route closed."** Full account: `argyros_sigma_completeness_handoff.md`,
>   §"THREE families killed by one mechanism."
> - **(named open sub-lemma)** Is $(Y_n,\mathfrak{T})$ **strongly** zero-dimensional
>   ($\dim=0$, i.e. $\beta Y_n$ zero-dim)? Argyros gives only a clopen base
>   ($\operatorname{ind}=0$); this does NOT follow, and $\mathfrak{T}$ finer-than-product
>   can break the Lindelöf upgrade. Needed only for the *impossibility* direction;
>   the witness direction routes around it (work in $B=\operatorname{Clop}(Y_n)$,
>   $\sigma$-complete ⟺ $\operatorname{St}(B)=\beta_0 Y_n$ b.d., unconditionally).
>
> GJ scans: `notes/literature_review/literature/gillman_jerison_pages/`. The
> reduction is rigorous/citeable; the witness construction and impossibility proof
> are the human Phase-4 step (not LLM-derivable).

1. **The two sub-questions above** (limit-branch witness; strong-zero-dim
   sub-lemma) — the live concrete targets for step 1.
2. If $Y_n$ proves basically disconnected (route closed), investigate attack
   mode C (consistency construction under ◇/CH).
3. Inspect Kunen/Fedorchuk examples against Strategy D conditions.
4. Further progress on the impossibility side likely requires collaboration with
   a set theorist; the witness side is a concrete hand-construction in $Y_n$.
