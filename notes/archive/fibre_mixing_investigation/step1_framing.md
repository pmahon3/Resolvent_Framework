# Step 1 — Fixing the Framing

*2026-04-20*

**Status:** In progress. Two prerequisite checks before framing B is locked.

---

## The load-bearing choice

Framing B (finitary observational / query-level derivability) is the natural
analogue of the CE setting. But before committing to it, two checks are needed:

1. Is fibre mixing expressible in query-system language?
2. Is there a genuine gap between ergodicity and fibre mixing?

If (1) fails, framing B is vacuous (fibre mixing isn't even a query-level
condition, so derivability from query-level structure is trivially impossible).
If (2) fails, the question collapses to whether ergodicity is derivable, which
is a different and already-studied question.

---

## Check 1: Fibre mixing in query-system language

Recall the query-system setup (Paper I): an index set $\iota$, outcome spaces
$\mathsf{O}_i$, refinement maps $\pi_{ij}$, evaluation maps $\mathrm{eval}_i :
\Omega \to \mathsf{O}_i$, and a compatible family of charges $\{\mu_i\}$ on
the cylinder algebra $\mathcal{C}$.

At lag $L$, the delay query system produces:
- The delay map $\Phi_h^{(L)} : \Omega \to \mathsf{O}^L$ (joint outcome at
  lags $0, 1, \ldots, L-1$)
- The lag-$L$ cylinder partition: $\{C_z\}_{z \in \mathsf{O}^L}$ where
  $C_z = \{\omega : \Phi_h^{(L)}(\omega) = z\}$
- Fibre masses: $p_z = \mu(C_z)$ — these are values of the compatible charge
  on cylinder sets, hence **query-system data**
- Conditional measures: $\mu_z(\cdot) = \mu(\cdot \mid C_z)$ — conditionals
  given cylinder sets, hence **also query-system data** (conditional on the
  cylinder partition)

So fibre mixing involves:
- $\nu_L$ = distribution of $\Phi_h^{(L)}$: determined by $\{p_z\}$, which
  are charges on cylinder sets — **query-system data**
- $\mu_z(S^*)$: conditional measure of $S^*$ given fibre $C_z$ — expressible
  as $\mu(S^* \cap C_z)/\mu(C_z)$, which depends on charges on cylinder
  intersections — **query-system data**
- The condition $\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z$: a condition on
  ratios of cylinder charges

**Conclusion:** Fibre mixing *is* expressible in query-system language —
specifically in terms of the conditional structure of the compatible charge
family on the lag-$L$ cylinder partition.

**But the structural data available is richer than in the CE case:**
- CE: Boolean algebra + normalized finitely additive charge (marginal structure)
- Fibre mixing: same, plus conditional structure on the lag-$L$ partition

This means a "structural condition" in framing B could in principle involve
conditional charges, not just marginal ones. The framing B question is:

> Is fibre mixing derivable from the finitary conditional structure of the
> compatible charge family — i.e., from cylinder charges and their
> conditionals on lag-$L$ partitions — without reference to the global
> dynamics?

This is the right version of framing B.

---

## Check 2: Gap between ergodicity and fibre mixing

**Known:** ergodicity implies fibre mixing (Paper IV, Definition 5.1 remark).

**Question:** Does fibre mixing hold for any non-ergodic system?

**A candidate non-ergodic system satisfying fibre mixing:**

Let $(X, \mathcal{B}, \mu, T)$ be a direct product of two ergodic systems:
$X = X_1 \times X_2$, $\mu = \mu_1 \otimes \mu_2$, $T = T_1 \times T_2$.

The system is non-ergodic (the factor $\sigma$-algebras $\mathcal{B}_1 \otimes
\{\emptyset, X_2\}$ and $\{\emptyset, X_1\} \otimes \mathcal{B}_2$ are both
$T$-invariant).

Choose $h : X \to \mathbb{R}$ that separates points in both factors —
e.g., $h(x_1, x_2) = h_1(x_1) + \alpha h_2(x_2)$ for $\alpha$ irrational,
with $h_1, h_2$ cyclic for $T_1, T_2$ respectively.

At large lag $L$, the delay vectors $\Phi_h^{(L)}(x)$ separate points in
both factors (by the reconstruction theorem applied to each factor). The
fibres of $\Phi_h^{(L)}$ are singletons or near-singletons in both
coordinates.

For an event $S^* = S_1 \times X_2$ with $\mu_1(S_1) \in (0,1)$:
- $\mu_z(S^*) \approx \mu_1(S_1)$ for fibres $z$ that separate $x_1$
- $\mu_z((S^*)^c) \approx 1 - \mu_1(S_1)$
- $p_z \approx$ small (fibres are near-singletons)

So $\mu_z(S^*)\mu_z((S^*)^c) \approx \mu_1(S_1)(1-\mu_1(S_1)) > 0$, while
$c \cdot p_z \to 0$. The condition $\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z$
is satisfied for small enough $p_z$.

**Tentative conclusion:** A direct product of two ergodic systems is
non-ergodic but satisfies fibre mixing (at large enough lag). This would
confirm the gap exists.

**But:** this argument is informal and needs verification. The key issue is
whether the constant $c$ can be chosen uniformly across fibres, or whether
it depends on $z$ in a way that prevents uniform $(c,\varepsilon)$-mixing.

---

## A candidate non-ergodic system failing fibre mixing

The more interesting question for irreducibility: is there a system that
satisfies every finitary structural condition on the query system yet fails
fibre mixing?

**Candidate:** Let $T = \mathrm{id}$ (the identity transformation).

Then $\Phi_h^{(L)}(x) = (h(x), h(x), \ldots, h(x))$ for all $L$ — the
delay map is constant along all lags. The fibre over $z = (h(x), \ldots)$
is the level set $\{x' : h(x') = h(x)\}$.

If $h$ is not injective, fibres have positive measure. Then:
- $p_z = \mu(\{h = z_0\})$ for $z = (z_0, z_0, \ldots)$
- $\mu_z(S^*) = \mu(S^* \cap \{h = z_0\})/\mu(\{h = z_0\})$

For fibre mixing to hold, we need an $S^*$ with
$\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z$ for a.e. large fibre.

If $h$ is a.e. constant (constant observable), then all of $\Omega$ is one
fibre, $p_z = 1$, and we need $\mu(S^*)\mu((S^*)^c) \geq c$ — which holds
for any event with $\mu(S^*) \in (c, 1-c)$. Fibre mixing is trivially
satisfied.

If $h$ takes many values, fibres are level sets of $h$. Fibre mixing
requires an event that mixes *within* each level set. For $T = \mathrm{id}$,
the dynamics are trivial — no mixing across fibres occurs — but fibre mixing
is a condition on the event $S^*$, not on the dynamics. It can still be
satisfied if $S^*$ cuts each fibre in a balanced way.

**Assessment:** $T = \mathrm{id}$ does not immediately give a failure witness.
The condition is on the event $S^*$, which can be chosen to satisfy fibre
mixing even with trivial dynamics. This suggests fibre mixing is more about
the observable and the measure than about the dynamics per se.

---

## Revised picture

Fibre mixing may be better understood as a condition on the pair $(h, \mu)$
than on $T$ alone. The dynamics $T$ enter only through $\delta(L)$ (the
algebraic error) — fibre mixing is what makes $\delta(L)$ track $H_2(\nu_L)$.

This shifts the irreducibility question: not "is fibre mixing not derivable
from the dynamics?" but "is fibre mixing not derivable from the observable
and the compatible charge family?"

A failure witness would be a pair $(h, \mu)$ with:
- All finitary structural conditions satisfied (compatible charges, cylinder
  algebra, normalization)
- Fibre mixing fails for every event $S^*$ in a residual set of fibres

The natural target: a measure that is pathologically concentrated on a
small set of level sets of $h$, making $p_z$ large for those $z$ but
$\mu_z(S^*)\mu_z((S^*)^c)$ small because the conditional measures are
degenerate.

---

## Next steps

1. Verify the direct-product example rigorously — does it satisfy fibre
   mixing, and does $c$ exist uniformly?
2. Look for a measure/observable pair where conditional measures on fibres
   are degenerate — this is the natural failure witness candidate
3. State precisely what "structural conditions on the query system" means
   in framing B, now that we know conditional structure is available

**Key question to answer next:** Can a compatible charge family have
degenerate conditional measures on the lag-$L$ cylinder partition while
satisfying every finitary structural condition? If yes, that is the failure
witness.
