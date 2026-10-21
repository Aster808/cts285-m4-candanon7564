"""
adventure_start.py - THE NIGHT SHIFT (starter story, Python)

Run it:   python adventure_start.py
Check it: python story_check.py adventure_start.py --map

RULES FOR THIS FILE
- One function = one passage.
- A passage function starts with  passage_  (example: passage_start).
- An ending function starts with  ending_   (example: ending_free).
- A passage ends by calling the next passage. Endings call nothing.
- story_check.py reads these names. Keep the prefixes.
"""


# ---------------------------------------------------------------
# Tool (provided): ask()
# Shows numbered options. Repeats until the player enters a valid
# number. Returns the number the player chose (1, 2, 3, ...).
# ---------------------------------------------------------------
def ask(prompt, options):
    while True:
        print()
        print(prompt)
        for number, text in enumerate(options, start=1):
            print(f"  {number}. {text}")
        try:
            raw = input("> ").strip()
        except EOFError:
            raise SystemExit  # input closed: stop the program
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw)
        print(f"Enter a number from 1 to {len(options)}.")


# ---------------------------------------------------------------
# Passages
# ---------------------------------------------------------------
def passage_start():
    print("You are locked in the campus lab. It is 11 PM. The lights hum.")
    choice = ask("What do you do?", [
        "Try the front door",
        "Check the server closet",
    ])
    if choice == 1:
        passage_door()
    elif choice == 2:
        passage_closet()


def passage_door():
    print("The front door is locked. The handle does not move.")
    choice = ask("What do you do?", [
        "Shake the handle hard",
        "Go back",
    ])
    if choice == 1:
        ending_caught()
    elif choice == 2:
        passage_start()


def passage_closet():
    print("A key card hangs on a hook. A fan roars. A vent cover is loose.")
    # TODO 1: Add a third option, "Crawl into the vent".
    #         Make it call passage_vent(). Then run story_check.py again.
    choice = ask("What do you do?", [
        "Take the key card",
        "Go back",
    ])
    if choice == 1:
        passage_hallway()
    elif choice == 2:
        passage_start()


def passage_hallway():
    print("A side exit has a card reader. A guard sleeps in a chair nearby.")
    choice = ask("What do you do?", [
        "Swipe the key card",
        "Wake the guard to ask for help",
    ])
    if choice == 1:
        ending_free()
    elif choice == 2:
        ending_caught()


def passage_vent():
    print("The vent is tight. Cold air blows from the far end. You see the roof.")
    choice = ask("What do you do?", [
        "Climb out onto the roof",
    ])
    if choice == 1:
        ending_free()


# TODO 3: Write at least 3 new passages of your own.
#         Link each one from a passage that already exists.
#         Add at least 1 new ending.


# ---------------------------------------------------------------
# Endings
# ---------------------------------------------------------------
def ending_free():
    print("\nYou step into the cool night air. You are free!")


def ending_caught():
    print("\nThe guard turns on the light. You are caught.")


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------
def main():
    print("=== THE NIGHT SHIFT ===")
    passage_start()
    print("\nThe end.")
    # TODO 2: Put the story in a loop so the player can play again.
    #         After the ending, call ask("Play again?", ["Yes", "No"]).
    #         Stop the loop when the player chooses No.

    # TODO 4 (hook): Keep a variable, for example  has_key = False.
    #                Use it so one choice only works after the player
    #                picks up the key card.


if __name__ == "__main__":
    main()
