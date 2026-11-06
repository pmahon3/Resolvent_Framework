#!/usr/bin/env python3
"""Re-run Poland V_G (validated) and reach sequence with the corrected detrend-then-rank pipeline."""
import sys, importlib.util
from pathlib import Path
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm); return mm
pv = mod("pv", "vg_poland_validated.py"); pv.ORDER = "detrend_then_rank"
sr = mod("sr", "source_reach_poland.py"); sr.pv.ORDER = "detrend_then_rank"
print("=== V_G validated test, prep2"); pv.main(sys.argv[1], sys.argv[2])
print("\n=== reach sequence, prep2"); sr.main(sys.argv[1], sys.argv[2])
