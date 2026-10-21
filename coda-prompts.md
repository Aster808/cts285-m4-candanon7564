# Coda: Prompting in Stages

An AI helper is optional. If you use one, split the work into stages.

## Why split the work

"Make me a text adventure" gives you a big answer. You cannot check a big answer.
A small prompt gives you a small answer. You can check a small answer.

Each stage makes one thing. That thing is the input for the next stage.

```
IDEA          PLAN             BUILD              CHECK
  |             |                |                  |
  v             v                v                  v
pitch  --->  brief.md  --->  story file  --->  story_check.py
                    ^
                    |
            PLANNING GATE: your player says "yes"
```

### How to split any task

1. Name the final product. (Here: a story file that runs.)
2. List what you must know to make it. (Idea, player, map, passages.)
3. Put the steps in order. Each step uses the output of the one before.
4. Add a check after each step. You do the check, not the AI.

## Four questions for every prompt

| Question | Example answer |
|---|---|
| Who is it for? | A first-year student who knows loops and functions. |
| How big? | 4 ideas, under 40 words each. |
| What shape? | A table. Or: only a code block. |
| What happens next? | I paste it into `brief.md`. |

Also: one task per prompt. One verb, one object.

---

## Stage 1: Idea

**Goal:** choose one story idea. You choose. The AI helps you think.

**Prompt 1A. The AI interviews you.**

```
I am a first-year programming student. I must build a text adventure
with 8 passages, 2 endings, and one replay loop.
Ask me 5 questions, one at a time, to help me find an idea.
Wait for my answer before you ask the next question.
```

**Prompt 1B. The AI gives options.**

```
My answers: [paste your answers here].
Give me 4 story ideas. For each idea, write:
- a title
- one sentence of premise
- the two endings
Keep each idea under 40 words. Do not write any code.
```

**Prompt 1C. The AI helps you write a pitch.**

```
I pick idea [number]. Write a pitch of 3 sentences:
who the player is, what they want, and what stops them.
```

**Your check:**

- [ ] I picked the idea. The AI did not pick it.
- [ ] 8 passages can tell this story.
- [ ] My player might want to play it.

---

## Stage 2: Plan (audience and requirements)

**Goal:** a finished `brief.md`. Input: your interview notes from part 1.

**Prompt 2A. User stories.**

```
Here are my interview notes with my player:
[paste your notes here]
Write 4 user stories in this shape:
As a [kind of player], I want [action], so that [reason].
Use only things in my notes. Do not add new needs.
```

**Your check:** find the note behind each story. Delete any story with no note behind it.

**Prompt 2B. Acceptance checks.**

```
Here are my user stories: [paste them here].
For each story, write one acceptance check.
Each check must be a yes/no test I can do by playing the game.
Do not write checks about code style.
```

**Your check:** can you answer each check with yes or no, by playing? If not, rewrite it.

**Prompt 2C. Story map.**

```
Here are my pitch and my user stories: [paste them here].
Draw a story map as a Mermaid flowchart.
Use 8 passages and 2 endings.
Name passages passage_something. Name endings ending_something.
Every passage needs at least one link, except endings.
Output only the Mermaid code block.
```

**Prompt 2D. Ask for problems, not fixes.**

```
Here is my story map: [paste it here].
List 3 problems. Look for: a passage nobody can reach,
a passage with no way out, a story with only one path.
Do not fix them.
```

**Your check:** you decide which problems are real. Fix the map yourself.
Then pass the planning gate: show the brief to your player.

---

## Stage 3: Design and build

**Goal:** a story file that runs. Work on one passage at a time.

**Prompt 3A. Design first, code later.**

```
Here is my story map: [paste it here].
Write a passage list as a table with 3 columns:
passage name, what happens (one sentence), links to.
Do not write code yet.
```

**Prompt 3B. Build one passage.**

```
Here is one passage from my starter file. It shows the style I use:
[paste passage_closet here]
Write the passage passage_server_room in the same style, in Python.
It has 3 choices:
1. "Read the screen" -> passage_screen
2. "Unplug the fan" -> ending_caught
3. "Go back" -> passage_closet
Use ask(). Return only the function.
```

(C++ route: say "in C++" and paste the C++ passage. Twee route: paste a Twee passage.)

**Your check:** paste the function into your file. Run the story. Run `story_check.py`.
Do this after every passage.

**Prompt 3C. Fix an error.**

```
My program shows this error:
[paste the exact error text here]
Here is the function that fails:
[paste the function here]
Explain the cause in 2 sentences. Then show the smallest fix.
```

**Prompt 3D. Read the checker report.**

```
story_check.py says:
[paste the findings here]
Here are the passages in the findings: [paste them here].
Explain each finding in plain words. Do not change my code.
```

**Prompt 3E. Understand what you have.**

```
Explain this function line by line.
I am a first-year student. Use short sentences.
[paste the function here]
```

**Prompt 3F. Add a hook (example: state).**

```
Here are my passage_closet and passage_hallway: [paste them here].
Add a variable has_key. The choice "Swipe the key card"
must work only when has_key is true.
Show only the changed lines. Say where each line goes.
```

**Your check:** you can explain every line you submit. If you cannot, ask Prompt 3E.

---

## Prompting basics: the short list

1. **One task per prompt.** One verb, one object.
2. **Give the input.** Paste your notes, your code, your error. The AI cannot see your screen.
3. **Say the size.** "4 ideas", "under 40 words", "one function".
4. **Say the shape.** "A table", "only a code block", "3 sentences".
5. **Say what not to do.** "Do not write code yet." "Do not fix them."
6. **Check the answer yourself.** The AI can be wrong. Run the code. Play the story.

## Weak prompts and better prompts

| Weak | Why it is weak | Better |
|---|---|---|
| "Make me a text adventure." | No player, no size, no shape. You cannot check it. | Use the 3 stages above. |
| "Fix my code." | The AI cannot see the code or the error. | Prompt 3C: paste both. |
| "Write the whole story file." | Too big to check in one pass. | Prompt 3B: one passage at a time. |
| "Give me an idea." | Any idea fits. You get a generic one. | Prompt 1A, then 1B. |

## Practice (5 minutes)

Rewrite "Make me a text adventure" with the four questions: who, how big, what shape, what next.
Trade with a classmate. Can they tell what you want?

## Keep a log: prompts.md

Your instructor asks you to record your AI use. Copy this block for each prompt you use.

```
## Stage: [idea | plan | build]
Prompt:
What the AI gave me (one line):
What I kept, changed, or threw away:
```

Write the last two lines in your own words.
