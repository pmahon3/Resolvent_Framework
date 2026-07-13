from __future__ import annotations
import json, os, subprocess, time
from pathlib import Path

def codex_command(*, cwd: Path | None, schema: Path, output: Path, sandbox: str, model: str = "", jsonl=True):
    cmd = ["codex", "exec", "--ephemeral", "--sandbox", sandbox]
    if cwd: cmd += ["--cd", str(cwd)]
    if model: cmd += ["--model", model]
    cmd += ["--output-schema", str(schema), "--output-last-message", str(output)]
    if jsonl: cmd += ["--json"]
    cmd += ["-"]
    assert "resume" not in cmd
    return cmd

def run_codex(prompt: str, cmd: list[str], events: Path):
    events.parent.mkdir(parents=True, exist_ok=True)
    with events.open("w", encoding="utf-8") as stream:
        proc = subprocess.run(cmd, input=prompt, text=True, stdout=stream, stderr=subprocess.PIPE)
    if proc.returncode: raise RuntimeError(proc.stderr[-4000:])

def run_openai_review(prompt: str, schema: dict, output: Path, model: str, retries=3):
    if not model: raise RuntimeError("reviewer_model is required for OpenAI review")
    if not os.environ.get("OPENAI_API_KEY"): raise RuntimeError("OPENAI_API_KEY is not set")
    from openai import OpenAI
    client = OpenAI()
    kwargs = {"model": model, "input": prompt, "store": False,
              "text": {"format": {"type":"json_schema","name":"relay_review","strict":True,"schema":schema}}}
    assert "previous_response_id" not in kwargs and "conversation" not in kwargs and kwargs["store"] is False
    for attempt in range(retries):
        try:
            response = client.responses.create(**kwargs)
            output.write_text(response.output_text, encoding="utf-8")
            return getattr(response, "usage", None)
        except Exception:
            if attempt + 1 == retries: raise
            time.sleep(min(2 ** attempt, 8))

class FakeBackend:
    def __init__(self, result): self.result = result
    def run(self, output: Path): output.write_text(json.dumps(self.result), encoding="utf-8")
