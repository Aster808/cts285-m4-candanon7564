// adventure_start.cpp - THE NIGHT SHIFT (starter story, C++)
//
// Build:  g++ -std=c++17 -Wall -Wextra adventure_start.cpp -o adventure
// Run:    ./adventure            (Windows: adventure.exe)
// Check:  python story_check.py adventure_start.cpp --map
//
// RULES FOR THIS FILE
// - One function = one passage.
// - A passage function starts with  passage_  (example: passage_start).
// - An ending function starts with  ending_   (example: ending_free).
// - A passage ends by calling the next passage. Endings call nothing.
// - story_check.py reads these names. Keep the prefixes.

#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// ---------------------------------------------------------------
// Prototypes
// ---------------------------------------------------------------
int ask(const string& prompt, const vector<string>& options);

void passage_start();
void passage_door();
void passage_closet();
void passage_hallway();
void passage_vent();
void ending_free();
void ending_caught();
// TODO 3: Add a prototype for each new passage you write.

// ---------------------------------------------------------------
// Main
// ---------------------------------------------------------------
int main() {
    cout << "=== THE NIGHT SHIFT ===\n";
    passage_start();
    cout << "\nThe end.\n";
    // TODO 2: Put the story in a loop so the player can play again.
    //         After the ending, call ask("Play again?", {"Yes", "No"}).
    //         Stop the loop when the player chooses No.

    // TODO 4 (hook): Keep a variable, for example  bool hasKey = false;
    //                Use it so one choice only works after the player
    //                picks up the key card. (Hint: it must live where
    //                every passage can reach it.)
    return 0;
}

// ---------------------------------------------------------------
// Tool (provided): ask()
// Shows numbered options. Repeats until the player enters a valid
// number. Returns the number the player chose (1, 2, 3, ...).
// This tool supports up to 9 options.
// ---------------------------------------------------------------
int ask(const string& prompt, const vector<string>& options) {
    int count = static_cast<int>(options.size());
    while (true) {
        cout << "\n" << prompt << "\n";
        for (int i = 0; i < count; i++) {
            cout << "  " << (i + 1) << ". " << options[i] << "\n";
        }
        cout << "> ";
        string line;
        if (!getline(cin, line)) {
            exit(0);  // input closed: stop the program
        }
        if (line.size() == 1 && line[0] >= '1' && line[0] <= '9') {
            int choice = line[0] - '0';
            if (choice <= count) {
                return choice;
            }
        }
        cout << "Enter a number from 1 to " << count << ".\n";
    }
}

// ---------------------------------------------------------------
// Passages
// ---------------------------------------------------------------
void passage_start() {
    cout << "You are locked in the campus lab. It is 11 PM. The lights hum.\n";
    int choice = ask("What do you do?", {
        "Try the front door",
        "Check the server closet",
    });
    if (choice == 1) {
        passage_door();
    } else if (choice == 2) {
        passage_closet();
    }
}

void passage_door() {
    cout << "The front door is locked. The handle does not move.\n";
    int choice = ask("What do you do?", {
        "Shake the handle hard",
        "Go back",
    });
    if (choice == 1) {
        ending_caught();
    } else if (choice == 2) {
        passage_start();
    }
}

void passage_closet() {
    cout << "A key card hangs on a hook. A fan roars. A vent cover is loose.\n";
    // TODO 1: Add a third option, "Crawl into the vent".
    //         Make it call passage_vent(). Then run story_check.py again.
    int choice = ask("What do you do?", {
        "Take the key card",
        "Go back",
    });
    if (choice == 1) {
        passage_hallway();
    } else if (choice == 2) {
        passage_start();
    }
}

void passage_hallway() {
    cout << "A side exit has a card reader. A guard sleeps in a chair nearby.\n";
    int choice = ask("What do you do?", {
        "Swipe the key card",
        "Wake the guard to ask for help",
    });
    if (choice == 1) {
        ending_free();
    } else if (choice == 2) {
        ending_caught();
    }
}

void passage_vent() {
    cout << "The vent is tight. Cold air blows from the far end. You see the roof.\n";
    int choice = ask("What do you do?", {
        "Climb out onto the roof",
    });
    if (choice == 1) {
        ending_free();
    }
}

// TODO 3: Write at least 3 new passages of your own.
//         Link each one from a passage that already exists.
//         Add at least 1 new ending.

// ---------------------------------------------------------------
// Endings
// ---------------------------------------------------------------
void ending_free() {
    cout << "\nYou step into the cool night air. You are free!\n";
}

void ending_caught() {
    cout << "\nThe guard turns on the light. You are caught.\n";
}
