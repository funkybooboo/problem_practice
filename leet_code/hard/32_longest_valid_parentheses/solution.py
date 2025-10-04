class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = [-1]
        max_length = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
            else:
                return 0

        return max_length
