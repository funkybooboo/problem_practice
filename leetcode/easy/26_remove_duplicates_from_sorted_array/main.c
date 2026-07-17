#include <stdio.h>
#include <stdlib.h>
#include "solution.h"

// Function to print the results
void printResults(int* nums, int k) {
    printf("Number of unique elements: %d\n", k);
    printf("Unique elements: ");
    for (int i = 0; i < k; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
}

int main(int argc, char* argv[]) {
    // If no arguments are provided, print a usage message and return
    if (argc < 2) {
        printf("Usage: %s <sorted-integers>\n", argv[0]);
        return 1;
    }

    // Allocate memory for the numbers
    int nums[argc - 1];

    // Convert the command-line arguments to integers
    for (int i = 1; i < argc; i++) {
        nums[i - 1] = atoi(argv[i]);  // Convert string to integer
    }

    // Get the size of the input array
    int numsSize = argc - 1;

    // Call the removeDuplicates function
    int k = removeDuplicates(nums, numsSize);

    // Print the results
    printResults(nums, k);

    return 0;
}
