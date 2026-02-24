#!/bin/bash

# Usage: ./create.sh <difficulty> "<problem_number>. <Problem Name>"
# Example: ./create.sh easy "496. Next Greater Element I"

set -e

if [ $# -ne 2 ]; then
    echo "Usage: $0 <difficulty> \"<problem_number>. <Problem Name>\""
    echo "Example: $0 easy \"496. Next Greater Element I\""
    exit 1
fi

DIFFICULTY=$1
PROBLEM_FULL=$2

# Extract problem number and name
PROBLEM_NUMBER=$(echo "$PROBLEM_FULL" | grep -oP '^\d+')
PROBLEM_NAME=$(echo "$PROBLEM_FULL" | sed -E 's/^[0-9]+\.\s*//')

# Convert problem name to folder format (lowercase, underscores)
FOLDER_NAME=$(echo "${PROBLEM_NUMBER}_${PROBLEM_NAME}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/_/g' | sed 's/__*/_/g' | sed 's/_$//')

# Create directory path
DIR_PATH="${DIFFICULTY}/${FOLDER_NAME}"

if [ -d "$DIR_PATH" ]; then
    echo "Error: Directory $DIR_PATH already exists"
    exit 1
fi

echo "Creating problem directory: $DIR_PATH"
mkdir -p "$DIR_PATH"

# Create README.md
cat > "$DIR_PATH/README.md" << 'EOF'
# Problem Description

Add problem description here.

EOF

# Create solution.py
cat > "$DIR_PATH/solution.py" << 'EOF'
from typing import List

class Solution:
    def solve(self):
        pass

EOF

# Create test.py
cat > "$DIR_PATH/test.py" << 'EOF'
import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        # Add test case
        pass

if __name__ == "__main__":
    unittest.main()

EOF

echo "Successfully created:"
echo "  - $DIR_PATH/README.md"
echo "  - $DIR_PATH/solution.py"
echo "  - $DIR_PATH/test.py"
