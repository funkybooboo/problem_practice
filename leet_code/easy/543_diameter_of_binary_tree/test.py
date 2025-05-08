import unittest
from solution import Solution, TreeNode


class TestDiameterOfBinaryTree(unittest.TestCase):

    def test_1(self):
        root = TreeNode.from_list([1, 2, 3, 4, 5])
        result = Solution().diameterOfBinaryTree(root)
        self.assertEqual(result, 3)

    def test_2(self):
        root = TreeNode.from_list([1, 2])
        result = Solution().diameterOfBinaryTree(root)
        self.assertEqual(result, 1)

    def test_3(self):
        root = TreeNode.from_list([1])
        result = Solution().diameterOfBinaryTree(root)
        self.assertEqual(result, 0)

    def test_4(self):
        root = TreeNode.from_list([])
        result = Solution().diameterOfBinaryTree(root)
        self.assertEqual(result, 0)

    def test_5(self):
        root = TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])
        result = Solution().diameterOfBinaryTree(root)
        self.assertEqual(result, 4)

    def test_6(self):
        root = TreeNode.from_list([1, 2, None, 3, None, 4])
        result = Solution().diameterOfBinaryTree(root)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
