import unittest
from solution import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        # Initialize a fresh trie before each test
        self.trie = Trie()

    def test_insert_and_search(self):
        # After inserting "apple", search("apple") should be True,
        # but search("app") should still be False.
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"),
                        msg='Expected search("apple") to return True after insert')
        self.assertFalse(self.trie.search("app"),
                         msg='Expected search("app") to return False before inserting "app"')

    def test_startsWith(self):
        # startsWith("app") should be True after inserting "apple"
        self.trie.insert("apple")
        self.assertTrue(self.trie.startsWith("app"),
                        msg='Expected startsWith("app") to return True')
        # And a non‐existent prefix should return False
        self.assertFalse(self.trie.startsWith("aplz"),
                         msg='Expected startsWith("aplz") to return False')

    def test_insert_prefix_and_search(self):
        # Insert "apple", confirm "app" is not found, then insert "app"
        # and confirm search("app") becomes True.
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("app"),
                         msg='Expected search("app") to return False before inserting "app"')
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"),
                        msg='Expected search("app") to return True after inserting "app"')

if __name__ == "__main__":
    unittest.main()
