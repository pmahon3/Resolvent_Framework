# Assumption Audit and Conceptual Stress Test
## Observational Foundations of Probability

*Date: 2026-03-17*

---

## (A) Executive Summary

The paper is technically sound and the main theorem is correctly stated and proved. The observable-first rhetoric is largely honest and the framework is a genuine improvement over starting from a product-coordinate space. However, the paper carries several assumptions that do significant conceptual work while being presented as nearly inevitable or merely technical. The three most important hidden load-bearers are:

1. **Measurable structure on outcome spaces is given, not derived.** Queries are defined with outcome spaces $(O_Q, \mathcal{B}(O_Q))$ already equipped with $\sigma$-algebras. This is the single biggest gap between the rhetoric and the formalism.

2. **Realizability (surjectivity of all eval maps) is stronger than the paper acknowledges.** It appears late, is described mildly as a "coherence condition," and is used in a genuinely critical way in the well-definedness of the premeasure. It is also not guaranteed in general without topology.

3. **Sequential common refinements is a strong structural hypothesis that does real analytic work, but its conceptual status — is it a structural fact about the observational interface, or an assumption about the richness of the query system? — is not clearly resolved.**

The paper genuinely earns: the uniqueness theorem (essentially clean), the finite-content construction (clean given its hypotheses), and the form of the extension argument (elegant). What it still significantly assumes: the measurable infrastructure on outcome spaces, the realizability of the projective limit, and the sequential refinement property. The deepest gap is the first one.

---

## (B) Detailed Audit

---

### PART I. Global Assumption Audit

**A1. Each query $Q$ has a given measurable outcome space $(O_Q, \mathcal{B}(O_Q))$**

- *Classification:* Hidden ontological assumption / Structural assumption
- *Where:* Definition 1 (Query), §3
- *Role:* Foundational. All cylinder sets, the observable $\sigma$-field, compatibility, the premeasure, and the extension theorem depend on having $\sigma$-algebras on each $O_Q$.
- *Conceptual status:* This is the single largest import of structure that the paper has not earned from observable experience. The paper says it starts from "admissible queries," but a query immediately comes equipped with a full $\sigma$-algebra on its outcome space. This $\sigma$-algebra decides which events are observable — yet that decision is presented as given, not derived.
- *Stronger than necessary?* Yes. The $\sigma$-algebra $\mathcal{B}(O_Q)$ is never generated from anything. It is just there.
- *More earned reformulation:* The measurable structure on $O_Q$ should arise from the distinguished events an observer can report at resolution $Q$ — i.e., from a class $\mathcal{E}_Q \subset 2^{O_Q}$ of "reportable events," with $\mathcal{B}(O_Q) := \sigma(\mathcal{E}_Q)$. Under this framing, what is primitive is a class of admissible observable distinctions at each resolution, and the measurable structure is derived.

---

**A2. The preorder $(\mathcal{Q}, \preceq)$ on queries**

- *Classification:* Structural assumption
- *Where:* Definition 2 (Query system)
- *Role:* Organizes the information lattice; required for coherence maps, cylinder intersections, and directedness.
- *Conceptual status:* Partially earned. The intuition (finer queries determine coarser ones by post-processing) is well-motivated. But the preorder is simply assumed to exist on whatever collection $\mathcal{Q}$ is taken as primitive; there is no derivation of it from any more elementary structure.
- *More earned reformulation:* The refinement relation could be defined operationally as "$Q_1 \preceq Q_2$ iff there exists a measurable map $\pi: O_{Q_2} \to O_{Q_1}$ such that the distributions are consistent under $\pi$." This would make the preorder a consequence of the compatibility structure rather than an input to it. (The paper gestures toward this in §7 but does not make it the foundation.)

---

**A3. The coherence relations $\pi^Q_Q = \mathrm{id}$ and $\pi^{Q_3}_{Q_1} = \pi^{Q_2}_{Q_1} \circ \pi^{Q_3}_{Q_2}$**

- *Classification:* Structural assumption / Technical proof device
- *Where:* Definition 2, functoriality conditions
- *Role:* Essential for the projective limit to be well-defined as a subset of $\prod_Q O_Q$.
- *Conceptual status:* Partially earned. Functoriality of post-processing maps is natural. But requiring it strictly (rather than up to a.e. equivalence) is a nontrivial demand. In probabilistic contexts, maps often only cohere a.e. under some measure. The paper requires strict pointwise coherence.
- *Potentially weakenable:* Coherence a.e. under the compatible family $\{\nu_Q\}$ would be a weaker and arguably more empirically natural condition, though it would complicate the projective limit construction significantly.

---

**A4. Common coarsenings (lower-directedness)**

- *Classification:* Structural assumption
- *Where:* Definition 3, used in Lemma (Cylinder $\pi$-system) and Cylinder semiring
- *Role:* Ensures that finite collections of cylinder constraints can be expressed at a single query level — needed for the $\pi$-system property and the semiring structure.
- *Conceptual status:* Partially earned. The intuition is that any two observational resolutions can be jointly dominated by a coarser one. This is reasonable as a structural assumption about the query system and is better understood as an assumption about **joint expressibility** of observations at a single coarser resolution — a real constraint.
- *Stronger than necessary?* For the uniqueness theorem, probably not. It is the minimal condition for the cylinder family to be a $\pi$-system.

---

**A5. Common refinements (upper-directedness)**

- *Classification:* Structural assumption
- *Where:* Definition 4, used in premeasure well-definedness
- *Role:* Needed so that any finite collection of query constraints can be "lifted" to a single finer level. This is what makes the premeasure well-defined — it ensures the value assigned to a cylinder doesn't depend on which level you use to represent it.
- *Conceptual status:* Partially earned. Requires the system to be join-semilattice-like from above. Conceptually this means: any two experiments can be jointly refined by a third, which is a strong but intelligible structural hypothesis.
- *Stronger than necessary?* For well-definedness of the premeasure, this is the right condition given the proof strategy.

---

**A6. Sequential common refinements**

- *Classification:* Structural assumption / Technical proof device
- *Where:* Definition 5, used in Step 2 of the extension theorem
- *Role:* The key analytic hypothesis. Ensures that any countable family of cylinders can be compressed to a single query level, reducing $\sigma$-subadditivity of the premeasure to $\sigma$-subadditivity of a single probability measure.
- *Conceptual status:* Genuinely ambiguous. Is it a fact about the richness of the observational interface (there is always a query that jointly resolves any countable family)? Or is it an analytic regularity condition imposed for technical reasons? The paper says it is "the key analytic hypothesis" but does not clearly situate it as an assumption about joint observability. It implies the query system behaves like a directed $\omega$-complete poset.
- *Stronger than necessary?* Possibly. Whether a $\sigma$-finite or measure-theoretically weaker analogue would suffice is not discussed.

---

**A7. Realizability (surjectivity of all eval maps)**

- *Classification:* Structural assumption — **the strongest hidden assumption**
- *Where:* Definition 6; used critically in the premeasure well-definedness proof and in Step 2 of the extension theorem
- *Role:*
  - (i) Premeasure well-definedness: surjectivity of $\mathrm{eval}_{Q_*}$ is used to transfer equality of cylinder sets in $\Omega$ to equality of preimage sets in $O_{Q_*}$.
  - (ii) $\sigma$-subadditivity: set inclusion in $\Omega$ must be translated to set inclusion in $O_{Q_*}$; realizability ensures no element of $O_{Q_*}$ is "missing" from $\Omega$.
- *Conceptual status:* The paper describes it as a "coherence condition" asserting no "phantom outcomes." This framing is reasonable but understates what is being assumed. Realizability is not merely a coherence property — it is an assertion that the projective limit is sufficiently rich, which fails in general without topological hypotheses.
- *Stronger than necessary?* Quite possibly. **Almost-sure realizability** — for each $Q$ and $\nu_Q$-almost every $o \in O_Q$, there exists $\omega \in \Omega$ with $\mathrm{eval}_Q(\omega) = o$ — would suffice for the measure-theoretic arguments and is strictly weaker.
- *Paper's treatment:* Realizability is mentioned as being satisfied "whenever the projective limit is non-degenerate" — but non-degeneracy is exactly what realizability asserts. This is circular. The Polish + countable sufficient condition (Corollary 6.1) should be clearly flagged as the main route to realizability, with the general measurable case acknowledged as requiring a genuine assumption.

---

**A8. Each $\nu_Q$ is a full countably additive probability measure**

- *Classification:* Measure-theoretic assumption
- *Where:* Hypothesis 4 of the extension theorem
- *Role:* The $\sigma$-subadditivity of $\nu_{Q_*}$ in Step 2 relies on countable additivity.
- *Conceptual status:* Partly hidden. The paper asks when compatible observable laws "determine" a canonical probability measure, but the observable laws $\nu_Q$ are themselves required to already be countably additive. The paper is not constructing $\sigma$-additivity from scratch — it is propagating it. The question of where the $\sigma$-additivity of the $\nu_Q$ comes from is left entirely open.

---

**A9. Carathéodory extension theorem (used as a black box)**

- *Classification:* Technical proof device
- *Where:* Step 3 of the extension theorem proof
- *Role:* Converts the $\sigma$-subadditive finitely additive content to a full measure.
- *Conceptual status:* Proof scaffold, explicitly cited. The paper should be more explicit that this is where countable additivity is "created" from $\sigma$-subadditivity, and that $\sigma$-subadditivity is itself only available because the $\nu_{Q_*}$ are already countably additive.

---

### PART II. Pressure-Test of the "Observable-First" Claim

| Structure | Verdict | Comment |
|---|---|---|
| Preorder / refinement organization | **Assumed** | Preorder is given as primitive; derivation from post-processing relations is mentioned in §7 but not foundational |
| Measurable structure on outcome spaces | **Assumed** | The central weakness; $\mathcal{B}(O_Q)$ is never generated from observable distinctions |
| Coherence of refinement maps | **Assumed** | Strict functorial coherence required; not derived; could be relaxed to a.e. |
| Projective-limit realization space | **Partially earned** | Correctly derived as the set of coherent answers; risk of emptiness without realizability not foregrounded |
| Observable $\sigma$-field $\sigma(\mathcal{Q})$ | **Earned** | Cleanly derived as the $\sigma$-algebra generated by evaluation maps |
| Surjectivity / realizability | **Assumed, presented as mild** | The strongest hidden assumption; used critically in two places; should be foregrounded |
| Finite additivity | **Earned** (given inputs) | Follows cleanly from compression and additivity of $\nu_{Q_*}$ |
| Countable additivity / $\sigma$-subadditivity | **Partially earned** | Derived from sequential refinements + existing $\sigma$-additivity of $\nu_{Q_*}$; source of $\sigma$-additivity unaddressed |
| Carathéodory extension | **Proof scaffold** | Major theorem applied; should be more openly acknowledged |

---

### PART III. Specific Stress Points

**1. Query System Structure**

The preorder and refinement maps are primitive. A more foundational treatment would derive $Q_1 \preceq Q_2$ from the existence of a measurable $\pi: O_{Q_2} \to O_{Q_1}$ with $\pi_\# \nu_{Q_2} = \nu_{Q_1}$, making the preorder a consequence of compatibility rather than an input. The paper names this correspondence in §7 but does not make it foundational.

**2. Measurable Structure on Outcome Spaces**

The paper's weakest point relative to its philosophy. $(O_Q, \mathcal{B}(O_Q))$ is given with no derivation. The observable-first approach demands that the paper either:
- (a) Explicitly acknowledge this as a primitive input, or
- (b) Reframe: a query is a set $O_Q$ with a designated class $\mathcal{E}_Q$ of reportable events, and $\mathcal{B}(O_Q) := \sigma(\mathcal{E}_Q)$.

Option (b) would make the measurable structure genuinely observable-first.

**3. Directedness Assumptions**

- **Lower-directedness:** Conceptually natural. Means any two observable resolutions can be jointly described at a coarser one.
- **Upper-directedness:** More substantive. Means any two observable resolutions can be jointly refined — an assumption about the richness of the observational interface that may fail (e.g., incompatible measurement devices).
- **Sequential common refinements:** The strongest. Means however many (countably many) experiments you choose, there exists one finer than all of them. This implies the query system is $\omega$-directed. The paper should say explicitly: "we assume the observational interface is closed under countable joint refinement" — this is an assumption about the **observational world**, not merely a technical hypothesis.

**4. Realization Space**

The projective limit is well-framed as derived from consistency. However:
- (i) The paper does not flag that $\Omega$ can be empty without realizability. The claim that realizability holds "whenever the projective limit is non-degenerate" is circular.
- (ii) The latent-state risk is real: $\Omega \subseteq \prod_Q O_Q$ looks like a latent state space. The paper should explicitly note that $\Omega$ carries no structure beyond what the query system forces.

**5. Realizability / Surjectivity**

The strongest hidden assumption in the paper. Two distinct uses:
1. Premeasure well-definedness: equality of cylinders in $\Omega$ $\Rightarrow$ equality of preimage sets in $O_{Q_*}$. Fails without surjectivity.
2. $\sigma$-subadditivity: inclusion of cylinders in $\Omega$ $\Rightarrow$ inclusion of base sets in $O_{Q_*}$. Fails without surjectivity.

**Possible weakenings:**
- Almost-sure realizability: for $\nu_Q$-a.e. $o \in O_Q$, $\exists \omega \in \Omega$ with $\mathrm{eval}_Q(\omega) = o$. Sufficient for all measure-theoretic arguments.
- Essential surjectivity: $\nu_{Q_*}(\mathrm{image\;of\;eval}_{Q_*}) = 1$.

The paper should foreground realizability as a genuine substantive assumption and discuss these weakenings.

**6. Additivity / Extension**

The compression argument is elegant. But the paper does not clearly say: *the countable additivity of $P$ is propagated from the countable additivity of the $\nu_Q$, not constructed from below.* If the $\nu_Q$ were only finitely additive, the argument would break at Step 2. A philosophically careful treatment would say: "We assume observable laws are countably additive and show this propagates canonically to a global probability measure."

---

### PART IV. Mathematical Necessity vs Proof Choice

| Assumption | Where used | Needed for theorem? | Needed for proof? | Philosophically comfortable? | Candidate weakening |
|---|---|---|---|---|---|
| $(O_Q, \mathcal{B}(O_Q))$ given | Throughout | Some $\sigma$-algebra needed | Yes | **No** | Generate from reportable event classes $\mathcal{E}_Q$ |
| Preorder $(\mathcal{Q}, \preceq)$ given | Throughout | Yes as stated | Yes | Partially | Derive from post-processing relations among $\nu_Q$ |
| Strict functorial coherence | Projective limit, compression | Yes as stated | Yes | Partially | Relax to a.e. coherence under $\{\nu_Q\}$ |
| Lower-directedness | $\pi$-system, semiring, uniqueness | Yes | Yes | Yes | No obvious weakening |
| Upper-directedness | Premeasure well-def | Yes for well-def | Yes | Partially | Essential upper-directedness a.e.? |
| Sequential common refinements | $\sigma$-subadditivity | Yes for current proof | Yes | Conceptually strong | $\sigma$-finite analogue? Measure-class version? |
| Realizability (surjectivity) | Premeasure well-def, $\sigma$-subadd | Not in strongest form | Yes | **No** | Almost-sure realizability under $\{\nu_Q\}$ |
| Each $\nu_Q$ is $\sigma$-additive | $\sigma$-subadditivity step | Yes | Yes | Partially — source unaddressed | N/A — foundational input |
| Carathéodory extension | Extension step | Yes | Yes | Yes | N/A |

---

### PART V. Philosophical / Conceptual Consistency

**Where rhetoric outpaces formalism:**

1. **Abstract:** *"In this sense probability appears not as a primitive structure but as the completion of observable compatibility."* Partially true. Given measurable outcome spaces, given countably additive observable laws, given a realizable projective limit, and given the three directedness conditions, probability on $\Omega$ is derived. But measurable outcome spaces and countably additive observable laws are themselves substantial pre-existing probabilistic structure. The paper has not bootstrapped probability from pure observation — it has shown that *global* probability follows from *local* probability under structural hypotheses.

2. **Introduction:** *"we derive the observable $\sigma$-field from a family of measurable maps."* True — but the measurable maps require measurable outcome spaces, which are given. The derivation is one layer deep.

3. **Realizability remark in §3:** *"It is satisfied whenever the projective limit is non-degenerate, for instance when each outcome space is Polish and the system is countable."* This makes realizability sound nearly automatic. Non-degeneracy of the projective limit is exactly what realizability states. The remark is circular.

4. **Main theorem in the Introduction:** The hypothesis list (lower-directed, sequentially upper-directed, realizable, etc.) is not stated in the Introduction-level theorem. A reader will believe the result is essentially unconditional. It is not.

---

### PART VI. Concrete Revision Advice

**1. Strongest hidden assumptions, ranked:**

1. Measurable structure on $O_Q$ is given, not derived — deepest departure from the paper's philosophy.
2. Realizability (surjectivity of all eval maps) — presented as mild; actually a strong existence assertion.
3. Each $\nu_Q$ is already countably additive — source of $\sigma$-additivity never addressed.
4. Sequential common refinements — force as an assumption about the observational interface underemphasized.
5. Strict functorial coherence of refinement maps — pointwise, not a.e.

**2. Assumptions that should be explicitly foregrounded:**

- In §1 or §3: *"We treat each query as coming equipped with a $\sigma$-algebra on its outcome space. A deeper treatment would derive this structure from classes of admissible observable distinctions; we flag this as a direction for further foundational work."*
- Before/after the Realizability definition: *"Realizability is a substantive assumption. It asserts that the projective limit is non-degenerate in a strong sense. Without it the premeasure construction breaks down."*
- In §5–6: *"The countable additivity of $P$ is propagated from the assumed countable additivity of the observable laws $\nu_Q$. We are not constructing $\sigma$-additivity from scratch but showing it is forced globally by its presence locally."*

**3. Assumptions that are candidates for weakening:**

- Realizability → **almost-sure realizability** under each $\nu_Q$ (most important)
- Strict coherence → **a.e. coherence** of refinement maps under the compatible family
- Sequential common refinements → investigate $\sigma$-finite or measure-class version
- Upper-directedness → investigate well-definedness under a weaker a.e. condition

**4. Suggested rewrites of key passages:**

*Current Definition 1 (Query):*
> "A query $Q$ consists of a measurable outcome space $(O_Q, \mathcal{B}(O_Q))$."

*Suggested:*
> "A query $Q$ consists of a set of outcomes $O_Q$ together with a designated collection $\mathcal{E}_Q \subseteq 2^{O_Q}$ of admissible observable events, representing the distinctions an observer can report at resolution $Q$. The observable $\sigma$-algebra is $\mathcal{B}(O_Q) := \sigma(\mathcal{E}_Q)$."

---

*Current Realizability remark:*
> "It is satisfied whenever the projective limit is non-degenerate, for instance when each outcome space is Polish and the system is countable."

*Suggested:*
> "Realizability is a non-trivial structural assumption. It asserts that the projective limit $\Omega$ is sufficiently rich: no outcome is locally achievable but globally blocked by an inconsistency elsewhere in the system. A sufficient condition is that each $O_Q$ is Polish, the refinement maps are continuous, and the query index set is countable — in which case the projective limit is itself Polish and realizability follows. For general measurable spaces, realizability must be verified or assumed. A natural weakening sufficient for the measure-theoretic arguments is that each evaluation map $\mathrm{eval}_Q$ is surjective $\nu_Q$-almost everywhere."

---

*Current abstract claim:*
> "In this sense probability appears not as a primitive structure but as the completion of observable compatibility."

*Suggested:*
> "Under the structural hypotheses developed below — measurable outcome spaces, compatible countably additive observable laws, joint refinement properties of the query system, and realizability of the projective limit — probability on the realization space appears as the canonical extension of observable compatibility. Each hypothesis is identified and its role in the construction made explicit."

---

**5. Suggested new remark to add after Theorem 6.1 (Extension theorem):**

> *Remark (What the theorem assumes versus derives).* The theorem assumes: (i) measurable structure on each outcome space, (ii) countable additivity of each observable law $\nu_Q$, (iii) lower-directedness, sequential upper-directedness, and realizability of the query system. It derives: a canonical $\sigma$-additive probability measure on the realization space whose evaluation marginals recover all observable laws. Countable additivity of $P$ is not constructed from below but propagated from the countable additivity of the $\nu_{Q_*}$. Assumptions (i) and (ii) are inputs from classical probability theory that a more foundational treatment should aim to derive from the structure of observable distinctions themselves.

---

### PART VII. Overall Verdict

**What the paper genuinely earns:**
- The uniqueness theorem is clean and fully earned from the observable structure given the inputs.
- The finite-content construction is genuine: given compatible laws and structural hypotheses, the premeasure is forced.
- The compression argument for $\sigma$-subadditivity is elegant and conceptually clear.
- The Carathéodory-route proof is cleaner than any topological/projective-limit route.
- The correspondence with Le Cam experiment theory is well-handled.

**What it still assumes:**
- Measurable structure on outcome spaces — not derived.
- Countable additivity of the observable laws $\nu_Q$ — not derived.
- Realizability — assumed, not derived except under topological hypotheses relegated to a corollary.
- Sequential common refinements — a strong structural hypothesis on the observational interface whose conceptual force is underemphasized.

**Deepest conceptual success:**
The compression argument (Step 2 of the extension theorem) — reducing $\sigma$-subadditivity of the global premeasure to $\sigma$-subadditivity of a single $\nu_{Q_*}$ — is the paper's strongest genuinely earned result. It shows that the global measure is assembled from local ones in a precise and verifiable way.

**Deepest hidden assumption:**
The measurable structure on outcome spaces. The paper derives $\sigma(\mathcal{Q})$ from the queries — correctly — but $\sigma(\mathcal{Q})$ is built from the $\mathcal{B}(O_Q)$, which are given. The question of what makes an event at resolution $Q$ "observable" is never addressed. This is where the paper is furthest from its stated philosophy.

**How close to the goal?**
The paper achieves roughly 60–70% of what its stated goal requires. It successfully shows that *given local probabilistic structure* (measurable outcome spaces + countably additive laws) and *given structural conditions on the query system* (directedness + realizability), a canonical global probability space exists and is unique. What it does not yet achieve is deriving the local probabilistic structure from the observable interface itself. That would require treating event-class specification and the origin of $\sigma$-additivity as part of the foundational picture. The paper is an excellent first stage; a deeper treatment would need to push below the level of measurable spaces into the structure of admissible observable distinctions.
