import unittest
from solution import Solution, TreeNode

class TestInvertTree(unittest.TestCase):

    def test_example_1(self):
        root = TreeNode(5)
        root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
        root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
        solution = Solution()
        self.assertTrue(solution.hasPathSum(root, 22))

    def test_example_2(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        solution = Solution()
        self.assertFalse(solution.hasPathSum(root, 5))

    def test_example_3(self):
        root = None
        solution = Solution()
        self.assertFalse(solution.hasPathSum(root, 0))

    def test_example_4(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        solution = Solution()
        self.assertTrue(solution.hasPathSum(root, 3))

    def test_example_5(self):
        root = TreeNode(-15, TreeNode(10), TreeNode(20, TreeNode(15), TreeNode(5, None, TreeNode(-5))))
        solution = Solution()
        self.assertFalse(solution.hasPathSum(root, 15))

    def test_example_6(self):
        root = TreeNode(1, TreeNode(1), TreeNode(0, TreeNode(1)))
        solution = Solution()
        self.assertTrue(solution.hasPathSum(root, 2))

if __name__ == "__main__":
    unittest.main()
