import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_is_an_anagram(self):
        result = Solution().isAnagram("anagram", "nagaram")
        self.assertEqual(result, True)

    def test_is_not_an_anagram(self):
        result = Solution().isAnagram("rat", "car")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
