import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) == 1:
        print("Usage: python main.py <nums>")
        return
    nums: List[int] = [int(i) for i in args[1:]]
    print(Solution().containsDuplicate(nums))


if __name__ == "__main__":
    main(sys.argv)
