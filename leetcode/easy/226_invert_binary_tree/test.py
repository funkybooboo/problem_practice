import unittest
from solution import Solution, TreeNode


class TestInvertTree(unittest.TestCase):

    def test_1(self):
        root = TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])
        inverted = Solution().invertTree(root)
        self.assertEqual(TreeNode.to_list(inverted), [4, 7, 2, 9, 6, 3, 1])

    def test_2(self):
        root = TreeNode.from_list([2, 1, 3])
        inverted = Solution().invertTree(root)
        self.assertEqual(TreeNode.to_list(inverted), [2, 3, 1])

    def test_3(self):
        root = TreeNode.from_list([])
        inverted = Solution().invertTree(root)
        self.assertEqual(TreeNode.to_list(inverted), [])

    def test_4(self):
        root = TreeNode.from_list([1])
        inverted = Solution().invertTree(root)
        self.assertEqual(TreeNode.to_list(inverted), [1])


if __name__ == "__main__":
    unittest.main()
