"""C5 has no gap (A = 2). Is its odd-loop twist (every edge 'differ', each value evenly) hidden or visible?
Evaluate the twist's linear functional on every buildable set; if all >= 0 it is a hidden twist, and by the
Farkas lemma its witness must be a non-binary non-negative span element."""
import numpy as np
from gap_five_vertex import run
E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
D, V01, pts = run("C5", 5, E)
n = len(pts)
cells = np.array([[1.0 if (p[i] == a and p[j] == b) else 0.0 for p in pts] for (i, j) in E for a in (0, 1) for b in (0, 1)]).T
mu = np.array([0.5 if a != b else 0.0 for (i, j) in E for a in (0, 1) for b in (0, 1)])
vals = []
for m in D:
    f = np.array([(m >> t) & 1 for t in range(n)], float)
    c = np.linalg.lstsq(cells, f, rcond=None)[0]; assert np.allclose(cells @ c, f)
    vals.append(c @ mu)
print("min over buildable sets:", round(min(vals), 9))
s = np.array([sum(p[i] != p[j] for (i, j) in E) for p in pts], float)  # disagreements round the loop
g = 4 - s; c = np.linalg.lstsq(cells, g, rcond=None)[0]; assert np.allclose(cells @ c, g)
print("witness g = 4 - #disagreements: values", sorted(set(g)), " functional value", round(c @ mu, 9))
