import unittest
from solution import Solution

class TestLeastInterval(unittest.TestCase):

    def test_1(self):
        tasks = ["A","A","A","B","B","B"]
        n = 2
        self.assertEqual(Solution().leastInterval(tasks, n), 8)

    def test_2(self):
        tasks = ["A","C","A","B","D","B"]
        n = 1
        self.assertEqual(Solution().leastInterval(tasks, n), 6)

    def test_3(self):
        tasks = ["A","A","A", "B","B","B"]
        n = 3
        self.assertEqual(Solution().leastInterval(tasks, n), 10)

    def test_4(self):
        tasks = ["A"]
        n = 0
        self.assertEqual(Solution().leastInterval(tasks, n), 1)

    def test_5(self):
        tasks = ["A", "A", "B", "B", "C", "C", "D", "D"]
        n = 3
        self.assertEqual(Solution().leastInterval(tasks, n), 8)

    def test_6(self):
        tasks = ["A", "B", "C", "D"]
        n = 1
        self.assertEqual(Solution().leastInterval(tasks, n), 4)

if __name__ == "__main__":
    unittest.main()
