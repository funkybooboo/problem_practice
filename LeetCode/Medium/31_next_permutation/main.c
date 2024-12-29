#include "solution.h"
#include <stdio.h>
#include <stdlib.h>

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(" ");
    }
    printf("\n");
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s num1 num2 ... numN\n", argv[0]);
        return 1;
    }

    int numsSize = argc - 1;
    int* nums = malloc(numsSize * sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        nums[i] = atoi(argv[i + 1]);
    }

    printf("Original Array: ");
    printArray(nums, numsSize);

    nextPermutation(nums, numsSize);

    printf("Next Permutation: ");
    printArray(nums, numsSize);

    free(nums);
    return 0;
}
