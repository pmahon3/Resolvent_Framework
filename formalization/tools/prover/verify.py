"""Splice a candidate proof into its source file and re-elaborate with Lean.

Success requires exit 0, no `error:`, and no `uses 'sorry'` warning -- the last is
essential because `sorry` elaborates cleanly and would otherwise score as a pass.
"""
import os, re, subprocess, tempfile, json

PROJ = r"C:\Users\pmahon\Research\Mathematics\Resolvent_Framework\formalization\QuerySystem"

def _machine_path():
    p = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         '[System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + '
         '[System.Environment]::GetEnvironmentVariable("Path","User")'],
        capture_output=True, text=True, timeout=60)
    return p.stdout.strip() if p.returncode == 0 and p.stdout.strip() else os.environ.get("PATH", "")


ENV = dict(os.environ, PATH=_machine_path())

# Windows CreateProcess resolves the exe against the CALLING process's PATH,
# not env=, so `lake` must be an absolute path.
LAKE = next((os.path.join(d, "lake.exe") for d in ENV["PATH"].split(os.pathsep)
             if d and os.path.isfile(os.path.join(d, "lake.exe"))), "lake")

FENCE = re.compile(r"^\s*```(?:lean4?)?\s*|\s*```\s*$", re.M)

# Mathlib *search* tactics. These close goals by brute-force library search, so a
# candidate containing one measures Mathlib's reach, not the model's. Banned from
# model candidates; allowed only when deliberately measuring the null baseline.
SEARCH = re.compile(r"(?<![\w'])(exact\?|apply\?|rw\?|simp\?|aesop\?|hint|library_search|"
                    r"exact_mod_cast\?|polyrith)(?![\w'])")


def clean(candidate: str) -> str:
    c = FENCE.sub("", candidate).strip()
    # models often re-emit the signature; keep only the proof body if so
    return c


def verify(case, candidate, timeout=180, allow_search=False):
    """Return (ok, reason, stdout+stderr)."""
    src = open(case["path"], encoding="utf-8", errors="replace").read()
    body = clean(candidate)
    if not body:
        return False, "empty", ""
    if re.search(r"(?<![\w'.])sorry(?![\w'])", body):
        return False, "contains-sorry", ""
    if not allow_search and SEARCH.search(body):
        return False, "search-tactic", ""

    spliced = src[:case["proof_start"]] + " " + body + "\n" + src[case["decl_end"]:]

    d = os.path.join(PROJ, "_eval")
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(suffix=".lean", dir=d, text=True)
    os.close(fd)
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(spliced)
        try:
            p = subprocess.run([LAKE, "env", "lean", tmp],
                               cwd=PROJ, env=ENV, capture_output=True,
                               text=True, encoding="utf-8", errors="replace",
                               timeout=timeout)
        except subprocess.TimeoutExpired:
            return False, "timeout", ""
        out = (p.stdout or "") + (p.stderr or "")
        if "uses 'sorry'" in out or "declaration uses" in out:
            return False, "sorry-warning", out
        if p.returncode != 0:
            return False, "lean-error", out
        if re.search(r"^\S*\.lean:\d+:\d+: error", out, re.M) or "error:" in out:
            return False, "lean-error", out
        return True, "ok", out
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass


if __name__ == "__main__":
    import sys, time
    HERE = os.path.dirname(os.path.abspath(__file__))
    cases = json.load(open(os.path.join(HERE, "evalset.json"), encoding="utf-8"))
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4

    # smoke tests: shortest proofs, so failures are the harness not the maths
    sample = sorted(cases, key=lambda c: c["proof_chars"])[:n]

    print("=" * 84)
    print("HARNESS SELF-TEST  (ground truth must PASS; sorry and garbage must FAIL)")
    print("=" * 84)
    GARBAGE = "by exact absolutely_no_such_lemma_xyz"
    good = bad_s = bad_g = null_solved = 0
    for c in sample:
        t0 = time.time()
        ok1, r1, o1 = verify(c, c["proof"])
        t1 = time.time() - t0
        ok2, r2, _ = verify(c, "sorry")
        ok3, r3, _ = verify(c, GARBAGE)
        # null baseline: can Mathlib's own search close it with no model at all?
        ok4, r4, _ = verify(c, "by exact?", allow_search=True)
        good += ok1
        bad_s += (not ok2)
        bad_g += (not ok3)
        null_solved += ok4
        print(f"\n  {c['file'][:30]:<30} {c['name'][:28]:<28}")
        print(f"    original     : {'PASS' if ok1 else 'FAIL'}  ({r1})  {t1:5.1f}s")
        print(f"    sorry        : {'PASS' if ok2 else 'FAIL'}  ({r2})   <- want FAIL")
        print(f"    garbage      : {'PASS' if ok3 else 'FAIL'}  ({r3})   <- want FAIL")
        print(f"    exact? (null): {'PASS' if ok4 else 'FAIL'}  ({r4})   <- baseline, not a gate")
        if not ok1:
            print("    --- lean output ---")
            for ln in (o1 or "").splitlines()[:12]:
                print("      " + ln)

    n = len(sample)
    trust = (good == n and bad_s == n and bad_g == n)
    print("\n" + "=" * 84)
    print(f"  ground-truth passed : {good}/{n}")
    print(f"  sorry rejected      : {bad_s}/{n}")
    print(f"  garbage rejected    : {bad_g}/{n}")
    print(f"  null baseline solved: {null_solved}/{n}  (Mathlib search alone -- "
          f"a model must beat this)")
    print("  HARNESS %s" % ("TRUSTWORTHY" if trust
                            else "NOT TRUSTWORTHY - do not run evals yet"))
