# Batched version of check5a.py (iii) for larger grids: are all M = co-D¹∖D¹ sets positive cyclic-order sets
# for some interleaving of the labelled values?  Usage: python3 check5a_cyc.py n0 n1 n2
import sys, itertools, numpy as np
exec(open('check5a.py').read().split("# (ii') is N1")[0])
labels = [(i, v) for i in range(3) for v in range(n[i])]; L = len(labels)
P = np.array(pts); off = [0, n[0], n[0] + n[1]]
cols = [P[:, 0] + off[0], P[:, 1] + off[1], P[:, 2] + off[2]]
w = (np.uint64(1) << np.arange(N, dtype=np.uint64))
cyc = set(); it = itertools.permutations(range(L)); B = 200000
while True:
    chunk = list(itertools.islice(it, B))
    if not chunk: break
    R = np.array(chunk, dtype=np.int8)
    a, b, c = R[:, cols[0]], R[:, cols[1]], R[:, cols[2]]
    pos = ((a < b) & (b < c)) | ((b < c) & (c < a)) | ((c < a) & (a < b))
    cyc.update((pos.astype(np.uint64) * w).sum(axis=1).tolist())
print('(iii) distinct cyclic-order sets', len(cyc), ' M ⊆ cyc:', M <= cyc, ' |M ∩ cyc|', len(M & cyc),
      ' cyc ∩ N1', len(cyc & N1), ' cyc outside N1 ∪ M', len(cyc - N1 - M), flush=True)
