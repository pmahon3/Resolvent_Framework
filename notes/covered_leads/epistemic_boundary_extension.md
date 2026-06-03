# Maximal Fibre Invariants of Partial Probability Data (PARKED)

**Date:** 2026-06-02 (parked same day)  
**Phase:** 2 complete — unification claim PARKED  
**Status:** PARKED. The three-way unification (Paper I / OML / κ_Q)
FAILS — see Q0 verdict below. Productive residue (the two-axis
correction to the OML problem) was extracted and applied to
`notes/open_questions/oml_extension_problem` and Paper II. This note
is retained as the end-to-end record of *why* the unification fails
and how the two-axis distinction was found.

**Revival trigger:** none standing. The OML extension bridge theorem
(single-domain, not unification) is the live descendant and lives in
`open_questions/`.

**Claimed type(s):** TBD — depends on whether Q0 below has a positive
answer. If yes: Type 1 (new theorem) or Type 3 (unifying framework).
If no: DEAD.

**Risk acknowledgement:** The Five-Traditions unification thread died
(2026-05-18) on "assembling instances under a common frame" that
collapsed to published results with fancier coordinates. Phase 2
audit (2026-06-02) killed the initial Type 3 framing ("common
category for extension") because:
- The {Paper I, OML} pair is already unified in effectus theory
  (Cho-Westerbaan-van de Wetering 2020)
- κ_Q is a different mathematical operation (marginal lifting ≠
  σ-additivity upgrading)
- The best transfer candidate degenerated to a tautology

What survived the audit: the three problems share a *situation* —
partial data constraining a space of completions — even though the
specific operations differ. The present note reformulates around
this surviving structure.

---

## The situation (invariant across domains)

In each of three settings, an agent holds:
1. **Partial data** $p$ — a structured assignment of probabilities
   on an algebra smaller than the "true" one.
2. **A restriction functor** $U : \mathbf{Complete} \to \mathbf{Partial}$
   expressing how complete structures project to partial ones.
3. **A fibre** $U^{-1}(p)$ — the space of all completions compatible
   with the partial data.

The fibre may be empty (extension impossible), a singleton (extension
unique), or large (extension underdetermined). The question is not
"does the fibre contain a point?" but:

> **What features of the fibre are determined by $p$ alone — without
> enumerating the fibre?**

| Setting | $U$ | $p$ | Fibre $U^{-1}(p)$ | Known fibre-invariant |
|---------|-----|-----|-------------------|----------------------|
| Paper I | restrict σ-additive measure to charges on subalgebras | compatible charges $\{\ell_i\}$ | singleton or empty | **Yosida-Hewitt $\ell_p$**: the purely finitely additive part. $\ell_p = 0$ iff fibre is a singleton. Computable from $p$. |
| OML | restrict Baire measure on $S_0(A)$ to state on clopens | state $s : A \to [0,1]$ | unknown | **???** — this is the open problem. De Simone-Navara's YH-type decomposition for OMPs is a candidate. |
| κ_Q | marginalise joint law to conditional kernel on $\sigma(Q)$ | $\kappa_Q$ | always large (non-singleton, non-empty) | **Level-3 necessary conditions**: ACF decay rate, dispersion structure, between-stratum character. Computable from residuals. Constrain the fibre but don't collapse it. |

---

## Q0: Is there a well-posed mathematical question?

The candidate:

> **For a restriction functor $U : \mathbf{C} \to \mathbf{D}$ between
> categories of probability structures, and partial data $p \in \mathbf{D}$,
> characterise the maximal invariant of the fibre $U^{-1}(p)$ that is
> computable from $p$ alone.**

"Maximal" = maximally constraining (rules out the most completions).
"Computable from $p$" = does not require explicit construction of
any element of the fibre.

### What "maximal invariant" would mean

An invariant $I(p)$ of the fibre is a quantity or structure such that:
- $I(p)$ is determined by $p$ (not by any specific completion)
- For any completion $\hat{p} \in U^{-1}(p)$, $\hat{p}$ satisfies $I(p)$
- $I(p)$ is non-trivial: there exist hypothetical completions that
  violate $I(p)$ (i.e., $I$ rules something out)

The *maximal* invariant would be the finest such constraint — the
strongest thing $p$ determines about its completions. If it exists,
every other fibre-invariant factors through it.

### The prototype: Yosida-Hewitt

In Paper I's Boolean setting, the Yosida-Hewitt decomposition gives:
$$\ell = \ell_c + \ell_p$$
where $\ell_c$ is σ-additive (the "completable part") and $\ell_p$ is
purely finitely additive (the "obstruction"). This decomposition:
- Is computable from $\ell$ alone
- Determines the fibre completely: fibre = singleton iff $\ell_p = 0$
- Is maximal: it tells you *everything* about whether and how
  extension works

The question is whether YH's *role* — maximal fibre invariant
computable from partial data — has analogues in other settings,
even if the specific construction is entirely different.

---

## Sub-questions (to determine if Q0 is well-posed)

### SQ1: Does "maximal invariant" exist categorically?

In what generality does a restriction functor $U$ admit a "largest
thing you can compute about the fibre from the base point alone"?

This might connect to:
- **Sufficient statistics** (classical: a statistic $T(x)$ is
  sufficient for $\theta$ if $P(x|T)$ doesn't depend on $\theta$).
  A fibre-invariant is like a "sufficient obstruction" — it captures
  all information $p$ carries about its completions.
- **Kan extensions** — the left/right Kan extension of a functor
  along $U$ is the "best approximation" from one side. Is the
  maximal fibre-invariant a Kan extension?
- **Galois connections** — if there's an adjunction between "fibre
  properties" and "base-computable invariants," the maximal
  invariant is the fixed point.

### SQ2: What is the OML analogue of Yosida-Hewitt?

For a state $s$ on an OML $A$:
- Is there a canonical decomposition $s = s_\sigma + s_p$ where
  $s_\sigma$ "extends" and $s_p$ "obstructs"?
- De Simone-Navara study YH-type decompositions for OMPs. What do
  they find? Does the decomposition determine the extension fibre?
- If the decomposition exists but doesn't determine the fibre, what
  additional information is needed? (That gap would be the genuinely
  new obstruction in the OML case.)

### SQ3: What is the κ_Q analogue?

For a conditional kernel $\kappa_Q$:
- Level-3 necessary conditions (ACF structure, dispersion) are
  *partial* fibre-invariants — they constrain but don't determine.
- Is there a *maximal* invariant? What is the strongest thing
  $\kappa_Q$ determines about all compatible joint laws?
- This connects to: identifiability theory (what parameters are
  identified from the marginal?), partial identification
  (Manski — bounds on parameters, not point identification),
  the information inequality (Cramér-Rao as a bound on what
  partial data can say about completions).

### SQ4: Does the answer to SQ2 or SQ3 generate something non-trivial?

The test for whether Q0 is the right question:
- If answering "what is the maximal fibre-invariant for OML states?"
  yields a theorem (not just a reformulation), Q0 is productive.
- If answering "what is the maximal fibre-invariant for κ_Q?" yields
  something beyond the Level-3 necessary conditions (either a proof
  they're maximal, or something stronger), Q0 is productive.
- If both answers are trivial reformulations: Q0 is the wrong
  question. DEAD.

---

## Why this might not be the Five-Traditions pattern

The Five-Traditions thread tried to unify by finding a *common
category* — a single framework housing all instances. The audit
correctly killed that.

This seed is different: it doesn't claim a common category. It
claims a common *role* — the Yosida-Hewitt decomposition plays a
specific role (maximal fibre-invariant) in Paper I, and asks whether
that role has occupants in other settings. The question is:

> Does the *role* of YH generalise, even if the *construction*
> doesn't?

This is more like asking "what plays the role of curvature in this
geometry?" than "are these two geometries isomorphic?" The former
can be productive even when the latter fails.

The discriminator: if the answer to SQ2 or SQ3 is non-trivial
(yields a theorem, not a restatement), the question was productive.
If both degenerate, the "common role" was an illusion and the seed
dies.

---

## Literature scout findings (2026-06-02)

### A. YH decomposition for OMLs exists but is not connected to extension

**De Simone, A. and Navara, M.** "Yosida-Hewitt and Lebesgue
decompositions of states on orthomodular posets." *J. Math. Anal.
Appl.* 255(1), 74–104 (2001).

The decomposition $s = s_\sigma + s_{\mathrm{wpfa}}$ exists for
states on OMPs. The "weakly purely finitely additive" (wpfa)
component replaces the classical purely finitely additive part.
**Uniqueness fails in general** — it holds only under the Riesz
Decomposition Property (RDP), which forces the state space to be a
Choquet simplex (Dvurečenskij 2011). For non-Boolean OMLs whose
state spaces are not simplices, the decomposition is non-unique.

**Critical gap (apparently unstudied):** No source connects the
De Simone-Navara decomposition to the state extension problem.
The Boolean bridge — "$\ell_p = 0$ iff extension exists" — has
no published OML analogue. This is not a gap due to difficulty
of the bridge theorem; it appears to be simply unasked.

**Obstruction interaction:** Pták (1994) shows that if all
states on an OML are σ-additive (i.e., all wpfa parts vanish),
the lattice is forced to be Boolean. So the wpfa component is
*generically nonzero* on non-Boolean OMLs, and any extension
theory must accommodate states with nonzero wpfa parts.

**Schindler (1989):** Unique Jordan-Hahn decomposition on a
finite OMP with a strong section of states iff the OMP is
Boolean. Uniqueness of decomposition is itself a Boolean
certificate.

### B. "Maximal fibre-invariant" is a real concept with established names

The concept degenerates in the bare set-theoretic case (the fibre
is trivially determined by the base point and the functor). It
becomes substantive when equipped with computability/structural
constraints. Established instances:

**1. Maximal invariant (mathematical statistics).** Given a group
$G$ acting on a sample space $X$, a statistic $T(x)$ is a
*maximal invariant* if it separates $G$-orbits: $T(x_1) = T(x_2)$
iff $x_2 = g \cdot x_1$ for some $g$. Universal property: any
invariant statistic factors through $T$. Always exists under mild
measurability. (Wijsman 1967; Lehmann-Romano 2005, Ch. 6–8.)

**2. Sharp identified set (econometrics).** When a model is not
point-identified, the sharp identified set $\Theta_I$ is "the set
of parameter values consistent with the data and maintained
assumptions" — exactly the strongest constraint on completions
determined by partial observations. Key theorem: Beresteanu,
Molchanov, Molinari (2011, *Econometrica* 79(6)): for models with
convex moment predictions, $\Theta_I$ admits a support-function
characterisation via Artstein's inequalities. **Sharpness is itself
a theorem** — proving that the identified set cannot be tightened
without additional assumptions.

References: Manski (2003) *Partial Identification*; Tamer (2010)
*Ann. Rev. Econ.* 2; Molinari (2020) *Handbook of Econometrics*
vol. 7 (arXiv:2004.11751).

**3. Right Kan extension (category theory).** For
$U : \mathbf{C} \to \mathbf{D}$ and $F : \mathbf{C} \to \mathbf{E}$,
$(\mathrm{Ran}_U F)(d) = \lim_{(c,\, U(c) \to d)} F(c)$.
When $F = \mathrm{id}$, this computes "the best approximation to
fibre structure visible from $d$." Existence requires the
relevant limits. In fibred categories, **effective descent** is the
precise criterion for "the base determines the fibre" — a morphism
is an effective descent morphism iff the pullback functor is
monadic (Bénabou-Roubaud 1970).

**4. Galois connection / closure operator.** The maximal
fibre-invariant is the fixed point of the closure operator
$g \circ f$ where $f \dashv g$ is the adjunction associated to $U$.
Exists precisely when the right adjoint preserves the relevant
structure.

**Unifying principle:** These are all instances of one
universal-property pattern — the maximal base-computable invariant
is the value at $p$ of the right adjoint associated to $U$.
Content comes from *computing* it tractably in specific settings.

---

## What the scout sharpens

### The OML question (SQ2) is now precise:

> **Does the De Simone-Navara wpfa component $s_{\mathrm{wpfa}}$
> determine whether $s$ extends to a σ-additive measure on the
> Baire algebra of $S_0(A)$?**

Sub-cases:
- If $s_{\mathrm{wpfa}} = 0$ (the state is σ-additive on $A$):
  does extension follow? (In the Boolean case: yes, trivially.
  In the OML case: non-trivial because Carathéodory is unavailable.)
- If $s_{\mathrm{wpfa}} \neq 0$: is extension necessarily blocked?
  Or can a state with nonzero wpfa part still extend (unlike the
  Boolean case)?
- When the decomposition is non-unique (non-simplex state space):
  do *all* decompositions agree on the extension question? If not,
  extension depends on *which* decomposition — a genuinely new
  phenomenon.

This question is apparently unstudied and non-trivial. It connects
two established literatures (De Simone-Navara decomposition theory;
OML extension/Gleason theory) that have not been bridged.

### The κ_Q question (SQ3) has an exact econometric parallel:

> **Are the Level-3 necessary conditions *sharp* — i.e., for every
> Z satisfying them, does there exist a joint law consistent with
> $\kappa_Q$?**

This is literally the Manski/Beresteanu-Molchanov-Molinari question
applied to the κ_Q setting. "Sharp" means: the identified set
cannot be tightened. If Level-3 conditions are sharp, they are the
maximal invariant. If not, there exist tighter constraints
computable from $\kappa_Q$.

Methods for proving sharpness: Artstein's inequality
characterisation of random-set selections; support function
equality (Beresteanu et al. 2011); Andrews-Shi (2013) moment
inequality inference.

### The unifying question (Q0) refines to:

> **For each restriction functor $U$, does the right adjoint
> (maximal fibre-invariant) admit a tractable characterisation,
> and does it decompose into "determined part" + "free part" in a
> way that generalises Yosida-Hewitt?**

The Boolean case says yes (YH is the decomposition; the
σ-additive part is determined, the wpfa part is the free
component). The OML and κ_Q cases are open instances of this
question.

---

## What to investigate next

1. **Bridge theorem for OML (SQ2).** Read De Simone-Navara (2001)
   in detail. Formulate the precise statement: "on an OML $A$
   satisfying [conditions], $s$ extends to a σ-additive measure on
   $S_0(A)$ iff $s_{\mathrm{wpfa}} = 0$." Identify what conditions
   are needed. Check whether the Pták obstruction blocks this
   outright or only blocks it in the unital/global case.

2. **Sharpness of Level-3 for κ_Q (SQ3).** Can the Beresteanu-
   Molchanov-Molinari machinery prove sharpness (or non-sharpness)
   of the Level-3 necessary conditions in the Diggle/DHLZ
   covariance-decomposition setting? This is concrete and
   potentially executable with the MITACS data.

3. **Is the "right adjoint / maximal invariant" framing the correct
   formal umbrella?** Or is it too general (subsumes everything,
   predicts nothing)? Test: does the categorical framing *predict*
   that SQ2 and SQ3 should have the same structural answer (yes/no
   for sharpness), or does it merely *permit* them to be asked?

---

## Relation to existing programme

- **Paper I:** provides the *solved prototype* — YH is the maximal
  fibre-invariant, and we know it works.
- **OML extension (open_questions/):** provides the *hard test case*
  — does the role have an occupant?
- **κ_Q (covered_leads/, parked):** provides the *applied test case*
  — are Level-3 conditions the maximal invariant, or is there
  something stronger?
- **Five-Traditions (DEAD):** provides the *failure mode* — if this
  reduces to "same epistemological observation, different math," it
  dies the same death.

## Q0 verdict (2026-06-02): the three-way unification FAILS, but the
## two-way (Boolean↔OML) link is sharpened

The deep-read on the OML bridge question (does σ-additivity of a
state imply extension to a measure on $S_0(A)$?) returned a
structural correction that settles Q0.

**The finding splits the problem by axis.** $S_0(A)$ is a Stone
space (McDonald-Bimbó Cor. 3.7, verified against the paper). Its
*full* clopen algebra is Boolean; the state lives only on the
⊥-stable clopens (the OML, = image of $h$, Thm. 3.9). So extension
of a state on $A$ to a measure on $S_0(A)$ decomposes:

- **(A) Extension axis** — extend the orthogonally-additive state
  from the OML of ⊥-stable clopens to a finitely additive charge on
  the *full* Boolean algebra of clopens. Requires assigning
  consistent values to non-⊥-stable clopens (unions $h(a) \cup h(b)$
  for non-orthogonal $a,b$). This is the Pták-Pulmannová frontier.
  **σ-additivity does not help here.**
- **(B) Compactness** — once (A) succeeds, the charge extends to a
  σ-additive Borel measure automatically (Stone space). Free.
- **Descent** — σ-additivity of the state controls whether the
  resulting measure concentrates on $P(A)$ or leaks to non-principal
  filters. This presupposes (A).

**Why Q0 fails.** Map the three settings onto the two axes:

| | Extension axis | Descent axis |
|---|---|---|
| Paper I (Boolean) | trivial (free) | $\ell_p$ (Yosida-Hewitt) |
| OML | Pták-Pulmannová obstruction | wpfa (De Simone-Navara) |
| κ_Q | non-identifiability | **NONE** |

- The **descent axis** is the genuine Boolean↔OML parallel —
  σ-additivity governs *where mass lives* in both, via $\ell_p$ /
  wpfa. But this pair is *already* unified (effectus theory), and
  **κ_Q has no descent axis at all** — no dual space, no
  principal/non-principal leak. The κ_Q fibre is only "joints with
  this marginal" — purely extension-axis.
- The **extension axis** has three *different* obstructions (trivial
  / non-distributive / information-theoretic), sharing only "fibre
  of a restriction map" — the tautology.

So the maximal-fibre-invariant framing *permits* all three questions
but *predicts* nothing across them. κ_Q still plays the
Five-Traditions/Abramsky role: the different-category instance whose
removal leaves the already-published Boolean↔OML pair.

**Type 3 verdict: FAIL** (shared vocabulary, not method transfer).
**Q0 as a three-way unifying question: DEAD.**

**Caveat carried forward (correction to the descent story):** The
McDonald-Bimbó duality is purely *finitary*. The identity
$h(\bigvee_n a_n) = (\bigcup_n h(a_n))^{\perp\perp}$ holds for
*finite* joins but is **false in general for countable joins** —
finitary OML homomorphisms don't preserve infinite suprema. So even
the descent story in the OML case needs additional σ-completeness +
continuity hypotheses the duality doesn't supply. (Verified against
arXiv:2208.07430.)

## What survives (single-domain, not unification)

The session's productive residue is **not** a unifying framework. It
is a sharpened statement of the OML extension problem itself:

> In the Boolean case the first arrow (charge → Stone measure) is
> free and only descent is at stake. In the OML case **the first
> arrow is no longer free** — extending a state to a charge on the
> full clopen Boolean algebra of $S_0(A)$ is the open problem, and
> σ-additivity (wpfa) governs descent, not this extension.

This correction belongs in `open_questions/oml_extension_problem`
and is applied there. It does not depend on Q0.

## Audit history

- **2026-06-02, Round 1:** Type 3 (common category) FAIL. κ_Q is a
  different operation; {Paper I, OML} already unified in effectus
  theory; best transfer candidate degenerated. Seed reformulated
  around "maximal fibre-invariant" question.
- **2026-06-02, Round 2:** Q0 (maximal fibre-invariant as three-way
  unifier) FAIL. The Boolean↔OML link is genuine but lives on the
  descent axis, where κ_Q has no instance; the extension axis has
  three disjoint obstructions. Productive residue is the single-
  domain two-axis correction to the OML problem, not a unification.
  **Recommendation: PARK the unification claim; apply the two-axis
  correction to the OML note.**
