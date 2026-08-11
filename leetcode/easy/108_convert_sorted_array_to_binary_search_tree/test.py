import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def inorder_traversal(self, root):
        """Helper: Return inorder traversal of tree"""
        result = []
        if root:
            result.extend(self.inorder_traversal(root.left))
            result.append(root.val)
            result.extend(self.inorder_traversal(root.right))
        return result

    def is_valid_bst(self, root, min_val=float("-inf"), max_val=float("inf")):
        """Helper: Check if tree is a valid BST"""
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.is_valid_bst(root.left, min_val, root.val) and self.is_valid_bst(
            root.right, root.val, max_val
        )

    def get_height(self, root):
        """Helper: Get height of tree"""
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def is_height_balanced(self, root):
        """Helper: Check if tree is height-balanced"""
        if not root:
            return True

        def check_height(node):
            if not node:
                return 0
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)

        return check_height(root) != -1

    def test_example_one(self):
        nums = [-10, -3, 0, 5, 9]
        result = self.sol.sortedArrayToBST(nums)

        # Verify inorder traversal gives original sorted array
        self.assertEqual(self.inorder_traversal(result), nums)
        # Verify it's a valid BST
        self.assertTrue(self.is_valid_bst(result))
        # Verify it's height-balanced
        self.assertTrue(self.is_height_balanced(result))

    def test_example_two(self):
        nums = [1, 3]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_height_balanced(result))

    def test_single_element(self):
        nums = [0]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(result.val, 0)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)
        self.assertEqual(self.inorder_traversal(result), nums)

    def test_two_elements(self):
        nums = [1, 2]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_height_balanced(result))

    def test_larger_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_height_balanced(result))
        # Height should be minimal for balanced BST (log2(n) + 1)
        self.assertLessEqual(self.get_height(result), 4)

    def test_all_negative(self):
        nums = [-10, -5, -3, -1]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_height_balanced(result))

    def test_mixed_positive_negative(self):
        nums = [-5, -3, -1, 0, 2, 4, 6]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_height_balanced(result))

    def test_empty_array(self):
        nums = []
        result = self.sol.sortedArrayToBST(nums)

        self.assertIsNone(result)

    def test_power_of_two_minus_one_length(self):
        """Test array of length 7 (2^3 - 1) - perfect balanced tree"""
        nums = [1, 2, 3, 4, 5, 6, 7]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_height_balanced(result))

    def test_duplicates_not_allowed(self):
        """Test that strictly increasing constraint is maintained"""
        # This test verifies the constraint mentioned in the problem
        # nums is sorted in strictly increasing order
        nums = [1, 2, 3, 4, 5]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertTrue(self.is_valid_bst(result))

    def test_large_values(self):
        """Test with values at constraint boundaries"""
        nums = [-10000, 0, 10000]
        result = self.sol.sortedArrayToBST(nums)

        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_height_balanced(result))


if __name__ == "__main__":
    unittest.main()
