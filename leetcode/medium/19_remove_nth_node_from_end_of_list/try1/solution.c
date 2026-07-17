#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

// Helper function to create a linked list from an array of values
struct ListNode* createList(const int* arr, const int size) {
    if (size == 0) {
        return NULL;
    }
    struct ListNode* head = malloc(sizeof(struct ListNode));
    head->val = arr[0];
    head->next = NULL;
    struct ListNode* current = head;

    for (int i = 1; i < size; i++) {
        struct ListNode* newNode = malloc(sizeof(struct ListNode));
        newNode->val = arr[i];
        newNode->next = NULL;
        current->next = newNode;
        current = newNode;
    }
    return head;
}

// Helper function to print the list
void printList(const struct ListNode* head) {
    const struct ListNode* current = head;
    while (current != NULL) {
        printf("%d", current->val);
        if (current->next != NULL) {
            printf(" -> ");
        }
        current = current->next;
    }
    printf("\n");
}

// Function to remove the Nth node from the end of the list
struct ListNode* removeNthFromEnd(struct ListNode* head, const int n) {
    if (head == NULL) {
        return NULL;
    }
    if (n < 1) {
        return head;
    }

    const struct ListNode* right = head;
    struct ListNode* left = head;

    // Move the 'right' pointer n steps ahead
    for (int i = 0; i < n; i++) {
        if (right == NULL) {
            return head; // if n is greater than the number of nodes
        }
        right = right->next;
    }

    // If right is NULL, it means we need to remove the head node
    if (right == NULL) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
        return head;
    }

    // Move both pointers until 'right' reaches the end
    while (right->next != NULL) {
        right = right->next;
        left = left->next;
    }

    // Remove the Nth node
    struct ListNode* temp = left->next;
    left->next = left->next->next;
    free(temp);

    return head;
}
