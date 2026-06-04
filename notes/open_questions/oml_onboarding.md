# σ-Additive Probability on Orthomodular Lattices: A Survey and an Open Problem

*Survey note — June 2026. Markdown twin of `oml_onboarding.tex`; the .tex
is the typeset authority (numbered definitions, full bibliography).*

**Abstract.** The passage from a finitely coherent assignment of
probabilities to a countably additive measure is, in the Boolean case,
governed by a single condition (countable additivity) and executed by
classical machinery (Carathéodory; Loomis–Sikorski; Stone duality). On a
*non-distributive* orthomodular lattice (OML) — the algebra of propositions
of a quantum system — this machinery breaks, and the question of when
finite coherence forces countable behaviour is open. This note surveys the
problem at the level needed to begin work on it: the apparatus, the split
into two independent axes (*extension* / *descent*), what is known and
ruled out, and the one open residue — whether a concrete, non-Boolean,
infinite σ-complete OML admits a Loomis–Sikorski-type representation. We
close by setting out the two directions of attack.

---

## 1. Introduction

All measurement is finite, yet the frameworks that organise empirical
knowledge rest on infinite structures. The passage requires a commitment
no finite evidence can compel. In probability theory the locus is
**countable additivity**; de Finetti held only finite additivity is
empirically grounded, Kolmogorov adopted σ-additivity as an axiom.

In quantum theory the same tension recurs: the propositions of a quantum
system form an **orthomodular lattice** `L(H)` (closed subspaces of a
Hilbert space) in which distributivity may fail, so Carathéodory's outer
measure does not apply. For the single lattice `L(H)` this is rescued by
Gleason's rigidity theorem; but Hilbert space is special, and for general
OMLs no analogue is known.

This note asks the shared question — *when does finite coherence force
countable behaviour?* — in the OML setting. Our organising observation: the
question splits into two independent axes, one classical and settled, the
other genuinely open.

**The relational standpoint.** Following "structure from observation"
(Paper I): begin with propositions and their entailment order, not a space
of outcomes. For non-Boolean algebras the natural dual is the
McDonald–Bimbó space of *filters* (§2.3). A positive answer to the open
problem would be a **point-free** (relational) σ-additive probability
theory on a non-distributive lattice — the non-Boolean analogue of localic
measure theory (§5).

---

## 2. Preliminaries

All notions standard.

### 2.1 Orthomodular lattices, and the orthogonal/meet-zero gap

**Def 2.1 (Orthocomplemented lattice).** A bounded lattice (join `∨`, meet
`∧`, top `1`, bottom `0`) with `a ↦ a^⊥` satisfying (i) `a∧a^⊥=0`,
`a∨a^⊥=1`; (ii) `a^⊥⊥=a`; (iii) `a≤b ⟹ b^⊥≤a^⊥`.

**Def 2.2 (Orthogonal; meet-zero).** `a ⊥ b` if `a ≤ b^⊥`; *meet-zero* if
`a∧b=0`. **Orthogonal ⟹ meet-zero always; the converse holds in every
Boolean algebra but FAILS once non-distributive.** This gap drives
everything.

**Def 2.3 (Orthomodular lattice).** Orthocomplemented + `a≤b ⟹ b =
a∨(a^⊥∧b)`. Boolean = distributive special case. Motivating non-Boolean
example: `L(H)`.

**Example 2.4 (MOₙ, the gap made concrete).** `MOₙ` = `0`, `1`, and `n`
complementary pairs of incomparable atoms sharing only `0`,`1`.
Non-distributive for `n≥2`: any two distinct atoms have `a∧b=0` yet are
*not* orthogonal. `MO₃` is the smallest non-distributive OML.

**Def 2.5 (OMP; concrete logic).** Orthomodular *poset*: joins required
only for orthogonal pairs. *Concrete* (= set-representable): embeds in
`(P(X),⊆,complement)` preserving orthogonal joins.

**Remark 2.6 (Concreteness does not close the gap).** Set-representable
needs only complement + *disjoint*-union closure (Burešová–Pták);
intersection-closure would force Boolean. `MO₃` is *itself* concrete (Gudder
order-determining two-valued states), so the flagship meet-zero≠orthogonal
example is concrete. The gap closes under a *richness/atomicity* condition,
not concreteness; the abstract form `a∧b=0 ⟹ a⊥b` is Tkadlec's *Boolean
orthoposet* condition (≠ Boolean *algebra*).

### 2.2 The state / meet-additive / charge ladder

**Def 2.7 (State; meet-additive state; charge-extendible).** A *state*:
`s:A→[0,1]`, `s(1)=1`, additive on **orthogonal** pairs. Three
strengthenings, strictly increasing once non-distributive:
1. **State** — additive on orthogonal pairs.
2. **Meet-additive** — additive on every **meet-zero** pair (binary,
   stronger). We avoid "valuation": in lattice theory that denotes the
   modular function `v(a)+v(b)=v(a∧b)+v(a∨b)`, a different condition.
3. **Charge-extendible** — *n*-ary: `Σ s(aᵢ) ≤ 1` for every
   pairwise-meet-zero family. *This is the extension condition (§3).*

**Example 2.8 (Ladder is strict).** On MO₃, `s ≡ ½` is meet-additive but
fails (3) at `{p,q,r}` (`³⁄₂ > 1`). No state on MO₃ is charge-extendible.

### 2.3 The McDonald–Bimbó dual space

**Def 2.9 (Dual space; representation map).** MB duality assigns to `A` a
compact space `S₀(A) = (F(A), ⊆, ⊥_A, P(A), T(S))`, with `F(A)` the
*filters* and `P(A) ⊆ F(A)` the *principal* filters — the physical points,
the realisation datum (canonical here, unlike the Boolean pure points).
`h(a)={x∈F(A):a∈x}` is an OML iso onto the ⊥-stable clopens; set
`μ(h(a))=s(a)`.

**Remark 2.10 (The duality is finitary — the wall).** `h(⋁ₙ aₙ) =
(⋃ₙ h(aₙ))^⊥⊥` holds for *finite* joins, fails for countable — finitary
OML homs need not preserve infinite suprema. This is the wall the open
problem runs into. (It is a *countable*-join phenomenon, not specific to
joins: since `a ↦ a^⊥` is an order anti-isomorphism, `⋀ₙ aₙ = (⋁ₙ aₙ^⊥)^⊥`,
so the failure to preserve countable meets is its De Morgan dual — the wall
obstructs countable meets and joins together.) Cannon–Döring is also
finitary, no measure; MB chosen for carrying `P(A)` explicitly.

### 2.4 The Boolean engine: Loomis–Sikorski

In the Boolean case the descent argument ("σ-additive ⟺ measure
concentrates on the physical points") runs on a **Loomis–Sikorski**
representation: a σ-complete Boolean algebra is a σ-tribe of sets mod a
σ-ideal. **There is no OML analogue** — supplying one, or proving none
exists, is the open problem (§5). The Boolean proof has an engine; the OML
proof needs one and doesn't have it.

---

## 3. Two axes: extension and descent

The headline question — *when does a state `s` on OML `A` extend to a
σ-additive measure on `S₀(A)`?* — splits into two **independent** axes the
Boolean case fuses:

|             | **Extension axis** | **Descent axis** |
|-------------|--------------------|------------------|
| **Question**    | Does μ extend to a finitely additive charge on the FULL Boolean clopen algebra of S₀(A)? | Once extended, does the measure concentrate on the physical points P(A)? |
| **Governed by** | the meet-zero/orthogonal gap (§2.1) | σ-additivity — needs the missing engine (§2.4) |
| **Status**      | **settled**: Horn–Tarski/Pitowsky feasibility; finite case = decidable LP; can fail for every state. | **open**. *This is the residue.* |

**Prop 3.1 (Finite case).** For finite `A` the extension condition is a
decidable LP (Horn–Tarski / Pitowsky feasibility); since `h` preserves
meets, meet-zero elements map to disjoint clopens and a charge needs
`Σ s(aᵢ) ≤ 1` over pairwise-meet-zero families. Can fail for *every* state
(MO₃, Ex 2.8).

**Prop 3.2 (Infinite L(H), normal states).** For `dim H=∞`, any state with
`s(e)>0` for some finite-dimensional `e` fails to extend to a charge on `S₀(L(H))`;
in particular no normal (Gleason) state extends. *Proof sketch:* in a
2-plane `e`, `k` distinct lines give `2k` pairwise-meet-zero lines, forcing
`k·s(e) ≤ 1` for all `k`; take `k>1/s(e)`. Finitary; σ-completeness
irrelevant.

By Takesaki normal/singular decomposition (Mackey–Gleason/Bunce–Wright
lift, valid as `B(H)` has no type I₂ summand), the only escapees are the
**singular** states (`s(e)=0` for all finite-dimensional `e`; ultrafilter vector
states, Calkin pullbacks), forming a clean dichotomy with the normal
states. So the sole survivors on the extension axis are the singular states
of `L(H)` (§6). The genuine open problem lives on the descent axis (§5).

---

## 4. What is known

**4.1 Boolean benchmark.** Kelley–Vladimirov–Pták (Fremlin Thm 391D): a
Boolean algebra carries a strictly positive σ-additive measure iff Dedekind
σ-complete + weakly (σ,∞)-distributive + chargeable. No clean OML analogue:
weak (σ,∞)-distributivity relies on `⋀` over `⋁`; chargeability has no
structural OML characterisation.

**4.2 Positive / obstructive OML results.** Positive (need Hilbert-like
richness): Gleason (`L(H)`, σ-additive *on the lattice*), Bunce–Wright
(JBW), Chetcuti–Dvurečenskij. Obstructive: Pták–Pulmannová (forcing
σ-additivity collapses to Boolean), Navara (regularity ⇏ σ-additivity),
Pták (exotic state spaces via Greechie pasting).

**4.3 Three blocked routes to a σ-OML engine.**
(i) **RDP/effect-algebra** — Loomis–Sikorski holds for σ-MV and monotone
σ-effect algebras *with* RDP, but lattice-EA has RDP iff MV, and OML∩MV =
Boolean. So **OML+RDP ⟺ Boolean**.
(ii) **MacNeille completion** — need not be orthomodular (Harding); can't
complete to absorb joins.
(iii) **σ-Stone duality** — none exists. MB finitary (Rmk 2.10); Freytes
equational, no set/tribe representation.

**4.4 Prior art on point-free quantum probability.** Each construction
lands on one side of the σ-additivity-on-non-distributive line:
- **Gleason tradition** — σ-additive non-distributive, but real-valued on a
  fixed lattice, *not point-free*.
- **Döring 2009** — point-free on the spectral presheaf, but only *finitely
  additive*, on a distributive Heyting algebra.
- **Bohrification (HLS)** — point-free, internal valuation *is* σ-additive
  (Scott-continuous), but factors through an internally *distributive*
  locale, per commutative context. Non-distributivity tamed, not native.
- **Localic valuations** (Vickers, Simpson, Coquand–Spitters) — point-free
  σ-additive, but on *frames*, distributive by definition.
- **OML Stone dualities** (McDonald–Bimbó, Cannon–Döring) — purely
  structural, no measure, no σ-version.

The unoccupied conjunction — point-free × σ-additive × natively
non-distributive × directed-system-built — is exactly the descent residue.
(The directed-context⟹non-distributivity *idea* is not new — it's the shape
of Bohrification and colimit-over-Boolean-contexts generation. Novelty
would lie in the σ-additive-point-free-native combination.)

**Remark 4.1 (The boundary of the negative results).**
(i) *No impossibility theorem* covers the **concrete** class: known no-gos
are finite/two-valued, and the one positive occupant P(H)+Gleason is
*non-concrete* (Kochen–Specker), so concreteness is the qualifier on which
the open frontier turns. (ii) *The absence of a σ-Loomis–Sikorski* is
visible in the dualities themselves: both take infinite joins as a
*closure* not a union (Cannon–Döring `cls(⋃Sᵢ)`, MB `(⋃h(aₙ))^⊥⊥`). One
should not overstate this: Gudder concrete logics ARE set-representable
non-Boolean orthoposets — but as point-ful posets, not via a
σ-Loomis–Sikorski theorem.

---

## 5. The open problem

> **Does a σ-complete, concrete, non-Boolean, infinite OML admit a
> Loomis–Sikorski-type representation (a σ-tribe of sets mod a σ-ideal), or
> a countable-join-preserving σ-Stone duality — or can one prove none
> exists?**

A positive answer is the engine for *relational probability without
realisations*: σ-additive probability built from the entailment relation of
a non-distributive OML, not descended from any sample space — the
non-Boolean analogue of localic measure theory. A negative answer
(impossibility theorem) closes the whole cluster, both residues, at once.
Either way the outcome is decisive: no impossibility theorem is known for
the live class (Rmk 4.1), and all three constructive routes are blocked
(§4.3), so the state of the art is not "needs a new idea" but "needs a
representation bypassing all three blocked
routes."

**Remark 5.1 (Why L(H)+Gleason does NOT already settle this — the (A)/(B)
point-space equivocation).** The motivating idea ("probability from
relations, point-free") may *look* delivered by `L(H)`+Gleason. It is not.
**(A)** the Hilbert rays of `H`, from which the Gleason density `ρ` in
`s=tr(ρ·)` is built; **(B)** the MB dual filters `P(A)`. The programme
defines *realisation* = concentration on **(B)**. Gleason removes **(B)**
but *requires* **(A)** — and is a *representation* theorem (reduces every
lattice state to the point datum `ρ`, the most point-ful result available).
So `L(H)`/Gleason exhibits a *separation* — a σ-additive measure exists on
the lattice while none concentrates on the dual points `P(A)` — NOT
point-freeness, and cannot be the existence proof. Because it
cannot, the σ-OML representation is the *only* candidate engine; it would be
an error to regard Gleason's theorem as already furnishing a relational,
point-free probability.

---

## 6. Directions

Two lines of attack present themselves, both bounded by the same
finitary-to-σ obstruction.
- **The general construction** — construct a Loomis–Sikorski-type
  representation, or a countable-join-preserving σ-Stone duality, for a
  concrete non-Boolean infinite σ-OML, or prove none exists. This resolves
  the open problem directly, but no partial construction is currently in
  hand.
- **The singular case for L(H)** — determine whether a *singular*
  orthoadditive state on `L(H)` extends to a charge on `S₀(L(H))`: a
  question about one specific lattice, accessible to operator-algebraic
  methods (Calkin, Bunce–Wright, Takesaki), and conditionally
  self-contained (subject to the finite-versus-countable question below).

The singular case is the more tractable entry point, and it is informative
whichever way it resolves. If a singular state fails to extend, then by the
dichotomy following Prop 3.2 *no* state on `L(H)` extends; since the
singular states are the only remaining candidates for a state whose descent
behaviour is independent of extension, this would settle that subsidiary
question negatively. If a singular state does extend, it is the first
explicit example of a state that extends but may fail to concentrate on
`P(A)` — the motivating example the general construction lacks.

Whether the singular case is genuinely more tractable, however, turns on a
prior question.

> **Open Problem (finite versus countable).** Is the obstruction to
> extending a singular state on `L(H)` realised by a **finite** or only by
> a **countable** pairwise-meet-zero family?

Prop 3.2 is finitary — it uses finitely many lines in a single 2-plane —
which is why it avoids the descent-axis obstruction entirely. For singular
states the relevant pairwise-meet-zero families are infinite-dimensional
subspaces with trivial intersection, and the line argument is vacuous there
(`s(e)=0` on every finite-dimensional `e`). That the line argument is
vacuous does not, however, imply that the obstruction requires a countable
family: whether a *finite* family of infinite-dimensional pairwise-meet-zero
subspaces can force `Σᵢ s(aᵢ) > 1` is unsettled. If such a finite
obstruction exists, the singular case is a self-contained operator-algebraic
problem, separable from the general construction; if only a countable family
obstructs, it is governed by the same finitary-to-σ passage as the general
case. The question reduces, concretely, to whether orthoadditivity of a
singular state forces `Σᵢ s(aᵢ) > 1` on some finite family of
infinite-dimensional, pairwise-trivially-intersecting subspaces of `H`.
