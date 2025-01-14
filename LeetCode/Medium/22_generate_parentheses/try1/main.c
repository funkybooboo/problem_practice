#include "solution.h"
#include <stdio.h>
#include <stdlib.h>

int main(const int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s <n>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    if (n < 1 || n > 8) {
        printf("n must be between 1 and 8.\n");
        return 1;
    }

    int returnSize = 0;
    char** result = generateParenthesis(n, &returnSize);

    printf("Generated parentheses combinations for n = %d:\n", n);
    for (int i = 0; i < returnSize; i++) {
        printf("%s\n", result[i]);
        free(result[i]); // Free each string after printing
    }

    free(result); // Free the result array
    return 0;
}
