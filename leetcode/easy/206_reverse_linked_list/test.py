import unittest
from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        input_list = [1, 2, 3, 4, 5]
        head = Solution.from_list(input_list)
        reversed_head = Solution().reverseList(head)
        self.assertEqual(Solution.to_list(reversed_head), [5, 4, 3, 2, 1])

    def test_2(self):
        input_list = [1, 2]
        head = Solution.from_list(input_list)
        reversed_head = Solution().reverseList(head)
        self.assertEqual(Solution.to_list(reversed_head), [2, 1])

    def test_3(self):
        input_list = []
        head = Solution.from_list(input_list)
        reversed_head = Solution().reverseList(head)
        self.assertEqual(Solution.to_list(reversed_head), [])

    def test_4(self):
        input_list = [0, 1, 2, 3]
        head = Solution.from_list(input_list)
        reversed_head = Solution().reverseList(head)
        self.assertEqual(Solution.to_list(reversed_head), [3, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()
