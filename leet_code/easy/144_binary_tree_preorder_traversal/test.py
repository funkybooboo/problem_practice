import unittest
from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), [1, 2, 3])

    def test_example_2(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
            TreeNode(3, None, TreeNode(8, None, TreeNode(9))),
        )
        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), [1, 2, 4, 5, 6, 7, 3, 8, 9])

    def test_example_3(self):
        root = None
        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), [])

    def test_example_4(self):
        root = TreeNode(1)
        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), [1])

    def test_example_5(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), [1, 2, 4, 5, 3, 6, 7])

    def test_example_6(self):
        root = TreeNode(
            1, TreeNode(2, None, TreeNode(4, None, TreeNode(5))), TreeNode(3)
        )
        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), [1, 2, 4, 5, 3])


if __name__ == "__main__":
    unittest.main()
