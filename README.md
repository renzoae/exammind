# ExamMind — Adaptive Study Coach

[العربية](README.ar.md) · **v1.2** · [Changelog](CHANGELOG.md)

A Claude skill that turns your course material into a personal study coach **and** an interactive study app. It finds your weak topics, including the ones you *think* you know, and works on them with you until exam day.

**[⬇ Download exammind-skill.zip](https://github.com/renzoae/exammind/raw/main/exammind-skill.zip)**

## Features

- **Study web app from your notes.** Upload your slides, notes or past papers and get a phone-friendly app with lessons, flashcards, an adaptive quiz and a mistake log.
- **Adaptive coaching in chat.** It quizzes you one question at a time and makes questions harder as you improve. When you're wrong, it explains why and gives you a similar question to try.
- **Blind-spot detection.** You rate your confidence on each answer. A wrong answer you were sure about gets extra attention.
- **One plan for all your exams.** A day-by-day plan with spaced review, balanced by how close each exam is and how ready you are.
- **Mock exams with timing,** plus mistake review, teach-back and flashcards.
- **Saves your progress** in a spreadsheet or a file, and replies **in your language** (English and Arabic built in).

## Install

1. [Download `exammind-skill.zip`](https://github.com/renzoae/exammind/raw/main/exammind-skill.zip).
2. **Claude app:** upload the zip in your skill settings. **Claude Code:** unzip it into `~/.claude/skills/`.

## Use

> I have Cell Biology on 20 December and Statistics on 23 December. Help me study with ExamMind.

Upload your materials when it asks. You'll get your study app, a quick diagnostic and a plan.

| Say | What happens |
|---|---|
| `quiz me` | Practice on today's topics |
| `study app` | Build or rebuild your study app |
| `my mistakes` | Review open mistakes |
| `mock exam [course]` | Timed exam with timing feedback |
| `flashcards` · `teach back [topic]` · `explain [topic]` | Other study modes |
| `show my progress` · `I'm behind` | Progress and plan changes |

**Try the app:** download [`examples/cell-biology-demo.html`](examples/cell-biology-demo.html) and open it in any browser. Also see the [example chat session](examples/example-session.md).

## Repo layout

```
exammind/                 the skill (this is what goes in the zip)
  SKILL.md                core workflow, which Claude always reads
  references/             details Claude reads only when needed
  templates/              study-app.html and the progress layout
  scripts/build_app.py    turns course data into a study app
examples/                 demo app, its course data, and an example session
tests/test-prompts.md     manual checks after changing the skill
tools/package.py          checks the skill and rebuilds the zip
```

## Contributing

1. Edit the files in `exammind/`.
2. Run `python tools/package.py`, which checks the skill and rebuilds the zip.
3. Go through [tests/test-prompts.md](tests/test-prompts.md), then open a pull request.

To change the app, edit `exammind/templates/study-app.html`, then rebuild the demo:
`python exammind/scripts/build_app.py examples/cell-biology-demo.json examples/cell-biology-demo.html`

## License

MIT
