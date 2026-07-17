#include <stdio.h>
#include "solution.h"

// Helper function to check and print the test result
void checkTestResult(const int condition, const char* testName) {
    if (condition) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\n", testName);
    }
}

// Helper function to print the current array
void printArray(int* nums, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
}

// Test Case 1: Removing elements from array with duplicates
void testCase1() {
    int nums[] = {3, 2, 2, 3};
    int size = 4;
    int val = 3;
    int k = removeElement(nums, size, val);
    checkTestResult(k == 2, "Test Case 1");
    printArray(nums, k); // Should print the elements that are not 3
}

// Test Case 2: Removing an element with more varied values
void testCase2() {
    int nums[] = {0, 1, 2, 2, 3, 0, 4, 2};
    int size = 8;
    int val = 2;
    int k = removeElement(nums, size, val);
    checkTestResult(k == 5, "Test Case 2");
    printArray(nums, k); // Should print 0, 1, 3, 0, 4 (order doesn't matter)
}

// Test Case 3: Edge case of an empty array
void testCase3() {
    int nums[] = {};
    int size = 0;
    int val = 1;
    int k = removeElement(nums, size, val);
    checkTestResult(k == 0, "Test Case 3");
}

// Test Case 4: No elements need to be removed
void testCase4() {
    int nums[] = {1, 2, 3, 4, 5};
    int size = 5;
    int val = 6;
    int k = removeElement(nums, size, val);
    checkTestResult(k == 5, "Test Case 4");
    printArray(nums, k); // Should print 1 2 3 4 5
}

// Test Case 5: All elements are equal to val and should be removed
void testCase5() {
    int nums[] = {2, 2, 2, 2};
    int size = 4;
    int val = 2;
    int k = removeElement(nums, size, val);
    checkTestResult(k == 0, "Test Case 5");
}

// Test Case 6: Single element equal to `val`
void testCase6() {
    int nums[] = {2};
    int size = 1;
    int val = 2;
    int k = removeElement(nums, size, val);
    checkTestResult(k == 0, "Test Case 6");
}

// Test Case 7: Single element not equal to `val`
void testCase7() {
    int nums[] = {3};
    int size = 1;
    int val = 2;
    int k = removeElement(nums, size, val);
    checkTestResult(k == 1, "Test Case 7");
    printArray(nums, k); // Should print 3
}

int main() {
    // Run all test cases
    testCase1();
    testCase2();
    testCase3();
    testCase4();
    testCase5();
    testCase6();
    testCase7();

    return 0;
}
