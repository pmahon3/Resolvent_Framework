"""
Exhaustive class-rho0 stall search at (p,q) = (9,27) (session 5).

The all-dirty 2c stall (the last case of the lock-avoidance proof) forces
every participating shared vertex into the class tau(y) = (j_y - i_y) mod q
== multiple of p (class rho0), and needs p >= 2M+2 with q = Mp; (9,27) is
the smallest instance. This script enumerates ALL class-rho0 glueings
(shared vertices at distinct i-slots, tau in {0, 9, 18}) and checks:
  - all-odd survivors with failing (9,27) pairs: do they violate L1
    (no pair works at laps (1,1))?
  - step-9 endgame dichotomy on every failing pair's minimal ordered kill
    (via lock_avoidance_probe_endgame.endgame_check).

Result on record (2026-07-10): 72,171 configs checked, 2,358 all-odd with
failing pairs, 0 L1 violations; 7,458 failing pairs, all 2c minimal-kill
endgames verified, 0 assertion failures.
"""
import sys, os, itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crossed_cycle_master_lemma import simple_cycles
from lock_avoidance_lemma import (build_glued, odd_cycle_pairs,
                                  kill_edges_11, family_search)
from lock_avoidance_probe_endgame import endgame_check

def main():
    p, q = 9, 27
    checked = allodd_fail = l1_viol = n_fail = n_2c = 0
    for s in (8, 9):
        for islots in itertools.combinations(range(9), s):
            if 0 not in islots:
                continue
            for taus in itertools.product((0, 9, 18), repeat=s):
                jpos = tuple((i + t - islots[0] - taus[0]) % q
                             for i, t in zip(islots, taus))
                if len(set(jpos)) < s or jpos[0] != 0:
                    continue
                checked += 1
                rel, A = build_glued(p, q, islots, jpos)
                cycles = simple_cycles(rel, A)
                if any(len(C) % 2 == 0 for C in cycles):
                    continue
                had_fail = False
                for Ci, Cj in odd_cycle_pairs(cycles):
                    kills = kill_edges_11(Ci, Cj)
                    if any(not ks for ks in kills.values()):
                        continue
                    had_fail = True
                    n_fail += 1
                    if endgame_check(rel, A, Ci, Cj) == 'ok':
                        n_2c += 1
                if had_fail:
                    allodd_fail += 1
                    best, hits = family_search(rel, A, cycles, 5)
                    if best is None or '11mingap' not in hits:
                        l1_viol += 1
                        print("L1 VIOLATION: islots=%s jpos=%s"
                              % (islots, jpos))
    print("configs %d | all-odd-with-failing %d | L1 violations %d | "
          "failing pairs %d | 2c endgames verified %d"
          % (checked, allodd_fail, l1_viol, n_fail, n_2c))

if __name__ == "__main__":
    main()
