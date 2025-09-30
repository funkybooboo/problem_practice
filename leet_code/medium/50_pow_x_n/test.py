import unittest

from solution import Solution

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        solution = Solution()
        self.assertAlmostEqual(solution.myPow(2.00000, 10), 1024.00000)

    def test_example_2(self):
        solution = Solution()
        self.assertAlmostEqual(solution.myPow(2.10000, 3), 9.26100)

    def test_example_3(self):
        solution = Solution()
        self.assertAlmostEqual(solution.myPow(2.00000, -2), 0.25000)

    def test_example_4(self):
        solution = Solution()
        self.assertAlmostEqual(solution.myPow(2.00000, 5), 32.00000)

    def test_example_5(self):
        solution = Solution()
        self.assertAlmostEqual(solution.myPow(1.10000, 10), 2.59374)

    def test_example_6(self):
        solution = Solution()
        self.assertAlmostEqual(solution.myPow(2.00000, -3), 0.12500)

if __name__ == "__main__":
    unittest.main()
