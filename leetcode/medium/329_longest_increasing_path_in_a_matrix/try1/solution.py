from typing import List, Tuple, Dict


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(x: int, y: int) -> int:
            if (x, y) in cache:
                return cache[(x, y)]

            longest: int = 1
            if x + 1 < len(matrix) and matrix[x][y] < matrix[x + 1][y]:
                longest = max(dfs(x + 1, y) + 1, longest)
            if x - 1 > -1 and matrix[x][y] < matrix[x - 1][y]:
                longest = max(dfs(x - 1, y) + 1, longest)
            if y + 1 < len(matrix[0]) and matrix[x][y] < matrix[x][y + 1]:
                longest = max(dfs(x, y + 1) + 1, longest)
            if y - 1 > -1 and matrix[x][y] < matrix[x][y - 1]:
                longest = max(dfs(x, y - 1) + 1, longest)

            cache[(x, y)] = longest
            return cache[(x, y)]

        max_longest: int = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                max_longest = max(dfs(x, y), max_longest)
        return max_longest
