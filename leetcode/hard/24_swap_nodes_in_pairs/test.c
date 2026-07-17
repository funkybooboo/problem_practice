#include "helper.h"
#include "solution.h"
#include <stdio.h>
#include <stdlib.h>

// Function to verify test results
void verifyTestResult(const int condition, const char* testName) {
    if (condition) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\n", testName);
    }
}

// Test 1: Testing the swap with the list [1, 2, 3, 4]
void testSwapPairs_Example1() {
    int arr[] = {1, 2, 3, 4};
    struct ListNode* head = buildList(arr, 4);
    struct ListNode* result = swapPairs(head);
    printf("Test 1 Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 2, "Test 1");
}

// Test 2: Testing an empty list []
void testSwapPairs_EmptyList() {
    struct ListNode* head = NULL;
    struct ListNode* result = swapPairs(head);
    printf("Test 2 Result: ");
    printList(result);
    verifyTestResult(result == NULL, "Test 2");
}

// Test 3: Testing a list with a single node [1]
void testSwapPairs_SingleNode() {
    int arr[] = {1};
    struct ListNode* head = buildList(arr, 1);
    struct ListNode* result = swapPairs(head);
    printf("Test 3 Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 1, "Test 3");
}

// Test 4: Testing a list with an odd number of nodes [1, 2, 3]
void testSwapPairs_OddNumberOfNodes() {
    int arr[] = {1, 2, 3};
    struct ListNode* head = buildList(arr, 3);
    struct ListNode* result = swapPairs(head);
    printf("Test 4 Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 2, "Test 4");
}

// Test 5: Testing a list with an even number of nodes [1, 2, 3, 4, 5, 6]
void testSwapPairs_EvenNumberOfNodes() {
    int arr[] = {1, 2, 3, 4, 5, 6};
    struct ListNode* head = buildList(arr, 6);
    struct ListNode* result = swapPairs(head);
    printf("Test 5 Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 2, "Test 5");
}

// Test 6: Testing a list with no nodes [ ]
void testSwapPairs_EmptyListEdge() {
    struct ListNode* head = NULL;
    struct ListNode* result = swapPairs(head);
    printf("Test 6 Result: ");
    printList(result);
    verifyTestResult(result == NULL, "Test 6");
}

// Main function to run all tests
int main() {
    testSwapPairs_Example1();
    testSwapPairs_EmptyList();
    testSwapPairs_SingleNode();
    testSwapPairs_OddNumberOfNodes();
    testSwapPairs_EvenNumberOfNodes();
    testSwapPairs_EmptyListEdge();

    return 0;
}
