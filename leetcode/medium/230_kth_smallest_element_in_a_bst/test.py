import unittest
from solution import Solution, TreeNode


class TestKthSmallest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # root = [3,1,4,null,2], k = 1 → 1
        root = TreeNode.from_list([3, 1, 4, None, 2])
        self.assertEqual(self.solution.kthSmallest(root, 1), 1)

    def test_example2(self):
        # root = [5,3,6,2,4,null,null,1], k = 3 → 3
        root = TreeNode.from_list([5, 3, 6, 2, 4, None, None, 1])
        self.assertEqual(self.solution.kthSmallest(root, 3), 3)

    def test_single_node(self):
        root = TreeNode.from_list([42])
        self.assertEqual(self.solution.kthSmallest(root, 1), 42)

    def test_k_equals_n(self):
        # full traversal
        root = TreeNode.from_list([2, 1, 3])
        self.assertEqual(self.solution.kthSmallest(root, 3), 3)

    def test_middle_k(self):
        root = TreeNode.from_list([2, 1, 3])
        self.assertEqual(self.solution.kthSmallest(root, 2), 2)

    def test_left_skewed(self):
        # [3,2,null,1]
        root = TreeNode.from_list([3, 2, None, 1])
        self.assertEqual(self.solution.kthSmallest(root, 2), 2)

    def test_right_skewed(self):
        # [1,null,2,null,3]
        root = TreeNode.from_list([1, None, 2, None, 3])
        self.assertEqual(self.solution.kthSmallest(root, 3), 3)


if __name__ == "__main__":
    unittest.main()
