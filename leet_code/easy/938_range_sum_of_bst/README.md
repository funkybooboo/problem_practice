Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Example 3:

Input: root = [5,3,8,1,4,7,9,null,2], low = 3, high = 8
Output: 27
Explanation: Nodes 5, 3, 8, 4 and 7 are in the range [3, 8]. 5 + 3 + 8 + 4 + 7 = 27.

Example 4:

Input: root = [4,3,5,2,null], low = 2, high = 4
Output: 9
Explanation: Nodes 4, 3, and 2 are in the range [2, 4]. 4 + 3 + 2 = 9.


Constraints:

    The number of nodes in the tree is in the range [1, 2 * 104].
    1 <= Node.val <= 105
    1 <= low <= high <= 105
    All Node.val are unique.

