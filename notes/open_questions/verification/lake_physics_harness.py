#!/usr/bin/env python3
"""Pre-registered lake physics harness (notes/open_questions/views_across_records/LAKE_PHYSICS_HARNESS.md).
Reuses lake_harness.py with a different loader. Groups: wtemp, o2, o2sat at 1 m (else shallowest depth <= 1 m).
Flags not used (the pre-registration did not mention them). Usage: python3 -I lake_physics_harness.py <ntl29_v15.csv>"""
import csv, sys, collections, importlib.util
from pathlib import Path
import numpy as np
sp = importlib.util.spec_from_file_location("h", Path(__file__).with_name("lake_harness.py"))
h = importlib.util.module_from_spec(sp); sp.loader.exec_module(h)
VARS = ["wtemp", "o2", "o2sat"]


def load(path):
    rows = collections.defaultdict(list)                 # (lake,date) -> [(depth, vals)]
    for r in csv.DictReader(open(path)):
        if r["lakeid"] not in h.LAKES or r["depth"] == "": continue
        d = float(r["depth"])
        if d > 1: continue
        try: v = [float(r[k]) for k in VARS]
        except ValueError: continue
        rows[(r["lakeid"], r["sampledate"])].append((d, v))
    data = {lk: [] for lk in h.LAKES}
    for (lk, dt), lst in sorted(rows.items()):
        at1 = [v for d, v in lst if d == 1]
        if not at1:
            m = min(d for d, _ in lst); at1 = [v for d, v in lst if d == m]
        data[lk].append((int(dt[:4]), list(np.mean(at1, axis=0))))
    return data


if __name__ == "__main__":
    h.load = load
    h.main(sys.argv[1])
