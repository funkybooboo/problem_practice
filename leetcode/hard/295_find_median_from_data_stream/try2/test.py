import unittest
from solution import MedianFinder


class TestMedianFinder(unittest.TestCase):
    def test_example(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertAlmostEqual(mf.findMedian(), 1.5, places=5)
        mf.addNum(3)
        self.assertAlmostEqual(mf.findMedian(), 2.0, places=5)

    def test_single_element(self):
        mf = MedianFinder()
        mf.addNum(10)
        self.assertAlmostEqual(mf.findMedian(), 10.0, places=5)

    def test_even_number_of_elements(self):
        mf = MedianFinder()
        for num in [5, 3, 8, 1]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), (3 + 5) / 2, places=5)

    def test_odd_number_of_elements(self):
        mf = MedianFinder()
        for num in [5, 3, 8]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), 5.0, places=5)

    def test_negative_numbers(self):
        mf = MedianFinder()
        for num in [-5, -10, -3]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), -5.0, places=5)

    def test_large_range(self):
        mf = MedianFinder()
        for num in [100000, -100000, 0]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), 0.0, places=5)


if __name__ == "__main__":
    unittest.main()
