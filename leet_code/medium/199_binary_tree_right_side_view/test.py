import unittest
from solution import Solution, TreeNode

class TestRightSideView(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        root = TreeNode.from_list([1, 2, 3, None, 5, None, 4])
        expected = [1, 3, 4]
        self.assertEqual(self.solution.rightSideView(root), expected)

    def test_example2(self):
        root = TreeNode.from_list([1, 2, 3, 4, None, None, None, 5])
        expected = [1, 3, 4, 5]
        self.assertEqual(self.solution.rightSideView(root), expected)

    def test_example3(self):
        root = TreeNode.from_list([1, None, 3])
        expected = [1, 3]
        self.assertEqual(self.solution.rightSideView(root), expected)

    def test_example4_empty(self):
        root = TreeNode.from_list([])
        expected = []
        self.assertEqual(self.solution.rightSideView(root), expected)

    def test_single_node(self):
        root = TreeNode.from_list([42])
        expected = [42]
        self.assertEqual(self.solution.rightSideView(root), expected)

    def test_left_skewed(self):
        root = TreeNode.from_list([1, 2, None, 3])
        expected = [1, 2, 3]
        self.assertEqual(self.solution.rightSideView(root), expected)

    def test_right_skewed(self):
        root = TreeNode.from_list([1, None, 2, None, 3])
        expected = [1, 2, 3]
        self.assertEqual(self.solution.rightSideView(root), expected)

if __name__ == "__main__":
    unittest.main()
