
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "session_data.json"

PROBLEMS = [
    {
        "id": 1,
        "question": "What is 8 + 7?",
        "answer": "15"
    },
    {
        "id": 2,
        "question": "What is 6 x 4?",
        "answer": "24"
    }
]


def get_problem(problem_id=1):
    for problem in PROBLEMS:
        if problem["id"] == problem_id:
            return problem
    return None


def load_session():
    if not DATA_FILE.exists():
        return {
            "problem_id": 1,
            "attempts_used": 0,
            "completed": False
        }

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_session(session):
    with open(DATA_FILE, "w") as file:
        json.dump(session, file, indent=4)


def reset_session():
    session = {
        "problem_id": 1,
        "attempts_used": 0,
        "completed": False
    }
    save_session(session)
    return session
