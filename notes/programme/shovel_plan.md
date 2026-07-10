# The shovel plan (adopted 2026-07-10)

**The filter:** "complete the seed" ≠ "everything open." A neighbourhood needs
*trustworthy foundations* plus *well-posed vacant lots* — different lists. Four
theorems to prove ourselves; the rest deliberately left open, posed to
shovel-readiness, shipped as invitations not debts.

Sits on top of `frontier_map.md` (which frames the veins); this note fixes
*which* get dug and in what order.

---

## The four theorems (the seed's next season, in order)

### 1. Pruning lemma, phase-parametrized + theorem-let B  *(first: tractable, banks the tool)*
With it, Safe(ρ) is provably eventually-periodic and effectively computable — the
*instrument* an outsider runs on their own examples. A neighbourhood attracts
builders when there's a certificate-backed decision procedure. Most tractable
item: finite, at its best-ever specification, incubating at the head of the
design lane. Joint-1 ⟦HAND⟧ closure exists (73728-check adversarial scan 0-fail);
the work = the proved, phase-parametrized statement.
Nav: `papers/reconstruction/notes/pruning_k2_theorem.md`; frontier item 2 (Joint 1).

### 2. The OML case at the regularity transition  *(the defining boundary)*
Does a concrete σ-complete orthomodular **lattice** carry a σ-essential state?
Conjectured NO. First question the quantum-logic community asks (lattice = their
default object; the lineage is lattice-titled); the paper's most visible open
edge. Either exit completes the crossing: lattices tame ⟹ the slogan becomes a
theorem (*the phenomenon lives strictly between orthomodular poset and
orthomodular lattice*, non-latticehood certified as discriminator); a lattice
witness ⟹ bigger result than the current one. Evidence strong (three independent
meet-destruction mechanisms; every wild object a non-lattice); difficulty real —
needs an idea, not a refinement. Also quietly discharges the σ-scale
non-distributivity scoping caveat (spine needs only necessity, proved; the
sufficiency-side precision IS this question). This is the load-bearing CASE of
the latticehood family; the full family stays a vacant lot.
**Attack opened 2026-07-10 s8** — statement of record, mechanisms, skeletons
A/B/C, scout results: `notes/open_questions/oml_lattice_regularity_attack.md`
(see §Execution-order item 3 for current next-step).
**s9 (audited):** first banked result — theorem-let: *no non-Boolean concrete
σ-class OML has all its σ-additive states JP* (MPT 1992 Props 3.2 + 4.4
primary-verified, ⟦HAND⟧ glue only; note §7c) ⟹ BNPW 1985 excluded from
Adm ∩ OML under every reading (BNPW pull demoted to confirmation-only);
Skeleton C's first half REFUTED as stated (MO₂, machine-checked); Prop 4.4
= new lever for Skeleton B.
Nav: `papers/spine/` §4; frontier item 1.

### 3. Positive-selection, at least to a consistency bound  *(the recruiting hook)*
Can a non-principal coherent σ-additive selection exist on an admissible carrier
— the inverted question, where large-cardinal strength may genuinely hide (Ψ, the
negative instance, cost nothing). Doesn't need full resolution: the right partial
statement (UB from a measurable, or LB via an inner-model argument) turns a
remark into an open problem with stakes — the hook that recruits a set theorist.
**Inherited fences** (from `sigma_essential_large_cardinal_bounds.md`): forcing
is the WRONG ENGINE for strength transfer (Lévy–Solovay); the Ulam-style LB route
is DEAD on the concrete carrier (no masa, §3a). New engines only.
Nav: frontier item 3 (third descendant); bounds hub.

### 4. A first exact slice of the Φ-characterization  *(the template)*
Not the full boundary of Φ among concrete σ-classes — ONE nontrivial
exactly-characterized subclass (candidates: σ-classes with countably many blocks;
quotient carriers), proved by us, with the product Ulam carrier as canonical
failure and the CE machinery as the standing candidate criterion (closes the loop
to the programme's oldest thread). First theorems in a would-be area double as
templates others imitate on the general case. Note the quarantine theorem
explicitly does NOT touch this.
Nav: frontier item 3 (second descendant); `papers/spine/notes/VERIFICATION_PASS.md`.

---

## The vacant lots (open by design, posed to shovel-readiness)
- **Latticehood family across all three transitions** — the hard central
  conjecture (theorem 2 above = its load-bearing case).
- **Universal impossibility** (the fork; combinatorics hook). ⚠ Disposition of
  the ACTIVE crossed-cycle sub-attack is the one open sequencing question — see
  interaction note below.
- **Minimal-cardinality question for the witness** (the tower's exact edge).
- **No-singletons regime** (literal irreducibility; needs a rigidity mechanism
  we don't have).
- **The statistics layer** (the applied hook — the community that arrives with
  data rather than lattices; prior-art verdict pending, frontier item 4).

A field with everything closed attracts citations; certified foundations +
graded open problems attract *inhabitants*.

## Execution order (recorded 2026-07-10, post-consolidation)

1. **Clear the small owed debts** (each ≤ a session):
   a. ✅ DONE 2026-07-10 (session 5): lock-avoidance lemma PROVED (crossed-
      cycle branch of L-B closed; census law now a theorem) + hostile
      prior-art scout run (equivalence & primitive⟹crossed NOT FOUND;
      Thomassen citation corrected). See
      `papers/reconstruction/notes/HANDOFF_2026-07-10_session5.md`.
   b. ✅ ALREADY DONE — discovered 2026-07-10 (session 6) that this debt was
      paid 2026-06-13 in commit `931a565` ("Paper II §4: reposition
      philosophical upshot as honest synthesis"): §4 repositioned as
      positioning-not-novelty, Stairs 1983 + arXiv:2603.22353 (Gunji2026)
      cited in text and bib. The "owed" record was stale.
2. ✅ **Theorem 1 DONE 2026-07-10 (session 7)** — pruning lemma
   phase-parametrized + theorem-let B: full written proof (Theorem P all k +
   generator lemma + Lemma NG overcount; Theorem B effective certificate) in
   `papers/reconstruction/notes/pruning_theorem_and_B.md`; instrument
   `papers/reconstruction/oracles/safe_rho_instrument.py` (Safe(ρ)
   certificate, raw-DFS-anchored per-k, 15 targets, all windows crossing
   S+P, 0 failures; reproduces Safe(ρ₂₀)=6ℤ and Safe(ρ₁₃)={3} with the
   cofinite tail certified). ⟦HAND⟧ + instrument; Lean durability optional,
   still not owed.
3. **Theorem 2** — OML-lattice case at regularity. **ATTACK OPENED
   2026-07-10 (session 8):** `notes/open_questions/oml_lattice_regularity_attack.md`
   — three meet-destruction mechanisms collected; conjecture split into 2a
   (representability: concrete σ-complete irreducible non-Boolean OML ⟹
   Polish-representable ⟹ tame via DW) + 2b (direct); three proof skeletons
   (A representability, B meet-closed-overlap dichotomy, C Jauch–Piron
   forcing); scout run (Q3 negative: NO infinite concrete σ-complete
   non-Boolean irreducible OML located anywhere — 2a plausibly
   open-but-unasked). Named obstruction = the engine gap (RDP too strong /
   Polish not known to apply). **Session 9 (audited): theorem-let banked —
   no non-Boolean concrete σ-class OML has all σ-additive states JP
   (MPT 1992 Props 3.2 + 4.4 primary-verified; ⟦HAND⟧ glue; attack note
   §7c) ⟹ BNPW 1985 not in Adm ∩ OML under any reading; Skeleton C first
   half REFUTED by MO₂ (σ-JP-forcing = Booleanness-forcing on concrete
   σ-class OMLs); Prop 4.4 = new lever for Skeleton B (any lattice in 𝒞
   has an intersection-poor pair + non-JP Dirac state). s9b (user
   directive): user-gated items PARKED as non-blocking — ILL pulls
   (Bunce–Hamhalter 2000; BNPW 1985 confirmation-grade) are background,
   nothing waits on them (B–H treated as unknown, cite nothing). Next =
   the LLM-doable frontier, any order: (i) Skeleton B cold attack
   (⟦HAND⟧, Prop 4.4 proof pattern as entry); (ii) Skeleton A read — DW
   Thm D.6 + Maharam §8, PDFs IN LIBRARY (derr_williamson_2023.pdf,
   maharam_1972.pdf): locate the load-bearing inner-regularity step, ask
   what latticehood could re-supply; (iii) Skeleton C surviving branch —
   PP1994 σ-unitality engine analysis (ptak_pulmannova_1994.pdf in
   library).**
4. **Theorems 3–4** — positive-selection bound, then one exact Φ-slice.
5. **Parallel, user-gated — PARKED, blocks nothing (s9b directive):**
   σ-essential dissemination (FIDELITY_REVIEW sign-off + abstract length =
   user's), the statistics-layer prior-art verdict (deep-research run is
   out; Phase-1 seed gated on it), ILL pulls (B–H 2000; BNPW 1985), and
   the ⟦HAND⟧-glue checks (pruning proof-read; attack note §7c glue).
   None of these gate the theorem work; they resolve whenever the user
   gets to them.

Nothing in 2–4 blocks anything else; dissemination independent. Open user
decision: fidelity-review sign-off. (Recommendation 1a executed 2026-07-10:
the lemma is banked; the fork's crossed-cycle basement is finished. The
remaining open half of L-B — bar-D aperiodicity — parks with the vacant lot
as planned.)

## Interactions
- **None of the four gate dissemination.** 1 and 3 would strengthen the
  σ-essential paper's reception, but it stands without them; 2 completes
  reconstruction internally; 4 is spine-level. Sequencing stays independent —
  ship when ready (σ-essential first + alone, standing recommendation).
- **Crossed-cycle sub-attack vs vacant-lot status** — RESOLVED 2026-07-10
  (session 5): the lock-avoidance lemma is PROVED and banked
  (`HANDOFF_2026-07-10_session5.md`); "no safe-on-odds" is certified and the
  census law is a theorem. The rest of the fork (bar-D aperiodic half of L-B
  + the winding-2→full bridge) parks as the open lot, basement finished.
