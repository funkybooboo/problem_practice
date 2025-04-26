import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) < 3:
        print("Usage: python main.py <token1> <token2> <...>")
        return
    tokens: List[str] = args[1:]
    print(Solution().evalRPN(tokens))


if __name__ == "__main__":
    main(sys.argv)
