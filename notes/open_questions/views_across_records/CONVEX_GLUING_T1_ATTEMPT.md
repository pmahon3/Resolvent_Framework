# T1 (twist–location) attempt: the two-valued and probabilistic cases

reviewed: false. 2026-11-06. Machine-assisted attempt. ⟦HAND⟧ marks arguments not checked by Lean or by an independent
agent. No prior-art pass has been run on anything here, so nothing below is claimed as new. Scripts:
`~/.claude/jobs/26482d7b/tmp/t1/checks.py`.

*Terminology (added 2026-11-06, terminology pass).* "Flat" below = **globally glued / amalgamable**: the window family has a global section (Abramsky–Brandenburger 2011), here one ultrafilter on Ω. New text uses that term; "flat" was dropped because a flat connection can still have holonomy round a loop. Records below are kept as written. See `../../programme/TERMINOLOGY_CROSSWALK.md`.

## Puzzle

Three friends sit at a triangle, and each pair-window shows the pair's actual seat numbers. The views agree, so they give
one seating a. Could a consistent answer pattern on the **built** questions still disagree with a?
- On a ring of 4 or more: no.
- On the triangle: open. Only a question built from infinitely many pieces could do it.

## 1. Statements, in the programme's language

The setting:
- Ω = X^V, with V finite unless stated otherwise.
- The windows are pairs (the edges of a graph G).
- The carrier D is the Dynkin closure of the window events: closed under complements and countable disjoint unions, as
  `D₃` and `glued` are in Lean.
- A state s : D → {0,1} is finitely additive.
- Its window family is (u_w), with u_w an ultrafilter on X^w (`obj.state`).
- The point / ideal point / pointless trichotomy is as in `obj.trichotomy`.

The definitions:
- **Locally ordinary:** every u_w is principal. This is the norm-closed hull of the Diracs. The weak*-closed hull must not
  be used: every ultrafilter is a weak* limit of Diracs, so that reading admits free consensus ultrafilters and makes T1
  false.
  - For non-measurable |X|, locally ordinary is the same as "u_w σ-additive" (Ulam).
- **Trivial twist** means *flat* (`obj.window_family_flatness`): the family amalgamates to an ultrafilter W on Ω.
  - Cycle form: cut the cycle at window k, glue the remaining path by Beck–Chevalley (`own.beta_beck_chevalley`), and ask
    whether some gluing agrees with u_k. This is existential, because two-valued path gluing is not rigid. It is the
    same as flatness.
  - Check (i): the staircase u_k = p⊗p is non-flat (`thm.staircase_no_ideal`), so the pointless triangle is twisted.
  - Check (ii): a consensus family is the restriction of one ultrafilter, so it is flat.
  - Scope: for a single cycle, flat is the same as trivial twist on that cycle. On graphs with two or more cycles,
    per-cycle flatness can be weaker than global flatness. The difference is idle in the two-valued principal case
    (principal families are globally flat), but it is real in the probabilistic multi-cycle case, which is NOT
    addressed here.

Two readings of T1:
- **T1-exist (the framework file's §4 form):** locally ordinary and flat ⇒ the fibre ρ⁻¹(x) contains a point.
- **T1-state (the content):** every state whose window family is principal (resp. flat) is δ_a|D (resp. W|D).
  Equivalently, **no pointless state has a flat window family.** This is `conj.window_restriction_r` O1, restricted to
  flat families.

## 2. T1-exist is a tautology (two-valued)

- Principal window ultrafilters that agree on overlaps assign one value to each site. That gives a ∈ Ω, and δ_a|D lies in
  the fibre.
- More generally, a flat family gives an amalgamation W, and W|D lies in the fibre.
- A principal family is automatically flat. So **the twist hypothesis does no work** in the two-valued case, and the
  framework's T1 should be restated as T1-state. The framework file was not edited; this is a flag for the user.

## 3. Proved ⟦HAND⟧

**Lemma A (bounded base-point decomposition).** Let V be finite and E ∈ D. Then 1_E is a finite signed sum of indicators
of window events and coordinate events, with coefficients bounded by deg(i).
- Proof for the triangle: Box(E) holds (`box_of_mem`, Lean).
- Take corners (x₀,x₁,x₂) and (b₀,b₁,b₂). Box then reads
  1_E(x) = E(x₀x₁b₂) + E(b₀x₁x₂) + E(x₀b₁x₂) − E(x₀b₁b₂) − E(b₀x₁b₂) − E(b₀b₁x₂) + E(b).
  Each term is a window event or a coordinate event.
- The seven-term identity was checked on random pair-sums, n = 5 (`checks.py`).
- General G: the identity "no interaction off the edges" holds at every finite set of corners, and it survives
  complements and countable disjoint unions. So the same ANOVA-at-base-point formula holds ⟦HAND⟧.

**Prop B (coherent ⇒ window-determined).** If a state s on D extends to a linear functional on span{1_F : F ∈ D} (in
particular, to a charge on P(Ω)), then s(F) = Λ(F) := Σ ± u_w(sections of F).
- Proof: apply linearity to Lemma A.
- Λ depends only on the window family. Changing the base point changes the decomposition by bounded coboundaries, and
  equal marginals cancel them (`obs.forced_functional`).
- Corollaries:
  - (a) A coherent state with a principal family equals δ_a.
  - (b) All ideal points with the same window family agree on D.
  - (c) A locally ordinary state other than δ_a|D is automatically pointless (non-coherent), and is not signed-extendable.
- Dead construction: δ_a + (W − W′)|D₃, and any signed combination of ultrafilters (such as `sstar`), is linear. So it
  equals Λ, and gives no counterexample.

**Prop C (triangle-free graphs, V finite, any alphabet, including every ring L ≥ 4): T1-state holds.**
- By `thm.shape_lemma`, E = ⊔ E_w is a finite union over the windows of one star, and s(E) = Σ u_w(E_w).
  - The scope of Lemma shape was re-read in `pointless_coherence.tex`: its closure step covers countable disjoint unions
    (regroup window by window), and the alphabet is arbitrary.
- Principal family: s(E) = Σ 1_{E_w}(a) = 1_E(a).
- Flat family: s(E) = Σ W(E_w) = W(E).
- So forests and all single cycles of length ≥ 4 satisfy T1-state.
- **On a single cycle, a counterexample can only live on the triangle.**
- Scope: V finite. For an infinite star the sum Σ u_w(E_w) is infinite, and finite additivity can break it. This is
  untested.

**Prop D (structure of any triangle counterexample).** Let s have a principal family at a with s ≠ δ_a|D₃. Then:
- s is non-coherent (Prop B).
- s = δ_a on finitely built sets (`obs.forced_functional`).
- Take a disagreement F of least Dynkin rank. It has the form F = ⊔ₙ Fₙ with a ∉ F, s(F) = 1 and s(Fₙ) = 0 for all n.
- So F escapes to infinity in a way no window sees. F also meets every window event that contains a, since disjoint true
  sets are impossible.
- Non-linear two-valued states do exist on concrete logics: De Simone–Navara–Pták Ex 2.2 has 1_A + 1_C = 1_B + 1_D
  (verified in `checks.py`) with s(A)+s(C) = 0 ≠ 2. So linearity on D₃ is a real hypothesis, not automatic.

## 4. What is owned (Task 2)

The acyclic case is **not** exactly Atserias–Kolaitis. The split:
- **Existence along forests:**
  - two-valued: Beck–Chevalley for β (`own.beta_beck_chevalley`);
  - σ-additive: Vorob'ev / BFMY (`own.vorobev_acyclic`);
  - finitely additive probability: charge compatibility (`own.charge_compatibility`).
- **The converse and the reduction to the triangle or an induced C≥4:** A–K arXiv:2009.09488, Thms 3–4 and Lemmas 13–16
  (`own.acyclic_line_and_reduction`). This is about relations and K-relations, not states on D.
- **State-level determination on D:** `thm.shape_lemma` (prior art UNCLEAR).
- **Flat = global section:** Abramsky–Brandenburger Thm 8.1.

## 5. Probabilistic version (Task 4)

Here states are finitely additive probabilities on D, and locally ordinary means each window marginal is σ-additive.

**Lemma E (tightness) ⟦HAND⟧.** Let V be finite and X countable, and let μ be a charge on P(Ω) whose coordinate marginals
are σ-additive. Then μ is σ-additive, and μ = Σ μ{ω}δ_ω.
- Proof: pick finite Kᵢ with μ(xᵢ ∉ Kᵢ) < ε/|V|. Then μ(∏Kᵢ) > 1−ε, so Σ_ω μ{ω} = 1.
- So μ(A) ≥ Σ_{ω∈A} μ{ω}, and the same holds for Aᶜ. The two sides sum to 1, so equality holds.

Consequences:
- **T1-exist (prob.) is again a tautology once flat means "some charge on P(Ω) has these marginals".** Lemma E makes that
  charge a σ-mixture of points: finitely additive gluing of σ-additive window marginals is automatically σ-additive.
- **Non-flat is a real possibility.** It is the cycle marginal problem (twist): for example, anticorrelated fair bits on
  the three edges of the triangle are compatible but have no joint. The finite hidden twists at 3×4×4 (`§16`, `§22`) are
  non-flat, so they are consistent with T1.
- **T1-state (prob.):**
  - holds on triangle-free graphs (Prop C, with s(E) = Σ μ_w(E_w));
  - holds on every finite-alphabet triangle (all of D₃ is finitely built, so s = Λ);
  - holds for coherent states (Prop B with Lemma E);
  - on the infinite triangle, it is open exactly where the two-valued case is open.

**Kolmogorov.** No Kolmogorov-type failure can happen with V finite and X countable (Lemma E). Failure needs infinitely
many sites over a non-product or non-standard Ω.
- Andersen–Jessen (eventually-zero sequences, fair-coin marginals; `papers/paper_i/notes/PAPER_I_REVERSAL_CHECK.md`):
  per-level σ-additivity does not give a σ-additive glued charge.
- Outside scope: infinite V. On {0,1}^ℕ the limit lim_U δ_{eₙ} is locally principal but free; on the path carrier it
  seems to restrict to δ₀ ⟦HAND, untested⟧.

## 6. Counterexample hunt

**None found.** The following are excluded:
- signed combinations of ultrafilters;
- rings L ≥ 4 and triangle-free finite graphs;
- finite alphabets;
- limits of linear states.

What remains is a non-linear two-valued state on D₃ over an infinite alphabet (Prop D).

## 7. Refined conjecture

**T1′ (window determination on the triangle).** Over any alphabet, every finitely additive state on D₃ (two-valued or
probabilistic) equals Λ of its window family, i.e. D₃ is "linear".

Consequences:
- O1 has a positive answer on the triangle.
- **Failure transports upward; proof does not.** Let s be a principal-family counterexample on D₃. Pull it back along ψ,
  which copies the triangle coordinates and sets the other coordinates to constants: s′(E) = s(ψ⁻¹E). This gives a
  principal-family counterexample on D_G for every finite G that contains a triangle.
  - Non-coherence transports too: push forward along the projection π, using π∘ψ = id.
  - The transport is Atserias–Kolaitis Lemma 15 (`thm.loops_travel`; `own.dynkin_good_sets_transport`) ⟦HAND⟧.
  - So the triangle is the minimal case. A proof there does not by itself settle larger graphs with triangles.
- The weaker form that is already proved: T1-state for triangle-free finite covers, and for all coherent states.

Proposed gate (pre-register before running): is every two-valued state on D₃ over ℕ linear?
- Yes ⇒ T1′ holds, and `conj.window_restriction_r` O1 is answered on the triangle (larger graphs with triangles
  still need their own argument).
- No ⇒ a pointless, locally ordinary, untwisted state exists, and T1 fails at the triangle.

## Bearing on WHY.md

- **Loop?** Yes, and specifically the triangle.
- **Hidden idealisation?** If ordinary views ever fail to fix the answers, the failure lives only in infinitely built
  questions. This is a lens, not an application.
