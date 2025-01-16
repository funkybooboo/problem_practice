import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <words>")
        return
    print(Solution().groupAnagrams(args[1:]))


if __name__ == "__main__":
    main(sys.argv)
