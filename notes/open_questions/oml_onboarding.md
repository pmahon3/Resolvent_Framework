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
*subadditivity* of the separating states (Pták–Pulmannová), not σ-additivity. Read
"relational" as **no hidden realisation** — the measure not recoverable from a
posited auxiliary space of definite states — which, by Fine's theorem, is exactly
a *contextual* state: one not in the closed convex hull of the lattice's
dispersion-free states. The open problem is then sharp: **does a non-Boolean,
σ-complete, concrete OML carry a σ-additive contextual state whose contextuality is
σ-essential** (witnessed by no finite sub-OML)? The finite version is *already
settled* — Wright's pentagon is a finite concrete OML with a contextual state — so
the live content is the σ-essential refinement, a *compactness failure* of exactly
the Paper I (CE) type that rejoins the programme's origin. The state of the
question: well-posed and principled but *uninhabited* — no witness (`∏ₙ MO₂` fails
it; Wright is finite), no impossibility proof. A positive answer is the non-Boolean
analogue of localic measure theory; a negative one a σ-essential impossibility
theorem, reinstating empiricist-underdetermination as a theorem. We review what is
known and ruled out, and close with the two exits.

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
to the open problem would be a **relational** σ-additive probability theory
on a non-distributive lattice — the non-Boolean analogue of localic measure
theory. (The §5 statement makes "relational" precise as a *contextual* state,
no hidden realisation.) The standpoint is developed further in Paper I.

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

The **"sharp-skeleton" evasion** (represent the OML as the *sharp* elements of an
ambient RDP effect algebra, so only the ambient carries RDP, not the OML) also
**closes**: in any RDP effect algebra the sharp elements coincide with the center
and are therefore Boolean (Jenča 2001, Cor. 4.3 — `a` sharp ⟺ central ⟺ principal,
given RDP — via Greechie–Foulis–Pulmannová 1995, *The center of an effect algebra*,
Order 12). A non-Boolean sharp skeleton in fact *witnesses* RDP-failure (Jenča 2001,
Ex. 5.7). So route (i) is closed against this refinement too. *(σ-completeness is not
on the load path — "Boolean" suffices for the kill. Verdict:
`sharp_skeleton_RDP_subroute_verdict.md`.)*
(ii) **MacNeille completion** — need not be orthomodular (Harding); can't
complete to absorb joins. The topological version (clopens of S₀(A) mod the
meagre ideal) is the same completion in disguise and collapses
non-distributivity (Rmk 2.11).
(iii) **σ-Stone duality** — none *known*, none *ruled out*. The existing
dualities are finitary (MB, Rmk 2.10) or equational with no set/tribe
representation (Freytes), but no theorem forbids a countable-join-preserving
one. This is the open route = the Open Problem (§5).
**[ORIENTATION POLE — the standing target across sessions.** Route (iii) =
"is there a σ-Loomis–Sikorski for *concrete* OMLs?" is the live objective. Two
fences: (a) the *faithful* σ-tribe (∧,∨ → ∩,∪) is Boolean-forcing by §5.1, CLOSED;
the open object is the non-faithful concrete logic. (b) The obstruction is NOT the
representation/join — ∏ₙMO₂ already has a concrete non-union join and still fails;
the teeth are off-center σ-essential contextuality on an *irreducible* concrete
σ-complete OML (non-band generators, HW Problem 2, untooled). NB ⊥⊥-closure joins
are a dead end here (`X^⊥⊥=X` in a concrete logic; ⊥⊥ lives in non-concrete L(H)).**]

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

**The topos route, read for the mechanism (does/doesn't buy).** The
topos/Bohrification programme is the one machinery supplying a point-free *and*
σ-additive (directed-continuous) valuation on a quantum logic, so it is the
candidate to crack route (iii). A primary-source read settles it as **the same
wall, with tools**: the σ-additive valuation always lives on a *distributive*
object, and the bridge to the non-distributive lattice routes its countable
additivity through per-context Boolean blocks. (Verdict log:
`verification/topos_route_read_2026-06-19.md`.)
- **Bohrification (HLS, "Bohrification", arXiv:0909.3468; Def/Thm numbers from
  this chapter, not the CMP "A topos for algebraic quantum theory").** A state becomes a *continuous
  probability valuation* `μ : O(Σ(A)) → [0,1]_l` on the internal Gelfand
  spectrum `Σ(A)` — an internal **locale** (compact regular *frame*), hence
  distributive. The continuity axiom `μ(⋁ᵢUᵢ)=⋁ᵢμ(Uᵢ)` for directed families
  (Def 6.11) *is* the localic Scott-continuous form of σ-additivity — but on a
  frame, where `⋁` is distributive. Non-commutativity sits in the base poset
  `𝒞(A)` and the internal intuitionistic logic; the valuation never integrates
  over a non-distributive lattice.
  - *Objection (Thm 6.19).* HLS bijects valuations on `Σ(A)` with probability
    *measures on `Proj(A)`* — the non-distributive object — so it *looks* like a
    σ-measure on a non-distributive OML. **Defused, two independent ways.**
    (1) *σ-essential (primary, concreteness-free):* by Def 6.17(a) such a measure
    restricts to a σ-Boolean morphism *on every countably complete Boolean
    sublattice* — its countable additivity is defined block-by-block and glued by
    naturality over `𝒞(A)`, never crossing a non-distributive join. That is the
    **antithesis** of σ-essential contextuality (the prize wants contextuality
    witnessed by no Boolean sub-structure; the topos route puts *all* its
    σ-additivity *inside* Boolean blocks). (2) *Non-concrete (secondary):*
    `Proj(A)` is the Gleason/`L(H)`-type lattice, non-concrete by Kochen–Specker
    — Bohrification *recasts the Gleason occupant* in topos language; it does not
    reach the concrete class.
- **Döring–Isham (spectral presheaf, arXiv:0809.4847).** Measures live on
  `Sub_cl(Σ)`, a complete Heyting algebra / locale — distributive, explicitly
  *not* a σ-algebra. `Proj(H)` enters only via *daseinisation*
  `δ : Proj(H) → Sub_cl(Σ)`, a coarse-graining, *not* a homomorphism: outer `δ^o`
  preserves all joins but not meets, inner `δ^i` all meets but not joins, and
  (Wolters, arXiv:1010.2031) *"it cannot preserve both, as `Sub_cl(Σ)` is
  distributive whereas `Proj(H)` is non-distributive"* — the exact topos twin of
  the finitary-duality wall (Rmk 2.10). The measure is only *finitely* additive
  (ceiling driven by the state class — type III/KMS/non-normal); σ-additivity is
  recovered only *locally*, for families orthogonal at one context `V` (one
  Boolean block) and only for normal states.
- **f.a.-vs-σ diagnosis.** σ-additivity is available *precisely where the object
  is distributive* (internal frame, or per-context Boolean blocks where
  Loomis–Sikorski already applies — "the first arrow is free"), and degrades to
  finite additivity exactly when one global measure is demanded across the
  non-distributive whole. Of the four requirements the route satisfies three and
  misses *native non-distributivity* — the crux. It **sidesteps** the wall (an
  internally distributive spectrum is a design goal) rather than **settling** the
  σ-essential question, which stays open.

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

> **Open problem.** Is there a non-Boolean, σ-complete, *concrete* OML carrying a
> σ-additive *contextual* state — a state with no global hidden joint distribution,
> equivalently one not in the closed convex hull of the lattice's dispersion-free
> (2-valued) states — whose contextuality is *σ-essential*, i.e. witnessed by no
> finite sub-OML? Or can one prove no such state exists?

This is the relational-probability prize made precise. "Relational" means **no
hidden realisation**: the measure must not be recoverable from positing an
auxiliary space of definite states behind the propositions. **Three point-spaces
must be kept apart** (the recurring trap of this subject): the *canonical* dual
`P(A) = {↑p}` (one principal filter per *element*, §2.3); the *dispersion-free
states* (2-valued states, one per consistent global *valuation* — the
hidden-variable points); and the *external (A)-points* (Gleason's Hilbert rays,
Rmk 5.2). The canonical `P(A)` is *permitted*; the objection is only to building
the measure on a *smuggled* space — the (A)-points, or equivalently a global
hidden-variable joint over the dispersion-free states. A state has a hidden
realisation exactly when it is a mixture of dispersion-free states (Fine's
theorem), so a relational measure *is* a contextual state, and the reduction below
makes the existence question this one. (This is a condition on the dispersion-free
states, *not* on `P(A)`: a witness is point-rich on `P(A)` yet has no global
dispersion-free joint — the two spaces are different, which is exactly why
"permitted" and "escaped" do not conflict.) *(We do not pursue the
stricter "no canonical points either" reading: it makes concreteness itself the
enemy and collapses against the universal below, so it offers no inhabitable
target.)*

### 5.1 The reduction to contextuality, and what frames it

**The universal floor.** A *faithful set representation* (σ-tribe / Loomis–Sikorski,
preserving `∧,∨` as `∩,∪`) has a distributive image, so it forces the OML Boolean
(§2). Hence no non-Boolean OML admits one, and a relational measure can never arise
from a faithful descent to points. What a concrete OML *does* have is an
order-determining family of dispersion-free states; the live question is whether
every state is built from them.

**The reduction.** A σ-additive state `w` on a concrete OML is *non-contextual* iff
it lies in the closed convex hull of the dispersion-free states iff it admits a
global hidden joint. So

> relational (no hidden realisation) ⟺ contextual (not spanned by dispersion-free states).

The handle is *spanning*, not simplicity — non-uniqueness of the decomposition is
irrelevant; only *existence* of a dispersion-free decomposition matters. The prize
is a concrete σ-complete OML with a σ-additive state outside the dispersion-free
hull.

**Why σ-essential, and why it is principled.** The finite version is *already
inhabited*: Wright's pentagon (Wright 1978) is a finite, concrete OML (a Greechie
loop of length five, hence a lattice) with a separating family of dispersion-free
states yet a state outside their hull — a contextual state. So "concrete OML with a
contextual state" is a 1978 fact, and the general spanning theorem is
correspondingly false. What Wright does *not* supply is contextuality that
*requires* the countable structure: the pentagon's is witnessed by a finite
sub-OML (itself). The prize must therefore be **σ-essential** — contextual in the
σ-complete whole but in no finite sub-OML. This is not a device to evade Wright:
"every finite piece has a global section, the countable whole has none" is a
*compactness failure*, the same finite-additivity-has-compactness /
σ-additivity-lacks-it structure that is the core of Paper I (CE). The descent
question thereby rejoins the programme's origin.

**Status.** The σ-essential cell has *no known inhabitant* and *no impossibility
proof*. `∏ₙ MO₂` provably fails it (its contextual states are only finitely
additive — diffuse states on its central `P(ℕ)`; σ-additivity forces concentration
on points and kills them); Wright is finite; no construction is in hand. The
question is well-posed and principled but uninhabited. *(Computations and the
literature verdict: companion notes `reading1_prize_reduction.md` and
`direction2_gate_finding.md`.)*

### 5.2 What the combinatorial route settles, and why it is not enough

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

With the extension axis closed on `L(H)` (Prop 3.2), the combinatorial route shown
to deliver only segregated objects (§5.2), and the prize reduced to a σ-essential
contextual state (§5.1), the problem has a clean win/kill dichotomy. Two exits,
each a genuine terminus. *(Pen-and-paper kit:* `problemset_oml_descent.{tex,pdf}` —
a self-contained working problem-set with the apparatus, the formal target, and
these exits as concrete sub-tasks.)*

**Exhibit a σ-essential witness.** Construct an infinite concrete OML carrying a
σ-additive contextual state that no finite sub-OML witnesses — the relational
prize. The likely attack is a compactness-failure construction in the CE mould: a
concrete σ-complete OML whose finite sublogics are all classically interpretable
(dispersion-free states span them), but whose countable joins force a
Kochen–Specker-type obstruction only in the limit. The faithful set representation
is ruled out at every stage (§5.1), so the obstruction must be carried by the
σ-structure itself, not by any finite block. *Target sharpened (CE-routing
subsession, 2026-06-12): the witness must put its infinitary structure
**off-center** (irreducible / non-central-infinite) — a product of finite blocks
like ∏ₙMO₂ is excluded a priori, since it forces all infinitary content into the
Boolean center where the Stone argument kills it. Pasting / countable colimit of
Wright-type blocks is the place to look. See* `reading1_prize_reduction.md`,
`sigma_essential_nonemptiness_finding.md`.

**Prove no such witness exists.** A compactness/spanning theorem: every σ-additive
state on a σ-complete concrete OML lies in the closed convex hull of its
dispersion-free states *except* where a finite sub-OML is already contextual
(Wright). This is a Type-5 impossibility, and it would reinstate the
*empiricist-underdetermination* conclusion as a theorem: σ-essential relational
probability cannot exist, so the relational content the programme seeks is
operationally invisible after all. The Boolean boundary — subadditivity of the
separating states (Pták–Pulmannová, Rmk 5.1) — is the natural lever. *Caveat
(2026-06-12): this cannot reuse the ∏ₙMO₂ / Stone-over-center mechanism — vacuous
off-center — so a genuinely different finite-witnessing argument is needed.*

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
