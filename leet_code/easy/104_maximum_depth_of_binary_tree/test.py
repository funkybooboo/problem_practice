import unittest
from solution import Solution, TreeNode


class TestMaxDepth(unittest.TestCase):
    def test_1(self):
        # root = [3,9,20,null,null,15,7] -> depth = 3
        root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        self.assertEqual(Solution().maxDepth(root), 3)

    def test_2(self):
        # root = [1,null,2] -> depth = 2
        root = TreeNode.from_list([1, None, 2])
        self.assertEqual(Solution().maxDepth(root), 2)

    def test_3(self):
        # empty list -> no nodes -> depth = 0
        root = TreeNode.from_list([])
        self.assertEqual(Solution().maxDepth(root), 0)

    def test_4(self):
        # [42] -> just the root -> depth = 1
        root = TreeNode.from_list([42])
        self.assertEqual(Solution().maxDepth(root), 1)

    def test_left_heavy(self):
        # [1,2,None,3] represents:
        #     1
        #    /
        #   2
        #  /
        # 3
        # -> depth = 3
        root = TreeNode.from_list([1, 2, None, 3])
        self.assertEqual(Solution().maxDepth(root), 3)

    def test_5(self):
        # [1,None,2,None,3] represents a right-leaning chain -> depth = 3
        root = TreeNode.from_list([1, None, 2, None, 3])
        self.assertEqual(Solution().maxDepth(root), 3)


if __name__ == "__main__":
    unittest.main()
