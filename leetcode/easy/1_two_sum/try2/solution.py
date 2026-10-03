class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m: dict[int, int] = {}  # amount needed to get to target : index to fill the gap
        for i, n in enumerate(nums):
            d: int = target - n
            if d in m:
                return [m[d], i]
            m[n] = i
        return []


# nums = 1 2 3 4 5
# target = 6
#
# m = { }
# i = 0, n = 1
# d = 6 - 1 = 5
# m = { 5: 0 }
# i = 1, n = 2
# d = 6 - 2 = 4
#
