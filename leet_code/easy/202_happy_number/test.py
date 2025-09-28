import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        self.assertTrue(solution.isHappy(19))

    def test_example_2(self):
        solution = Solution()
        self.assertFalse(solution.isHappy(2))

    def test_example_3(self):
        solution = Solution()
        self.assertTrue(solution.isHappy(100))

    def test_example_4(self):
        solution = Solution()
        self.assertFalse(solution.isHappy(101))


if __name__ == "__main__":
    unittest.main()