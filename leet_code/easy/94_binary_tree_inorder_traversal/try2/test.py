import unittest
from solution import Solution
from solution import TreeNode


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        # Input: root = [1,null,2,3]
        root = TreeNode(1)
        root.right = TreeNode(2, left=TreeNode(3))
        expected_output = [1, 3, 2]
        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), expected_output)

    def test_example_2(self):
        # Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
        root = TreeNode(1)
        root.left = TreeNode(
            2, left=TreeNode(4, left=TreeNode(6, left=TreeNode(7)), right=TreeNode(5))
        )
        root.right = TreeNode(3, right=TreeNode(8, left=TreeNode(9)))
        expected_output = [7, 6, 4, 5, 2, 1, 3, 9, 8]
        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), expected_output)

    def test_example_3(self):
        # Input: root = []
        root = None
        expected_output = []
        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), expected_output)

    def test_example_4(self):
        # Input: root = [1]
        root = TreeNode(1)
        expected_output = [1]
        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), expected_output)

    def test_example_5(self):
        # Input: root = [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
        root.right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
        expected_output = [4, 2, 5, 1, 6, 3, 7]
        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), expected_output)

    def test_example_6(self):
        # Input: root = [1,2,3,null,4,5,null]
        root = TreeNode(1)
        root.left = TreeNode(2, right=TreeNode(4))
        root.right = TreeNode(3, right=TreeNode(5))
        expected_output = [2, 4, 1, 3, 5]
        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), expected_output)


if __name__ == "__main__":
    unittest.main()
