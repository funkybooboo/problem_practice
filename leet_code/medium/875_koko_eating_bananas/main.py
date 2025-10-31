import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <piles> <h>")
        return
    piles: List[int] = [int(i) for i in args[1 : len(args) - 1]]
    h: int = int(args[len(args) - 1])
    print(Solution().minEatingSpeed(piles, h))


if __name__ == "__main__":
    main(sys.argv)
