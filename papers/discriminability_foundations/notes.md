# Discriminability Foundations (Paper −1 seed)

**Status:** Pre-paper notes. Mathematical exploration in progress.
**Date started:** 2026-03-20

---

## The question

The current program (Papers 0–4) assumes that each query $Q$ comes equipped with a full
σ-algebra $\mathcal{B}(O_Q)$ of distinguishable events. This is labelled as a primitive
input in Paper 1 (observational_foundations, Remark after Definition 2.1):

> "A more foundational treatment would derive this σ-algebra from a designated class
> $\mathcal{E}_Q$ of admissible observable distinctions via $\mathcal{B}(O_Q) =
> \sigma(\mathcal{E}_Q)$; we regard this as a direction for future work."

**SP1** asks whether this deferral can be closed: can the σ-algebra be *derived* from
something more primitive, rather than assumed?

---

## The saddle point

The question lives at the boundary between two territories:

- **Philosophy side:** What structures must an observer bring to experience for coherent
  probabilistic reasoning to be possible at all? (Kantian: conditions of possibility.)
  Falling too far this way produces unbounded discussion without mathematical traction.

- **Mathematics side:** Carathéodory extension, Horn-Tarski theorem, σ-algebras generated
  by Boolean algebras, continuity conditions on premeasures. Rigorous but potentially
  disconnected from the foundational motivation.

The productive place is the saddle: a single mathematically precise question whose
answer would settle something genuinely foundational.

---

## The Kantian framing (motivating, not load-bearing)

Kant's synthetic a priori: what structures must the mind *bring to* experience for
experience to be possible at all? Not empirical (contingent), not analytic (logical
tautology) — but *forced by the conditions of coherent experience*.

SP1 asks: is the σ-algebra synthetic in this sense? Not out there in the world (ontic),
not a logical necessity (analytic) — but *forced by the conditions of coherent
observational commitment*?

The σ-algebra would then be the *form* that observational experience must take; the
specific measures are the *content*. SP1 asks whether the form is derivable from
coherence constraints on the content.

Connection to logic: the σ-algebra is to the Boolean algebra $\mathcal{E}_Q$ as
infinitary logic (Lω₁ω, with countable conjunctions/disjunctions) is to finitary
propositional logic. The σ-closure step is exactly the move from finitary to infinitary
reasoning — and this is precisely where classical completeness theorems break down.
This is not a coincidence.

---

## The single-observer setup

**Primitive data:** A Boolean algebra $\mathcal{E}$ of distinctions (closed under finite
∧, ∨, ¬) and a normalized finitely-additive valuation $\ell : \mathcal{E} \to [0,1]$.

No σ-algebra assumed. No topology assumed. Just: what the observer can currently
distinguish, and how they weight those distinctions.

**The question:** Under what conditions — stateable purely in terms of $\ell$ on
$\mathcal{E}$ — does $\ell$ extend uniquely to a σ-additive measure on $\sigma(\mathcal{E})$?

---

## The first attempt: exhaustiveness

The Horn-Tarski theorem suggests: $\ell$ extends iff it is *exhaustive* — $\ell(E_n) \to 0$
for every disjoint sequence $(E_n) \subset \mathcal{E}$.

**But this is trivially true.** For any normalized finitely-additive $\ell$ and disjoint
sequence $(E_n)$: $\sum_{n=1}^N \ell(E_n) \leq 1$ for all $N$, so the series converges,
so $\ell(E_n) \to 0$. No compatibility, no directedness, nothing needed.

**Lesson:** Exhaustiveness is the wrong condition. The real obstruction to extending
$\ell$ to $\sigma(\mathcal{E})$ is elsewhere.

---

## The real obstruction

The correct extension condition is *continuity at ∅ from above*:

For every decreasing sequence $E_1 \supseteq E_2 \supseteq \cdots$ in $\mathcal{E}$
with $\bigcap_n E_n = \emptyset$ **in $\sigma(\mathcal{E})$** (not necessarily in
$\mathcal{E}$), we need $\ell(E_n) \to 0$.

**This is where the real philosophical content lives.** The observer must assign
vanishing weight to events whose intersection escapes their language — they must be
coherent about things they cannot directly express. The intersection $\bigcap_n E_n$
may not be in $\mathcal{E}$ at all; it lives in $\sigma(\mathcal{E}) \setminus
\mathcal{E}$, which is precisely what the observer doesn't have access to.

So the condition asks: can the observer be coherent about events they cannot see?

---

## The query system version and the negative result

In a directed query system $\{(\mathcal{E}_Q, \ell_Q)\}$ with compatible valuations,
the refinement structure might witness emptiness that a single query cannot. Precisely:

**Candidate theorem:** If $E_1 \supseteq E_2 \supseteq \cdots$ in $\mathcal{E}_Q$ and
there exists a finer query $Q' \succeq Q$ such that $\bigcap_n \pi^{-1}(E_n) = \emptyset$
*in $\mathcal{E}_{Q'}$ itself*, then compatibility forces $\ell_Q(E_n) \to 0$.

**Proof attempt:** $\ell_Q(E_n) = \ell_{Q'}(\pi^{-1}(E_n))$ by compatibility. The
sequence $\pi^{-1}(E_n)$ is decreasing in $\mathcal{E}_{Q'}$ with intersection $\emptyset$
in $\mathcal{E}_{Q'}$. But finite additivity on $\mathcal{E}_{Q'}$ still does not give
$\ell_{Q'}(\pi^{-1}(E_n)) \to 0$ — the same wall appears one level up.

**The negative result:** The regress is real and structural. To force $\ell(E_n) \to 0$
from purely finitary conditions, you need something that can *see the limit* — something
that can witness $\bigcap_n E_n = \emptyset$ from within the finitary structure. Purely
algebraic/combinatorial means cannot close this gap. Three candidates for the extra
ingredient:

1. **Topology** (compactness): compact sets witness emptiness — a decreasing family of
   nonempty compact sets has nonempty intersection. Failure of continuity at ∅ would
   contradict compactness.

2. **A limit query** (colimit in the directed system): a query $Q_\infty$ that sits above
   all $Q$ and whose event algebra *contains* the limits — so $\bigcap_n E_n \in
   \mathcal{E}_{Q_\infty}$ and its measure is forced by compatibility.

3. **An explicit continuity axiom**: simply assume the observer is continuous at ∅.
   Honest but unsatisfying — it restates σ-additivity rather than deriving it.

**The philosophical payoff of the negative result:** The σ-algebra is *not* synthetic
a priori in Kant's strong sense. It genuinely requires something beyond pure coherence.
The program's use of compactness or Polish structure is not a technical crutch — it is
the *minimal witness* needed to bridge finitary commitments and countable closure. This
gives a foundational *justification* for those structural hypotheses: they are exactly
the conditions under which the semantic completeness of the valuation system forces the
syntactic closure of the event algebra.

---

## The open question

Which of the three options (topology, limit query, continuity axiom) is:

- The most *primitive* — closest to what an observer actually has access to?
- The most *intrinsic* — stated in the program's own language without importing topology?
- The most *general* — applying beyond compact and Polish cases?

The **limit query** option is the most intrinsic candidate. It asks: does the query
system have a colimit? If so, does the colimit query's event algebra contain the relevant
limits? And does compatibility with the colimit force continuity at ∅ at every finite level?

This is the natural next question.

---

## Connections to the existing program

- **SP2** (σ-additivity from compatibility) is SP1 one layer up: it asks about the global
  measure on $\Omega$, not the individual $\ell_Q$. Resolving SP1 via the limit query
  option would likely reshape how SP2 is stated.

- **Paper 0** closes SP2 for compact (Prokhorov) and standard Borel (Musiał) cases via
  topology. The limit query option for SP1 would be a topology-free route that might
  simultaneously address both SP1 and SP2 in the general case.

- **The exhaustiveness false start** is itself useful: it shows that the program's
  finitely-additive starting point is not the obstruction. The problem is not at the
  level of individual events but at the level of *sequences escaping the algebra*.

---

## The central chord (2026-03-20)

The exploration above converges on a single insight that reframes the entire program.

### Discriminability requires incompleteness

The program has been building toward:
$$\text{coherent observable commitments} \longrightarrow \text{probability}$$

But the condition of possibility for that arrow — invisible until SP1 — is:
$$\text{discriminability requires incompleteness}$$

An observer who can see everything ($\mathcal{E}_Q = \sigma(\mathcal{E}_Q)$) is not an
observer in the program's sense. They have no horizon, no outside, no space into which
refinement can reach. The gap $\sigma(\mathcal{E}_Q) \setminus \mathcal{E}_Q$ is not a
defect to be patched. It is the *constitutive outside* that makes the observer an observer
— and makes refinement possible.

The program's chain should be read as:
$$\text{bounded discriminability} \to \text{refinement} \to \text{coherence} \to \text{probability}$$

where bounded discriminability — necessary incompleteness — is what makes refinement
meaningful, refinement is what makes cross-level coherence non-trivial, and coherence is
what forces probability to emerge.

**Paper −1 is not a technical preliminary to the program. It is the program's foundation
— the thing that explains why the program has the shape it does.**

### The Gödelian resonance (handled carefully)

Gödel: any sufficiently rich consistent formal system has true sentences it cannot prove.
The system cannot close its own gap from within.

SP1b (analogue): any observer embedded in a nontrivial refinement system has events in
$\sigma(\mathcal{E}_Q) \setminus \mathcal{E}_Q$ — distinctions it cannot currently make
but that the refinement structure is oriented toward. The observer cannot close their own
gap from within.

The difference from Gödel: the gap here is not a *failure* but a *feature*. Without the
gap there is no refinement. Without refinement there is no program.

The danger to avoid: sliding from this analogy into computability/completeness theory
proper. The connection is structural and motivating, not a reduction. The program's
questions are about *measure*, not *proof* — the gap is metric, not syntactic.

### Two theorems Paper −1 needs

**Theorem A (necessity of incompleteness):** In any nontrivial query system with a
genuine refinement order, no observer at a finite level $Q$ has $\mathcal{E}_Q =
\sigma(\mathcal{E}_Q)$. The gap is nonempty. Discriminability is necessarily incomplete.

*What "nontrivial" means needs to be made precise — likely: there exists $Q' \succ Q$
such that $\mathcal{E}_{Q'} \not\subseteq \mathcal{E}_Q$ after pullback. The refinement
genuinely adds distinctions.*

**Theorem B (witnessing from above):** Under sequential upper-directedness, the
refinement structure witnesses the gap from above — the colimit sees what finite levels
cannot, and compatibility propagates that witnessing back down to force continuity at ∅
at every finite level.

*This is the positive result that SP1b makes possible: the observer needs the system
(cannot close the gap alone), and the system provides the witness (sequential upper-
directedness is the minimal condition for the system to do so).*

Together: **the observer needs the system, and the system needs the gap.**

---

## Next questions (to be addressed)

1. Make "nontrivial refinement" precise for Theorem A. What is the minimal condition on
   the query system that forces $\mathcal{E}_Q \subsetneq \sigma(\mathcal{E}_Q)$?

2. Can the limit query option be made precise for Theorem B? Is sequential
   upper-directedness exactly the right colimit condition, or something stronger/weaker?

3. Is there a known result in the theory of Boolean algebras or Stone spaces that
   corresponds to the limit query option? (The Stone space of $\sigma(\mathcal{E})$ is
   the closure of the Stone space of $\mathcal{E}$ — this may be the right lens for
   making the gap precise topologically, even if the program ultimately avoids topology.)

4. What is the relationship between Theorem B and the sequential upper-directedness
   already in the program? Can the existing hypothesis be shown to be *equivalent* to
   the witnessing condition, making SP1 a theorem of the existing framework rather than
   a new axiom?
