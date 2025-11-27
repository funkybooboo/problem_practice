from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def dfs(i: int, acc: int):
            if i == len(nums):
                return acc
            return (
                    dfs(i + 1, acc) + # skip i
                    dfs(i + 1, acc ^ nums[i]) # take i
            )

        return dfs(0, 0)

# from functools import reduce
#
# class Solution:
#     def subsetXORSum(self, nums):
#         subsets = reduce(
#             lambda acc, x: acc + list(map(lambda y: y ^ x, acc)),
#             nums,
#             [0]
#         )
#         return sum(subsets)

# from functools import reduce
#
# class Solution:
#     def subsetXORSum(self, nums):
#         return sum(
#             reduce(lambda acc, x: acc + [y ^ x for y in acc], nums, [0])
#         )
