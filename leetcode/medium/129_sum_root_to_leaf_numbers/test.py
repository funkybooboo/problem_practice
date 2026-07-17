import unittest
from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # Examples from README
    def test_example_1_two_leaf_nodes(self):
        # Tree: [1,2,3] -> paths: 1->2 (12) and 1->3 (13)
        # Expected sum: 12 + 13 = 25
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.sol.sumNumbers(root), 25)

    def test_example_2_three_leaf_nodes(self):
        # Tree: [4,9,0,5,1] -> paths: 4->9->5 (495), 4->9->1 (491), 4->0 (40)
        # Expected sum: 495 + 491 + 40 = 1026
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        self.assertEqual(self.sol.sumNumbers(root), 1026)

    # Edge cases
    def test_single_node_zero(self):
        # Single node with value 0
        root = TreeNode(0)
        self.assertEqual(self.sol.sumNumbers(root), 0)

    def test_single_node_non_zero(self):
        # Single node with value 5
        root = TreeNode(5)
        self.assertEqual(self.sol.sumNumbers(root), 5)

    def test_single_node_max_digit(self):
        # Single node with maximum digit value (9)
        root = TreeNode(9)
        self.assertEqual(self.sol.sumNumbers(root), 9)

    def test_two_nodes_left_only(self):
        # Tree: 1->2 (only left child)
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.sol.sumNumbers(root), 12)

    def test_two_nodes_right_only(self):
        # Tree: 1->3 (only right child)
        root = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(self.sol.sumNumbers(root), 13)

    # Boundary cases
    def test_all_zeros(self):
        # Tree with all zero values: [0,0,0]
        # Paths: 0->0 (0) and 0->0 (0), sum = 0
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        self.assertEqual(self.sol.sumNumbers(root), 0)

    def test_all_nines(self):
        # Tree with all nine values: [9,9,9]
        # Paths: 9->9 (99) and 9->9 (99), sum = 198
        root = TreeNode(9)
        root.left = TreeNode(9)
        root.right = TreeNode(9)
        self.assertEqual(self.sol.sumNumbers(root), 198)

    def test_deep_left_skewed_tree(self):
        # Deep left-skewed tree: 1->2->3->4->5
        # Single path: 12345
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.left.left = TreeNode(5)
        self.assertEqual(self.sol.sumNumbers(root), 12345)

    def test_deep_right_skewed_tree(self):
        # Deep right-skewed tree: 9->8->7->6->5
        # Single path: 98765
        root = TreeNode(9)
        root.right = TreeNode(8)
        root.right.right = TreeNode(7)
        root.right.right.right = TreeNode(6)
        root.right.right.right.right = TreeNode(5)
        self.assertEqual(self.sol.sumNumbers(root), 98765)

    def test_maximum_depth_path(self):
        # Tree with depth 10 (maximum per constraints)
        # Path: 1->2->3->4->5->6->7->8->9->0 = 1234567890
        root = TreeNode(1)
        current = root
        for val in [2, 3, 4, 5, 6, 7, 8, 9, 0]:
            current.left = TreeNode(val)
            current = current.left
        self.assertEqual(self.sol.sumNumbers(root), 1234567890)

    # Domain-specific cases
    def test_complete_binary_tree_depth_3(self):
        # Complete binary tree with 7 nodes
        # Tree: [1,2,3,4,5,6,7]
        # Paths: 1->2->4 (124), 1->2->5 (125), 1->3->6 (136), 1->3->7 (137)
        # Sum: 124 + 125 + 136 + 137 = 522
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.sol.sumNumbers(root), 522)

    def test_unbalanced_tree_more_left_leaves(self):
        # Unbalanced tree with more leaves on left side
        # Tree: root=1, left subtree has 3 leaves, right has 1 leaf
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(6)
        # Paths: 1->2->3->6 (1236), 1->2->4 (124), 1->5 (15)
        # Sum: 1236 + 124 + 15 = 1375
        self.assertEqual(self.sol.sumNumbers(root), 1375)

    def test_tree_with_zeros_in_middle(self):
        # Tree with zeros in middle of paths: [1,0,2]
        # Paths: 1->0 (10) and 1->2 (12)
        # Sum: 10 + 12 = 22
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(2)
        self.assertEqual(self.sol.sumNumbers(root), 22)

    def test_tree_with_leading_zero_path(self):
        # Tree starting with zero: [0,1,2]
        # Paths: 0->1 (01 = 1) and 0->2 (02 = 2)
        # Sum: 1 + 2 = 3
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.sol.sumNumbers(root), 3)

    def test_multiple_paths_same_sum(self):
        # Tree where different paths yield same number
        # Tree: [1,1,2,0,1] -> paths: 1->1->0 (110), 1->1->1 (111), 1->2 (12)
        # Sum: 110 + 111 + 12 = 233
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(1)
        self.assertEqual(self.sol.sumNumbers(root), 233)


if __name__ == "__main__":
    unittest.main()
