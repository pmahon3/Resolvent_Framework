# Inspect M-sets on 3x4x4 that are not positive cyclic-order sets of a strict interleaving.
import sys, itertools, numpy as np
from collections import Counter
sys.argv = ['x', '3', '4', '4']
exec(open('check5a_cyc.py').read().split("print('(iii)")[0])
odd = sorted(M - cyc)
print('odd', len(odd), Counter(bin(m).count('1') for m in odd))
for m in odd[:2]:
    S = [p for p in pts if m >> idx[p] & 1]
    print(len(S), S)
# tie-allowing generalised cyclic sets: sigma_i : X_i -> {0..V-1}, conventions R in {<,<=}^3, 'exactly two'
rng = np.random.default_rng(0); found = Counter(); gen = set()
ops = [np.less, np.less_equal]
for trial in range(400):
    V = rng.integers(2, 12)
    R = rng.integers(0, V, size=(20000, L)).astype(np.int8)
    a, b, c = R[:, cols[0]], R[:, cols[1]], R[:, cols[2]]
    for conv in itertools.product(range(2), repeat=3):
        t = ops[conv[0]](a, b).astype(np.int8) + ops[conv[1]](b, c) + ops[conv[2]](c, a)
        gen.update(((t == 2).astype(np.uint64) * w).sum(axis=1).tolist())
oddset = set(odd)
print('generalised (ties, 8 conventions) sets sampled', len(gen), ' odd covered', len(oddset & gen), 'of', len(oddset),
      ' sampled sets outside D3', len(gen - N1 - M))
