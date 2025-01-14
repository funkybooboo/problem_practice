import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().evalRPN(["2","1","+","3","*"])
        self.assertEqual(result, 9)

    def test_2(self):
        result = Solution().evalRPN(["4","13","5","/","+"])
        self.assertEqual(result, 6)

    def test_3(self):
        result = Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        self.assertEqual(result, 22)

    def test_4(self):
        result = Solution().evalRPN(["1","2","+","3","*","4","-"])
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
