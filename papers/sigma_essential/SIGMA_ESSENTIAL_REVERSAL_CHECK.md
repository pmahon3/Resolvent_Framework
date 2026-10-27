# Independent check of the v2.1 re-audit's reversal claims (σ-essential paper)

reviewed: false. 2026-10-27. Checker: Claude (Opus), fresh context, hostile to both the paper and
`SIGMA_ESSENTIAL_REAUDIT_v21.md`. This is the only file written. Nothing was committed.

Read levels: **[R]** read here; **[R-Lean]** Lean source read, and `#print axioms` re-run here (`lake env lean`
on a scratch file in /tmp); **[W]** web abstract; **[H]** ⟦HAND⟧ argument in this file, not in Lean.

## Summary

| Claim | Verdict | Decisive line |
|---|---|---|
| (A) Few-line witness without irreducibility, so Type 1 PASS → UNCLEAR | **CONFIRMED, split by sentence.** For the Lean sentence `Psi` / `psi_ZFC` (formerly `PsiAmended`) it is a *routine consequence*, which is stronger than UNCLEAR. For the paper's Def 1.2 / `TargetA_sharp` (with essential irreducibility) it is **UNCLEAR**, and the residue is exactly irreducibility. | D = Binder–Navara carrier with X = 4even, plus the U-limit of 4even's non-Dirac state, meets every conjunct of `Psi`. It fails `EssentiallyIrreducible` through ξ×F. |
| (B) Measurable-cardinal claims false | **CONFIRMED** for §2(c) and Rem 3.7. **PARTLY** for Rem 6.1: its explanatory clause is false, but its ZFC conclusion stands. | Countable–cocountable algebra on ω₁: a Boolean σ-algebra containing every singleton, with a non-Dirac σ-additive two-valued measure, and ℵ₁ is not measurable. No qualifier in the wording excludes it. |
| (C) Citations | **CONFIRMED** (arXiv:1905.08267; Akemann–Weaver needs CH). **PARTLY** (Wright). | arXiv abstract: Barbosa–Douce–Emeriau–Kashefi–Mansfield. arXiv:math/0606168: "Assuming the continuum hypothesis…". |
| (D) Drift | **CONFIRMED.** | The quotient half of Cor 5.12 is not in Lean, and the segregation definitions differ. `targetA_sharp_countable_literal` answers Q 6.5's first question. |

**WHY.md bearing.** This is question 3, a hidden idealisation. Once irreducibility is dropped, the
σ-failure is just "a product of Specker triangles over ω₁, read through an ultrafilter". The finite
loop coheres fibrewise, and only the σ-idealisation over ω₁ makes it pointless. The only part that is
not a composition of known pieces is irreducibility: the requirement that the world not split into
independent local copies.

---

## 1. Exact targets

### Paper (`sigma_essential.tex` + `sigma_essential_body.tex`; numbering from `.aux`)

- **Def 1.2 (`def:sigma-essential`):** "…finitely coherent on 𝓛 but extends to *no* global σ-additive
  two-valued state on 𝓛. … We require 𝓛 to be non-Boolean and *essentially irreducible*: the quotient
  of 𝓛 by the σ-ideal of countable sets has centre {0,1}".
- **§6, Ψ:** `Ψ :≡ ∃ 𝓛 ∈ Adm ¬Φ(𝓛)`, where Adm is "concrete, σ-complete, non-Boolean, essentially
  irreducible, non-segregated (the last a consequence of witnesshood…)".
- **Thm 1.3 / 5.18 (`thm:main-intro`, `thm:main`):** ZFC, |Ω| = ℵ₁, …, "every σ-additive two-valued
  state on 𝓛 is Dirac, and 𝓛 is non-Boolean, essentially irreducible, and non-segregated."
- **§2 obstruction (c):** "away from a measurable cardinal, every σ-additive two-valued state on a
  Boolean σ-algebra is Dirac [Sikorski1964, Jech2003]".
- **Rem 3.7 (`rem:not-measurable`):** "For a compatible block family (a single Boolean base 𝓑 on Ω), a
  coherent non-principal σ-additive selection s: 𝓑→{0,1} has U_s := s⁻¹(1) a non-principal σ-complete
  ultrafilter on 𝓑, so ∃ s ⟹ |Ω| measurable [Jech2003]."
- **Rem 6.1 (`rem:strength`):** "a measurable-cardinal lower bound [fails], because reduce-to-Dirac is a
  σ-*algebra* theorem unavailable on σ-classes".
- **§4 item (2):** "Akemann–Weaver [AkemannWeaver2008] give a pure state on B(H) multiplicative on no
  masa". There is no CH qualifier.
- **Rem 3.8:** "…σ-additive form [AbramskyBarbosaEtAl2022]". Bib: Abramsky & Barbosa, "The sheaf-theoretic
  structure of definite causality", CMP 391 (2022), "see also arXiv:1905.08267".
- **§1:** "Wright's theorem [Wright1978], that every two-valued state on a *finite* OML is finitely
  realised, forbids any *finite* witness". Q 6.5 repeats it.
- **Verification paragraph (§1):** "subsequently *formalized in Lean 4 in full* … The formalization covers
  … the centre (Corollary 5.12) …".
- **Q 6.5 (`q:cardinality`):** "The witness has |Ω| = ℵ₁. … can a countable Ω carry one (necessarily
  without all singletons, or with a different rigidity mechanism)?"

### Lean [R-Lean]

- **`PsiAmended` no longer exists as an identifier** (grep is empty). Its text, quoted in
  `FIDELITY_REVIEW.md` §5, is identical to the current `SigmaEssentialWitness.Psi`:
  `∃ Ω d B s₀, IsSigmaEssential s₀`.
- `IsSigmaEssential s₀ := FinitelyCoherent s₀ ∧ ¬ ∃ s : TwoValuedState d, ExtendsS s s₀`.
- `FinitelyCoherent s₀ := ∃ μ : FinAddState d, ExtendsF μ s₀`.
- The carrier is a `DynkinSystem` (σ-class).
- `Block` = a finset closed under complement.
- `LocalState` needs only `Val Aᶜ ↔ ¬Val A` on B.
- **`psi_ZFC : Psi`.** It carries no admissibility. Non-Boolean is derived (`carrier_not_interClosed`).
- **`TargetA_sharp := ∃ Ω d B s₀, Admissible d ∧ IsSigmaEssential s₀`**, where:
  - `Admissible := EssentiallyIrreducible ∧ NonSegregated`;
  - `EssentiallyIrreducible d := ∀ E, Centre d E → E.Countable ∨ Eᶜ.Countable`;
  - `Centre d E := d.Has E ∧ ∀ A, d.Has A → d.Has (E ∩ A)`;
  - `NonSegregated := ¬ SegregatedStructural` (every f.a. state blockwise pointed).
- `witness_nonSegregated` shows that **any** witness is NonSegregated.
- Receipts re-run here: `psi_ZFC`, `targetA_sharp_ZFC` and
  `WindowGluing.Cyclic.targetA_sharp_countable_literal` each depend on exactly
  `[propext, Classical.choice, Quot.sound]`.

## 2. (A): the few-line witness, built and checked [H]

**Setup.**
- F = {1,2,3,4}.
- 4even = the even-size subsets of F. This is MO₃ realised concretely: three blocks
  {12,34}, {13,24}, {14,23}.
- t: 4even → {0,1} with t = 1 exactly on F, 12, 13, 23.
- Within 4even the only disjoint pairs with union in 4even are complement pairs and pairs involving ∅,
  so t is a state.
- t is non-Dirac: 12∩13∩23 = ∅. (MO₃ has 8 two-valued states, 4 of them Dirac and 4 not. Recorded
  as read: Burešová–Pták 2024, G3 entry audit l.66.)

**Carrier.**
D := {E ⊆ ω₁×F : the fibre E^x := {f : (x,f) ∈ E} ∈ 4even for all but countably many x}.

This is literally Binder–Navara's carrier `{M ⊆ U×X : T(M) countable}`, as described in
`GATE_BETA_REPORT.md`, with X = 4even.

1. **D is a σ-class.**
   - ∅ and Ω are in D.
   - D is closed under complement, since complementing in F preserves evenness.
   - Take a countable disjoint family. Off the countable union of the exceptional sets, every fibre of
     the union is a disjoint union of even subsets of a 4-set, so it is even. A countable union of
     countable sets is countable.
2. **Contents of D.**
   - Every singleton (one bad fibre).
   - Every ξ×F (fibres F or ∅).
   - Every cell C_{α,n}×F.
   - The cores A₁, A₂, A₃ (constant fibres 12, 13, 23).
   - So **the paper's 𝓛 ⊆ D**: 𝓛 is the least σ-class containing generators that all lie in D.
3. **Pattern.**
   - B = {∅, Ω, Aᵢ, Aᵢᶜ} and s₀(Aᵢ) = 1, exactly as in the paper.
   - Every cross intersection is a full fibre, so it is nonempty, and s₀ is a state on B.
4. **Finitely coherent.**
   - Fix an ultrafilter U on ω₁ that extends the co-countable filter.
   - Set m(E) = 1 iff {x : t(E^x) = 1} ∈ U. The value of t on the countably many bad fibres does not
     matter mod U.
   - Additivity: let E ⊔ G = H in D. Off a countable set, t(H^x) = t(E^x) + t(G^x). So the H-set equals
     the E-set ⊔ the G-set mod countable, and since U is an ultrafilter, m(H) = m(E) + m(G).
   - m(Ω) = 1 and m(Aᵢ) = 1.
   - So m is a `FinAddState` extending s₀.
5. **No σ-extension (rigidity).**
   - Let s be σ-additive and two-valued on D. Then ξ ↦ s(ξ×F) is a σ-additive two-valued measure on
     P(ω₁), so by Ulam (ZFC) it is principal at some x.
   - {x}×F is a disjoint union of four singletons in D, so some s({(x,f)}) = 1.
   - Monotonicity (relative complement holds in any σ-class) then gives s = δ_(x,f).
   - A Dirac extending s₀ needs a point in A₁∩A₂∩A₃ = ∅, which is impossible.
   - Equivalently, B–N Thm 4 says the state is countably carried; a two-valued state countably carried
     is Dirac.
6. **Non-Boolean, not a lattice.**
   - A₁∩A₂ = ω₁×{1} has odd fibres everywhere, so it is ∉ D. Concrete compatibility needs the
     intersection, so A₁ and A₂ are incompatible.
   - Lower bounds of {A₁, A₂} are sets in D inside ω₁×{1}. Their fibres must be ∅ almost everywhere,
     so they are the countable subsets, and there is no maximum.
7. **NonSegregated** is forced by step 4 and step 5 together (`witness_nonSegregated`).

**So D satisfies every conjunct of Lean `Psi` (= the old `PsiAmended`)**, with a proof of about ten lines
from Ulam + B–N's carrier + the MO₃ state.

**Vote state = U-limit.**
- Take E ∈ 𝓛 with normalised representation (ξ,κ). For U-most x the fibre indicator is κΔ1111 if
  x ∈ ξ and κ otherwise, which is exactly v(E) = κ Δ u(ξ)·1111.
- 1[v ∈ Ŝ] = t, since Ŝ = {1111,1100,1010,0110} = {F,12,13,23}.
- So the paper's m is m_D restricted to 𝓛.
- Thm 5.16 (additivity), Cor 5.11 (non-Boolean, not a lattice) and the f.a. side all follow from
  𝓛 ⊆ D without the normal form.

**Where D fails: `EssentiallyIrreducible` and Def 1.2.**
- Let ξ ⊆ ω₁ be uncountable and co-uncountable.
- For every A ∈ D, the fibres of (ξ×F)∩A are A^x or ∅, so (ξ×F)∩A ∈ D. Hence ξ×F is central in D
  (Lean's `Centre`), and it is neither countable nor co-countable.
- Its class is also a non-trivial central element of D/ctble.
- In 𝓛 the cell C×F is *not* central: C×{1,2} ∉ 𝓛 by Thm 5.8 (traces (C,C,∅,∅) are not in P̃ unless C is countable or co-countable). **The normal form is used for exactly
  this, the centre computation of Cor 5.12.** The re-audit's §2.1 point 4 is right.

**Anti-oscillation (repo record).**
- `PHASE2_AUDIT_VERDICT.md` answered the "Czech-school exercise" deflation by locating the content in
  the normal form, which "makes the incompatibility uncountably deep so the additivity certificate
  cannot form". **That rebuttal fails.** Once m exists on D, no additivity certificate can form in D or
  in any sub-σ-class, whatever normal form is used.
- The pre-registered reversal trigger (`GATE_BETA_REPORT.md`) flips the PASS if a source "contains (or
  reduces to an exercise) the CONJUNCTION — concrete σ-complete non-Boolean carrier + finitely coherent
  two-valued pattern + no σ-additive extension". **Irreducibility is not in that conjunction.**
- Honest caveat: the trigger names items 1–3 (DNP 1992, Navara 1984, PP1991), not Binder–Navara.
  But its condition, "reduces to an exercise", is met through B–N Thm 4, which Gate β read in full.
- Gate β cleared B–N for having "no f.a. side". That was the wrong test: the f.a. side is the one-line
  U-limit.
- `VERIFICATION_VERDICT.md` §2.3 already called irreducibility mod countable "METHOD-forced".
  `FIDELITY_REVIEW.md` §5 already scoped `PsiAmended` as omitting irreducibility.
- So this is not a swing. It locates the old PASS's content in the conjunct the old documents already
  flagged as the weak one.

**Verdict on (A).**
- **For `psi_ZFC` (Lean Ψ), Type 1 falls to "known by routine consequence".**
- **For the paper's theorem (Def 1.2 / Thm 5.18 with essential irreducibility, Lean `targetA_sharp_ZFC`),
  UNCLEAR is the right label, not FAIL.** Irreducibility is the standard non-degeneracy demand in OML
  theory: D is "ω₁ copies of MO₃", which is exactly the reducible case it excludes. The demand is
  therefore better motivated than "method-forced". Whether the normal-form step is itself routine was
  not settled here (Navara 2000 §17 and PP1991 are unread).
- The paper must say this decomposition explicitly. If it does not, a referee will.

## 3. (B): countable–cocountable on ω₁ [H]

**Construction.**
- Σ = {A ⊆ ω₁ : A countable or co-countable}.
- μ(A) = 1 iff A is co-countable.

**Checks.**
- A disjoint family has at most one co-countable member, because two co-countable sets meet.
- A countable union is co-countable iff some member is.
- So μ is σ-additive and two-valued.
- μ({x}) = 0 ≠ δ_x({x}), so μ is non-Dirac.
- ℵ₁ is a successor, hence not measurable. The construction is ZFC.

**Against each wording.**
- **§2(c): false as stated.** "Boolean σ-algebra" carries no "= P(Ω)", "complete" or "atomless"
  qualifier. Σ is atomic and contains every singleton, so even a charitable "point-separating" reading
  fails. The true statement is for P(κ), κ below the first measurable (or σ-algebras containing an
  Ulam matrix and singletons, as Thm 5.13 itself uses).
- **Rem 3.7: false as stated.**
  - Take 𝓑 = Σ and s = μ. s is non-principal in Q 3.6(c)'s sense: for each ω₀, the block
    {{ω₀}, ω₁∖{ω₀}} selects the cell not containing ω₀.
  - "U_s is a σ-complete ultrafilter on 𝓑" is *true*. The false step is "⟹ |Ω| measurable", which
    needs 𝓑 = P(Ω).
  - Hostile footnote: Q 3.6 glosses a block as "a countable partition". Under that gloss, a single
    block admits no non-principal σ-selection, and the implication is vacuously true. But the gloss is
    itself wrong for σ-class blocks: Σ is a block and is not generated by a countable partition. So
    the gloss does not rescue the remark; it is a second error.
- **Rem 6.1: PARTLY.**
  - The clause "reduce-to-Dirac is a σ-algebra theorem unavailable on σ-classes" is false in both
    directions: it fails on Σ, a σ-algebra, and it holds on 𝓛, a σ-class (Thm 5.13). The remark's own
    next sentences ("embraced, not escaped") already contradict it.
  - The conclusion (Ψ is a ZFC theorem, with no large-cardinal strength) is correct (Lean).
  - I do **not** adopt the re-audit's "nothing to resolve". Blecher–Weaver tie a σ-additive pure-state
    phenomenon on a non-distributive σ-complete OML to Ulam-measurability, so a referee *could*
    reasonably expect strength. A correctly stated "strength" remark survives; the lower-bound half
    must go.
- Repo record: `sigma_essential_taxonomy.json` `gate.lb_mechanism` fired "refuted" on 2026-06-26, and
  the paper prose was never synced. Confirmed.

## 4. (C) citations

- **arXiv:1905.08267: CONFIRMED** [W, arxiv.org/abs]. It is Barbosa, Douce, Emeriau, Kashefi, Mansfield,
  "Continuous-variable nonlocality and contextuality", CMP 391 (2022) 1047–1089. The bib's
  authors/title ("Abramsky & Barbosa, The sheaf-theoretic structure of definite causality") are wrong.
  The *content* fits the use: measure-theoretic contextuality.
- **Akemann–Weaver: CONFIRMED for arXiv:math/0606168** [W]: "Assuming the continuum hypothesis, we prove
  that B(H) has a pure state whose restriction to any masa is not pure."
  - The PNAS 105 (2008) 5313 page returned 403, so the published abstract was not seen. The bib title
    ("…not multiplicative on any masa") differs from the arXiv title. No source suggests the PNAS
    version drops CH.
  - The paper's unconditional use (§4 item (2)) needs "under CH".
  - The re-audit's "ZFC version via Koszmider 2020 + MSS" was **not verified** here. Koszmider's
    non-diagonalizable pure state is about atomic masas, not every masa. Do not repeat that claim
    without reading it.
  - The item is rhetorical (boundary map), not load-bearing.
- **Wright 1978: PARTLY.**
  - "Finitely realised" is undefined in the paper.
  - The only shelf record (Svozil 2001, a secondary source) attributes to Wright a convex-combination
    result.
  - The fact used (there is no finite witness) is immediate from "finite ⇒ f.a. = σ-additive", which §1
    already says.
  - Dropping the citation is confirmed. "Misattributed" is plausible but unverified at the primary level.

## 5. (D) drift

**"Formalized in Lean 4 in full": CONFIRMED overclaim.**
- Lean has `central_countable_or_cocountable`, the *literal* centre ⊆ countable ∪ co-countable
  (paragraph 1 of Cor 5.12).
- Def 1.2 demands a trivial centre of the **quotient** 𝓛/ctble, which is paragraph 2 of Cor 5.12.
  Paragraph 2 has no Lean counterpart; grep finds "quotient" only in docstrings.
- The literal condition does not imply the quotient condition in general.
- Segregation: the paper's notion (Rem 4.4: "every countable orthogonal family lies in a single block
  whose σ-states rescue every trace") differs from Lean's `SegregatedStructural` (every f.a. state
  blockwise pointed).
- Thm 1.3, which claims non-segregated and essentially irreducible, is advertised as "machine-checked
  end-to-end". That holds only up to these two definitional substitutions.
- Hygiene: the `UlamWitnessLatticeGap.lean` §5 docstring still says the centre steps are "not yet
  written".
- Direction of the gap: every literally central element is quotient-central, so Lean's
  `EssentiallyIrreducible` is *weaker* than Def 1.2's quotient condition. The hand proof (Cor 5.12
  ¶2) is plausible but unchecked by machine. The paper should name the predicate it checks.

**Q 6.5 stale: CONFIRMED.**
- `targetA_sharp_countable_literal : Countable Ω₄ ∧ Irreducible D₄ ∧ NonSegregated D₄ ∧ IsSigmaEssential s₀`,
  with axioms clean (re-run here).
- Ω₄ = ℕ⁴, D₄ = the glued 4-ring of coordinate windows, and Cₖ = {x : xₖ < xₖ₊₁}.
- The σ-failure proof read here: each window's σ-state selects a pair a < b, adjacent windows force
  equal coordinates, and the cyclic chain gives a₀ < a₀. This is "a different rigidity mechanism",
  exactly Q 6.5's parenthetical.
- D₄ meets Def 1.2. On countable Ω the quotient condition is degenerate (vacuous), and Lean's literal
  `Irreducible` (centre = {∅, Ω}) is strictly stronger.
- So Q 6.5's first question is answered yes in Lean. VERIFICATION_VERDICT's "literal irreducibility:
  OPEN" row is also stale.
- Caveats, all carried over:
  - there has been no hand audit of D₄ beyond the step read above;
  - prior art is "not found after three passes", with Bhaskara Rao and Goldberg/Hindman–Strauss bodies
    unread;
  - `MeetsExist D₄` is undecided. If D₄ were a lattice it would refute the conjecture in Q 6.4.

## 6. What this check does not settle

- Whether the parity normal form's irreducibility step is itself routine. Read Navara 2000 §17, PP1991
  and Navara–Pták–Rogalewicz 1988 (prescribed centre).
- The PNAS text of Akemann–Weaver.
- Wright 1978 primary.
- Whether D₄ is a lattice.
