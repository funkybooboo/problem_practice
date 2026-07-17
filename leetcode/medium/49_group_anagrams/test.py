import unittest

from solution import Solution


class Test(unittest.TestCase):

    def test_1(self):
        result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(result, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    def test_2(self):
        result = Solution().groupAnagrams([""])
        self.assertEqual(result, [[""]])

    def test_3(self):
        result = Solution().groupAnagrams(["a"])
        self.assertEqual(result, [["a"]])


if __name__ == "__main__":
    unittest.main()
