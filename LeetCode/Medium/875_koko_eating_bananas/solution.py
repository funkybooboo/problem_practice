from copy import copy
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1
        s = sum(piles)
        for k in range(1, max(piles) + 1):
            piles_copy = copy(piles)
            i = 0
            e = 0
            for _ in range(h):
                if k >= piles_copy[i]:
                    e += piles_copy[i]
                    piles_copy[i] = 0
                    i += 1
                else:
                    e += k
                    piles_copy[i] -= k

                if e == s:
                    return k
        return -1
