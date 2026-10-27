## Audit: notes/open_questions/cyclic_marginal/hidden_failure/SEED.md (mode: full) — Phase 2, 2026-10-26

reviewed: false. Hostile referee, opus. Shelf first (SHELF_INDEX, taxonomy `owned_regions`), then about 10 standard web
searches. Read levels are given per source. One probe was computed for this audit (§2), with its script kept outside
the repo at `notes/open_questions/verification/audit_exclusivity/ (copied from /tmp/audit_ce/)ce1_test.py`. Nothing in the repo was edited except this file.

### Declared contribution type(s): Type 1, Type 3, Type 6 (declared, with bars). Seed is Phase-2 ready.

### Pure Verdict: UNCLEAR (headline two-thirds KNOWN; narrowed kernel NOT FOUND)

**Stripped statement (standard language).**

Let Ω = [r₁]×[r₂]×[r₃] be finite, A the no-three-way-interaction design matrix, and L ⊂ ℝ^Ω its row space (the span of
the pair-cell indicators). Let P = conv(columns of A) be the marginal polytope, and let D be the smallest family of
subsets of Ω that contains the pair cells and is closed under complement and disjoint union (a finite concrete logic /
λ-system).

- A **carrier state** is a consistent, normalised pair-law vector μ with μ(E) ≥ 0 for every E ∈ D. Write K_D for the
  set of carrier states. The functional is automatically linear on L, by Dynkin induction.
- A "mixture of points" is a μ ∈ P, i.e. a state that extends to a state on 2^Ω.

**Claim:** K_D = P ⇔ P is compressed (⇔ r₂ ≥ 4 and r₃ ≥ 3 fails, sorted).

By cone duality this is: cone(1_D) = L ∩ ℝ^Ω_{≥0} ⇔ compressed.

Let K_{V01} be the set of μ that are ≥ 0 on every 0/1 vector in L. Then:

- **(a) K_{V01} = P ⇔ compressed.** This is Sullivant 2006 Thm 2.4, condition (2), restated. Facet functionals of P
  are the extreme rays of L₊, and width one means a multiple of a 0/1 vector. It takes two lines and is
  **folklore-level / KNOWN**.
- **(b) Not compressed ⇒ K_D ⊋ P.** Since D ⊆ V01, K_D ⊇ K_{V01} ⊋ P. Separation from an exact non-binary ray
  gives this. On a finite Ω this is plain Farkas. Maharam 6.1, "finitely additive" and "countable disjoint union" are
  costume here, since every state on a finite D is finitely additive and every union is finite. **Trivial given
  Sullivant.**
- **(c) Compressed ⇒ K_D = K_{V01}.** It suffices that every 0/1 facet functional lies in cone(1_D). The seed proves
  the stronger **D = V01 at r×s×2 and r×3×3**. This is the **only candidate new mathematics**. It is a combinatorial
  lemma about a generated λ-system, and it does not follow from Sullivant: a λ-system is in general smaller than the
  0/1 part of its span (cf. Keleti–Preiss for the infinite case, and the in-repo E* over ℤ).

**Owned (cite, don't claim):**

| Item | Owner | Read level |
|---|---|---|
| Threshold, including 3×4×4 as the first failure | Sullivant 2006 Prop 5.8 | full text, this audit |
| Size table | Ohsugi–Hibi 2010 | shelf, read |
| (a) | Sullivant Thm 2.4 | full text |
| Template "compressed ⇔ a relaxation is exact" | Sullivant Thm 4.3 / Cor 5.1 | full text |
| Cone/mixture criterion | Maharam 1972; Berti–Rigo 2021; Horn–Tarski via Bhaskara Rao Thm 3.2.10 | shelf / secondary |
| Pairwise-consistent but no joint on a cycle | Vorob'ev; BFMY 1983; Atserias–Kolaitis 2020/21 | shelf, PDF grep |
| Probabilistic vs logical hierarchy | Abramsky–Brandenburger 2011 | shelf |

Atserias–Kolaitis was grepped this audit: it has no compressed or size threshold. Its integer and NP-hardness
results concern the normal/Hilbert-basis side, a different threshold.

**New owner-of-framing found (must be added as an owned region):**

- **De Simone–Navara–Pták 2007** (IJTP 46; arXiv math-ph/0311012), full text read this audit. It poses exactly the
  seed's question for a general finite concrete logic Δ ⊆ exp X: when does a state on Δ extend to a state on exp X?
  They handle X_even and difference-closed logics, and their Thm 2.8/2.9 has the same shape as the seed: a signed
  extension exists, so the question reduces to positivity.
- The seed's D is a finite concrete logic, so **the seed's question is an instance of the DNP/Ovchinnikov
  state-extension problem**. The answer for this family (the triangle logic, as a function of sizes) was not found.
- **Ovchinnikov, "Measures on finite concrete logics", PAMS 127 (1999) 1957–66**, and **Ovchinnikov–Sultanbekov, IJTP
  37 (1998)**: abstract only (AMS page 403). Both study exactly this extension problem for finite concrete logics. If
  either gives a general structural criterion, the triangle could fall out of it. **READ BOTH IN FULL BEFORE ANY
  CLAIM.** This is the single biggest residual kill risk.

**Hostile probe: is D a disguised exclusivity principle?** (computed this audit; facets from cdd, LP via HiGHS, then exact re-check at 3×3×3)

- CE¹ is the single-copy exclusivity / local-orthogonality relaxation: consistent pair laws with Σ over every maximal
  clique of pairwise-disjoint cells ≤ 1. Every carrier state lies in CE¹.
- For each facet of P, the probe minimised the facet functional over CE¹.

| Size | Facets | Max cliques | Facets violated on CE¹ |
|---|---|---|---|
| 2×2×2 | 16 | 17 | 0 |
| 2×2×3 | 28 | 37 | 0 |
| 2×3×3 | 57 | 89 | 0 |
| 2×2×4 | 48 | 77 | 0 |
| 2×3×4 | 110 | 193 | 0 |
| 2×4×4 | 228 | 425 | 0 |
| **3×3×3** | 207 | 237 | **72** (worst −1/6) |
| **3×3×4** | 717 | 533 | **432** (worst −1/6) |

All facets at all of these sizes are width one, consistent with Sullivant.

- **Exact upgrade at 3×3×3** (`notes/open_questions/verification/audit_exclusivity/ (copied from /tmp/audit_ce/)ce1_vs_D.py`):
  - exact closure gives |D| = 15914, matching the repo;
  - all 72 violated facet supports S lie in D (exact bitmask lookup);
  - each LP minimiser, rationalised, satisfies every clique and consistency constraint exactly, with μ(S) < 0 exactly.
  - So **CE¹ ⊋ K_D at 3×3×3 is exact**, independent of the seed's r×3×3 enumeration. It is also consistent with the seed's D = V01 at 3×3×3: no facet support was missing from D.
  - 3×3×4 is float-level only, since D was not closed.
- **Reading:**
  - **At r×s×2 the standard CE¹/LO relaxation is already exact** at every size tested. There the seed's lemma is
    implied by a weaker, standard relaxation, so that half carries little independent weight. It is plausibly a
    known or perfect-graph-type fact; not searched to closure.
  - **At r×3×3, CE¹ is strictly larger than P, while D is exact** (seed, exact enumeration). So D's *iterated*
    constructions (complements of disjoint unions of complements…) do real work exactly on the r×3×3 family.
- This **sharpens and saves the kernel.** The surviving candidate is:
  > *On the triangle, the λ-closure relaxation is exact at every compressed size, and at r×3×3 it is strictly
  > stronger than single-copy exclusivity.*
- This was not found in algebraic statistics (Sullivant, Ohsugi–Hibi, Aoki–Takemura snippets), contextuality
  (AFLS 2015, LO, Abramsky–Hardy logical Bell inequalities: snippet/abstract), concrete logics (DNP read; Ovchinnikov
  unread), or databases (AK grep).

**Would an expert say "obvious"?** For (a) and (b), yes. For (c) at r×3×3, no: the seed needed slicing plus exhaustive
enumeration, and the natural one-step relaxation fails there.

**Residual risk.** Vlach 1986 and Aoki–Takemura give the face structure / Markov bases of 3×3×K. A referee would ask
for a facet-class-by-facet-class buildability proof instead of enumeration, which is not a kill. The same facet
literature might contain a "every facet is a clique/logical inequality" statement; not found at snippet level.

### Applied Verdict: not evaluated as a pass

No pipeline or data is shown, and the seed disclaims practical occurrence. On the practitioner test ("I check
pairwise consistency plus LP feasibility; why your event checks?"), the seed has no answer: the LP is cheap and
exact, so the event checks are dominated. **FAIL / N/A.**

### Contribution Type Verdicts

**Type 1 (new theorem): UNCLEAR.** The narrowed kernel could pass, conditional on the items below.

The headline "hidden failure possible iff r₂ ≥ 4, r₃ ≥ 3" is, as stated, two-thirds owned:
- the threshold is Sullivant's (Prop 5.8);
- ⇐ is trivial, by Thm 2.4 plus Farkas.

What can be claimed is lemma (c), with the CE¹ separation as the reason it is not cheap. Conditions:
1. Read Ovchinnikov 1999 and Ovchinnikov–Sultanbekov 1998 in full.
2. Fresh-context check of r×3×3 (already a seed gate).
3. Close the rigour gaps below.

**Rigour gaps a referee would flag:**
- **i. Explicit 3×4×4 example.** `certify_344.py` rests "Λ ≥ 0 on all of V01" on HiGHS MILP optimality, which is
  float. Only the optimum's value is re-checked exactly, so the explicit example is **not exactly certified**.
  - `intuition_kit.tex` §3 has "certified by computation" struck through, while the seed says "certified": they are
    inconsistent.
  - The abstract existence of a hidden state is unaffected, because the ray is exact.
  - Fix: since D ⊆ V01 is all that is used, enumerate the 0/1 facet functionals of P at 3×4×4 exactly (cdd in
    rationals), or certify with an exact ILP/SAT.
- **ii. Row-type enumeration.** `rx3x3_row_types.py` searches k ∈ [−2,2]³ and h ∈ [−3,3]. Write down why this range
  is exhaustive up to the shift (h,k) → (h+c, k−c).
- **iii. Status of the r×3×3 step.** It is now exact (`rx3x3_exact.py`: c₀ ≤ 3 exact carriers; c₀ = 4 via a pullback
  supply), so the "4×3×3 LP float" note in §22 is superseded. Say so in the seed.
- **iv. Transport for heterogeneous sizes.** It is hand-level, but it is a standard 3-line λ-system argument
  (preimages commute with complement and disjoint union), not a real gap.
- **v. Costume.** Drop Maharam, finite additivity and countable unions in the finite statement. Keep them only for
  the infinite side.
- **vi. Volume figure.** The "29% by volume" figure is float or sampled; label it so.

**Type 3 (unifying framework / method transfer): FAIL.**
- What moves from algebraic statistics is a *criterion*, Thm 2.4, used once, for the trivial direction.
- The non-trivial direction (c) uses no algebraic-statistics technique: it is slicing plus enumeration.
- The "new statement in the target field" (event-level checks certify noncontextuality iff compressed) is a
  restatement of (a) plus lemma (c). No technique becomes available in contextuality or merging that was not there.
- Pattern-coincidence with Sullivant's LP-exactness template is explicitly the failure mode named by the bar.

**Type 6 (exposition/translation): FAIL as a standalone contribution.**
- (a) The audience, contextuality and data-merging readers, is named.
- (b) The literature is not inaccessible. Sullivant 2006 is open access (arXiv math/0412535), 14 pages, with the
  triangle classification stated as Prop 5.8. Ohsugi–Hibi is on arXiv. Contextuality readers already have the
  marginal/noncontextual-polytope language (Araújo et al.; KIO 2406.19961 on cycle scenarios with arbitrary outcomes;
  AFLS 2015).
  - Unverified: whether Sullivant's textbook *Algebraic Statistics* (AMS 2018) covers compressedness and disclosure.
- (c) The translation (facets ↔ extreme rays of the nonnegative span cone) is notation.
- The puzzle (three committees) is good exposition. It can carry a note, but it does not clear the bar.

**Better-fitting type:** narrowed Type 1, i.e. lemma (c) plus the CE¹ separation. Type 5 does not fit: no active
direction is closed. Type 4 was not declared and was not tested.

### Cross-reference

The components are known: the threshold, the relaxation template, the mixture criterion, and the state-extension
problem on finite concrete logics.

The novelty is confined to one combinatorial lemma (D = V01 at compressed sizes). It is non-trivial only on r×3×3,
where the probe shows that the standard exclusivity relaxation fails. Type 3 and Type 6 add nothing beyond Type 1.

**Taxonomy updates (owned_by):**
- add `own.state_extension_finite_concrete_logics`:
  - De Simone–Navara–Pták 2007 (full text read): the problem and the signed-then-positive pattern;
  - Ovchinnikov PAMS 1999 and Ovchinnikov–Sultanbekov IJTP 1998 (abstract only; owed);
  - Horn–Tarski criterion (Bhaskara Rao 3.2.10, secondary).
- append to `own.compressed_threshold`: "K_{V01} = P ⇔ compressed is Thm 2.4 verbatim".
- record the CE¹ probe as data on `own.exclusivity_principle`: CE¹ is exact at r×s×2 (6 sizes) and strictly larger at
  3×3×3 and 3×3×4. This answers that region's owed question: D-states ≠ single-copy E-principle in general.

**WHY.md:** this is the cleanest finite instance of "local views each correct, every question built from them
consistent, yet no world". It bears on *hidden idealisation* (the gap appears only where the facet geometry stops
being 0/1) and on *loop*: trees glue, and this triangle hides only past a size threshold. It changes no bar.

### Coverage: named, not searched (honesty)

- **Not searched this audit:**
  - Bernstein–Sullivant (unimodular binary hierarchical models);
  - Rauh–Kahle;
  - Dobra–Fienberg bounds;
  - Hoşten–Sullivant;
  - Malvestuto;
  - Capotorti–Vantaggi (on a finite Ω, coherence = extendability, a direct neighbour of K_D vs P);
  - the Abramsky–Barbosa–Mansfield contextual fraction;
  - Bhaskara Rao (beyond Thm 3.2.10);
  - Vlach 1986.
- **Czech school (σ-classes, Navara–Pták 1983, Chrapčiaková).** Per `own.sigma_class_integral_additivity`, which was
  read earlier, these concern two-valued states and integral additivity. **No finite size threshold** is recorded
  there, and none was found this pass.
  - Finite two-valued states on D are points (in-repo), so that school's mechanism does not reach the probabilistic
    finite threshold.
- **Ovchinnikov 1999.** A full-text fetch was attempted: AMS PDF 403; the KPFU record lists only a 42 KB file, not
  opened. It remains OWED.

### Recommendation

**Do not draft the headline theorem.** Redirect to the narrowed Type-1 kernel. Before Phase 3:

1. Read Ovchinnikov 1999 and Ovchinnikov–Sultanbekov 1998 in full. This is the kill risk.
2. Fresh-context check of r×3×3, and ideally a facet-class proof using the 3×3×K facet description (Vlach 1986 /
   Aoki–Takemura) instead of enumeration.
3. Make the 3×4×4 example exactly certified, or stop calling it certified. Fix the kit and seed inconsistency.
4. Decide whether the r×s×2 half is subsumed by CE¹ exactness, and look for an owner (perfect-graph / exclusivity
   literature).
5. Re-run `/audit pure` on the narrowed statement.

Types evaluated: 1 (UNCLEAR), 3 (FAIL), 6 (FAIL). Applied: N/A.

Sources (web, standard mode):
- Ovchinnikov PAMS 1999 abstract: https://www.ams.org/journals/proc/1999-127-07/S0002-9939-99-04761-9 (403;
  abstract via search), https://dspace.kpfu.ru/xmlui/handle/net/132998
- Ovchinnikov–Sultanbekov: https://portal.mardi4nfdi.de/entity/Q1266012 (abstract)
- AFLS: https://arxiv.org/abs/1212.4084 (snippet)
- LO: https://arxiv.org/abs/1210.3018 (snippet)
- Abramsky–Hardy: https://arxiv.org/abs/1203.1352 (abstract)
- KIO: https://arxiv.org/abs/2406.19961 (abstract)
- Aoki–Takemura: https://www.keisu.t.u-tokyo.ac.jp/data/2002/METR02-02.pdf (snippet)
- Sullivant: https://arxiv.org/abs/math/0412535 (full text, shelf)
