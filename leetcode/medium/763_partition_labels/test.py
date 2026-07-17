import unittest
from solution import Solution


class TestPartitionLabels(unittest.TestCase):
    def test_example_1(self):
        # Example 1: s = "ababcbacadefegdehijhklij"
        self.assertEqual(
            Solution().partitionLabels("ababcbacadefegdehijhklij"), [9, 7, 8]
        )

    def test_example_2(self):
        # Example 2: s = "eccbbbbdec"
        self.assertEqual(Solution().partitionLabels("eccbbbbdec"), [10])

    def test_single_letter(self):
        # Single letter string, partition size is 1
        self.assertEqual(Solution().partitionLabels("a"), [1])

    def test_all_same_letter(self):
        # String with all same letters, partition size is length of the string
        self.assertEqual(Solution().partitionLabels("aaaa"), [4])

    def test_no_duplicates(self):
        # String with no duplicate letters, each letter is a separate partition
        self.assertEqual(Solution().partitionLabels("abcdefg"), [1, 1, 1, 1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
