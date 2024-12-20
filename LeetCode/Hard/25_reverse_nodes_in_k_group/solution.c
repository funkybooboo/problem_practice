#include "helper.h"
#include <stdio.h>
#include <stdlib.h>

// Function to reverse k nodes
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    // If the list is empty or has less than k nodes, return as is
    const struct ListNode* temp = head;
    for (int i = 0; i < k; i++) {
        if (temp == NULL) {
            return head;  // Not enough nodes to reverse
        }
        temp = temp->next;
    }

    // Reverse the first k nodes
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    struct ListNode* next = NULL;
    for (int i = 0; i < k; i++) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    // After reversing, `head` becomes the new tail of the group
    if (head != NULL) {
        head->next = reverseKGroup(curr, k);  // Recursively reverse the rest of the list
    }

    // `prev` is now the head of the reversed k-group
    return prev;
}
