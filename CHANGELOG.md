# Changelog

## v1.2 — 2026-11-05

**New**
- **Study web app.** ExamMind turns the student's materials into a single-page app with lessons, flashcards, an adaptive quiz with confidence ratings, a mistake log, and a "Copy progress" button that hands results back to the chat. It works on phones, in light and dark mode, and right-to-left for Arabic.
- `scripts/build_app.py` checks the course data and builds the app.
- Demo app: `examples/cell-biology-demo.html`.

**Simpler and more efficient**
- `SKILL.md` is about half as long: the core loop stays there, and details load from `references/` only when needed.
- The two progress templates are merged into one `templates/progress.md`.
- `tools/package.py` checks the skill and rebuilds the zip in one command.
- Shorter README.

## v1.1 — 2026-11-05

**New**
- **Several courses at once.** One combined plan that balances all your exams by how close they are and how ready you are.
- **Confidence check.** Rate each answer 1–3. Confident wrong answers are flagged as **blind spots** and get extra practice.
- **Mistake log.** Every mistake is recorded with why it happened; ExamMind spots repeated patterns and runs **mistake review** sessions.
- **Flashcards.** Made from your own notes, including cards for your open mistakes.
- **Teach-back mode.** Explain a topic in your own words and get it graded.
- **Mock exam timing.** Time budget per question, and feedback on where you'd run out of time.
- **Calibration.** Shows how often you're right when you feel certain.

**Improved**
- Progress sheet now has Courses and Mistakes tabs.
- Exam readiness accounts for blind spots.
- Final 3 days before each exam now follow a set routine (mistake review → mock exam → light review).

**Repo**
- Example session, test prompts, Arabic README, and this changelog.

## v1.0 — 2026-11-05

- First release: diagnostic quiz, study plan with spaced review, adaptive practice, questions from your own notes, progress sheet or file, replies in your language.
