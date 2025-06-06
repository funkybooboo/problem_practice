from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def helper(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            helper(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, cur, total)

        helper(0, [], 0)
        return result
