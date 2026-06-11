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
genuinely open. There it splits into two coupled questions, distinguished by
which countable joins they require: a *structural* one — whether a σ-complete
OML admits a Loomis–Sikorski representation, neither constructed nor ruled out —
and a *descent-relevance* one on the weaker σ-orthocomplete class, which we show
is non-empty and (update 2026-06-10, §5 resolution box) whose `MO₂`-swap member
`𝓛₂` satisfies the interleaving condition (★) — so it does *not* segregate — but
whose **concreteness** is the remaining open question that decides everything.
The stake is more than
technical: a positive resolution would furnish a *point-free*, σ-additive
probability theory on a non-distributive lattice — the non-Boolean analogue of
localic measure theory — built from the entailment relation rather than
descended from a sample space. We review what is known and what is ruled out,
and close with the directions in which the open problem might be approached.

---

## 1. Introduction

All measurement is finite, yet the frameworks that organise empirical
knowledge rest on infinite structures. The passage requires a commitment
no finite evidence can compel. In probability theory the locus is
**countable additivity**:

$$A_1 \supseteq A_2 \supseteq \cdots, \quad \bigcap_n A_n = \varnothing
\quad\Longrightarrow\quad \mu(A_n) \to 0.$$

De Finetti held only finite additivity is empirically grounded; Kolmogorov
adopted σ-additivity as an axiom.

The same tension recurs once observations need not be jointly performable.
An observation *context* — a set of measurements that can be performed
together — is Boolean. Gluing contexts along their shared observations (a
categorical colimit) returns a Boolean algebra when the contexts are mutually
compatible, but a generically non-distributive **orthomodular lattice** (OML)
when they are not: Gunji et al. (2026) show the gluing produces an OML, and
the compatible/incompatible dichotomy is the organising point of Paper II.
The OML is forced by the context structure, not postulated; incompatibility —
quantum complementarity, but equally contextual experimental design or
interfering sensors — is what drives the observation algebra out of the
Boolean world. For the non-quantum examples the incompatibility must be
*operationally imposed* (contexts genuinely non-co-realizable, no joint
probability space): it cannot arise intrinsically from the dynamics of a
single classical system, since any finite family of classical observables on
a common space jointly distributes (Kolmogorov), hence stays Boolean —
contextuality there is failure of a global section (Abramsky–Brandenburger
2011; Fine 1982), a statement about non-co-realizable settings, not about one
underlying process. `L(H)` (closed subspaces of a Hilbert space, distributivity
failing) is the prototype, not the premise.

On any such OML, distributivity may fail, so Carathéodory's outer measure
does not apply. For the single lattice `L(H)` this is rescued by Gleason's
rigidity theorem; but Hilbert space is special, and for general OMLs no
analogue is known. Dropping distributivity does not by itself remove the
2-valued homomorphisms the Boolean engine needs — `MO₃` is non-distributive
yet still carries them (§2.1, §4) — but it removes the *guarantee*, and for
`L(H)` at `dim ≥ 3` they fail outright (Kochen–Specker, §4). Whether enough
survive is a question of concreteness, not non-distributivity — where an OML is
*concrete* (Def 2.5) when its elements model faithfully as honest *sets of
outcomes*, equivalently when it carries an order-determining set of two-valued
states (Gudder); "enough survive" is then almost the definition. This is the
qualifier on which the open problem turns (§4, §5).

This note asks the shared question — *when does finite coherence force
countable behaviour?* — in the OML setting. Our organising observation: the
question splits into two axes that the Boolean case fuses — an *extension*
axis, classical and fully settled (on `L(H)` no state extends), and a
*descent* axis that is genuinely open.

**The relational standpoint.** Two established moves motivate the approach.
De Finetti's operationalism founds probability without a presupposed sample
space: probabilities are coherent commitments about events, not measures on a
pre-given Ω. Quantum theory, since Birkhoff and von Neumann, reads
propositions as a lattice — the orthomodular lattice of §2 — rather than as
subsets of a phase space. Combining the two, we begin from the propositions
and their entailment order, not from a space of outcomes, and ask what that
relational structure alone determines. This is the measure-theoretic,
non-distributive counterpart of pointless (localic) topology, which recovers
spaces from their lattices of opens. The natural dual is then not a point
space but the McDonald–Bimbó space of *filters* (§2.3), and a positive answer
to the open problem would be a **point-free** σ-additive probability theory
on a non-distributive lattice — the non-Boolean analogue of localic measure
theory (§5). The standpoint is developed further in Paper I.

---

## 2. Preliminaries

### 2.1 Orthomodular lattices, and the orthogonal/meet-zero gap

*All notions standard. The one gap that classical logic lacks (Def 2.2) is
flagged where it first appears.*

**Def 2.1 (Orthocomplemented lattice).** A bounded lattice (join `∨`, meet
`∧`, top `1`, bottom `0`) with a negation `a ↦ a^⊥` satisfying

$$a \wedge a^\perp = 0, \quad a \vee a^\perp = 1, \quad a^{\perp\perp} = a,
\quad a \le b \Rightarrow b^\perp \le a^\perp.$$

*(The properties of Hilbert-space orthogonal complement that survive without
distributivity.)*

**Def 2.2 (Orthogonal; meet-zero).**

$$a \perp b \iff a \le b^\perp \quad(\text{one entails the other's negation
— decisively incompatible}); \qquad a \text{ meet-zero } b \iff a \wedge b =
0 \quad(\text{no common refinement, weaker}).$$

**Remark 2.2a (meet-zero versus orthogonal).** Orthogonal ⟹ meet-zero always;
the converse holds in every Boolean algebra but fails once the lattice is
non-distributive, where meet-zero is strictly weaker than orthogonality. The
distinctions developed below all turn on this separation.

**Def 2.3 (Orthomodular lattice).** Orthocomplemented, plus the orthomodular
law

$$a \le b \quad\Longrightarrow\quad b = a \vee (a^\perp \wedge b).$$

*(The controlled amount of distributivity quantum logic keeps.)* Boolean =
distributive special case. Motivating non-Boolean example: `L(H)`.

**Example 2.4 (MOₙ, the gap made concrete).** `MOₙ` = `0`, `1`, and `n`
complementary pairs of incomparable atoms sharing only `0`,`1`. *Picture `n`
lines through the origin: each line `a` is `⊥` to its perpendicular `a^⊥`,
but two atoms from distinct pairs are non-perpendicular lines —*

$$a \wedge b = 0 \quad(\text{meet only at the origin}) \qquad\text{yet}\qquad
a \not\perp b.$$

Non-distributive for `n≥2`; `MO₃` is the smallest non-distributive OML.

**Def 2.5 (OMP; concrete logic).** Orthomodular *poset*: joins required
only for orthogonal pairs. *Concrete* (= set-representable): embeds in

$$(P(X), \subseteq, \text{complement}) \quad\text{preserving orthogonal
joins}$$

— *its propositions model as actual sets of outcomes.* *(Concreteness
separates the open frontier from the settled cases, §5.)*

**Remark 2.6 (Concreteness does not close the gap).** Set-representable
needs only complement + *disjoint*-union closure (Burešová–Pták);
intersection-closure would force Boolean. `MO₃` is *itself* concrete (Gudder
1979, order-determining two-valued states), so the paradigmatic meet-zero≠orthogonal
example is concrete. The gap closes under a *richness/atomicity* condition,
not concreteness; the abstract form `a∧b=0 ⟹ a⊥b` is Tkadlec's *Boolean
orthoposet* condition (Tkadlec 1994; ≠ Boolean *algebra*).

### 2.2 The state / meet-additive / charge ladder

**Def 2.7 (State; meet-additive state; charge-extendible).** A *state* is a
map

$$s : A \to [0,1], \quad s(1) = 1, \quad s(a \vee b) = s(a) + s(b)
\text{ for } a \perp b.$$

*(Probability, but additivity is only guaranteed where propositions are
decisively incompatible.)* Three strengthenings, strictly increasing in
general (e.g. on MO₃, Ex 2.8), differing in **which** pairs additivity is
demanded on:
1. **State** — additive on orthogonal pairs.
2. **Meet-additive** — additive on every **meet-zero** pair (binary,
   stronger — it reaches the gap pairs of Def 2.2). We avoid "valuation": in
   lattice theory that denotes the modular function `v(a)+v(b) =
   v(a∧b)+v(a∨b)`, a different condition.
3. **Charge-extendible** — the *n*-ary version,

   $$\sum_i s(a_i) \le 1 \quad\text{for every pairwise-meet-zero family }
   \{a_i\}.$$

   *This is the extension condition (§3).*

**Example 2.8 (Ladder is strict).** On MO₃ the uniform assignment `s ≡ ½`
is meet-additive, but fails (3) on the three atoms `{p,q,r}`:

$$s(p) + s(q) + s(r) = \tfrac{3}{2} > 1.$$

No state on MO₃ is charge-extendible.

### 2.3 The McDonald–Bimbó dual space

**Def 2.9 (Dual space; representation map).** MB duality assigns to `A` a
compact space

$$S_0(A) = (F(A),\ \subseteq,\ \perp_A,\ P(A),\ T(S)),$$

with `F(A)` the *filters* and `P(A) ⊆ F(A)` the *principal* filters — the
physical points, the realisation datum (canonical here, unlike the Boolean
pure points). The representation map

$$h(a) = \{x \in F(A) : a \in x\}, \qquad \mu(h(a)) = s(a),$$

is an OML iso onto the ⊥-stable clopens, carrying a state `s` to a set
function `μ`. *(Read `h(a)` as "the points where `a` holds" — the open
problem is whether `μ` survives countable operations on these sets.)*

**Remark 2.10 (The duality is finitary — the wall).** The representation
respects *finite* joins,

$$h\Big(\bigvee_{n=1}^{N} a_n\Big) = \Big(\bigcup_{n=1}^{N}
h(a_n)\Big)^{\perp\perp},$$

but **fails** for countable ones — finitary OML homs need not preserve
infinite suprema. This is the wall the open problem runs into. (It is a
*countable*-join phenomenon, not specific to joins: since `a ↦ a^⊥` is an
order anti-isomorphism,

$$\bigwedge_n a_n = \Big(\bigvee_n a_n^\perp\Big)^\perp,$$

so the failure to preserve countable meets is the De Morgan dual — the wall
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
*The slogan: in the Boolean world "realised" bundles two properties that
quantum non-distributivity pulls apart.* The Boolean bridge fuses two
conditions on a realised point `x` — being *closed under countable meets*
and being *off the countable-join defect*,

$$x \ni \bigvee_n a_n \quad\Longrightarrow\quad x \ni a_n \text{ for some }
n \quad(\text{join-primeness});$$

Rao–Rao's "vanishes on meagre sets" is exactly their coincidence. In a
non-distributive OML they *split*: a principal filter `↑p` is always
meet-closed, yet may fail join-primeness —

$$p \le \bigvee_n a_n \quad\not\Longrightarrow\quad p \le a_n \text{ for any
} n \qquad\big(a_n = \mathrm{span}(e_n),\ p = \mathrm{span}(v),\ v = e_1 +
e_2\big).$$

Such `↑p` is a *realised* point sitting inside the join-defect

$$D = h\Big(\bigvee_n a_n\Big) \setminus \bigcup_n h(a_n),$$

and is topologically *isolated* in `S₀(L(H))`, so `D` is non-meagre — the
reverse of the Boolean nowhere-dense case. The category route (clopens mod
meagre) chokes on the same `D` as the measure route, and reduces to the
MacNeille completion (§4.3(ii)). See
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
| **Status**      | settled: Horn–Tarski/Pitowsky feasibility; finite case = decidable LP; can fail for every state. | open. |

The extension axis is the abstract form of the Bell question: extending a
finitely-additive assignment on incompatible propositions to a single joint
distribution is exactly the feasibility behind the Bell inequalities (Fine
1982: Bell model ⟺ joint distribution; Pitowsky 1989: Bell inequalities =
facets of a correlation polytope), and Bell + Kochen–Specker non-classicality
are jointly one extension problem for partial Boolean algebras
(Budroni–Morchio, arXiv:1010.4662, with the necessary-and-sufficient Horn–Tarski
conditions). The obstruction is the same *finitary* one — it does **not** reach
the σ-additive descent axis below.

**Prop 3.1 (Finite case).** For finite `A` the extension condition is a
decidable LP (Horn–Tarski / Pitowsky feasibility; Budroni–Morchio for the
partial-Boolean-algebra form); since `h` preserves
meets, meet-zero elements map to disjoint clopens and a charge needs
`Σ s(aᵢ) ≤ 1` over pairwise-meet-zero families. Can fail for *every* state
(MO₃, Ex 2.8).

**Prop 3.2 (Infinite L(H), all states).** For `dim H=∞`, *no* state on
`L(H)` — normal or singular — extends to a charge on `S₀(L(H))`.

*Proof.* *(The idea: hide a copy of MO₂ inside `L(H)` whose four atoms are
all infinite-dimensional, so even singular states must charge them.)* Write
`H = H₀ ⊗ ℂ²` with `H₀` infinite-dimensional and `e,f` an orthonormal basis
of `ℂ²`. The four infinite-dimensional subspaces

$$a_1 = H_0 \otimes \mathbb{C}e, \quad a_1^\perp = H_0 \otimes \mathbb{C}f,
\quad a_2 = H_0 \otimes \mathbb{C}(e+f), \quad a_2^\perp = H_0 \otimes
\mathbb{C}(e-f)$$

form a copy of `MO₂`: `a₁⊥a₁^⊥`, `a₂⊥a₂^⊥`, each pair joining to `H`, all
four *cross* pairs meet-zero (`aᵢ∩aⱼ=0`) but not orthogonal.
Orthoadditivity gives

$$s(a_i) + s(a_i^\perp) = s(H) = 1 \qquad(\text{uses only } s(1)=1 +
\text{additivity on orthogonal pairs — so } \textit{every} \text{ state}),$$

whence summing over the pairwise-meet-zero family `{a₁,a₁^⊥,a₂,a₂^⊥}`,

$$\sum_i s(a_i) = 2.$$

Since `h` preserves meets (filters are meet-closed), meet-zero elements map
to disjoint clopens, so any charge forces `Σ ≤ 1`. Contradiction. Finite
(`n=4`); σ-completeness irrelevant. ∎

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
`s(pᵢ)+s(pᵢ^⊥)=s(e₀)`, so a charge forces

$$k \cdot s(e_0) \le 1 \quad\text{for all } k \quad\Longrightarrow\quad
\text{impossible once } s(e_0) > 0.$$ Lifting via Mackey–Gleason/Bunce–Wright (`B(H)`
has no type I₂ summand) and the Takesaki decomposition identifies the
states reached — nonzero normal part, including every Gleason state — and
those missed — the purely singular ones (ultrafilter vector states, Calkin
pullbacks). Prop 3.2 subsumes this; the line argument is recorded for its
independent technique and because it locates the singular states. The
open problem is on the descent axis (§5).

---

## 4. What is known

The extension axis is settled — on `L(H)` no state extends (Prop 3.2); the
descent axis turns on whether the Boolean engine of §2.4 has an OML
analogue. Three things bear on that question: the Boolean benchmark such an
analogue would have to match, the partial OML results, and the routes already
known to be blocked.

**4.1 Boolean benchmark.** *(The target an OML engine would have to hit.)*
Kelley–Vladimirov–Pták (Fremlin Thm 391D): a Boolean algebra carries a
strictly positive σ-additive measure iff

$$\text{Dedekind } \sigma\text{-complete} \;+\; \text{weakly }
(\sigma,\infty)\text{-distributive} \;+\; \text{chargeable}.$$

No clean OML analogue: weak (σ,∞)-distributivity relies on `⋀` over `⋁`
(distributing meets over joins — exactly what non-distributivity denies);
chargeability has no structural OML characterisation.

**4.2 Positive / obstructive OML results.** Positive (need Hilbert-like
richness): Gleason (`L(H)`, σ-additive *on the lattice*), Bunce–Wright
(JBW), Chetcuti–Dvurečenskij. Obstructive: Pták–Pulmannová 1994
(*subadditive*-unitality collapses to Boolean — a **finitary** measure
condition `s(a∨b)≤s(a)+s(b)` + unitality, **no** σ-additivity or
countable joins; Theorem 1, lattice-only — the OMP version is *false*,
Müller's 1993 set-representable counterexample), Navara (regularity ⇏
σ-additivity), Pták (exotic state spaces via Greechie pasting).

**4.3 Three routes to a σ-OML engine, all unavailable.** The descent argument
needs an OML analogue of the Boolean engine — a σ-Stone duality, equivalently a
Loomis–Sikorski representation. The three known routes are all unavailable, but
not on the same footing: (i) and (ii) are closed by *theorem*; (iii) is *open*
(no construction known, none ruled out) — and is the Open Problem of §5 restated.
(i) **RDP/effect-algebra** — Loomis–Sikorski holds for σ-MV and monotone
σ-effect algebras *with* RDP, but lattice-EA has RDP iff MV, and OML∩MV =
Boolean, so the hypothesis that would buy the representation collapses the
class:

$$\text{OML} + \text{RDP} \iff \text{Boolean}.$$
(ii) **MacNeille completion** — need not be orthomodular (Harding); can't
complete to absorb joins. The topological version (clopens of S₀(A) mod the
meagre ideal) is the same completion in disguise and collapses
non-distributivity (Rmk 2.11).
(iii) **σ-Stone duality** — none *known*, none *ruled out*. The existing
dualities are finitary (MB, Rmk 2.10) or equational with no set/tribe
representation (Freytes), but no theorem forbids a countable-join-preserving
one. This is the open route = the Open Problem (§5).

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

The open case is their conjunction — point-free × σ-additive × natively
non-distributive × directed-system-built — satisfied by no existing
construction.
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
should not overstate this: Gudder's concrete logics (Gudder 1979) are
set-representable non-Boolean orthoposets — but as point-ful posets, not via
a σ-Loomis–Sikorski theorem.

---

## 5. The open problem

> **Two coupled questions, distinguished by which completeness they require.**
>
> **(Q1) Structural.** Does a *σ-complete*, concrete, non-Boolean, infinite OML
> admit a Loomis–Sikorski-type representation (a σ-tribe of sets mod a σ-ideal),
> or a countable-join-preserving σ-Stone duality — or can one prove none exists?
> (Open via route (iii), §4.3.)
>
> **(Q2) Descent-relevance.** The *σ-orthocomplete*, concrete, non-Boolean,
> infinite class is non-empty (`MO₂`-swap, below). Does any member *exercise
> descent* — carry an (★)-witness — or does every member segregate into a
> Boolean skeleton with merely decorative non-Boolean blocks?

The two ask for different objects because they invoke different countable joins:
a σ-tribe is closed under *all* countable unions (→ σ-complete, Q1), whereas a
state's σ-additivity invokes `⋁ₙ aₙ` *only* for orthogonal families (→
σ-orthocomplete, Q2). They coincide in the Boolean case — any countable family
orthogonalises, `bₙ = aₙ ∧ (a₁∨…∨aₙ₋₁)^⊥` — which is why the classical statement
fuses them; non-distributivity splits Q1 from Q2, as it splits extension from
descent (§3).

**Remark 5.0 (whether the class is inhabited).** A prior question is whether
the class contains an example that exercises the descent axis at all. A
member is descent-relevant only if it carries non-trivial countable
orthogonal structure (infinite pairwise-orthogonal families, so that
σ-additivity is more than finite additivity) and meet-zero≠orthogonal pairs.
The completeness the measure question requires is therefore
σ-*ortho*completeness (countable *orthogonal* joins), not full
σ-completeness, which is the stronger structural notion that the
Loomis–Sikorski representation manipulates. The obvious candidates do not
qualify: `MO_κ` (κ infinite) is concrete, infinite, non-Boolean and
complete, but its maximal pairwise-orthogonal family of nonzero elements has
only two members (`a⊥b` among atoms iff `a=b^⊥`), so descent is vacuous, and
it carries the `MO₂` obstruction (no state extends, as on `L(H)`).

The closest candidate is Navara's σ-orthocomplete lattice logic (Navara
1992): infinite, non-Boolean, and σ-orthocomplete, with rich countable
orthogonal structure, yet non-concrete, since its Greechie-stateless building
blocks leave too few two-valued states to be order-determining. Substituting
a concrete, stateful, non-Boolean block (`MO₂`) for Navara's stateless one
yields concreteness for free, since sub-OMPs and products of concrete logics
are concrete; and σ-orthocompleteness **survives** the substitution, since
Navara's closure argument (Navara 1992, p. 428) is state-free — the one step
that uses the block, "`f_j(m)=0` and `f_i ⊥ f_j` force `f_j` constant (`=0`)
on the block," carries verbatim for `MO₂`, where the only elements below
`a^⊥` are `{0, a^⊥}`. So `MO₂` is a genuine member of the class
{concrete, σ-orthocomplete, infinite, non-Boolean}: **non-emptiness of this
class is established** (no further check needed). Whether any member is
*descent-relevant* is a separate, open question.

The sharper question is whether any such member is descent-relevant in the
strong sense — the non-distributivity and the infinite orthogonal structure
**interleave**, rather than segregating into a Boolean support skeleton
carrying merely decorative non-Boolean blocks. The discriminating condition
is *element-versus-family*:

> (★) ∃ an element `p` and an **infinite** orthogonal family `{aₙ}` with
> `p ∧ aₙ = 0` for all `n`, yet `p ⊀ aₙ^⊥` (i.e. `p` is not orthogonal to
> any `aₙ`).

Within a single orthogonal family this never happens — such a family
generates a Boolean subalgebra, where meet-zero *is* orthogonality — so the
interleaving must be of one element *against* the family. On `L(H)`, (★)
holds: for an orthonormal basis `{eₙ}` and a skew vector `f = Σ cₙ eₙ` with
all `cₙ ≠ 0`, the ray `P_f` meets each `P_{eₙ}` at `0` yet is orthogonal to
none. On `MO_κ` it fails vacuously (no infinite orthogonal family).

For the `MO₂`-swap, (★) is **not** blocked by constancy, and there is an
explicit candidate witness. Navara's elements are `⋁_{C∈ℱ} v_C|C` with `ℱ`
mutually disjoint subsets of `M` (p. 428); an infinite orthogonal family
forces infinitely many disjoint `Cₙ` (`MO₂` caps within-block orthogonal
families at 2). Write `MO₂` atoms `a, a^⊥, b, b^⊥` with `a∧b = 0`, `a ⊀ b^⊥`.
Set `aₙ := a|Cₙ` and `p := ⋁ₙ b|Cₙ`. Constancy is **per coordinate** and the
`Cₙ` are disjoint, so `p` violates nothing; `p ∈ L` as a countable
orthogonal (disjoint-support) join, supplied by σ-orthocompleteness itself.
Coordinatewise in `W`: `p ∧ aₙ = 0` (on `Cₙ`, `a∧b=0`; off `Cₙ`, disjoint),
yet `p ⊀ aₙ^⊥` (on `Cₙ`, `a ⊀ b^⊥`). So **(★) holds in `W`**.

It remains only to determine whether this transfers to `L`. Navara warns "the
lattice operations in `L` do not coincide with those of `W`" (p. 428), and
orthogonality is defined through the orthocomplement. The whole question
reduces to one check:

> **(HINGE)** In `L`, is `a|C ⊀ (b|C)^⊥` — i.e. are distinct non-complementary
> `MO₂` atoms on the same `C` non-orthogonal in `L` (inheriting from `MO₂`)?

If (HINGE) holds, `p` witnesses (★): the swap is a concrete σ-orthocomplete
non-Boolean OML satisfying interleaving, the richness-starves-concreteness
conjecture is **false**, and the swap is the relational-probability object
sought. If `L`'s orthocomplement forces `a|C ⊥ b|C`, the swap **segregates**
and `L(H)` remains the only known witness. (Earlier framing — "open by an
element in `MO₂`-position in infinitely many blocks" — is resolved:
constancy *permits* it; the live hinge is the orthocomplement check, not the
support count.)

> **▶ RESOLUTION (2026-06-10) — (HINGE) = YES, but the deciding question is
> CONCRETENESS, not (HINGE).** Reading Navara p. 428 in full: `L` is a *sublogic
> of* `W` (order = restriction), closed under orthocomplements *in* `W`, and its
> countable orthogonal joins are computed *in* `W` (the closure proof says "let
> `f` be its join in `W`"). So `a|C ⊀ (b|C)^⊥` transfers from `MO₂`, (HINGE)
> holds, and `p = ⋁ₙ b|Cₙ` witnesses (★) in `L`. **However, this does NOT
> falsify the conjecture, because the conjecture is about *concrete* OMLs and
> (★) does not give concreteness.** Navara's block is Greechie *stateless*
> precisely to make `L` non-concrete; the `MO₂`-swap drops statelessness to *try*
> for concreteness, but the **horizontal-sum step** (`V` = pasting of `T×MO₂`
> copies — pasting destroys states) is exactly where concreteness can fail.
> "Sub-OMP of concrete is concrete" covers the product and sublogic steps, NOT
> the horizontal sum. **So the open problem is now: is `L_MO₂` concrete?** —
> the `/audit full` target. Canonical statement:
> `descent_axis_residue_post_kill.md`.
>
> **⛔ RESOLVED 2026-06-10 (`/audit full`, opus Agent — descent axis PARKED).**
> `L_MO₂` **IS** concrete, so the conjecture is FALSE as worded — but the lead is
> DEAD anyway, and the framing above contained a false premise. **(i)** `V` is a
> **Kalmbach horizontal sum (blocks glued only at {0,1})**, NOT atom-sharing
> Greechie pasting (Navara p. 428: "construct the horizontal sum 𝒱 … see [5]
> [=Kalmbach 1983]"). Pure horizontal sums of concretes are concrete; the
> horizontal sum was never the danger — **statelessness** was Navara's only
> source of non-concreteness, and the MO₂-swap removes it. Concreteness is then
> mechanical (MO₂ → 𝒯×MO₂ → hsum → `W=∏V` → `L⊆W`). **(ii)** No contribution:
> plain `∏ₙ MO₂` exhibits the whole bundle (concrete + σ-orthocomplete +
> non-Boolean + (★)) with zero Navara scaffolding (Types 1/3/5 FAIL on
> triviality). **(iii)** Already characterized, sharper — **Pták–Pulmannová 1994**:
> an OML is Boolean iff it has a unital set of *subadditive* measures; the
> Boolean-forcing property is **subadditivity**, not σ-additivity/concreteness.
> 6th death of the descent arc, NEW reason. Parked:
> `../covered_leads/descent_axis_residue_post_kill.md`.

One qualification carries over: `L(H)` and Navara fail to be concrete
for *different* reasons: for `L(H)` the orthogonal richness itself obstructs
two-valued states (Kochen–Specker colouring), whereas Navara's state-poverty
is imported with a finite, orthogonality-free stateless block. This sharpens
rather than replaces the one-example status of the
richness-obstructs-concreteness heuristic: `L(H)` alone, by Kochen–Specker,
both satisfies (★) and is non-concrete. (The σ-ortho-vs-σ-complete distinction
is now carried by the Q1/Q2 split of the problem statement above.) Details of
the substitution and the (★) reduction are recorded in
`verification/inhabitation_check.md`.

A positive answer would furnish a relational probability theory without
realisations: σ-additive probability built from the entailment relation of a
non-distributive OML rather than descended from a sample space — the
non-Boolean analogue of localic (pointless) measure theory. A negative
answer, in the form of an impossibility theorem, would close the entire
cluster at once. The present state of the art constrains the
problem from both sides without closing it: no impossibility theorem is known
for the concrete class (Rmk 4.1), while the two *theorem-closed* routes to a
σ-OML engine — RDP and MacNeille (§4.3(i),(ii)) — are ruled out, leaving only
σ-Stone duality (iii), which is itself open. What is required is a
representation that lives in that gap: non-distributive enough to evade
(i),(ii), yet σ-faithful where the known dualities are merely finitary.

**Remark 5.2 (Why L(H)+Gleason does not already settle this — the (A)/(B)
point-space equivocation).** The motivating idea ("probability from
relations, point-free") may *look* delivered by `L(H)`+Gleason. It is not,
and the reason is an equivocation between two point-spaces: (A) the
Hilbert rays of `H`, from which the Gleason density `ρ` in `s=tr(ρ·)` is
built, and (B) the MB dual filters `P(A)`. The programme defines
*realisation* as concentration on (B). Gleason removes (B) but *requires* (A)
— and is a *representation* theorem, reducing every lattice state to the
point datum `ρ`, the most point-ful result available.
So `L(H)`/Gleason exhibits a *separation* — a σ-additive measure exists on
the lattice (Gleason, for the normal states) while (by Prop 3.2) no state
of any kind even extends to a charge on `S₀(L(H))`, so a fortiori none
concentrates on the dual points `P(A)` — not
point-freeness, and it cannot serve as the existence proof sought. Because it
cannot, the σ-OML representation is the *only* candidate engine; it would be
an error to regard Gleason's theorem as already furnishing a relational,
point-free probability.

---

## 6. Directions

With the extension axis closed on `L(H)` (Prop 3.2), the descent axis remains,
entered through either of its two coupled questions (§5).
- **The hinge check (Q2)** — ✅ **RESOLVED YES (2026-06-10).** Distinct
  non-complementary `MO₂` atoms on a common coordinate *do* stay non-orthogonal
  in Navara's `L` (order/orthocomplement/orthogonal-join all restrict
  coordinatewise from `W`, p. 428), so `𝓛₂` satisfies (★) and segregation is
  refuted. **This is no longer the entry point.** The new near-term question is
  **concreteness (Q3, below)** — whether the horizontal-sum step keeps `𝓛₂`
  concrete; that, not the hinge, decides whether the conjecture is false and
  whether there is a contribution. See the §5 resolution box and
  `../covered_leads/descent_axis_residue_post_kill.md`.
- **The concreteness check (Q3) — ⛔ RESOLVED 2026-06-10, axis PARKED.** `𝓛₂`
  **IS** concrete (conjecture FALSE as worded), but the lead is DEAD: the §5-box
  framing had a false premise — `V` is a **Kalmbach horizontal sum (glued at
  {0,1})**, NOT Greechie atom-sharing, so it does not destroy states;
  statelessness was Navara's only obstruction, and the MO₂-swap removes it. The
  result is then trivial (plain `∏ₙ MO₂` has the bundle) and already characterized
  (**Pták–Pulmannová 1994**: *subadditivity*, not σ-additivity, is the
  Boolean-forcing property). No contribution. Parked:
  `../covered_leads/descent_axis_residue_post_kill.md`.
- **The general construction (Q1)** — construct a Loomis–Sikorski-type
  representation, or a countable-join-preserving σ-Stone duality, for a
  concrete non-Boolean infinite *σ-complete* OML, or prove none exists. This
  resolves the structural question directly, but no partial construction is
  currently in hand. This is the deeper open case on the *descent* axis: the obstruction
  is the failure of `h` to preserve countable joins (§2.3), not the
  orthogonal/meet-zero gap, so Prop 3.2 does not reach it.

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
> (`n=4`) pairwise-meet-zero family forcing `Σᵢ s(aᵢ) = 2`,
> state-independently. So the singular case is self-contained and finitary,
> separable from the general construction — not governed by the
> finitary-to-σ passage at all. The line argument is vacuous on singular
> states; the `MO₂`-with-infinite-dimensional-atoms argument is not, and
> that is the whole difference.
