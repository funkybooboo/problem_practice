// solution.h

#ifndef SOLUTION_H
#define SOLUTION_H

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode* next;
};

// Function declarations
struct ListNode* createList(int* arr, int size);
void printList(const struct ListNode* head);
struct ListNode* removeNthFromEnd(struct ListNode* head, int n);

#endif // SOLUTION_H
