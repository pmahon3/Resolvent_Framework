# Step 6 — The Derivability Question

*2026-04-20*

**Status:** Bridge note proof read carefully. Exact condition extracted. The
derivability question is now precisely posed. A positive argument sketched;
failure mode identified. Genuine gap remains.

---

## What the proof actually requires

From the bridge note (Theorem 3.1 and its proof):

**Bound:**
$$(\mu \otimes \mu)(R_L) \leq \frac{1}{c}\,\delta_L + \frac{1+c}{c}\,\varepsilon$$

where $S^*$ is an $\varepsilon$-maximizer of $\delta_L$ and $S^*$ is
$(c, \varepsilon)$-mixing across fibres.

**Corollary 3.2 proof:** Takes $\varepsilon_k \to 0$ and $\varepsilon_k$-maximizers
$S^*_k$, each $(c, \varepsilon_k)$-mixing with the **same** $c > 0$. This gives
$(\mu \otimes \mu)(R_L) \leq (1/c)\,\delta_L$, so $(\mu \otimes \mu)(R_L) \to 0$
when $\delta_L \to 0$.

**The precise condition the corollary needs** (extracted from the proof):

> There exists a single $c > 0$ (possibly depending on $L$) such that for
> all small enough $\varepsilon > 0$, every $\varepsilon$-maximizer of $\delta_L$
> is $(c, \varepsilon)$-mixing.

If $c = c_L$ depends on $L$, then:
$$(\mu \otimes \mu)(R_L) \leq \frac{\delta_L}{c_L} + \frac{1+c_L}{c_L}\,\varepsilon_k \xrightarrow{\varepsilon_k \to 0} \frac{\delta_L}{c_L}$$

For $(\mu \otimes \mu)(R_L) \to 0$ as $L \to \infty$, it suffices that $\delta_L/c_L \to 0$.

**This weakens UFM:** we do not need $c_L$ to be bounded below uniformly across
$L$ — only that $c_L$ doesn't deteriorate faster than $\delta_L$.

---

## The bridge note remark on fibre mixing vs ergodicity

From Remark 3.2 (bridge note):

> "The fibre mixing condition fails only when $S^*$ is aligned with the fibre
> structure — large fibres entirely inside or entirely outside $S^*$ — an
> 'adversarially structured' failure that ergodicity rules out but strict
> measure-theoretic conditions do not require to be impossible."

This is the key structural description of when fibre mixing fails. The failure
is not generic — it requires the near-maximizer to be "aligned" with the fibres.
Ergodicity prevents this alignment.

---

## The derivability question, precisely posed

**Question.** In the Paper IV regime (measure-preserving $(X, \mathcal{B}, \mu, T)$,
ergodic $T$, $h \in L^\infty(\mu)$): does ergodicity guarantee that for every $L$,
every $\varepsilon$-maximizer $S^*$ of $\delta_L$ is $(c_L, \varepsilon)$-mixing
with $c_L$ bounded below by a function of $\delta_L$ — specifically, with
$\delta_L/c_L \to 0$?

Equivalently: **can a near-maximizer be adversarially aligned with the fibres
in an ergodic system?**

---

## The positive argument: why ergodicity may force good mixing

**Setup.** Fix $L$ and let $S^*$ be a $\delta_L$-maximizer:
$$\mathbb{E}[\text{Var}(\mathbf{1}_{S^*} \mid \mathcal{O}_h^{(L)})] = \delta_L$$

By the conditional variance identity (Lemma 3.1 of bridge note):
$$\delta_L = \int p_z \cdot \mu_z(S^*)\mu_z((S^*)^c)\,d\nu_L(z)$$

Split over $\varepsilon$-large and small fibres:
$$\delta_L = \int_{\{p_z \geq \varepsilon\}} p_z \cdot \mu_z(S^*)\mu_z((S^*)^c)\,d\nu_L(z)
+ \int_{\{p_z < \varepsilon\}} p_z \cdot \mu_z(S^*)\mu_z((S^*)^c)\,d\nu_L(z)$$

The small-fibre term is bounded by $\varepsilon$ (since $p_z < \varepsilon$ and
$\mu_z(S^*)\mu_z((S^*)^c) \leq 1/4$, and $\int p_z\,d\nu_L = 1$):
$$\int_{\{p_z < \varepsilon\}} p_z \cdot \mu_z(S^*)\mu_z((S^*)^c)\,d\nu_L(z) \leq \varepsilon/4$$

So for small $\varepsilon < \delta_L/2$:
$$\int_{\{p_z \geq \varepsilon\}} p_z \cdot \mu_z(S^*)\mu_z((S^*)^c)\,d\nu_L(z) \geq \delta_L/2$$

This says: **if $\delta_L > 0$ and $\varepsilon < \delta_L/2$, then some $\varepsilon$-large
fibres have positive $\mu_z(S^*)\mu_z((S^*)^c)$ — the integral over large fibres
is $\geq \delta_L/2$.**

**Now apply the fibre mixing condition:** we need, for a.e. $\varepsilon$-large fibre $z$:
$$\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z$$

The integral lower bound $\geq \delta_L/2$ does NOT immediately give this a.e.
condition. It is possible that the integral concentrates on a few fibres with
large $\mu_z(S^*)\mu_z((S^*)^c)$ while most $\varepsilon$-large fibres are
monochromatic. The a.e. condition is stronger than the integral lower bound.

**The gap:** The integral argument gives "some large fibres have positive mixing
product," but fibre mixing requires "a.e. large fibres have mixing product bounded
below by $c \cdot p_z$." These are different statements.

---

## Where ergodicity intervenes

Ergodicity says: $T$ has no non-trivial invariant sets. Equivalently, the
$T$-invariant $\sigma$-algebra is trivial.

**How this constrains $\mu_z(S^*)$:** In an ergodic system, for any event $S^*$
with $\mu(S^*) \in (0,1)$ and for any lag $L$:

The conditional measure $\mu_z(S^*)$ is a function of $z \in \mathbb{R}^{L+1}$.
As $L \to \infty$, by the martingale convergence theorem:
$$\mu_z(S^*) = \mathbb{E}[\mathbf{1}_{S^*} \mid \mathcal{O}_h^{(L)}](x) \to \mathbb{E}[\mathbf{1}_{S^*} \mid \mathcal{O}_h^{(\infty)}](x)$$

where $\mathcal{O}_h^{(\infty)} = \bigvee_L \mathcal{O}_h^{(L)}$ is the tail
$\sigma$-algebra of the observable. Under reconstruction ($\delta_L \to 0$),
$\mathcal{O}_h^{(\infty)} = \mathcal{B}$ (mod null sets), so:
$$\mu_z(S^*) \to \mathbf{1}_{S^*}(x) \quad \mu\text{-a.e.}$$

**Implication:** As $L \to \infty$ (in the reconstruction regime), $\mu_z(S^*)$
converges to 0 or 1 pointwise — the conditional probabilities concentrate. This
is exactly the direction *opposite* to what fibre mixing requires. Good fibre
mixing needs $\mu_z(S^*) \in (c, 1-c)$ uniformly; reconstruction forces
$\mu_z(S^*) \to \{0,1\}$.

**This is the central tension:**
- Reconstruction $(\delta_L \to 0)$ means the fibres are becoming injective:
  each fibre is essentially a singleton, so $\mu_z(S^*) \to 0$ or $1$.
- Fibre mixing requires $\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z > 0$:
  the conditional measure must remain bounded away from both 0 and 1.

As $L \to \infty$ and reconstruction occurs, fibre mixing is forced to degrade —
the product $\mu_z(S^*)\mu_z((S^*)^c)$ collapses to 0 as fibres become singletons.

**But:** as fibres become singletons, $p_z \to 0$ as well. The condition is:
$$\frac{\mu_z(S^*)\mu_z((S^*)^c)}{p_z} \geq c$$

Both numerator and denominator go to 0; the question is the ratio.

---

## The key computation: the ratio in the reconstruction regime

In the reconstruction regime, as $L \to \infty$, fibres shrink to singletons.
Consider a specific fibre $C_z$ of measure $p_z$ straddling $S^*$ (i.e.,
$C_z \cap S^* \neq \emptyset$ and $C_z \cap (S^*)^c \neq \emptyset$). Then:

$$\mu_z(S^*) = \frac{\mu(S^* \cap C_z)}{p_z}, \quad
\mu_z((S^*)^c) = \frac{\mu((S^*)^c \cap C_z)}{p_z}$$

$$\mu_z(S^*)\mu_z((S^*)^c) = \frac{\mu(S^* \cap C_z)\,\mu((S^*)^c \cap C_z)}{p_z^2}$$

The condition $\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z$ becomes:
$$\mu(S^* \cap C_z)\,\mu((S^*)^c \cap C_z) \geq c \cdot p_z^3$$

This is a condition on how the measure $\mu$ distributes within the fibre $C_z$.
As $p_z \to 0$, the right-hand side goes to 0 faster ($p_z^3$) than the product
of internal masses ($\sim p_z^2$ if the fibre is internally balanced). So:

$$\frac{\mu(S^* \cap C_z)\,\mu((S^*)^c \cap C_z)}{p_z^3} \geq c$$

**If the fibre is internally balanced** — i.e., $\mu(S^* \cap C_z) \approx \alpha p_z$
and $\mu((S^*)^c \cap C_z) \approx (1-\alpha) p_z$ for some $\alpha \in (0,1)$
bounded away from 0 and 1 — then:
$$\frac{\alpha(1-\alpha) p_z^2}{p_z^3} = \frac{\alpha(1-\alpha)}{p_z} \to \infty$$

The condition is satisf... **wait.** This gives $\mu_z(S^*)\mu_z((S^*)^c) = \alpha(1-\alpha) \geq c$ — the condition holds trivially with $c = \alpha(1-\alpha)/4 > 0$, independent of $p_z$.

**If the fibre is monochromatic** — $\mu(S^* \cap C_z) = 0$ or $p_z$ — then
$\mu_z(S^*)\mu_z((S^*)^c) = 0 < c \cdot p_z$, so fibre mixing fails on this fibre.

**Conclusion:** The fibre mixing condition fails on a fibre if and only if that
fibre is monochromatic (entirely inside or outside $S^*$). On balanced fibres,
the condition holds with $c = \mu_z(S^*)\mu_z((S^*)^c) / p_z$, which may be
large (not small).

---

## The exact characterisation of failure

Fibre mixing fails for $S^*$ if and only if: for a positive-measure set of
$\varepsilon$-large fibres $z$, the fibre $C_z$ is monochromatic with respect
to $S^*$ — entirely inside or entirely outside $S^*$.

**Under ergodicity:** Can a near-maximizer $S^*$ have a positive-measure set of
$\varepsilon$-large monochromatic fibres?

**If it can:** fibre mixing fails for that $L$ and $S^*$.

**If it cannot:** fibre mixing holds for all near-maximizers at lag $L$, and the
derivability question has a positive answer.

**The ergodicity constraint:** A $T$-invariant set $A$ satisfies $\mu(A) \in \{0,1\}$.
Fibres $C_z$ are not $T$-invariant in general. But if a large fibre is
monochromatic (entirely inside $S^*$), and $S^*$ is a near-maximizer (close to
realizing $\sup_S \mathbb{E}[\text{Var}(\mathbf{1}_S \mid \mathcal{O}_h^{(L)})]$),
then $S^*$ is chosen adversarially — it maximizes the approximation error, not
the fibre mixing condition. It can, in principle, be chosen to be aligned with
the fibres.

---

## The adversarial event: the critical example

**Claim:** There exists a non-ergodic system where $\delta_L > 0$ for all $L$
but fibre mixing fails, and the failure is witnessed by an adversarially aligned
near-maximizer. For example:

Let $(X, \mu, T) = ([0,1], \text{Leb}, \text{id})$ (identity transformation),
$h(x) = x$. Then $\Phi_h^{(L)}(x) = (x, x, \ldots, x)$ for all $L$.
Fibres are level sets of $h$ — singletons $\{x\}$ with $p_z = 0$. No
$\varepsilon$-large fibres. Fibre mixing is vacuous. Not useful.

**Better candidate:** Let $T$ have a genuine invariant factor. Let $X = A \cup B$
with $\mu(A) = \mu(B) = 1/2$, $T(A) \subset A$ and $T(B) \subset B$ (the system
decomposes into two ergodic components). Let $h$ be constant on each component:
$h|_A = 0$, $h|_B = 1$. Then all delay vectors from $A$ are $(0,0,\ldots,0)$
and from $B$ are $(1,1,\ldots,1)$. Two fibres of equal mass $1/2$.

The near-maximizer $S^* = A$: $\mu_z(S^*) = 1$ for $z = (0,\ldots,0)$ and
$\mu_z(S^*) = 0$ for $z = (1,\ldots,1)$. Both large fibres are monochromatic.
Fibre mixing fails completely, and $\delta_L = 1/2$ for all $L$.

**But this is non-ergodic.** The question is whether ergodicity prevents this.

**In an ergodic system:** the observable $h$ must separate $\mu$-a.e. pairs
eventually (under reconstruction), so fibres shrink. The adversarial event $S^*$
at lag $L$ is the supremum of $\mathbb{E}[\text{Var}(\mathbf{1}_S \mid \mathcal{O}_h^{(L)})]$.
Can $S^*$ be chosen to be a $T$-invariant set (or close to one)?

**Key:** In an ergodic system, there are no non-trivial $T$-invariant sets. If
$S^*$ is close to a $T$-invariant set, $\mu(S^*) \in (0,1)$ but
$T^{-1}S^* \approx S^*$. For such $S^*$: the conditional measure $\mu_z(S^*)$
is approximately $\mu(S^*)$ for all fibres $z$ (because $S^*$ is spread uniformly
across the orbit). So $\mu_z(S^*)\mu_z((S^*)^c) \approx \mu(S^*)(1-\mu(S^*)) > 0$
uniformly — fibre mixing holds.

The failure would require $S^*$ to be aligned with the fibres *and* be a near-
maximizer. In an ergodic system, the near-maximizer is the "hardest to approximate"
set. Events aligned with the fibres are *easy* to approximate (they are almost
$\mathcal{O}_h^{(L)}$-measurable). So near-maximizers tend to be *mis-aligned*
with the fibres — they are the events that the observable cannot capture.

**This is the key insight:** In an ergodic system, the near-maximizer is by
definition the event hardest to approximate by $\mathcal{O}_h^{(L)}$ — the event
most different from any $\mathcal{O}_h^{(L)}$-measurable event. Such an event
tends to *cross* the fibres, not be aligned with them.

---

## Towards a proof of derivability

**Informal argument.** Suppose $S^*$ is an $\varepsilon$-maximizer of $\delta_L$
in an ergodic system. Then $S^*$ is far (in $\mu$-measure) from any
$\mathcal{O}_h^{(L)}$-measurable set. This means $S^*$ cannot be approximated
by unions of fibres — it must straddle many fibres.

More precisely: if a large fibre $C_z$ is monochromatic with respect to $S^*$
(entirely inside or outside), then replacing $S^*$ by $S^* \triangle C_z$ changes
the approximation error by at most $p_z^2$ (second-order in fibre size). So
having many monochromatic large fibres doesn't help achieve a large
approximation error — the maximizer must straddle fibres to maximize variance.

**Formal version:** Let $S^*_0$ be the $\mathcal{O}_h^{(L)}$-measurable set
closest to $S^*$: $S^*_0 = \text{argmin}_{E \in \mathcal{O}_h^{(L)}} \mu(S^* \triangle E)$.
On each fibre $C_z$: $S^*_0 \cap C_z$ is either $\emptyset$ or $C_z$ (since
$S^*_0$ is a union of fibres). The best choice is to include $C_z$ in $S^*_0$
iff $\mu_z(S^*) \geq 1/2$ (majority vote). Then:
$$\mu(S^* \triangle S^*_0) = \int p_z \cdot \min(\mu_z(S^*), \mu_z((S^*)^c))\,d\nu_L(z)$$

For this to equal $\delta_L > 0$, we need many fibres $z$ where $\min(\mu_z(S^*),
\mu_z((S^*)^c)) > 0$ — i.e., fibres that are not monochromatic. The contribution
of monochromatic fibres to $\mu(S^* \triangle S^*_0)$ is exactly $0$. So:

$$\delta_L = \int_{\text{non-monochromatic}} p_z \cdot \min(\mu_z(S^*), \mu_z((S^*)^c))\,d\nu_L(z)$$

**All of $\delta_L$ comes from non-monochromatic fibres.** Monochromatic fibres
contribute 0 to the approximation error — they are already perfectly approximated.

Now apply the fibre mixing condition on non-monochromatic fibres. For a non-
monochromatic fibre: $\mu_z(S^*), \mu_z((S^*)^c) > 0$, so
$\mu_z(S^*)\mu_z((S^*)^c) > 0$. The question is whether this product is bounded
below by $c \cdot p_z$.

---

## The quantitative question

For a non-monochromatic fibre $C_z$ with $\mu_z(S^*) = \alpha_z \in (0,1)$:
$$\mu_z(S^*)\mu_z((S^*)^c) = \alpha_z(1-\alpha_z) \geq 4\min(\alpha_z, 1-\alpha_z)^2$$

The fibre mixing condition requires $\alpha_z(1-\alpha_z) \geq c \cdot p_z$.

This holds (for some $c > 0$) if and only if $\alpha_z$ is bounded away from 0
and 1 on a positive-measure set of large fibres, *with the bound uniform in $c$.*

**Can $\alpha_z$ approach 0 on all large fibres in an ergodic reconstructing system?**

If $\alpha_z = \mu_z(S^*) \to 0$ for $\nu_L$-a.e. large fibre, then almost all
mass of $\mu(S^* \cap C_z)$ concentrates on small fibres. The total mass of
$S^*$ in large fibres is:
$$\int_{\{p_z \geq \varepsilon\}} \mu_z(S^*) p_z\,d\nu_L(z) = \int_{\{p_z \geq \varepsilon\}} \mu(S^* \cap C_z)\,d\nu_L(z) \to 0$$

But the total mass of large fibres is $\int_{\{p_z \geq \varepsilon\}} p_z\,d\nu_L(z) = (\mu \otimes \mu)(R_L^{>\varepsilon}) \geq (\mu \otimes \mu)(R_L) - \varepsilon$.

So if $\alpha_z \to 0$ on large fibres, then $\mu(S^*)$ is concentrated on small
fibres, meaning $S^*$ is essentially a union of small fibres. But then $S^*$ is
approximately $\mathcal{O}_h^{(L)}$-measurable (since small fibres contribute
little to the approximation error), contradicting $S^*$ being a near-maximizer
with $\delta_L > \varepsilon$.

**This gives a contradiction:** if $\delta_L > 2\varepsilon$ and $S^*$ is an
$\varepsilon$-maximizer, then $\mu_z(S^*)$ cannot approach 0 or 1 on all large
fibres — some positive fraction of large fibres must have $\alpha_z$ bounded
away from 0 and 1.

---

## A sketch of the derivability result

**Proposition (informal, to be made rigorous).** Let $(X, \mathcal{B}, \mu, T)$
be any measure-preserving system (not necessarily ergodic). Let $S^*$ be an
$\varepsilon$-maximizer of $\delta_L$ with $\delta_L > 4\varepsilon$. Then:

$$\nu_L\bigl(\{z : p_z \geq \varepsilon,\; \mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z\}\bigr) \geq C(\delta_L, \varepsilon)$$

for some explicit $c, C > 0$ depending on $\delta_L$ and $\varepsilon$.

In particular: if $\delta_L > 0$ is bounded below, then some positive fraction
of large fibres satisfies the fibre mixing condition — the condition holds on
a positive-measure set of fibres (but not necessarily a.e.).

**The a.e. condition:** The fibre mixing definition requires the condition to hold
for $\nu_L$-**a.e.** $\varepsilon$-large fibre, not just a positive fraction.
The argument above gives "positive fraction" but not "a.e." The gap between
"positive fraction" and "a.e." is exactly where ergodicity (or some other
condition) would be needed.

**Ergodicity and the a.e. condition.** In an ergodic system: the conditional
measures $\mu_z(S^*)$ are controlled by the orbit structure of $T$. An ergodic
argument (e.g., the ergodic theorem applied to the sequence of $\mu_z(S^*)$ values)
might show that the fraction of monochromatic fibres cannot be positive for
a near-maximizer — ergodicity prevents the fibre system from having a full
component of aligned large fibres.

**This is the remaining gap:** the argument shows "positive fraction straddles"
but not "a.e. straddles." The a.e. condition likely requires ergodicity. This
is where the bridge note remark lives: "an adversarially structured failure that
ergodicity rules out."

---

## Summary and status

| Claim | Status |
|---|---|
| All of $\delta_L$ comes from non-monochromatic fibres | **Proved** (exact computation above) |
| Near-maximizer must have $\alpha_z$ bounded from 0/1 on a positive fraction of large fibres | **Sketched** (follows from $\delta_L > 2\varepsilon$ and near-maximizer property) |
| The positive fraction is a.e. | **Open** — this is where ergodicity intervenes |
| Ergodicity prevents monochromatic large fibres for near-maximizers | **Bridge note remark asserts this; proof not given in current papers** |
| UFM is derivable from ergodicity + reconstruction | **Plausible but not proved** |
| UFM is irreducible (not derivable) | **No longer the leading hypothesis** |

---

## Next step

The key open gap is: does ergodicity force $\alpha_z = \mu_z(S^*)$ to be bounded
away from 0 and 1 for $\nu_L$-**a.e.** large fibre, when $S^*$ is a near-maximizer?

A natural approach: use the ergodic theorem to show that for a typical orbit point
$x$, the fibre $C_z$ through $x$ has $\mu_z(S^*)$ close to $\mu(S^*)$ — i.e.,
fibres are "representative" of the global measure. This would give
$\mu_z(S^*) \approx \mu(S^*) \in (0,1)$ for a.e. large fibre, hence
$\alpha_z(1-\alpha_z) \approx \mu(S^*)(1-\mu(S^*)) > 0$ — fibre mixing holds
with $c \approx \mu(S^*)(1-\mu(S^*))/4$.

**The argument:** In an ergodic system, by the ergodic theorem, for $\mu$-a.e.
$x$ and any $S^*$:
$$\frac{1}{n}\sum_{k=0}^{n-1} \mathbf{1}_{S^*}(T^k x) \to \mu(S^*)$$

The conditional measure $\mu_z(S^*)$ on the fibre $C_z$ containing $x$ is not
directly the time average, but it is related to the distribution of the orbit
within the fibre structure. Formalizing this connection is the next task.
