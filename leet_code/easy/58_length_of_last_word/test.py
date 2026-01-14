import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "Hello World"
        self.assertEqual(self.solution.lengthOfLastWord(s), 5)

    def test_example_2(self):
        s = "   fly me   to   the moon  "
        self.assertEqual(self.solution.lengthOfLastWord(s), 4)

    def test_example_3(self):
        s = "luffy is still joyboy"
        self.assertEqual(self.solution.lengthOfLastWord(s), 6)

    def test_single_word(self):
        s = "Hello"
        self.assertEqual(self.solution.lengthOfLastWord(s), 5)

    def test_trailing_spaces(self):
        s = "word     "
        self.assertEqual(self.solution.lengthOfLastWord(s), 4)

    def test_leading_spaces(self):
        s = "     word"
        self.assertEqual(self.solution.lengthOfLastWord(s), 4)

    def test_multiple_spaces_between_words(self):
        s = "a   b   c"
        self.assertEqual(self.solution.lengthOfLastWord(s), 1)

    def test_min_length_string(self):
        s = "a"
        self.assertEqual(self.solution.lengthOfLastWord(s), 1)

if __name__ == "__main__":
    unittest.main()

