import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().checkInclusion("ab", "eidbaooo")
        self.assertEqual(result, True)

    def test_2(self):
        result = Solution().checkInclusion("ab", "eidboaoo")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
