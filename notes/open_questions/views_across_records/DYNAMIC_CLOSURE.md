# Decoupling the shape of the centre from dynamics: the dynamic closure (theory + validation + Poland). Pre-registered 2026-11-06, before running

reviewed: false. Responds to: "to what extent have we decoupled the polycentric reading from any dynamical reading?" Answer so far: not for the
shape tests on levels.

## Proposition (⟦HAND⟧; likely owned as the time-series trek rule, cf. Sullivant–Talaska–Draisma 2010; to check)
VAR(1): x_{t+1} = B x_t + ε_t, with ε i.i.d. (0, Q), ρ(B) < 1. Stationary S = Σ_{k≥0} Bᵏ Q Bᵏᵀ. If Q ∈ FW_H, i.e. Q = D + Σ_{S∈H} C_S, then
Bᵏ C_S Bᵏᵀ ⪰ 0 is supported on N_k(S) (sites reachable from S in k steps of G_B), and Bᵏ D Bᵏᵀ is supported on the N_k({i}). Hence
**S ∈ FW_{H*}, H* = {N_k(S) : S ∈ H ∪ singletons, k ≥ 0}** (the interaction-closure of the shock centres).
- Levels confound H (shock centres) with G_B (interactions). A large level reach can come from small shock centres spread by B.
- The reach-k contributions scale like ‖Bᵏ‖², so a large closure reach from small centres needs ρ(B) near 1 (the persistence result in
  `SPACE_TIME_DYNAMICS.md`).
- **Decoupling:** estimate B, form the innovations ε̂, and test Q ∈ FW_H on them. This is valid given consistent VAR estimation (standard), and the bootstrap
  re-fits B in each resample.

## Validation (10-site ring, a = 0.95 own persistence)
- **World Lc (local, closure-large):** shocks on ring edges only (pairwise, at the FW₂ boundary as in P2), plus dispersal d = 0.15 to ring neighbours.
  Innovations ∈ FW₂ (local); levels may need a larger reach.
- **World Rg (regional):** one shock common to all sites plus independent noise (Moran), no dispersal. Innovations ∉ FW₂.
- Tests (m = 2 pairwise ceiling, the cheap local hypothesis): **L** on levels; **I_full** on innovations from a full VAR(1); **I_ring** on innovations from a
  restricted VAR (own lag + two ring-neighbour lags, OLS per site). Spearman, Politis–White blocks, ε = ∞, 500 resamples, re-fitting the VAR in each.
- n ∈ {53, 200}; 100 simulations. Population V_G of levels and innovations reported.
- **Predictions:**
  - Lc: I_full and I_ring ≤ 0.10. L rejects at a rate that rises with n (and the population level V_G > 0).
  - Rg: L, I_full and I_ring all reject (≥ 0.8 at n = 200).
  - I_full may be noisier than I_ring at n = 53 (110 vs 30 parameters).

## Poland (declared now, run after validation; only if I_ring holds size on Lc)
Restricted VAR per site: own lag + the lags of its 2 nearest sites. Innovations → (i) the pairwise V_G test; (ii) the reach test m = 3, 4; (iii) the radius test H(d) on the
same d grid as step 4. Jittered Spearman, 5 jitter draws. **Prediction:** the innovations still require a regional centre (a regional same-time driver), with d̂ in the top
deciles; or, if d̂ drops, the level-scale regionality was partly accumulated local history.

## Validation result (2026-11-06): PASS, predictions held. Script `verification/dynamic_closure.py` (4 min)
| world | population V_G levels / innovations | n = 53: L, I_full, I_ring | n = 200: L, I_full, I_ring |
|---|---|---|---|
| Lc local shocks + dispersal | +2.40 / 0.00 | 0.22, 0.00, 0.00 | **0.78**, **0.00**, **0.00** |
| Rg regional shock | +3.50 / +3.50 | 0.71, 1.00, 0.99 | 0.93, 1.00, 1.00 |
- **Decoupling demonstrated:** in Lc the levels need a big centre (the dynamic closure), while the innovations correctly stay pairwise (size 0.00, full and
  restricted VAR). In Rg the regional same-time shock is detected in both.
- The restricted VAR is as good as the full one here. It is used for Poland.

## Poland innovations result (2026-11-06): the regional centre is a SAME-TIME shock, not accumulated local history
Script `verification/dynamic_closure_poland.py` (2.5 min). Restricted VAR (own lag + 2 nearest sites' lags), n = 52 innovations, 5 jitter draws,
Politis–White blocks, 300 resamples.
| hypothesis on the same-time shocks | T | rejected |
|---|---|---|
| pairwise only | 32.0 | 5/5 |
| reach ≤ 3 | 12.4 | 5/5 |
| reach ≤ 4 | 5.9 | 0/5 |
| radius ≤ 129 … 368 km | 32.0 … 10.2 | 5/5 at every radius |
| radius ≤ 397 km | 7.6 | 0/5 |
- **The innovations reproduce the levels exactly:** m̂* = 4 and d̂ = 397 km. Prediction (first branch) held.
- **Reading:** after removing what the lagged dynamics (own and neighbour carry-over) spread, the *same-time* shocks still need a centre binding stands
  > ~370 km apart. The Polish regionality is a **regional same-time driver** (weather, the solstice-timed cue) or the shared protocol. It is **not** local
  history accumulated by interaction. This fits beech's anti-persistence: a centre in time needs long memory, which beech lacks.
- Within the restricted VAR's assumptions (linear; two-neighbour lags). The protocol confound remains.
