#include <stdio.h>
#include <stdlib.h>
#include "solution.h"

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode head;
    struct ListNode* tail = &head;
    head.next = NULL;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // Append the remaining part of the non-null list
    if (list1 != NULL) {
        tail->next = list1;
    } else {
        tail->next = list2;
    }

    return head.next;
}
