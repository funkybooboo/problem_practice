import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().topKFrequent([1,1,1,2,2,3], 2)
        self.assertEqual(result, [1,2])

    def test_2(self):
        result = Solution().topKFrequent([1], 1)
        self.assertEqual(result, [1])


if __name__ == '__main__':
    unittest.main()

