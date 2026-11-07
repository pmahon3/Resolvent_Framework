# Convex gluing systems: prior-art map

reviewed: false. 2026-11-06. Hostile, cross-field scout of `CONVEX_GLUING_FRAMEWORK.md`. Read levels: [full], [meth] = theorem statements
and proofs read, [abs], [snip] = search snippet, [recall] = from memory, unverified. Rows that `glued_carriers_taxonomy.json` already
records are cited by their id and not re-derived.

*Terminology (added 2026-11-06, terminology pass).* "Frustrated" (correlation sense) = **not antibalanced**: signs not multiplying to (−1)^{length}, i.e. frustration of −R, the reverse of the signed-graph usage on triangles (Toulouse 1977; Zaslavsky; Harary 1953 says "unbalanced").

## 1. Owned regions

| Region | Owner(s) | Read |
|---|---|---|
| Presheaf of distributions over a measurement cover; compatible families = no-signalling; global section = existence | Abramsky–Brandenburger 2011 (D_R ∘ E) | [read, shelf] |
| Same with measures (infinite outcomes) | Barbosa et al. 1905.08267 (`own.cv_sheaves_sigma`) | recorded |
| Convex-set-valued (simplicial) distributions as a categorical object; noncontextual ⟺ weakly invertible; simplicial homotopy detects extremals | Kharoof–Okay, TAC 44 (2025), arXiv:2211.00571; Okay–Kharoof–Ipek, Quantum 2023 | [abs] |
| Ω-free colimit; compatible families = limit of local Stone spectra | van den Berg–Heunen 2012 (`own.stone_space_of_logic`) | recorded |
| Existence, uniqueness and extremes of a fibre for specifications | Georgii ch. 7; Dynkin, Ann. Prob. 6 (1978) (simplex + extremes = 0-1 law via sufficient statistics, no Choquet) | [abs] |
| Extreme points of a marginal or moment fibre | Douglas, Michigan Math. J. 11 (1964); Lindenstrauss 1965; Winkler, MOR 13 (1988); Girardin, CJM (1995); "Extremal solutions of a general marginal problem", CMUC 32 (1991) | [snip] |
| Acyclic ⟺ local-to-global | `own.acyclic_line_and_reduction`, `own.vorobev_acyclic` | recorded |
| Gluing f.a. charges along forests; ambient-Ω compatibility condition | `own.charge_compatibility` (Guy 1961; CMU-Z 2025) | recorded |
| Čech obstruction ("twist") ⇒ contextuality; false positives | Abramsky–Mansfield–Barbosa 2011 Prop 4.2–4.3, §8; Carù 2017 §4, Prop 6.3 (H¹ = torsors); ABKLM 2015 Thm 21 (AvN ⇒ CSC ⇒ SC) | [meth, shelf] |
| Kolmogorov extension and 0-1 laws in Markov categories; Giry weak pullbacks (standard Borel only) | Fritz–Rischel 2020 (arXiv:1912.02769); arXiv:2502.14941 Thm 3.7; Luckhardt CT2025 | [abs/snip] |
| min = max tensor of cones ⟺ one factor is simplicial | Namioka–Phelps 1969 [recall]; Aubrun–Lami–Palazuelos–Plávala, GAFA 31 (2021) | [abs] |
| Test of θ ∈ closed convex cone with a bootstrap of a sublinear statistic | Fang–Santos, REStud 2019 §4 (already used in `VG_INFERENCE_METHODS.md`); Fang–Seo, Econometrica 89 (2021); Silvapulle–Sen 2004 | [abs/meth] |

## 2. Verdicts

**(a) Framework definition: OWNED.** The functor-plus-limit-plus-gluing-map package is Abramsky–Brandenburger's empirical-model
presheaf with convex coefficients. Kharoof–Okay make it explicitly convex-categorical. The existence / uniqueness / extremes-of-the-fibre
triple is the standard agenda of the marginal problem (Kellerer; Douglas–Lindenstrauss–Winkler) and of DLR theory (Georgii, Dynkin). The
**ordinary-vs-ideal** layer is **PARTLY** owned: per instance by Dynkin (extremes = 0-1), Bureshova–Pták and `own.stone_space_of_logic`
(two-valued = Dirac on S(D)), and Kirman–Sondermann. No uniform functorial definition of "location" was found [abs-level search only].

**(b) T1: AMBIGUOUS. The strong reading is refuted by owned finite examples; the intended (weak) reading's acyclic case is owned; the residue is cyclic and infinite.**
- *Strong reading* (trivial twist + locally ordinary ⇒ a global point exists): refuted by owned finite examples. T1 must therefore assume F_x ≠ ∅, which is a precision fix, not a kill.
  - Full-support CHSH-violating Bell model: every local point extends, so the twist is trivial, yet no joint exists (Abramsky–Brandenburger hierarchy).
  - Cohomological false positives: the Hardy model; the KS cover {ABC, BDE, CDE, ADF, AEG} (AMB 2011 §8); Carù 2017's symmetric, connected counterexample to AMB Conj 8.1. Only "obstruction ≠ 0 ⇒ (strongly) contextual" is known (AMB Prop 4.3).
  - Ambient Ω, no cycle ⟦HAND⟧: Ω = {1,2,3}, A = ⟨{1}⟩, B = ⟨{3}⟩, with δ₁ on A and δ₃ on B. These agree on A∩B = {∅, Ω}, but {1} ⊆ {1,2} gives 1 ≤ 0, so Guy's condition fails (`own.charge_compatibility`). The free colimit (vdBH) glues the same data. So T1 depends on whether the global object is free or a carrier inside Ω. Identifying the draft's product cover with the free case is ⟦HAND⟧.
- *Weak reading* (F_x ≠ ∅ ⇒ not pointless): the answer depends on how conv‾(P) is closed.
  - **Weak\*** is the closure that keeps point, ideal and pointless distinct. On a non-Boolean carrier D, the closure of the Dirac hull is the set of coherent states, the restrictions of charges on P(Ω) (`own.coherence_extension`; G9 in `own.stone_space_of_logic`). Pointless therefore means non-coherent, which is the programme's own definition. Local ordinariness becomes automatic, because the local contexts are Boolean.
  - T1 then reads: trivial twist ⇒ some coherent global extension. The acyclic case is **owned** (`own.charge_compatibility`: forest-compatible window charges extend to P(Ω)).
  - Consensus check: under weak\*, a free ultrafilter *is* locally ordinary, and globally it is an ideal point inside the hull. The draft's reasoning is wrong there, but its conclusion (T1 not contradicted) survives.
  - **σ-additive hull** (secondary; this reading feeds σ-essential): here "ideal" collapses into "pointless", which clashes with the answers-first stance. Acyclic σ-additive gluing additionally needs compactness, independent of twist. It is owned on standard Borel or perfect spaces (Kolmogorov; Fritz–Rischel; Giry weak pullbacks) and fails in general (Kellerer 1964 p.179 [read]; Andersen–Jessen, `papers/paper_i/PAPER_I_REVERSAL_CHECK.md`).

**(c) T2 (linking the three questions): pairwise links OWNED per instance; no uniform three-way theorem FOUND.**
- Existence ↔ simplex: min = max tensor ⟺ a factor is classical (Namioka–Phelps; ALPP 2021). This is the cleanest owned
  existence–face link.
- Uniqueness of decomposition ↔ simplex ↔ extremes = 0-1: Choquet; Dynkin 1978; Georgii ch. 7.
- Existence ↔ invertibility, and extremality ↔ homotopy: Kharoof–Okay.
- Existence gauge ↔ frustrated supports: Boman (as recorded in the draft).
- A statement tying gauge positivity, fibre size and ideal extremes through the face lattice of ρ(K_I) was not found [abs-level].
  Next check: the full text of Kharoof–Okay §§5–6.

**(d) T3: OWNED.**
- Testing membership of a closed convex cone with a bootstrap of the sublinear/support function is Fang–Santos §4 and Fang–Seo 2021.
- The domination step V(x+y) ≤ V(x) + h(y) is folklore subadditivity.
- Lifting from correlations to any gluing system is a corollary, not a theorem. Claim it at most as an application.

## 3. Most promising unowned residue, with its nearest killers

**R. Twist and coherence on cyclic covers at infinity.** Take a finite *cyclic* window cover with infinite local algebras, and x ∈ Comp with F_x ≠ ∅ (a state on the glued carrier D). If the holonomy of ultrafilter local choices is trivial, is x coherent (not pointless)? Equivalently: does every pointless state carry a non-trivial twist? A secondary variant asks the same with σ-additive gluing on standard-Borel local spaces.
- **This is the only reading of T1 that is neither false (strong reading) nor owned (acyclic case).**
- **Nearest killers.**
  1. Dravecký–Šipoš Ex 6 and Navara–Pták 1983 (`own.dravecky_sipos_flight_subcarrier`, `own.navara_ptak_1983_triangle_of_observables`).
     If their pointless witnesses have trivial holonomy, R is dead. **Check this first: it is on the shelf.**
  2. Kellerer 1964 §§3–4: the positive marginal problem, unread; it may already give the cyclic σ-additive criterion.
  3. Carù's H¹ = torsors and Ghrist–Cooperband 2025 (torsor obstructions) supply the twist language, though finite.
  4. Hrushovski / Goodrick–Kim–Kolesnikov H¹ amalgamation obstructions (`own.type_amalgamation`): infinite and cyclic, in model theory.
- **Low prior for T2.** Expect it to fragment into the owned per-instance links above.

**Bearing on WHY.md.** The strong T1 failure says local views with no visible twist can still fail to add up: the obstruction is
*probabilistic*, not holonomic. Hidden idealisation: the choice of closure (weak\* or σ-additive) decides whether ideal points count as ordinary.

Not done: any primary read of Kharoof–Okay, Kellerer §§3–4, Douglas, or Dynkin beyond the abstract. No shelf edits; no commit.
