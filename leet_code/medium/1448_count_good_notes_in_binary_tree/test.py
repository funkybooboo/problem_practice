import unittest
from solution import Solution, TreeNode

class TestGoodNodes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # root = [3,1,4,3,null,1,5] -> 4 good nodes
        root = TreeNode.from_list([3,1,4,3,None,1,5])
        self.assertEqual(self.solution.goodNodes(root), 4)

    def test_example2(self):
        # root = [3,3,null,4,2] -> 3 good nodes
        root = TreeNode.from_list([3,3,None,4,2])
        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_example3(self):
        # root = [1] -> 1 good node
        root = TreeNode.from_list([1])
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_all_increasing(self):
        # every node is ≥ all ancestors -> count == total nodes
        vals = [1,2,3,4,5,6,7]
        root = TreeNode.from_list(vals)
        # total nodes = len(vals)
        self.assertEqual(self.solution.goodNodes(root), len(vals))

    def test_negative_values(self):
        # mix of negatives
        root = TreeNode.from_list([-1, -2, -3, -4, None, None, -1])
        # good nodes: -1 (root), -2? no (root -1 > -2), -3? no, -4? no, -1 (rightmost) yes (-1 ≥ -1)
        self.assertEqual(self.solution.goodNodes(root), 2)

    def test_empty_tree(self):
        self.assertEqual(self.solution.goodNodes(None), 0)

if __name__ == "__main__":
    unittest.main()
