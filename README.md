# ExamMind — Adaptive Study Coach

[العربية](README.ar.md) · **Version 1.1** · [Changelog](CHANGELOG.md)

ExamMind is a Claude skill that turns Claude into a study coach for university exams. It learns your courses from your own notes and slides, finds your weak topics, including the ones you *think* you know, and keeps working on them with you until you're ready.

**[⬇ Download ExamMind (exammind-skill.zip)](https://github.com/renzoae/exammind/raw/main/exammind-skill.zip)**

## What it does

- **Diagnostic quiz.** A short test on each topic shows where you stand.
- **All your exams in one plan.** A day-by-day plan that balances every course by how close the exam is and how ready you are, with spaced review so you don't forget.
- **Adaptive practice.** Questions get harder as you improve. When you're wrong, it explains why and gives you a similar question to try again.
- **Confidence check.** Rate each answer: guess, fairly sure or certain. Confident wrong answers are flagged as **blind spots**, the misunderstandings that cost the most marks, and get extra attention.
- **Mistake log.** Every mistake is recorded with *why* it happened. ExamMind spots patterns ("you keep forgetting units") and runs mistake review sessions before each exam.
- **Mock exams with timing.** Built like your real exam, with a time budget per question and feedback on where you'd run out of time.
- **Flashcards and teach-back.** Flashcards from your notes, and a mode where you explain a topic in your own words and get it graded.
- **Learns from your notes.** Questions come from your own slides, notes and past papers.
- **Saves your progress.** It keeps a progress sheet, or a progress file, so you can continue in any session.
- **Your language.** It replies in whatever language you write in.

See it in action: **[example session](examples/example-session.md)**.

## Install

1. **[Download exammind-skill.zip](https://github.com/renzoae/exammind/raw/main/exammind-skill.zip)**
2. Add it to Claude:
   - **Claude app (claude.ai):** upload `exammind-skill.zip` in your skill settings. You don't need to unzip it.
   - **Claude Code:** unzip it and copy the `exammind` folder into `~/.claude/skills/`.

## Use it

Start a chat and say something like:

> I have Cell Biology on 20 December and Statistics on 23 December. Help me study with ExamMind.

Then upload your notes, slides or past papers when it asks.

### Commands you can use any time

| Say this               | What happens                                       |
|------------------------|----------------------------------------------------|
| `quiz me`              | Practice on today's topics                         |
| `focus on [topic]`     | Practise only that topic                           |
| `my mistakes`          | Review your open mistakes                          |
| `flashcards [topic]`   | Flashcards from your notes                         |
| `teach back [topic]`   | Explain it yourself and get it graded              |
| `mock exam [course]`   | Timed exam-style questions with timing feedback    |
| `explain [topic]`      | Short lesson, then 2 check questions               |
| `show my progress`     | Readiness, mastery, mistakes and plan              |
| `add a course`         | Add another exam to your plan                      |
| `I'm behind`           | Rebuilds the plan for the time left                |

## How it works

Each topic has a **mastery score from 0 to 100**. Correct answers raise it, wrong ones lower it, and confident wrong answers lower it more. Topics you haven't practised for a week slowly drop. The score decides how hard your next question is and how much time the topic gets in your plan.

```
exammind/                        # ← the skill
├── SKILL.md                     # Main instructions for Claude
├── references/
│   ├── mastery-model.md         # Scoring, confidence, blind spots, readiness
│   ├── question-design.md       # How questions are written for each level
│   ├── study-plan-rules.md      # Single- and multi-course planning
│   └── study-modes.md           # Mistake review, flashcards, teach-back, mock exams
└── templates/
    ├── progress-sheet.md        # Progress spreadsheet layout
    └── exammind-progress.md     # Progress file used when a sheet isn't available
examples/example-session.md      # What a session looks like
tests/test-prompts.md            # Prompts for checking the skill after changes
exammind-skill.zip               # Ready-to-upload skill
```

## Contributing

Ideas and improvements are welcome. Open an issue or a pull request. If you change the skill, run through [tests/test-prompts.md](tests/test-prompts.md) to check that it still behaves as expected.

## License

MIT. See [LICENSE](LICENSE).
