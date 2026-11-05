#!/usr/bin/env python3
"""Check the skill and rebuild exammind-skill.zip.  Run from the repo root:  python tools/package.py"""
import re, sys, zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
skill = root / "exammind"
text = (skill / "SKILL.md").read_text(encoding="utf-8")

# 1. Frontmatter has a name and a short enough description
m = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n", text)
if not m:
    sys.exit("SKILL.md frontmatter must start with name and description")
if len(m.group(2)) > 1024:
    sys.exit("description is longer than 1024 characters")

# 2. Every file SKILL.md points to exists
missing = [p for p in sorted(set(re.findall(r"`((?:references|templates|scripts)/[\w./-]+)`", text)))
           if not (skill / p).exists()]
if missing:
    sys.exit("SKILL.md points to missing files: " + ", ".join(missing))

# 3. Build the zip (skip caches and hidden files)
out = root / "exammind-skill.zip"
files = sorted(p for p in skill.rglob("*")
               if p.is_file() and "__pycache__" not in p.parts and not p.name.startswith("."))
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for p in files:
        z.write(p, p.relative_to(root))
print(f"OK: {len(files)} files → {out.name} ({out.stat().st_size // 1024} KB)")
