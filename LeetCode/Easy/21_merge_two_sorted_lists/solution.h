#ifndef SOLUTION_H
#define SOLUTION_H

struct ListNode {
  int val;
  struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2);

#endif // SOLUTION_H
