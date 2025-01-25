from typing import List

class Solution:
    def maxTrap(self, heights: List[int]) -> int:
        if not heights or len(heights) < 3:
            return 0
        m = 0
        for l in range(len(heights) - 2):
            if heights[l] < 1:
                continue
            for r in range(l + 2, len(heights)):
                if heights[r] < 1:
                    continue
                h = min(heights[l], heights[r])
                a = 0
                v = True
                for i in range(l + 1, r):
                    if heights[i] >= h:
                        v = False
                        break
                    a += h - heights[i]
                if v:
                    m = max(m, a)
        return m

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        l_m, r_m = height[l], height[r]
        t = 0
        while l < r:
            if l_m < r_m:
                l += 1
                l_m = max(l_m, height[l])
                t += l_m - height[l]
            else:
                r -= 1
                r_m = max(r_m, height[r])
                t += r_m - height[r]
        return t
