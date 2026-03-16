# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

_pick = 0


def guess(num: int) -> int:
    """Mock implementation of the guess API"""
    global _pick
    if num > _pick:
        return -1
    elif num < _pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        min: int = 1
        max: int = n

        while True:
            mid: int = (max + min) // 2
            g: int = guess(mid)

            if g > 0:  # too low
                min = mid + 1
            elif g < 0:  # too high
                max = mid - 1
            else:  # got it
                return mid
