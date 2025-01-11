import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().longestConsecutive([100,4,200,1,3,2])
        self.assertEqual(result, 4)

    def test_2(self):
        result = Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
