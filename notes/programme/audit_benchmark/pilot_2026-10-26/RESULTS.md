# Audit pilot 2026-10-26: owner-finding on known items (NOT community calibration)

Scope: does /audit (opus, mode full) find the owner of items whose owner we know? This tests applying
OUR bar; it does not calibrate against community standards (see `feedback_calibrate_to_community`;
community bank pending, web search was rate-limited 2026-10-26).

Blinding: sandbox dir with seed + AUDIT_SKILL.md + contribution_evaluation.md only; instructed not to
read other paths (not enforced). Item C (triangle/Sullivant) dropped: CLAUDE.md names the owner.
Finding: two of three historical kill seeds already cited their own owner (countable-additivity note
cites FHM; Strategy D dossier mentions Gaifman 6x), so seeds A and B were rewritten without owners.

| Item | Ground truth | Web arm | No-web arm |
|---|---|---|---|
| A Strategy D (rewritten) | KNOWN, Gaifman 1964 | KNOWN; simpler kill P(ω)/fin (not ccc); Jech arXiv:1705.01006 §1; Gaifman for ccc version | KNOWN; same P(ω)/fin kill; Gaifman named |
| B countable additivity (rewritten) | KNOWN, FHM 1990 + Loeb 1975; proof broken | KNOWN; proof invalid; Hrushovski-Pillay-Simon arXiv:1002.4763 Rem 6.2(i) (full text); FHM second-hand | KNOWN (Keisler 1985, FHM); proof invalid (Loeb) |
| D planted costume (Vorob'ev) | KNOWN, Vorob'ev 1962 / BFMY 1983 | KNOWN; Vorob'ev; Atserias-Kolaitis §4.1; caught a non-equivalence in the costume (fixed value sets) | — |
| E Livson-Pritam-Prokopenko 2026 (calibration, out of metrics) | our read: neighbour | PARK (Types 1, 4, 6 FAIL); owner Chia 2015 Prop 2.8 (full); claims Thm 5 (RP2) incorrect | — |

Owner hit 6/6 (A, B both arms; D). No-web arms matched web arms: for well-known owners recall may be doing
the work (contamination). False-kill side untested (no known-good item).

Item E, Thm 5 check ⟦HAND, main session, 2026-10-26⟧: identifying the two capping disks of the sphere
N(V) gives a space where edge points have three half-disc sheets (not a surface), with pi_1 = Z
(Klein bottle pi_1 = <a,b | bab^-1 = a^-1>, then the disk kills a), not Z/2. So Thm 5's construction as
defined is not RP2; Thm 4 (Klein bottle) stands. The appendix proof uses a different map (auditor).

Community-calibration contrast: E is on arXiv (v6) and was covered by Quanta, yet fails all our bars and
has an error in Thm 5. Community attention and our bar diverge; one data point.
