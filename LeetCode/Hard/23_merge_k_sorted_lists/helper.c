#include "helper.h"

#include <stdio.h>
#include <stdlib.h>

// Helper function to create a new ListNode
struct ListNode* newNode(const int value) {
    struct ListNode* node = malloc(sizeof(struct ListNode));
    node->val = value;
    node->next = NULL;
    return node;
}

// Helper function to build a linked list from an array
struct ListNode* buildList(const int* values, const int size) {
    if (size == 0) {
        return NULL;
    }

    struct ListNode* head = newNode(values[0]);
    struct ListNode* tail = head;
    for (int i = 1; i < size; i++) {
        tail->next = newNode(values[i]);
        tail = tail->next;
    }
    return head;
}

// Helper function to print the linked list
void printList(const struct ListNode* head) {
    while (head) {
        printf("%d", head->val);
        if (head->next) {
            printf(" -> ");
        }
        head = head->next;
    }
    printf("\n");
}
