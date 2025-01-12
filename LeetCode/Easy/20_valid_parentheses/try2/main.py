import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) == 1:
        print("Usage: python main.py <s>")
        return
    s: str= args[1]
    print(Solution().isValid(s))


if __name__ == "__main__":
    main(sys.argv)
