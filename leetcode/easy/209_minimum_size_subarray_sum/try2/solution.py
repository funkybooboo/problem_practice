from typing import List, Optional


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target < 1 or len(nums) == 0:
            return 0

        s_d: Optional[int] = None
        s: int = 0
        l: int = 0

        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                d: int = r - l + 1
                if not s_d or d < s_d:
                    s_d = d
                s -= nums[l]
                l += 1

        return s_d if s_d else 0
