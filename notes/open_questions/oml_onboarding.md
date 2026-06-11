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
kind extends, by an elementary finite construction. The *descent* axis is where
the genuinely open question lives, and we locate it precisely. The combinatorial
route — seeking the object among concrete, σ-orthocomplete, set-representable
OMLs — is **settled and does not produce it**: the interleaving property that
would make σ-additivity exceed finite additivity on a concrete non-Boolean
lattice is satisfied trivially by the plain product `∏ₙ MO₂`, which is concrete,
σ-complete, non-Boolean, infinite — and exactly the *segregated* object
(non-distributivity confined to finite blocks) that a relational probability
theory must exclude. The deeper reason is that a faithful σ-tribe representation
has a distributive image, forcing the OML Boolean, so the point-based route is
closed for every non-Boolean OML (and the witness `∏ₙ MO₂` has, concretely, no
two-valued homomorphisms at all); the forcing boundary to Boolean is
*subadditivity* of the separating states (Pták–Pulmannová), not σ-additivity. The open problem is therefore necessarily
**point-free**: does a non-Boolean, σ-complete OML carry a σ-additive probability
that is genuinely relational — the non-Boolean analogue of a localic (point-free)
measure — rather than reducible to a point space? The two richly non-distributive
poles frame it: `L(H)`+Gleason has a σ-additive lattice measure but is the *most*
point-ful object, not point-free (the (A)/(B) analysis of §5); the concrete
combinatorial objects are segregated. A positive answer is the non-Boolean
analogue of localic measure theory; a negative answer, an impossibility theorem
closing the cluster. We review what is known and what is ruled out, and close
with the directions in which the problem might be approached.

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

> **Open problem.** Does a *point-free*, non-distributive σ-additive probability
> theory exist? Concretely: is there a non-Boolean, σ-complete OML carrying a
> σ-additive probability that is genuinely *relational* — built from the
> entailment order of incompatible propositions, the non-Boolean analogue of a
> localic (point-free) measure — rather than reducible to a measure on an
> underlying point space? Or can one prove that any such structure collapses,
> either to a point space or to the Boolean case?

"Point-free" qualifies the *measure*, and it must negate *both* point-spaces of
Rmk 5.2: the measure must neither concentrate on the (B)-realisation (the dual
points `P(A)`) *nor* be built by reduction to the (A)-points (e.g. recovered as
`s = tr(ρ·)` from an underlying ray/density datum). Negating (B) alone is not
enough — `L(H)`+Gleason passes (B) (Prop 3.2: nothing concentrates on `P(A)`) yet
is the *most* (A)-ful object there is — so a witness must escape both, which is
what "genuinely relational" means here. The condition bites even when the lattice
itself happens to be set-representable: it is the *measure*, not the lattice, that
must be point-free. The localic framing is forced, not preferred, because the
point-based route is closed in advance. A full σ-tribe / Loomis–Sikorski
representation preserves `∧,∨` as `∩,∪`, so its image is a sublattice of a Boolean
algebra, hence distributive — forcing the OML Boolean (§2). So "relational
probability via a faithful set representation" is impossible by a one-line
argument for *any* non-Boolean OML; the only coherent target is the point-free
one, where the measure lives on the lattice (or its dual frame) without descending
to points. The two richly non-distributive poles frame
the difficulty: `L(H)`+Gleason gives a σ-additive measure on the lattice but is
*not* point-free — it is the *most* point-ful object available (Rmk 5.2, the
(A)/(B) analysis) — while the concrete combinatorial objects are *segregated*
(non-distributivity confined to finite blocks, the countable structure Boolean
across them, §5.1). The open problem is whether a genuinely point-free, genuinely
non-distributive σ-additive probability exists between these poles; a positive
answer is the non-Boolean analogue of localic measure theory, a negative one an
impossibility theorem closing the cluster.

### 5.1 What the combinatorial route settles, and why it is not enough

It is tempting to look for the object among concrete σ-*orthocomplete* OMLs, on
the grounds that a state's σ-additivity invokes `⋁ₙ aₙ` only for orthogonal
families (§2.1). **This route is settled, and it does not produce the object.**
The property that would make σ-additivity genuinely exceed finite additivity on a
concrete non-Boolean lattice is the interleaving condition

> (★) ∃ an element `p` and an **infinite** orthogonal family `{aₙ}` with
> `p ∧ aₙ = 0` for all `n`, yet `p ⊀ aₙ^⊥`,

and (★) is satisfied **trivially** by the plain product `∏ₙ MO₂`: take `aₙ = a`
in coordinate `n` (0 elsewhere), and `p = ⋁ₙ bₙ` where `bₙ = b` in coordinate `n`
(0 elsewhere) — a genuine countable *orthogonal* join, so `p = (b,b,b,…)` exists
by σ-orthocompleteness. Then `p ∧ aₙ = 0` (coordinate `n`: `a∧b = 0`; elsewhere
`aₙ=0`) and `p ⊀ aₙ^⊥` (coordinate `n`: `b ⊀ a^⊥`). Since `∏ₙ MO₂` is concrete,
σ-complete (a product of finite, hence complete, lattices), non-Boolean, and
infinite, it satisfies (★) and *every* combinatorial hypothesis one might
impose — yet it is exactly the *segregated* object the open problem must exclude.
So the combinatorial axioms (σ-completeness, concreteness, (★)) are *not* the
discriminator; the missing ingredient is non-segregation, a point-free notion,
not a closure property.

**Remark 5.1 (the witness has no points, and the Boolean boundary).** The
universal closure above (a faithful set representation forces distributivity)
already rules out the point-based route for every non-Boolean OML. The witness
`∏ₙ MO₂` shows the failure concretely and at the level of points: `MO₂` admits
**no** two-valued *homomorphism* — each of its four separating two-valued *states*
(`a↦0, b↦0`, etc.) fails `ω(a∨b) ≤ ω(a)+ω(b)` because `a∨b = 1`, so none
preserves `∨` — and `∏ₙ MO₂` inherits this, since its diagonal copy
`{⊥, ⊤, (a,a,…), (a^⊥,…), (b,b,…), (b^⊥,…)}` is a sub-`MO₂` on which any
homomorphism would restrict to one of `MO₂`'s (none exists). (This is special to
`MO₂` and its products — a generic non-Boolean OML such as `2 × MO₂` *does* carry
homomorphisms, e.g. the projection; the universal obstruction is the
distributivity argument, not homomorphism-scarcity.) So the witness is concrete
(order-determining two-valued *states*) and σ-complete yet has no points in the
homomorphism sense at all — the point-free target is forced, not engineered. The
same arithmetic records the sharp Boolean boundary: an OML is Boolean iff it
carries a unital set of *subadditive* states (Pták–Pulmannová 1994), so concrete
non-Boolean OMLs exist precisely *because* their separating two-valued states fail
subadditivity — and the forcing property is subadditivity, not σ-additivity.

**A worked instance (the cautionary example).** Navara's construction (1992)
produces an infinite, σ-orthocomplete, rich OML whose inner block is a finite
*stateless* Greechie logic — which is exactly what makes Navara's `L`
non-concrete. Replacing the stateless block by `MO₂` (write `L₂`) removes the
only source of non-concreteness: the assembly is a product of a sublogic of a
*Kalmbach horizontal sum* (blocks glued only at `{0,1}`, **not** an atom-sharing
Greechie loop), and pure horizontal sums of concrete logics are concrete, as are
sublogics and products. So `L₂` is concrete, σ-orthocomplete, non-Boolean, and
carries (★) — yet it is not a new object: it is `∏ₙ MO₂` with extra scaffolding,
segregated in the same way, and it likewise admits no σ-tribe representation. It
is the cautionary example: exhibiting (★) and concreteness together is easy and
does *not* reach the open problem. (Derivation history of this dead inhabitation
attempt:
`../archive/oml_descent_inhabitation_dead/inhabitation_check.md`.)

The art constrains the open (σ-complete) problem from both sides without closing
it: no impossibility theorem is known for the concrete class (Rmk 4.1), while the
two *theorem-closed* routes to a σ-OML engine — RDP and MacNeille (§4.3(i),(ii))
— are ruled out, leaving only σ-Stone duality (iii), which is itself open. What
is required is a representation that lives in that gap: non-distributive enough
to evade (i),(ii), yet σ-faithful where the known dualities are merely finitary.

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

With the extension axis closed on `L(H)` (Prop 3.2) and the combinatorial
(σ-orthocomplete, set-representable) route shown to deliver only segregated
objects (§5.1), the live problem is the point-free existence question of §5.
Three directions bear on it.
- **Build the point-free engine, or prove it collapses.** Seek a σ-additive
  probability on a non-Boolean σ-complete OML (or its dual frame) that does *not*
  descend to a point space — a genuine non-Boolean localic measure — or prove
  that any such structure collapses to a point space or to the Boolean case. The
  point-based form is already ruled out (Rmk 5.1: a faithful σ-tribe
  representation has a distributive image, forcing the OML Boolean — so no σ-tribe
  representation of a non-Boolean OML exists at any cardinality); the open content
  is whether the point-free form can be non-trivial, which is why the engine must
  be sought localically (route (iii), §4.3), not as a field of sets.
- **Settle the (A)/(B) status of `L(H)`+Gleason.** Decide whether `L(H)`+Gleason
  counts as a genuine point-free non-distributive σ-additive witness or is
  disqualified by the point-space equivocation (Rmk 5.2); if it counts, ask
  whether it is essentially unique. This is the same problem as the first item
  under a semantic rather than constructive description — "does point-free
  non-distributive σ-additive probability exist?" *is* the content of the
  localic-engine question — so progress on either informs the other.
- **Sharpen the impossibility side via subadditivity.** The Boolean boundary is
  subadditivity of the separating states (Pták–Pulmannová, Rmk 5.1). A negative
  resolution would likely run through the dual frame: quantify how far a
  non-Boolean OML's measures must fail subadditivity, and whether requiring a
  point-free σ-additive measure forces enough subadditive structure to collapse
  the object to a point space or to the Boolean case — the impossibility form of
  the open problem.

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
