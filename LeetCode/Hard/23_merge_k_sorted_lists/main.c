#include "solution.h"
#include "helper.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to free the linked list nodes
void freeList(struct ListNode* head) {
    while (head != NULL) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
    }
}

// Helper function to convert a comma-separated string to an integer array
int* parseInput(const char* input, int* size) {
    int* result = NULL;
    int capacity = 10;
    int count = 0;

    result = (int*)malloc(capacity * sizeof(int));

    // Create a copy of input to safely use strtok (strtok modifies the string)
    char* inputCopy = strdup(input);
    const char* token = strtok(inputCopy, ",");

    while (token != NULL) {
        if (count >= capacity) {
            capacity *= 2;
            result = (int*)realloc(result, capacity * sizeof(int));
        }
        result[count++] = atoi(token);  // Convert the token to an integer and store
        token = strtok(NULL, ",");
    }

    *size = count;  // Set the size of the array
    free(inputCopy);  // Free the copy of the input string
    return result;  // Return the dynamically allocated array
}

int main(const int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: ./main <k> <list1> <list2> ...\n");
        return 1;
    }

    int k = atoi(argv[1]);  // Get the number of lists
    if (k == 0) {
        printf("No lists to merge\n");
        return 1;
    }

    // Allocate memory for the list pointers
    struct ListNode** lists = malloc(k * sizeof(struct ListNode*));

    // Parse each list from the command-line arguments
    for (int i = 0; i < k; i++) {
        int size = 0;
        int* values = parseInput(argv[i + 2], &size);  // Convert the input string to an array of integers
        lists[i] = buildList(values, size);  // Build the linked list from the array
        free(values);  // Free the temporary array after using it
    }

    // Merge the k sorted linked lists
    const struct ListNode* mergedList = mergeKLists(lists, k);

    // Print the merged list
    printList(mergedList);
    printf("\n");

    // Free the individual linked lists (the original lists)
    for (int i = 0; i < k; i++) {
        freeList(lists[i]);  // Free each original list
    }

    // Free the array holding the pointers to the linked lists
    free(lists);

    // **Do NOT free mergedList here**, as it contains nodes already freed in the original lists
    return 0;
}
