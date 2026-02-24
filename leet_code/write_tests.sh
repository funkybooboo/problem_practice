#!/bin/bash

# Usage: ./write_tests.sh <path_to_problem_directory>
# Example: ./write_tests.sh /home/nate/projects/problem_practice/leet_code/easy/496_next_greater_element_i

set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <path_to_problem_directory>"
    echo "Example: $0 /home/nate/projects/problem_practice/leet_code/easy/496_next_greater_element_i"
    exit 1
fi

PROBLEM_DIR=$1

# Verify directory exists
if [ ! -d "$PROBLEM_DIR" ]; then
    echo "Error: Directory $PROBLEM_DIR does not exist"
    exit 1
fi

# Verify required files exist
README="$PROBLEM_DIR/README.md"
SOLUTION="$PROBLEM_DIR/solution.py"
TEST="$PROBLEM_DIR/test.py"

if [ ! -f "$README" ]; then
    echo "Error: README.md not found in $PROBLEM_DIR"
    exit 1
fi

if [ ! -f "$SOLUTION" ]; then
    echo "Error: solution.py not found in $PROBLEM_DIR"
    exit 1
fi

if [ ! -f "$TEST" ]; then
    echo "Error: test.py not found in $PROBLEM_DIR"
    exit 1
fi

# Create the prompt for opencode
PROMPT="Read README.md and solution.py. Overwrite test.py with comprehensive unittest tests covering: examples, edge cases (empty/single/min/max), boundaries, and domain-specific cases. Use descriptive names, add comments for complex cases. Keep unittest structure (TestSolution class, setUp). Only edit test.py. No explanations."

# Run opencode with the files attached using Anthropic Sonnet 4.5 (headless mode)
cd "$PROBLEM_DIR"
opencode run --model anthropic/claude-sonnet-4-5 --format default --file README.md --file solution.py --file test.py -- "$PROMPT" > /dev/null 2>&1

EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
    echo "Error: Test generation failed with exit code $EXIT_CODE" >&2
    exit $EXIT_CODE
fi
