from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        triangle: List[List[int]] = [[1], [1, 1]]
        if rowIndex == 0:
            return triangle[0]
        if rowIndex == 1:
            return triangle[1]

        while len(triangle) <= rowIndex:
            lastRow: List[int] = triangle[len(triangle) - 1]
            row: List[int] = [1]
            while len(row) < len(triangle):
                row.append(lastRow[len(row) - 1] + lastRow[len(row)])

            row.append(1)
            triangle.append(row)

        return triangle[rowIndex]
