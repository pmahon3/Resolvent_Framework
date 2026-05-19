# Tail Decay and Graded Sigma-Additivity

**Status: PARKED (2026-05-18).** Phase 2 audit failed. The central
thesis — a single graded parameter interpolating light tails →
heavy tails → PFA — is contradicted by Schervish-Seidenfeld-Kadane
(2021), who show that improper-distribution limits (interior tail
behavior) and FAP limits (boundary mass) are independent
characteristics, not endpoints of one axis. The
supremum-over-refinements definition collapses to {0, ∞} (recovers
only the binary Halmos dichotomy). The filtration-dependent version
is Rényi information dimension under a different name. The candidate
theorem restates definitions. Taxonomic — no new mathematics.

---

## The question

Sigma-additivity is a binary condition: either $\mu(E_n) \to 0$
whenever $E_n \searrow \emptyset$, or it doesn't.  But the
*rate* at which $\mu(E_n) \to 0$ varies enormously among
$\sigma$-additive measures, and the extreme case where
$\mu(E_n) \not\to 0$ is precisely pure finite additivity.

Heavy-tailed distributions ($\alpha$-stable laws, regularly
varying tails) are $\sigma$-additive measures on $\mathbb{R}$
whose tail decay $\mu(\{|X| > t\}) \sim t^{-\alpha}$ is slow.
Purely finitely additive charges are measures whose "tails"
never decay at all --- they assign persistent mass to
arbitrarily remote events.

**Is there a formal graded parameter interpolating between fast
tail decay ($\sigma$-additive, light tails), slow tail decay
($\sigma$-additive, heavy tails), and no tail decay (purely
finitely additive)?  And is any such parameter invariant under
the choice of refinement structure, or is it
observer-dependent?**

---

## Known ingredients

Three classical results together establish the conceptual axis.
None is new; the question is whether their conjunction says
something none says alone.

### Halmos characterization (1950)

A finitely additive charge $\mu$ on an algebra $\mathcal{A}$ is
$\sigma$-additive if and only if $E_n \searrow \emptyset$ implies
$\mu(E_n) \to 0$.  This is the qualitative end of the axis: a
binary yes/no.

### Yosida-Hewitt decomposition (1952)

Every bounded finitely additive charge decomposes uniquely as
$\mu = \mu_c + \mu_p$ where $\mu_c$ is $\sigma$-additive and
$\mu_p$ is purely finitely additive (vanishes on every set
where a $\sigma$-additive measure could concentrate).

The decomposition gives a "distance from $\sigma$-additivity"
in a crude sense: the total variation $\|\mu_p\|$ measures how
much mass is purely finitely additive.  But this is a single
number, not a rate.

### Stone-Cech support theorem (Dunford-Schwartz 1958)

Under the isometric identification $\text{ba}(\mathbb{N})
\cong M(\beta\mathbb{N})$:
- $\sigma$-additive measures correspond to measures supported
  on $\mathbb{N}$ (the isolated / principal ultrafilter points);
- purely finitely additive measures correspond to measures
  supported on $\beta\mathbb{N} \setminus \mathbb{N}$ (the
  remainder --- "points at infinity").

So PFA = mass at infinity.  This is a theorem.

### Dubins (1977)

"Measurable tail disintegrations of the Haar integral are purely
finitely additive."  When you disintegrate a $\sigma$-additive
measure with respect to the tail $\sigma$-field, the conditional
measures are PFA.  The tail field *sees* the purely finitely
additive component.

This is the contrapositive direction: tail structure forces
finite additivity in the disintegration.

### Schervish-Seidenfeld-Kadane (2021)

When a sequence of $\sigma$-additive probabilities converges:
- the improper-distribution limit captures interior behavior;
- the finitely additive limit captures mass escaping to the
  boundary.

These two phenomena are independent.

---

## What this is NOT

- It is not the Yosida-Hewitt decomposition (which is binary:
  $\sigma$-additive part vs PFA part).
- It is not the Halmos characterization (which is qualitative:
  $\mu(E_n) \to 0$ or not).
- It is not the Stone-Cech support theorem (which is
  topological: support on $\mathbb{N}$ vs
  $\beta\mathbb{N} \setminus \mathbb{N}$).
- It is not the regular-variation theory of heavy tails (which
  works entirely within $\sigma$-additive measures on
  $\mathbb{R}$).

The question is whether there is a *graded* invariant that
unifies the axis: light tails $\longleftrightarrow$ heavy tails
$\longleftrightarrow$ PFA, using the rate of tail decay as the
parameter.

---

## The refinement-dependence problem

On $\mathbb{R}$ with Borel sets, "tail decay" has a canonical
meaning: $\mu(\{|X| > t\})$ as $t \to \infty$.  The parameter
$\alpha$ in $\mu(\{|X| > t\}) \sim t^{-\alpha}$ is
well-defined and refinement-independent.

On a general Boolean algebra $B$ with no metric, there is no
canonical notion of "distance to infinity."  A refining sequence
$E_n \searrow \emptyset$ depends on the choice of sequence.
Different sequences give different rates.

**This is the central obstacle.**  Without a canonical
refinement, "rate of tail decay" is observer-dependent.  Three
possible resolutions:

1. **Supremum over refinements.**  Define
   $$\alpha(\mu) = \sup \left\{ \alpha \geq 0 :
   \mu(E_n) = O(n^{-\alpha})
   \text{ for all } E_n \searrow \emptyset \right\}.$$
   This gives a refinement-independent invariant, but it might
   collapse to $\{0, \infty\}$ (trivial) or depend on the
   algebra in ways that make it uncomputable.

2. **Natural refinement from programme structure.**  In the
   query-system framework, the cylinder refinement
   $\mathcal{B}_0 \subseteq \mathcal{B}_1 \subseteq \cdots$
   provides a canonical filtration.  The rate of
   $\mu(E_n) \to 0$ relative to this filtration is
   observer-dependent (it depends on the query system), but
   *that is the point* --- the programme already treats the
   observer as primitive.

3. **Valuation of refinement.**  The programme's existing
   concept: a function $\Lambda(k)$ turning the refinement
   index into a scale.  The rate becomes
   $\mu(E_n) = O(e^{-\Lambda(n)})$ or similar, and dimension
   is distinguishability growth per unit valuation.  Tail
   decay rate might be a dual quantity.

---

## Connection to CE

CE in the programme is: $E_n \searrow \emptyset$ in the
observable algebra $\implies \mu(E_n) \to 0$.  This is the
Halmos characterization restricted to a specific refinement
system.

"CE at rate $r$" would be: $\mu(E_n) \to 0$ at rate $r$
relative to the cylinder refinement.  The rate $r$ would then
connect to:
- the tail index $\alpha$ (for measures on $\mathbb{R}$ with
  the standard refinement);
- the observational resolution dimension $D_\Lambda$ (for
  the finite-sample theory);
- the Yosida-Hewitt pure part $\|\mu_p\|$ (as $r \to 0$,
  the measure approaches PFA).

Whether this triangle closes formally is the central question.

---

## Candidate theorem (informal)

**Statement.**  Let $(B, \mu)$ be a Boolean algebra with a
bounded finitely additive charge, and let
$\mu = \mu_c + \mu_p$ be the Yosida-Hewitt decomposition.
For a refining sequence $\mathcal{E} = (E_n)$ with
$E_n \searrow \emptyset$:

(a) $\mu_c(E_n) \to 0$ at a rate determined by the "tail
    index" of $\mu_c$ relative to $\mathcal{E}$;

(b) $\mu_p(E_n) = \mu_p(E_1)$ for all $n$ (the PFA part
    has constant mass on the tail --- zero decay);

(c) the total charge $\mu(E_n) \to \mu_p(E_1)$, and the
    rate of convergence to this limit is the tail index of
    the $\sigma$-additive part.

Part (b) is false as stated --- $\mu_p$ can vary along a
refining sequence.  But $\mu_p$ does satisfy
$\inf_n \mu_p(E_n) > 0$ whenever $\mu_p \neq 0$ and the
$E_n$ are chosen to witness failure of $\sigma$-additivity.
The correct version requires care about which sequences
witness the PFA component.

**Status:** Not verified.  Needs Lean or manual proof.
Part (b) is the load-bearing claim and is likely wrong as
stated.  The Yosida-Hewitt pure part is characterized by
$\inf\{\mu_p(A) : A \supseteq E\} = 0$ for suitable $E$,
which is subtler than "constant on tails."

---

## What a new idea would need to do

For this seed to survive audit, it must produce one of:

1. A refinement-independent invariant $\alpha(\mu)$ that is
   non-trivial (not always 0 or $\infty$) and recovers the
   tail index on $\mathbb{R}$.

2. A theorem connecting the CE rate in a query system to a
   quantity in the heavy-tail / regular-variation literature,
   showing that the programme's "valuation of refinement"
   specializes to the classical tail index.

3. A structural result showing that the Yosida-Hewitt
   decomposition, when refined by rate information, produces
   a natural graded spectrum that is invisible to the binary
   decomposition alone.

Without at least one of these, the seed is taxonomic ---
assembling known results under a new label without proving
anything.

---

## Key references

| Source | What it provides |
|--------|-----------------|
| Halmos (1950), Section 13 | $\sigma$-additivity $\iff$ $E_n \searrow \emptyset \implies \mu(E_n) \to 0$ |
| Yosida-Hewitt (1952) | unique decomposition $\mu = \mu_c + \mu_p$ |
| Dunford-Schwartz (1958) | $\text{ba}(\mathbb{N}) \cong M(\beta\mathbb{N})$; PFA = support on remainder |
| Dubins (1977) | tail disintegrations of Haar are PFA |
| Schervish-Seidenfeld-Kadane (2021) | improper vs FA limits are independent |
| Bingham-Goldie-Teugels (1987) | regular variation; classical tail-index theory |
| Resnick (1987, 2007) | heavy tails and regular variation |

---

## Open questions

1. Does the supremum-over-refinements definition of
   $\alpha(\mu)$ collapse to $\{0, \infty\}$, or does it
   take intermediate values?

2. On $\mathbb{R}$ with Borel sets, does $\alpha(\mu)$
   recover the classical tail index?

3. Is the Dubins (1977) result a special case of a general
   principle: "disintegration with respect to a tail-like
   sub-$\sigma$-field always produces PFA conditionals"?

4. Does the regular-variation literature contain invariants
   that transfer to the Boolean-algebra setting via Stone
   duality?

---

*Seed note, 2026-05-18.  Prompted by observation that heavy
tails and PFA charges share the structural feature of
persistent mass at infinity.  Not yet audited.*
