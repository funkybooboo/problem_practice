import unittest
from solution import Solution, Node


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        # Create the tree for the first example
        root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        solution = Solution()
        result = solution.postorder(root)
        expected = [5, 6, 3, 2, 4, 1]
        self.assertEqual(result, expected)

    def test_example_2(self):
        # Create the tree for the second example
        root = Node(
            1,
            [
                Node(2, [Node(6, [Node(14)])]),
                Node(3, [Node(7, [Node(11, [Node(12)])])]),
                Node(4, [Node(8, [Node(13)])]),
                Node(5, [Node(9, [Node(10)])]),
            ],
        )
        solution = Solution()
        result = solution.postorder(root)
        expected = [14, 6, 2, 12, 11, 7, 3, 13, 8, 4, 10, 9, 5, 1]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
