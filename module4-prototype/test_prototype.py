
import unittest

from business_logic import (
    evaluate_attempt,
    check_answer,
    can_attempt
)


class TestDataMan(unittest.TestCase):

def test_correct_answer(self):
    result = evaluate_attempt("15", "15", 0)
    self.assertEqual(result["status"], "completed")
    self.assertTrue(result["completed"])

def test_first_wrong_answer(self):
    result = evaluate_attempt("10", "15", 0)
    self.assertEqual(result["status"], "open")
    self.assertFalse(result["completed"])
    self.assertEqual(result["attempts_used"], 1)

def test_second_wrong_answer(self):
    result = evaluate_attempt("10", "15", 1)
    self.assertEqual(result["status"], "revealed")
    self.assertFalse(result["completed"])
    self.assertEqual(result["attempts_used"], 2)
    
def test_answer_comparison(self):
    self.assertTrue(check_answer("15", "15"))
    self.assertFalse(check_answer("10", "15"))

def test_attempt_limit(self):
    self.assertFalse(can_attempt(2, False))
    self.assertFalse(can_attempt(1, True))
    self.assertTrue(can_attempt(1, False))


if __name__ == "__main__":
    unittest.main()
