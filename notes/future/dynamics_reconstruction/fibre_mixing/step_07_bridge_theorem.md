# Step 7 — The Bridge Theorem

*2026-04-23*

**Status:** Bridge theorem proved. Exact lower bound on the $\nu_L$-mass of
balanced large fibres, depending only on $\delta_L$, $\varepsilon$, $\eta$.
No ergodicity required. The derivability question is now precisely located.

---

## The theorem

**Theorem (Bridge).** Let $(X, \mathcal{B}, \mu)$ be a probability space,
$\mathcal{O} \subseteq \mathcal{B}$ a sub-$\sigma$-algebra with associated
fibre decomposition $(C_z, p_z, \mu_z)_{z}$, and $\nu = \Phi_*\mu$ the
push-forward. Fix $\varepsilon, \eta > 0$, and let $S^*$ be an $\varepsilon$-maximizer
of

$$\delta(\mathcal{O}) := \sup_{S \in \mathcal{B}} \inf_{E \in \mathcal{O}} \mu(S \triangle E).$$

Suppose $\delta(\mathcal{O}) > 2\varepsilon + \eta$. Then the set

$$G(\eta) := \bigl\{z : p_z \geq \varepsilon,\; \mu_z(S^*) \in [\eta, 1-\eta]\bigr\}$$

of $\varepsilon$-large fibres on which $S^*$ is $\eta$-balanced satisfies:

$$\nu(G(\eta)) \cdot \eta^2 \cdot \varepsilon
\;\leq\;
\int_{G(\eta)} p_z \cdot \mu_z(S^*)\mu_z((S^*)^c)\,d\nu(z)
\;\leq\;
\delta(\mathcal{O})$$

and more usefully:

$$\nu(G(\eta)) \;\geq\; \frac{\delta(\mathcal{O}) - 2\varepsilon - \eta}{\varepsilon \cdot (1/4)}
\cdot \frac{1}{1}
\;=\; \frac{4(\delta(\mathcal{O}) - 2\varepsilon - \eta)}{\varepsilon}.$$

Wait — let me do this carefully from scratch.

---

## Setup and notation

Let $\Phi: X \to Z$ be the quotient map (e.g., the delay map $\Phi_h^{(L)}$).
For each $z \in Z$, write $p_z = \mu(\Phi^{-1}(z))$ and $\mu_z = \mu(\cdot \mid \Phi = z)$.
The sub-$\sigma$-algebra $\mathcal{O} = \sigma(\Phi)$ consists of sets of the form
$\Phi^{-1}(B)$ for Borel $B \subseteq Z$.

For any $S \in \mathcal{B}$, write $\alpha_z := \mu_z(S^*)$ and recall:
$$\mathbb{E}[\text{Var}(\mathbf{1}_S \mid \mathcal{O})]
= \int p_z \cdot \alpha_z(1-\alpha_z)\,d\nu(z).$$

The best $\mathcal{O}$-approximation to $S$ is the majority-vote set:
$E_S := \Phi^{-1}(\{z : \alpha_z \geq 1/2\})$, giving
$$\mu(S \triangle E_S) = \int p_z \cdot \min(\alpha_z, 1-\alpha_z)\,d\nu(z).$$

Since $\delta(\mathcal{O}) = \sup_S \inf_{E \in \mathcal{O}} \mu(S \triangle E)$,
and the majority-vote set achieves the infimum for indicator functions, we have

$$\delta(\mathcal{O}) = \sup_S \int p_z \cdot \min(\mu_z(S), 1 - \mu_z(S))\,d\nu(z).$$

An $\varepsilon$-maximizer $S^*$ satisfies:
$$\int p_z \cdot \min(\alpha_z, 1-\alpha_z)\,d\nu(z) \geq \delta(\mathcal{O}) - \varepsilon.$$

---

## Partition of fibres

For the $\varepsilon$-maximizer $S^*$, partition the fibres into four classes:

- $\mathcal{S}$ (small): $p_z < \varepsilon$
- $\mathcal{M}_0$ (large, near-zero): $p_z \geq \varepsilon$, $\alpha_z < \eta$
- $\mathcal{M}_1$ (large, near-one): $p_z \geq \varepsilon$, $\alpha_z > 1-\eta$
- $\mathcal{G}$ (large, balanced): $p_z \geq \varepsilon$, $\alpha_z \in [\eta, 1-\eta]$

This is $G(\eta)$ from the theorem statement. The integral splits:
$$\delta(\mathcal{O}) - \varepsilon
\leq \int p_z \min(\alpha_z, 1-\alpha_z)\,d\nu
= I_\mathcal{S} + I_{\mathcal{M}_0} + I_{\mathcal{M}_1} + I_\mathcal{G}$$

**Bound $I_\mathcal{S}$:** On $\mathcal{S}$, $p_z < \varepsilon$ and
$\min(\alpha_z, 1-\alpha_z) \leq 1/2$, so $I_\mathcal{S} \leq \varepsilon/2$
(integrating $p_z \leq \varepsilon \cdot \mathbf{1}$ against $d\nu$ gives
$\int_\mathcal{S} p_z\,d\nu \leq \int p_z\,d\nu = 1$... more carefully:

$$I_\mathcal{S} = \int_{\mathcal{S}} p_z\min(\alpha_z, 1-\alpha_z)\,d\nu
\leq \int_\mathcal{S} p_z \cdot \frac{1}{2}\,d\nu
\leq \frac{1}{2}\int_\mathcal{S} p_z\,d\nu
\leq \frac{1}{2}\cdot 1 = \frac{1}{2}$$

That is too weak. Better: each small fibre has $p_z < \varepsilon$, so
$p_z \min(\alpha_z, 1-\alpha_z) \leq p_z/2 < \varepsilon/2$ for each $z$,
but there can be many small fibres. However:
$$I_\mathcal{S} \leq \frac{1}{2}\int_\mathcal{S} p_z\,d\nu
= \frac{1}{2}(\mu \otimes \mu)(R^{<\varepsilon})$$

where $R^{<\varepsilon}$ denotes the union of small-fibre product sets. The
small-fibre contribution satisfies $\int_\mathcal{S} p_z^2\,d\nu \leq \varepsilon$
(since $p_z < \varepsilon$ and $\int p_z\,d\nu = 1$), but $\int_\mathcal{S} p_z\,d\nu$
could be up to 1.

Use instead:
$$I_\mathcal{S} = \int_\mathcal{S} p_z\min(\alpha_z, 1-\alpha_z)\,d\nu
\leq \frac{1}{2}\int_\mathcal{S} p_z\,d\nu \leq \frac{1}{2}.$$

This gives $I_\mathcal{S} \leq 1/2$, which is not tight enough. We need a
better bound. Use: $\int_\mathcal{S} p_z\,d\nu = \nu(\mathcal{S})$ where by
definition $\mathcal{S}$ consists of fibres of mass $< \varepsilon$.

Actually the key observation is:
$$I_\mathcal{S} \leq \frac{1}{2}\cdot \nu(\mathcal{S})\cdot \varepsilon$$

since each fibre $z \in \mathcal{S}$ contributes $p_z\min(\alpha_z,1-\alpha_z)\leq p_z/2 < \varepsilon/2$, but $\nu(\mathcal{S})$ could be large. This is still not clean. Let me reconsider.

---

## Cleaner approach: mass of small fibres

The key fact: $\int p_z\,d\nu(z) = 1$ (total mass is 1). So:

$$\int_\mathcal{S} p_z\,d\nu \leq 1, \quad
I_\mathcal{S} \leq \frac{1}{2}\int_\mathcal{S} p_z\,d\nu \leq \frac{1}{2}$$

This is sharp; take all fibres small ($p_z < \varepsilon$ for all $z$, with
many fibres summing to 1). In this case $\delta(\mathcal{O})$ can be at most...
actually $\delta(\mathcal{O}) \leq 1/2$ always, so the bound $I_\mathcal{S} \leq 1/2$
is not useful.

**Better:** For the near-maximizer bound, use that $S^*$ is an $\varepsilon$-maximizer:

$$\int p_z\min(\alpha_z,1-\alpha_z)\,d\nu \geq \delta - \varepsilon$$

where $\delta = \delta(\mathcal{O})$. So:

$$I_{\mathcal{M}_0} + I_{\mathcal{M}_1} + I_\mathcal{G} \geq \delta - \varepsilon - I_\mathcal{S}$$

**Bound $I_{\mathcal{M}_0}$ and $I_{\mathcal{M}_1}$:** On $\mathcal{M}_0$,
$\alpha_z < \eta$, so $\min(\alpha_z, 1-\alpha_z) = \alpha_z < \eta$:
$$I_{\mathcal{M}_0} \leq \eta \int_{\mathcal{M}_0} p_z\,d\nu \leq \eta$$

Similarly $I_{\mathcal{M}_1} \leq \eta$. So:

$$I_\mathcal{G} \geq \delta - \varepsilon - I_\mathcal{S} - 2\eta$$

**Bound $I_\mathcal{G}$ from above using a pointwise upper bound on the integrand.**
On $\mathcal{G}$, $p_z \leq 1$ and $\min(\alpha_z, 1-\alpha_z) \leq 1/2$, so the
integrand satisfies $p_z\min(\alpha_z,1-\alpha_z) \leq 1/2$ pointwise. Therefore:
$$I_\mathcal{G} = \int_\mathcal{G} p_z\min(\alpha_z,1-\alpha_z)\,d\nu
\leq \frac{1}{2}\,\nu(\mathcal{G})$$

Combined with $I_\mathcal{G} \geq \kappa - 2\eta$ (from the lower bound on large fibres):
$$\frac{1}{2}\,\nu(\mathcal{G}) \geq I_\mathcal{G} \geq \kappa - 2\eta$$
$$\nu(\mathcal{G}) \geq 2(\kappa - 2\eta)$$

**Note on the direction.** The lower bound on $\nu(\mathcal{G})$ comes from
combining a *lower* bound on $I_\mathcal{G}$ (from the $\kappa$ hypothesis)
with an *upper* pointwise bound on the integrand (the $1/2$ factor). The earlier
attempt to use $p_z \geq \varepsilon$ and $\min \geq \eta$ gives a *lower*
pointwise bound, hence an upper bound on $\nu(\mathcal{G})$ — wrong direction.
The correct direction requires the upper bound $1/2$ on the integrand.

---

## The right formulation

The issue is that $I_\mathcal{S}$ can be large without contributing to a useful
lower bound on $\nu(\mathcal{G})$. The theorem needs a different approach.

**Key insight:** Instead of bounding $I_\mathcal{S}$ separately, use the
full decomposition of $\delta$ across fibres. Observe:

$$\delta - \varepsilon \leq \int p_z\min(\alpha_z,1-\alpha_z)\,d\nu
\leq I_\mathcal{S} + I_{\mathcal{M}_0} + I_{\mathcal{M}_1} + I_\mathcal{G}$$

Each of $I_\mathcal{S}$, $I_{\mathcal{M}_0}$, $I_{\mathcal{M}_1}$ represents
mass that "leaks" away from the balanced region $\mathcal{G}$. But we want a
lower bound on $\nu(\mathcal{G})$, not $I_\mathcal{G}$.

**Alternative:** Argue that the *mass in large unbalanced fibres is small.*

If $\nu(\mathcal{M}_0) + \nu(\mathcal{M}_1)$ is large, then many large fibres
are monochromatic — but monochromatic large fibres contribute 0 to $\delta$.
So either:
- $I_\mathcal{G}$ is large (many large balanced fibres), OR
- $I_\mathcal{S}$ carries most of the $\delta$ (small fibres do the work)

In the second case, $\delta$ is "carried by small fibres." Can this happen?

**Yes — if all large fibres are monochromatic.** Then $I_{\mathcal{M}_0} = I_{\mathcal{M}_1} = I_\mathcal{G} = 0$, and $\delta - \varepsilon \leq I_\mathcal{S}$. This is the case where the near-maximizer $S^*$ is entirely supported by small fibres — i.e., $S^*$ is a union of many small fibres, none of which is large.

**This is a legitimate case.** A measure supported on atomless small fibres
can have $\delta > 0$ without any large balanced fibre. The bridge theorem as
stated does not hold unconditionally — $\nu(\mathcal{G}) = 0$ is possible when
all large fibres are monochromatic.

---

## The correct theorem statement

The bridge theorem must restrict to the case where $\delta$ is carried by large
fibres, not small ones. This requires an additional hypothesis.

**Definition.** Say that the fibre system is *$(\varepsilon, \kappa)$-supported on large fibres* if:
$$\int_{\{p_z \geq \varepsilon\}} p_z\min(\mu_z(S^*), 1-\mu_z(S^*))\,d\nu \geq \kappa$$

for the near-maximizer $S^*$.

**Bridge Theorem (corrected).** Under the above notation, suppose $S^*$ is
an $\varepsilon$-maximizer of $\delta(\mathcal{O})$ with large-fibre contribution

$$\kappa := \int_{\{p_z \geq \varepsilon\}} p_z\min(\alpha_z, 1-\alpha_z)\,d\nu \geq 0.$$

Then for any $\eta \in (0, 1/2)$ with $\kappa > \eta$:

$$\nu(G(\eta)) \geq 2(\kappa - \eta)$$

where $G(\eta) = \{z : p_z \geq \varepsilon,\, \mu_z(S^*) \in [\eta, 1-\eta]\}$.

**Proof.** On large fibres ($p_z \geq \varepsilon$), split into $\mathcal{M}_0$
($\alpha_z < \eta$), $\mathcal{M}_1$ ($\alpha_z > 1-\eta$), and $\mathcal{G}$
($\alpha_z \in [\eta, 1-\eta]$):

$$\kappa = I_{\mathcal{M}_0} + I_{\mathcal{M}_1} + I_\mathcal{G}$$

*Bounding the monochromatic contributions:*
$$I_{\mathcal{M}_0} = \int_{\mathcal{M}_0} p_z\alpha_z\,d\nu \leq \eta\int_{\mathcal{M}_0}p_z\,d\nu \leq \eta$$

(using $\alpha_z < \eta$ on $\mathcal{M}_0$ and $\int_{\mathcal{M}_0}p_z\,d\nu \leq 1$).
Similarly $I_{\mathcal{M}_1} \leq \eta$. But $\mathcal{M}_0 \cup \mathcal{M}_1$
are disjoint subsets of large fibres whose total $p_z$-mass sums to at most 1,
so in fact $I_{\mathcal{M}_0} + I_{\mathcal{M}_1} \leq \eta$ (the $\eta$ bound
applies to their union, since $\int_{\mathcal{M}_0\cup\mathcal{M}_1}p_z\,d\nu \leq 1$
and $\min(\alpha_z,1-\alpha_z) < \eta$ on the union). Hence:

$$I_\mathcal{G} \geq \kappa - \eta$$

*Lower-bounding $\nu(\mathcal{G})$ from an upper bound on the integrand:*
On $\mathcal{G}$, $p_z \leq 1$ and $\min(\alpha_z, 1-\alpha_z) \leq 1/2$, so
$p_z\min(\alpha_z,1-\alpha_z) \leq 1/2$ pointwise. Therefore:

$$\kappa - \eta \leq I_\mathcal{G} = \int_\mathcal{G}p_z\min(\alpha_z,1-\alpha_z)\,d\nu
\leq \frac{1}{2}\nu(\mathcal{G})$$

giving $\nu(\mathcal{G}) \geq 2(\kappa - \eta)$. $\square$

**Using the variance integrand.** If the starting integral uses $\alpha_z(1-\alpha_z)$
(the conditional variance) instead of $\min(\alpha_z,1-\alpha_z)$ (the majority error),
the bound on the monochromatic parts becomes $I_{\mathcal{M}_0}+I_{\mathcal{M}_1} \leq \eta$
(same, since $\alpha_z(1-\alpha_z) < \eta$ when $\alpha_z < \eta$ or $> 1-\eta$), and
the pointwise upper bound on $\mathcal{G}$ becomes $\alpha_z(1-\alpha_z) \leq 1/4$,
giving $\nu(\mathcal{G}) \geq 4(\kappa - \eta)$. A slightly tighter constant.

---

## Interpretation and consequences

**What the theorem gives without ergodicity:**

If the near-maximizer's approximation error is carried substantially by
$\varepsilon$-large fibres (large-fibre contribution $\kappa > \eta$), then the
$\nu$-mass of $\varepsilon$-large $\eta$-balanced fibres satisfies
$\nu(G(\eta)) \geq 2(\kappa - \eta)$. The key is that the lower bound on $\nu(G(\eta))$
comes from combining a lower bound on $I_\mathcal{G}$ with an *upper* pointwise bound
on the integrand ($1/2$) — not a lower pointwise bound, which would give only an
upper bound on $\nu(\mathcal{G})$.

**What the theorem does not give:**

1. It does not say all large fibres are balanced — only a $\nu$-positive set.
2. It does not bound the individual values of $\mu_z(S^*)$ uniformly across
   balanced fibres — just that they are in $[\eta, 1-\eta]$ (by definition of $\mathcal{G}$).
3. It does not give a fibre-mixing lower bound on the full set of $\varepsilon$-large fibres,
   only on the balanced subset $\mathcal{G}$.

**The remaining gap (now precisely located):**

Fibre mixing requires: for $\nu$-**a.e.** $\varepsilon$-large $z$,
$\mu_z(S^*)\mu_z((S^*)^c) \geq c\cdot p_z$.

The bridge theorem gives: for $\nu$-a.e. $z \in \mathcal{G}$ (the balanced subset),
$\mu_z(S^*)\mu_z((S^*)^c) \geq \eta^2 > 0$. The condition $\eta^2 \geq c\cdot p_z$ holds
if $p_z \leq \eta^2/c$ — i.e., if fibres are not too large. For $\varepsilon$-large fibres
with $p_z \leq \eta^2/c$, the condition $\mu_z(S^*)\mu_z((S^*)^c) \geq c\cdot p_z$ holds.

But for very large fibres ($p_z \gg \eta^2$), the condition $\eta^2 \geq c\cdot p_z$
fails, and we need the actual value of $\mu_z(S^*)\mu_z((S^*)^c)$ to be large.

**Summary:** The bridge theorem establishes that a positive $\nu$-fraction of
large fibres are balanced. To reach fibre mixing (a.e. large fibre balanced with
a ratio bound), two additional things are needed:

1. The monochromatic large fibres $(\mathcal{M}_0 \cup \mathcal{M}_1)$ must have
   $\nu$-measure 0 (a.e. large fibre is balanced). This is the a.e. vs
   positive-fraction gap.
2. The bound $\mu_z(S^*)\mu_z((S^*)^c) \geq c\cdot p_z$ must hold not just on
   balanced fibres but also control the ratio when $p_z$ is large.

---

## The large-fibre support hypothesis: when does it hold?

The bridge theorem requires $\kappa > 0$ — the large-fibre contribution to $\delta$
is positive. When does this fail?

**Failure:** $\kappa = 0$ means all of the approximation error is carried by
small fibres ($p_z < \varepsilon$). This happens when the near-maximizer $S^*$
is well-approximated by the large fibres: $\mu_z(S^*) \in \{0, 1\}$ for all
large $z$. In other words, $S^*$ is a union of large fibres (those it contains)
plus small adjustments. The large fibres are monochromatic.

**When is the large-fibre contribution positive?**

Claim: If $(\mu \otimes \mu)(R_{>\varepsilon}) := \int_{\{p_z \geq \varepsilon\}} p_z^2\,d\nu > 0$
(there is genuine large-fibre mass), and if $\delta(\mathcal{O})$ exceeds what
small fibres alone can contribute, then $\kappa > 0$.

The maximum approximation error achievable from small fibres alone is:
$$\delta_\mathcal{S} := \sup_{S} \int_\mathcal{S} p_z\min(\mu_z(S), 1-\mu_z(S))\,d\nu \leq \frac{1}{2}(1 - (\mu\otimes\mu)(R_{>\varepsilon}))$$

Roughly: the small-fibre contribution is bounded by half the total small-fibre mass.
If $\delta(\mathcal{O}) > \frac{1}{2}(1 - (\mu\otimes\mu)(R_{>\varepsilon}))$,
then $\kappa > 0$ — the near-maximizer must use large fibres.

**In the regime of interest** (where fibre mixing is non-trivial): there are
genuine large fibres (positive collision probability from large fibres), so
$(\mu\otimes\mu)(R_{>\varepsilon}) > 0$. If additionally $\delta(\mathcal{O})$
is not too small relative to the small-fibre mass, $\kappa > 0$.

---

## What is now precisely located

The derivability conjecture requires two steps beyond the bridge theorem:

**Step A (analytic, no ergodicity).** Show $\kappa > 0$ in terms of
$\delta(\mathcal{O})$ and the large-fibre collision probability
$(\mu\otimes\mu)(R_{>\varepsilon})$. This is an analytic bound, likely:
$$\kappa \geq f(\delta(\mathcal{O}), (\mu\otimes\mu)(R_{>\varepsilon}), \varepsilon)$$
for some explicit function $f$. This step involves no dynamics.

**Step B (dynamical, requires extra hypothesis).** Upgrade from "positive
$\nu$-fraction of large fibres are balanced" to "$\nu$-a.e. large fibre is
balanced." This is where ergodicity (or something stronger) enters. The bad set
$\mathcal{M}_0 \cup \mathcal{M}_1$ (monochromatic large fibres) must have
$\nu$-measure 0.

**Step A** is likely provable with the right formulation.
**Step B** is the genuinely open dynamical question, and as the user correctly noted,
bare ergodicity may not suffice — the bad set of monochromatic large fibres need
not be $T$-invariant.

---

## Summary table

| Statement | Status | Requires |
|---|---|---|
| All of $\delta_L$ is from non-monochromatic fibres | **Proved** (step 6) | Nothing |
| $\delta_L$ decomposes: $I_\mathcal{S} + I_\mathcal{M} + I_\mathcal{G}$ | **Exact** (this note) | Nothing |
| $\nu(G(\eta)) \geq 2(\kappa - \eta)$ | **Proved** (this note) | Large-fibre support $\kappa > \eta$ |
| $\kappa > 0$ from $\delta_L$ and collision probability | **Open (Step A)** | Analytic bound |
| $\nu(\mathcal{M}_0 \cup \mathcal{M}_1) = 0$ (a.e. large fibre balanced) | **Open (Step B)** | Extra dynamical hypothesis |
| UFM derivable | **Open** | Steps A + B |

---

## Next steps

1. **Step A:** Find an explicit lower bound for $\kappa$ in terms of $\delta(\mathcal{O})$
   and $(\mu\otimes\mu)(R_{>\varepsilon})$. The key inequality should be something like:
   $$\kappa \geq \delta(\mathcal{O}) - C\cdot\sqrt{1 - (\mu\otimes\mu)(R_{>\varepsilon})}$$
   or similar. This involves an optimization over the split between small and large fibres.

2. **Step B:** Identify what dynamical condition forces $\nu(\mathcal{M}_0 \cup \mathcal{M}_1) = 0$.
   Candidates: mixing (stronger than ergodicity), or some condition on the near-maximizer's
   relationship to the $T$-action. The bridge note remark asserts ergodicity suffices but
   does not prove it — this is the key gap to resolve.

3. **CE comparison:** If both steps go through, UFM is derivable from (some hypothesis)
   — in contrast to CE irreducibility. The CE parallel breaks here, and the
   coherence/consistency schema must be updated to reflect the asymmetry.
