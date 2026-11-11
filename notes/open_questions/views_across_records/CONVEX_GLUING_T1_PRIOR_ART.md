# Restated T1 (= O1, `conj.window_restriction_r`): prior-art scout

> **Superseded in part (2026-11-10).** The triangle gate closed YES: D₃ = D_fin, so the window family determines the state on the triangle. Evidence: hand proof, re-derived by two independent agents (`TRIANGLE_5DE_CHECK.md` C6; `TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`: CONFIRMED WITH FIXES); **fully machine-checked later the same day** in `formalization/QuerySystem/QuerySystem/TriangleFinitary.lean` (`mem_dfin`, `state_ext`, `normal_form`; no `sorry`; axioms propext, Classical.choice, Quot.sound; alphabet ℕ, other alphabets by a hand pullback remark); prior art: one weak scout pass (`TRIANGLE_CARRIER_PRIOR_ART.md`: finite case partly owned, infinite normal form and determination not found; Fishburn–Lagarias–Reeds–Shepp, Kemperman and Pták–Pulmannová 1991 unread); not claimed as new. This file is kept as a dated record; statements below that call the infinite triangle, L1, L2 or the level-2 step open are overtaken. See `TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`.

reviewed: false. 2026-11-06. Hostile, cross-field scout of the restated T1 in `CONVEX_GLUING_T1_ATTEMPT.md`.

*Terminology (added 2026-11-06, terminology pass).* "Flat" below = **globally glued / amalgamable**: the window family has a global section (Abramsky–Brandenburger 2011), here one ultrafilter on Ω. New text uses that term; "flat" was dropped because a flat connection can still have holonomy round a loop. Records below are kept as written. See `../../programme/TERMINOLOGY_CROSSWALK.md`.

Read levels:
- [full]: primary text read (shelf PDF, pdftotext);
- [meth]: theorem statements read;
- [snip]: search snippet;
- [recall]: unverified.

Rows already in `glued_carriers_taxonomy.json` are cited by id. ⟦HAND⟧ marks arguments produced in this scout.

**Statement checked.** On D (the Dynkin closure of the pair-window events, V finite, X possibly infinite), no two-valued
finitely additive state with a FLAT window family is pointless. Equivalently on D₃, s = Λ(window family).

**Caveat on "equivalently".** In general, "determined by the generators" and "flat ⇒ not pointless" are different statements:
- Take Ω = ℕ with one generator, the finite–cofinite algebra. Its Dynkin closure is P(ℕ), because every set is a countable
  disjoint union of singletons.
- Two distinct free ultrafilters agree on the generator but differ on P(ℕ).
- Both are ideal points, so "not pointless" holds while "determined" fails.

On D₃ the two statements coincide only through Lemma A and Prop B of the attempt note (⟦HAND⟧, not owned).

## Q1. Is a (two-valued) state on a concrete logic or σ-class determined by its restriction to the generating blocks?

**Verdict: PARTLY OWNED.** It is owned in the finite, σ-additive and finitely-built forms. The general form is false. The
residue, finitely additive states on D₃ with infinite X, is NOT FOUND.

- **σ-additive: OWNED.** The proof of Navara–Pták 1983, Thm 1 (p. 226) says "if two measures agree on all generators of a
  σ-class, they have to agree on the entire σ-class" [full]. The same step is in the Proposition of Navara, Math. Slovaca 34
  (1984), p. 331 [full]. On D this is `own.sigma_generator_uniqueness`: σ-additive two-valued states on D are points.
  - So **any T1 counterexample must be purely finitely additive.**
- **Finite carriers: OWNED / trivial ⟦HAND⟧.** The agreement set {E : s(E) = t(E)} is closed under complements and finite
  disjoint unions. On a finite Ω it is therefore a Dynkin system that contains the generators.
  - So on any finite concrete logic, flat ⇒ s = δ_a.
- **Finitely built sets: OWNED.** See `obs.forced_functional` (Abramsky–Brandenburger Thm 5.9).
- **General finitely additive form: FALSE**, by the finite–cofinite example above. No general owner can exist. A proof of T1′
  must use the triangle structure, namely the bounded base-point decomposition in Lemma A.
- **Nearest finite analogue of T1′ (linearity of D₃): OWNED in the finite case.** Ovchinnikov, PAMS 127 (1999), Thm 3.3,
  p. 1960 [full]: Δ(n×m), the logic of x, y, x+y on a grid, is *regular*, meaning every signed measure extends to a signed
  measure on P(Λ) (Def 2.1). Rem 3.6 adds that its two-valued states are points (via Navara–Pták).
  - Scope gap: Δ(Λ) is finite. It is the difference sub-carrier (x, y, x+y), not D₃ with full pair windows.
  - Infinite Λ is not treated. Rem 3.2 (citing [21] = Navara–Pták) records that integral additivity fails for bounded
    infinitely-valued f, g, but only for **σ-additive** measures on a **non-flat** state (see Q2).
- **Integral-additivity school** (Gudder 1969; Zerbe–Gudder 1985; Dravecký–Šipoš 1980; Navara 1984; Chrapčiaková 1987;
  `own.sigma_class_integral_additivity`). "Λ two-valued" is additivity of the Gudder integral. The whole school assumes
  σ-additive measures, so it never meets the purely finitely additive residue.
- Search: Navara/Pták/De Simone/Ovchinnikov names, plus "state determined by generators" and "signed extension
  concrete logic infinite" [snip]. No owner was found for the finitely additive question on Dynkin systems generated by
  sub-σ-algebras.

## Q2. Do the shelf pointless witnesses have flat window families?

**Verdict: NO, they are all twisted, so the restated T1 is NOT FALSIFIED by them.**

A family of principal window states is flat iff its true fibres have a common point (FIP). Each witness below fails this.

| Witness | True fibres | Common point? | Read |
|---|---|---|---|
| Navara–Pták 1983, Example p. 227: Ω = (ℚ∩(0,1))², windows A_f, A_g, A_{f+g} | B = {x = 1/3}, C = {y = 1/2}, D = {x+y = 1/2} | B∩C∩D = ∅, stated in the paper: impossible triple ⇒ **non-flat** | [full] |
| Dravecký–Šipoš 1980, Ex 6, p. 301 (X = ℝ², α = (0,0), β = (1,1)) | {f = f(α)}, {g = g(α)}, {f+g = f(β)+g(β)} | empty, since f(α)+g(α) ≠ f(β)+g(β) ⇒ **non-flat** | [full] |
| De Simone–Navara–Pták 2007, Ex 2.2 (finite, MO₄) | Aᶜ = {4,5,6}, B = {2,3,4}, Cᶜ = {1,2,6}, D = {1,3,5} | Aᶜ∩B∩Cᶜ = ∅ ⇒ **non-flat** | [full] |
| Navara 1984, final Example (ℤ×ℕ₀; probabilistic, σ-additive) | marginals ½ on f, g, f+g ∈ {0,1} | a joint charge would give E(f+g) = Ef + Eg = 1, but E(f+g) = ½ ⇒ **non-flat** | [full] |

There is a second reason the first two witnesses cannot falsify T1:
- They live on the union class A_f ∪ A_g ∪ A_{f+g}. On that class, determination by the generators is tautological.
- They do not extend to D₃ (`own.dravecky_sipos_flight_subcarrier`).
- They are σ-additive, and every σ-additive two-valued state on D₃ is a point.

Navara 1984 is a case of *determination without flatness*: "the extension … is unique" (p. 335). That is consistent with T1
and irrelevant to it.

Also non-flat, hence consistent:
- Pták 1987 free hidden variable on X_even(4) (h{12} = h{23} = h{13} = 1 forces a common point that does not exist);
- the Zerbe–Gudder 1985 §4 six-point state;
- Gudder 1984 Ex 6.1 (rows / columns / diagonals of ℤ²: the same impossible-triple shape).

All of these come from `own.*` rows; the shape was checked against their recorded data, but the PDFs were not re-read.

## Q3. Non-linear states; triangle carriers with infinite alphabets

**Verdict: NOT FOUND for the infinite triangle.**
- **Non-linear (non-signed-extendable) two-valued states: OWNED, finite only.**
  - DNP 2007 Ex 2.2 (p. 2);
  - DNP 2007 Ex 2.6 (MO₁₅, difference-closed; the state there is only prescribed on six sets, so whether it is two-valued is unstated);
  - DNP 2015 Thm 3;
  - Gudder 1984 Ex 3.2 (Prather class) and Zerbe–Gudder 1985 §4.
- By Q1, on finite (and σ-additive) carriers, **non-linear ⇒ non-flat** ⟦HAND⟧. So every printed non-linear state is twisted,
  and none bears on flat families.
- The only room left for a counterexample is an infinite carrier with a purely finitely additive state. There the agreement
  set is closed only under *finite* disjoint unions: exactly Prop D's "escape to infinity".
- Nothing found on non-linear states on triangle-generated or pair-window carriers with infinite alphabets.
- The nearest infinite results on symmetric logics concern σ-additive extension, not linearity of finitely additive states:
  - DNP 2015 Thms 4–6 [full via shelf index];
  - Bikchentaev–Navara 2016 Ex 4.4 (`own.symmetric_logics_extension`).

**Book checks (hardcopy; NOT blocking for this note).** Neither book is expected to settle the infinite triangle.

1. **Bhaskara Rao & Bhaskara Rao, *Theory of Charges* (1983):**
   - (a) §3.2, Def 3.2.1–3.2.2, Thm 3.2.5 and Thm 3.2.10 (Horn–Tarski extension of partial charges; locations as cited in
     DNP 2007 p. 4). Check whether the criterion has a **signed** version: a {0,1} partial charge s on a Dynkin system
     extends to a bounded signed charge iff Σcᵢ1_{Aᵢ} = 0 ⇒ Σcᵢs(Aᵢ) = 0. That condition is T1′ on D₃.
   - (b) **Thm 3.5.1(v)**, cited in DNP 2007 p. 3 for non-extendability on X_even. This is a new pointer. Check its exact
     statement and whether it covers infinite generated classes.
   - (c) Any uniqueness-of-extension result (Łoś–Marczewski type) for partial charges whose domain is closed under countable
     disjoint unions.
2. **Pták–Pulmannová, *Orthomodular Structures as Quantum Logics* (1991).** The table of contents was not found online,
   so the sections are **to be located by hand**. Look in the concrete-logic and σ-class chapters for:
   - (a) states, or two-valued states, on σ-classes generated by several sub-σ-algebras, and whether they are determined by
     their restrictions;
   - (b) Gudder-integral additivity beyond finitely valued observables, for **finitely additive** states;
   - (c) signed (weak) extension of states on infinite concrete logics.

   These join the existing pinned items in `pinned_book_checks.md`.

## Net

- T1 restated as O1 survives every shelf witness, because all of them are twisted (non-flat).
- The owned parts are the σ-additive form, the finite form, the finitely-built form, and the finite analogue of linearity
  (Ovchinnikov Thm 3.3).
- The live residue is narrow: **purely finitely additive two-valued states on D₃ over an infinite alphabet**, which is the
  gate already proposed in the attempt note.

**Bearing on WHY.md.**
- Hidden idealisation: if flat local views ever fail to fix the answers, the failure has to be finite additivity at
  infinity.
- Every printed failure is a visible loop (a twist), not a hidden one.

Not done: the Pták–Pulmannová and Bhaskara Rao bodies (hardcopy); Chrapčiaková 1987; Navara 1989 (on the shelf, not
grepped). No shelf edits; no commit.
