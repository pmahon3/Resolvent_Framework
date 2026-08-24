"""Run a model against the retrodiction eval set and score with the Lean verifier.

Two modes:
  chat  (default) -- whole-proof generation, works with any instruct model
  raw   (--raw)   -- BFS-Prover's native `{state}:::` completion format
"""
import os, re, json, time, argparse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OLLAMA = "http://127.0.0.1:11434/api/generate"

SYS = """You are a Lean 4 (Mathlib, v4.29) proof engine.
Given a theorem signature, output ONLY the proof body that follows `:=`.
No markdown fences, no restatement of the signature, no commentary.
Never use `sorry`. Prefer short tactic proofs."""


def header_of(path, limit=60):
    """Imports / opens / variables / set_options -- the ambient context."""
    keep = []
    for ln in open(path, encoding="utf-8", errors="replace").read().splitlines():
        s = ln.strip()
        if s.startswith(("import ", "open ", "variable", "universe", "set_option",
                         "namespace ", "noncomputable section", "section")):
            keep.append(ln)
        if len(keep) >= limit:
            break
    return "\n".join(keep)


def call(model, prompt, temperature, raw=False, num_predict=512, timeout=300):
    body = {"model": model, "prompt": prompt, "stream": False,
            "options": {"temperature": temperature, "num_predict": num_predict}}
    if raw:
        body["raw"] = True
    else:
        body["system"] = SYS
    req = urllib.request.Request(
        OLLAMA, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read())
    return d.get("response", ""), d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--n", type=int, default=20, help="number of cases")
    ap.add_argument("--k", type=int, default=1, help="samples per case (pass@k)")
    ap.add_argument("--temp", type=float, default=0.0)
    ap.add_argument("--raw", action="store_true")
    ap.add_argument("--max-lines", type=int, default=12,
                    help="only cases whose reference proof is at most this many lines")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    import verify as V

    cases = json.load(open(os.path.join(HERE, "evalset.json"), encoding="utf-8"))
    pool = [c for c in cases if c["proof_lines"] <= a.max_lines]
    pool.sort(key=lambda c: (c["proof_chars"], c["name"]))
    sel = pool[:a.n]

    print("=" * 90)
    print(f"MODEL {a.model}   cases={len(sel)}  k={a.k}  temp={a.temp}  "
          f"raw={a.raw}  max_lines={a.max_lines}")
    print("=" * 90)

    results, solved, t_start = [], 0, time.time()
    for i, c in enumerate(sel, 1):
        hdr = header_of(c["path"])
        got, reason, cand_kept = False, "", ""
        t0 = time.time()
        for j in range(a.k):
            sig = c["sig"].rstrip()
            sig = sig[:-2].rstrip() if sig.endswith(":=") else sig
            if a.raw:
                prompt = f"{sig}:::"
            else:
                prompt = (f"-- file context --\n{hdr}\n\n"
                          f"-- prove this --\n{sig} :=\n")
            try:
                resp, _ = call(a.model, prompt,
                               a.temp if j == 0 else max(a.temp, 0.7), raw=a.raw)
            except Exception as e:
                reason = f"model-error:{type(e).__name__}"
                continue
            ok, why, _out = V.verify(c, resp)
            if ok:
                got, reason, cand_kept = True, "ok", V.clean(resp)
                break
            reason = why
        dt = time.time() - t0
        solved += got
        results.append({"file": c["file"], "name": c["name"], "ok": got,
                        "reason": reason, "ref_lines": c["proof_lines"],
                        "secs": round(dt, 1), "candidate": cand_kept})
        mark = "PASS" if got else "fail"
        print(f"  [{i:>3}/{len(sel)}] {mark}  {c['file'][:26]:<26} "
              f"{c['name'][:30]:<30} ref={c['proof_lines']:>2}L {dt:5.1f}s  {reason}")

    el = time.time() - t_start
    print("\n" + "=" * 90)
    print(f"  pass@{a.k}: {solved}/{len(sel)} = {100.0*solved/max(len(sel),1):.1f}%"
          f"   wall {el/60:.1f} min   {el/max(len(sel),1):.1f}s/case")
    from collections import Counter
    for r, n in Counter(x["reason"] for x in results if not x["ok"]).most_common():
        print(f"    fail: {r:<22} {n}")

    out = a.out or os.path.join(
        HERE, f"res_{re.sub(r'[^A-Za-z0-9]+','_',a.model)}_k{a.k}.json")
    json.dump({"model": a.model, "k": a.k, "temp": a.temp, "raw": a.raw,
               "n": len(sel), "solved": solved, "results": results},
              open(out, "w", encoding="utf-8"), indent=1)
    print(f"  wrote {out}")


if __name__ == "__main__":
    main()
