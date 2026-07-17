import unittest

from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Constructing the first tree: [1,3,2,5]
        root1 = TreeNode(1)
        root1.left = TreeNode(3)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(5)

        # Constructing the second tree: [2,1,3,null,4,null,7]
        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)
        root2.left.right = TreeNode(4)
        root2.right.right = TreeNode(7)

        merged_root = self.solution.mergeTrees(root1, root2)

        # Expected output: [3,4,5,5,4,null,7]
        expected_output = [3, 4, 5, 5, 4, None, 7]

        self.assertEqual(self.tree_to_list(merged_root), expected_output)

    def test_example_2(self):
        # Constructing the first tree: [1]
        root1 = TreeNode(1)

        # Constructing the second tree: [1,2]
        root2 = TreeNode(1)
        root2.left = TreeNode(2)

        merged_root = self.solution.mergeTrees(root1, root2)

        # Expected output: [2,2]
        expected_output = [2, 2]

        self.assertEqual(self.tree_to_list(merged_root), expected_output)

    def test_example_3(self):
        # Constructing the first tree: [1]
        root1 = TreeNode(1)

        # Constructing the second tree: [2]
        root2 = TreeNode(2)

        merged_root = self.solution.mergeTrees(root1, root2)

        # Expected output: [3]
        expected_output = [3]

        self.assertEqual(self.tree_to_list(merged_root), expected_output)

    def test_example_4(self):
        # Constructing the first tree: []
        root1 = None

        # Constructing the second tree: [2]
        root2 = TreeNode(2)

        merged_root = self.solution.mergeTrees(root1, root2)

        # Expected output: [2]
        expected_output = [2]

        self.assertEqual(self.tree_to_list(merged_root), expected_output)

    def tree_to_list(self, root):
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result


if __name__ == "__main__":
    unittest.main()
