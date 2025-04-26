#include "solution.h"
#include "helper.h"
#include <stdio.h>
#include <stdlib.h>

struct ListNode* swapPairs(struct ListNode* head) {
    // Handle the case where the list is empty or has only one node
    if (head == NULL || head->next == NULL) {
        return head;
    }

    struct ListNode* new_head = head->next;
    struct ListNode* prev = NULL;
    struct ListNode* current = head;

    // Traverse the list and swap pairs
    while (current && current->next) {
        // Perform the swap directly without extra temporary variables
        struct ListNode* next_node = current->next;
        current->next = next_node->next;
        next_node->next = current;

        // Connect the previous pair to the current one
        if (prev) {
            prev->next = next_node;
        }

        // Move the pointers to the next pair
        prev = current;
        current = current->next;
    }

    return new_head;
}
