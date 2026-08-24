# RESUME — Bell ↔ σ-additive-OML deep research (synthesis only)

> **✅ DONE — this resume is CLOSED (2026-06-10).** The synthesis was completed:
> see `bell_synthesis.md` (same directory). Verdict confirmed — Bell = finitary
> extension axis; does NOT touch the σ-additive descent axis. Nothing to resume.
> File retained only as a record of the deep-research run + the
> [[feedback_token_economy]] 1.35M-token incident (see Cost note below). Do NOT
> re-run.

**Status (2026-06-09):** deep-research workflow ran, adversarially verified
~25 claims, then **died at the synthesis step** on a session/token limit. The
verified claims are saved and durable. Only the *synthesis* remains — it needs
**no** web fetches or new agents. *(↑ superseded: synthesis is now done, see banner.)*

## To finish, in a FRESH context, paste this:

> Read `notes/open_questions/verification/bell_deepresearch_partial.json` — it
> holds ~25 adversarially-verified claims (each with `claim`/`source`/`quote`/
> `vote`) from a deep-research run on how the σ-additive-OML-probability open
> problem (survey `oml_onboarding.tex` §5, the Q1/Q2 frontier) relates to
> Bell's theorem. Synthesize ONLY: merge semantic duplicates, group by the 5
> research angles below, rank by confidence (vote margin), write a cited
> report. Do NOT re-run searches or verification — work only from the saved
> claims. Then answer: (a) is the {σ-additive × point-free × natively
> non-distributive} gap confirmed real? (b) any result that PRE-EMPTS the open
> problem?

## The 5 angles the claims map to
1. Bell as an extension / joint-distribution question (Fine 1982, Pitowsky
   correlation polytope, Horn–Tarski feasibility, Budroni–Morchio PBA/PPT).
2. Finite-vs-countable: does σ-additivity add anything beyond finite additivity
   in the contextuality setting? (Bell/KS are finitary.)
3. Kochen–Specker as a concreteness / no-two-valued-states obstruction; KS vs
   Bell (single-system value-definiteness vs cross-party correlations).
4. Sheaf/presheaf/topos unification (Abramsky–Brandenburger "no global
   section"); is σ-additivity addressed in that literature or is it a gap?
5. Point-free / localic angle; σ-additive probability on a *natively*
   non-distributive (OML, not frame/Heyting) structure — occupied or open?

## Expected verdict (what the survey claims — confirm or break it)
- Bell = the **finitary shadow of the EXTENSION axis** (via Pitowsky/Fine),
  already absorbed in the survey under Pitowsky/Horn–Tarski. ✅ strongly
  supported by saved claims (Fine 5-way equivalence; Budroni–Morchio H-T
  extension; correlation-polytope NP-completeness = finitary).
- Bell does **NOT** touch the σ-additive **DESCENT** axis (the open Q1/Q2).
  Watch for any claim that contradicts this.
- The {σ-additive × point-free × natively non-distributive} combination is the
  open case. Watch angles 4 & 5 for a PRE-EMPTION (someone already posed
  σ-additive point-free probability on an OML).

## Cost note
Full workflow burned ~1.35M tokens / 102 agents. The synthesis-only resume is a
single file-read + one pass (~few k tokens). Do NOT re-launch the workflow.
Saved claims: `bell_deepresearch_partial.json` (32 KB, ~25 claims).
