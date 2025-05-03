#include "helper.h"
#include "solution.h"

#include <stdio.h>
#include <stdlib.h>

// Helper function to check and print the test result
void verifyTestResult(const int condition, const char* testName) {
    if (condition) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\n", testName);
    }
}

// Test Case 1: Merge Three Sorted Linked Lists
void testMergingThreeSortedLists() {
    const int values1[] = {1, 4, 5};
    const int values2[] = {1, 3, 4};
    const int values3[] = {2, 6};

    struct ListNode* list1 = buildList(values1, 3);
    struct ListNode* list2 = buildList(values2, 3);
    struct ListNode* list3 = buildList(values3, 2);

    struct ListNode* lists[] = {list1, list2, list3};

    const struct ListNode* result = mergeKLists(lists, 3);

    // Expected result: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> NULL
    const int expectedResult[] = {1, 1, 2, 3, 4, 4, 5, 6};
    int i = 0;
    const struct ListNode* temp = result;
    while (temp != NULL) {
        if (temp->val != expectedResult[i]) {
            verifyTestResult(0, "testMergingThreeSortedLists");
            return;
        }
        temp = temp->next;
        i++;
    }
    verifyTestResult(1, "testMergingThreeSortedLists");
}

// Test Case 2: Empty List
void testMergingWithEmptyInput() {
    struct ListNode* lists[] = {NULL};

    const struct ListNode* result = mergeKLists(lists, 0);

    // The expected result is NULL
    if (result == NULL) {
        verifyTestResult(1, "testMergingWithEmptyInput");
    } else {
        verifyTestResult(0, "testMergingWithEmptyInput");
    }
}

// Test Case 3: Single Empty List
void testMergingWithSingleEmptyList() {
    struct ListNode* lists[] = {NULL};

    const struct ListNode* result = mergeKLists(lists, 1);

    // The expected result is NULL
    if (result == NULL) {
        verifyTestResult(1, "testMergingWithSingleEmptyList");
    } else {
        verifyTestResult(0, "testMergingWithSingleEmptyList");
    }
}

// Main function
int main() {
    testMergingThreeSortedLists();
    testMergingWithEmptyInput();
    testMergingWithSingleEmptyList();

    return 0;
}
