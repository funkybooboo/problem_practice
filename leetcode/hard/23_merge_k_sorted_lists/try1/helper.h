#ifndef HELPER_H
#define HELPER_H

struct ListNode {
    int val;
    struct ListNode* next;
};

void printList(const struct ListNode* head);

struct ListNode* newNode(int value);

struct ListNode* buildList(const int* values, int size);

#endif
