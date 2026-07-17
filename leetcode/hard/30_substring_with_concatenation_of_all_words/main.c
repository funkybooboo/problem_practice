#include "solution.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        printf("Usage: %s <string> <word1> <word2> ...\n", argv[0]);
        return 1;
    }

    char* s = argv[1];
    int wordsSize = argc - 2;
    char** words = &argv[2];

    int returnSize;
    int* result = findSubstring(s, words, wordsSize, &returnSize);

    printf("Indices: ");
    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    free(result);
    return 0;
}