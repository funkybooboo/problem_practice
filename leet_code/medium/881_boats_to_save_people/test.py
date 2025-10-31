import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        people = [1, 2]
        limit = 3
        expected_output = 1
        self.assertEqual(solution.numRescueBoats(people, limit), expected_output)

    def test_example_2(self):
        solution = Solution()
        people = [3, 2, 2, 1]
        limit = 3
        expected_output = 3
        self.assertEqual(solution.numRescueBoats(people, limit), expected_output)

    def test_example_3(self):
        solution = Solution()
        people = [3, 5, 3, 4]
        limit = 5
        expected_output = 4
        self.assertEqual(solution.numRescueBoats(people, limit), expected_output)

    def test_example_4(self):
        solution = Solution()
        people = [5, 1, 4, 2]
        limit = 6
        expected_output = 2
        self.assertEqual(solution.numRescueBoats(people, limit), expected_output)

    def test_example_5(self):
        solution = Solution()
        people = [1, 3, 2, 3, 2]
        limit = 3
        expected_output = 4
        self.assertEqual(solution.numRescueBoats(people, limit), expected_output)


if __name__ == "__main__":
    unittest.main()
