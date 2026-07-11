#!/usr/bin/env python3
"""C11 witness -- finite shadow only.  The witness (hand proof):
Omega = N;  K1 = {C_n : n in N}, C_n = {0} u [n, inf);
            K2 = {D_n : n in N}, D_n = {1} u [n, inf).
K1 is countably compact: every subfamily's intersection contains 0.
K2 likewise via 1.  The union contains {C_n} u {D_n}, which has the FIP
(any finite subfamily contains a common tail), yet its TOTAL intersection is
({0} n {1}) = empty, since every k >= 2 escapes C_{k+1}.

The empty total intersection is a limit statement; this script verifies the
finite bookkeeping in a window [0, N)."""
N = 200
checks = 0


def ck(b, msg):
    global checks
    checks += 1
    assert b, msg


C = [frozenset({0}) | frozenset(range(n, N)) for n in range(N)]
D = [frozenset({1}) | frozenset(range(n, N)) for n in range(N)]

# each class pointed (hence countably compact): 0 resp. 1 in every member
for n in range(N):
    ck(0 in C[n], 'K1 pointed at 0')
    ck(1 in D[n], 'K2 pointed at 1')

# FIP of the mixed family, windowed: every initial segment intersects
acc = frozenset(range(N))
for n in range(N):
    acc = acc & C[n] & D[n]
    ck(acc != frozenset(), 'mixed family has the FIP at each stage')

# total windowed intersection = {0} n {1} u {N-1} (the window artifact);
# every FIXED k in 2..N-2 has escaped, witnessing emptiness in the limit
ck(acc == frozenset({N - 1}), 'window artifact only: the top point')
for k in range(2, N - 1):
    ck(k not in C[k + 1], f'{k} escapes C_(k+1): total intersection misses it')
ck(0 not in frozenset.intersection(*D), '0 not in cap K2-part')
ck(1 not in frozenset.intersection(*C), '1 not in cap K1-part')

print(f'PASS check_c11_truncation: {checks} checks '
      f'(limit step is hand-proof-only)')
