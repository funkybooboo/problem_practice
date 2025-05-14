import unittest
from solution import Solution, TreeNode

class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Input: [3,9,20,null,null,15,7]
        root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        expected = [[3], [9, 20], [15, 7]]
        self.assertEqual(self.solution.levelOrder(root), expected)

    def test_example2(self):
        # Input: [1]
        root = TreeNode.from_list([1])
        expected = [[1]]
        self.assertEqual(self.solution.levelOrder(root), expected)

    def test_empty_tree(self):
        # Input: []
        self.assertEqual(self.solution.levelOrder(None), [])

    def test_left_skewed(self):
        # Input: [1,2,null,3]
        root = TreeNode.from_list([1, 2, None, 3])
        expected = [[1], [2], [3]]
        self.assertEqual(self.solution.levelOrder(root), expected)

    def test_right_skewed(self):
        # Input: [1,null,2,null,3]
        root = TreeNode.from_list([1, None, 2, None, 3])
        expected = [[1], [2], [3]]
        self.assertEqual(self.solution.levelOrder(root), expected)

if __name__ == "__main__":
    unittest.main()
