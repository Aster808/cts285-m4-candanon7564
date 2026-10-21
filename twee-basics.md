# Twee Basics

For students who use Twine and do not know JavaScript.

## What Twee is

Twee is a plain-text version of a Twine story. One text file holds every passage.
Twine reads the file and draws the story map for you.

## Which dialect we use

- **File format:** Twee 3. Twine 2.6 and later can import and export it.
- **Story format:** Harlowe 3. It is the default story format in Twine 2.
  You do not need JavaScript. This module uses only links, `(set:)`, and `(if:)`.

## The parts of a .twee file

```
:: StoryTitle
The Night Shift

:: StoryData
{
  "ifid": "32ED7F51-BB19-4C18-BD5D-959282437C79",
  "format": "Harlowe",
  "format-version": "3.3.9",
  "start": "Start"
}

:: Start
You are locked in the campus lab.

[[Try the front door->Door]]
[[Check the server closet->Closet]]
```

| Part | What it does |
|---|---|
| `:: Name` | Starts a passage. The name follows `::`. |
| Text under it | What the player reads. |
| `[[text->Target]]` | A choice. The player sees *text*. The story goes to *Target*. |
| `StoryData` | Settings in JSON. `"start"` names your first passage. |
| `StoryTitle` | The title of the story. |

Keep the `ifid` line as it is. If you start a new story, make a new ID (any
online "UUID generator" works).

## Five rules

1. Passage names are case-sensitive. `Door` and `door` are different passages.
2. The target in a link must match a passage name exactly.
3. Use one link style only: `[[text->Target]]`.
4. Name every ending so it starts with `Ending` (example: `EndingFree`).
5. Every passage that is not an ending needs at least one link.

## Open your story in Twine

1. Open Twine 2.6 or later (desktop app, or the web version at twinery.org).
2. In the Library, choose **Import**. Pick your `.twee` file.
3. Open the story. Twine shows the passages as boxes with arrows. This is your visual map.
4. Edit in Twine if you like. To get the text back, choose **Build**, then **Export As Twee**.
5. To play it: **Build**, then **Play**.

## Make a choice depend on something (state)

Harlowe uses a variable that starts with `$`.

```
:: Setup [startup]
(set: $hasKey to false)

:: Closet
A key card hangs on a hook.

(if: $hasKey is false)[ [[Take the key card->TakeKey]] ]
[[Go back->Start]]

:: TakeKey
(set: $hasKey to true)You take the key card.

[[Back to the closet->Closet]]

:: Hallway
A side exit has a card reader.

(if: $hasKey is true)[ [[Swipe the key card->EndingFree]] ]
[[Wake the guard->EndingCaught]]
```

- `(set: $hasKey to true)` stores a value.
- `(if: $hasKey is true)[ ... ]` shows the text between the brackets only when the test is true.
- The tag `[startup]` runs a passage once, before the first passage. Set your variables there.
  Do not set them in `Start`. The player can return to `Start`, and that would reset them.
- Put a space inside the hook brackets when the hook holds a link: `[ [[link]] ]`.

## Twee and code: the same ideas

| In Python or C++ | In Twee |
|---|---|
| A function named `passage_door` | A passage named `Door` |
| `ask()` and `if` / `elif` | `[[links]]` |
| A call to the next passage | A link to the next passage |
| A function named `ending_free` | A passage named `EndingFree` |
| A variable such as `has_key` | A variable such as `$hasKey` |
| `if has_key:` | `(if: $hasKey is true)[ ... ]` |

Twee has no functions in this module. Loops are your Python and C++ job.
In Twee, a link back to an earlier passage makes a cycle in your map. That is the same idea.

## Check your Twee story

```
python story_check.py example.twee --map
```

The checker finds orphans, dead ends, broken links, and traps.
It ignores passages tagged `startup`, `header`, `footer`, `script`, and `stylesheet`.

## Common mistakes

- A typo in a link target. The checker reports **BROKEN LINK**.
- No `"start"` in `StoryData` and no passage named `Start`. The checker reports **NO START**.
- A last passage with no links and no `Ending` in its name. The checker reports **DEAD END**.
- Three brackets together: `[[[link]]]`. Put a space inside: `[ [[link]] ]`.
