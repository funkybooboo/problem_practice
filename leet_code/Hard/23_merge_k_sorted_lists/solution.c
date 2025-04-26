#include "solution.h"
#include "helper.h"

#include <stdio.h>
#include <stdlib.h>

// Min-Heap node definition
struct MinHeapNode {
    struct ListNode* listNode;
    int listIndex;
};

// Function to create a Min-Heap
struct MinHeap {
    struct MinHeapNode* heapArray;
    int size;
    int capacity;
};

// Function to create a MinHeap of given capacity
struct MinHeap* createMinHeap(const int capacity) {
    struct MinHeap* minHeap = malloc(sizeof(struct MinHeap));
    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->heapArray =
        (struct MinHeapNode*)malloc(capacity * sizeof(struct MinHeapNode));
    return minHeap;
}

// Function to swap two heap nodes
void swapMinHeapNode(struct MinHeapNode* a, struct MinHeapNode* b) {
    const struct MinHeapNode temp = *a;
    *a = *b;
    *b = temp;
}

// Function to min-heapify the heap
void minHeapify(struct MinHeap* minHeap, const int idx) {
    int smallest = idx;
    const int left = (2 * idx) + 1;
    const int right = (2 * idx) + 2;

    if (left < minHeap->size &&
        minHeap->heapArray[left].listNode->val <
            minHeap->heapArray[smallest].listNode->val) {
        smallest = left;
    }

    if (right < minHeap->size &&
        minHeap->heapArray[right].listNode->val <
            minHeap->heapArray[smallest].listNode->val) {
        smallest = right;
    }

    if (smallest != idx) {
        swapMinHeapNode(&minHeap->heapArray[smallest],
                        &minHeap->heapArray[idx]);
        minHeapify(minHeap, smallest);
    }
}

// Function to insert a new node into the heap
void insertMinHeap(struct MinHeap* minHeap, struct ListNode* node,
                   const int listIndex) {
    int idx = minHeap->size++;
    minHeap->heapArray[idx].listNode = node;
    minHeap->heapArray[idx].listIndex = listIndex;

    while (idx && minHeap->heapArray[idx].listNode->val <
                      minHeap->heapArray[(idx - 1) / 2].listNode->val) {
        swapMinHeapNode(&minHeap->heapArray[idx],
                        &minHeap->heapArray[(idx - 1) / 2]);
        idx = (idx - 1) / 2;
    }
}

// Function to extract the minimum node from the heap
struct ListNode* extractMin(struct MinHeap* minHeap) {
    if (minHeap->size == 0) {
        return NULL;
    }

    struct ListNode* root = minHeap->heapArray[0].listNode;
    if (minHeap->size > 1) {
        minHeap->heapArray[0] = minHeap->heapArray[minHeap->size - 1];
        minHeapify(minHeap, 0);
    }

    minHeap->size--;
    return root;
}

// Function to merge k sorted lists
struct ListNode* mergeKLists(struct ListNode** lists, const int listsSize) {
    if (listsSize == 0) {
        return NULL;
    }

    struct MinHeap* minHeap = createMinHeap(listsSize);
    for (int i = 0; i < listsSize; i++) {
        if (lists[i]) {
            insertMinHeap(minHeap, lists[i], i);
        }
    }

    struct ListNode* head = NULL;
    struct ListNode* tail = NULL;

    while (minHeap->size > 0) {
        struct ListNode* minNode = extractMin(minHeap);
        if (!head) {
            head = minNode;
            tail = head;
        } else {
            tail->next = minNode;
            tail = tail->next;
        }

        if (minNode->next) {
            insertMinHeap(minHeap, minNode->next, minNode->next->val);
        }
    }

    // We don't need to free the merged nodes here; they are part of the original lists.
    free(minHeap->heapArray);
    free(minHeap);

    return head;
}
