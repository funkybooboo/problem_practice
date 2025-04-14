#include <stdio.h>
#include "solution.h"
#include "helper.h"


// Helper function to check and print the test result
void checkTestResult(const int condition, const char* testName) {
    if (condition) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\n", testName);
    }
}

// Test Case 1: Merging two non-empty lists
void testMergeTwoNonEmptyLists() {
    int list1Arr[] = {1, 2, 4};
    int list2Arr[] = {1, 3, 4};
    struct ListNode* list1 = createList(list1Arr, 3);
    struct ListNode* list2 = createList(list2Arr, 3);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {1, 1, 2, 3, 4, 4};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeTwoNonEmptyLists");
        temp = temp->next;
        i++;
    }
}

// Test Case 2: Merging one empty list and one non-empty list
void testMergeOneEmptyList() {
    int list1Arr[] = {0};
    struct ListNode* list1 = createList(list1Arr, 1);
    const struct ListNode* result = mergeTwoLists(NULL, list1);
    const int expected[] = {0};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeOneEmptyList");
        temp = temp->next;
        i++;
    }
}

// Test Case 3: Merging two empty lists
void testMergeTwoEmptyLists() {
    const struct ListNode* result = mergeTwoLists(NULL, NULL);
    checkTestResult(result == NULL, "testMergeTwoEmptyLists");
}

// Test Case 4: Merging a list with a single element and an empty list
void testMergeSingleElementWithEmptyList() {
    int list1Arr[] = {5};
    struct ListNode* list1 = createList(list1Arr, 1);
    const struct ListNode* result = mergeTwoLists(list1, NULL);
    const int expected[] = {5};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeSingleElementWithEmptyList");
        temp = temp->next;
        i++;
    }
}

// Test Case 5: Merging two lists where one list has only one element
void testMergeSingleElementLists() {
    int list1Arr[] = {1};
    int list2Arr[] = {2};
    struct ListNode* list1 = createList(list1Arr, 1);
    struct ListNode* list2 = createList(list2Arr, 1);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {1, 2};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeSingleElementLists");
        temp = temp->next;
        i++;
    }
}

// Test Case 6: Merging two lists of the same length
void testMergeTwoListsOfSameLength() {
    int list1Arr[] = {1, 3, 5};
    int list2Arr[] = {2, 4, 6};
    struct ListNode* list1 = createList(list1Arr, 3);
    struct ListNode* list2 = createList(list2Arr, 3);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {1, 2, 3, 4, 5, 6};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeTwoListsOfSameLength");
        temp = temp->next;
        i++;
    }
}

// Test Case 7: Merging a sorted list with duplicate values
void testMergeListsWithDuplicates() {
    int list1Arr[] = {1, 3, 3, 5};
    int list2Arr[] = {2, 3, 4, 6};
    struct ListNode* list1 = createList(list1Arr, 4);
    struct ListNode* list2 = createList(list2Arr, 4);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {1, 2, 3, 3, 3, 4, 5, 6};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeListsWithDuplicates");
        temp = temp->next;
        i++;
    }
}

// Test Case 8: Merging two lists with different sizes
void testMergeListsWithDifferentSizes() {
    int list1Arr[] = {1, 2};  // List 1 has 2 elements
    int list2Arr[] = {3, 4, 5, 6};  // List 2 has 4 elements
    struct ListNode* list1 = createList(list1Arr, 2);
    struct ListNode* list2 = createList(list2Arr, 4);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {1, 2, 3, 4, 5, 6};  // The merged list should be sorted

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeListsWithDifferentSizes");
        temp = temp->next;
        i++;
    }
}

// Test Case 9: Merging two lists where one list has elements larger than the other
void testMergeListsWithLargerElements() {
    int list1Arr[] = {1, 2, 3};  // Smaller elements
    int list2Arr[] = {10, 20, 30};  // Larger elements
    struct ListNode* list1 = createList(list1Arr, 3);
    struct ListNode* list2 = createList(list2Arr, 3);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {1, 2, 3, 10, 20, 30};  // The merged list should be sorted

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeListsWithLargerElements");
        temp = temp->next;
        i++;
    }
}

// Test Case 10: Merging lists with negative numbers
void testMergeListsWithNegativeNumbers() {
    int list1Arr[] = {-5, -3, -1};
    int list2Arr[] = {-6, -4, -2};
    struct ListNode* list1 = createList(list1Arr, 3);
    struct ListNode* list2 = createList(list2Arr, 3);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {-6, -5, -4, -3, -2, -1};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeListsWithNegativeNumbers");
        temp = temp->next;
        i++;
    }
}

// Test Case 11: Merging lists with all equal elements
void testMergeListsWithEqualElements() {
    int list1Arr[] = {1, 1, 1};
    int list2Arr[] = {1, 1, 1};
    struct ListNode* list1 = createList(list1Arr, 3);
    struct ListNode* list2 = createList(list2Arr, 3);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {1, 1, 1, 1, 1, 1};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeListsWithEqualElements");
        temp = temp->next;
        i++;
    }
}

// Test Case 12: Merging two lists of very large size (upper bound test)
void testMergeLargeLists() {
    int list1Arr[50];
    int list2Arr[50];

    for (int i = 0; i < 50; i++) {
        list1Arr[i] = i * 2;  // Even numbers
        list2Arr[i] = i * 2 + 1;  // Odd numbers
    }

    struct ListNode* list1 = createList(list1Arr, 50);
    struct ListNode* list2 = createList(list2Arr, 50);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[100] = {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
        38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
        56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
        74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91,
        92, 93, 94, 95, 96, 97, 98, 99
    };

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeLargeLists");
        temp = temp->next;
        i++;
    }
}

// Test Case 13: Merging two lists with random unsorted values
void testMergeListsWithRandomValues() {
    int list1Arr[] = {10, 30, 20};
    int list2Arr[] = {5, 40, 15};
    struct ListNode* list1 = createList(list1Arr, 3);
    struct ListNode* list2 = createList(list2Arr, 3);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {5, 10, 15, 20, 30, 40};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeListsWithRandomValues");
        temp = temp->next;
        i++;
    }
}

// Test Case 14: Merging two lists where one list has duplicate values
void testMergeListsWithDuplicateValuesInOneList() {
    int list1Arr[] = {1, 1, 1};
    int list2Arr[] = {2, 3, 4};
    struct ListNode* list1 = createList(list1Arr, 3);
    struct ListNode* list2 = createList(list2Arr, 3);
    const struct ListNode* result = mergeTwoLists(list1, list2);
    const int expected[] = {1, 1, 1, 2, 3, 4};

    const struct ListNode* temp = result;
    int i = 0;
    while (temp != NULL) {
        checkTestResult(temp->val == expected[i], "testMergeListsWithDuplicateValuesInOneList");
        temp = temp->next;
        i++;
    }
}

// Main test function that runs all the tests
int main() {
    testMergeTwoNonEmptyLists();
    testMergeOneEmptyList();
    testMergeTwoEmptyLists();
    testMergeSingleElementWithEmptyList();
    testMergeSingleElementLists();
    testMergeTwoListsOfSameLength();
    testMergeListsWithDuplicates();
    testMergeListsWithDifferentSizes();
    testMergeListsWithLargerElements();
    testMergeListsWithNegativeNumbers();
    testMergeListsWithEqualElements();
    testMergeLargeLists();
    testMergeListsWithRandomValues();
    testMergeListsWithDuplicateValuesInOneList();

    return 0;
}
