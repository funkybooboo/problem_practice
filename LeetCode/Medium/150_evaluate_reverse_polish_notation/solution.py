from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack[-2] += stack[-1]
                stack.pop()
            elif t == "-":
                stack[-2] -= stack[-1]
                stack.pop()
            elif t == "*":
                stack[-2] *= stack[-1]
                stack.pop()
            elif t == "/":
                a, b = stack[-2], stack[-1]
                stack.pop()
                stack[-1] = int(a / b)
            else:
                stack.append(int(t))
        return stack[0]  # Only one item should be left on the stack
