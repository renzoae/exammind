# ExamMind — Adaptive Study Coach

ExamMind is a Claude skill that turns Claude into a study coach for university exams. It learns your course from your own notes and slides, finds your weak topics, and keeps quizzing you on them until you're ready.

## What it does

- **Diagnostic quiz.** A short test on each topic to find what you already know and what you don't.
- **Study plan.** A day-by-day plan up to your exam date. Weak and high-yield topics get more time, and topics come back for spaced review so you don't forget them.
- **Adaptive practice.** Questions get harder as you improve. When you get one wrong, it explains the mistake and gives you a similar question to try again.
- **Learns from your notes.** Questions come from your own lecture notes, slides and past papers, in the same format as your real exam.
- **Saves your progress.** It keeps a progress sheet (or a progress file) so you can continue across sessions.
- **Your language.** It replies in whatever language you write in.

## Install

**[⬇ Download ExamMind (exammind-skill.zip)](https://github.com/renzoae/exammind/raw/main/exammind-skill.zip)**

- **Claude app (claude.ai):** upload `exammind-skill.zip` in your skill settings. You don't need to unzip it.
- **Claude Code:** unzip it and copy the `exammind` folder into `~/.claude/skills/`.

## Use it

Start a chat and say something like:

> I have my Organic Chemistry exam on 15 December. Help me study with ExamMind.

Then upload your notes, slides or past papers when it asks.

### Commands you can use any time

| Say this               | What happens                                  |
|------------------------|-----------------------------------------------|
| `quiz me`              | Practice on today's topics                    |
| `focus on [topic]`     | Practise only that topic                      |
| `mock exam`            | Timed exam-style questions, marked at the end |
| `show my progress`     | Your mastery table and plan                   |
| `I'm behind`           | Rebuilds the plan for the time left           |
| `explain [topic]`      | Short lesson, then 2 check questions          |

## How it works

```
exammind/
├── SKILL.md                     # Main instructions for Claude
├── references/
│   ├── mastery-model.md         # How topic scores go up and down
│   ├── question-design.md       # How questions are written for each level
│   └── study-plan-rules.md      # How the study plan is built
└── templates/
    ├── progress-sheet.md        # Layout of the progress spreadsheet
    └── exammind-progress.md     # Progress file used when a sheet isn't available
```

Each topic has a mastery score from 0 to 100. Correct answers raise it, wrong ones lower it, and topics you haven't practised for a week slowly drop. The score decides how hard your next question is and how much time the topic gets in your plan.

## Contributing

Ideas and improvements are welcome. Open an issue or a pull request.

## License

MIT. See [LICENSE](LICENSE).
