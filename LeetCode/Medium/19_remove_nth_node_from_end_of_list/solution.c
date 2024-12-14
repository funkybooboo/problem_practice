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
    const struct ListNode* first = head;
    struct ListNode* second = head;

    // Move the 'first' pointer n steps ahead
    for (int i = 0; i < n; i++) {
        if (first == NULL) {
            return head; // if n is greater than the number of nodes
        }
        first = first->next;
    }

    // If first is NULL, it means we need to remove the head node
    if (first == NULL) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
        return head;
    }

    // Move both pointers until 'first' reaches the end
    while (first->next != NULL) {
        first = first->next;
        second = second->next;
    }

    // Remove the Nth node
    struct ListNode* temp = second->next;
    second->next = second->next->next;
    free(temp);

    return head;
}
