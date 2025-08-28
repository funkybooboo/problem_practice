from typing import List, Dict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        if n == 0:
            return []
        if n == 1:
            return [1]

        last_occurrence: Dict[str, int] = {}
        for i, c in enumerate(s):
            last_occurrence[c] = i

        parts: List[int] = []
        start = 0
        end = 0

        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])
            if i == end:
                parts.append(i - start + 1)
                start = i + 1

        return parts
