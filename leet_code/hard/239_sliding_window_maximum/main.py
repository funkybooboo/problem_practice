import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <nums> <k>")
        return
    nums: List[int] = [int(i) for i in args[1 : len(args) - 1]]
    k: int = int(args[len(args) - 1])
    print(Solution().maxSlidingWindow(nums, k))


if __name__ == "__main__":
    main(sys.argv)
