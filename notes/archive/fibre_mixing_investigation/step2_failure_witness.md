# Step 2 — Candidate Failure Witnesses

*2026-04-20*

**Status:** Framing B witness likely easy (infinitary quantifier argument); pivots
to harder dynamical question. Both outcomes recorded here.

---

## What a failure witness must do

A witness for framing B irreducibility is a compatible charge family
$\{\mu_i\}$ on a cylinder algebra $\mathcal{C}$ that:

1. Satisfies every *finitary structural condition* — normalization,
   compatibility with refinement maps, finite additivity, conditional
   consistency across coarsenings
2. Fails fibre mixing: for every candidate event $S^* \in \mathcal{C}$, the
   condition $\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z$ fails on a set of
   fibres of positive $\nu_L$-measure (for every $c > 0$)

The same quality requirement as the finite-cofinite charge: the witness must
satisfy every finitary condition that genuine dynamical systems satisfy, not
just be a degenerate case.

---

## Framing B: precise structural conditions

The finitary structural conditions on a compatible charge family
$\{\mu_i\}_{i \in \iota}$ are:

**(FC1) Normalization:** $\mu_i(\mathsf{O}_i) = 1$ for all $i$.

**(FC2) Finite additivity:** $\mu_i(A \cup B) = \mu_i(A) + \mu_i(B)$ for
disjoint $A, B \in \mathcal{C}_i$.

**(FC3) Compatibility:** $\mu_i = \mu_j \circ \pi_{ij}^{-1}$ for $i \leq j$
(charges commute with refinement maps).

**(FC4) Conditional consistency:** For the lag-$L$ partition $\{C_z\}$, the
conditional charges $\mu_z(\cdot) = \mu(\cdot \mid C_z)$ are themselves
finitely additive and satisfy: for $i \leq j$ and $z$ a lag-$j$ fibre
sitting inside lag-$i$ fibre $z'$,
$$\mu_z(A) = \mu_{z'}(A \cap C_z) / \mu_{z'}(C_z)$$
whenever $\mu_{z'}(C_z) > 0$.

These are the conditions expressible in finite observational windows. Note
that **(FC4)** is the key condition: it says the conditional structure is
internally consistent across refinements. Nothing in (FC1)–(FC4) controls the
behaviour of $\mu_z(S^*)$ as the fibre $z$ varies or as $L \to \infty$.

---

## The witness: a degenerate compatible charge family

**Construction.** Let the index set $\iota = \mathbb{N}$ (lag parameter),
outcome space $\mathsf{O} = [0,1]$, so at lag $L$ the cylinder partition
consists of cells $C_z = [z \cdot 2^{-L}, (z+1) \cdot 2^{-L})$ for
$z \in \{0, 1, \ldots, 2^L - 1\}$.

Define the charge on the lag-$L$ cylinder algebra by:
$$\mu_L(C_z) = 2^{-L} \quad \text{(uniform, for all } z \text{)}$$

so $\nu_L$ is the uniform distribution on $2^L$ fibres (each has equal mass).

Now define the conditional measure $\mu_z$ on each fibre $C_z$ by:

$$\mu_z(\cdot) = \delta_{z \cdot 2^{-L}}(\cdot) \quad
\text{(Dirac mass at the left endpoint of } C_z \text{)}$$

More precisely: within fibre $C_z$, put all mass at the single point
$z \cdot 2^{-L}$. The full charge is:

$$\mu = \sum_z 2^{-L} \cdot \delta_{z \cdot 2^{-L}}$$

i.e., the uniform distribution on the $2^L$ dyadic rationals of level $L$.

**Does this satisfy (FC1)–(FC4)?**

- (FC1): $\mu([0,1]) = 1$. Yes.
- (FC2): Finite additivity. Yes, $\mu$ is a finitely additive probability.
- (FC3): Compatibility. At lag $L-1$, each cell $C_{z'}$ at level $L-1$
  contains two level-$L$ cells $C_{2z'}$ and $C_{2z'+1}$, each with mass
  $2^{-L}$. So $\mu_{L-1}(C_{z'}) = 2^{-(L-1)}$. Compatibility holds.
- (FC4): Conditional consistency. Given lag-$L$ fibre $C_z$, the conditional
  measure is $\delta_{z \cdot 2^{-L}}$. Given lag-$(L-1)$ fibre $C_{z'}$
  containing $C_z$ and $C_{z+1}$ (assuming $z$ even), the conditional measure
  is $\delta_{z' \cdot 2^{-(L-1)}}$. Nested conditionality: $\mu_z = \mu_{z'}$
  restricted to $C_z$ and normalized — but $\mu_{z'}$ puts mass at
  $z' \cdot 2^{-(L-1)} = z \cdot 2^{-L}$, so if this falls in $C_z$, the
  conditional is $\delta_{z \cdot 2^{-L}}$, consistent. (FC4) holds at each
  finite lag.

**Does it fail fibre mixing?**

For any event $S^* = [a, b) \subset [0,1]$ with $\mu(S^*) \in (0,1)$:

At lag $L$, the conditional measure on fibre $C_z$ is $\delta_{z \cdot 2^{-L}}$.
So $\mu_z(S^*) \in \{0, 1\}$ — either the Dirac point falls in $S^*$ or it
doesn't. Thus:

$$\mu_z(S^*)\mu_z((S^*)^c) = 0 \quad \text{for every fibre } z.$$

But $p_z = 2^{-L} > 0$, so the condition $\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z$
fails for every $c > 0$ and every $S^*$ that is a proper interval. Fibre
mixing fails completely — for every event.

**Assessment:** This is a valid framing B witness. The compatible charge
family satisfies all four finitary structural conditions. The conditional
measures are atomic (Dirac masses), making fibre mixing trivially fail for
every non-trivial event.

---

## Is the witness too cheap?

**The concern** (from the CE parallel): the finite-cofinite charge works as
a CE witness because it satisfies every first-order property that
$\sigma$-additive measures satisfy. Does the Dirac-on-dyadic-rationals charge
satisfy every first-order property that dynamical systems with fibre mixing
satisfy?

The answer is **no** — and this is the key point. The Dirac conditional
measures above fail a simple first-order property of dynamical systems: any
system with a non-trivial ergodic component has conditional measures that are
non-atomic on non-trivial $\sigma$-algebras. The witness is too thin.

This suggests framing B irreducibility, while provable by the above, may not
be the interesting result. The witness is essentially a degenerate Dirac
family that no reasonable dynamical system would produce.

**Conclusion:** Framing B irreducibility is provable but cheap. The
interesting question is at the level of framing A (dynamical language).

---

## The pivot to framing A

The real question is: is fibre mixing derivable from any first-order condition
in the dynamical language $\mathcal{L}_{\mathrm{dyn}}$ — the language of
measure-preserving systems $(X, \mathcal{B}, \mu, T, h)$?

Specifically: is there a first-order sentence $\phi \in \mathcal{L}_{\mathrm{dyn}}$
such that $\phi \implies$ fibre mixing? If no such $\phi$ exists, fibre mixing
is genuinely irreducible at the dynamical level.

**Why this is hard.** Fibre mixing involves:
- A limit as $L \to \infty$ (or: for all large $L$)
- A quantifier over events $S^*$
- Conditional measures on fibres (which are not standard first-order objects)
- A uniform lower bound $c > 0$

The conditional measure $\mu_z(S^*)$ is not obviously expressible as a
first-order formula in a standard dynamical language. This is the structural
obstacle that makes the CE parallel non-trivial.

---

## The infinitary quantifier structure

Both CE and fibre mixing are *infinitary* conditions:

- **CE:** $\mu(\bigcap_k A_k) = \lim_k \mu(A_k)$ for all decreasing sequences
  $A_k \searrow \emptyset$. This involves a quantifier over countably many sets
  and a limit — not first-order.

- **Fibre mixing:** For all large $L$, for $\nu_L$-a.e. $z$, for the event
  $S^*$: $\mu_z(S^*)\mu_z((S^*)^c) \geq c \cdot p_z$. This involves:
  - Quantification over $L$ (countably many lags)
  - An a.e. quantifier over fibres (not finitely checkable)
  - Conditional measures (defined as limits or quotients)

**In both cases, the condition escapes any finitary first-order axiomatization.**
The CE argument makes this precise: Łoś's theorem plus the finite-cofinite
counterexample shows that no first-order theory can force CE. For fibre mixing,
the same logic applies at the dynamical level — but the construction of the
analogue of the finite-cofinite charge is the open problem.

---

## What the dynamical failure witness must look like

For a dynamical-level irreducibility result, the witness needs to be:

**(W1)** A sequence of dynamical systems $(X_n, \mathcal{B}_n, \mu_n, T_n, h_n)$
each satisfying fibre mixing.

**(W2)** An ultraproduct $\mathcal{U}$-$\lim (X_n, T_n, \mu_n, h_n)$ that
fails fibre mixing.

**(W3)** Every first-order sentence in $\mathcal{L}_{\mathrm{dyn}}$ satisfied
by all $(X_n, \ldots)$ is also satisfied by the ultraproduct (Łoś's theorem).

The obstacle: the ultraproduct of dynamical systems is not a standard
measure-preserving system — it is a nonstandard model. And fibre mixing, as
an infinitary condition on conditional measures, is not obviously preserved
under ultraproducts (which preserve only first-order properties).

**The natural candidate for $(X_n, T_n, \mu_n, h_n)$:** a sequence of
ergodic systems with fibre mixing, whose ultraproduct produces a system where
conditional measures on fibres are degenerate (Dirac-like). If such a
sequence exists, the Łoś argument closes the proof.

---

## Natural candidate sequence

Let $X_n = [0,1]^{\mathbb{Z}}$ (the full shift space), $T_n = $ shift,
$\mu_n = $ a $T_n$-ergodic measure with good mixing properties, and
$h_n : x \mapsto x_0$ (the zero-coordinate observable).

Each $(X_n, T_n, \mu_n, h_n)$ is ergodic, hence satisfies fibre mixing.

As $n \to \infty$, let the ergodic measures $\mu_n$ converge weak-* to a
measure $\mu_\infty$ that is not ergodic — e.g., a convex combination of
two ergodic measures. Or: let $\mu_n$ concentrate on an increasingly fine
periodic orbit, so the limit is an atomic measure.

**Assessment:** If $\mu_\infty$ is atomic (supported on a single orbit),
the conditional measures on fibres of $\Phi_h^{(L)}$ are eventually Dirac
masses, and fibre mixing fails. The question is whether the ultraproduct
(which need not equal the weak-* limit) has the same property.

This is the key open construction. It requires:
1. Showing the ultraproduct of ergodic systems with fibre mixing can fail
   fibre mixing
2. Verifying this is a genuine first-order consequence of the individual
   properties, not a second-order artifact

---

## Summary and status

| Question | Status |
|---|---|
| Framing B irreducibility | **Provable** (Dirac-conditional witness); but witness is too cheap |
| Framing A irreducibility | **Open** — requires dynamical ultraproduct construction |
| Failure witness quality | Needs (W1)–(W3) with non-degenerate individual systems |
| Łoś argument transfer | Blocked by non-first-order nature of conditional measures |

**The investigation pivots here.** The real content is:

> Is there a sequence of measure-preserving systems each satisfying fibre
> mixing whose ultraproduct (in the sense of nonstandard analysis) fails
> fibre mixing?

If yes: fibre mixing is not first-order axiomatizable in $\mathcal{L}_{\mathrm{dyn}}$.
If no: fibre mixing may be a consequence of some first-order condition that
is preserved under ultraproducts.

**Key technical obstacle:** Fibre mixing involves conditional measures, which
are not first-order expressible in standard model-theoretic terms. The right
formalism may be continuous logic (for metric structures) rather than
classical first-order logic.

---

## Next steps

1. Investigate whether conditional measures are expressible in continuous logic
   for metric structures (the right framework for measure-preserving systems)
2. Look for a Keisler-type compactness argument: if fibre mixing has a
   finitary approximation schema, its failure can be witnessed by an
   ultraproduct
3. Check whether the direct-product example (Step 1, Check 2) gives the
   required sequence: direct products of ergodic systems are non-ergodic but
   satisfy fibre mixing; can an ultraproduct of direct products fail fibre
   mixing?
4. Assess whether "fibre mixing" is expressible as an approximate formula in
   continuous logic — if so, Łoś's theorem for metric structures (Ben Yaacov
   et al.) applies directly
