import unittest
from solution import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_1(self):
        # Initialize LRUCache with capacity 2
        lru = LRUCache(2)

        # Perform operations
        lru.put(1, 1)              # cache is {1=1}
        lru.put(2, 2)              # cache is {1=1, 2=2}
        self.assertEqual(lru.get(1), 1)    # returns 1

        lru.put(3, 3)              # evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(lru.get(2), -1)   # returns -1 (not found)

        lru.put(4, 4)              # evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(lru.get(1), -1)   # returns -1 (not found)
        self.assertEqual(lru.get(3), 3)    # returns 3
        self.assertEqual(lru.get(4), 4)    # returns 4

    def test_2(self):
        lru = LRUCache(2)
        lru.put(1, 10)
        lru.put(2, 20)
        lru.get(1)                 # access key 1 -> makes key 2 the LRU
        lru.put(3, 30)             # evicts key 2
        self.assertEqual(lru.get(2), -1)
        self.assertEqual(lru.get(1), 10)
        self.assertEqual(lru.get(3), 30)

    def test_3(self):
        lru = LRUCache(2)
        lru.put(1, 10)
        lru.put(2, 20)
        lru.put(1, 15)             # update value of existing key
        self.assertEqual(lru.get(1), 15)
        lru.put(3, 30)             # evicts key 2
        self.assertEqual(lru.get(2), -1)

    def test_4(self):
        lru = LRUCache(1)
        lru.put(1, 1)
        self.assertEqual(lru.get(1), 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(2), 2)


if __name__ == "__main__":
    unittest.main()


