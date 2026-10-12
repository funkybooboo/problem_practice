import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test_is_anagram(self):
        self.assertEqual(self.sol.isAnagram("racecar", "carrace"), True)

    def test_is_not_anagram(self):
        self.assertEqual(self.sol.isAnagram("jar", "jam"), False)


if __name__ == "__main__":
    unittest.main()
