import unittest

from solution import Solution


class TestMaxCoins(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.maxCoins([3,1,5,8]), 167)

    def test_example2(self):
        self.assertEqual(self.solution.maxCoins([1,5]), 10)

    def test_single(self):
        self.assertEqual(self.solution.maxCoins([5]), 5)

    def test_all_zeros(self):
        self.assertEqual(self.solution.maxCoins([0,0,0]), 0)

    def test_increasing(self):
        self.assertEqual(self.solution.maxCoins([1,2,3,4]), 40)

    def test_decreasing(self):
        self.assertEqual(self.solution.maxCoins([4,3,2,1]), 40)

    def test_mixed(self):
        self.assertEqual(self.solution.maxCoins([3,1,2,5]), 56)

if __name__ == "__main__":
    unittest.main()
