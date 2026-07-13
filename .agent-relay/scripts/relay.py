#!/usr/bin/env python3.11
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, re, shutil, subprocess, sys
try:
    import tomllib
except ModuleNotFoundError:  # Permit `doctor` to explain an older system Python.
    tomllib = None
from pathlib import Path
HERE=Path(__file__).resolve().parent; RELAY=HERE.parent; REPO=RELAY.parent
sys.path.insert(0,str(HERE))
import backends, git_ops, packet_builder, validation

def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def load_json(p): return json.loads(Path(p).read_text())
def write_json(p,d): Path(p).write_text(json.dumps(d,indent=2)+"\n")
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def config():
    p=RELAY/"config.toml" if (RELAY/"config.toml").exists() else RELAY/"config.example.toml"
    if tomllib:
        with p.open("rb") as f:return tomllib.load(f)
    values={}
    for raw in p.read_text().splitlines():
        line=raw.split("#",1)[0].strip()
        if not line or "=" not in line: continue
        key,value=(x.strip() for x in line.split("=",1))
        if value.startswith('"') and value.endswith('"'): values[key]=value[1:-1]
        elif value in ("true","false"): values[key]=value=="true"
        else:
            try: values[key]=int(value)
            except ValueError: values[key]=value
    return values
def current(): return load_json(RELAY/"CURRENT.json")
def save_current(c): c["updated_at"]=now(); write_json(RELAY/"CURRENT.json",c)
def run_dir(c):
    if not c.get("last_run_id"): raise RuntimeError("no active run")
    return REPO/config()["run_root"]/c["last_run_id"]
def ensure_initialized(c):
    if c["status"]=="uninitialized": raise RuntimeError("run init first")
def unique_run_id(c):
    rid=f"run-{c['iteration']+1:04d}"
    if any(json.loads(x)["run_id"]==rid for x in (RELAY/"LEDGER.jsonl").read_text().splitlines() if x.strip()): raise RuntimeError("repeated run ID")
    if (REPO/config()["run_root"]/rid).exists(): raise RuntimeError("run directory already exists")
    return rid

def doctor(_):
    failures=[]
    def check(label,ok,detail=""):
        print(f"{'PASS' if ok else 'FAIL'} {label}{(': '+detail) if detail else ''}");
        if not ok: failures.append(label)
    check("repository root",git_ops.root(REPO)==REPO)
    check("accepted worktree clean",not git_ops.porcelain(REPO))
    check("Python >= 3.11",sys.version_info >= (3,11))
    check("Git installed",shutil.which("git") is not None)
    check("Codex installed",shutil.which("codex") is not None)
    login=subprocess.run(["codex","login","status"],cwd=REPO,capture_output=True,text=True) if shutil.which("codex") else None
    check("Codex authenticated",bool(login and login.returncode==0))
    lake=shutil.which("lake") or str(Path.home()/".elan/bin/lake")
    check("lake available",Path(lake).is_file(),"required for Lean changes")
    for p in (RELAY/"schemas").glob("*.json"):
        try: json.loads(p.read_text()); ok=True
        except Exception: ok=False
        check(f"schema parses {p.name}",ok)
    tracked=subprocess.run(["git","ls-files",".agent-relay-local"],cwd=REPO,text=True,capture_output=True).stdout.strip()
    check("transient directory untracked",not tracked)
    relay_text="".join(p.read_text(errors="ignore") for p in RELAY.rglob("*") if p.is_file())
    check("no obvious committed API key",re.search(r"sk-(?:proj|live)-[A-Za-z0-9_-]{20,}",relay_text) is None)
    cfg=config()
    if cfg["review_backend"]=="openai":
        try: import openai; package=True
        except ImportError: package=False
        check("OpenAI package",package); check("OPENAI_API_KEY set",bool(os.environ.get("OPENAI_API_KEY")))
    return 1 if failures else 0

def init(args):
    c=current()
    if c["status"]!="uninitialized" and not args.force: raise RuntimeError("relay already initialized; use --force")
    dirty=git_ops.porcelain(REPO,ignore_relay_setup=True)
    if dirty: raise RuntimeError("refusing initialization: non-relay worktree changes exist")
    c.update(branch=git_ops.branch(REPO),accepted_commit=git_ops.head(REPO),iteration=0,status="initialized",review_backend=config()["review_backend"])
    save_current(c)
    text=(RELAY/"STATE.md").read_text().replace("Populated by `relay.py init`.",c["accepted_commit"])
    (RELAY/"STATE.md").write_text(text)
    print(f"initialized at {c['accepted_commit']} on {c['branch']}; no model launched")

def status(_):
    c=current(); rd=(REPO/config()["run_root"]/c["last_run_id"]) if c.get("last_run_id") else None
    print(json.dumps({**c,"active_run_dir":str(rd) if rd and rd.exists() else None,
      "pending_handoff":(RELAY/"HANDOFF.md").exists(),"human_action_required":c["status"]=="awaiting_human"},indent=2))

def import_handoff(args):
    text=sys.stdin.read() if args.file=="-" else Path(args.file).read_text()
    if not text.strip(): raise RuntimeError("handoff is empty")
    packet_builder.reject_secrets(text); (RELAY/"HANDOFF.md").write_text(text.rstrip()+"\n"); print("handoff imported")

def prepare(_):
    c=current(); ensure_initialized(c); git_ops.ensure_clean(REPO); rid=unique_run_id(c); cfg=config(); rd=REPO/cfg["run_root"]/rid; wt=REPO/cfg["worktree_root"]/rid
    rd.mkdir(parents=True); git_ops.create_worktree(REPO,wt,f"relay/{rid}",c["accepted_commit"])
    # Relay files may be initialized but not yet committed during setup; real runs require them in the accepted commit.
    if not (wt/".agent-relay").exists(): raise RuntimeError("relay files must be committed before a real run")
    meta={"run_id":rid,"iteration":c["iteration"]+1,"started_at":now(),"accepted_parent_commit":c["accepted_commit"],"worktree":str(wt),"branch":f"relay/{rid}","handoff_sha256":sha(RELAY/"HANDOFF.md"),"state_sha256_before":sha(RELAY/"STATE.md")}
    write_json(rd/"META.json",meta); (rd/"EXECUTOR_PACKET.md").write_text(packet_builder.executor_packet(RELAY,rid)); c.update(last_run_id=rid,status="prepared"); save_current(c); print(rid)

def execute(_):
    c=current(); rd=run_dir(c); meta=load_json(rd/"META.json"); cfg=config(); out=rd/"RESULT.json"
    cmd=backends.codex_command(cwd=Path(meta["worktree"]),schema=RELAY/"schemas/executor-result.schema.json",output=out,sandbox=cfg["executor_sandbox"],model=cfg["executor_model"])
    backends.run_codex((rd/"EXECUTOR_PACKET.md").read_text(),cmd,rd/"executor-events.jsonl")
    result=load_json(out); meta["executor_commit"]=(result.get("commits") or [git_ops.head(Path(meta["worktree"]))])[-1]; write_json(rd/"META.json",meta); c.update(status="executed",last_outcome=result["outcome"]); save_current(c)

def validate(_):
    c=current(); rd=run_dir(c); meta=load_json(rd/"META.json"); commit=meta.get("executor_commit") or git_ops.head(Path(meta["worktree"])); meta["executor_commit"]=commit; write_json(rd/"META.json",meta)
    data=validation.run_all(Path(meta["worktree"]),meta["accepted_parent_commit"],commit,rd,config()); c["status"]="validated"; save_current(c); print(data["status"])

def review(_):
    c=current(); rd=run_dir(c); meta=load_json(rd/"META.json"); cfg=config(); wt=Path(meta["worktree"]); result=load_json(rd/"RESULT.json"); val=load_json(rd/"VALIDATION.json")
    stat=git_ops.run(["git","diff","--stat",f"{meta['accepted_parent_commit']}..{meta['executor_commit']}"],wt).stdout
    diff=git_ops.run(["git","diff",f"{meta['accepted_parent_commit']}..{meta['executor_commit']}"],wt).stdout
    packet=packet_builder.review_packet(RELAY,result,meta["accepted_parent_commit"],meta["executor_commit"],stat,diff,val,cfg["review_diff_limit_bytes"]); (rd/"REVIEW_PACKET.md").write_text(packet)
    if cfg["review_backend"]=="codex":
        cmd=backends.codex_command(cwd=None,schema=RELAY/"schemas/review.schema.json",output=rd/"REVIEW.json",sandbox=cfg["reviewer_sandbox"],model=cfg["reviewer_model"])
        backends.run_codex(packet,cmd,rd/"reviewer-events.jsonl")
    else: backends.run_openai_review(packet,load_json(RELAY/"schemas/review.schema.json"),rd/"REVIEW.json",cfg["reviewer_model"],cfg["api_retry_count"])
    c["status"]="awaiting_human"; save_current(c); summary(c)

def summary(c):
    rd=run_dir(c); r=load_json(rd/"RESULT.json"); v=load_json(rd/"VALIDATION.json"); q=load_json(rd/"REVIEW.json")
    print(f"Run: {c['last_run_id']}\nExecutor outcome: {r['outcome']}\nIndependent validations: {v['status']}\nReviewer verdict: {q['verdict']}\nMaterial scope corrections: {len([x for x in q['scope_corrections'] if x['severity']!='minor'])}\nProposed next task: {q['state_patch']['next_task']}\nCommands:\n  relay.py accept\n  relay.py reject")

def append_ledger(entry):
    existing=[json.loads(x) for x in (RELAY/"LEDGER.jsonl").read_text().splitlines() if x.strip()]
    if any(x["run_id"]==entry["run_id"] for x in existing): raise RuntimeError("ledger already contains run ID")
    with (RELAY/"LEDGER.jsonl").open("a") as f:f.write(json.dumps(entry,separators=(",",":"))+"\n")

def finish(decision):
    c=current(); rd=run_dir(c); meta=load_json(rd/"META.json"); res=load_json(rd/"RESULT.json"); rev=load_json(rd/"REVIEW.json"); val=load_json(rd/"VALIDATION.json"); wt=Path(meta["worktree"])
    git_ops.ensure_clean(wt); commit=meta["executor_commit"]
    if not git_ops.commit_exists(REPO,commit): raise RuntimeError("executor commit missing")
    if decision=="accept":
        if val["status"]!="pass": raise RuntimeError("cannot accept failed validations")
        git_ops.ensure_clean(REPO); git_ops.run(["git","merge","--ff-only",commit],REPO)
        patch=rev["state_patch"]; state=(RELAY/"STATE.md").read_text()+"\n## Accepted iteration additions\n"+"\n".join(f"- {x}" for x in patch["banked_results_add"]+patch["closed_architectures_add"])+f"\n\n## Current open gate\n\n{patch['open_gate']}\n\n## Formalization boundary\n\n{patch['formalization_boundary']}\n\n## Single best next strategic problem\n\n{patch['next_task']}\n"
        (RELAY/"STATE.md").write_text(state); (RELAY/"HANDOFF.md").write_text(rev["next_handoff"].rstrip()+"\n"); final=git_ops.head(REPO); c.update(accepted_commit=final,iteration=meta["iteration"],status="initialized",consecutive_rejections=0)
    else: final=None; c.update(iteration=meta["iteration"],status="initialized",consecutive_rejections=c["consecutive_rejections"]+1)
    entry={"run_id":meta["run_id"],"iteration":meta["iteration"],"started_at":meta["started_at"],"completed_at":now(),"accepted_parent_commit":meta["accepted_parent_commit"],"executor_commit":commit,"final_accepted_commit":final,"handoff_sha256":meta["handoff_sha256"],"state_sha256_before":meta["state_sha256_before"],"state_sha256_after":sha(RELAY/"STATE.md") if decision=="accept" else None,"executor_outcome":res["outcome"],"review_verdict":rev["verdict"],"validation_status":val["status"],"changed_files":val["changed_files"],"claims_accepted":rev["verified_claims"] if decision=="accept" else [],"claims_rejected":rev["unsupported_claims"],"next_task":rev["state_patch"]["next_task"],"executor_usage":{},"reviewer_usage":{},"human_decision":decision}
    append_ledger(entry); c["last_outcome"]=res["outcome"]; save_current(c); print(decision+"ed")
def accept(_): finish("accept")
def reject(_): finish("reject")
def cycle(_): prepare(None); execute(None); validate(None); review(None)
def run_cmd(args):
    for _ in range(args.max_iterations): cycle(None); break

def main():
    p=argparse.ArgumentParser(); sp=p.add_subparsers(dest="cmd",required=True)
    for name,fn in [("doctor",doctor),("status",status),("prepare",prepare),("execute",execute),("validate",validate),("review",review),("accept",accept),("reject",reject),("cycle",cycle)]: sp.add_parser(name).set_defaults(fn=fn)
    q=sp.add_parser("init");q.add_argument("--force",action="store_true");q.set_defaults(fn=init)
    q=sp.add_parser("import-handoff");q.add_argument("file");q.set_defaults(fn=import_handoff)
    q=sp.add_parser("run");q.add_argument("--max-iterations",type=int,default=1);q.set_defaults(fn=run_cmd)
    args=p.parse_args()
    try:return args.fn(args) or 0
    except Exception as e: print(f"ERROR: {e}",file=sys.stderr);return 1
if __name__=="__main__":raise SystemExit(main())
