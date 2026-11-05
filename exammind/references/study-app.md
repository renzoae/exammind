# Study app

When the student shares their materials, ExamMind turns them into an interactive **study app**: a single web page with lessons, flashcards, an adaptive quiz with confidence ratings, and a mistake log. They can study with it on their phone at any time, even outside the chat.

## When to build it

- **Automatically**, as soon as the student has shared materials and confirmed the topic list (Setup, step 1). Build one app per course.
- **On request**: "make me a study app", "build the app", "web app for [course]".
- **Rebuild** it when the student adds new materials, adds topics, or asks for more questions.

If the student shared no materials, still offer the app, but say the content will come from standard course knowledge rather than their notes.

## Step 1: Write the course data (JSON)

Write a `course.json` file with this shape:

```json
{
  "course": "Cell Biology",
  "exam_date": "2026-12-20",
  "language": "en",
  "dir": "ltr",
  "topics": [
    {
      "id": "membrane",
      "title": "Membrane transport",
      "high_yield": true,
      "summary": "2–4 sentence plain-language overview.",
      "key_points": ["4–6 short facts the student must know"],
      "example": "One worked example or real-world case.",
      "source": "Lecture 3, slides 4–15",
      "flashcards": [
        {"front": "Question or term", "back": "Answer in 2 lines or fewer"}
      ],
      "questions": [
        {
          "level": 1,
          "q": "Question text",
          "options": ["A", "B", "C", "D"],
          "answer": 2,
          "explanation": "Why the correct answer is right (1–3 sentences).",
          "why_tempting": {"1": "Why option 1 is a tempting wrong answer."}
        }
      ]
    }
  ]
}
```

Field rules:

- `language`: the student's language code (`en`, `ar`, …). English and Arabic interface text are built in. For any other language, add a `"ui"` object that translates the interface keys (copy the `en` keys from the template's `UI` block).
- `dir`: `"rtl"` for Arabic, Hebrew, Persian or Urdu; otherwise `"ltr"`.
- Write **all content** (summaries, questions, cards) in the student's language. Keep technical terms as in their materials, with a translation in brackets where helpful.
- `answer` is the **index** (starting at 0) of the correct option. The app shuffles the options, so there's no need to vary the position yourself.
- `why_tempting` keys are indexes of **wrong** options. Add one for every distractor that's a real, common mistake. This is what makes the feedback useful.
- `source` points to where in the student's materials the topic comes from.

Content per topic:

| Item        | How many | Notes |
|-------------|----------|-------|
| key_points  | 4–6      | Short and testable |
| flashcards  | 3–8      | One idea per card |
| questions   | 5–9      | At least 2 at Level 1, 2 at Level 2 and 1 at Level 3, so the app can adapt and has "similar question" follow-ups |

Follow `references/question-design.md`. Every question must be answerable from the student's materials, and every fact must be correct. Check math and science answers before writing them. In the app, all questions are multiple choice, so it can mark them instantly. Keep essay and calculation practice in the chat.

## Step 2: Build the page

If you can run Python:

```bash
python scripts/build_app.py course.json "<Course> - ExamMind.html"
```

The script checks the data (missing fields, wrong answer indexes, too few questions) and writes a self-contained HTML file from `templates/study-app.html`. Fix anything it reports, then build again.

If you can't run code, copy `templates/study-app.html` and replace the JSON inside `<script type="application/json" id="course-data">…</script>` with the course data, writing `<\/` instead of `</` inside any text. Also put the course name in the `<title>`.

## Step 3: Deliver it

- If you can publish **artifacts or web pages**, publish the HTML so the student gets a link they can open on their phone and share with classmates.
- Otherwise, give them the HTML file and tell them to open it in any browser.

Tell the student in 2–3 lines what's inside (topics, number of questions and cards), and how it connects to ExamMind in the chat:

> Your study app is ready: 6 topics, 42 questions, 30 flashcards. Your progress is saved in this browser. When you come back to chat with me, tap **Copy progress** at the bottom of the Home screen and paste it here, and I'll update your plan and mistake log.

## Using the app's progress

When the student pastes text starting with **"ExamMind progress from the study app"**, treat it like a progress file: update topic mastery, blind spots and open mistakes in the progress tracker, then continue with the plan. Mastery scores in the app use the same model as `references/mastery-model.md`, except that new topics start at 20.

## What the app does (so you can explain it)

- **Home:** readiness, accuracy, calibration, topics sorted from weakest, open mistakes, and Copy progress.
- **Learn:** a lesson per topic (summary, key points, example, source), with buttons to practise or open that topic's flashcards.
- **Cards:** flip cards by topic; "Again" cards come back first in the next round.
- **Quiz:** smart practice. It picks weak topics and blind spots first, at the level that suits each topic's mastery. The student picks an answer, then rates their confidence. A wrong answer shows why it's tempting, the explanation and the source, followed by a similar question. A confident wrong answer becomes a blind spot and gets two follow-ups. Sessions are 12 questions, with a summary at the end.
- **Mistakes:** every wrong answer and lucky guess, with a "Review my mistakes" session.
- Progress is saved in the student's browser on that device only.
