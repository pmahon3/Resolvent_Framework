# Gate 1: does the cheap route go countable? (2026-10-27)

> **REVERSAL.** The countable σ-essential witness is **not** new as a theorem. A routine countable,
> literally irreducible witness W★ exists (§2), so Type 1 for `thm.countable_witness` /
> `thm.literal_irreducible_L4` FAILS per the pre-registration. Places that still assert it is novel or
> live are **owed updates (not edited here, by instruction):**
> - `countable_ring_witness/SEED.md`: Type 1 status, and "answers q:cardinality positively" as a claim;
> - `entry_audits/RESOLUTION_ovchinnikov_dnp.md` Item 2 ("NOVEL at entry level");
> - `entry_audits/G4_countable_witness.md`: proposed status line and the §1.4 scoped NOVEL claim;
> - `glued_carriers_taxonomy.json`: `thm.countable_witness` (l.~134) and `thm.literal_irreducible_L4`
>   (l.~155); entries citing it as "residual = base witness" (l.~260, ~294, ~465) need a scope note (§4);
> - `CLAUDE.md` "Infinity side" bullet ("no owner found after three prior-art passes");
> - auto-memory `MEMORY.md` breadcrumb ("σ-ESSENTIAL WITNESS ON COUNTABLE RINGS … NOT FOUND");
> - `notes/programme/program_overview.md` l.~67 (σ lane: countable witness on every ring L ≥ 4).

reviewed: false. Hand mathematics, every step ⟦HAND⟧. Machine answer key: two small finite scripts
(`/tmp/gate1/check.py`, `/tmp/gate1/rigid.py`, not kept in the repo; described in §5). No Lean.
Pre-registration: `SEED.md` § Gate 1. The outcomes are not changed here.

## Outcome: **A. The cheap route works.**

A countable, literally irreducible σ-essential witness is built from the listed routine ingredients:
- Pták's X_even(4) fibre with its free state t;
- an ultrafilter limit over the fibres;
- a product of fibres, glued by a parity code.

Per the pre-registration: **Type 1 FAILS for `thm.countable_witness` / `thm.literal_irreducible_L4`.**
Park the ring witness as a routine instance and keep the Lean as a receipt.

**Decisive line.** Index 4-point fibres by the nonzero vectors of the countable group G = ⊕_ℕ 𝔽₂.
Admit exactly the sets whose fibre-parity pattern is a character of G. Take the U-limit of the MO₃
state along an ultrafilter that kills every character. Then:
- the carrier is a countable σ-class with centre {∅, Ω};
- every σ-additive two-valued state on it is Dirac;
- the U-limit is a free finitely additive state.

---

## 0. Puzzle first

There are infinitely many rooms. Each has four lamps and is labelled by a nonzero on/off pattern of
finitely many switches. A *question* is a set of lamps, possibly spread over many rooms. Askable
questions obey one rule: pick a "secret switch set" Y; then in every room g, the number of the
question's lamps in room g has the parity of |g ∩ Y| (how many switches of Y are set in g's label).
So the parity pattern of an askable question across rooms has to be *linear* in the label.

- **The ultrafilter "votes".** In almost every room (in the ultrafilter's sense) every askable question
  has an even number of lamps. There the Specker-style answer works: the questions "lamps 12?",
  "lamps 13?" and "lamps 23?" (taken in every room) are all answered *yes*. No lamp lies in all three.
- **A single room cannot cheat.** Let Y be a single switch from that room's label. Then some askable
  questions have an odd number of lamps in that room, and these force any σ-additive answer pattern
  concentrated on that room to name a single lamp.

The local views cohere only "at infinity". Any σ-additive world has to be a single lamp in a single
room, and no lamp makes all three answers *yes*.

Scope: this puzzle is exactly the witness W★ of §2. Every claim in it is checked in §2.

---

## 1. Attempts (a) and (c): what fails, and why

### (a) Countable Binder–Navara carriers ⟦HAND⟧

Let Ω = ℕ×F, F = {1,2,3,4}, X = 4even, and let I be an ideal on ℕ. Set
D_I = {E : {n : E^n ∉ X} ∈ I}.

- **D_I is a σ-class ⟺ I is a σ-ideal.**
  - (⇐) This is Binder–Navara's argument.
  - (⇒) Suppose N_k ∈ I but ⋃N_k ∉ I. Disjointify the N_k to N'_k and set E_k = N'_k×{1}. These sets
    are disjoint and lie in D_I, but their union has odd fibres on ⋃N_k.
- **Every σ-ideal on a countable set is principal.** I = P(N₀) with N₀ = ⋃I, because N₀ is a countable
  union of members of I.
- **So D_I is one of three things, and none is a witness:**
  - P(N₀×F) ⊕ ∏_{n∉N₀} X, a direct sum and so reducible;
  - the plain product;
  - P(Ω) when N₀ = ℕ, which is Boolean.
- **The killing step fails.** Binder–Navara's rigidity needs every single fibre to be "exceptionable",
  i.e. {n} ∈ I for all n. That forces I = P(ℕ).
- **"All but finitely many fibres in X" is not σ-closed.** Its σ-closure contains every singleton, so it is
  P(Ω), which is Boolean. (On countable Ω, any σ-class containing all singletons is P(Ω).)
- **The same holds for exceptions taken pointwise in Ω.** These are E with E Δ P ∈ J for some product
  set P. A σ-ideal J on countable Ω is P(Z₀), and Z₀ is then central.

**What (a) does and does not show.** The *ideal* form of the exception mechanism needs a σ-ideal that
contains every point and misses an ultrafilter. That needs an index set of size ≥ ℵ₁. (DNP 2015 Thm 4
requires uncountable cofinality for the same reason.) This rules out *ideals*. It does not rule out other
gluings, and §2 is one that gets through.

### (c) Direct sums and products of countably many finite logics ⟦HAND⟧

- **Not literally irreducible.** Each sub-sum ⊔_{n∈S} Ω_n is central, since its meet with any element has
  fibres that are either that element's fibres or ∅. The Lean receipt is
  `Admissibility.descentClass_not_irreducible`.
- **Not σ-essential when the fibre is a fixed finite logic X.**
  - Partition ℕ by the type of the block's fibre configuration. There are finitely many types.
  - One class N_τ is m-true, and G ↦ m(N_τ×G) is a state on X realising τ.
  - Then δ_n ⊗ that state, for n ∈ N_τ, is σ-additive and extends s₀.
  - G4 §1.2(1) already recorded the X_even(6) case.
- Unbounded fibres were not pursued. The reducibility kills them anyway.

### (b) Gluing fibres: the first attempt fails

Take D = {E : all fibres have the same parity}.
- It is a σ-class: at most four all-odd sets can be pairwise disjoint.
- It is not a witness. Every finitely additive two-valued m on it is a restricted ultrafilter.
  - Proof: m(E) depends only on the U-germ of (E^n), by adding and removing parity-0 sets off a U-set.
  - The germ logic is all of P(F), because the odd sets ℕ×X are in D. So the germ state is a Dirac δ_f.
  - The kernel on any finite block is therefore nonempty.

**The lesson that led to §2.** Odd sets must exist at every *single* fibre, which kills each fibre's local
non-Dirac σ-state. But odd sets must be *U-null as a pattern*, so the germ logic stays 4even and t
survives.

---

## 2. Attempt (b), second form: the witness W★

### Data

- G = ⊕_{j∈ℕ} 𝔽₂, the finite subsets of ℕ under Δ, and G* = G∖{0}, which is countable.
- F = {1,2,3,4}, and **Ω = G*×F**, which is countable.
- **Characters.** For y ⊆ ℕ, *arbitrary* (not only finite), χ_y(g) = |g∩y| mod 2. These are exactly the
  homomorphisms G → 𝔽₂.
- **Parity pattern.** For E ⊆ Ω, p_E(g) = |E^g| mod 2.
- **Carrier.** **D = {E ⊆ Ω : p_E = χ_y|G* for some y ⊆ ℕ}.**

### Checks

1. **D is a concrete σ-class.** ⟦HAND⟧
   - ∅ and Ω have pattern χ_∅.
   - Complement keeps every fibre parity, since |F| = 4.
   - Countable disjoint union ⊔E_k:
     - at each g at most four E_k have nonempty fibre;
     - so p_{⊔E_k} = Σ_k χ_{y_k}, a pointwise-finite sum;
     - each term vanishes at g unless that E_k meets fibre g;
     - a pointwise-finite sum of homomorphisms is a homomorphism, hence some χ_y.
   - D is also closed under Δ (p_{EΔE′} = p_E + p_{E′}), so **D is a symmetric logic**. See §4.

2. **D is not Boolean and contains no singletons.**
   - A nonzero character is 1 on a coset of an index-2 subgroup, which is infinite. So e_g (one odd
     fibre) is never a character, and {(g,a)} ∉ D.
   - A₁∩A₂ below has the all-ones pattern on G*. That is not a character, since 1 + 1 ≠ 1 at {1}, {2}
     and {1,2}. So D is not intersection-closed.

3. **The ultrafilter.** ⟦HAND⟧
   - For finitely many y₁,…,y_k, the set Z = {g ∈ G* : χ_{y_i}(g) = 0 ∀i} is a finite-index subgroup minus
     0, so it is infinite.
   - So {Z(y₁..y_k)} together with the cofinite sets has the finite intersection property. Fix an
     ultrafilter U on G* extending it. It is free, and **{g : χ_y(g) = 1} ∉ U for every y**. In other
     words, U converges to 0 in the Bohr topology of G.
   - Hence **every E ∈ D has even fibres U-almost everywhere.**

4. **Finitely additive two-valued state.** ⟦HAND⟧
   - Let t be Pták's free state on 4even: t = 1 on F, {1,2}, {1,3}, {2,3}, and 0 on ∅, {3,4}, {2,4}, {1,4}.
   - It is a state: within 4even the only nontrivial disjoint pairs are complementary pairs, and t
     picks exactly one of each.
   - Set m(E) = 1 ⟺ {g : E^g even and t(E^g) = 1} ∈ U. Then:
     - m(Ω) = 1 and m(∅) = 0;
     - m(Eᶜ) = 1 − m(E), since on U-most g the fibres are even and t is complement-additive;
     - for disjoint E, E′ ∈ D, on U-most g all three fibres are even and t(E^g ⊔ E′^g) = t(E^g) + t(E′^g).
   - So m is a `FinAddState`.

5. **Pattern with empty kernel.**
   - Let A_i = G*×P_i with P₁ = {1,2}, P₂ = {1,3}, P₃ = {2,3}. Each has pattern χ_∅ and lies in D.
   - B = {A_i, A_iᶜ}, with s₀(A_i) = 1. This is a `LocalState`.
   - m extends s₀, so s₀ is **finitely coherent**.
   - A₁∩A₂∩A₃ = G*×∅ = ∅, so the kernel is empty and no Dirac state extends s₀.

6. **Every σ-additive two-valued state on D is Dirac.** ⟦HAND⟧ This is new, because Binder–Navara's
   step 5 needs singletons and D has none.
   - **(i) One fibre is chosen.** The fibres {g}×F (pattern 0) partition Ω countably. σ-additivity makes
     exactly one of them true, say at g₀. Two disjoint true sets are impossible, by the monotonicity
     argument in Dynkin systems.
   - **(ii) Monotonicity off g₀.** (G*∖{g₀})×F ∈ D is false. Any E ∈ D disjoint from fibre g₀ is a
     subset of it, and the relative complement lies in D. So s(E) = 0.
   - **(iii) Locality.** If E, E′ ∈ D have the same pattern and the same fibre at g₀, then s(E) = s(E′).
     - Reduce each to a canonical form: off g₀, an odd fibre becomes {1} and an even fibre becomes ∅.
     - Do this in at most three global steps. Each step adds or removes a pattern-0 set supported off g₀.
       Such a set lies in D and is false by (ii), so it does not change s.
     - Write Σ(χ, X) for the common value.
   - **(iv) Additivity.** Σ(χ+χ′, X⊔X′) = Σ(χ, X) + Σ(χ′, X′). Disjoint realisations with any prescribed
     off-g₀ parities exist in a 4-set. Also Σ(χ, ∅) = 0 by (ii).
   - **(v) The fibre state is Dirac.** Pick y with χ_y(g₀) = 1, e.g. y = {j} for some j ∈ g₀. Define μ on
     P(F) by μ(X) = Σ(0, X) for X even and μ(X) = Σ(χ_y, X) for X odd.
     - (iv) gives additivity for even⊔even, even⊔odd and odd⊔odd (using χ_y + χ_y = 0).
     - μ(F) = 1.
     - So μ is a two-valued additive state on the Boolean algebra P(F), hence μ = δ_f.
   - **(vi) s is δ_(g₀,f).**
     - For χ with χ(g₀) = 0: Σ(χ, X) = Σ(χ, ∅) + Σ(0, X) = δ_f(X).
     - For χ with χ(g₀) = 1: Σ(χ, X) = Σ(χ+χ_y, ∅) + Σ(χ_y, X) = δ_f(X).
     - So s = δ_(g₀,f).
   - **Answer key.** `rigid.py` checks the 4×4 system f(a,b) + f(a′,b′) = t′({a,a′}) (a ≠ a′, b ≠ b′),
     using the odd sets {(g₀,a)} ⊔ R_b with R_b = {(h,b) : h ≠ g₀, χ_y(h) = 1}. It has **0 solutions for
     each of the 4 non-Dirac t′**, and exactly one solution, the Dirac row, for each Dirac t′. This agrees
     with (v)–(vi).

7. **σ-essential.** By 4, 5 and 6, s₀ is finitely coherent, and every σ-additive two-valued state is a
   Dirac at a point outside the empty kernel. So `IsSigmaEssential s₀` holds. `NonSegregated` follows
   from `witness_nonSegregated`, and `Admissible` from that plus the vacuous `EssentiallyIrreducible`.

8. **Literally irreducible: centre = {∅, Ω}.** ⟦HAND⟧ Let E be central.
   - Meet E with {g}×X for X even, which has pattern 0. The result has pattern e_g·|E^g∩X|, and e_g is
     not a character (check 2). So |E^g∩X| is even for every even X. Taking X = F and X = the pairs
     forces E^g ∈ {∅, F}. So E = S×F.
   - Fix j and meet E with O_j (fibre {1} where j ∈ g, ∅ otherwise; pattern χ_{{j}}). The result has
     pattern f_j(g) = [j∈g]·1_S(g), which must be a homomorphism.
   - For g ∌ j and g′ ∋ j: 1_S(gΔg′) = f_j(gΔg′) = f_j(g′) = 1_S(g′). So 1_S is constant on
     {g : j ∈ g}.
   - These families overlap pairwise, since {j,k} ∈ both. So S ∈ {∅, G*}.
   - The k = 2 finite slice agrees (`check.py`: |D| = 2048 on 12 points, no singletons, centre
     {∅, Ω}). That is finite and says nothing about σ.

So W★ meets every conjunct of `targetA_sharp_countable_literal`'s shape:
- countable Ω;
- concrete σ-class;
- two-valued finitely additive state;
- no σ-additive extension;
- `Irreducible`;
- `NonSegregated`.

The proof is about a page and elementary, and uses only Pták's X_even(4) state and an ultrafilter
with the finite intersection property.

---

## 3. Gate 1 verdict, per the pre-registration

**Outcome A.** The routine variant listed as (b) in the task (a finite non-Boolean fibre glued along a
countable index, read through an ultrafilter limit) produces an explicit countable, literally
irreducible witness. So:
- **Type 1 FAILS** for `thm.countable_witness` and `thm.literal_irreducible_L4`. The seed's own bar
  was "the cheap route below must fail to give one", and it does not fail.
- Park the ring witness as a routine instance. Keep the Lean (`sL_sigmaEssential`,
  `targetA_sharp_countable_literal`, `D₄_six_conjuncts`) as a receipt.
- The structural reason sketched as Outcome B in the pre-registration (that the countable-ideal
  exception collapses on ℕ) is **true but not decisive**. It kills the *ideal* form of the exception
  (§1(a)), but a parity *code* closed under pointwise-finite sums does the same job. The difference
  between W★'s gluing and Binder–Navara's is **not** used to argue B or C. That would be rescue by
  framing.

**Hostile notes on W★ itself, recorded rather than resolved:**
- It is ⟦HAND⟧ and not in Lean. Formalizing it would follow the `Ulam` / `WindowGluing` suites, but it
  is not needed for the gate.
- "Routine" here means "built from the pre-listed ingredients and verified in a page". It does not mean
  "printed somewhere". Whether W★ itself is owned is a Gate-2-type question, and it is moot for the
  ring's Type 1.

**What is left of the ring, as a fact and not a claim.** These features of the ring are not shared
by W★:
- its σ-states are forced Dirac coordinatewise by windows P(ℕ²);
- the empty kernel comes from the non-commutativity of p⊗p around a cycle, the order kind of twist
  (note §9; attribution ⟦HAND⟧);
- it σ-generates P(ℕ⁴).

Whether any of this has value is a theory question for the glued-carriers collection, not a Type 1
claim.

## 4. For Gate 2 / taxonomy (not edited here)

- **W★ is a countable σ-complete symmetric logic** (closed under Δ) with a free, non-extendable
  two-valued state. That is exactly the *existence question* G4 §1.2(3) flagged. DNP 2015 Thms 4–6 are
  positive extension results, not witness constructions, so they do not contain W★. Gate 2 must check
  whether the symmetric-logic school owns W★ or a near relative: DNP 2015, Bikchentaev–Navara 2016,
  Bikchentaev–Yakushev IJTP 53 (2014) Problem 7.2, Bikchentaev 2009.
- **Scope of the reversal.** W★ is a fibre/code carrier, not a window carrier. Results that use the ring
  as *base witness* (`thm.loops_travel`, the "pointless ⟺ not a forest" assembly) keep it as their base
  instance. What fails is the ring's Type 1 as "a countable witness".
- Suggested `owned_regions` / probe entry (proposal only): "countable σ-essential witnesses are routine
  via parity-code gluing of X_even(4) fibres over ⊕𝔽₂ with a Bohr-null ultrafilter (GATE1.md)".
- Affected (per the SEED): `thm.countable_witness` and `thm.literal_irreducible_L4` move to
  `status: … Gate 1 = A (routine instance W★); Type 1 FAIL`. Not edited here.

## 5. Machine answer key (scratch, not kept)

- `check.py`: G = 𝔽₂²∖0, Ω of 12 points. D = pattern ∈ characters, |D| = 2048. It checks complement
  closure and 200k random disjoint unions, no singletons in D, and centre = {∅, Ω}.
- `rigid.py`: the 2¹⁶-assignment 4×4 system of §2.6, for all 8 states on 4even. Non-Dirac gives 0
  solutions. Dirac at a gives one solution, f(a,·) ≡ 1.

## WHY.md bearing

- **Question 3, hidden idealisation.** The countable witness comes from an ultrafilter that cannot see
  any linear parity pattern. Every room can be forced to commit to one lamp, but "almost every room"
  never is. The pointlessness lives entirely in the idealised "at infinity" vote.
- **"Circle, or composition?"** W★ is a **composition**: a finite Specker fibre, multiplied out and
  glued by a code. It has no cycle of windows. So countability alone does not need the cycle × infinity
  seam. Whatever the ring adds has to be argued on other grounds.
