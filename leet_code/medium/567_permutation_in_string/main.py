import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <s1> <k2>")
        return
    s1 = args[1]
    s2 = args[2]
    print(Solution().checkInclusion(s1, s2))


if __name__ == "__main__":
    main(sys.argv)
