from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1

        return count
