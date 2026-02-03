from typing import List, Dict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts: Dict[int, int] = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        return max(counts, key=counts.get)

