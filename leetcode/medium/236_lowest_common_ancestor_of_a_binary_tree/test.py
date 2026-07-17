import unittest
from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def build_tree_from_list(self, values):
        """Helper to build binary tree from level-order list representation."""
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def find_node(self, root, val):
        """Helper to find a node with given value in the tree."""
        if not root:
            return None
        if root.val == val:
            return root
        
        left = self.find_node(root.left, val)
        if left:
            return left
        
        return self.find_node(root.right, val)

    # Example test cases from README
    def test_example_1_lca_of_5_and_1(self):
        """Example 1: LCA of nodes 5 and 1 in tree [3,5,1,6,2,0,8,null,null,7,4] is 3."""
        root = self.build_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = self.find_node(root, 5)
        q = self.find_node(root, 1)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 3)

    def test_example_2_lca_of_5_and_4(self):
        """Example 2: LCA of nodes 5 and 4 is 5 (node can be ancestor of itself)."""
        root = self.build_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = self.find_node(root, 5)
        q = self.find_node(root, 4)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 5)

    def test_example_3_minimal_tree(self):
        """Example 3: LCA in minimal tree [1,2] where p=1, q=2 is 1."""
        root = self.build_tree_from_list([1, 2])
        p = self.find_node(root, 1)
        q = self.find_node(root, 2)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 1)

    # Edge cases - minimum tree size
    def test_two_node_tree_right_child(self):
        """Minimal tree with right child: [1, null, 2]."""
        root = self.build_tree_from_list([1, None, 2])
        p = self.find_node(root, 1)
        q = self.find_node(root, 2)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 1)

    # Edge cases - one node is ancestor of the other
    def test_p_is_ancestor_of_q(self):
        """When p is an ancestor of q, LCA should be p."""
        root = self.build_tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = self.find_node(root, 2)
        q = self.find_node(root, 4)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    def test_q_is_ancestor_of_p(self):
        """When q is an ancestor of p, LCA should be q."""
        root = self.build_tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = self.find_node(root, 3)
        q = self.find_node(root, 2)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    def test_root_is_one_of_the_nodes(self):
        """When one of p or q is the root itself."""
        root = self.build_tree_from_list([3, 5, 1, 6, 2, 0, 8])
        p = self.find_node(root, 3)
        q = self.find_node(root, 5)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 3)

    # Boundary cases - nodes at different depths
    def test_nodes_at_same_depth_different_subtrees(self):
        """Nodes at same depth but in different subtrees."""
        root = self.build_tree_from_list([6, 2, 8, 0, 4, 7, 9])
        p = self.find_node(root, 0)
        q = self.find_node(root, 7)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 6)

    def test_nodes_at_different_depths(self):
        """Nodes at very different depths in the tree."""
        root = self.build_tree_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        p = self.find_node(root, 8)  # Deep left
        q = self.find_node(root, 3)  # Shallow right
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 1)

    def test_leaf_nodes_same_parent(self):
        """Two leaf nodes with the same immediate parent."""
        root = self.build_tree_from_list([6, 2, 8, 0, 4, 7, 9])
        p = self.find_node(root, 7)
        q = self.find_node(root, 9)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 8)

    # Domain-specific cases - skewed trees
    def test_left_skewed_tree(self):
        """Left-skewed tree (essentially a linked list to the left)."""
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(2)
        root.left.left.left.left = TreeNode(1)
        
        p = self.find_node(root, 5)
        q = self.find_node(root, 1)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 5)

    def test_right_skewed_tree(self):
        """Right-skewed tree (essentially a linked list to the right)."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        
        p = self.find_node(root, 2)
        q = self.find_node(root, 5)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    # Boundary cases - extreme values
    def test_negative_values(self):
        """Tree with negative node values."""
        root = self.build_tree_from_list([-10, -5, -15, -3, -7, -12, -20])
        p = self.find_node(root, -3)
        q = self.find_node(root, -7)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, -5)

    def test_large_values(self):
        """Tree with large node values (near constraint limit)."""
        root = self.build_tree_from_list([1000000000, 500000000, -1000000000])
        p = self.find_node(root, 500000000)
        q = self.find_node(root, -1000000000)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 1000000000)

    def test_mixed_positive_negative_values(self):
        """Tree with mix of positive and negative values."""
        root = self.build_tree_from_list([0, -5, 5, -10, -2, 2, 10])
        p = self.find_node(root, -10)
        q = self.find_node(root, 10)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 0)

    # Domain-specific - complete binary tree
    def test_complete_binary_tree(self):
        """Complete binary tree with all levels filled."""
        root = self.build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
        p = self.find_node(root, 4)
        q = self.find_node(root, 6)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 1)

    def test_siblings_in_left_subtree(self):
        """Both nodes are siblings in the left subtree."""
        root = self.build_tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = self.find_node(root, 0)
        q = self.find_node(root, 4)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    def test_siblings_in_right_subtree(self):
        """Both nodes are siblings in the right subtree."""
        root = self.build_tree_from_list([6, 2, 8, 0, 4, 7, 9])
        p = self.find_node(root, 7)
        q = self.find_node(root, 9)
        result = self.sol.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 8)


if __name__ == "__main__":
    unittest.main()
