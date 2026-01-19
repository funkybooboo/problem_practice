import unittest
from solution import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_common_prefix(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "fl")

    def test_no_common_prefix(self):
        strs = ["dog", "racecar", "car"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_single_string(self):
        strs = ["alone"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "alone")

    def test_all_strings_identical(self):
        strs = ["test", "test", "test"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "test")

    def test_common_prefix_entire_shortest_string(self):
        strs = ["interspecies", "interstellar", "interstate"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "inters")

    def test_one_empty_string(self):
        strs = ["abc", "", "ab"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_all_empty_strings(self):
        strs = ["", "", ""]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_mixed_empty_and_non_empty(self):
        strs = ["", "nonempty", ""]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_prefix_is_single_character(self):
        strs = ["a", "ab", "ac"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "a")

    def test_prefix_stops_before_mismatch(self):
        strs = ["prefix", "preform", "prevent"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "pre")

    def test_case_with_short_string_first(self):
        strs = ["go", "gone", "going"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "go")

    def test_case_with_short_string_later(self):
        strs = ["going", "gone", "go"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "go")

    def test_large_input_same_prefix(self):
        strs = ["a" * 200 for _ in range(200)]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "a" * 200)

    def test_large_input_no_prefix(self):
        strs = [chr(97 + i % 26) * 5 for i in range(200)]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_prefix_with_full_overlap_except_last_char(self):
        strs = ["abcdef", "abcdeg", "abcdeh"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "abcde")


if __name__ == "__main__":
    unittest.main()

