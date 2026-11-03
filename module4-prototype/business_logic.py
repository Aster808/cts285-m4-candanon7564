
MAX_ATTEMPTS = 2


def check_answer(user_answer, correct_answer):
    """Check whether the submitted answer is correct."""
    return str(user_answer).strip() == str(correct_answer).strip()


def evaluate_attempt(user_answer, correct_answer, attempts_used):
    """Apply DataMan's two-attempt feedback rule."""
    attempts_used += 1

    if check_answer(user_answer, correct_answer):
        return {
            "status": "correct",
            "attempts_used": attempts_used,
            "feedback": "Correct! You completed the problem."
        }

    if attempts_used < MAX_ATTEMPTS:
        return {
            "status": "retry",
            "attempts_used": attempts_used,
            "feedback": "Incorrect. You have one try remaining."
        }

    return {
        "status": "revealed",
        "attempts_used": attempts_used,
        "feedback": (
            f"Maximum attempts reached. "
            f"The correct answer is {correct_answer}."
        )
    }


def can_attempt(attempts_used, completed):
    """Determine whether another attempt is allowed."""
    return not completed and attempts_used < MAX_ATTEMPTS
