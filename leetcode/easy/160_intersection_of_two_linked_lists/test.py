import unittest
from solution import Solution, ListNode


def build_linked_list_with_intersection(listA_vals, listB_vals, skipA, skipB):
    """
    Build two linked lists that intersect at a specific node.
    Returns (headA, headB, intersection_node)
    """
    if not listA_vals or skipA >= len(listA_vals):
        # No intersection case
        headA = build_linked_list(listA_vals)
        headB = build_linked_list(listB_vals)
        return headA, headB, None

    # Build the common tail starting from intersection point
    tail_vals = listA_vals[skipA:]

    # Build the common tail nodes (shared by both lists)
    common_nodes = [ListNode(val) for val in tail_vals]
    for i in range(len(common_nodes) - 1):
        common_nodes[i].next = common_nodes[i + 1]

    # Build list A prefix
    if skipA == 0:
        headA = common_nodes[0]
    else:
        a_nodes = [ListNode(val) for val in listA_vals[:skipA]]
        for i in range(len(a_nodes) - 1):
            a_nodes[i].next = a_nodes[i + 1]
        a_nodes[-1].next = common_nodes[0]
        headA = a_nodes[0]

    # Build list B prefix
    if skipB == 0:
        headB = common_nodes[0]
    else:
        b_nodes = [ListNode(val) for val in listB_vals[:skipB]]
        for i in range(len(b_nodes) - 1):
            b_nodes[i].next = b_nodes[i + 1]
        b_nodes[-1].next = common_nodes[0]
        headB = b_nodes[0]

    return headA, headB, common_nodes[0]


def build_linked_list(vals):
    """Build a simple linked list with no intersection."""
    if not vals:
        return None
    nodes = [ListNode(val) for val in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        # intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
        headA, headB, expected = build_linked_list_with_intersection(
            [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3
        )
        result = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, expected)
        self.assertEqual(result.val, 8)

    def test_example_two(self):
        # intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
        headA, headB, expected = build_linked_list_with_intersection(
            [1, 9, 1, 2, 4], [3, 2, 4], 3, 1
        )
        result = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, expected)
        self.assertEqual(result.val, 2)

    def test_example_three_no_intersection(self):
        # intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
        headA = build_linked_list([2, 6, 4])
        headB = build_linked_list([1, 5])
        result = self.sol.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_intersection_at_head(self):
        # Both lists start at the same node (skipA = skipB = 0)
        headA, headB, expected = build_linked_list_with_intersection(
            [8, 4, 5], [8, 4, 5], 0, 0
        )
        result = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, expected)
        self.assertEqual(result.val, 8)

    def test_one_empty_list(self):
        headA = build_linked_list([1, 2, 3])
        headB = None
        result = self.sol.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_both_empty_lists(self):
        result = self.sol.getIntersectionNode(None, None)
        self.assertIsNone(result)

    def test_intersection_at_last_node(self):
        # Intersection is at the very last node only
        headA, headB, expected = build_linked_list_with_intersection(
            [1, 2, 3], [4, 5, 3], 2, 2
        )
        result = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, expected)
        self.assertEqual(result.val, 3)

    def test_different_lengths_no_intersection(self):
        headA = build_linked_list([1, 2, 3, 4, 5])
        headB = build_linked_list([6, 7, 8])
        result = self.sol.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_single_node_intersection(self):
        # Lists with only the intersection node
        headA, headB, expected = build_linked_list_with_intersection([1], [1], 0, 0)
        result = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, expected)
        self.assertEqual(result.val, 1)


if __name__ == "__main__":
    unittest.main()
