import unittest
from solution import Solution, TreeNode

class TestIsSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_same_tree(self):
        p = TreeNode.from_list([1, 2, 3])
        q = TreeNode.from_list([1, 2, 3])
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_different_structure(self):
        p = TreeNode.from_list([1, 2])
        q = TreeNode.from_list([1, None, 2])
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_different_values(self):
        p = TreeNode.from_list([1, 2, 1])
        q = TreeNode.from_list([1, 1, 2])
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_both_empty(self):
        self.assertTrue(self.solution.isSameTree(None, None))

    def test_one_empty(self):
        p = TreeNode.from_list([1])
        q = None
        self.assertFalse(self.solution.isSameTree(p, q))

if __name__ == "__main__":
    unittest.main()
