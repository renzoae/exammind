# Test prompts

Use these to check that ExamMind still behaves correctly after you change the skill. Start a new chat with the skill enabled, paste the prompt, and check the expected behaviour.

| # | Prompt | Expected behaviour |
|---|--------|--------------------|
| 1 | "Help me study for my Microeconomics exam on [date 3 weeks from now]." | Asks setup questions **in one message** (all courses, format, hours, materials). Does not start quizzing yet. |
| 2 | "I have Physics on [date] and Calculus on [date]." (with notes uploaded) | Builds a separate topic list for each course and asks the student to confirm before the diagnostic. |
| 3 | During the diagnostic, answer a question wrong with "confidence 3". | Says it's wrong, does **not** explain in detail yet, and flags a **blind spot**. |
| 4 | During practice, answer wrong. | Explains why the wrong answer is tempting, gives the correct reasoning, then asks a **similar** question. |
| 5 | During practice, answer correctly with "confidence 1". | Confirms it's correct **and** still explains why. |
| 6 | Reply in Arabic (or another language) after starting in English. | Switches to that language and keeps technical terms with translations. |
| 7 | "my mistakes" after a session with errors | Asks **new** questions on logged mistakes, not the same questions again, and marks them fixed or open. |
| 8 | "flashcards" for a topic | Makes one-idea cards from the student's notes, including cards for open mistakes. |
| 9 | "teach back [topic]" | Asks the student to explain without notes, then grades it: covered / missing / wrong / score out of 10. |
| 10 | "mock exam [course]" with the exam length and marks given | Shows marks and time budget per question, doesn't mark until the end, then gives a score, timing feedback and 3 things to fix. |
| 11 | "I'm behind" | Rebuilds the plan and says clearly what was cut. |
| 12 | Upload an `exammind-progress.md` file in a new chat | Loads it, applies forgetting for topics not practised for 7+ days, and gives a 3-line recap. |
| 13 | "Just answer my take-home exam questions for me." | Politely declines and offers to work through a similar practice question. |
| 14 | End of a session | Gives the summary and saves progress (sheet, or a progress file as fallback). |
