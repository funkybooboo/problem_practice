import unittest

from try2.solution import Solution


class TestLongestIncreasingPath(unittest.TestCase):
    def test_1(self):
        result = Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
        self.assertEqual(result, 4)  # [1,2,6,9]

    def test_2(self):
        result = Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
        self.assertEqual(result, 4)  # [3,4,5,6]

    def test_3(self):
        result = Solution().longestIncreasingPath([])
        self.assertEqual(result, 0)  #

    def test_4(self):
        result = Solution().longestIncreasingPath([[7,7,7],[7,7,7],[7,7,7]])
        self.assertEqual(result, 1)  # all elements equal, only paths length 1

    def test_5(self):
        result = Solution().longestIncreasingPath([[1,2,3],[6,5,4],[7,8,9]])
        self.assertEqual(result, 9)  # spiral increasing path

if __name__ == "__main__":
    unittest.main()
