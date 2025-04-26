import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <target> <numbers>")
        return
    target = int(args[1])
    numbers = [int(i) for i in args[2:]]
    print(Solution().twoSum(numbers, target))


if __name__ == "__main__":
    main(sys.argv)
