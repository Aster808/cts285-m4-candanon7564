<!-- compositor: M3A · assess — interstitial bonus module between M3 and M4. Plain register; no fiction framing until the instructor records an approval. -->

# M3A Bonus — Fall Break Adventure

**Build a choose-your-own-adventure story for one real player. Plan it from evidence. Decide what fits. Then build it.**

This assignment is optional. It is bonus credit. Plan for about 5 hours over the break.

## Purpose

In Modules 1 to 3 you worked on DataMan. The manual was your evidence. The stakeholders were on paper. Somebody else set the scope.

This time the product is yours. The stakeholder is a real person you can ask. The budget is small, so you cannot build everything your player wants. You must decide what goes in and say why.

You will also try three ideas from Module 4 on a small scale. Module 4 will feel familiar when you get there.

## What you use again, and where

You already know these ideas. This assignment asks you to use them, not to repeat them.

| From | Idea | Where you use it here |
|---|---|---|
| M1 | An observation needs evidence | Your player's answers are your evidence. |
| M2 | Evidence → need → requirement | Each user story points to one answer from your player. |
| M3 | A story has a user, a need, and a value | You write 4 to 6 user stories. |
| M3 | An acceptance check must pass or fail | You write one check for each story. |
| M3 | Capacity forces a trade | You have a passage budget. You cut something and record why. |

## What is new (a preview of Module 4)

| Idea | What you do |
|---|---|
| **Ask before you build** | Before you write code, name one thing you do not know yet. |
| **Use the lightest evidence** | Answer that question with the smallest thing that works: a map, a table, or a short test run. |
| **Know where each job lives** | Your program does three jobs: it shows text, it applies rules, and it holds the story. Say where each job is in your file. |

## Pick your route

| Route | Start with |
|---|---|
| Python | `adventure_start.py` |
| C++ | `adventure_start.cpp` |
| Twee | `example.twee` and `twee-basics.md` |

The rules are the same on every route. Python is the route closest to the Flask work in Module 5.

## What to do

**Source document:** `brief-template.md`. Copy it to `brief.md`. You fill it in as you go.

### Part 1. Plan from evidence (no code yet)

1. Interview one player. Write their answers in `brief.md` part 1. Give each answer an ID: E-01, E-02, and so on.
2. Write 4 to 6 user stories. Each story must name the answer it comes from.
3. Write one acceptance check for each story. A check names something you can see or count while you play.
4. Set your budget. You may build **8 to 12 passages**.
5. Put your stories in order of value to your player. Keep what fits the budget. Move the rest to the cut list.
6. For each cut story, write what would have to change for it to come back.
7. Draw your story map.

**Analyst rule:** A story with no evidence behind it is your preference, not your player's need. Delete it or find the evidence.

**Caution:** "So that" must give a reason. If it repeats "I want", rewrite it.

### Planning gate

Show parts 1 to 5 of `brief.md` to your player. Ask: "Is this a story you would play?"

Start Part 2 only after your player says yes.

No player? Use Prompt 2N in `coda-prompts.md`. An AI helper interviews you, and you answer as the player. The AI cannot pass the gate. Put the brief away, read it again later, and say yes or no yourself.

### Part 2. Ask before you build

Before you write code, find one thing you do not know yet. Write it as a question in `brief.md` part 6.

Examples:

- "Can the player reach every ending in 5 choices or fewer?"
- "If the player picks up the key and then goes back, do they still have it?"
- "My player said 'no dead ends'. Does my map have a passage with no way out?"

Then answer it with the lightest evidence that works:

| If your question is about… | Use |
|---|---|
| Paths and endings | Your story map, or `story_check.py --map` on a first draft |
| Something the player carries or remembers | A short table: what it is, where it changes, where it is read |
| Whether a choice feels right | Play a two-passage draft yourself |

Record your decision. Use one word and one sentence:

- **Ready** — build it as planned.
- **Revise** — change the plan first. Say what changed.
- **Split** — build part now. Move the rest to the cut list.
- **Hold** — you cannot answer it yet. Say what would answer it.

**Analyst rule:** A decision is not finished until it names its evidence.

### Part 3. Build

**Source documents:** `adventure_start.py`, `adventure_start.cpp`, `example.twee`, `twee-basics.md`.

1. Run the starter. Play it.
2. Run `python story_check.py` on the starter. Read the finding.
3. Do the `TODO` marks in your starter file.
4. Add one passage at a time. Run the story after each one. Run the checker after each one.
5. In `brief.md` part 7, write one sentence for each job:
   - **Shows text:** which lines print and read input?
   - **Applies rules:** which lines decide what happens next?
   - **Holds the story:** where are the passage words?

You do not have to move any code. You only have to find each job and name it.

### Part 4. Check, then decide

**Source document:** `story_check.py`. It finds orphans, dead ends, broken links, and traps.

1. Run `python story_check.py YOUR_FILE`. Fix every finding.
2. Play your story. Mark each acceptance check pass or fail in `brief.md`.
3. Let your player play it. Watch. Do not help. Write down where they stop or look confused.
4. In `brief.md` part 8, write your decision: **Accept** or **Revise**. Name the evidence.

**Analyst rule:** The checker proves the map works. Only the player can show that the story works. You need both.

Two ways to run the checker:

```
python story_check.py YOUR_FILE
python story_check.py YOUR_FILE --map
```

## Requirements

1. `brief.md` parts 1 to 8 are complete. Your player said yes at the planning gate (no player: you said yes).
2. Each user story names the player answer it comes from.
3. Each user story has one acceptance check that can pass or fail.
4. The cut list has at least one story, and each cut story says what would bring it back.
5. Part 6 has one design question, its evidence, and a decision.
6. The story has 8 to 12 passages and at least 2 endings.
7. At least 2 passages give the player a choice.
8. Python and C++: the player can play again (`TODO 2`). Twee: one link goes back to an earlier passage, and one `(if:)` changes what the player sees.
9. `story_check.py` shows no orphans and no broken links.
10. The story is in your own words. You can explain every line you submit.

## Hooks

Pick any you want to explore.

| Hook | Done when |
|---|---|
| **H1 State** | A variable (`has_key`, `health`, `score`) changes what the player can do. Your part 6 table shows where it changes and where it is read. |
| **H2 Story as data** | The passage words live in one place (a dictionary, a list, or a file). The rest of the program reads them. You can add a passage without writing a new function. |
| **H3 Plan vs built** | `brief.md` shows your final map from `--map` beside your first map. You explain what changed and why. |
| **H4 Bring one back** | You build one story from the cut list. You show what changed so that it fits. |
| **H5 Your own input** | You write your own input tool. It accepts a word ("door") as well as a number. |
| **H6 Playtest** | Your playtest log has 3 or more problems. You fixed each one, or you recorded why you did not. |
| **H7 Twee export** | Your program writes a `.twee` file. Twine opens it and shows the same map. |
| **H8 Second route** | The same story runs on a second route. |
| **H9 Your idea** | You tell your instructor your own hook. They say yes first. |

**H2 is the closest preview of Module 4.** It separates the words of the story from the rules that move the player.

## How far you take it

- **Meets the requirements:** all requirements.
- **One hook:** all requirements and 1 hook.
- **Two hooks and a clean report:** all requirements, 2 hooks, and `story_check.py` shows no findings at all.

## Using an AI helper

You may use one. Read `coda-prompts.md` first. It shows how to split the work into stages.

**Generated is not accepted.** An AI can write a user story, a passage, or a map. It cannot know what your player said. Everything it gives you is a candidate until you check it against your evidence.

- Keep a log in `prompts.md`.
- For each prompt, write what you kept, changed, or threw away, in your own words.
- You must be able to explain every line you submit.

## What to submit

Put your files in a folder named `m3a` in your CTS-285 repository:

- `brief.md`
- your story file (`.py`, `.cpp`, or `.twee`)
- `prompts.md` (if you used an AI helper)
- anything extra for your hooks

Submit the direct GitHub URL to the `m3a` folder in Canvas.

## Get help

- Stuck on the map? Open `widget.html`. Break a link. Watch the checker.
- Stuck on Twee? Read `twee-basics.md`.
- Stuck on code? Run `story_check.py`. Read the **Fix** line.
- Need the lecture? Open `slides.html`. Use the arrow keys.

## Before you submit

- [ ] Each user story names the player answer behind it.
- [ ] My cut list says what would bring each cut story back.
- [ ] My design question has evidence and a decision.
- [ ] My player said yes to my brief (no player: I said yes).
- [ ] I marked each acceptance check pass or fail.
- [ ] My player played my story. I did not help.
- [ ] I wrote Accept or Revise, with evidence.
- [ ] `story_check.py` shows no orphans and no broken links.
- [ ] I can explain every line I submit.

---

<!-- Canvas fields. Canvas renders these. They are not emitted to the HTML. -->

## Due date

*[Not in source]*

## Points

*[Not in source]*

## How to submit

Website URL — direct link to the `m3a` folder.

## Credit for each level

*[Not in source]*
