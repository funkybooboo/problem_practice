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

// Test 1: Testing the reverse with the list [1, 2, 3, 4] and k = 2
void testReverseKGroup_k2() {
    int arr[] = {1, 2, 3, 4};
    struct ListNode* head = buildList(arr, 4);
    struct ListNode* result = reverseKGroup(head, 2);
    printf("Test 1 (k=2) Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 2, "Test 1 (k=2)");
}

// Test 2: Testing the reverse with the list [1, 2, 3, 4] and k = 3
void testReverseKGroup_k3() {
    int arr[] = {1, 2, 3, 4};
    struct ListNode* head = buildList(arr, 4);
    struct ListNode* result = reverseKGroup(head, 3);
    printf("Test 2 (k=3) Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 3, "Test 2 (k=3)");
}

// Test 3: Testing the reverse with the list [1, 2, 3, 4, 5] and k = 2
void testReverseKGroup_k2_multiple_nodes() {
    int arr[] = {1, 2, 3, 4, 5};
    struct ListNode* head = buildList(arr, 5);
    struct ListNode* result = reverseKGroup(head, 2);
    printf("Test 3 (k=2, multiple nodes) Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 2, "Test 3 (k=2, multiple nodes)");
}

// Test 4: Testing the reverse with the list [1, 2, 3, 4, 5] and k = 3
void testReverseKGroup_k3_multiple_nodes() {
    int arr[] = {1, 2, 3, 4, 5};
    struct ListNode* head = buildList(arr, 5);
    struct ListNode* result = reverseKGroup(head, 3);
    printf("Test 4 (k=3, multiple nodes) Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 3, "Test 4 (k=3, multiple nodes)");
}

// Test 5: Testing the reverse with an even number of nodes [1, 2, 3, 4, 5, 6] and k = 3
void testReverseKGroup_k3_even_nodes() {
    int arr[] = {1, 2, 3, 4, 5, 6};
    struct ListNode* head = buildList(arr, 6);
    struct ListNode* result = reverseKGroup(head, 3);
    printf("Test 5 (k=3, even nodes) Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 3, "Test 5 (k=3, even nodes)");
}

// Test 6: Testing the reverse with an odd number of nodes [1, 2, 3, 4, 5] and k = 4
void testReverseKGroup_k4_odd_nodes() {
    int arr[] = {1, 2, 3, 4, 5};
    struct ListNode* head = buildList(arr, 5);
    struct ListNode* result = reverseKGroup(head, 4);
    printf("Test 6 (k=4, odd nodes) Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 4, "Test 6 (k=4, odd nodes)");
}

// Test 7: Testing the reverse with an odd number of nodes [1, 2, 3, 4, 5] and k = 2
void testReverseKGroup_k2_odd_nodes() {
    int arr[] = {1, 2, 3, 4, 5};
    struct ListNode* head = buildList(arr, 5);
    struct ListNode* result = reverseKGroup(head, 2);
    printf("Test 7 (k=2, odd nodes) Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 2, "Test 7 (k=2, odd nodes)");
}

// Test 8: Testing with an empty list [] and k = 2
void testReverseKGroup_EmptyList_k2() {
    struct ListNode* head = NULL;
    struct ListNode* result = reverseKGroup(head, 2);
    printf("Test 8 (empty list) Result: ");
    printList(result);
    verifyTestResult(result == NULL, "Test 8 (empty list)");
}

// Test 9: Testing with a single node [1] and k = 1
void testReverseKGroup_k1_single_node() {
    int arr[] = {1};
    struct ListNode* head = buildList(arr, 1);
    struct ListNode* result = reverseKGroup(head, 1);
    printf("Test 9 (k=1, single node) Result: ");
    printList(result);
    verifyTestResult(result != NULL && result->val == 1, "Test 9 (k=1, single node)");
}

// Main function to run all tests
int main() {
    testReverseKGroup_k2();
    testReverseKGroup_k3();
    testReverseKGroup_k2_multiple_nodes();
    testReverseKGroup_k3_multiple_nodes();
    testReverseKGroup_k3_even_nodes();
    testReverseKGroup_k4_odd_nodes();
    testReverseKGroup_k2_odd_nodes();
    testReverseKGroup_EmptyList_k2();
    testReverseKGroup_k1_single_node();

    return 0;
}
