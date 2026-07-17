import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_front_back_duplicates(self):
        result = Solution().isValid("[]")
        self.assertEqual(result, True)

    def test_middle_duplicates(self):
        result = Solution().isValid("([{}])")
        self.assertEqual(result, True)

    def test_no_duplicates(self):
        result = Solution().isValid("[(])")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
