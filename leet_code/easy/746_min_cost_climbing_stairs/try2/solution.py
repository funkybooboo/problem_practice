from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        memo = [-1] * (n + 1)

        def count_ways(current_step: int) -> int:
            if current_step >= n:
                return 0
            if memo[current_step] != -1:
                return memo[current_step]

            one_step = count_ways(current_step + 1)
            two_steps = count_ways(current_step + 2)

            memo[current_step] = cost[current_step] + min(one_step, two_steps)
            return memo[current_step]

        return min(count_ways(0), count_ways(1))
