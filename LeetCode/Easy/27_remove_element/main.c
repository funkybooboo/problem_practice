#include <stdio.h>
#include <stdlib.h>
#include "solution.h"

// Helper function to print the array
void printArray(int* nums, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <array of integers> <value to remove>\n", argv[0]);
        return 1;
    }

    // Last argument is the value to remove
    int val = atoi(argv[argc - 1]);

    // Array of integers is all arguments before the last one
    int numsSize = argc - 2;
    int* nums = (int*)malloc(numsSize * sizeof(int));

    // Parse the integers into the nums array
    for (int i = 0; i < numsSize; i++) {
        nums[i] = atoi(argv[i + 1]);
    }

    // Call the function to remove `val` from `nums`
    int k = removeElement(nums, numsSize, val);

    // Print the result
    printf("Number of elements remaining: %d\n", k);
    printf("Array after removal: ");
    printArray(nums, k);

    // Free the allocated memory for the array
    free(nums);

    return 0;
}
