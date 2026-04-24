# Fibre Mixing Irreducibility — Investigation

*Opened 2026-04-20*

**Status:** Active investigation. First question: does the Łoś-type argument transfer?

---

## The question

Is fibre mixing derivable from any structural condition on the query system or
the dynamics? Or is it irreducible in the same sense as CE — i.e., no
first-order (or finitary structural) condition can imply it?

---

## What fibre mixing says

**Definition** (Paper IV, Definition 5.1). Fix $\varepsilon > 0$. An event
$S^* \in \mathcal{B}$ is $(c, \varepsilon)$-mixing across fibres if there
exists $c > 0$ such that

$$\mu_z(S^*)\,\mu_z((S^*)^c) \;\geq\; c \cdot p_z
\quad \text{for $\nu_L$-a.e.\ $\varepsilon$-large fibre } z.$$

Here $\nu_L$ is the distribution of the lag-$L$ delay vector $\Phi_h^{(L)}(x)$,
$p_z = \mu(\{\Phi_h^{(L)} = z\})$ is the fibre mass, and $\mu_z$ is the
conditional measure on the fibre over $z$.

**What it does:** Under fibre mixing, the algebraic witness $\delta(L)$ and
the entropy witness $H_2(\nu_L)$ are asymptotically equivalent:
$$\delta(L) \to 0 \iff H_2(\nu_L) \to +\infty.$$

**Where it sits:** Ergodicity implies fibre mixing. Fibre mixing is
independent of the uniform separation condition (US). It is not a standing
assumption of Paper IV — it is used only in the entropy characterisation
(Corollary 5.12).

---

## The CE parallel

CE is to Paper I what fibre mixing is to Paper IV:

| | CE | Fibre mixing |
|---|---|---|
| **Role** | Necessary and sufficient for σ-additive extension | Necessary for δ(L) ↔ H₂(ν_L) equivalence |
| **Implied by** | σ-additivity (trivially) | Ergodicity |
| **Weaker than** | Ergodicity / compactness | Ergodicity |
| **Irreducibility** | Proved (Łoś + finite-cofinite) | **Open** |
| **Failure witness** | Finite-cofinite charge | ? |

The CE irreducibility proof has three components:
1. A family of individually good structures (Dirac charges $\delta_n$, each σ-additive)
2. An ultraproduct that produces a bad structure (finite-cofinite charge $\ell$)
3. Łoś's theorem: any first-order theory satisfied by all $\delta_n$ is satisfied
   by the ultraproduct — but the ultraproduct fails CE. Contradiction.

The question is whether this template transfers to fibre mixing.

---

## First questions

### Q1. What is the right language?

CE irreducibility was proved in $\mathcal{L}_{\mathrm{BA},\mu}$ — the first-order
language of Boolean algebras with a normalized finitely additive charge. That
language is very primitive, and the result is strong: no accumulation of
first-order conditions in that language can imply CE.

For fibre mixing, the relevant language is richer: it involves dynamics ($T$),
a lag parameter ($L$), fibres of the delay map, and conditional measures. The
question is what the right first-order language is — or whether the right
notion of "structural condition" is not first-order at all but something
finitary in a different sense.

**Two candidate framings:**

**(A) First-order in a dynamical language.** Define a language $\mathcal{L}_{\mathrm{dyn}}$
with symbols for the measure space, the transformation $T$, and the observable
$h$. A structural condition is a first-order sentence in this language. Is
fibre mixing first-order axiomatizable in $\mathcal{L}_{\mathrm{dyn}}$?

**(B) Derivable from finitary observational data.** A structural condition
is any condition expressible from the query system alone — cylinder sets,
compatible charges, refinement maps — without reference to the global dynamics
or the measure on fibres. Is fibre mixing derivable from such data?

Framing (B) is more natural for the programme. It is the direct analogue of
the CE question: CE is not derivable from any structural condition on the
query system; is fibre mixing not derivable from any structural condition on
the dynamics visible to finite observation?

### Q2. Does the Łoś argument transfer?

The CE proof works because:
- Dirac charges are individually σ-additive (individually satisfy CE)
- Their ultraproduct is the finite-cofinite charge (fails CE)
- The failure is witnessed by a decreasing sequence $A_k \searrow \emptyset$
  with $\ell(A_k) = 1$ for all $k$

For fibre mixing, the analogous construction would need:
- A family of dynamical systems $(X_n, T_n, \mu_n, h_n)$ each individually
  satisfying fibre mixing
- An ultraproduct (in some sense) that fails fibre mixing
- A first-order sentence that holds in each factor but fails in the ultraproduct

The obstacle: fibre mixing involves conditional measures on fibres of the
delay map, which are not obviously first-order expressible. The ultraproduct
of dynamical systems is also more complex than the ultraproduct of Boolean
charge spaces.

**Key sub-question:** Is there a first-order sentence $\phi$ in
$\mathcal{L}_{\mathrm{dyn}}$ that is satisfied by every ergodic system but
fails in some system lacking fibre mixing? If so, fibre mixing is a consequence
of ergodicity + $\phi$, not of fibre mixing alone — and the irreducibility
question sharpens to whether $\phi$ can be dropped.

### Q3. What is the failure witness?

For CE, the failure witness is the finite-cofinite charge: it satisfies every
first-order structural condition yet fails CE. The witness is canonical and
explicit.

For fibre mixing, the failure witness — a system that satisfies every
"structural" condition yet fails fibre mixing — is not known. Identifying it
is the central task.

**Candidate witnesses:**
- A system with large trivial fibres: $T = \mathrm{id}$, so all delay vectors
  are the same point, fibres are the whole space, and $\mu_z(S^*)\mu_z((S^*)^c)$
  is bounded away from zero but $p_z$ is large. Does fibre mixing fail?
- A system with a sparse mixing structure: ergodicity fails but some weaker
  condition holds. Is fibre mixing then genuinely independent?
- A non-ergodic system with a non-trivial invariant factor: the fibres of the
  delay map may be concentrated on the invariant factor, making fibre mixing
  vacuously true or false depending on the factor.

---

## What would constitute a result

**Irreducibility (negative for derivability):**
Exhibit a family of dynamical systems each satisfying fibre mixing, whose
ultraproduct (or some limiting construction) fails fibre mixing, while every
"structural" first-order condition satisfied by the family is also satisfied
by the limit. Then argue by the Łoś analogue.

**Derivability (positive):**
Show that fibre mixing follows from ergodicity alone, or from some weaker
structural condition expressible in the relevant language. This would break
the CE/fibre-mixing parallel and require a reframing of the programme's
three-obstruction table.

**Partial result:**
Show that fibre mixing is not derivable from any *finitary observational*
condition (framing B), even if it might be derivable from some dynamical
condition. This would still be significant — it would say the obstruction
is invisible to the observational layer, even if not to the dynamical layer.

---

## Status checklist

- [x] Fix the right language / notion of structural condition (Q1) — see step1_framing.md
- [x] Framing B: expressible in conditional cylinder-charge language (step1_framing.md)
- [x] Framing B irreducibility: provable via Dirac-conditional witness, but witness is
      too cheap — no dynamical system produces atomic conditionals generically (step2_failure_witness.md)
- [x] **Pivot: real question is framing A** — is fibre mixing first-order axiomatizable
      in $\mathcal{L}_{\mathrm{dyn}}$? Correct framework: continuous logic for metric
      structures (step2_failure_witness.md)
- [x] Assess whether the Łoś argument transfers in continuous logic (Q2) — yes for
      lag-by-lag (LBL); UFM escapes continuous logic expressibility; gap is uniformity
      across lags, exactly as CE (step3_continuous_logic.md)
- [x] Witness construction well-posed: irrational rotations $\alpha_n \to 0$ with
      binary observable $h = \mathbf{1}_{[0,1/2)}$; fibre mixing constant
      $c(\alpha_n, L) \approx \Theta(\alpha_n) \to 0$ for fixed $L$; ultraproduct
      preserves LBL (Łoś) but loses UFM (no uniform $c'>0$); three-distance theorem
      governs fibre sizes (step4_rotation_computation.md)
- [x] Rotation witness hits a fundamental obstruction: binary observable on circle
      does not reconstruct ($\delta_L \not\to 0$), so fibre mixing corollary is vacuous
      in this regime. Honest assessment in step5_synthesis.md.
- [x] Derivability question precisely posed (step6_derivability.md); all of $\delta_L$
      is from non-monochromatic fibres (proved); near-maximizer carries balanced large fibres
- [x] Bridge theorem proved (step7_bridge_theorem.md): $\nu(G(\eta)) \geq 2(\kappa-\eta)$
      where $\kappa$ = large-fibre contribution to approximation error; no ergodicity needed.
      Key: lower bound on $\nu(G)$ requires upper pointwise bound on integrand ($\leq 1/2$),
      not lower bound (which gives only an upper bound on $\nu(G)$ — wrong direction).
- [x] Two-step structure identified: Step A (analytic, $\kappa > 0$ bound) and Step B
      (dynamical, upgrade positive-fraction to a.e.); bare ergodicity may not suffice for Step B
- [ ] **Step A:** explicit lower bound for $\kappa$ in terms of $\delta_L$ and $(\mu\otimes\mu)(R_{>\varepsilon})$
- [ ] **Step B:** identify what dynamical condition forces $\nu(\mathcal{M}_0\cup\mathcal{M}_1)=0$
      (a.e. large fibre balanced). Ergodicity asserted sufficient in bridge note remark — not proved.
- [ ] State derivability theorem once Steps A+B resolved; update CE vs UFM parallel accordingly
- [ ] Determine relationship between fibre mixing and ergodicity more precisely
- [ ] Determine whether fibre mixing is necessary (not just sufficient) for
      δ(L) ↔ H₂(ν_L) equivalence

---

## Relationship to coherence/consistency schema

Once this investigation has a result — irreducibility or derivability — it
becomes the second worked example in the coherence/consistency schema
(`notes/future/coherence_consistency_direction.md`):

- **Local data:** finitary observational data from the query system
- **Global realization:** equivalence of algebraic and entropy witnesses
- **Failure mode:** fibre mixing fails — fibres are too large or too uniform
  to make the conditional variance identity tight

The coherence/consistency schema should not be developed until this
investigation has a clear answer.
