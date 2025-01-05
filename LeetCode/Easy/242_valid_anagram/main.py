import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <s> <t>")
        return
    s: str = args[1]
    t: str = args[2]
    print(Solution().isAnagram(s, t))


if __name__ == "__main__":
    main(sys.argv)
