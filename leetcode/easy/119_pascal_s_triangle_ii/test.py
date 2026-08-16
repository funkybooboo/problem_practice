import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        self.assertEqual(self.sol.getRow(3), [1, 3, 3, 1])

    def test_example_two(self):
        self.assertEqual(self.sol.getRow(0), [1])

    def test_example_three(self):
        self.assertEqual(self.sol.getRow(1), [1, 1])

    def test_row_two(self):
        self.assertEqual(self.sol.getRow(2), [1, 2, 1])

    def test_row_four(self):
        self.assertEqual(self.sol.getRow(4), [1, 4, 6, 4, 1])

    def test_row_five(self):
        self.assertEqual(self.sol.getRow(5), [1, 5, 10, 10, 5, 1])


if __name__ == "__main__":
    unittest.main()
