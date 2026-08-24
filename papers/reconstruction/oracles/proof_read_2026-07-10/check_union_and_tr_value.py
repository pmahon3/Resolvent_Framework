"""Two checks:
1. Union/complement of ev.periodic sets: threshold=max(thresholds),
   period=lcm(periods) is a VALID (not necessarily minimal) certificate --
   the proof only claims 'eventually periodic', doesn't claim minimality
   survives union. Verify validity by brute-force random ev-periodic sets.
2. tr_value(certk, L) off-by-one check: certk=(s,p,pred) where pred[t] defined
   for 1<=t<=s+p (from tr_k_certificate). For L<=s+p uses pred[L] directly.
   For L>s+p, uses pred[s+1+((L-s-1) % p)]. Confirm this correctly maps L into
   the periodic window [s+1, s+p] preserving period p from threshold s.
"""
import random
from math import lcm

# --- Check 1: union validity ---
def make_ev_periodic_set(s, p, cap=200, seed=0):
    r = random.Random(seed)
    prefix = [r.random()<0.5 for _ in range(s)]
    period_vals = [r.random()<0.5 for _ in range(p)]
    def member(L):
        if L < s:
            return prefix[L]
        return period_vals[(L-s) % p]
    return member

random.seed(1)
fails=0
for trial in range(100):
    s1,p1 = random.randint(0,5), random.randint(1,5)
    s2,p2 = random.randint(0,5), random.randint(1,5)
    A = make_ev_periodic_set(s1,p1,seed=trial*2)
    B = make_ev_periodic_set(s2,p2,seed=trial*2+1)
    S = max(s1,s2)
    P = lcm(p1,p2)
    # union should be periodic with threshold S, period P (not nec minimal)
    ok = True
    for L in range(S, S+3*P):
        if (A(L) or B(L)) != (A(L+P) or B(L+P)):
            ok = False
    if not ok:
        fails += 1
        print("UNION FAIL", s1,p1,s2,p2)
print(f"Union bookkeeping check: {100-fails}/100 pass (threshold=max, period=lcm valid)")

# --- Check 2: tr_value indexing ---
def tr_value(certk, L):
    s, p, pred = certk
    if L <= s + p:
        return pred[L]
    return pred[s + 1 + ((L - s - 1) % p)]

# Build a fake pred dict consistent with period p from threshold s, defined 1..s+p
random.seed(2)
fails2 = 0
for trial in range(200):
    s = random.randint(0,6)
    p = random.randint(1,6)
    period_vals = [random.random()<0.5 for _ in range(p)]
    prefix_vals = [random.random()<0.5 for _ in range(max(s,1))]
    def true_val(L, s=s, p=p, period_vals=period_vals, prefix_vals=prefix_vals):
        if L <= s:
            # L in [1..s] uses "prefix" (pred[1..s] should be arbitrary/prefix)
            return prefix_vals[(L-1) % len(prefix_vals)]
        else:
            return period_vals[(L - s - 1) % p]
    pred = {t: true_val(t) for t in range(1, s+p+1)}
    certk = (s,p,pred)
    ok = True
    for L in range(1, s+3*p+5):
        expected = true_val(L)
        got = tr_value(certk, L)
        if expected != got:
            ok = False
            print(f"  MISMATCH s={s} p={p} L={L} expected={expected} got={got}")
    if not ok:
        fails2 += 1
print(f"tr_value indexing check: {200-fails2}/200 trials consistent with period p from threshold s")
