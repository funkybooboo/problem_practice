import unittest
from solution import Solution, ListNode


def build_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        head = build_list([1, 2, 2, 1])
        self.assertTrue(self.s.isPalindrome(head))

    def test_example2(self):
        head = build_list([1, 2])
        self.assertFalse(self.s.isPalindrome(head))

    def test_example3(self):
        head = build_list([1, 2, 3, 2, 1])
        self.assertTrue(self.s.isPalindrome(head))

    def test_example4(self):
        head = build_list([2, 2])
        self.assertTrue(self.s.isPalindrome(head))

    def test_example5(self):
        head = build_list([2, 1])
        self.assertFalse(self.s.isPalindrome(head))


if __name__ == "__main__":
    unittest.main()
