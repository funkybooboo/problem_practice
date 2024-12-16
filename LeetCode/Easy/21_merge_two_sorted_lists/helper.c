#include <stdio.h>
#include <stdlib.h>
#include "solution.h"

// Helper function to create a linked list from an array of integers
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

// Print the created list
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
