import unittest
from solution import Solution, TreeNode

class TestIsValidBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        # An empty tree is a valid BST
        self.assertTrue(self.solution.isValidBST(None))

    def test_single_node(self):
        # Single node has no children to violate BST properties
        root = TreeNode.from_list([1])
        self.assertTrue(self.solution.isValidBST(root))

    def test_simple_valid_bst(self):
        #    2
        #   / \
        #  1   3
        root = TreeNode.from_list([2, 1, 3])
        self.assertTrue(self.solution.isValidBST(root))

    def test_simple_invalid_bst(self):
        #    5
        #   / \
        #  1   4
        #     / \
        #    3   6
        # 3 is not > 5 so this is not a valid BST
        root = TreeNode.from_list([5, 1, 4, None, None, 3, 6])
        self.assertFalse(self.solution.isValidBST(root))

    def test_subtree_violation(self):
        #    10
        #   /  \
        #  5    15
        #      /  \
        #     6    20
        # 6 is not > 10, so violates the BST constraint
        root = TreeNode.from_list([10, 5, 15, None, None, 6, 20])
        self.assertFalse(self.solution.isValidBST(root))

    def test_left_descendant_violation(self):
        #    8
        #   / \
        #  3   10
        #   \
        #    9    <- 9 is in left subtree of 8 but > 8
        root = TreeNode.from_list([8, 3, 10, None, 9])
        self.assertFalse(self.solution.isValidBST(root))

if __name__ == "__main__":
    unittest.main()
