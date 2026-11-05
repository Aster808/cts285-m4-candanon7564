# CTS-285 Module 4 — Design Validation

## Project
**DataMan: Check an Answer + Two-Try Feedback**

## Selected Product Slice
ST-1.1 / ST-1.2 — Check an Answer + Two-Try Feedback

## Design Question
How should DataMan check a learner's answer, provide feedback after an incorrect answer, and allow a second attempt before revealing the correct answer?

## Three-Layer Architecture

### 1. Text Interface — app.py
- Displays the math problem.
- Receives the learner's answer.
- Displays feedback.
- Allows the learner to quit and resume a session.

### 2. Business Logic — business_logic.py
- Checks submitted answers.
- Tracks the number of attempts.
- Allows one retry after an incorrect answer.
- Reveals the correct answer after the second incorrect attempt.
- Prevents additional attempts after completion or reaching the attempt limit.

### 3. Stubbed Data Layer — data_layer.py
- Provides sample math problems.
- Loads and saves learner session state.
- Preserves the problem ID, attempt count, and completion status.
- Uses local JSON file storage as a temporary substitute for the final database.

## State Design
The prototype tracks:
- Problem ID
- Number of attempts used
- Whether the problem is completed
- Problem status (open, completed, or revealed).
  
Session information is saved outside the text interface so that unfinished progress can be restored when the program is reopened.

## Acceptance Criteria

- AC-1: A correct first answer completes the problem.
- AC-2: An incorrect first answer provides feedback and allows another attempt.
- AC-3: A second incorrect answer reveals the correct answer.
- AC-4: Reopening an unfinished session restores the previous attempt count.
- AC-5: Reopening a completed or revealed problem preserves its previous status.

## Testing

The automated tests in `test_prototype.py` check:
- Correct answer behavior.
- First incorrect answer behavior.
- Second incorrect answer behavior.
- Answer comparison.
- Attempt limits.

### Manual Persistence Test
- Deleted the previous session data to start fresh.
- Entered an incorrect answer (10).
- Quit the application using Q.
- Restarted the application.
- Confirmed that it restored the session and displayed
  "Resuming session: Try 2 of 2."
- Entered the correct answer (15).
- Confirmed that the problem completed successfully.

### Revealed Status Persistence Test
- Started a fresh session.
- Entered an incorrect answer twice.
- Confirmed that the correct answer was revealed.
- Closed and restarted the application.
- Confirmed that the application displayed "This problem is already closed."
- Confirmed that the revealed answer remained available after restarting.

### Automated Test Results
- Ran: python -m unittest test_prototype.py
- Result: 5 tests passed.
- Ran: python app.py
- Result: Application launched successfully.
  
### Observation from Testing
During testing, I noticed that entering text such as `abc` or entering `15.0` instead of `15` counts as an incorrect attempt. This made me realize that the prototype does not currently distinguish between an invalid input format and an incorrect answer. A future revision could validate the input before using an attempt. This would make the feedback clearer for learners.

## Evaluation and Revision

The prototype demonstrates that answer checking and two-try feedback can operate independently of the text interface.

The JSON data layer addresses the investigation finding that learner progress should not disappear when the program closes.

The prototype also demonstrates why completion status must be stored separately from the attempt count.

This supports the revised design decision to preserve session and attempt information outside the interface.

## Intentionally Stubbed Work
- JSON storage replaces the future database.
- Only sample math problems are provided.
- User authentication is not implemented.
- Curator permissions are not implemented.
- The 10-problem practice limit is not implemented.
- A graphical interface is not implemented.
- Full learner history and multi-user access are not implemented.

## Unresolved Questions
- Which curators should be allowed to access learner histories?
- What permissions should curators have?
- How should individual attempts and learner sessions be stored in the final database?
- How should the system support practice sets of up to ten problems?

## Module 5 Handoff

The selected product slice, business rules, state requirements, and acceptance criteria should carry into Module 5.

The next implementation question is how to replace temporary JSON storage with a database while preserving learner sessions, individual attempts, and the ability to review learner history.

The Flask interface should reuse the existing business logic instead of rebuilding the answer-checking rules.

## Related Design Evidence
See `m4-design-investigation-record.md` for the original investigation, design decisions, complications, and product requirements.
