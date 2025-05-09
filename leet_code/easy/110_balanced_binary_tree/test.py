import unittest
from solution import Solution, TreeNode

class TestIsBalanced(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_balanced_tree(self):
        root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        self.assertTrue(self.solution.isBalanced(root))

    def test_unbalanced_tree(self):
        root = TreeNode.from_list([1, 2, 2, 3, 3, None, None, 4, 4])
        self.assertFalse(self.solution.isBalanced(root))

    def test_empty_tree(self):
        root = TreeNode.from_list([])
        self.assertTrue(self.solution.isBalanced(root))

    def test_one_node(self):
        root = TreeNode.from_list([1])
        self.assertTrue(self.solution.isBalanced(root))

    def test_skewed_tree(self):
        root = TreeNode.from_list([1, 2, None, 3, None, 4])
        self.assertFalse(self.solution.isBalanced(root))

if __name__ == "__main__":
    unittest.main()
