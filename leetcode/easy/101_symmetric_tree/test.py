import unittest
from solution import Solution, TreeNode
from typing import Optional, List


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def build_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """Build a binary tree from level-order array representation."""
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            # Left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root

    def test_example_one(self):
        """Test symmetric tree: [1,2,2,3,4,4,3]"""
        root = self.build_tree([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_example_two(self):
        """Test asymmetric tree: [1,2,2,null,3,null,3]"""
        root = self.build_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_single_node(self):
        """Test tree with single node - always symmetric"""
        root = self.build_tree([1])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_two_nodes_symmetric(self):
        """Test tree with two nodes having same value"""
        root = self.build_tree([1, 2, 2])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_two_nodes_asymmetric(self):
        """Test tree with two nodes having different values"""
        root = self.build_tree([1, 2, 3])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_left_heavy_asymmetric(self):
        """Test tree with only left children"""
        root = self.build_tree([1, 2, None, 3])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_right_heavy_asymmetric(self):
        """Test tree with only right children"""
        root = self.build_tree([1, None, 2, None, 3])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_deeper_symmetric_tree(self):
        """Test deeper symmetric tree: [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]"""
        root = self.build_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_deeper_asymmetric_tree(self):
        """Test deeper asymmetric tree where values differ at deeper level"""
        root = self.build_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 9])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_structural_asymmetry(self):
        """Test tree with structural asymmetry (different shapes)"""
        root = self.build_tree([1, 2, 2, None, 3, None, None])  # Fixed!
        self.assertFalse(self.sol.isSymmetric(root))

    def test_symmetric_with_negatives(self):
        """Test symmetric tree with negative values"""
        root = self.build_tree([-1, -2, -2, -3, -4, -4, -3])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_asymmetric_leaf_values(self):
        """Test tree where leaf values don't match"""
        root = self.build_tree([1, 2, 2, 3, 4, 4, 5])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_null_root(self):
        """Test with None root (edge case)"""
        self.assertTrue(self.sol.isSymmetric(None))

    def test_complex_symmetric(self):
        """Test complex symmetric structure"""
        root = self.build_tree(
            [2, 3, 3, 4, 5, 5, 4, None, None, 8, 9, 9, 8, None, None]
        )
        self.assertTrue(self.sol.isSymmetric(root))


if __name__ == "__main__":
    unittest.main()
