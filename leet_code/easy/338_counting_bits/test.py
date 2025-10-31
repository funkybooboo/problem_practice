import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.countBits(2), [0, 1, 1])

    def test_example_2(self):
        sol = Solution()
        self.assertEqual(sol.countBits(5), [0, 1, 1, 2, 1, 2])

    def test_example_3(self):
        sol = Solution()
        self.assertEqual(sol.countBits(4), [0, 1, 1, 2, 1])


if __name__ == "__main__":
    unittest.main()
