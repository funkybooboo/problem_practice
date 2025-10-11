import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("25525511135"), ["255.255.11.135", "255.255.111.35"])

    def test_example_2(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("0000"), ["0.0.0.0"])

    def test_example_3(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("101023"), ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])

    def test_example_4(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("101023"), ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])

    def test_example_5(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("010010"), ["0.10.0.10", "0.100.1.0"])

    def test_example_6(self):
        sol = Solution()
        self.assertEqual(sol.restoreIpAddresses("11111"), ['1.1.1.11', '1.1.11.1', '1.11.1.1', '11.1.1.1'])

if __name__ == '__main__':
    unittest.main()
