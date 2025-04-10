import unittest

from solution import TimeMap


class TestTimeMap(unittest.TestCase):
    def test_1(self):
        timeMap = TimeMap()
        timeMap.set("foo", "bar", 1)
        self.assertEqual(timeMap.get("foo", 1), "bar")
        self.assertEqual(timeMap.get("foo", 3), "bar")
        timeMap.set("foo", "bar2", 4)
        self.assertEqual(timeMap.get("foo", 4), "bar2")
        self.assertEqual(timeMap.get("foo", 5), "bar2")

    def test_2(self):
        timeMap = TimeMap()
        timeMap.set("alice", "happy", 1)
        self.assertEqual(timeMap.get("alice", 1), "happy")
        self.assertEqual(timeMap.get("alice", 2), "happy")
        timeMap.set("alice", "sad", 3)
        self.assertEqual(timeMap.get("alice", 3), "sad")

    def test_3(self):
        timeMap = TimeMap()
        self.assertEqual(timeMap.get("nonexistent", 1), "")
        timeMap.set("x", "val", 10)
        self.assertEqual(timeMap.get("x", 5), "")

    def test_4(self):
        timeMap = TimeMap()
        timeMap.set("a", "apple", 1)
        timeMap.set("b", "banana", 2)
        timeMap.set("a", "apricot", 3)
        self.assertEqual(timeMap.get("a", 2), "apple")
        self.assertEqual(timeMap.get("a", 3), "apricot")
        self.assertEqual(timeMap.get("b", 2), "banana")

if __name__ == '__main__':
    unittest.main()
