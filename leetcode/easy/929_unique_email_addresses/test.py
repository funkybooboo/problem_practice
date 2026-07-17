import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_basic(self):
        emails = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@leetcode.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_multiple_domains(self):
        emails = [
            "a@leetcode.com",
            "b@leetcode.com",
            "a@leetcode.org",
            "a@leetcode.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 3)

    def test_plus_handling(self):
        emails = [
            "user+spam@gmail.com",
            "user+work@gmail.com",
            "user@gmail.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_dot_handling(self):
        emails = [
            "u.ser@gmail.com",
            "us.er@gmail.com",
            "user@gmail.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_dot_and_plus_combined(self):
        emails = [
            "u.s.e.r+spam@gmail.com",
            "user+work@gmail.com",
            "u.s.e.r@gmail.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_no_special_characters(self):
        emails = [
            "alice@example.com",
            "bob@example.com",
            "charlie@example.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 3)

    def test_same_local_different_domain(self):
        emails = [
            "user@gmail.com",
            "user@yahoo.com",
            "user@outlook.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 3)

    def test_multiple_at_symbols_not_present(self):
        emails = [
            "simple@example.com",
            "simple+test@example.com",
            "si.mple@example.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_single_email(self):
        emails = ["only.one@domain.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_empty_local_after_plus(self):
        emails = [
            "a+@example.com",
            "a@example.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_large_input_duplicates(self):
        base = "user.name+spam@gmail.com"
        emails = [base for _ in range(1000)]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_case_sensitivity_preserved(self):
        emails = [
            "User@gmail.com",
            "user@gmail.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 2)


if __name__ == "__main__":
    unittest.main()

