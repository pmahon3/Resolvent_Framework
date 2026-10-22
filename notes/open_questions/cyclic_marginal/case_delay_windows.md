# Case study 2: delay windows of one observable (2026-10-19)

reviewed: false. This is a CASE, not a generalisation (memory: feedback_reflective_equilibrium).
It is a companion to `case_heteroclinic_averages.md`.

## The system and the method

- **System.** The same rock-paper-scissors heteroclinic cycle (a/b = 2), observed through ONE
  scalar: y = which species is dominant. This is the delay-embedding setting the programme grew out
  of.
- **Queries.** Long-run frequencies of delay windows (y_t, y_{t+τ}). Lags 1, 1 and 2 make a
  triangle of windows.
- **Joint askability.** Each observer averages over its own epoch, as in case 1.
- **What a world is here.** One joint long-run law of (y_t, y_{t+1}, y_{t+2}) that produces all the
  window tables.

## Findings

**D1. Temporal windows of one observable share too much to twist.** ⟦hand⟧
- Every overlap between delay windows shares the *whole* one-time distribution of y.
- On a slowly switching system the lag tables are about diag(w): the system rarely switches within
  a lag.
- So observers who agree on overlaps share w, and the diagonal joint law fits them all. No
  pointlessness is possible.
- In case 1 the stations watched *different* species and shared only one species each. That is
  what let them disagree in a loop.

**D2. Confirmed numerically.** `verification/case2_delay_lags.py`
- The off-diagonal mass of the running lag tables shrinks roughly like 1/t at every lag. At lag 10
  it goes 0.094 → 0.037 → 0.014 over t = 800 → 2400 → 8000.

## What this does to the concepts (equilibrium so far)

- **Pushback.** In these two cases the twist needs observers of *different* variables, i.e.
  spatially separated views. Time windows of one variable did not twist here. This weakens the
  "cycle in time" metaphor again (cf. priority 3).
- **Scope.** This is one slowly switching system. A fast-mixing system, whose lag tables are not
  diagonal, could behave differently. A system whose transition statistics drift while its
  occupation statistics don't would be the natural place to look. Not tested.
- **Not supported:** any generalisation. Two cases so far.
