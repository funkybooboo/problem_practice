import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) > 2:
        print("Usage: python main.py <heights>")
        return
    heights: List[int] = [int(i) for i in args[1:]]
    print(Solution().largestRectangleArea(heights))


if __name__ == "__main__":
    main(sys.argv)
