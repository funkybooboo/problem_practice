class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m: dict[int, int] = {}  # { amount needed : idx }
        for i, n in enumerate(nums):
            if n in m:
                return [m[n], i]
            m[target - n] = i
        return []
