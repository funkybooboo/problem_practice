import unittest

from solution import Solution


class TestCheckValidString(unittest.TestCase):

    def test_valid_case_1(self):
        result = Solution().checkValidString("()")
        self.assertTrue(result)

    def test_valid_case_2(self):
        result = Solution().checkValidString("(*)")
        self.assertTrue(result)

    def test_valid_case_3(self):
        result = Solution().checkValidString("(*))")
        self.assertTrue(result)

    def test_invalid_case_1(self):
        result = Solution().checkValidString(")(")
        self.assertFalse(result)

    def test_invalid_case_2(self):
        result = Solution().checkValidString("(*)(")
        self.assertFalse(result)

    def test_invalid_case_3(self):
        result = Solution().checkValidString("((*")
        self.assertFalse(result)

    def test_invalid_case_4(self):
        result = Solution().checkValidString("))(")
        self.assertFalse(result)

    def test_invalid_case_5(self):
        result = Solution().checkValidString("(*)*")
        self.assertTrue(result)

    def test_invalid_case_6(self):
        result = Solution().checkValidString("***")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
