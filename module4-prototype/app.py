
from business_logic import evaluate_attempt, can_attempt
from data_layer import get_problem, load_session, save_session


def run():
    session = load_session()
    problem = get_problem(session["problem_id"])

    if problem is None:
        print("Problem not found.")
        return

    print("\n================================")
    print("       DataMan Answer Checker")
    print("================================")
    print("\nQuestion:", problem["question"])

    if session["status"] != "open":
        print("\nThis problem is already closed.")
        if session["status"] == "revealed":
            print("The correct answer was:", problem["answer"])
        return

    if session["attempts_used"] == 1:
        print("\nResuming session: Try 2 of 2.")

    while can_attempt(session["attempts_used"], session["completed"]):
        remaining = 2 - session["attempts_used"]
        print(f"\nAttempts remaining: {remaining}")

        user_answer = input("Enter your answer (or Q to quit): ")

        if user_answer.strip().lower() == "q":
            print("Session saved. Goodbye!")
            return

        result = evaluate_attempt(
            user_answer,
            problem["answer"],
            session["attempts_used"]
        )

        session["attempts_used"] = result["attempts_used"]
        session["completed"] = result["completed"]
        session["status"] = result["status"]

        save_session(session)
        print("\n" + result["feedback"])

    if session["status"] != "completed":
        print("\nThis problem is now closed.")


if __name__ == "__main__":
    run()
