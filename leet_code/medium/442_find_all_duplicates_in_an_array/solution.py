from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        r: List[int] = []

        i: int = 0
        while i < len(nums):
            n: int = abs(nums[i])
            n_index: int = n - 1

            if nums[n_index] < 0:
                r.append(n)
            else:
                nums[n_index] *= -1

            i += 1

        return r
