#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Helper function for backtracking
void backtrack(char** result, int* returnSize, char* current,
               const int openCount, const int closeCount, const int n) {
    // Base case: if we've used n open and n close parentheses, we have a valid
    // combination
    if (openCount == n && closeCount == n) {
        // Make a copy of current string and store it in result
        result[*returnSize] = strdup(current);

        // Check if strdup failed (i.e., memory allocation failure)
        if (result[*returnSize] == NULL) {
            fprintf(stderr,
                    "Memory allocation failed when duplicating string.\n");
            exit(1); // Exit with error code 1 if memory allocation fails
        }

        (*returnSize)++;
        return;
    }

    // Add opening parenthesis if we haven't used n opening parentheses yet
    if (openCount < n) {
        current[openCount + closeCount] = '(';
        backtrack(result, returnSize, current, openCount + 1, closeCount, n);
    }

    // Add closing parenthesis if it doesn't exceed the number of opening
    // parentheses
    if (closeCount < openCount) {
        current[openCount + closeCount] = ')';
        backtrack(result, returnSize, current, openCount, closeCount + 1, n);
    }
}

/**
 * Generates all combinations of well-formed parentheses.
 *
 * @param n The number of pairs of parentheses.
 * @param returnSize Pointer to an integer where the size of the result array
 * will be stored.
 * @return An array of strings representing all valid combinations of
 * parentheses.
 */
char** generateParenthesis(const int n, int* returnSize) {
    // Maximum possible combinations for a given n
    int maxCombinations = 1;
    for (int i = 0; i < n; i++) {
        maxCombinations *= 2 * (2 * i + 1);
        maxCombinations /= (i + 2);
    }

    // Allocate memory for storing results
    char** result = malloc(maxCombinations * sizeof(char*));
    if (result == NULL) {
        fprintf(stderr, "Memory allocation failed for result array.\n");
        exit(1); // Exit if memory allocation for result array fails
    }

    *returnSize = 0;

    // Allocate a temporary string to build combinations (size 2 * n + 1 for the
    // null terminator)
    char* current = malloc((2 * n) + 1);
    if (current == NULL) {
        fprintf(stderr, "Memory allocation failed for current string.\n");
        exit(1); // Exit if memory allocation for current string fails
    }
    current[2 * n] = '\0'; // Null-terminate the string

    // Start the backtracking process
    backtrack(result, returnSize, current, 0, 0, n);

    // Free the temporary string
    free(current);

    return result;
}
