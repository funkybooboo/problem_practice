import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = ["h","e","l","l","o"]
        Solution().reverseString(s)
        self.assertEqual(s, ["o","l","l","e","h"])

    def test_example2(self):
        s = ["H","a","n","n","a","h"]
        Solution().reverseString(s)
        self.assertEqual(s, ["h","a","n","n","a","H"])

    def test_example3(self):
        s = ["n","e","e","t"]
        Solution().reverseString(s)
        self.assertEqual(s, ["t","e","e","n"])

    def test_example4(self):
        s = ["r","a","c","e","c","a","r"]
        Solution().reverseString(s)
        self.assertEqual(s, ["r","a","c","e","c","a","r"])


if __name__ == "__main__":
    unittest.main()
