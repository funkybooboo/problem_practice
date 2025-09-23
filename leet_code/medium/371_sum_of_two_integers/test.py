import unittest

from solution import Solution

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.getSum(1, 2), 3)

    def test_example_2(self):
        sol = Solution()
        self.assertEqual(sol.getSum(2, 3), 5)

    def test_example_3(self):
        sol = Solution()
        self.assertEqual(sol.getSum(1, 1), 2)

    def test_example_4(self):
        sol = Solution()
        self.assertEqual(sol.getSum(4, 7), 11)

if __name__ == "__main__":
    unittest.main()
