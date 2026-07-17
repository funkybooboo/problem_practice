import unittest
from solution import Solution, TreeNode


class TestIsSubtree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_same_tree(self):
        root = TreeNode.from_list([1, 2, 3])
        subRoot = TreeNode.from_list([1, 2, 3])
        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_different_structure(self):
        root = TreeNode.from_list([1, 2])
        subRoot = TreeNode.from_list([1, None, 2])
        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_different_values(self):
        root = TreeNode.from_list([1, 2, 1])
        subRoot = TreeNode.from_list([1, 1, 2])
        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_both_empty(self):
        self.assertTrue(self.solution.isSubtree(None, None))

    def test_one_empty(self):
        root = TreeNode.from_list([1])
        subRoot = None
        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_example_1(self):
        root = TreeNode.from_list([3, 4, 5, 1, 2])
        subRoot = TreeNode.from_list([4, 1, 2])
        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_example_2(self):
        root = TreeNode.from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
        subRoot = TreeNode.from_list([4, 1, 2])
        self.assertFalse(self.solution.isSubtree(root, subRoot))


if __name__ == "__main__":
    unittest.main()
