import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(Solution().subsetXORSum([1, 3]), 6)

    def test_example2(self):
        self.assertEqual(Solution().subsetXORSum([5, 1, 6]), 28)

    def test_example3(self):
        self.assertEqual(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]), 480)

    def test_example4(self):
        self.assertEqual(Solution().subsetXORSum([2, 4]), 12)

    def test_example5(self):
        self.assertEqual(Solution().subsetXORSum([3, 1, 1]), 12)

    def test_single_element(self):
        self.assertEqual(Solution().subsetXORSum([7]), 7)

    def test_all_ones(self):
        self.assertEqual(Solution().subsetXORSum([1, 1, 1, 1]), 8)

    def test_all_twos(self):
        self.assertEqual(Solution().subsetXORSum([2, 2, 2, 2]), 16)


if __name__ == "__main__":
    unittest.main()
