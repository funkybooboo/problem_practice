import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("hello"), 13)

    def test_example_2(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("zaz"), 50)

    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("code"), 24)

    def test_example_4(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("neetcode"), 65)


if __name__ == "__main__":
    unittest.main()
