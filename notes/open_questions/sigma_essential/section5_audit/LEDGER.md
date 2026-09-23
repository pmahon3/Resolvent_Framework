# §5 audit: fibre-4 membership, hypothesis inventory, Ψ_lat next step. Verdict ledger
Date: 2026-09-22. Line numbers are for the working tree (includes the uncommitted intro edit). Paper: `papers/sigma_essential/sigma_essential_body.tex` (numbers
checked against `sigma_essential.aux`). Format follows `../automorphisms/AUT_LEDGER.md`.
The paper proofs are by hand. The Lean check is a scratch file compiled against the built
oleans and has not been committed to the library (see §4).
Lean fibres are indexed `0..3`, so the paper's fibre 4 is Lean's `3`. `coreA/B/C` =
`{0,1},{0,2},{1,2}` correspond to the paper's `{1,2},{1,3},{2,3}`.

## 1. Ledger

### Task 1: is M×{4} in L?

| ID | Claim | Verdict | One-line reason | Location |
|----|-------|---------|-----------------|----------|
| F4-mem | M×{4} ∉ L | **PROVED** | The traces are (∅,∅,∅,M). In any representation (ξ,κ), each coordinate is ≈ξ or ≈ξᶜ, so ξ≈∅ or ξ≈M. Then κ ∈ {0001, 1110}, both of odd weight, which contradicts Thm 5.8. The same argument shows no element of L is ≈M×{4}. **Via Cor 5.10, as asked:** M×{4} ⊆ A₁^⊥ with E₁, E₂ countable, so by the core-complement clause it is countable or ≈ A₁^⊥ = M×{3,4}. It is neither. | Cor 5.9/5.10; `fibre_slab_check.lean` `slabAt_not_mem U h 3` |
| F4-why | "because its pattern 0001 is odd" | **PROVED, one gap** | Representations are not unique a priori, so the argument must exclude the complement pattern 1110 as well. It is also odd. | same |
| F4-aut | AUT_LEDGER error 2: "M×{4} (odd weight) is not in L" | **PROVED** (the membership part) | Same as F4-mem. However, "L cannot see fibre 4" is not the reason fibre 4 is undistinguished: M×{1}, M×{2}, M×{3} are equally absent (Cor 5.9). AUT_LEDGER's operative reason (the Sym(F)-invariant six-set family) is the right one. This entry adds no Aut question. | `../automorphisms/AUT_LEDGER.md` §2 item 2 |
| F4-a | §5's `(A₁∪A₂∪A₃)^⊥ = M×{4}` can be misread as element-level | **SUPPORTED** | A₁∪A₂∪A₃ = M×{1,2,3} has pattern 1110 (odd), so it is not in L. `\orth` is otherwise used on elements of L. Nothing in §5 states that M×{4} ∉ L, since Cor 5.9 names only M×{1}. The notation is not formally wrong, because the paper also writes ξ^⊥ for set complements in M (Lem 5.5). | tex l.480–484 |
| F4-b | "exactly the 4 even-weight regions survive; the 4 odd ones (3 solo + joint-failure) do not, the solos being empty anyway, so the substantive absence is M×{4}" | **REFUTED** (the count is right, the members are misnamed) | Read by trace-pattern parity (𝔽₂⁴), the headline is correct: the even-trace regions (the four empty ones, each = ∅) are in L, and the odd-trace regions (the four fibres) are not. The parenthetical is wrong under either reading. (i) The solo regions are ∅ ∈ L, so they are not excluded. (ii) The joint-failure region 000 is even by region index (𝔽₂³) and odd by trace, while the solos are odd by index and even by trace, so no single parity makes "3 solo + joint-failure" the odd set. (iii) There are **four** substantive absences, M×{1}, M×{2}, M×{3}, M×{4}, not one. | Cor 5.9 applied to each fibre; `slabAt_not_mem` for all `g` |
| F4-b′ | "four inhabited Boolean regions" sentence (l.482–483) | **PROVED consistent** | The four fibres are exactly the inhabited regions, and the three solo regions are empty. | tex l.482 |
| F4-c | The joint-failure result is sharper than Cor 5.9 | **REFUTED** | M×{4} = A_i^⊥ ∩ A_j^⊥ for **every** i≠j, so it is itself a pairwise-meet region (of two core complements). Cor 5.9's proof covers it verbatim, and the proof of Thm 5.16 already uses these fibres as sets ("each pairwise intersection … is a full fibre"). | `slab3_eq_compl_inter`; tex l.855–856 |

**Source of the F4-b error.** The claim mixes two parities within one sentence: region-index
parity (𝔽₂³, membership in the cores), which makes the solos and the triple region 111 odd;
and trace-pattern parity (𝔽₂⁴, fibres), which makes the inhabited regions odd. Correct
statement: of the eight regions, the four empty ones (100, 010, 001, 111) are in L as ∅.
None of the four inhabited ones (110, 101, 011, 000 = the fibres) is in L. The last clause
should read "the substantive absences are all four fibres".

**Minimal fix (APPLIED 2026-09-23, together with the H-seg citation swap in Prop 5.19; the Polish clause is untouched):**
1. l.482: replace `$(A_1\cup A_2\cup A_3)\orth = M\times\{4\}$` with
   `$\Omega\setminus(A_1\cup A_2\cup A_3) = M\times\{4\}$`.
2. Cor 5.9 statement: "No element of $\Lo$ is $\approx$-equal (fibrewise) to any fibre
   $M\times\{f\}$; in particular the pairwise core meets $M\times\{1\},\{2\},\{3\}$ and
   $M\times\{4\}=A_i\orth\cap A_j\orth$ are not in $\Lo$." In the proof, replace "$1000$ and
   $0111$" with "a unit vector and its complement". The argument is otherwise unchanged.
   This makes the l.480–484 set identities safe by forward reference, and no new remark is
   needed.

**Verdict on (c):** it does not earn a remark. The claimed sharpening does not exist
(F4-c). The fibre-general statement of Cor 5.9 is the right size, at zero extra proof
cost.

### Task 2: hypothesis inventory, §5 (5.1–5.19)

| Item | Stated | Consumed | Gap |
|------|--------|----------|-----|
| 5.1 Ulam | ω₁, AC | AC; initial segments countable | none |
| 5.3 σ-basics | σ-class + all singletons | (1),(4): complement + finite disjoint union only; (2),(3),(5): singletons + σ-closure | readability, not inflation |
| 5.4 invariant (intrinsic form) | — | — | checked correct |
| 5.5 rep. rigidity | — | M uncountable | none |
| 5.6 table | E∩G=∅ | only E_f∩G_f countable; already states this | none |
| 5.7 trichotomy | countable, exactly disjoint | neither countability nor exact disjointness (only disjointness mod countable) | readability; the normal form needs the countable form |
| **5.8 normal form** | L (singletons, Ulam cells, cores) | singletons, cores, complement, countable disjoint unions, M uncountable. **Of the cells, only their X×F shape; none of Lemma 5.1.** | **genuine unstated generality (H-5.8)** |
| 5.9, 5.10 | Thm 5.8 | Thm 5.8 only | none |
| 5.11 incompat | — | Thm 5.8 (via 5.9/5.10), singletons (countable lower bounds), concrete compatibility ⇒ intersection | none |
| 5.12 centre | — | cores, Thm 5.8, 5.3(5), concrete compatibility | none; matrix-free |
| **5.13 rigidity** | L | singletons, cells, row disjointness, row covering, column disjointness, σ-closure, \|rows\|>ℵ₀ | none: the post-proof sentence is exact (H-5.13) |
| 5.14–5.16 state | L | Thm 5.8, Lem 5.5/5.6, an ultrafilter ⊇ co-countable filter | matrix-free (H-5.8) |
| 5.17 | — | Lemma 5.1 + ultrafilter | none |
| 5.18 main | — | 5.13, 5.16, Lemma 3.1 (concrete K(s₀)) | none |
| **5.19 admissibility** | — | see H-seg, H-pol | **two unsupported side reasons** |

| ID | Claim | Verdict | One-line reason | Location |
|----|-------|---------|-----------------|----------|
| H-OM | (a) Orthomodularity is never a hypothesis in §5 | **PROVED** (inspection) | Its concrete content is 5.3(1) (relative complement), which is *derived* from the σ-class axioms. It is consumed only via 5.3(4) (monotonicity) in the first case of 5.13, and even there 5.3(3) suffices: E = {ω} ⊔ (E∖{ω}). 5.11/5.12 use only "compatible ⇒ intersection ∈ L", which needs no OM law. | tex l.523–544, 765–775 |
| H-5.13 | (b) Thm 5.13 consumes only singletons, cells, rows, columns, σ-closure | **PROVED** | Cases: the singleton-Dirac case uses singletons + monotonicity; the null case uses countable sets ∈ L, row disjointness/covering, the pigeonhole over uncountably many rows, and column disjointness. No cores, no invariant. "Robust to any enlargement" is exact: any σ-class containing the singletons and cells inherits the rigidity proof. | tex l.765–789; Lean `rigidity` |
| H-conc | (c) Concreteness only supplies Diracs and non-vacuous two-valued states | **REFUTED** | Concreteness is the medium of all of 5.4–5.12: fibre traces, order = ⊆ (the lower bounds in 5.11), compatibility ⇔ intersection (5.11, 5.12), and K(s₀) = A₁∩A₂∩A₃ (Lemma 3.1 in 5.18(2)). The Dirac case of 5.13 is one use among several. | as listed |
| H-5.8 | Thm 5.8, Cors 5.9–5.12 and 5.14–5.16 never use Lemma 5.1 | **PROVED** | Cells enter only as `(C, 0000)`-represented generators. The results hold for the σ-class generated by the singletons, the cores, and {X×F : X ∈ 𝒳} for **any** 𝒳 ⊆ P(M), M any uncountable set. Lean agrees: `nrep_exists` uses only `U.C` (`represents_cell`). This mirrors the post-5.13 remark: the witness factors as matrix-free geometry plus core-free rigidity. | tex l.658–678; `UlamWitnessInvariant.lean:694` |
| H-seg | 5.19: "the diagonal block, the Boolean σ-algebra … generated by singletons and cells" | **UNDETERMINED** | This needs cells from different rows to be compatible, i.e. (C_{α,n}∩C_{β,m})×F ∈ L. That is unproved and matrix-dependent (cf. AUT_LEDGER B2/B5′). The conclusion survives: non-segregation follows from witnesshood (rem:segregated + Thm 5.18, as §6 says), and Lean's `witness_nonSegregated` uses exactly that. Fix = cite witnesshood. | tex l.894–896; `Admissibility.lean:101` |
| H-pol | 5.19 / §4 / §6: "not Polish-representable … via Derr–Williamson" | **UNDETERMINED; known on the Lean side, not propagated to the paper** | Commit fc4b43b (2026-08-30) deleted `dw_polish_no_witness`: DW Thm D.6 concerns σ-additive probabilities and a finitely coherent pattern does not meet its hypothesis. Commit 1268cc9 and `HANDOFF_2026-08-31.md` l.249–255 ("anything treating the Polish route as closed is void") record this. The paper still asserts the cut at l.93, l.332–343, l.897, l.911–913, l.927 and l.1005, and no tracked item covers the paper text (grep of the handoff, the human worklist, and `witness_candidate/*.md`). I did **not** re-read D.6. | tex; `git show fc4b43b` |

**Statements worth reformulating at their true generality** (proposals, not applied):
1. Thm 5.8, or a one-line remark after it: the normal form holds for any fibre-constant
   generating family. This gives the symmetric partner of the post-5.13 remark.
2. Prop 5.19: derive non-segregation from witnesshood, not from the "diagonal block".
3. Prop 5.19 / §4: bring the Polish claim in line with fc4b43b. Scope is the user's call.
   This is the most consequential item in Task 2, though it is not hypothesis inflation.

### Task 3: the Ψ_lat next step

| ID | Claim | Verdict | One-line reason | Location |
|----|-------|---------|-----------------|----------|
| D-lr-fact | (AUT_LEDGER D-lr) "'(LR*)' occurs nowhere; 'three-cell star' is only frontier_map l.94" | **REFUTED** | The repo writes `(LR_*)` (a subscript star), so a grep for "(LR*)" misses it: `docs/s11_quarantine_generality.md:251,257,263,267,295,299`. "Three-cell (conditional-diagonal) star" appears at `docs/psi_lat_attack_surface_ledger.md:171,244`, s11 l.4, 234–238, 298, and `psi_lat_attack_surface.md:752–794`. | as given |
| D-lr-thread | (D-lr) "cross-thread conflation: oml_attack ≠ this paper's question" | **REFUTED** | oml_attack *is* the Ψ_lat thread. The header of `oml_attack/CURRENT_STATE.md` is "whether a concrete σ-complete orthomodular lattice can carry a σ-essential state". Lean `UlamWitnessLatticeGap.lean` names `PsiOML` as the paper's open question. | as given |
| N-desig | "The (LR_*) three-cell star calculation is the designated next Ψ_lat hand step" | **SUPPORTED as the most recent designation; not the only one** | It is the most recent dated designation: s11 l.298–300 (2026-08-09), PLA-S11-3, and PLA-FLAT-1 "Specific hand target". The authoritative `program_overview.md` l.1163–1164 (git blame: 2026-07-16) still reads "`ARR-CYL`, or explicit construction of the actual mixed cut join, is the next gate"; that designation belongs to the T-FIN/re-base sub-line and was never retired. The 2026-08-31 handoff designates nothing. | docs as given; `program_overview.md:1164` |
| N-live | "…and it is *the* live next step" | **UNDETERMINED (overstated)** | The repo has **no single designated next move** (see N-desig). The star target was never executed: nothing after 2026-08-09 touches it, and Campaign 12 It.138 (2026-07-14, the compatible-face collapse) predates it and is an input. It is also underspecified: the star is a target specification, not a construction, and the interfaces are still to be chosen. | `HANDOFF_2026-08-31.md:267`; `CAMPAIGN_LOG.md:1635` |
| N-paper | "…a step *in this paper*" | **REFUTED** | Neither (LR) nor the star appears in the paper. The paper's only Ψ_lat content is Question 6.4. | tex l.980–995 |
| LR-status | (3a) status of (LR_*) | **UNDETERMINED (repo's grade)** | (LR) is the hypothesis of T1, machine-checked as `compat_of_locally_resolved` (`ConcreteOMLBlocks.lean:357`). The "locally resolved value-one meet lemma" (pair meet + (LR) + μ(a)=μ(b)=1 ⇒ μ(a∧b)=1) is HAND-proved. (LR_*) is (LR) at a designated value-one pair of star faces; the star's interface hypotheses neither force nor negate it (PLA-S11-3). | s11 §0.1, §1.1, Phase 2 |
| MO-block | (3b) MO_ω is recorded as blocking the naive lattice ⇒ Φ route | **SUPPORTED, scoped** | It blocks one proof route, "latticehood forces a live mixed meet" (s11 §1.2, PLA-S11-2 deletion boundary): concrete, σ-complete, essentially irreducible, with every private off-block meet 0, so (LR) fails. It is **not** evidence against the conjecture: MO_ω satisfies Φ (Lemma 4.3). | s11 §1.2 |
| MO-paper | MO_ω's (LR) role is visible in Q 6.4 | **REFUTED** | Q 6.4 cites neither T1 nor MO_ω. MO_ω appears only at l.398 (centre) and under Lemma 4.3 (it satisfies Φ). | tex l.398, 419, 980–995 |
| N-calc | (3c) the next concrete calculation | **SUPPORTED** | Attempt the coherence-preserving flat-realisation lemma on the three-cell *conditional-diagonal star* (`oml_attack/oml_distributed_relation_cell_assembly.md` §8 l.213), with non-countable-type, countable-quotient-visible interfaces (`oml_coarse_inhabitation_and_defect.md` §2–3). Test (LR_*) at the first mixed cut. The falsifier is a mixed-cut identity forced in every faithful realisation. | `psi_lat_attack_surface.md:750–775`; PLA-FLAT-1 |

**Conflation warning.** The three-cell *conditional-diagonal star* (above) is a different
object from the T-FIN three-cell *corner* {00,01,10} (`oml_attack/T_FIN_IMPOSSIBILITY_LEDGER.md`,
`CURRENT_STATE.md` l.391–406). The finite k=1,2,3 star runs (§9 of the assembly note) are
controls with point-state semantics, not the live construction.

**Optional Q 6.4 sentence (user's call; not applied).** "Any lattice witness must omit some
singletons: a concrete σ-class that is a lattice and contains all singletons is Boolean,
since singletons force every meet to be the set intersection. Latticehood alone does not
force a charged mixed meet ($MO_\omega$)." The first half is T1's global corollary, which
is folklore-level and needs a citation or its one-line proof. It replaces "limited evidence"
with the one proved structural fact.

### What would refute each
- **F4-mem / F4-b / F4-c**: an element of L with trace classes (∅,∅,∅,M), or with those of
  any single fibre. Excluded by Thm 5.8 plus parity; kernel-checked for all four fibres.
  F4-c specifically: some i≠j with A_i^⊥∩A_j^⊥ ≠ M×{4}. Kernel-checked for all three pairs.
- **F4-aut**: an element of L equal to M×{4}; see F4-mem. The "reason" remark is refuted by exhibiting a Sym(F)-invariant family singling out fibre 4, and none exists (AUT_LEDGER B-S3).
- **F4-why**: an even-weight pattern representing (∅,∅,∅,M). The only candidates are 0001 and 1110.
- **F4-a**: a §5 statement, before or near l.482, that the fibres are not in L. There is none (grep).
- **F4-b′**: an inhabited solo region. The cores cover fibres {1,2}, {1,3}, {2,3}, so every point lies in 0 or 2 cores.
- **H-OM**: a §5 step that uses the OM law, other than via 5.3(1) derived from the axioms. I found none.
- **H-5.13**: a step of the 5.13 proof that uses a core or P̃. I found none.
- **H-conc**: a proof of 5.9–5.12 from abstract OMP data without set traces. Not possible as written.
- **H-5.8**: a use of Lemma 5.1(1)–(3) in 5.8–5.16. None; Lean's `nrep_exists` takes `U` but uses only `U.C`.
- **H-seg**: a proof that all cross-row cell intersections lie in L for every Ulam matrix (would promote it to PROVED), or a matrix with an incompatible cell pair (would REFUTE it).
- **H-pol**: a re-read of DW D.6 showing it covers finitely coherent patterns (would restore the paper), or confirming fc4b43b (would refute the paper's claim).
- **D-lr-fact / D-lr-thread**: removal of the cited lines. Checked by grep 2026-09-22.
- **N-desig**: a repo designation dated after 2026-08-09 that supersedes the star, or a retirement of the star target. None found (git log since 2026-08-09 on oml_attack/, programme/, docs/).
- **N-paper**: an occurrence of (LR), the star, or a mixed-cut calculation in the paper's .tex. None (grep).
- **MO-paper**: a sentence in Q 6.4 or §6 citing T1 or MO_ω's (LR) failure. None (read of l.980–995).
- **N-live**: a record that the calculation was run, or its reaffirmation after 2026-08-31.
- **LR-status**: a proof that faithful star realisations force (LR_*), or negate it.
- **MO-block**: a proof that latticehood plus Adm implies (LR) at charged mixed pairs.
- **N-calc**: as N-desig.

## 2. Errors in the claim list (NOT empty)

1. **F4-b misnames its members.** The count (4 in, 4 out) is right. But the solo regions are
   ∅ ∈ L, not excluded; the excluded four are the fibres. There are four substantive
   absences, not only M×{4}.
2. **"Sharper than Cor 5.9" (F4-c).** M×{4} is a pairwise-meet region (A_i^⊥∩A_j^⊥), so
   Cor 5.9's argument already covers it.
3. **"M×{4} ∉ L because 0001 is odd"** omits the complement pattern 1110. This is minor;
   the proof needs both.
4. **"Concreteness does no more than supply Diracs" (H-conc)** is false. It carries the whole trace analysis.
5. **The prompt's Task 3 premise, "D-lr … and the repo confirms it", is false.** D-lr's
   repo facts are wrong (D-lr-fact, D-lr-thread). The chat's original claim was closer to
   the repo than D-lr: it names the most recent designated Ψ_lat hand target. It was wrong in
   calling it "in this paper" and "the live" step: the authoritative doc still names ARR-CYL
   (2026-07-16), and the 2026-08-31 handoff names nothing.
6. **"MO_ω blocks the naive lattice ⇒ Φ route"** is right about a proof route and wrong if
   read as evidence against the conjecture, since MO_ω satisfies Φ.
7. **Found in passing, not in the claim list:** the paper still asserts the Derr–Williamson
   Polish cut. The repo demoted it on 2026-08-30 on the Lean side, and the paper was never
   updated (H-pol). Prop 5.19's non-segregation
   reason is also unsupported (H-seg).

## 3. Corrected claim list

- **F4′** (PROVED, Lean-checked in scratch). No element of L is ≈ any fibre M×{f}, f=1..4.
  Of the eight Boolean regions of {A₁,A₂,A₃}, the four empty ones are in L (as ∅) and the
  four inhabited ones (the fibres) are not. M×{4} = A_i^⊥∩A_j^⊥ for all i≠j.
- **Paper action (proposed):** generalise the statement of Cor 5.9 to all fibres, and write
  Ω∖(A₁∪A₂∪A₃) at l.482. No new remark.
- **H′** (PROVED by inspection). §5 has two independent halves. Thm 5.8 and everything
  downstream except 5.13 and 5.17 are matrix-free. 5.13 is core-free. Orthomodularity is
  never assumed. Concreteness is structural throughout.
- **H-5.19′.** Non-segregation should be derived from witnesshood. The Polish clause is
  inconsistent with the repo since fc4b43b and needs the user's decision.
- **Ψ_lat′.** There is no single designated next move. Of the candidates, the most recent (2026-08-09) is the coherence-preserving
  flat-realisation lemma on the three-cell conditional-diagonal star, testing (LR_*) at the
  first mixed cut. It has not been executed, the 2026-08-31 handoff does not reaffirm it,
  and it is underspecified until the interfaces are chosen. It is not a paper item. MO_ω
  bounds the s11 route, not the conjecture. The other live designation is `ARR-CYL` / the
  actual mixed-cut join (`program_overview.md:1164`, 2026-07-16, T-FIN/re-base sub-line).

## 4. LEAN STATUS

- **Checked, not committed:** `fibre_slab_check.lean` (this directory). `slabAt_not_mem`
  (every fibre slab ∉ carrier) and `slab3_eq_compl_inter` compile against the built
  `QuerySystem.UlamWitnessLatticeGap` oleans (`lake env lean`, 2026-09-22). `#print axioms`
  on both returns `[propext, Classical.choice, Quot.sound]`. The check generalises
  `trace_slab` / `slab_codes_differ` / `slab0_not_mem` by index, which is real mathematics
  on existing infrastructure rather than a Sym(F)-invariance detour (that would be
  scaffolding on the closed Aut line).
- **Deliberately not committed to the library:** adding the declarations to
  `UlamWitnessLatticeGap.lean` needs a blueprint node (`blueprint/src/content.tex`) and a
  rerun of the six gates (coverage, checkdecls, axiomcheck, structure, buildtree). It is
  worth doing only if Cor 5.9 is generalised in the paper, and then it is a ~40-line
  replacement of `slab0_not_mem` by `slabAt_not_mem`.
- **Not attempted:** H-5.8 (a matrix-free normal form) — Lean already witnesses it
  structurally, since `nrep_exists` uses only `U.C`, so a restated theorem would certify a
  signature change. H-seg — an open matrix-dependent question, not a formalisation task.
- No `sorry` anywhere; no file under `formalization/` modified.
