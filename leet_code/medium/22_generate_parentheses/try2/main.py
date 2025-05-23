import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) > 2:
        print("Usage: python main.py <n>")
        return
    n = int(args[1])
    print(Solution().generateParenthesis(n))


if __name__ == "__main__":
    main(sys.argv)
