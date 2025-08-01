import unittest
from solution import Solution

class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_1(self):
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_n_2(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_n_3(self):
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_n_4(self):
        self.assertEqual(self.solution.climbStairs(4), 5)

    def test_n_5(self):
        self.assertEqual(self.solution.climbStairs(5), 8)

    def test_n_10(self):
        self.assertEqual(self.solution.climbStairs(10), 89)

    def test_n_45(self):
        self.assertEqual(self.solution.climbStairs(45), 1836311903)

if __name__ == "__main__":
    unittest.main()
