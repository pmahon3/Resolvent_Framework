"""Best-first proof search: BFS-Prover proposes tactics, the Lean REPL applies them.

The REPL speaks newline-delimited JSON terminated by a blank line:
    {"cmd": "...", "env": 0}         -> {"sorries":[{"proofState":N,"goal":"..."}], "env":M}
    {"tactic": "...", "proofState":N} -> {"proofState":M, "goals":[...]}
A state with an empty `goals` list is a closed proof.
"""
import os, json, heapq, subprocess, time, urllib.request, itertools, threading, queue

PROJ = r"C:\Users\pmahon\Research\Mathematics\Resolvent_Framework\formalization\QuerySystem"
REPL = r"C:\Users\pmahon\Research\Mathematics\repl\.lake\build\bin\repl.exe"
# Endpoint is configurable so a second instance can be driven on another GPU:
#   CUDA_VISIBLE_DEVICES=1 OLLAMA_HOST=127.0.0.1:11435 ollama serve
#   OLLAMA_URL=http://127.0.0.1:11435/api/generate python grind.py ...
OLLAMA = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")


from verify import ENV, LAKE, case_path  # resolved lake + machine PATH + per-machine paths


class ReplTimeout(Exception):
    pass


class Repl:
    """One REPL process, launched inside the project's `lake env` so imports resolve.

    stderr goes to DEVNULL: the project enables mathlib's linter set, so the REPL
    emits enough diagnostic noise to fill a 64K pipe buffer, after which the child
    blocks on write and any blocking read here deadlocks. Real errors come back as
    JSON on stdout, so nothing is lost. stdout is drained by a reader thread so a
    wedged REPL surfaces as a timeout instead of hanging forever.
    """

    def __init__(self, timeout=180):
        self.timeout = timeout
        self.p = subprocess.Popen(
            [LAKE, "env", REPL], cwd=PROJ, env=ENV,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            text=True, encoding="utf-8", errors="replace", bufsize=1)
        self.q = queue.Queue()
        self.t = threading.Thread(target=self._pump, daemon=True)
        self.t.start()

    def _pump(self):
        try:
            for line in self.p.stdout:
                self.q.put(line)
        except Exception:
            pass
        finally:
            self.q.put(None)          # EOF sentinel

    def send(self, obj, timeout=None):
        deadline = time.time() + (timeout or self.timeout)
        self.p.stdin.write(json.dumps(obj) + "\n\n")
        self.p.stdin.flush()
        buf = []
        while True:
            remaining = deadline - time.time()
            if remaining <= 0:
                raise ReplTimeout(f"no reply in {timeout or self.timeout}s")
            try:
                line = self.q.get(timeout=min(remaining, 5.0))
            except queue.Empty:
                continue
            if line is None:
                raise RuntimeError("repl exited")
            if line.strip() == "" and buf:
                break
            if line.strip():
                buf.append(line)
        return json.loads("".join(buf))

    def close(self):
        try:
            self.p.stdin.close()
        except Exception:
            pass
        try:
            self.p.terminate()
            self.p.wait(timeout=10)
        except Exception:
            try:
                self.p.kill()
            except Exception:
                pass


# Mathlib's own automation, with no model involved. This is the bar a prover must
# clear: a goal these close is not evidence about the model.
BASELINE_TACTICS = ["exact?", "aesop", "simp_all", "decide", "omega", "tauto",
                    "norm_num", "rfl", "trivial", "assumption", "simp", "positivity"]


def tactics(model, goal, k, temperature=0.8, num_predict=64):
    """Sample k candidate tactics for a goal state."""
    if model == "__baseline__":
        return list(BASELINE_TACTICS)
    out, seen = [], set()
    for i in range(k):
        body = {"model": model, "prompt": f"{goal}:::", "raw": True, "stream": False,
                "options": {"temperature": 0.0 if i == 0 else temperature,
                            "num_predict": num_predict, "seed": i}}
        req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                t = json.loads(r.read()).get("response", "").strip()
        except Exception:
            continue
        t = t.split("\n")[0].strip()
        if t and t not in seen and "sorry" not in t:
            seen.add(t); out.append(t)
    return out


def file_envs(repl, path, cases_sorted):
    """Yield (case, env_id) replaying the file in chunks.

    The environment handed to each case contains everything strictly *before* its
    declaration -- so the constants it mentions are committed to the kernel, while
    its own proof (and every later one) is absent and cannot be cited.
    """
    src = open(path, encoding="utf-8", errors="replace").read()
    env, pos = None, 0
    for c in cases_sorted:
        chunk = src[pos:c["decl_start"]]
        if chunk.strip() or env is None:
            msg = {"cmd": chunk} if env is None else {"cmd": chunk, "env": env}
            out = repl.send(msg)
            env = out.get("env", env)
        yield c, env
        pos = c["decl_start"]          # next chunk re-includes this real declaration


def search(repl, case, env, model, max_expansions=40, k=8, verbose=True):
    """Return (proof_tactics or None, stats)."""
    t0 = time.time()
    stmt = case["sig"].rstrip()
    stmt = stmt[:-2].rstrip() if stmt.endswith(":=") else stmt
    r = repl.send({"cmd": f"{stmt} := by sorry", "env": env})
    sor = r.get("sorries") or []
    if not sor:
        errs = [m for m in (r.get("messages") or []) if m.get("severity") == "error"]
        return None, {"reason": "no-initial-goal", "expansions": 0,
                      "secs": round(time.time() - t0, 1),
                      "raw": (str(errs[0].get("data"))[:200] if errs else str(r)[:200])}
    pick = sor[0]
    root, goal0 = pick["proofState"], pick["goal"]
    return search_from(repl, root, goal0, model, max_expansions, k, verbose, t0)


def search_from(repl, root, goal0, model, max_expansions=40, k=8, verbose=True, t0=None, extra=None):
    """Best-first search from an existing proofState. Split out of `search` so
    `grind.py` can drive it on the sorries the REPL reports for a whole file,
    rather than on a reconstructed statement. One implementation, no copy."""
    if t0 is None:
        t0 = time.time()
    ctr = itertools.count()
    pq = [(0, next(ctr), root, goal0, [])]
    seen, exp = {goal0}, 0

    while pq and exp < max_expansions:
        depth, _, ps, goal, path = heapq.heappop(pq)
        exp += 1
        for t in (tactics(model, goal, k) + (extra or [])):
            try:
                rr = repl.send({"tactic": t, "proofState": ps})
            except Exception:
                continue
            if "message" in rr:
                continue
            if any(m.get("severity") == "error" for m in (rr.get("messages") or [])):
                continue
            # a kernel failure can still report `goals: []`; never treat that as closed
            if str(rr.get("proofStatus", "")).startswith("Error"):
                continue
            if "proofState" not in rr:
                continue
            gs = rr.get("goals", [])
            newpath = path + [t]
            if not gs:
                if verbose:
                    print(f"      CLOSED after {exp} expansions: {' ; '.join(newpath)}")
                return newpath, {"reason": "closed", "expansions": exp,
                                 "secs": round(time.time() - t0, 1)}
            g = "\n".join(gs)
            if g in seen:
                continue
            seen.add(g)
            heapq.heappush(pq, (depth + 1 + len(gs), next(ctr),
                                rr["proofState"], g, newpath))
    return None, {"reason": "exhausted" if not pq else "budget",
                  "expansions": exp, "secs": round(time.time() - t0, 1)}


if __name__ == "__main__":
    import argparse, sys

    # Goals and tactics contain Lean's Unicode (⊢, ᭺, ∀). When stdout is a
    # pipe or a file, Python picks the locale encoding -- cp1252 on Windows --
    # and the first `print` of a tactic raises UnicodeEncodeError from *inside*
    # `search`, which the case loop then records as `err:UnicodeEncodeError`.
    # A case that had already closed its proof is scored as a failure that way,
    # so this is not cosmetic: it silently loses solved cases on one platform.
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="bfs-prover:7b-q4")
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--k", type=int, default=8)
    ap.add_argument("--budget", type=int, default=40)
    ap.add_argument("--max-lines", type=int, default=12)
    ap.add_argument("--evalset", default="evalset.json",
                    help="eval set to run against (default: the full corpus)")
    # Splitting one matched run across two GPUs. The pool is selected FIRST and
    # sliced after, so every case sees the same env it would see in the whole
    # run -- `file_envs` rebuilds each case's environment from the source before
    # its own declaration, not from the cases that preceded it. A shard is a
    # scheduling device, not a different experiment.
    ap.add_argument("--shard", default=None, metavar="I/M",
                    help="run only shard I of M (0-based) of the selected pool")
    ap.add_argument("--out", default=None,
                    help="results file (default res_bfs.json; set per shard so "
                         "concurrent runs do not clobber each other)")
    a = ap.parse_args()

    HERE = os.path.dirname(os.path.abspath(__file__))
    cases = json.load(open(os.path.join(HERE, a.evalset), encoding="utf-8"))
    BROKEN = {"PredictiveState.lean", "PredictiveOperators.lean"}  # do not compile
    pool = sorted([c for c in cases
                   if c["proof_lines"] <= a.max_lines and c["file"] not in BROKEN],
                  key=lambda c: (c["proof_chars"], c["name"]))[:a.n]

    shard = ""
    if a.shard:
        i, m = (int(x) for x in a.shard.split("/"))
        n = len(pool)
        pool = pool[n * i // m : n * (i + 1) // m]
        shard = f"  shard={i}/{m}"

    print("=" * 92)
    print(f"BFS SEARCH  model={a.model}  cases={len(pool)}  k={a.k}  budget={a.budget}{shard}")
    print("=" * 92)

    byfile = {}
    for c in pool:
        byfile.setdefault(case_path(c), []).append(c)

    solved, rows, i = 0, [], 0
    for path, cs in byfile.items():
        cs.sort(key=lambda c: c["decl_start"])
        repl = Repl()
        try:
            for c, env in file_envs(repl, path, cs):
                i += 1
                print(f"  [{i:>3}/{len(pool)}] {c['file'][:24]:<24} "
                      f"{c['name'][:30]:<30}", flush=True)
                try:
                    proof, st = search(repl, c, env, a.model, a.budget, a.k)
                except ReplTimeout:
                    proof, st = None, {"reason": "repl-timeout", "expansions": 0,
                                       "secs": 0}
                    repl.close(); repl = Repl()   # poisoned; start clean
                except Exception as e:
                    proof, st = None, {"reason": f"err:{type(e).__name__}",
                                       "expansions": 0, "secs": 0}
                solved += bool(proof)
                rows.append({"file": c["file"], "name": c["name"], "ok": bool(proof),
                             "proof": " ; ".join(proof) if proof else None, **st})
                extra = f"  {st.get('raw','')[:70]}" if st["reason"] == "no-initial-goal" else ""
                print(f"        -> {'PASS' if proof else 'fail'}  {st['reason']}  "
                      f"exp={st['expansions']}  {st['secs']}s{extra}", flush=True)
        except Exception as e:
            print(f"        !! file aborted: {type(e).__name__}: {str(e)[:90]}", flush=True)
        finally:
            repl.close()

    print("\n" + "=" * 92)
    print(f"  solved {solved}/{len(pool)} = {100.0*solved/max(len(pool),1):.1f}%")
    json.dump(rows, open(os.path.join(HERE, a.out or "res_bfs.json"), "w"), indent=1)
