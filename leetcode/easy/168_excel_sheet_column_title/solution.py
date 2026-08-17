class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return self._to_base(columnNumber, base=26, offset=1)

    def _to_base(self, n: int, base: int, offset: int) -> str:
        # Base case: below the minimum representable number
        if n < offset:
            return ""

        # Normalize to 0-indexed for the math to work
        normalized: int = n - offset

        # Split: higher digits, and current digit
        higher: int = normalized // base
        current: int = normalized % base

        # Current digit to letter
        letter: str = chr(ord("A") + current)

        # If no higher digits, done. Else recurse and prepend.
        return letter if higher == 0 else self._to_base(higher, base, offset) + letter
