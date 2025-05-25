import unittest
from solution import Solution, TreeNode

class TestBuildTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def is_same_tree(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return (
            a.val == b.val and
            self.is_same_tree(a.left, b.left) and
            self.is_same_tree(a.right, b.right)
        )

    def test_example1(self):
        preorder = [3, 9, 20, 15, 7]
        inorder  = [9, 3, 15, 20, 7]
        expected = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        result   = self.solution.buildTree(preorder, inorder)
        self.assertTrue(self.is_same_tree(result, expected))

    def test_example2(self):
        preorder = [-1]
        inorder  = [-1]
        expected = TreeNode.from_list([-1])
        result   = self.solution.buildTree(preorder, inorder)
        self.assertTrue(self.is_same_tree(result, expected))

    def test_empty(self):
        preorder = []
        inorder  = []
        result   = self.solution.buildTree(preorder, inorder)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
