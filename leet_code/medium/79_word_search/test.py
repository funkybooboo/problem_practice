import unittest
from solution import Solution

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word),
                        msg=f"Expected True for word {word} in board")

    def test_example2(self):
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word),
                        msg=f"Expected True for word {word} in board")

    def test_example3(self):
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word),
                         msg=f"Expected False for word {word} in board")

    def test_single_cell_match(self):
        board = [["X"]]
        word = "X"
        self.assertTrue(self.solution.exist(board, word),
                        msg="Expected True when board and word are both a single matching letter")

    def test_single_cell_no_match(self):
        board = [["X"]]
        word = "Y"
        self.assertFalse(self.solution.exist(board, word),
                         msg="Expected False when single-cell board does not match the word")

    def test_empty_word(self):
        board = [["A","B"],["C","D"]]
        word = ""
        # Depending on your spec, you might expect True or False here.
        # If an empty word should always be found, assert True; otherwise False.
        self.assertTrue(self.solution.exist(board, word),
                        msg="Expected True for empty word")

    def test_word_longer_than_cells(self):
        board = [["A","B"],["C","D"]]
        word = "ABCDE"
        self.assertFalse(self.solution.exist(board, word),
                         msg="Expected False when word length exceeds total cells")

if __name__ == "__main__":
    unittest.main()
