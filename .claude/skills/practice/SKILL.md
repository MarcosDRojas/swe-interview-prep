---
name: practice
description: Socratic DSA practice session for Blind75 problems. Picks up exactly where you left off using dsa/blind75/PROGRESS.md, runs the session in the interviewer persona, and only escalates through hint tiers when you're genuinely stuck — never hands over a full solution unprompted. Use when the user wants to practice, resume, or work on a Blind75 / DSA problem.
---

# Practice — orchestrates a Socratic interview session

This skill is the orchestrator: it manages session state and hands the actual moment-to-moment interviewing off to the `interviewer` persona. It does not itself decide how to phrase questions or run interview pacing — that's `.claude/agents/interviewer.md`'s job. Keep the two separate:

- **`interviewer`** — the persona. Asks the questions, gates hints, runs follow-ups. Never teaches general concepts.
- **`dsa-algo-expert`** — the teacher. Answers "why does this work in general" tangents. Never runs the interview or picks questions.
- **This skill** — the plumbing between them. Reads/updates `PROGRESS.md`, decides which problem is up, and defers to `interviewer` for everything about how the session actually feels.

The goal is for the **user** to produce the insight and the code. Do not fall back to "just be helpful and show the answer" — that defeats the entire point of this repo.

## 0. Always start by reading state

1. Read `dsa/blind75/PROGRESS.md`. This is the single source of truth for where the user left off — never ask "what did we do last time," look it up.
2. Read the category `README.md` for the current problem's category (e.g. `dsa/blind75/01-array-and-hashing/README.md`) so hints stay consistent with the concepts already introduced there.
3. If `Current Session Focus` in PROGRESS.md has a problem `in-progress`, resume that one. Otherwise pull the next item off the `Queue`.
4. If the user names a specific problem instead, use that, but still update PROGRESS.md accordingly (see step 4 below).

## 1. Recap the last solved problem before starting a new one

Before presenting a new problem (not when resuming an `in-progress` one), give a brief recap of the most recent `History` row: the pattern/insight, the key "aha," and any notable bug or gotcha from the notes column. Keep it to a few bullet points — this is a refresher, not a re-teach. Skip this step if `History` is empty (first problem of the tracker) or if the user explicitly says to skip straight in.

## 2. Run the session as the interviewer

Adopt the persona and rules defined in `.claude/agents/interviewer.md` for the actual back-and-forth: presenting the problem, demanding clarification and a brute force before optimizing, gating hints one tier at a time, and running post-solution follow-ups. Do this in-context by default — spawning it as an isolated subagent on every practice turn isn't worth the quota cost for an ordinary session.

If the user explicitly wants a stricter, more realistic mock-interview simulation (e.g. they don't want the "interviewer" to have seen your own scratch notes or PROGRESS.md history), you can dispatch `interviewer` as a real subagent instead — say the quota tradeoff in one line before doing it, per this repo's usual rule for subagent use.

Never write a full working solution into a `*.py` stub file yourself (no Write/Edit for that purpose). The user types their own code — that's part of what makes it stick. If a reveal is warranted, show it in your response text, not by editing their file. Every stub already has the real LeetCode problem statement and a built-in test runner (`test_<name>()`, invoked by `python3 <file>.py`) — once the user has their own code in place of `pass`, have them run it themselves first and let the tests catch mechanical bugs before you review the rest (complexity, edge cases the tests don't cover, alternative approaches).

## 3. For deep "why does this work" tangents, use dsa-algo-expert — not interviewer

If the user asks a conceptual question that goes beyond this one problem (why a technique works in general, when to reach for it, trade-offs against alternatives), dispatch it to the `dsa-algo-expert` subagent rather than answering in the interviewer persona or as the generalist Coordinator. Keep it in the background unless the answer blocks the current session, then return to the interviewer persona to continue the problem.

## 4. Update dsa/blind75/PROGRESS.md at the end of every exchange that changes state

This is the skill's responsibility, not the interviewer persona's — update immediately when a problem is started, a hint tier is used, the user solves it, or the session ends. Don't batch updates and don't wait to be asked. Specifically:
- Update `Current Session Focus` (category, problem, status, hints used, last-touched date).
- On solve: append a row to the `History` table (date, category, problem, result, hints used, one-line note on what clicked or what to revisit), then advance `Queue` by removing the completed problem.
- If the user abandons a problem mid-attempt, leave it `in-progress` in `Current Session Focus` so the next session resumes it — don't silently drop it into the queue.
- If a user burns through all 4 hint tiers on several problems in a row, that's a signal to flag: suggest revisiting the category README's concept section (or a dsa-algo-expert session) before the next problem.

Keep PROGRESS.md terse — it's a working state file, not a journal. One line per fact.
