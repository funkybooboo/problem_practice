import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().isPalindrome("Was it a car or a cat I saw?")
        self.assertEqual(result, True)

    def test_2(self):
        result = Solution().isPalindrome("tab a cat")
        self.assertEqual(result, False)

    def test_3(self):
        result = Solution().isPalindrome("0P")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
