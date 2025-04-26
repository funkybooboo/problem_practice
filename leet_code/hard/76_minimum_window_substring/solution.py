from collections import Counter
from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty or longer than s, no valid window exists
        if not t or len(t) > len(s):
            return ""

        # Count the frequency of characters needed from t
        required_chars: Dict[str, int] = Counter(t)
        window_chars: Dict[str, int] = {}

        # Number of unique characters that need to match
        required_matches: int = len(required_chars)
        current_matches: int = 0

        # Result window (start, end) and its length
        min_window: tuple[int, float] = (0, float("inf"))

        left: int = 0
        # Expand the right side of the sliding window
        for right in range(len(s)):
            char: str = s[right]
            window_chars[char] = window_chars.get(char, 0) + 1

            # If the character frequency matches what's required, count it as a match
            if char in required_chars and window_chars[char] == required_chars[char]:
                current_matches += 1

            # Try to shrink the window from the left while it's valid
            while current_matches == required_matches:
                window_length: int = right - left + 1
                if window_length < min_window[1] - min_window[0] + 1:
                    min_window = (left, right)

                # Remove the leftmost character and adjust match count if needed
                left_char: str = s[left]
                window_chars[left_char] -= 1
                if (
                        left_char in required_chars
                        and window_chars[left_char] < required_chars[left_char]
                ):
                    current_matches -= 1

                left += 1

        start, end = min_window
        return s[start:end + 1] if min_window[1] != float("inf") else ""
