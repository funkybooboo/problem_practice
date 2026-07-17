import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    # --- Provided Examples ---
    def test_example1(self):
        logs = ["d1/","d2/","../","d21/","./"]
        self.assertEqual(Solution().minOperations(logs), 2)

    def test_example2(self):
        logs = ["d1/","d2/","./","d3/","../","d31/"]
        self.assertEqual(Solution().minOperations(logs), 3)

    def test_example3(self):
        logs = ["d1/","../","../","../"]
        self.assertEqual(Solution().minOperations(logs), 0)

    def test_example4(self):
        logs = ["d1/","d2/","../","d21/","./"]
        self.assertEqual(Solution().minOperations(logs), 2)

    def test_example5(self):
        logs = ["d1/","../","../","../"]
        self.assertEqual(Solution().minOperations(logs), 0)

    def test_example6(self):
        logs = ["d1/","d2/","../","d3/","../","d4/","../","d5/"]
        self.assertEqual(Solution().minOperations(logs), 2)

    # --- Additional Edge Cases ---

    # Only "./" operations
    def test_all_current_directory(self):
        logs = ["./", "./", "./"]
        self.assertEqual(Solution().minOperations(logs), 0)

    # Only "../" operations
    def test_all_parent_from_root(self):
        logs = ["../", "../", "../"]
        self.assertEqual(Solution().minOperations(logs), 0)

    # Single child folder
    def test_single_child(self):
        logs = ["a/"]
        self.assertEqual(Solution().minOperations(logs), 1)

    # Deep nested path, no "../"
    def test_deep_nested(self):
        logs = ["a/","b/","c/","d/","e/"]
        self.assertEqual(Solution().minOperations(logs), 5)

    # Repeated up-down operations cancel each other
    def test_up_down_balance(self):
        logs = ["a/","../","b/","../","c/","../"]
        self.assertEqual(Solution().minOperations(logs), 0)

    # Complex mix ensuring never below root
    def test_mixed_never_below_root(self):
        logs = ["../","a/","../","../","b/","c/","../","./"]
        # Steps:
        # "../" -> stay at root
        # "a/" -> depth 1
        # "../" -> depth 0
        # "../" -> depth 0
        # "b/" -> depth 1
        # "c/" -> depth 2
        # "../" -> depth 1
        # "./" -> depth 1
        self.assertEqual(Solution().minOperations(logs), 1)

    # Folder names containing digits
    def test_folder_names_with_digits(self):
        logs = ["x1/", "x2/", "../", "x3/"]
        # depth = 2
        self.assertEqual(Solution().minOperations(logs), 2)

    # "." in folder names but not "./"
    def test_folder_name_contains_dot(self):
        logs = ["a./", "b./", "../"]
        # a. -> depth 1
        # b. -> depth 2
        # ../ -> depth 1
        self.assertEqual(Solution().minOperations(logs), 1)


if __name__ == "__main__":
    unittest.main()
