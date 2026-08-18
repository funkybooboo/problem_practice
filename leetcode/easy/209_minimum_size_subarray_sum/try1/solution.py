from typing import List, Optional


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target < 1 or len(nums) == 0:
            return 0

        s_d: Optional[int] = None
        for i, n in enumerate(nums):
            d: int = 1
            v: int = n
            if (not s_d and v >= target) or (s_d and d < s_d and v >= target):
                s_d = d
            prev_v: int = n
            for j in range(i - 1, -1, -1):
                d: int = i - j + 1
                v: int = prev_v + nums[j]
                prev_v = v
                if (not s_d and v >= target) or (s_d and d < s_d and v >= target):
                    s_d = d

        if s_d:
            return s_d

        return 0
