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

// Test case 1: Removing duplicates from a small array with two duplicate elements
void testRemoveDuplicates_twoDuplicates() {
    int nums[] = {1, 1, 2};
    int expected[] = {1, 2};
    int k = removeDuplicates(nums, 3);

    checkTestResult(k == 2 && nums[0] == expected[0] && nums[1] == expected[1], "Test - Two Duplicates");
}

// Test case 2: Removing duplicates from an array with multiple duplicate elements
void testRemoveDuplicates_multipleDuplicates() {
    int nums[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int expected[] = {0, 1, 2, 3, 4};
    int k = removeDuplicates(nums, 10);

    checkTestResult(k == 5 && nums[0] == expected[0] && nums[1] == expected[1] &&
                    nums[2] == expected[2] && nums[3] == expected[3] && nums[4] == expected[4],
                    "Test - Multiple Duplicates");
}

// Test case 3: Array where all elements are the same
void testRemoveDuplicates_allSameElements() {
    int nums[] = {1, 1, 1, 1, 1};
    int expected[] = {1};
    int k = removeDuplicates(nums, 5);

    checkTestResult(k == 1 && nums[0] == expected[0], "Test - All Same Elements");
}

// Test case 4: Array with several distinct elements and mixed duplicates
void testRemoveDuplicates_distinctAndDuplicates() {
    int nums[] = {1, 2, 2, 3, 3, 3, 4, 5, 5};
    int expected[] = {1, 2, 3, 4, 5};
    int k = removeDuplicates(nums, 9);

    checkTestResult(k == 5 && nums[0] == expected[0] && nums[1] == expected[1] &&
                    nums[2] == expected[2] && nums[3] == expected[3] && nums[4] == expected[4],
                    "Test - Distinct Elements and Mixed Duplicates");
}

// Test case 5: Empty array
void testRemoveDuplicates_emptyArray() {
    int nums[] = {};
    int k = removeDuplicates(nums, 0);

    checkTestResult(k == 0, "Test - Empty Array");
}

// Test case 6: Array with one element
void testRemoveDuplicates_singleElement() {
    int nums[] = {7};
    int expected[] = {7};
    int k = removeDuplicates(nums, 1);

    checkTestResult(k == 1 && nums[0] == expected[0], "Test - Single Element");
}

// Main function to run all the tests
void runTests() {
    testRemoveDuplicates_twoDuplicates();
    testRemoveDuplicates_multipleDuplicates();
    testRemoveDuplicates_allSameElements();
    testRemoveDuplicates_distinctAndDuplicates();
    testRemoveDuplicates_emptyArray();
    testRemoveDuplicates_singleElement();
}

int main() {
    runTests();
    return 0;
}
