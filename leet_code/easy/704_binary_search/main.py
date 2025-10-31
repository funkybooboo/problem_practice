import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <nums> <target>")
        return
    nums: List[int] = [int(i) for i in args[1 : len(args) - 1]]
    target: int = int(args[len(args) - 1])
    print(Solution().search(nums, target))


if __name__ == "__main__":
    main(sys.argv)
