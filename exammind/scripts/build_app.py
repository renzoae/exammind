#!/usr/bin/env python3
"""Build an ExamMind study app from course data.

Usage:
    python build_app.py course.json output.html

Reads course.json (format in references/study-app.md), checks it, and writes
a single self-contained HTML file based on templates/study-app.html.
"""
import html as htmllib
import json
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "templates" / "study-app.html"
START = '<script type="application/json" id="course-data">'
END = "</script>"


def check(data):
    problems = []
    if not data.get("course"):
        problems.append("missing 'course'")
    topics = data.get("topics") or []
    if not topics:
        problems.append("no topics")
    ids = set()
    for ti, t in enumerate(topics):
        where = f"topic {ti + 1} ({t.get('title', '?')})"
        tid = t.get("id") or f"t{ti}"
        if tid in ids:
            problems.append(f"{where}: duplicate id '{tid}'")
        ids.add(tid)
        if not t.get("title"):
            problems.append(f"{where}: missing title")
        qs = t.get("questions") or []
        if len(qs) < 3:
            problems.append(f"{where}: only {len(qs)} questions (need at least 3)")
        for qi, q in enumerate(qs):
            qw = f"{where}, question {qi + 1}"
            opts = q.get("options") or []
            if not q.get("q"):
                problems.append(f"{qw}: missing 'q'")
            if len(opts) < 2:
                problems.append(f"{qw}: needs at least 2 options")
            a = q.get("answer")
            if not isinstance(a, int) or not 0 <= a < len(opts):
                problems.append(f"{qw}: 'answer' must be the index of the correct option")
            if q.get("level", 1) not in (1, 2, 3):
                problems.append(f"{qw}: 'level' must be 1, 2 or 3")
            wt = q.get("why_tempting") or {}
            for k in wt:
                if not str(k).isdigit() or int(k) >= len(opts) or int(k) == a:
                    problems.append(f"{qw}: why_tempting key '{k}' must be a wrong option's index")
        for ci, c in enumerate(t.get("flashcards") or []):
            if not c.get("front") or not c.get("back"):
                problems.append(f"{where}, card {ci + 1}: needs 'front' and 'back'")
    return problems


def build(data):
    html = TEMPLATE.read_text(encoding="utf-8")
    start = html.index(START) + len(START)
    end = html.index(END, start)
    # Escape "</" so course text can never close the script tag early.
    payload = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    html = html[:start] + "\n" + payload + "\n" + html[end:]
    title = htmllib.escape(f"{data['course']} · ExamMind")
    return html.replace("<title>ExamMind Study App</title>", f"<title>{title}</title>", 1)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    problems = check(data)
    if problems:
        print("Fix these before building:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    Path(sys.argv[2]).write_text(build(data), encoding="utf-8")
    n_q = sum(len(t.get("questions") or []) for t in data["topics"])
    n_c = sum(len(t.get("flashcards") or []) for t in data["topics"])
    print(f"Built {sys.argv[2]}: {len(data['topics'])} topics, {n_q} questions, {n_c} flashcards")


if __name__ == "__main__":
    main()
