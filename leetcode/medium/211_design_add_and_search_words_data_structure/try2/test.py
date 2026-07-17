import unittest
from solution import WordDictionary


class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        # Initialize a fresh WordDictionary before each test
        self.d = WordDictionary()

    def test_example_scenario(self):
        # Corresponds to the example in the prompt
        self.d.addWord("bad")
        self.d.addWord("dad")
        self.d.addWord("mad")
        self.assertFalse(
            self.d.search("pad"), msg='Expected search("pad") to return False'
        )
        self.assertTrue(
            self.d.search("bad"), msg='Expected search("bad") to return True'
        )
        self.assertTrue(
            self.d.search(".ad"), msg='Expected search(".ad") to return True'
        )
        self.assertTrue(
            self.d.search("b.."), msg='Expected search("b..") to return True'
        )

    def test_single_character_and_dot(self):
        # Test behavior with single-letter words and wildcard
        self.d.addWord("a")
        self.assertTrue(self.d.search("a"), msg='Expected search("a") to return True')
        self.assertTrue(self.d.search("."), msg='Expected search(".") to return True')
        self.assertFalse(self.d.search("b"), msg='Expected search("b") to return False')

    def test_multiple_wildcards_and_lengths(self):
        # Insert words of different lengths
        for w in ["at", "ate", "atom", "bat"]:
            self.d.addWord(w)
        # Two-letter wildcard
        self.assertTrue(
            self.d.search(".."),
            msg='Expected search("..") to match any two-letter word',
        )
        # Mixed letter and wildcard
        self.assertTrue(
            self.d.search("a.."),
            msg='Expected search("a..") to match "ate" or "atom" truncated',
        )
        self.assertTrue(
            self.d.search(".at"), msg='Expected search(".at") to match "bat" or "at"'
        )

    def test_no_words_added(self):
        # Searching in an empty dictionary should always be False
        self.assertFalse(
            self.d.search(""),
            msg='Expected search("") to return False when no words added',
        )
        self.assertFalse(
            self.d.search("."),
            msg='Expected search(".") to return False when no words added',
        )
        self.assertFalse(
            self.d.search("word"),
            msg='Expected search("word") to return False when no words added',
        )


if __name__ == "__main__":
    unittest.main()
