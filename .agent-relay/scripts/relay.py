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

STATUSES = {
    "uninitialized", "initialized", "prepared", "executed",
    "executor_uncommitted", "validated", "awaiting_human", "finalized",
}

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
def require_status(current_state, *allowed):
    status=current_state.get("status")
    if status not in STATUSES: raise RuntimeError(f"invalid relay status: {status}")
    if status not in allowed:
        raise RuntimeError(f"command requires status {', '.join(allowed)}; current status is {status}")

def ledger_entries():
    entries=[]; seen=set()
    for line_number, raw in enumerate((RELAY/"LEDGER.jsonl").read_text().splitlines(),1):
        if not raw.strip(): continue
        try: entry=json.loads(raw)
        except json.JSONDecodeError as exc: raise RuntimeError(f"ledger corruption at line {line_number}: {exc}") from exc
        run_id=entry.get("run_id")
        if not run_id: raise RuntimeError(f"ledger corruption at line {line_number}: missing run_id")
        if run_id in seen: raise RuntimeError(f"ledger corruption: duplicate rows for {run_id}")
        seen.add(run_id); entries.append(entry)
    return entries

def ledger_entry(run_id):
    return next((entry for entry in ledger_entries() if entry["run_id"]==run_id),None)

def finalized_entry(run_id):
    entry=ledger_entry(run_id)
    return entry if entry and entry.get("human_decision") in {"accept","reject"} else None

def require_not_finalized(run_id):
    entry=finalized_entry(run_id)
    if entry:
        raise RuntimeError(f"{run_id} is already finalized as {entry['human_decision']}; finalized runs are immutable")

def active_run_id(c):
    run_id=c.get("last_run_id")
    if not run_id: raise RuntimeError("no active run")
    return run_id

def run_dir(c):
    return REPO/config()["run_root"]/active_run_id(c)
def ensure_initialized(c):
    if c["status"]=="uninitialized": raise RuntimeError("run init first")

def ensure_only_control_state_dirty():
    allowed={".agent-relay/CURRENT.json"}
    dirty=git_ops.porcelain(REPO)
    unexpected=[]
    for line in dirty:
        path=line[3:].split(" -> ")[-1]
        if path not in allowed: unexpected.append(line)
    if unexpected: raise RuntimeError("accepted worktree has non-phase-state changes:\n"+"\n".join(unexpected))
def unique_run_id(c):
    rid=f"run-{c['iteration']+1:04d}"
    if ledger_entry(rid): raise RuntimeError("repeated run ID")
    if (REPO/config()["run_root"]/rid).exists(): raise RuntimeError("run directory already exists")
    return rid

def base_commit(meta):
    return meta.get("base_commit") or meta.get("accepted_parent_commit")

def require_executor_commit(c, meta):
    commit=meta.get("executor_commit")
    if not commit or commit==base_commit(meta) or not git_ops.commit_exists(Path(meta["worktree"]),commit):
        raise RuntimeError("executor commit missing; review cannot begin (use recover-commit for an executor_uncommitted run)")
    return commit

def executor_recovery_instructions(meta):
    return (f"Executor changes are preserved in {meta['worktree']}\n"
            "Recover after inspection with:\n"
            "  python3.11 .agent-relay/scripts/relay.py recover-commit\n"
            "Then continue with:\n"
            "  python3.11 .agent-relay/scripts/relay.py validate\n"
            "  python3.11 .agent-relay/scripts/relay.py review")

def doctor(_):
    failures=[]
    def check(label,ok,detail=""):
        print(f"{label}: {'PASS' if ok else 'FAIL'}{(' ('+detail+')') if detail else ''}");
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
    common=None
    try: common=git_ops.resolve_git_common_dir(REPO); common_ok=True
    except Exception as exc: common_ok=False; common_detail=str(exc)
    check("Git common directory resolved",common_ok,"" if common_ok else common_detail)
    probe_root=REPO/config()["worktree_root"]; probe=probe_root/"doctor-permission-probe"
    worktree_ok=command_ok=False
    if common_ok:
        try:
            if probe.exists(): raise RuntimeError(f"probe path already exists: {probe}")
            git_ops.run(["git","worktree","add","--detach",str(probe),"HEAD"],REPO)
            worktree_ok=os.access(probe,os.W_OK)
            git_ops.preflight_commit_permissions(probe,common)
            command_ok="--add-dir" in backends.codex_command(cwd=probe,schema=RELAY/"schemas/executor-result.schema.json",output=probe/"result.json",sandbox="workspace-write",add_dirs=[common])
        except subprocess.CalledProcessError as exc:
            common_detail=(exc.stderr or str(exc)).strip()
        except Exception as exc:
            common_detail=str(exc)
        finally:
            if probe.exists(): git_ops.run(["git","worktree","remove","--force",str(probe)],REPO,check=False)
    check("Executor worktree writable",worktree_ok)
    check("Git common directory writable through executor command",command_ok,"" if command_ok else common_detail)
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
    c.update(schema_version=2,branch=git_ops.branch(REPO),accepted_commit=git_ops.head(REPO),iteration=0,status="initialized",review_backend=config()["review_backend"])
    save_current(c)
    text=(RELAY/"STATE.md").read_text().replace("Populated by `relay.py init`.",c["accepted_commit"])
    (RELAY/"STATE.md").write_text(text)
    print(f"initialized at {c['accepted_commit']} on {c['branch']}; no model launched")

def status(_):
    c=current(); rd=(REPO/config()["run_root"]/c["last_run_id"]) if c.get("last_run_id") else None
    print(json.dumps({**c,"active_run_dir":str(rd) if rd and rd.exists() else None,
      "pending_handoff":(RELAY/"HANDOFF.md").exists(),"human_action_required":c["status"]=="awaiting_human"},indent=2))

def import_handoff(args):
    c=current()
    if c.get("last_run_id") and not finalized_entry(c["last_run_id"]):
        raise RuntimeError(f"cannot import a handoff while {c['last_run_id']} is active and unfinalized")
    require_status(c,"initialized")
    text=sys.stdin.read() if args.file=="-" else Path(args.file).read_text()
    if not text.strip(): raise RuntimeError("handoff is empty")
    packet_builder.reject_secrets(text); (RELAY/"HANDOFF.md").write_text(text.rstrip()+"\n"); print("handoff imported")

def prepare(args):
    c=current(); ensure_initialized(c); require_status(c,"initialized"); git_ops.ensure_clean(REPO); rid=unique_run_id(c); cfg=config(); rd=REPO/cfg["run_root"]/rid; wt=REPO/cfg["worktree_root"]/rid
    base=git_ops.head(REPO); rd.mkdir(parents=True); git_ops.create_worktree(REPO,wt,f"relay/{rid}",base)
    # Relay files may be initialized but not yet committed during setup; real runs require them in the accepted commit.
    if not (wt/".agent-relay").exists(): raise RuntimeError("relay files must be committed before a real run")
    meta={"run_id":rid,"iteration":c["iteration"]+1,"started_at":now(),"base_commit":base,"worktree":str(wt),"branch":f"relay/{rid}","handoff_sha256":sha(RELAY/"HANDOFF.md"),"state_sha256_before":sha(RELAY/"STATE.md")}
    packet=packet_builder.executor_packet(RELAY,rid); metrics=packet_builder.packet_metrics(packet,[RELAY/"prompts/executor.md",RELAY/"RUNBOOK.md",RELAY/"STATE.md",RELAY/"HANDOFF.md"])
    packet_builder.enforce_packet_limit(metrics,warning_tokens=cfg.get("packet_warning_tokens",100000),hard_tokens=cfg.get("packet_hard_limit_tokens",150000),allow_large=bool(getattr(args,"allow_large_packet",False)),label="executor")
    meta["executor_packet_metrics"]=metrics; write_json(rd/"META.json",meta); (rd/"EXECUTOR_PACKET.md").write_text(packet); c.update(last_run_id=rid,status="prepared"); save_current(c); print(rid)

def execute(_):
    c=current(); require_status(c,"prepared"); require_not_finalized(active_run_id(c)); rd=run_dir(c); meta=load_json(rd/"META.json"); cfg=config(); out=rd/"RESULT.json"
    wt=Path(meta["worktree"]); common=git_ops.resolve_git_common_dir(REPO)
    git_ops.preflight_commit_permissions(wt,common)
    cmd=backends.codex_command(cwd=wt,schema=RELAY/"schemas/executor-result.schema.json",output=out,sandbox=cfg["executor_sandbox"],model=cfg["executor_model"],add_dirs=[common])
    meta["executor_command"]=cmd; meta["git_common_dir"]=str(common); write_json(rd/"META.json",meta)
    error=None
    try: backends.run_codex((rd/"EXECUTOR_PACKET.md").read_text(),cmd,rd/"executor-events.jsonl")
    except Exception as exc: error=exc
    changed=git_ops.changed_paths(wt); head=git_ops.head(wt)
    result=load_json(out) if out.exists() else {}
    if changed and head==base_commit(meta):
        meta["reported_changed_files"]=changed; meta["executor_error"]=str(error) if error else "executor returned without a commit"
        write_json(rd/"META.json",meta); c.update(status="executor_uncommitted",last_outcome=result.get("outcome","FAILED")); save_current(c)
        print("Changed files:\n  "+"\n  ".join(changed)); print(executor_recovery_instructions(meta))
        raise RuntimeError("executor changed files but did not create a commit")
    if error: raise error
    commit=(result.get("commits") or [head])[-1]
    if commit==base_commit(meta): raise RuntimeError("executor did not create a commit")
    meta["executor_commit"]=commit; write_json(rd/"META.json",meta); c.update(status="executed",last_outcome=result["outcome"]); save_current(c)

def validate(_):
    c=current(); run_id=active_run_id(c); require_not_finalized(run_id)
    if c.get("status") in {"validated","awaiting_human"}:
        data=load_json(run_dir(c)/"VALIDATION.json"); print(data["status"]); return
    require_status(c,"executed"); rd=run_dir(c); meta=load_json(rd/"META.json"); commit=require_executor_commit(c,meta)
    data=validation.run_all(Path(meta["worktree"]),base_commit(meta),commit,rd,config()); c["status"]="validated"; save_current(c); print(data["status"])

def review(args):
    c=current(); run_id=active_run_id(c); require_not_finalized(run_id)
    rd=run_dir(c)
    force=bool(getattr(args,"force",False))
    if c.get("status")=="awaiting_human" and (rd/"REVIEW.json").exists() and not force:
        summary(c); return
    require_status(c,"validated",*( ("awaiting_human",) if force else () ))
    if (rd/"REVIEW.json").exists() and not force:
        raise RuntimeError("REVIEW.json already exists; use review --force before finalization to replace it")
    meta=load_json(rd/"META.json"); cfg=config(); wt=Path(meta["worktree"]); result=load_json(rd/"RESULT.json"); val=load_json(rd/"VALIDATION.json")
    require_executor_commit(c,meta)
    base=base_commit(meta); stat=git_ops.run(["git","diff","--stat",f"{base}..{meta['executor_commit']}"],wt).stdout
    diff=git_ops.run(["git","diff",f"{base}..{meta['executor_commit']}"],wt).stdout
    packet=packet_builder.review_packet(RELAY,result,base,meta["executor_commit"],stat,diff,val,cfg["review_diff_limit_bytes"]); metrics=packet_builder.packet_metrics(packet,[RELAY/"prompts/reviewer-codex.md",RELAY/"RUNBOOK.md",RELAY/"STATE.md",RELAY/"HANDOFF.md",rd/"RESULT.json",rd/"VALIDATION.json"])
    packet_builder.enforce_packet_limit(metrics,warning_tokens=cfg.get("packet_warning_tokens",100000),hard_tokens=cfg.get("packet_hard_limit_tokens",150000),allow_large=bool(getattr(args,"allow_large_packet",False)),label="review")
    meta["review_packet_metrics"]=metrics; write_json(rd/"META.json",meta); (rd/"REVIEW_PACKET.md").write_text(packet)
    if cfg["review_backend"]=="codex":
        cmd=backends.codex_command(cwd=None,schema=RELAY/"schemas/review.schema.json",output=rd/"REVIEW.json",sandbox=cfg["reviewer_sandbox"],model=cfg["reviewer_model"])
        backends.run_codex(packet,cmd,rd/"reviewer-events.jsonl")
    else: backends.run_openai_review(packet,load_json(RELAY/"schemas/review.schema.json"),rd/"REVIEW.json",cfg["reviewer_model"],cfg["api_retry_count"])
    c["status"]="awaiting_human"; save_current(c); summary(c)

def recover_commit(args):
    c=current()
    require_status(c,"executor_uncommitted"); require_not_finalized(active_run_id(c))
    rd=run_dir(c); meta=load_json(rd/"META.json"); wt=Path(meta["worktree"])
    if meta.get("executor_commit") or meta.get("recovered_commit"): raise RuntimeError("executor commit is already recorded")
    if git_ops.head(wt)!=base_commit(meta): raise RuntimeError("worktree HEAD moved since executor failure")
    reported=sorted(meta.get("reported_changed_files",[])); actual=git_ops.changed_paths(wt)
    unexpected=sorted(set(actual)-set(reported)); missing=sorted(set(reported)-set(actual))
    if unexpected or missing: raise RuntimeError(f"change set differs from recorded executor changes; unexpected={unexpected}, missing={missing}")
    if not actual: raise RuntimeError("no executor changes remain to recover")
    print(git_ops.run(["git","diff","--stat","HEAD"],wt).stdout.rstrip() or "Only untracked files changed")
    recovered_validation=validation.run_uncommitted(wt,actual,rd,config())
    if recovered_validation["status"]!="pass": raise RuntimeError("configured recovery validations failed")
    if not args.yes:
        if not sys.stdin.isatty(): raise RuntimeError("recover-commit requires --yes or interactive confirmation")
        if input("Create the executor recovery commit? [y/N] ").strip().lower() not in ("y","yes"): raise RuntimeError("recovery cancelled")
    git_ops.run(["git","add","--"]+actual,wt)
    result=load_json(rd/"RESULT.json") if (rd/"RESULT.json").exists() else {}
    message=args.message or result.get("headline") or config().get("executor_commit_message") or f"Recover executor changes for {meta['run_id']}"
    git_ops.run(["git","commit","-m",message],wt)
    commit=git_ops.head(wt); meta["executor_commit"]=commit; meta["recovered_commit"]=commit; meta["recovered_at"]=now(); write_json(rd/"META.json",meta)
    c.update(status="executed",last_outcome=result.get("outcome",c.get("last_outcome"))); save_current(c); print(commit)

def summary(c):
    rd=run_dir(c); r=load_json(rd/"RESULT.json"); v=load_json(rd/"VALIDATION.json"); q=load_json(rd/"REVIEW.json")
    print(f"Run: {c['last_run_id']}\nExecutor outcome: {r['outcome']}\nIndependent validations: {v['status']}\nReviewer verdict: {q['verdict']}\nMaterial scope corrections: {len([x for x in q['scope_corrections'] if x['severity']!='minor'])}\nProposed next task: {q['state_patch']['next_task']}\nCommands:\n  relay.py accept\n  relay.py reject")

def append_ledger(entry):
    if ledger_entry(entry["run_id"]): raise RuntimeError(f"ledger already contains {entry['run_id']}")
    with (RELAY/"LEDGER.jsonl").open("a") as f:f.write(json.dumps(entry,separators=(",",":"))+"\n")

def review_override(decision, rev, override, reason):
    if decision=="reject": return None
    verdict=rev.get("verdict")
    if verdict=="accept": return None
    if verdict not in {"accept_with_corrections","reject","human_review"}:
        raise RuntimeError(f"unknown reviewer verdict: {verdict}")
    if not override:
        if verdict=="accept_with_corrections":
            raise RuntimeError("reviewer requires corrections; acceptance requires re-review or --override-review --reason TEXT")
        raise RuntimeError(f"reviewer verdict is {verdict}; acceptance requires --override-review --reason TEXT")
    if not reason or not reason.strip(): raise RuntimeError("--override-review requires a non-empty --reason")
    return {"reason":reason.strip(),"recorded_at":now()}

def preflight_finish(decision, override=False, reason=None):
    c=current(); run_id=active_run_id(c)
    existing=finalized_entry(run_id)
    if existing:
        prior=existing["human_decision"]
        if prior==decision:
            print(f"{run_id} already finalized as {decision}"); return None
        raise RuntimeError(f"{run_id} was finalized as {prior} and cannot be changed to {decision}")
    require_status(c,"awaiting_human")
    rd=run_dir(c)
    artifacts={}
    for name in ("RESULT.json","VALIDATION.json","REVIEW.json"):
        path=rd/name
        if not path.exists(): raise RuntimeError(f"finalization preflight failed: missing {name}")
        try: artifacts[name]=load_json(path)
        except (OSError,json.JSONDecodeError) as exc: raise RuntimeError(f"finalization preflight failed: invalid {name}: {exc}") from exc
    meta_path=rd/"META.json"
    if not meta_path.exists(): raise RuntimeError("finalization preflight failed: missing META.json")
    try: meta=load_json(meta_path)
    except (OSError,json.JSONDecodeError) as exc: raise RuntimeError(f"finalization preflight failed: invalid META.json: {exc}") from exc
    wt=Path(meta["worktree"]); commit=meta.get("executor_commit"); base=base_commit(meta)
    if not commit or not git_ops.commit_exists(wt,commit): raise RuntimeError("finalization preflight failed: executor commit missing")
    git_ops.ensure_clean(wt)
    # Any row, even an old non-final row, blocks mutation. Final rows were handled
    # above so same-decision retries remain idempotent.
    if ledger_entry(run_id): raise RuntimeError(f"finalization preflight failed: ledger already contains {run_id}")
    val=artifacts["VALIDATION.json"]; rev=artifacts["REVIEW.json"]
    if decision=="accept" and val.get("status")!="pass": raise RuntimeError("cannot accept failed validations")
    override_record=review_override(decision,rev,override,reason)
    ensure_only_control_state_dirty()
    if not base or not git_ops.commit_exists(REPO,base): raise RuntimeError("finalization preflight failed: base commit missing")
    if git_ops.head(REPO)!=base: raise RuntimeError("finalization preflight failed: branch HEAD moved since prepare")
    if not git_ops.is_ancestor(REPO,base,commit): raise RuntimeError("finalization preflight failed: executor commit does not descend from base_commit")
    return c,rd,meta,artifacts["RESULT.json"],val,rev,wt,commit,base,override_record

def commit_control_plane(run_id, decision):
    paths=[str(p.relative_to(REPO)) for p in (RELAY/"STATE.md",RELAY/"HANDOFF.md",RELAY/"CURRENT.json",RELAY/"LEDGER.jsonl")]
    git_ops.run(["git","add","--",*paths],REPO)
    git_ops.run(["git","commit","-m",f"Finalize relay run {run_id}: {decision}"],REPO)

def finish(decision, override=False, reason=None):
    checked=preflight_finish(decision,override,reason)
    if checked is None: return
    c,rd,meta,res,val,rev,wt,commit,base,override_record=checked; run_id=meta["run_id"]
    if decision=="accept":
        git_ops.run(["git","merge","--ff-only",commit],REPO)
        patch=rev["state_patch"]
        additions=patch["banked_results_add"]+patch["closed_architectures_add"]
        state=(RELAY/"STATE.md").read_text()+"\n## Accepted iteration additions\n"+"\n".join(f"- {x}" for x in additions)+f"\n\n## Current open gate\n\n{patch['open_gate']}\n\n## Formalization boundary\n\n{patch['formalization_boundary']}\n\n## Single best next strategic problem\n\n{patch['next_task']}\n"
        (RELAY/"STATE.md").write_text(state)
        c.update(accepted_commit=commit,iteration=meta["iteration"],status="finalized",consecutive_rejections=0)
        final_math=commit
    else:
        c.update(iteration=meta["iteration"],status="finalized",consecutive_rejections=c["consecutive_rejections"]+1)
        final_math=None
    # Both decisions hand the next run the review's corrective/strategic task.
    (RELAY/"HANDOFF.md").write_text(rev["next_handoff"].rstrip()+"\n")
    entry={"schema_version":2,"run_id":run_id,"iteration":meta["iteration"],"started_at":meta["started_at"],"completed_at":now(),"base_commit":base,"accepted_parent_commit":base,"executor_commit":commit,"final_accepted_commit":final_math,"handoff_sha256":meta["handoff_sha256"],"state_sha256_before":meta["state_sha256_before"],"state_sha256_after":sha(RELAY/"STATE.md") if decision=="accept" else None,"executor_outcome":res["outcome"],"review_verdict":rev["verdict"],"validation_status":val["status"],"changed_files":val["changed_files"],"claims_accepted":rev["verified_claims"] if decision=="accept" else [],"claims_rejected":rev["unsupported_claims"],"next_task":rev["state_patch"]["next_task"],"executor_usage":{},"reviewer_usage":{},"human_decision":decision,"review_override":override_record}
    append_ledger(entry); c.update(status="initialized",last_outcome=res["outcome"]); save_current(c)
    commit_control_plane(run_id,decision)
    if decision=="accept" and config().get("remove_worktree_on_accept",False): git_ops.remove_worktree(REPO,wt)
    print(decision+"ed")

def accept(args): finish("accept",args.override_review,args.reason)
def reject(_): finish("reject")

def reconcile(args):
    c=current(); run_id=c.get("last_run_id")
    report={"current_status":c.get("status"),"run_id":run_id,"branch_head":git_ops.head(REPO),"ledger_decision":None,"active_meta":None,"executor_worktree_head":None,"review_post_finalization":False,"changes_required":False}
    if not run_id:
        print(json.dumps(report,indent=2)); return
    entry=finalized_entry(run_id); report["ledger_decision"]=entry.get("human_decision") if entry else None
    rd=REPO/config()["run_root"]/run_id; meta_path=rd/"META.json"
    if meta_path.exists():
        meta=load_json(meta_path); report["active_meta"]={"base_commit":base_commit(meta),"executor_commit":meta.get("executor_commit"),"worktree":meta.get("worktree")}
        wt=Path(meta.get("worktree",""))
        if wt.exists(): report["executor_worktree_head"]=git_ops.head(wt)
    if entry:
        review_path=rd/"REVIEW.json"
        completed=dt.datetime.fromisoformat(entry["completed_at"])
        if review_path.exists():
            modified=dt.datetime.fromtimestamp(review_path.stat().st_mtime,dt.timezone.utc)
            report["review_post_finalization"]=modified>completed or c.get("status")=="awaiting_human"
        accepted_mismatch=entry["human_decision"]=="accept" and entry.get("final_accepted_commit") and c.get("accepted_commit")!=entry.get("final_accepted_commit")
        report["changes_required"]=c.get("schema_version")!=2 or c.get("status")!="initialized" or c.get("iteration")!=entry.get("iteration") or accepted_mismatch
        if report["review_post_finalization"]:
            report["note"]="REVIEW.json is post-finalization and non-authoritative; the ledger decision is preserved"
        if args.apply and report["changes_required"]:
            if report["review_post_finalization"] and review_path.exists():
                shutil.copy2(review_path,rd/"REVIEW.post-finalization.json")
            c.update(schema_version=2,status="initialized",iteration=entry["iteration"],last_outcome=entry.get("executor_outcome"))
            if entry["human_decision"]=="accept":
                c["accepted_commit"]=entry.get("final_accepted_commit") or c.get("accepted_commit")
                c["consecutive_rejections"]=0
            save_current(c); report["applied"]=True
    elif c.get("status")=="finalized":
        raise RuntimeError(f"{run_id} says finalized but has no authoritative ledger row")
    print(json.dumps(report,indent=2))
def cycle(args): prepare(args); execute(args); validate(args); review(args)
def run_cmd(args):
    for _ in range(args.max_iterations): cycle(args); break

def main():
    p=argparse.ArgumentParser(); sp=p.add_subparsers(dest="cmd",required=True)
    for name,fn in [("doctor",doctor),("status",status),("execute",execute),("validate",validate),("reject",reject)]: sp.add_parser(name).set_defaults(fn=fn)
    q=sp.add_parser("accept"); q.add_argument("--override-review",action="store_true"); q.add_argument("--reason"); q.set_defaults(fn=accept)
    for name,fn in [("prepare",prepare),("review",review),("cycle",cycle)]:
        q=sp.add_parser(name); q.add_argument("--allow-large-packet",action="store_true")
        if name=="review": q.add_argument("--force",action="store_true")
        q.set_defaults(fn=fn)
    q=sp.add_parser("recover-commit"); q.add_argument("--yes",action="store_true"); q.add_argument("--message"); q.set_defaults(fn=recover_commit)
    q=sp.add_parser("init");q.add_argument("--force",action="store_true");q.set_defaults(fn=init)
    q=sp.add_parser("import-handoff");q.add_argument("file");q.set_defaults(fn=import_handoff)
    q=sp.add_parser("reconcile");q.add_argument("--apply",action="store_true");q.set_defaults(fn=reconcile)
    q=sp.add_parser("run");q.add_argument("--max-iterations",type=int,default=1);q.add_argument("--allow-large-packet",action="store_true");q.set_defaults(fn=run_cmd)
    args=p.parse_args()
    try:return args.fn(args) or 0
    except Exception as e: print(f"ERROR: {e}",file=sys.stderr);return 1
if __name__=="__main__":raise SystemExit(main())
