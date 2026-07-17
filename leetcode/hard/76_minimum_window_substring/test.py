import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().minWindow("ADOBECODEBANC", "ABC")
        self.assertEqual(result, "BANC")

    def test_2(self):
        result = Solution().minWindow("a", "a")
        self.assertEqual(result, "a")

    def test_3(self):
        result = Solution().minWindow("a", "aa")
        self.assertEqual(result, "")

    def test_4(self):
        result = Solution().minWindow("OUZODYXAZV", "XYZ")
        self.assertEqual(result, "YXAZ")

    def test_5(self):
        result = Solution().minWindow("xyz", "xyz")
        self.assertEqual(result, "xyz")

    def test_6(self):
        result = Solution().minWindow("x", "xy")
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
