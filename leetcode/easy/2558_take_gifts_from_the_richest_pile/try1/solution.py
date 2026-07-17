import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            max_gift_index: int = 0
            for gift_index in range(len(gifts)):
                if gifts[gift_index] > gifts[max_gift_index]:
                    max_gift_index = gift_index
            gifts[max_gift_index] = math.floor(math.sqrt(gifts[max_gift_index]))

        return sum(gifts)
