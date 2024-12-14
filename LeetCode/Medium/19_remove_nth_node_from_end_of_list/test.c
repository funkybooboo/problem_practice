#include "solution.h"
#include <stdio.h>

// Helper function to check and print the test result
void checkTestResult(const int condition, const char* testName) {
    if (condition) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\n", testName);
    }
}

// Test case for removing 2nd node from the end of [1, 2, 3, 4, 5]
void testRemoveSecondNodeFromEnd() {
    int arr[] = {1, 2, 3, 4, 5};
    struct ListNode* head = createList(arr, 5);
    head = removeNthFromEnd(head, 2);

    const int result = (
        head != NULL && head->val == 1 &&
        head->next != NULL && head->next->val == 2 &&
        head->next->next != NULL && head->next->next->val == 3 &&
        head->next->next->next != NULL && head->next->next->next->val == 5
    );

    checkTestResult(result, "Test Remove Second Node From End");
}

// Test case for removing the only node from [1]
void testRemoveOnlyNode() {
    int arr[] = {1};
    struct ListNode* head = createList(arr, 1);
    head = removeNthFromEnd(head, 1);

    const int result = (head == NULL);

    checkTestResult(result, "Test Remove Only Node");
}

// Test case for removing the last node from [1, 2]
void testRemoveLastNode() {
    int arr[] = {1, 2};
    struct ListNode* head = createList(arr, 2);
    head = removeNthFromEnd(head, 1);

    const int result = (head != NULL && head->val == 1 && head->next == NULL);

    checkTestResult(result, "Test Remove Last Node");
}

// Test case for removing the first node from [1, 2, 3]
void testRemoveFirstNode() {
    int arr[] = {1, 2, 3};
    struct ListNode* head = createList(arr, 3);
    head = removeNthFromEnd(head, 3);

    const int result = (head != NULL && head->val == 2 && head->next != NULL &&
                        head->next->val == 3);

    checkTestResult(result, "Test Remove First Node");
}

// Test case for removing a node from a list of size 3, removing the second node
void testRemoveSecondNode() {
    int arr[] = {1, 2, 3};
    struct ListNode* head = createList(arr, 3);
    head = removeNthFromEnd(head, 2);

    const int result = (head != NULL && head->val == 1 && head->next != NULL &&
                        head->next->val == 3);

    checkTestResult(result, "Test Remove Second Node");
}

int main() {
    // Run all tests
    testRemoveSecondNodeFromEnd();
    testRemoveOnlyNode();
    testRemoveLastNode();
    testRemoveFirstNode();
    testRemoveSecondNode();

    return 0;
}
