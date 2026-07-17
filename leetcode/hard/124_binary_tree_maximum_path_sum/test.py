import unittest
from solution import Solution, TreeNode


class TestMaxPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # [1,2,3]  → best path 2→1→3 = 6
        root = TreeNode.from_list([1, 2, 3])
        self.assertEqual(self.solution.maxPathSum(root), 6)

    def test_example2(self):
        # [-10,9,20,null,null,15,7] → best path 15→20→7 = 42
        root = TreeNode.from_list([-10, 9, 20, None, None, 15, 7])
        self.assertEqual(self.solution.maxPathSum(root), 42)

    def test_single_node(self):
        # single negative node
        root = TreeNode.from_list([-3])
        self.assertEqual(self.solution.maxPathSum(root), -3)

    def test_empty_tree(self):
        # if None is allowed, expect 0
        self.assertEqual(self.solution.maxPathSum(None), 0)


if __name__ == "__main__":
    unittest.main()
