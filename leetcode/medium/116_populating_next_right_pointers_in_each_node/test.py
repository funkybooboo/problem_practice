import unittest
from solution import Solution, Node


class TestSolution(unittest.TestCase):
    def build_tree(self, values):
        """Build a perfect binary tree from level-order list of values."""
        if not values:
            return None

        root = Node(values[0])
        queue = [root]
        i = 1

        while i < len(values) and queue:
            node = queue.pop(0)

            if i < len(values):
                node.left = Node(values[i])
                queue.append(node.left)
                i += 1

            if i < len(values):
                node.right = Node(values[i])
                queue.append(node.right)
                i += 1

        return root

    def serialize_with_next(self, root):
        """
        Serialize tree with next pointers.
        Returns list with '#' marking end of each level.
        """
        if not root:
            return []

        result = []
        leftmost = root

        # Traverse level by level
        while leftmost:
            current = leftmost
            # Traverse current level using next pointers
            while current:
                result.append(current.val)
                current = current.next
            result.append("#")
            # Move to next level
            leftmost = leftmost.left

        return result

    def test_example1(self):
        """
        Example 1: Tree [1,2,3,4,5,6,7]
        Expected output: [1,#,2,3,#,4,5,6,7,#]
        """
        solution = Solution()
        root = self.build_tree([1, 2, 3, 4, 5, 6, 7])
        result = solution.connect(root)
        serialized = self.serialize_with_next(result)
        expected = [1, "#", 2, 3, "#", 4, 5, 6, 7, "#"]
        self.assertEqual(serialized, expected)

    def test_example2(self):
        """
        Example 2: Empty tree
        Expected output: []
        """
        solution = Solution()
        root = self.build_tree([])
        result = solution.connect(root)
        serialized = self.serialize_with_next(result)
        expected = []
        self.assertEqual(serialized, expected)

    def test_example3(self):
        """
        Example 3: Single node tree [1]
        Expected output: [1,#]
        """
        solution = Solution()
        root = self.build_tree([1])
        result = solution.connect(root)
        serialized = self.serialize_with_next(result)
        expected = [1, "#"]
        self.assertEqual(serialized, expected)


if __name__ == "__main__":
    unittest.main()
