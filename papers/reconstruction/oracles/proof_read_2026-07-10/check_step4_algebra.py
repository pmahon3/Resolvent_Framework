from math import gcd

def modinv(r, k):
    r = r % k
    for x in range(k):
        if (r * x) % k == 1:
            return x
    raise ValueError("no inverse")

fails = []
tested = []
for k in range(2, 9):   # k=1 handled separately by the proof's own remark
    for r in range(1, k+1):
        if gcd(r, k) != 1:
            continue
        rbar = modinv(r, k)
        u = list(range(k))
        def P(v):
            return [v[(j*rbar) % k] for j in range(k)]
        def sigma(v, s):
            return [v[(j+s) % k] for j in range(k)]
        sigma1_u = sigma(u, 1)
        lhs = P(sigma1_u)
        rhs = sigma(P(u), r)
        tested.append((k,r))
        if lhs != rhs:
            fails.append((k, r, lhs, rhs))

print(f"tested {len(tested)} (k,r) pairs, k=2..8, gcd(r,k)=1")
print("FAILS:", fails if fails else "NONE")
