from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Return the maximum area of an island (connected 4-directionally)
        in the given binary grid.
        """
        # Edge case: empty grid or empty rows
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        # 4-directional moves: down, up, right, left
        directions = [
            (1, 0),  # down
            (-1, 0),  # up
            (0, 1),  # right
            (0, -1),  # left
        ]

        max_area = 0  # largest island seen so far
        current_area = 0  # area of the island we're currently exploring

        def dfs(r: int, c: int) -> None:
            """
            Flood-fill from (r, c), marking visited land cells as water (0)
            and accumulating the size of the current island in `current_area`.
            """
            nonlocal current_area

            # Stop if out of bounds or on water/visited cell
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return

            # Mark this land cell as visited
            grid[r][c] = 0
            current_area += 1

            # Explore all 4 neighboring cells
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Scan every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Found unvisited land: reset counter and explore
                    current_area = 0
                    dfs(r, c)
                    # Update max_area if this island is the largest so far
                    if current_area > max_area:
                        max_area = current_area

        return max_area
