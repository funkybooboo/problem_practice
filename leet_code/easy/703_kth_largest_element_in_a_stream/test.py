import unittest
from solution import KthLargest


class TestKthLargest(unittest.TestCase):

    def test_example_1(self):
        kth = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kth.add(3), 4)
        self.assertEqual(kth.add(5), 5)
        self.assertEqual(kth.add(10), 5)
        self.assertEqual(kth.add(9), 8)
        self.assertEqual(kth.add(4), 8)

    def test_example_2(self):
        kth = KthLargest(4, [7, 7, 7, 7, 8, 3])
        self.assertEqual(kth.add(2), 7)
        self.assertEqual(kth.add(10), 7)
        self.assertEqual(kth.add(9), 7)
        self.assertEqual(kth.add(9), 8)

    def test_empty_init(self):
        kth = KthLargest(1, [])
        self.assertEqual(kth.add(5), 5)
        self.assertEqual(kth.add(2), 5)
        self.assertEqual(kth.add(10), 10)

    def test_negative_values(self):
        kth = KthLargest(2, [-10, -20, -30])
        self.assertEqual(kth.add(-5), -10)
        self.assertEqual(kth.add(-25), -10)
        self.assertEqual(kth.add(-1), -5)


if __name__ == "__main__":
    unittest.main()
