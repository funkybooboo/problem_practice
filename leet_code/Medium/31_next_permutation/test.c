#include "solution.h"
#include <stdio.h>
#include <string.h>

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(" ");
    }
    printf("\n");
}

void runTest(int* nums, int numsSize, int* expected, const char* testName) {
    int numsCopy[numsSize];
    memcpy(numsCopy, nums, numsSize * sizeof(int));
    nextPermutation(numsCopy, numsSize);

    int passed = 1;
    for (int i = 0; i < numsSize; i++) {
        if (numsCopy[i] != expected[i]) {
            passed = 0;
            break;
        }
    }

    if (passed) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\nExpected: ", testName);
        printArray(expected, numsSize);
        printf("Got: ");
        printArray(numsCopy, numsSize);
    }
}

int main() {
    int test1[] = {1, 2, 3};
    int expected1[] = {1, 3, 2};
    runTest(test1, 3, expected1, "Test 1");

    int test2[] = {3, 2, 1};
    int expected2[] = {1, 2, 3};
    runTest(test2, 3, expected2, "Test 2");

    int test3[] = {1, 1, 5};
    int expected3[] = {1, 5, 1};
    runTest(test3, 3, expected3, "Test 3");

    return 0;
}
