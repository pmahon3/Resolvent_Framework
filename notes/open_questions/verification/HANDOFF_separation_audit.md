# HANDOFF — L₂ dispersion-free/homomorphism separation, AUDIT phase (2026-06-10)

Everything below is durable + committed; working tree clean. This is the single
entry point for resuming. Supersedes `HANDOFF_descent_attack.md` for the
state-level work (that handoff's lattice-level ★ ATTACK is DONE — see below).

## ONE-LINE STATUS

The descent ATTACK's lattice side (★) is fully closed and Lean-verified; scouting
the *state* side produced a **new candidate contribution** — L₂ splits
dispersion-free states from 2-valued homomorphisms (a distinction Boolean & L(H)
fuse) — which is **NOT YET AUDITED**. Next move: `/audit full` on the separation,
then route it per the verdict.

## THE NEXT MOVE — audit the separation

**Invoke (per [[feedback_audit_invocation]]):** the `/audit` skill has
`disable-model-invocation: true`, so launch it as an **opus Agent**, NOT via the
Skill tool. Target = the separation finding.

**Audit target (the claim to be tested):**
> L₂ (the MO₂-block descent witness) has a separating family of σ-additive,
> dispersion-free states that are NOT 2-valued homomorphisms — exhibiting a
> concrete σ-orthocomplete OML on which "dispersion-free state" and "2-valued
> homomorphism" come apart, a distinction that Boolean algebras and L(H) fuse.
> Claimed contribution type(s): **Type 4 (vocabulary)** — the df-state/hom
> separation as a sharp axis — and/or **Type 6/exposition** as a Paper II §5
> refinement. **Bar:** Type 4 three-statements test (3 new statements + 1
> non-trivial result); is the distinction already standard in quantum-logic
> (Kalmbach, Pták–Pulmannová, Gudder)? If the separation is folklore, Type 4
> FAILS and this is at most an internal §5 correction (already applied).

**What the audit must check hardest (the kill-risks):**
1. **Is the df-state/homomorphism distinction already named/standard?** Kalmbach
   1983 Ch.4 treats dispersion-free states on horizontal sums; Gudder's
   concreteness ↔ separating 2-valued states. The containment
   S(A) ⊇ S_σ(A) ⊇ S_df(A) is explicitly called "standard" in Paper II line 626.
   If "df-state need not be a homomorphism" is textbook, Type 4 dies — the
   novelty would only be the *specific L₂ instantiation*, which is thin.
2. **Does L₂ add anything over MO₂?** The whole separation is already visible in
   finite MO₂ (df-state-not-hom is an MO₂ fact). L₂'s contribution is only the
   σ-additive + infinite + concrete packaging. Is that packaging load-bearing or
   decorative? (Compare the repeated "decorative σ-layer" kills in
   [[mechanistic_feasibility_parked]], [[distributed_sensor_contextuality_seed]].)
3. **Two-prizes framing:** is "homomorphism-free σ-additive probability" a real
   slot, or does it collapse into known point-free/relational-probability work
   (Döring, Cannon, localic — see [[oml_relational_prob_novelty]] which already
   mapped this terrain as PARTIALLY OCCUPIED)?

**Honest prior:** lean skeptical. The arc this sits in has died 4× on
"σ-additivity layer is decorative / the object is occupied everywhere"
([[mechanistic_feasibility_parked]]). The df-state/hom distinction being standard
is the most likely kill. The genuinely novel atom, if any: L₂ gets
homomorphism-freeness via the GAP with a rich state space (no KS), vs L(H) via
state-poverty — that *contrast* may clear Type 4 even if the bare distinction is
folklore. Audit should isolate exactly that.

## ROUTING (decided: decide-after-audit)

Do NOT pre-place into a paper. Run the audit, then:
- **Clears Type 4 / refinement bar** → fold into Paper II §5 as the sharp
  df-state/homomorphism distinction (paper already has the Remark hook + the
  MO₂ counterexample from the line-304 fix; that's the seam). Worksheet + Lean
  back it.
- **Clears only as exposition/correction** → the line-304 fix already applied IS
  the landing; record separation in notes, no new draft.
- **Fails all bars** → park honestly to `notes/covered_leads/`, matching the
  arc's prior 4 deaths. The line-304 Paper II fix STILL STANDS (it was a genuine
  bug regardless of whether the separation is a contribution).

## WHAT IS DONE (committed: 9fd95d8, 9ebe51e, 31e88fd)

**Lattice ★ (the gateway) — fully closed, Lean-verified.**
- `formalization/QuerySystem/QuerySystem/DescentWitness{Finite,Infinite,Consistency,Closure}.lean`,
  all 0 sorry. Closure.lean (this session) = hand-legs (ii)+(iii):
  `meet_bot_iff_blockwise`, `ortho_iff_blockwise`, `mo2_cap_two`,
  `mo2_pairwise_ortho_one_zero`, `aW_pairwise_ortho`. `#print axioms` = std trio
  only (NO project axioms — legs verify real content). See [[formalization_status]].

**State separation (the candidate) — verified by building, NOT audited.**
- `verification/l2_state_space_separation.md` — full record.
- `verification/l2_states.py`, `verify_mo2_state.py` — eval states are genuine
  σ-additive dispersion-free states, separating, concentrate p on points.
- `verification/diag_hom.py` — L₂ has NO homomorphism, via the DIAGONAL sub-OML
  (NOT the invalid "MO₂ has none ⟹ L₂ has none" lift — W-vs-L subtlety; the
  diagonal has global top/bot so the gap forces it cleanly, decide-reducible).
- Memory: [[l2_dispersion_free_homomorphism_separation]].

**Paper II §5 bug FIXED (independent of the audit outcome).**
- `papers/paper_ii/distributivity_and_realism_body.tex`: line 304 ("a
  dispersion-free state IS a 2-valued homomorphism") was false in general (L₂
  counterexample) and contradicted the paper's own Remark. 4 edits (VDR def,
  line-304 + MO₂ counterexample, horizontal-sums line, implication-chain line
  523). Operative VDR = dispersion-free state throughout. Compiles, 11pp.
  Remaining homomorphism sites (Boolean/L(H)/categorical/KS) checked — correct.

## DISCIPLINE (per memories)

- **Audit before drafting** (CLAUDE.md). Don't fold into Paper II until the audit
  clears a bar. **Park honestly** if no bar clears.
- Audit = opus Agent, not Skill tool ([[feedback_audit_invocation]]).
- Lit scans → one sonnet scout, not a Workflow ([[feedback_token_economy]]).
- Lean tactic-debug → subagent w/ toolchain (`~/.elan/bin/lake build`, no macOS
  `timeout`). Verify LLM math by building ([[feedback_verify_by_building]]) — this
  session the advisor caught a premature "VDR not blocked" overreach AND an invalid
  homomorphism-lift; both are why the audit prior is skeptical, not confident.
- Math-architecture + routing calls are the USER's.

## KEY MEMORIES
[[l2_dispersion_free_homomorphism_separation]] (the candidate),
[[oml_descent_inhabitation]] (full lead history, ★ + state-scout),
[[formalization_status]] (Lean suite), [[oml_relational_prob_novelty]] +
[[oml_two_point_spaces]] (occupied-terrain priors for the audit),
[[feedback_audit_invocation]], [[feedback_token_economy]],
[[feedback_verify_by_building]].
