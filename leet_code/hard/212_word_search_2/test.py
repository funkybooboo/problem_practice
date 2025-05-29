import unittest
from solution import Solution

class TestFindWords(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ]
        words = ["oath","pea","eat","rain"]
        expected = ["eat","oath"]
        result = self.solution.findWords(board, words)
        # order of results does not matter
        self.assertCountEqual(result, expected,
            msg=f"Expected {expected} but got {result}")

    def test_example2(self):
        board = [
            ["a","b"],
            ["c","d"]
        ]
        words = ["abcb"]
        expected = []
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, expected,
            msg=f"Expected {expected} but got {result}")

    def test_single_cell(self):
        board = [["a"]]
        words = ["a", "b"]
        expected = ["a"]
        result = self.solution.findWords(board, words)
        self.assertCountEqual(result, expected,
            msg=f"Expected {expected} but got {result}")

if __name__ == "__main__":
    unittest.main()
