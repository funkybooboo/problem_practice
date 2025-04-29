import unittest

from solution import Solution, ListNode


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().addTwoNumbers(ListNode.from_list([1,2,3]), ListNode.from_list([4,5,6]))
        self.assertEqual(ListNode.to_list(result), [5,7,9])

    def test_2(self):
        result = Solution().addTwoNumbers(ListNode.from_list([9]), ListNode.from_list([9]))
        self.assertEqual(ListNode.to_list(result), [8,1])

    def test_3(self):
        result = Solution().addTwoNumbers(ListNode.from_list([2,4,3]), ListNode.from_list([5,6,4]))
        self.assertEqual(ListNode.to_list(result), [7,0,8])

    def test_4(self):
        result = Solution().addTwoNumbers(ListNode.from_list([0]), ListNode.from_list([0]))
        self.assertEqual(ListNode.to_list(result), [0])

    def test_5(self):
        result = Solution().addTwoNumbers(ListNode.from_list([9,9,9,9,9,9,9]), ListNode.from_list([9,9,9,9]))
        self.assertEqual(ListNode.to_list(result), [8,9,9,9,0,0,0,1])



if __name__ == "__main__":
    unittest.main()
