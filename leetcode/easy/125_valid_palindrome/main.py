import sys
from typing import List

from solution import Solution


def main(args: List[str]):
    if len(args) > 2 or len(args) < 2:
        print("Usage: python main.py <string>")
        return
    string = args[1]
    print(Solution().isPalindrome(string))


if __name__ == "__main__":
    main(sys.argv)
