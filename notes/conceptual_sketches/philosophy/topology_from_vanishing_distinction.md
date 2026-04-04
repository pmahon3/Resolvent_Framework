# Topology from Vanishing Distinction

## The question

A binary tree of clopen cuts generates a Hausdorff topology — in the sense that
any two distinct infinite paths can be separated at some finite level. This is
exactly what discriminability says in the query-system framework: for any
$\omega \neq \omega'$, some cylinder event separates them.

But a Hausdorff topology is not yet a continuum. The Cantor space is Hausdorff.
The real line is Hausdorff. These are different objects, and the difference is
not about separation — it is about what happens to separations under infinite
refinement.

The question this note pursues: **can the continuum-like structure of the real
line, and more generally the topology of the state space, be derived from the
asymptotic behavior of separations in a query system, rather than assumed as
input?**

---

## Primitive objects

Let $(I, \leq)$ be a directed index set and $\{B_i\}_{i \in I}$ the associated
levelwise Boolean algebras of cylinder events, as in the query-system framework.
For $x, y \in \Omega$, define the **separation set**

$$\mathrm{Sep}(x,y) := \{ i \in I : \exists E \in B_i \text{ with } x \in E,\, y \notin E \}.$$

This records *at which levels* the pair can be told apart. It does not yet ask
whether that telling-apart is stable or transient.

Now define the **persistent-separation set**

$$\mathrm{Pers}(x,y) := \{ i \in I : \exists j \geq i \ \forall k \geq j,\ k \in \mathrm{Sep}(x,y) \}.$$

So $i \in \mathrm{Pers}(x,y)$ means that from some stage onward, separation at
$x$ and $y$ never disappears. The distinction has hardened.

---

## Three regimes

This gives a natural trichotomy:

**Observational equivalence** $x \sim y$:
$$\mathrm{Sep}(x,y) = \emptyset.$$
No query ever separates them. Under discriminability, this collapses to $x = y$.

**Persistent distinguishability** $x \perp y$:
$$\mathrm{Pers}(x,y) \neq \emptyset.$$
There is some level beyond which the distinction sticks.

**Vanishing distinction** $x \asymp y$:
$$\mathrm{Sep}(x,y) \neq \emptyset \quad \text{and} \quad \mathrm{Pers}(x,y) = \emptyset.$$
The pair can be separated at arbitrarily fine levels, but no separation ever
stabilizes.

$\asymp$ is the proposed primitive for *proto-nearness*: not indistinguishability,
not stable distinctness, but distinction that never fully settles.

---

## Key proposition: monotone observability kills the third regime

**Definition.** The system satisfies *monotone observability* if
$$i \leq j \text{ and } \mathrm{Sep}_i(x,y) \implies \mathrm{Sep}_j(x,y).$$
That is, refinement never destroys an already-available separation. This holds
automatically when finer Boolean algebras contain pullbacks of coarser ones —
exactly the condition satisfied by the cylinder refinement maps $\pi_{ij}$.

**Proposition.** If the system satisfies monotone observability and
discriminability, then $x \asymp y$ never occurs: for all $x \neq y$,
$\mathrm{Pers}(x,y) \neq \emptyset$.

*Proof.* By discriminability, there exists $i$ with $\mathrm{Sep}_i(x,y)$.
By monotone observability, $\mathrm{Sep}_k(x,y)$ holds for all $k \geq i$.
Hence $i \in \mathrm{Pers}(x,y)$. $\square$

**Consequence.** In an ordinary Boolean cylinder refinement system, $\asymp$ is
vacuous. The distinguishable/indistinguishable binary genuinely persists. The
third regime requires either relaxing monotone observability, or bringing in
additional structure beyond the Boolean algebra layer.

This is a diagnosis, not a dead end.

---

## Where the third regime lives: the measure-weighted version

The proposition above shows that $\asymp$ cannot arise from Boolean separation
alone in a monotone system. But it can arise when separation is weighted by the
measure.

Consider two paths in the binary tree:
- $x = 0.0111\ldots$
- $y = 0.1000\ldots$

At every finite level $i$, these land in different halves: $\mathrm{Sep}_i(x,y)$
holds for all $i$, so $\mathrm{Pers}(x,y) \neq \emptyset$ and $x \perp y$. They
represent the same real number after identification, but the Boolean algebra never
sees that — it only sees the formal cut.

What changes when the measure is brought in: the measure $\nu_i$ assigned to
the separating event $E \in B_i$ goes to zero as $i \to \infty$. The separation
exists formally at every level, but its *weight* vanishes.

This suggests the right definition of proto-nearness is not purely Boolean:

$$x \approx_i y \iff \text{every } E \in B_i \text{ separating } x \text{ and } y \text{ satisfies } \nu_i(E) < \varepsilon_i,$$

for some scale $\varepsilon_i \to 0$ along the refinement order. Then:

- **Persistent distinction**: the separating events retain measure bounded away from zero.
- **Vanishing distinction** ($\asymp$): separation events exist at every level, but their measure goes to zero.

Under this definition, the dyadic pair $0.0111\ldots$ and $0.1000\ldots$ satisfy
$\asymp$ — they are separated at every level, but the separating event has
vanishing measure — and this matches the geometric intuition that they are the
same point.

---

## Connection to CE

The parallel with collective exhaustion is structural.

CE says: if a sequence of events $E_n \searrow \emptyset$ in the observable
algebra, the *measure* assigned to them must witness the vanishing — no level
can assign persistent mass to events the completed observation sees as empty.

The measure-weighted $\asymp$ says: if a pair of points is separated at every
level but the *measure* of the separating events vanishes, the separation is
topologically inert.

Both conditions are about honesty between the formal/Boolean layer and the
valuation layer. In CE, the honesty is about mass not persisting on formally
empty events. In $\asymp$, the honesty is about distinctions not being declared
stable when their weight has vanished.

**Conjecture.** CE (on the valuation side) and measure-weighted $\asymp$ (on the
separation side) are two faces of a single coherence condition on the interplay
between a directed Boolean system and its charge. Under this unified condition,
the topology of the completed space would be derived, not assumed.

This is the principal open question of this note.

---

## Axioms for a proto-nearness structure

Setting the measure-weighted version aside, one can also study $\asymp$
axiomatically. The minimal structure is a family of binary relations
$\{{\approx_i}\}_{i \in I}$ on $\Omega$ satisfying:

- **(N1) Reflexive:** $x \approx_i x$.
- **(N2) Symmetric:** $x \approx_i y \Rightarrow y \approx_i x$.
- **(N3) Monotone shrinkage:** $j \geq i \Rightarrow (x \approx_j y \Rightarrow x \approx_i y)$.
- **(N4) Separation completeness:** for $x \neq y$, it is not the case that
  $\forall i\, \forall j \geq i,\ x \approx_j y$.

From these, define:

$$x \mathbin{\#} y \iff \exists i\, \forall j \geq i,\ \lnot(x \approx_j y),$$
$$x \asymp y \iff (\forall i\, \exists j \geq i,\ x \approx_j y) \text{ and } (\forall i\, \exists j \geq i,\ \lnot(x \approx_j y)).$$

Then $\#$ is stable apartness and $\asymp$ is vanishing distinction — the two
come apart precisely when coherence and incoherence alternate without either
stabilizing.

The proto-neighborhood of $x$ at level $i$ is $N_i(x) := \{y : x \approx_i y\}$.
By (N3), $j \geq i \Rightarrow N_j(x) \subseteq N_i(x)$: neighborhoods shrink
with refinement. Topology, if it emerges, comes later — from the convergence
theory of these nested approximations.

---

## Relation to the existing programme

The Stone space $\mathrm{St}(\mathcal{C})$ constructed in Paper I as a technical
device for measure extension is already a compact Hausdorff space whose topology
is generated by the clopen sets $[E]$ for $E \in \mathcal{C}$. That topology is
*given by the Boolean algebra* — it is the coarsest topology making all cylinder
events clopen.

But this is the topology of *all* consistent distinction patterns, including
non-principal ultrafilters. Discriminability and CE together ensure the measure
descends to the principal ultrafilters — the image of $\Omega$ inside
$\mathrm{St}(\mathcal{C})$.

The open question is whether the topology the observer should carry on $\Omega$
— the topology relevant to dynamics and reconstruction — is the subspace topology
from $\mathrm{St}(\mathcal{C})$, or something coarser determined by the
*measure-weighted* separation structure. If the latter, then Paper IV's task is
to derive that topology from the query-system and its charges, rather than
inheriting it from the Stone compactification.

---

## Summary of objects and open questions

| Object | Definition | Status |
|--------|-----------|--------|
| $\mathrm{Sep}(x,y)$ | Levels at which $x,y$ can be separated | Defined |
| $\mathrm{Pers}(x,y)$ | Levels from which separation stabilizes | Defined |
| $x \asymp y$ | $\mathrm{Sep} \neq \emptyset$, $\mathrm{Pers} = \emptyset$ | Vacuous under monotone observability |
| Measure-weighted $\asymp$ | Separating events have vanishing measure | Candidate definition |
| Unified CE / $\asymp$ coherence | Both faces of a single condition | **Conjecture — open** |
| Topology derived from $\asymp$ | Topology as organized failure of stable separation | **Programme of Paper IV** |

---

*Written 2026-04-03. Seed material from exploratory conversation; not yet formalized.*
