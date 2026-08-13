import unittest
from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def build_tree(self, values):
        """Build a binary tree from level-order list representation (None for null)."""
        if not values:
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
        # Input: root = [3,9,20,null,null,15,7]
        # Tree structure:
        #      3
        #     / \
        #    9  20
        #      /  \
        #     15   7
        # Shortest path: 3 -> 9 (depth 2)
        root = self.build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.sol.minDepth(root), 2)

    def test_example_two(self):
        # Input: root = [2,null,3,null,4,null,5,null,6]
        # Tree structure (right-skewed):
        # 2
        #  \
        #   3
        #    \
        #     4
        #      \
        #       5
        #        \
        #         6
        # Only path has depth 5
        root = self.build_tree([2, None, 3, None, 4, None, 5, None, 6])
        self.assertEqual(self.sol.minDepth(root), 5)

    def test_empty_tree(self):
        # Empty tree has depth 0
        self.assertEqual(self.sol.minDepth(None), 0)

    def test_single_node(self):
        # Single node is a leaf, depth 1
        root = TreeNode(1)
        self.assertEqual(self.sol.minDepth(root), 1)

    def test_left_heavy(self):
        # Tree: [1,2,null,3,null,4]
        #    1
        #   /
        #  2
        # /
        # 3
        # /
        # 4
        root = self.build_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.sol.minDepth(root), 4)

    def test_right_heavy(self):
        # Tree: [1,null,2,null,3,null,4]
        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        root = self.build_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.sol.minDepth(root), 4)

    def test_balanced_tree(self):
        # Tree: [1,2,3,4,5,6,7]
        #      1
        #     / \
        #    2   3
        #   / \  / \
        #  4  5 6  7
        # All leaves at depth 3
        root = self.build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.minDepth(root), 3)

    def test_one_leaf_shallow(self):
        # Tree where left is deep but right is shallow
        # [1,2,3,4,null,null,null]
        #      1
        #     / \
        #    2   3  <- leaf at depth 2
        #   /
        #  4
        root = self.build_tree([1, 2, 3, 4])
        self.assertEqual(self.sol.minDepth(root), 2)


if __name__ == "__main__":
    unittest.main()
