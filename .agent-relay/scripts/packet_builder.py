from __future__ import annotations
import json, os, re, subprocess
from pathlib import Path

SECRET_NAMES = ("OPENAI_API_KEY", "CODEX_API_KEY", "ANTHROPIC_API_KEY", "AWS_SECRET_ACCESS_KEY")

def _read(path: Path) -> str: return path.read_text(encoding="utf-8")
def section(title: str, body: str) -> str: return f"\n\n## {title}\n\n{body.strip()}\n"

def reject_secrets(text: str):
    for name in SECRET_NAMES:
        value = os.environ.get(name)
        if value and value in text: raise ValueError(f"secret-like environment value from {name} entered packet")

def executor_packet(relay: Path, run_id: str) -> str:
    parts = [_read(relay/"prompts/executor.md"), section("Run ID", run_id),
             section("Stable runbook", _read(relay/"RUNBOOK.md")),
             section("Accepted state", _read(relay/"STATE.md")),
             section("Current handoff", _read(relay/"HANDOFF.md"))]
    packet = "".join(parts); reject_secrets(packet); return packet

def bounded_diff(diff: str, limit: int):
    raw = diff.encode()
    headers = list(re.finditer(r"(?m)^diff --git a/(.*?) b/(.*?)$", diff))
    if len(raw) <= limit:
        return diff, [match.group(2) for match in headers], []
    selected=[]; included=[]; omitted=[]; used=0
    for index, match in enumerate(headers):
        end = headers[index + 1].start() if index + 1 < len(headers) else len(diff)
        section = diff[match.start():end]; size = len(section.encode())
        if used + size <= limit:
            selected.append(section); included.append(match.group(2)); used += size
        else: omitted.append(match.group(2))
    suffix = "\n[DIFF TRUNCATED AT FILE BOUNDARIES]\n" if omitted else ""
    return "".join(selected) + suffix, included, omitted


def change_manifest(worktree: Path, commit: str, changed_files: list[str], included: list[str]) -> list[dict]:
    included_set=set(included); manifest=[]
    for path in changed_files:
        oid = subprocess.run(["git", "rev-parse", f"{commit}:{path}"], cwd=worktree, text=True, capture_output=True)
        size = subprocess.run(["git", "cat-file", "-s", f"{commit}:{path}"], cwd=worktree, text=True, capture_output=True)
        manifest.append({
            "path": path, "git_object": oid.stdout.strip() if oid.returncode == 0 else None,
            "size_bytes": int(size.stdout.strip()) if size.returncode == 0 else None,
            "diff_inclusion": "complete" if path in included_set else "omitted",
        })
    return manifest

def review_packet(relay: Path, result: dict, parent: str, commit: str, stat: str, diff: str, validations: dict, limit: int, *, manifest: list[dict] | None = None) -> str:
    selected, included, omitted = bounded_diff(diff, limit)
    manifest = manifest or [{"path": path, "diff_inclusion": "complete" if path in included else "omitted"} for path in included + omitted]
    ordered = [(_read(relay/"prompts/reviewer-codex.md"), None), (_read(relay/"RUNBOOK.md"), "RUNBOOK"),
      (_read(relay/"STATE.md"), "STATE"), (_read(relay/"HANDOFF.md"), "HANDOFF"),
      (json.dumps(result, indent=2), "EXECUTOR RESULT"), (f"accepted_parent={parent}\nexecutor_commit={commit}", "COMMITS"),
      (stat, "DIFF STAT"), (selected, "RELEVANT DIFF"), (json.dumps(validations, indent=2), "VALIDATIONS"),
      (json.dumps(manifest, indent=2), "CRYPTOGRAPHIC CHANGE MANIFEST"),
      ("\n".join(omitted) or "none", "OMITTED FILES"),
      (json.dumps({"uncertainties":result.get("uncertainties",[]),"possible_overstatements":result.get("possible_overstatements",[])}, indent=2), "UNCERTAINTY")]
    packet = ordered[0][0] + "".join(section(title, body) for body,title in ordered[1:])
    reject_secrets(packet); return packet

def state_size_warning(path: Path, limit: int):
    size = path.stat().st_size
    return f"STATE.md is {size} bytes (soft limit {limit})" if size > limit else None

def packet_metrics(packet: str, included: list[Path]) -> dict:
    sizes = sorted(
        ((str(path), path.stat().st_size) for path in included if path.is_file()),
        key=lambda item: item[1], reverse=True,
    )
    byte_count = len(packet.encode("utf-8"))
    return {
        "bytes": byte_count,
        "estimated_tokens": (byte_count + 3) // 4,
        "included_files": len(sizes),
        "largest_included_files": sizes[:5],
    }

def enforce_packet_limit(metrics: dict, *, warning_tokens: int, hard_tokens: int, allow_large: bool, label: str):
    print(f"{label} packet bytes: {metrics['bytes']}")
    print(f"{label} packet estimated tokens: {metrics['estimated_tokens']}")
    print(f"number of included files: {metrics['included_files']}")
    print(f"largest included files: {metrics['largest_included_files']}")
    if metrics["estimated_tokens"] > hard_tokens and not allow_large:
        raise RuntimeError(
            f"{label} packet exceeds hard ceiling of {hard_tokens} estimated tokens; rerun with --allow-large-packet"
        )
    if metrics["estimated_tokens"] > warning_tokens:
        print(f"WARNING: {label} packet exceeds {warning_tokens} estimated tokens", flush=True)
