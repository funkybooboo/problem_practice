import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <s> <k>")
        return
    s = args[1]
    k = int(args[2])
    print(Solution().characterReplacement(s, k))


if __name__ == "__main__":
    main(sys.argv)

