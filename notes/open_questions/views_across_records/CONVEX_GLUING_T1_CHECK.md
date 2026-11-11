# T1 attempt: independent check

> **Superseded in part (2026-11-10).** The triangle gate closed YES: D₃ = D_fin, so the window family determines the state on the triangle. Evidence: hand proof, re-derived by two independent agents (`TRIANGLE_5DE_CHECK.md` C6; `TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`: CONFIRMED WITH FIXES); **fully machine-checked later the same day** in `formalization/QuerySystem/QuerySystem/TriangleFinitary.lean` (`mem_dfin`, `state_ext`, `normal_form`; no `sorry`; axioms propext, Classical.choice, Quot.sound; alphabet ℕ, other alphabets by a hand pullback remark); prior art: one weak scout pass (`TRIANGLE_CARRIER_PRIOR_ART.md`: finite case partly owned, infinite normal form and determination not found; Fishburn–Lagarias–Reeds–Shepp, Kemperman and Pták–Pulmannová 1991 unread); not claimed as new. This file is kept as a dated record; statements below that call the infinite triangle, L1, L2 or the level-2 step open are overtaken. See `TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`.

reviewed: false. 2026-11-06. Independent check of `CONVEX_GLUING_T1_ATTEMPT.md` (hostile; tried to break each item).
Script: `~/.claude/jobs/26482d7b/tmp/chk/t1chk.py` (binary triangle: |D₃| = 70, matching the paper; the 7-term formula holds
for every E ∈ D₃ at every base point; no singleton lies in D₃; additive signed states on D₃ are fixed by their window values,
with 0 free dimensions left).

*Terminology (added 2026-11-06, terminology pass).* "Flat" below = **globally glued / amalgamable**: the window family has a global section (Abramsky–Brandenburger 2011), here one ultrafilter on Ω. New text uses that term; "flat" was dropped because a flat connection can still have holonomy round a loop. Records below are kept as written. See `../../programme/TERMINOLOGY_CROSSWALK.md`.

Definitions were used consistently with `pointless_coherence.tex` (Appendix): Ω = X^V, carrier D = Dynkin closure of the
window questions (all subsets of X^w pulled back); a state is finitely additive and {0,1}-valued on D; ideal point = W|D for an
ultrafilter W on P(Ω); flat = the window family amalgamates to such a W (`CONVEX_GLUING_EQUILIBRIUM_GATES.md` G3).

## (i) Lemma A + Prop B: CORRECT WITH FIXES

**Actually proved.** Take V finite, any X, any simple graph G, and E ∈ D. For every base point b,
1_E(x) = Σ_{S ∈ {∅} ∪ V ∪ edges} Σ_{T⊆S} (−1)^{|S∖T|} 1_E(x_T, b_{V∖T}).
Every term is a section of E, hence a window or coordinate event in D. Vertex i carries coefficient 1 − deg(i).
If s extends to a linear functional on span{1_F : F ∈ D}, then s(F) = Λ(F) := Σ ± u_w(sections). Λ is independent of b:
a zero sum Σ g_e of edge functions has each g_e separable, since the mixed difference Δ_iΔ_j isolates g_{ij}, so
consistent marginals kill it.

- **Lean match.** `box_of_mem` (TriangleCyclic.lean:149) is exactly the 8-corner identity for X = ℕ on the triangle. Lean's
  `Box` (even-primed corners = odd-primed corners) rearranges to the attempt's 7-term formula; checked by hand and by
  script. Window events in Lean are `windowSigma`-measurable for the discrete ℕ, so all subsets: this matches. **Not in
  Lean:** an alphabet other than ℕ, a general G, and Prop B itself. All of these are routine ⟦HAND⟧ and the steps are sound
  (each S-interaction is a finite zero-sum linear identity, and it survives 1 − f and pointwise countable sums).
- **Fix 1 (a strengthening; it also corrects the wording of Prop D).** You do not need coherence to get s = Λ on finitely
  built sets. The class {E ∈ D : s(E) = Λ(E)} contains the window events and is closed under complements and *finite*
  disjoint unions, for any state, two-valued or probabilistic. So s = Λ on the finite-operation closure, and (X finite) on
  all of D. This is what justifies "all of D₃ is finitely built, so s = Λ" in §5. Note the scope: "finitely built" has to
  mean *finite-operation closure*, not "indicator in the span of window functions". `obs.forced_functional` states it for
  extending states only.
- **Fix 2 (citation).** Check (i) in §1 cites `thm.staircase_no_ideal`, which is the ring result. For the triangle, the
  relevant fact is that `sstar` makes the window steps C₀, C₁, C₂ all true with empty intersection
  (`triangle_pointless_state`), so its family is non-flat.
- **Owned.** `obs.forced_functional` is already marked KNOWN (Abramsky–Brandenburger 5.9). Prop B adds nothing new beyond
  the corollaries.

## (ii) Prop C (triangle-free finite G, incl. rings L ≥ 4): CORRECT

**Actually proved.** Let V be finite, X arbitrary, and G triangle-free. If a state's window family is principal at a, then
s = δ_a|D. If the family is flat with amalgamation W, then s = W|D. Either way the state is not pointless.

- **Steps checked.** Shape lemma: every E = ⊔ E_w is a disjoint union over the windows of one star. Rigidity holds because
  pairwise-meeting 2-sets with no triangle form a star. Slicing at x_c = a works because pieces in independent leaf
  coordinates can only be disjoint if all but one is empty. Closure works by regrouping a countable union window by window.
  Then s(E) = Σ s(E_w), using finite additivity on D, because the star is finite.
- **Hidden assumptions.** Finite degree is the only use of "V finite". The proof goes through on infinite V of bounded
  degree, but that is untested and not claimed. A principal family needs every vertex to lie in some window; isolated
  vertices are invisible to D anyway.
- **Scope.** The shape lemma is ⟦HAND⟧, machine-checked only on finite alphabets, and has prior-art status UNCLEAR
  (taxonomy). The result is only as strong as the shape lemma. Once that lemma is granted, the T1 step is a one-liner.
- The claim "on a single cycle a counterexample lives only on the triangle" is correct. The upward transport in §7
  (ψ⁻¹D_G ⊆ D₃, π⁻¹D₃ ⊆ D_G, π∘ψ = id) also checks out. It needs G to contain the three triangle edges, not an induced
  triangle.

## (iii) Lemma E (V finite, X countable): CORRECT, KNOWN, and over-applied in §5

**Actually proved.** Let μ be a finitely additive probability on **P(Ω)**, Ω = X^V, with V finite and X countable. If every
coordinate marginal is σ-additive on P(X), then μ is σ-additive and μ = Σ μ{ω}δ_ω.

- **Proof checked.** ∏Kᵢ is a finite set, so μ(∏Kᵢ) = Σ_{ω∈∏K} μ{ω} > 1 − ε. Hence Σμ{ω} = 1, and the inequality on A and
  on Aᶜ forces equality.
- **The prompt's diagonal coupling.** It gives no counterexample. A finitely additive coupling of σ-additive marginals on
  ℕ×ℕ, diagonal or not, is tight, so it is σ-additive. The diagonal non-σ-additive couplings are those whose marginal is
  itself a free ultrafilter or charge, and the hypothesis rules those out. Real counterexamples need infinitely many sites
  (Andersen–Jessen). A large X (real-valued measurable) is outside scope.
- **Known.** A charge on P(ℕ) is σ-additive iff Σμ{n} = 1 (Bhaskara Rao & Bhaskara Rao, *Theory of Charges*). Tightness of
  the joint follows from tightness of the marginals by a union bound. This is folklore, so claim no novelty.
- **Fix 3 (substantive).** Lemma E needs μ on P(Ω), or on an algebra containing the finite sets. **States live on D, and
  singletons are not in D₃:** the Box identity fails at a lone corner, which the script confirms. So Lemma E says nothing
  about a non-coherent probabilistic state on D₃ with σ-additive marginals. Two §5 sentences overreach and must be scoped
  to "charges on P(Ω)", i.e. to coherent states:
  - "finitely additive gluing of σ-additive window marginals is automatically σ-additive";
  - "No Kolmogorov-type failure can happen with V finite and X countable".
  The open case (a non-linear probabilistic state on D₃ over ℕ) is exactly what Lemma E does not reach. §5's own last bullet
  ("open exactly where the two-valued case is open") already says this, so the two sentences contradict it unless they are
  scoped.

## Other items

- §2 (T1-exist is a tautology; principal ⇒ flat): correct.
- Prop D: correct. A least-rank disagreement is a countable disjoint union F = ⊔Fₙ. If a ∈ Fₙ, then
  s(F) = s(Fₙ) + s(⊔_{m≠n}F_m) = 1 would agree with δ_a, so a ∉ F, every s(Fₙ) = 0 and s(F) = 1. Meeting every true window
  event follows from additivity. Use the Fix 1 wording for "finitely built".
- Locally ordinary ⇔ σ-additive u_w below the first measurable cardinal: correct (|X²| = |X|).
- Nothing found that makes T1′ false. The gate in §7 is stated correctly.
