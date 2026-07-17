from typing import List, Dict


class Solution:
    def jump(self, nums: List[int]) -> int:
        failed_code = 1_000_000
        cache: Dict[int, int] = {}
        goal = len(nums) - 1

        def dfs(index: int) -> int:
            nonlocal nums, cache, goal, failed_code
            if index in cache:
                return cache[index]
            if index == goal:
                return 0
            if nums[index] == 0:
                return failed_code

            max_jump: int = nums[index]
            for jump in range(1, max_jump + 1):
                if index + jump <= goal:
                    max_jump = jump

            result: int = failed_code
            for jump in range(1, max_jump + 1):
                result = min(result, dfs(index + jump) + 1)

            cache[index] = result
            return result

        r = dfs(0)
        return r if r != failed_code else 0
