# σ-Additive Probability on Orthomodular Lattices: A Survey and an Open Problem

*Survey note — June 2026. Markdown twin of `oml_onboarding.tex`; the .tex
is the typeset authority (numbered definitions, full bibliography).*

**Abstract.** The passage from a finitely coherent assignment of
probabilities to a countably additive measure is, in the Boolean case,
governed by a single condition (countable additivity) and executed by
classical machinery (Carathéodory; Loomis–Sikorski; Stone duality). On a
*non-distributive* orthomodular lattice (OML) — the algebra of propositions
of a quantum system — this machinery breaks, and the question of when
finite coherence forces countable behaviour is open. We survey the problem
at the level needed to begin work on it. After fixing the apparatus
(orthomodular lattices, the gap between orthogonality and meet-zero, the
state/meet-additive/charge ladder, the McDonald–Bimbó dual space), we
separate the question into two axes. The *extension* axis is classical
(Horn–Tarski feasibility) and fully settled: on `L(H)` no state of any
kind extends, by an elementary finite construction; the *descent* axis is
genuinely open and rests on a representation that does not exist: a
Loomis–Sikorski theorem for σ-complete OMLs. The stake is more than technical: such a representation
would furnish a *point-free*, σ-additive probability theory on a
non-distributive lattice — the non-Boolean analogue of localic measure
theory — built from the entailment relation rather than descended from a
sample space. We review what is known and what is ruled out, and close with
the two directions in which the open problem might be approached.

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
question splits into two axes that the Boolean case fuses — an *extension*
axis, classical and fully settled (on `L(H)` no state extends), and a
*descent* axis that is genuinely open.

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
Non-distributive for `n≥2`: two atoms from *distinct* complementary pairs
have `a∧b=0` yet are *not* orthogonal. `MO₃` is the smallest
non-distributive OML.

**Def 2.5 (OMP; concrete logic).** Orthomodular *poset*: joins required
only for orthogonal pairs. *Concrete* (= set-representable): embeds in
`(P(X),⊆,complement)` preserving orthogonal joins.

**Remark 2.6 (Concreteness does not close the gap).** Set-representable
needs only complement + *disjoint*-union closure (Burešová–Pták);
intersection-closure would force Boolean. `MO₃` is *itself* concrete (Gudder
order-determining two-valued states), so the paradigmatic meet-zero≠orthogonal
example is concrete. The gap closes under a *richness/atomicity* condition,
not concreteness; the abstract form `a∧b=0 ⟹ a⊥b` is Tkadlec's *Boolean
orthoposet* condition (≠ Boolean *algebra*).

### 2.2 The state / meet-additive / charge ladder

**Def 2.7 (State; meet-additive state; charge-extendible).** A *state*:
`s:A→[0,1]`, `s(1)=1`, additive on **orthogonal** pairs. Three
strengthenings, strictly increasing in general (e.g. on MO₃, Ex 2.8):
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

### 2.4 The Boolean engine: Stone duality

In the Boolean case the descent argument ("σ-additive ⟺ measure
concentrates on the physical points") runs on **Stone duality**: a Boolean
event algebra embeds in the clopen algebra of its Stone space, a charge
extends to a Baire measure there (Carathéodory), and σ-additivity is
equivalent to concentration on the realised points (Paper I). That
σ-additive step is realised measure-theoretically by the meagre-sets
characterization (Rao–Rao): the measure vanishes on meagre Baire sets,
equivalently lives on the ultrafilters closed under countable intersection
— exactly the realised points. This is the measure-theoretic face of the
**Loomis–Sikorski** representation — a σ-complete Boolean algebra is a
σ-tribe of sets mod a σ-ideal — the countable-join bookkeeping that makes
the equivalence go through. **There is no OML analogue of any of this** —
supplying one, or proving none exists, is the open problem (§5). The
Boolean proof has an engine; the OML proof needs one and doesn't have it.

**Remark 2.11 (why the bridge breaks: meet-closed but not join-prime).**
The Boolean bridge fuses two conditions on a realised point `x`: being
*closed under countable meets* and being *off the countable-join defect*
(`x ∋ ⋁aₙ ⟹ x ∋ aₙ` for some `n`); Rao–Rao's "vanishes on meagre sets" is
their coincidence. In a non-distributive OML they *split*: a principal
filter `↑p` is always meet-closed, yet may fail join-primeness (`p ≤ ⋁aₙ`
does not force `p ≤ aₙ` for any `n`; take `aₙ=span(eₙ)` and `p=span(v)` for
any line not basis-aligned — already `v=e₁+e₂`). Such `↑p` is a *realised* point sitting inside the
join-defect `D = h(⋁aₙ)∖⋃h(aₙ)`, and is topologically *isolated* in
`S₀(L(H))`, so `D` is non-meagre — the reverse of the Boolean nowhere-dense
case. The category route (clopens mod meagre) chokes on the same `D` as the
measure route, and reduces to the MacNeille completion (§4.3(ii)). See
`verification/meagre_vs_measure_check.md`.

---

## 3. Two axes: extension and descent

The central question — *when does a state `s` on OML `A` extend to a
σ-additive measure on `S₀(A)`?* — splits into two **independent** axes the
Boolean case fuses:

|             | **Extension axis** | **Descent axis** |
|-------------|--------------------|------------------|
| **Question**    | Does μ extend to a finitely additive charge on the FULL Boolean clopen algebra of S₀(A)? | Once extended, does the measure concentrate on the physical points P(A)? |
| **Governed by** | the meet-zero/orthogonal gap (§2.1) | σ-additivity — needs the missing engine (§2.4) |
| **Status**      | **settled**: Horn–Tarski/Pitowsky feasibility; finite case = decidable LP; can fail for every state. | **open**. *The descent residue.* |

**Prop 3.1 (Finite case).** For finite `A` the extension condition is a
decidable LP (Horn–Tarski / Pitowsky feasibility); since `h` preserves
meets, meet-zero elements map to disjoint clopens and a charge needs
`Σ s(aᵢ) ≤ 1` over pairwise-meet-zero families. Can fail for *every* state
(MO₃, Ex 2.8).

**Prop 3.2 (Infinite L(H), all states).** For `dim H=∞`, *no* state on
`L(H)` — normal or singular — extends to a charge on `S₀(L(H))`. *Proof:*
write `H = H₀ ⊗ ℂ²` with `H₀` infinite-dimensional and `e,f` an
orthonormal basis of `ℂ²`. The four infinite-dimensional subspaces
`a₁ = H₀⊗ℂe`, `a₁^⊥ = H₀⊗ℂf`, `a₂ = H₀⊗ℂ(e+f)`, `a₂^⊥ = H₀⊗ℂ(e−f)` form a
copy of `MO₂`: `a₁⊥a₁^⊥`, `a₂⊥a₂^⊥`, each pair joining to `H`, all four
*cross* pairs meet-zero (`aᵢ∩aⱼ=0`) but not orthogonal. Orthoadditivity
gives `s(aᵢ)+s(aᵢ^⊥)=s(H)=1` (uses only `s(1)=1` + additivity on
orthogonal pairs — so *every* state), whence `Σ s(aᵢ)=2` over the
pairwise-meet-zero family. Since `h` preserves meets (filters are
meet-closed), meet-zero elements map to disjoint clopens, so any charge
forces `Σ ≤ 1`. Contradiction. Finite (`n=4`); σ-completeness irrelevant.

The `MO₂` count is folklore (orthoadditivity + `s(1)=1`; cf. Kalmbach
1983), and `Σ s(aᵢ)=2` is already state-independent in `L(ℂ²)`. What it
buys *here* is reaching the states that vanish on finite rank. In `L(ℂ²)`
the atoms are lines (finite rank), so a singular state (`s(e)=0` on every
finite-dim `e`) assigns them `0` and the count, though valid, says nothing
— it constrains only states positive on finite rank. Infinite-dimensional
`H₀` keeps the atoms infinite-dim, so `s(aᵢ)+s(aᵢ^⊥)=1` regardless of
behaviour on finite rank — dropping the finite-rank precondition of the
line argument (Rem 3.3) and catching singular states too. That is what
closes the extension axis on `L(H)` completely.

*Alternative argument, normal states only (Rem 3.3).* If `s(e)>0` on some
finite-dim `e`, fix a 2-plane `e₀` where `s>0`; `k` pairwise-non-orthogonal
lines in `e₀` give `2k` distinct pairwise-meet-zero lines with
`s(pᵢ)+s(pᵢ^⊥)=s(e₀)`, so a charge forces `k·s(e₀) ≤ 1` for all `k` —
impossible once `s(e₀)>0`. Lifting via Mackey–Gleason/Bunce–Wright (`B(H)`
has no type I₂ summand) and the Takesaki decomposition identifies the
states reached — nonzero normal part, including every Gleason state — and
those missed — the purely singular ones (ultrafilter vector states, Calkin
pullbacks). Prop 3.2 subsumes this; the line argument is recorded for its
independent technique and because it locates the singular states. The
genuine open problem lives on the descent axis (§5).

---

## 4. What is known

The extension axis is settled — on `L(H)` no state extends (Prop 3.2); the
descent axis turns on whether the Boolean engine of §2.4 has an OML
analogue. We survey what the literature supplies on that question — the
Boolean benchmark it would have to match, the partial OML results, and the
routes already known to be blocked.

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

**4.3 Three blocked routes to a σ-OML engine.** The descent argument needs
an OML analogue of the Boolean engine — a σ-Stone duality, equivalently a
Loomis–Sikorski representation. The three known routes are all blocked.
(i) **RDP/effect-algebra** — Loomis–Sikorski holds for σ-MV and monotone
σ-effect algebras *with* RDP, but lattice-EA has RDP iff MV, and OML∩MV =
Boolean. So **OML+RDP ⟺ Boolean**.
(ii) **MacNeille completion** — need not be orthomodular (Harding); can't
complete to absorb joins. The topological version (clopens of S₀(A) mod the
meagre ideal) is the same completion in disguise and collapses
non-distributivity (Rmk 2.11).
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
are finite/two-valued, and the one positive occupant L(H)+Gleason is
*non-concrete* (Kochen–Specker, dim ≥ 3: L(H) admits no two-valued states
at all, a fortiori none order-determining), so concreteness is the qualifier on which
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
the lattice (Gleason, for the normal states) while (by Prop 3.2) no state
of any kind even extends to a charge on `S₀(L(H))`, so a fortiori none
concentrates on the dual points `P(A)` — NOT
point-freeness, and cannot be the existence proof. Because it
cannot, the σ-OML representation is the *only* candidate engine; it would be
an error to regard Gleason's theorem as already furnishing a relational,
point-free probability.

---

## 6. Directions

With the extension axis closed on `L(H)` (Prop 3.2), a single direction
remains.
- **The general construction** — construct a Loomis–Sikorski-type
  representation, or a countable-join-preserving σ-Stone duality, for a
  concrete non-Boolean infinite σ-OML, or prove none exists. This resolves
  the open problem directly, but no partial construction is currently in
  hand. This is the *descent*-axis residue: the obstruction is the failure
  of `h` to preserve countable joins (§2.3), not the orthogonal/meet-zero
  gap, so Prop 3.2 does not reach it.

The other candidate direction — the singular case for `L(H)` — is now
closed, and the way it closed is instructive. One might hope a *singular*
state would extend even though no normal state does, furnishing the first
explicit "extends but may fail to concentrate" example the general
construction lacks. It does not: Prop 3.2 catches every state, singular
included.

> **Finite versus countable: finite suffices.** One could ask whether the
> obstruction to extending a singular state is realised by a **finite** or
> only by a **countable** pairwise-meet-zero family. The line argument
> (Rem 3.3) is finitary but vacuous on singular states (`s(e)=0` on every
> finite-dim `e`), which might suggest the singular obstruction needs a
> countable family and is entangled with the descent-axis passage. It does
> not: the four infinite-dimensional subspaces of Prop 3.2 are a **finite**
> (`n=4`) pairwise-meet-zero family forcing `Σᵢ s(aᵢ)=2`,
> state-independently. So the singular case is self-contained and finitary,
> separable from the general construction — not governed by the
> finitary-to-σ passage at all. The line argument is vacuous on singular
> states; the `MO₂`-with-infinite-dimensional-atoms argument is not, and
> that is the whole difference.
