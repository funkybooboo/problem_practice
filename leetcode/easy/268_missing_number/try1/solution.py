from typing import List, Set


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s: Set[int] = set(nums)

        for i in range(len(nums) + 1):
            if i not in s:
                return i

        return -1
