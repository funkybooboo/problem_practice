import unittest

from solution import Solution


class TestSingleNumber(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(Solution().singleNumber([2, 2, 1]), 1)

    def test_example_2(self):
        self.assertEqual(Solution().singleNumber([4, 1, 2, 1, 2]), 4)

    def test_example_3(self):
        self.assertEqual(Solution().singleNumber([1]), 1)

    def test_example_4(self):
        self.assertEqual(Solution().singleNumber([3, 2, 3]), 2)

    def test_example_5(self):
        self.assertEqual(Solution().singleNumber([7, 6, 6, 7, 8]), 8)

if __name__ == "__main__":
    unittest.main()
