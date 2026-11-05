# Mastery model

Each topic has a **mastery score from 0 to 100**.

## Starting score (after the diagnostic)

| Diagnostic result         | Starting score |
|---------------------------|----------------|
| Both questions right      | 60             |
| One right                 | 35             |
| Both wrong / "don't know" | 10             |

Then adjust for confidence:

- A right answer marked **1 (guess)** counts as only half right: −10 from the starting score.
- A wrong answer marked **3 (certain)** marks the topic as a **blind spot**: −5, and add the "blind spot" flag.

## Updating the score after each practice answer

Base change:

| Answer                    | Level 1 | Level 2 | Level 3 |
|---------------------------|---------|---------|---------|
| Correct                   | +5      | +10     | +15     |
| Correct but needed a hint | +2      | +5      | +8      |
| Partly correct            | 0       | +3      | +5      |
| Wrong                     | −10     | −8      | −5      |

Confidence adjustment (add to the base change):

| Confidence     | If correct                 | If wrong                         |
|----------------|----------------------------|----------------------------------|
| 1 — guess      | halve the gain (round down)| no extra change                  |
| 2 — fairly sure| no change                  | no change                        |
| 3 — certain    | +2                         | −5 extra, and flag a blind spot  |

Keep the score between 0 and 100. Wrong answers on hard questions cost less, because those questions are meant to stretch the student.

**Clearing a blind spot:** remove the flag once the student answers two questions on that topic correctly *and* confidently (2 or 3) in a later session.

**Forgetting:** if a topic hasn't been practised for 7 or more days, take 10 points off when you load progress (only once per gap).

## Levels

| Score   | Level      | Questions to ask     |
|---------|------------|----------------------|
| 0–29    | Weak       | Mostly Level 1       |
| 30–59   | Developing | Mostly Level 2       |
| 60–84   | Strong     | Mostly Level 3       |
| 85–100  | Mastered   | Level 3; review only |

Mix in a question from the level below now and then, so the basics stay solid. A topic with a blind spot can't be "Mastered" until the flag is cleared.

## Calibration

Track how well the student's confidence matches their results: the share of their "certain" answers that were correct. Mention it in progress summaries in plain words, e.g. "When you're certain, you're right 92% of the time" or "You're often certain on answers that turn out wrong, so slow down and double-check on exam day."

## Exam readiness

For each course: readiness = the average mastery across its topics, with high-yield topics counting double, minus 3 points for each open blind spot (minimum 0). Show it as a percentage.
