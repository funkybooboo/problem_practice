import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        deadends = ["0201", "0101", "0102", "1212", "2002"]
        target = "0202"
        expected_output = 6
        solution = Solution()
        self.assertEqual(solution.openLock(deadends, target), expected_output)

    def test_example_2(self):
        deadends = ["8888"]
        target = "0009"
        expected_output = 1
        solution = Solution()
        self.assertEqual(solution.openLock(deadends, target), expected_output)

    def test_example_3(self):
        deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
        target = "8888"
        expected_output = -1
        solution = Solution()
        self.assertEqual(solution.openLock(deadends, target), expected_output)

    def test_example_4(self):
        deadends = ["1111", "0120", "2020", "3333"]
        target = "5555"
        expected_output = 20
        solution = Solution()
        self.assertEqual(solution.openLock(deadends, target), expected_output)

    def test_example_5(self):
        deadends = ["4443", "4445", "4434", "4454", "4344", "4544", "3444", "5444"]
        target = "4444"
        expected_output = -1
        solution = Solution()
        self.assertEqual(solution.openLock(deadends, target), expected_output)

if __name__ == '__main__':
    unittest.main()
