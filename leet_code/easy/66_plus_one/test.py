import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        solution = Solution()
        self.assertEqual(solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_example_2(self):
        solution = Solution()
        self.assertEqual(solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.plusOne([9]), [1, 0])

    def test_example_4(self):
        solution = Solution()
        self.assertEqual(solution.plusOne([1, 2, 3, 4]), [1, 2, 3, 5])

    def test_example_5(self):
        solution = Solution()
        self.assertEqual(solution.plusOne([9, 9, 9]), [1, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()
