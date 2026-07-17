Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:

Input: mat = [[5]]
Output: 5

Example 4:

Input: mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Output: 25

Example 5:

Input: mat = [
    [2,1,3,4],
    [1,2,9,8],
    [10,11,2,3],
    [2,2,2,2]
]
Output: 34

Example 6:

Input: mat = [[1]]
Output: 1


Constraints:

    n == mat.length == mat[i].length
    1 <= n <= 100
    1 <= mat[i][j] <= 100

 