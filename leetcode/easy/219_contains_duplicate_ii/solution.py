from typing import List, Set


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window: Set[int] = set()

        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[i - k])

        return False
