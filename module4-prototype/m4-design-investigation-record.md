# M4 Design Investigation Record

## Product Slice
ST-1.1 / ST-1.2 — Check an Answer + two-try feedback

## Initial Question
How should DataMan check a learner's answer, provide feedback after an incorrect answer, and allow a second attempt before revealing the correct answer?

## Planned Evidence
A behavior flow diagram and an ERD (Entity Relationship Diagram) to understand the two-attempt process and what information needs to be stored.

## Evidence Actually Used
- Use-case boundary / actor-goal framing
- Behavior/state flow and two-attempt simulation
- Data-model/schema and Memory Bank constraint stress tests
- Interface/wireframe comparison and state audit
- Design complication and critique

## Findings
### Use-Case Boundary / Question Framing
Learner → check an answer. Question: What must the learner see after the first wrong attempt so retry behavior is unambiguous?

### Behavior / State
How should the system track the learner's attempts and decide when to allow a retry or reveal the correct answer?

### Data / Persistence
The data-model investigation showed that the system needs to store more than the learner's current score. It needs to preserve learner information, practice sessions, individual problems, and attempts. The prototype uses a local JSON file to save the problem ID, number of attempts used, and completion status. This provides a simple way to test whether progress can be restored after closing and reopening the application. A full database is still needed for permanent learner and curator history.

### Memory Bank Constraint
The Memory Bank constraint stress test showed that the system must preserve important learner progress without depending only on information displayed in the interface. If session information is lost when the application closes, the learner's progress and attempt history may not be available later. The design therefore needs a separate data layer that can save and retrieve session information.

**Constraint boundary selected:** The selected constraint boundary is that learner session and attempt information must remain available outside the interface when the application closes and reopens. The interface should not be responsible for permanently storing learner progress. The data layer is responsible for saving and retrieving that information.

### Interaction
The interaction evidence showed that a simple score panel is not enough. The system needs to save the learner's history, sessions, and individual problem attempts so a curator can review scores, missed problems, and how many tries the learner used later.

## Layer Boundary Notes
**Business behavior that should remain outside the interface:**
The answer-checking rules, attempt counter, retry rules, and decision to reveal the correct answer should be handled by the business logic, not the text interface.

**Data that can be stubbed now:**
The prototype can use sample math problems and a local JSON file instead of a full database. It can store the current problem ID, attempt count, completion status, and problem status. Real learner accounts, curator permissions, complete practice-set records, individual attempt histories, and multi-user database access can remain future work.

## New Complication
**Response:** Revise state boundary

I chose to revise the state boundary because the evidence shows that the learner's attempt history could be lost when the program closes. Saving the attempt and session information outside the interface will allow the system to remember the learner's progress and help curators review results later. This is based on the need for reliable history, not just convenience.

## Build-Readiness Decision
**Disposition:** Revise

**Design decision:**
Revise the design before coding. The system needs to save learner attempts and session history outside the interface.

## Revision From Initial Thinking
At first, I thought tracking attempts in the interface was enough. Now I understand that the system must save progress so learners and curators can access the history later.

## Tradeoff Accepted
Saving extra information makes the design more complex, but it prevents important learner progress from being lost.

## Unresolved Uncertainty
I still need to determine which curators are allowed to access learner histories and what permissions they should have.

## Next Question
How should the system store and restore learner sessions and attempts when the program is closed and reopened?

## Three-Layer Prototype Bridge
Text interface: Handles learner input, displays questions, shows feedback, and provides buttons for retry, clear, and help.

Business logic: Checks answers, tracks the two attempts, decides when retries are allowed, controls when the correct answer is revealed, and enforces the 10-problem limit.

Stubbed data layer: Stores and retrieves learners, problems, practice sets, sessions, scores, and individual attempts. It should also preserve learner progress when the program closes so results can be reviewed later.

## Trace Back to Product Work
ST-1.1 and ST-1.2. The system must check answers, identify correct and incorrect responses, allow two attempts, and reveal the correct answer only after the second incorrect attempt.
