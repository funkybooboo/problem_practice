import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(4), 2)

    def test_example_2(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(8), 2)

    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(9), 3)

    def test_example_4(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(13), 3)


if __name__ == "__main__":
    unittest.main()
