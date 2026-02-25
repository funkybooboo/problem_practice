import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic(self):
        root = TreeNode(1)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_example_one_or_node_with_and_subtree(self):
        # root = [2,1,3,null,null,0,1]
        # Tree structure:
        #       2 (OR)
        #      / \
        #     1   3 (AND)
        #        / \
        #       0   1
        # Expected: True OR (False AND True) = True OR False = True
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_example_two_single_leaf_false(self):
        # root = [0]
        # Single leaf node with value 0 (False)
        root = TreeNode(0)
        self.assertFalse(self.sol.evaluateTree(root))

    def test_single_leaf_true(self):
        # Single leaf node with value 1 (True)
        root = TreeNode(1)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_or_node_true_or_true(self):
        # Tree: 2 (OR) with children 1, 1
        # Expected: True OR True = True
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_or_node_true_or_false(self):
        # Tree: 2 (OR) with children 1, 0
        # Expected: True OR False = True
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(0)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_or_node_false_or_false(self):
        # Tree: 2 (OR) with children 0, 0
        # Expected: False OR False = False
        root = TreeNode(2)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        self.assertFalse(self.sol.evaluateTree(root))

    def test_and_node_true_and_true(self):
        # Tree: 3 (AND) with children 1, 1
        # Expected: True AND True = True
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_and_node_true_and_false(self):
        # Tree: 3 (AND) with children 1, 0
        # Expected: True AND False = False
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(0)
        self.assertFalse(self.sol.evaluateTree(root))

    def test_and_node_false_and_false(self):
        # Tree: 3 (AND) with children 0, 0
        # Expected: False AND False = False
        root = TreeNode(3)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        self.assertFalse(self.sol.evaluateTree(root))

    def test_nested_or_nodes(self):
        # Tree structure:
        #       2 (OR)
        #      / \
        #     2   0
        #    / \
        #   0   0
        # Expected: (False OR False) OR False = False OR False = False
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(0)
        root.right = TreeNode(0)
        self.assertFalse(self.sol.evaluateTree(root))

    def test_nested_and_nodes(self):
        # Tree structure:
        #       3 (AND)
        #      / \
        #     3   1
        #    / \
        #   1   1
        # Expected: (True AND True) AND True = True AND True = True
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right = TreeNode(1)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_complex_mixed_operations(self):
        # Tree structure:
        #         3 (AND)
        #        / \
        #       2   2 (OR)
        #      / \ / \
        #     1  0 0  1
        # Expected: (True OR False) AND (False OR True) = True AND True = True
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(0)
        root.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_deep_tree_all_or(self):
        # Tree structure:
        #           2 (OR)
        #          / \
        #         2   2
        #        / \ / \
        #       0  0 0  1
        # Expected: (False OR False) OR (False OR True) = False OR True = True
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(0)
        root.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)
        self.assertTrue(self.sol.evaluateTree(root))

    def test_deep_tree_all_and(self):
        # Tree structure:
        #           3 (AND)
        #          / \
        #         3   3
        #        / \ / \
        #       1  1 1  0
        # Expected: (True AND True) AND (True AND False) = True AND False = False
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(0)
        self.assertFalse(self.sol.evaluateTree(root))

if __name__ == "__main__":
    unittest.main()

