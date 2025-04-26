import unittest
from solution import Solution, ListNode


class TestHasCycle(unittest.TestCase):

    def test_example_1(self):
        head = ListNode.to_list_with_cycle([3, 2, 0, -4], 1)
        self.assertTrue(Solution().hasCycle(head))

    def test_example_2(self):
        head = ListNode.to_list_with_cycle([1, 2], 0)
        self.assertTrue(Solution().hasCycle(head))

    def test_example_3(self):
        head = ListNode.to_list_with_cycle([1], -1)
        self.assertFalse(Solution().hasCycle(head))

    def test_empty_list(self):
        head = ListNode.to_list_with_cycle([], -1)
        self.assertFalse(Solution().hasCycle(head))

    def test_single_node_cycle(self):
        head = ListNode.to_list_with_cycle([1], 0)
        self.assertTrue(Solution().hasCycle(head))

    def test_single_node_no_cycle(self):
        head = ListNode.to_list_with_cycle([1], -1)
        self.assertFalse(Solution().hasCycle(head))

    def test_large_list_no_cycle(self):
        values = list(range(10000))
        head = ListNode.to_list_with_cycle(values, -1)
        self.assertFalse(Solution().hasCycle(head))

    def test_large_list_with_cycle(self):
        values = list(range(10000))
        head = ListNode.to_list_with_cycle(values, 123)
        self.assertTrue(Solution().hasCycle(head))


if __name__ == "__main__":
    unittest.main()
