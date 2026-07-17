import unittest
from solution import Solution, TreeNode


class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Tree: [6,2,8,0,4,7,9,null,null,3,5]
        root = TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = root.left  # node with val=2
        q = root.right  # node with val=8
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertIs(lca, root)  # LCA should be node 6

    def test_example_2(self):
        # Same tree as example 1
        root = TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = root.left  # node with val=2
        q = root.left.right  # node with val=4
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertIs(lca, p)  # LCA should be node 2

    def test_example_3(self):
        # Tree: [2,1]
        root = TreeNode.from_list([2, 1])
        p = root  # node with val=2
        q = root.left  # node with val=1
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertIs(lca, root)  # LCA should be node 2

    def test_args_order_irrelevant(self):
        # Re-check example 2 but swap p and q
        root = TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = root.left.right  # node with val=4
        q = root.left  # node with val=2
        lca = self.solution.lowestCommonAncestor(root, p, q)
        self.assertIs(lca, q)  # still node 2


if __name__ == "__main__":
    unittest.main()
