import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        expected = [3, 2, 1]
        self.assertEqual(Solution().postorderTraversal(root), expected)

    def test_example_2(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6), TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(8, TreeNode(9))))
        expected = [6, 7, 4, 5, 2, 9, 8, 3, 1]
        self.assertEqual(Solution().postorderTraversal(root), expected)

    def test_example_3(self):
        root = None
        expected = []
        self.assertEqual(Solution().postorderTraversal(root), expected)

    def test_example_4(self):
        root = TreeNode(1)
        expected = [1]
        self.assertEqual(Solution().postorderTraversal(root), expected)

    def test_example_5(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        expected = [4, 5, 2, 6, 7, 3, 1]
        self.assertEqual(Solution().postorderTraversal(root), expected)

    def test_example_6(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(4, TreeNode(5))), TreeNode(3))
        expected = [5, 4, 2, 3, 1]
        self.assertEqual(Solution().postorderTraversal(root), expected)

if __name__ == "__main__":
    unittest.main()
