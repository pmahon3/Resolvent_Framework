"""Seed data for SHELF_INDEX.json (2026-10-20). For each shelf item (PDF, or a folder of chapters):
pdfinfo title/author, pages, text-layer size, the first ~700 characters, and every repo file that mentions
the item's filename stem or its first-author surname. Output: JSON on stdout. Summaries are written by hand
from this seed plus reading; nothing here is a summary.
Usage: python3 shelf_index_seed.py <shelf_dir> <repo_root>
"""
import json, os, re, subprocess, sys
shelf, root = sys.argv[1], sys.argv[2]
def run(cmd):
    try: return subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout
    except Exception: return ""
def mentions(token):
    out = run(["grep", "-rIl", "--include=*.md", "--include=*.tex", "--include=*.json", "--include=*.bib",
               "-i", token, os.path.join(root, "notes"), os.path.join(root, "papers"), os.path.join(root, "WHY.md")])
    return sorted({os.path.relpath(p, root) for p in out.split() if "SHELF_INDEX" not in p})
items = []
for name in sorted(os.listdir(shelf)):
    p = os.path.join(shelf, name)
    if name.startswith(".") or name.endswith(".json"): continue
    files = sorted(os.path.join(p, f) for f in os.listdir(p)) if os.path.isdir(p) else [p]
    pdfs = [f for f in files if f.endswith(".pdf")]
    first = pdfs[0] if pdfs else files[0]
    info = run(["pdfinfo", first]) if pdfs else ""
    meta = {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in info.splitlines() if ":" in l)}
    text = run(["pdftotext", "-l", "2", first, "-"]) if pdfs else ""
    stem = os.path.splitext(name)[0]
    surname = re.split(r"[_\-0-9]", stem)[0]
    items.append({"file": name + ("/" if os.path.isdir(p) else ""), "n_files": len(files),
                  "pdf_title": meta.get("Title", ""), "pdf_author": meta.get("Author", ""), "pages": meta.get("Pages", ""),
                  "text_chars_p1_2": len(text), "head": re.sub(r"\s+", " ", text)[:700],
                  "mentions_stem": mentions(stem), "mentions_surname": mentions(surname)[:25]})
json.dump(items, sys.stdout, indent=1, ensure_ascii=False)
