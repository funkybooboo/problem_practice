import unittest
from solution import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        # root = [10,5,15,3,7,null,18], low = 7, high = 15
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.right = TreeNode(18)

        solution = Solution()
        result = solution.rangeSumBST(root, 7, 15)
        self.assertEqual(result, 32)

    def test_example_2(self):
        # root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(18)
        root.left.left.left = TreeNode(1)
        root.left.right.left = TreeNode(6)

        solution = Solution()
        result = solution.rangeSumBST(root, 6, 10)
        self.assertEqual(result, 23)

    def test_example_3(self):
        # root = [5,3,8,1,4,7,9,null,2], low = 3, high = 8
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(8)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.left.right = TreeNode(2)

        solution = Solution()
        result = solution.rangeSumBST(root, 3, 8)
        self.assertEqual(result, 27)

    def test_example_4(self):
        # root = [4,3,5,2,null], low = 2, high = 4
        root = TreeNode(4)
        root.left = TreeNode(3)
        root.right = TreeNode(5)
        root.left.left = TreeNode(2)

        solution = Solution()
        result = solution.rangeSumBST(root, 2, 4)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
