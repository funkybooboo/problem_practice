from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            # Compute index from value; subtract 1 because values are in range [1, n]
            # Guaranteed to be in bounds because nums has length n+1 and values are in [1, n]
            idx = abs(num) - 1

            # If the value at this index is already negative, we've seen this number before
            if nums[idx] < 0:
                return abs(num)

            # Mark the index as visited by negating the value at that index
            nums[idx] *= -1

        # Fallback return; problem guarantees at least one duplicate
        return -1
